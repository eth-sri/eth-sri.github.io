#!/usr/bin/env python3
"""Migrate project websites into project-sites/<name>/ and check them.

A project site is a standalone static website (its own HTML/CSS/JS, no SRI
header) that GitHub Pages serves verbatim at
https://www.sri.inf.ethz.ch/project-sites/<name>/.
Full guide, including how to fix every check error: project-sites/README.md

examples:
  # preview a migration without writing anything
  python3 script/project_sites.py migrate eth-sri/baxbench-website baxbench --dry-run

  # migrate a GitHub repo (the old domain is read from its CNAME file)
  python3 script/project_sites.py migrate eth-sri/baxbench-website baxbench --prune-unreferenced

  # validate a site after editing it, or a new site created by hand
  python3 script/project_sites.py check baxbench

exit codes: 0 = ok (warnings allowed), 1 = check errors, 2 = usage error
"""

import argparse
import fnmatch
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import quote

SITE_URL = "https://www.sri.inf.ethz.ch"
SITES_DIR = "project-sites"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_BYTES = 5_000_000  # larger files belong on files.sri.inf.ethz.ch
WARN_BYTES = 1_000_000

# Repository plumbing that is not part of a site and is never copied.
SKIP_AT_ROOT = {".git", ".github", "CNAME", ".nojekyll", ".gitignore"}
SKIP_ANYWHERE = {".DS_Store"}

# Files scanned for references (unreferenced check) and rewritten (old domain).
REF_EXTS = {".html", ".htm", ".css", ".js", ".json"}
SITE_TEXT_EXTS = REF_EXTS | {".xml", ".txt", ".svg", ".webmanifest"}
MAIN_TEXT_EXTS = {".html", ".md", ".markdown", ".yml", ".yaml"}
MAIN_DIRS = ["_publications", "_projects", "_newsposts", "_blogposts",
             "_includes", "_layouts", "_data", "_people"]

FRONT_MATTER_RE = re.compile(rb"\A---[ \t]*\r?\n")
ROOT_ABS_ATTR_RE = re.compile(r"""\b(src|href|action|poster|srcset)\s*=\s*["']/(?!/)([^"']*)["']""", re.I)
ROOT_ABS_CSS_RE = re.compile(r"""url\(\s*["']?/(?!/)[^)]*\)""", re.I)


class UsageError(Exception):
    """Bad arguments or a failed precondition (exit code 2)."""


class Report:
    """Findings and actions of one run, printed as text or JSON."""

    def __init__(self, command, name):
        self.command = command
        self.name = name
        self.errors = []
        self.warnings = []
        self.extra = {}  # migrate-only fields

    def error(self, code, path, detail):
        self.errors.append({"code": code, "path": path, "detail": detail})

    def warn(self, code, path, detail):
        self.warnings.append({"code": code, "path": path, "detail": detail})

    @property
    def ok(self):
        return not self.errors

    def as_dict(self):
        return {"command": self.command, "name": self.name, "ok": self.ok, **self.extra,
                "errors": self.errors, "warnings": self.warnings}


def repo_root():
    """Top level of the git repository containing the current directory."""
    try:
        proc = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                              capture_output=True, text=True, check=True)
    except (OSError, subprocess.CalledProcessError):
        raise UsageError("run this inside a clone of eth-sri.github.io")
    root = Path(proc.stdout.strip())
    if not (root / "_config.yml").is_file():
        raise UsageError(f"{root} has no _config.yml; run this inside a clone of eth-sri.github.io")
    return root


def validate_name(name):
    if not NAME_RE.match(name):
        raise UsageError(f"invalid site name {name!r}: use lowercase letters, digits and single "
                         "hyphens, e.g. 'baxbench' or 'llm-quantization-attack'")


def read_lossy(path):
    return path.read_bytes().decode("utf-8", errors="replace")


def site_files(site_dir):
    return sorted(p for p in site_dir.rglob("*") if p.is_file())


def jekyll_excludes(root):
    """The `exclude:` entries of _config.yml (block or inline list, parsed without PyYAML)."""
    lines = (root / "_config.yml").read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        match = re.match(r"^exclude:\s*(.*)$", line)
        if not match:
            continue
        inline = match.group(1).split(" #")[0].strip()
        if inline.startswith("["):
            return [item.strip().strip("'\"") for item in inline.strip("[]").split(",") if item.strip()]
        entries = []
        for item in lines[i + 1:]:
            if not item.strip() or item.lstrip().startswith("#"):
                continue
            match = re.match(r"^\s+-\s+(.*)$", item)
            if not match:
                break
            entries.append(match.group(1).split(" #")[0].strip().strip("'\""))
        return entries
    return []


