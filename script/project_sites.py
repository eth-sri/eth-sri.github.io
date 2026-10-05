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
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote

SITE_URL = "https://www.sri.inf.ethz.ch"
SITES_DIR = "project-sites"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_BYTES = 5_000_000  # larger files belong on files.sri.inf.ethz.ch
WARN_BYTES = 1_000_000

# Files scanned for references to other files (the unreferenced check).
REF_EXTS = {".html", ".htm", ".css", ".js", ".json"}

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


def render(report):
    """Human-readable report."""
    lines = []
    for title, items in (("Errors", report.errors), ("Warnings", report.warnings)):
        if items:
            lines.append(f"{title} ({len(items)}):")
            lines += [f"  [{i['code']}] {i['path']}: {i['detail']}" for i in items]
    if not report.ok:
        lines.append(f"FAILED: {len(report.errors)} error(s). How to fix each code: {SITES_DIR}/README.md")
    else:
        lines.append("OK: no errors.")
    return "\n".join(lines)


def build_parser():
    parser = argparse.ArgumentParser(prog="python3 script/project_sites.py", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    check_cmd = commands.add_parser("check", help="validate project-sites/<name>/",
                                    description="Validate project-sites/<name>/ against the project-site rules.")
    check_cmd.add_argument("name", help="folder under project-sites/, e.g. baxbench")
    check_cmd.add_argument("--allow-large", action="store_true", help="allow files over 5 MB (warn instead)")
    check_cmd.add_argument("--json", action="store_true", help="print one JSON object (for scripts and agents)")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    report = Report(args.command, args.name)
    try:
        root = repo_root()
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