def jekyll_skips(rel_path, excludes):
    """Whether Jekyll 3 leaves rel_path (relative to the repo root) out of the built site."""
    if any(seg[:1] in ("_", ".", "#") or seg.endswith("~") for seg in rel_path.split("/")):
        return True
    return any(rel_path == pattern.rstrip("/") or rel_path.startswith(pattern)
               or fnmatch.fnmatchcase(rel_path, pattern) for pattern in excludes)


def git_ignored(root, rel_paths):
    """The subset of rel_paths that the repository's .gitignore rules ignore."""
    if not rel_paths:
        return set()
    proc = subprocess.run(["git", "check-ignore", "-z", "--stdin"], cwd=root,
                          input="\0".join(rel_paths) + "\0", capture_output=True, text=True)
    if proc.returncode not in (0, 1):
        raise UsageError(f"git check-ignore failed: {proc.stderr.strip()}")
    return set(filter(None, proc.stdout.split("\0")))


def root_absolute_paths(text):
    """References starting with a single '/', which break below the domain root."""
    found = [f'{m.group(1)}="/{m.group(2)}"' for m in ROOT_ABS_ATTR_RE.finditer(text)
             if not (m.group(1).lower() == "href" and m.group(2) == "")]  # href="/" = main site
    return found + [m.group(0) for m in ROOT_ABS_CSS_RE.finditer(text)]


def unreferenced_files(site_dir):
    """Files whose name appears in no HTML/CSS/JS/JSON file of the site (index.html exempt)."""
    files = site_files(site_dir)
    corpus = "\n".join(read_lossy(f) for f in files if f.suffix.lower() in REF_EXTS)
    return [f for f in files
            if f.name != "index.html" and f.name not in corpus and quote(f.name) not in corpus]


def check_site(root, site_dir, name, allow_large, report):
    """Report every rule violation of the site in site_dir, served as project-sites/<name>/."""
    prefix = f"{SITES_DIR}/{name}"
    files = site_files(site_dir)
    rel = {f: f"{prefix}/{f.relative_to(site_dir).as_posix()}" for f in files}
    excludes = jekyll_excludes(root)
    ignored = git_ignored(root, list(rel.values()))

    if not (site_dir / "index.html").is_file():
        report.error("no-index", f"{prefix}/", "add an index.html at the site root")
    for f in files:
        path, ext, size = rel[f], f.suffix.lower(), f.stat().st_size
        if jekyll_skips(path, excludes):
            report.error("jekyll-skipped", path, "Jekyll leaves out names starting with _ . # or "
                         "ending in ~, and paths in the exclude list of _config.yml; rename it")
        if path in ignored:
            report.error("git-ignored", path, "the repo's .gitignore ignores it, so it would never be committed")
        if ext == ".pdf":
            report.error("pdf", path, "host it on files.sri.inf.ethz.ch (or arXiv) and link to that URL")
        if ext in (".md", ".markdown"):
            report.error("markdown", path, "GitHub Pages would render it as a page; convert it to HTML or delete it")
        with f.open("rb") as handle:
            if FRONT_MATTER_RE.match(handle.read(64)):
                report.error("front-matter", path, "remove the leading --- block; site files must be served verbatim")
        if ext in (".html", ".htm", ".css"):
            for ref in root_absolute_paths(read_lossy(f)):
                report.error("root-absolute-path", path, f"{ref}: make it relative (no leading /)")
        if size > MAX_BYTES and not allow_large:
            report.error("too-large", path, f"{size / 1e6:.1f} MB > 5 MB; host it on files.sri.inf.ethz.ch")
        elif size > WARN_BYTES:
            report.warn("large", path, f"{size / 1e6:.1f} MB")
    for f in unreferenced_files(site_dir):
        report.warn("unreferenced", rel[f], "nothing in the site mentions it; delete it if unused")


def normalize_domain(value):
    """'https://www.Example.org/' -> 'example.org'."""
    domain = re.sub(r"^[a-z]+://", "", value.strip().lower()).split("/")[0]
    return domain[4:] if domain.startswith("www.") else domain


def fetch_source(source, clone_dir):
    """A local directory, or a fresh shallow clone of the GitHub repo owner/repo."""
    local = Path(source).expanduser()
    if local.is_dir():
        return local.resolve()
    if re.fullmatch(r"[\w.-]+/[\w.-]+", source):
        url = f"https://github.com/{source}.git"
        proc = subprocess.run(["git", "clone", "--quiet", "--depth", "1", url, str(clone_dir)],
                              capture_output=True, text=True,
                              env={**os.environ, "GIT_TERMINAL_PROMPT": "0"})
        if proc.returncode != 0:
            raise UsageError(f"could not clone {url}: {proc.stderr.strip()}")
        return clone_dir
    raise UsageError(f"source {source!r} is neither a local directory nor a GitHub owner/repo")


def read_cname(source):
    cname = source / "CNAME"
    words = cname.read_text(encoding="utf-8", errors="replace").split() if cname.is_file() else []
    return normalize_domain(words[0]) if words else None


def files_to_copy(source):
    """Paths (relative to source) of all site files, skipping repository plumbing."""
    found = []
    for dirpath, dirnames, filenames in os.walk(source):
        rel_dir = Path(dirpath).relative_to(source)
        if rel_dir == Path("."):
            dirnames[:] = [d for d in dirnames if d not in SKIP_AT_ROOT]
            filenames = [f for f in filenames
                         if f not in SKIP_AT_ROOT and not f.upper().startswith("README")]
        dirnames.sort()
        found += [rel_dir / f for f in sorted(filenames) if f not in SKIP_ANYWHERE]
    return found


def domain_pattern(domain):
    """Matches http(s)://[www.]<domain> plus an optional path, query or fragment."""
    return re.compile(r"https?://(?:www\.)?" + re.escape(domain)
                      + r"(?!\.?[A-Za-z0-9-])(?P<rest>[/?#][^\s\"'<>()]*)?", re.I)


def rewrite_file(path, pattern, new_url, write):
    """Point links to the old domain at new_url; returns the number of replacements."""
    try:
        text = path.read_bytes().decode("utf-8")
    except UnicodeDecodeError:
        return 0  # not UTF-8 text: leave it untouched

    def replace(match):
        rest = match.group("rest") or ""
        return new_url + (rest[1:] if rest.startswith("/") else rest)

    new_text, count = pattern.subn(replace, text)
    if count and write:
        path.write_bytes(new_text.encode("utf-8"))
    return count


def main_site_files(root, name):
    """Main-site sources and other project sites that may link to the old domain."""
    for directory in MAIN_DIRS:
        if (root / directory).is_dir():
            yield from (p for p in sorted((root / directory).rglob("*"))
                        if p.is_file() and p.suffix.lower() in MAIN_TEXT_EXTS)
    yield from (p for p in sorted(root.glob("*")) if p.is_file() and p.suffix.lower() in (".html", ".md"))
    sites = root / SITES_DIR
    if sites.is_dir():
        yield from (p for p in sorted(sites.rglob("*"))
                    if p.is_file() and p.suffix.lower() in SITE_TEXT_EXTS
                    and p.relative_to(sites).parts[0] != name)


def remove_empty_dirs(top):
    for dirpath, _, _ in os.walk(top, topdown=False):
        if Path(dirpath) != top and not os.listdir(dirpath):
            os.rmdir(dirpath)


def migrate(args, root, report):
    """Stage the source site, prune, rewrite, check, then write it and rewrite main-site links."""
    validate_name(args.name)
    prefix = f"{SITES_DIR}/{args.name}"
    target = root / prefix
    if target.exists():
        raise UsageError(f"{prefix}/ already exists; choose another name or delete it first")
    new_url = f"{SITE_URL}/{prefix}/"
    with tempfile.TemporaryDirectory() as tmp:
        source = fetch_source(args.source, Path(tmp) / "clone")
        domain = normalize_domain(args.domain) if args.domain else read_cname(source)
        x = report.extra = {"source": args.source, "domain": domain, "url": new_url,
                            "dry_run": args.dry_run, "copied_files": [], "pruned_files": [],
                            "changed_files": []}

        staging = Path(tmp) / "site"
        staging.mkdir()
        for rel in files_to_copy(source):
            (staging / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source / rel, staging / rel)
            x["copied_files"].append(f"{prefix}/{rel.as_posix()}")

        if args.prune_unreferenced:
            for f in unreferenced_files(staging):
                x["pruned_files"].append(f"{prefix}/{f.relative_to(staging).as_posix()}")
                f.unlink()
            remove_empty_dirs(staging)

        if domain:
            pattern = domain_pattern(domain)
            for f in site_files(staging):
                if f.suffix.lower() in SITE_TEXT_EXTS:
                    count = rewrite_file(f, pattern, new_url, write=True)
                    if count:
                        x["changed_files"].append({"path": f"{prefix}/{f.relative_to(staging).as_posix()}",
                                                   "replacements": count})
        else:
            report.warn("no-domain", f"{prefix}/", "no CNAME in the source and no --domain given: "
                        "links to the old domain were not rewritten")

        check_site(root, staging, args.name, args.allow_large, report)
        if not args.dry_run:
            shutil.copytree(staging, target)
        if domain:
            for f in main_site_files(root, args.name):
                count = rewrite_file(f, pattern, new_url, write=not args.dry_run)
                if count:
                    x["changed_files"].append({"path": f.relative_to(root).as_posix(), "replacements": count})


def render(report):
    """Human-readable report."""
    lines = []
    x = report.extra
    if report.command == "migrate":
        lines.append(f"{'[dry run: nothing written] ' if x['dry_run'] else ''}Migrating {x['source']} "
                     f"-> {SITES_DIR}/{report.name}/ (old domain: {x['domain'] or 'unknown'})")
        lines.append(f"Copied {len(x['copied_files'])} files.")
        if x["pruned_files"]:
            lines.append(f"Pruned {len(x['pruned_files'])} unreferenced files:")
            lines += [f"  {p}" for p in x["pruned_files"]]
        if x["changed_files"]:
            lines.append(f"Rewrote links to {x['domain']} -> {x['url']} in {len(x['changed_files'])} files:")
            lines += [f"  {c['path']} ({c['replacements']})" for c in x["changed_files"]]
    for title, items in (("Errors", report.errors), ("Warnings", report.warnings)):
        if items:
            lines.append(f"{title} ({len(items)}):")
            lines += [f"  [{i['code']}] {i['path']}: {i['detail']}" for i in items]
    if not report.ok:
        written = report.command == "migrate" and not x["dry_run"]
        lines.append(f"FAILED: {len(report.errors)} error(s). How to fix each code: {SITES_DIR}/README.md"
                     + (f"\nThe files were written; fix the errors, then re-run: "
                        f"python3 script/project_sites.py check {report.name}" if written else ""))
    elif report.command == "check":
        lines.append("OK: no errors.")
    elif x["dry_run"]:
        lines.append("OK: no errors. Run again without --dry-run to write the files.")
    else:
        lines.append(f"OK: review `git status` and `git diff`, then commit. Once merged into master "
                     f"the site is served at {x['url']}")
    return "\n".join(lines)


def build_parser():
    parser = argparse.ArgumentParser(prog="python3 script/project_sites.py", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    migrate_cmd = commands.add_parser(
        "migrate", help="copy an existing website into project-sites/<name>/",
        description="Copy a website into project-sites/<name>/, rewrite links to its old domain "
                    "(in the site, the main site and other project sites), then run check.")
    migrate_cmd.add_argument("source", help="GitHub owner/repo (e.g. eth-sri/baxbench-website) or a local directory")
    migrate_cmd.add_argument("name", help="folder under project-sites/, e.g. baxbench")
    migrate_cmd.add_argument("--domain", help="old domain whose links are rewritten (default: the source's CNAME)")
    migrate_cmd.add_argument("--prune-unreferenced", action="store_true",
                             help="delete files nothing in the site mentions (review the printed list)")
    migrate_cmd.add_argument("--dry-run", action="store_true", help="report everything, write nothing")
    check_cmd = commands.add_parser("check", help="validate project-sites/<name>/",
                                    description="Validate project-sites/<name>/ against the project-site rules.")
    check_cmd.add_argument("name", help="folder under project-sites/, e.g. baxbench")
    for cmd in (migrate_cmd, check_cmd):
        cmd.add_argument("--allow-large", action="store_true", help="allow files over 5 MB (warn instead)")
        cmd.add_argument("--json", action="store_true", help="print one JSON object (for scripts and agents)")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    report = Report(args.command, args.name)
    try:
        root = repo_root()
        if args.command == "migrate":
            migrate(args, root, report)
        else:
            validate_name(args.name)
            site_dir = root / SITES_DIR / args.name
            if not site_dir.is_dir():
                raise UsageError(f"{SITES_DIR}/{args.name}/ does not exist")
            check_site(root, site_dir, args.name, args.allow_large, report)
    except UsageError as err:
        if args.json:
            print(json.dumps({"command": args.command, "name": args.name, "ok": False, "usage_error": str(err)}))
        else:
            print(f"error: {err}", file=sys.stderr)
        return 2
    print(json.dumps(report.as_dict(), indent=2) if args.json else render(report))
    return 0 if report.ok else 1


if __name__ == "__main__":
    sys.exit(main())
