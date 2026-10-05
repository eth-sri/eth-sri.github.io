# Project Sites Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Serve standalone project websites verbatim under `https://www.sri.inf.ethz.ch/project-sites/<name>/`, with a script that migrates and validates them, docs that people and agents can find, and a pilot migration of llm-quantization-attack.org.

**Architecture:** Site files live in `project-sites/<name>/` without front matter, so Jekyll (GitHub Pages) copies them verbatim. `script/project_sites.py` (Python 3 standard library plus the git CLI) has two subcommands. `check` validates a folder against the rules. `migrate` stages a copy of a source site in a temp dir, optionally prunes unreferenced files, rewrites old-domain links, runs `check`, then writes the site and rewrites old-domain links across the main site. `AGENTS.md`/`CLAUDE.md`/`project-sites/README.md` make the process discoverable, and `_config.yml` excludes them from the build.

**Tech Stack:** Python 3.10 (stdlib: argparse, pathlib, re, fnmatch, shutil, subprocess, tempfile, unittest), git, Jekyll 3.10 via the `github-pages` gem.

**Spec:** `docs/superpowers/specs/2026-10-05-project-sites-design.md`

## Global Constraints

- Python standard library plus the `git` CLI only. No PyYAML or other packages.
- Public URL: `https://www.sri.inf.ethz.ch/project-sites/<name>/`. Folder: `project-sites/<name>/`.
- Site name must match `^[a-z0-9]+(-[a-z0-9]+)*$`.
- `too-large` error above 5 MB (`5_000_000` bytes); `large` warning above 1 MB (`1_000_000` bytes).
- Exit codes: `0` ok (warnings allowed), `1` check errors, `2` usage error or failed precondition.
- Project-site files are served verbatim. Never add front matter, layouts, or a shared header to them.
- No redirects from old domains. The script never touches old repositories.
- Do not push to `master` or to other repositories, and do not archive repositories. Work stays on branch `project-sites`.

## Review Focus

1. Text-extension files that are not UTF-8 (for example a Latin-1 `.txt`) must be copied byte for byte, and the domain rewrite must skip them without crashing. Test: Task 2 `test_non_utf8_and_binary_files_are_copied_byte_for_byte`.
2. Lookalike domains (`notdemo.org`, `demo.org.cn`, `demo.organic`, `sub.demo.org`) must not be rewritten. A sentence-final `https://demo.org.` must be rewritten with its period kept. Test: Task 2 `test_leaves_lookalike_domains_alone`.
3. Agents often run commands from a subdirectory. Both subcommands must find the repo root via git. Tests: Task 1 and Task 2 `test_runs_from_a_subdirectory`.
4. CRLF line endings and binary files must survive the copy and rewrite unchanged, apart from the rewritten URLs. Test: Task 2 `test_non_utf8_and_binary_files_are_copied_byte_for_byte`.
5. A `CNAME` with a `www.` prefix or trailing newline, and `--domain` given as a full URL, must normalize to the bare domain. Tests: Task 2 `test_cname_with_www_prefix`, `test_domain_flag_overrides_cname`.

---

### Task 1: `check` subcommand

**Files:**
- Create: `script/project_sites.py`
- Test: `script/test_project_sites.py`

**Interfaces:**
- Produces (used by Task 2):
  - `SITE_URL`, `SITES_DIR`, `MAX_BYTES`, `WARN_BYTES`, `REF_EXTS` constants
  - `class UsageError(Exception)`
  - `class Report(command: str, name: str)` with `.error(code, path, detail)`, `.warn(code, path, detail)`, `.ok`, `.extra: dict`, `.as_dict() -> dict`
  - `repo_root() -> Path`, `validate_name(name: str) -> None`, `read_lossy(path: Path) -> str`, `site_files(site_dir: Path) -> list[Path]`
  - `unreferenced_files(site_dir: Path) -> list[Path]`
  - `check_site(root: Path, site_dir: Path, name: str, allow_large: bool, report: Report) -> None`
  - `render(report: Report) -> str`
- Test harness (used by Task 2 tests): `Fixture(tmp)` with `.root`, `.tmp`, `.write(rel, content, base=None) -> Path`, `.run(*args, cwd=None)`, `.run_json(*args, cwd=None) -> (int, dict)`, `.snapshot() -> dict`; helper `findings(out, kind) -> set[tuple[str, str]]`.

- [ ] **Step 1: Write the failing tests**

Create `script/test_project_sites.py`:

```python
#!/usr/bin/env python3
"""Tests for script/project_sites.py.

Run from the repo root: python3 -m unittest script/test_project_sites.py -v
"""

import json
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "project_sites.py"
NEW = "https://www.sri.inf.ethz.ch/project-sites/demo/"

CONFIG = textwrap.dedent("""\
    title: Test site
    exclude:
      - Gemfile
      - "*.bak"   # backups
      - project-sites/README.md
    plugins:
      - jekyll-feed
""")


class Fixture:
    """A throwaway stand-in for the repo: a git repo with _config.yml and .gitignore."""

    def __init__(self, tmp):
        self.tmp = Path(tmp)
        self.root = self.tmp / "repo"
        self.root.mkdir()
        (self.root / "_config.yml").write_text(CONFIG, encoding="utf-8")
        (self.root / ".gitignore").write_text("*.pdf\n*.log\n_site\n", encoding="utf-8")
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)

    def write(self, rel, content, base=None):
        path = (base or self.root) / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(content, bytes):
            path.write_bytes(content)
        else:
            path.write_text(content, encoding="utf-8")
        return path

    def run(self, *args, cwd=None):
        return subprocess.run([sys.executable, str(SCRIPT), *args],
                              cwd=cwd or self.root, capture_output=True, text=True)

    def run_json(self, *args, cwd=None):
        proc = self.run(*args, "--json", cwd=cwd)
        return proc.returncode, json.loads(proc.stdout)

    def snapshot(self):
        return {p.relative_to(self.root).as_posix(): p.read_bytes()
                for p in sorted(self.root.rglob("*"))
                if p.is_file() and ".git" not in p.relative_to(self.root).parts}


def findings(out, kind):
    return {(f["code"], f["path"]) for f in out[kind]}


class CheckTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.fx = Fixture(self._tmp.name)
        self.fx.write("project-sites/demo/index.html",
                      '<link rel="stylesheet" href="static/site.css"><a href="/">SRI Lab</a>')
        self.fx.write("project-sites/demo/static/site.css", "body { color: black; }")

    def tearDown(self):
        self._tmp.cleanup()

    def assertError(self, out, code, path):
        self.assertIn((code, path), findings(out, "errors"))

    def test_clean_site_passes(self):
        code, out = self.fx.run_json("check", "demo")
        self.assertEqual(code, 0)
        self.assertEqual((out["ok"], out["errors"], out["warnings"]), (True, [], []))

    def test_front_matter_is_an_error(self):
        self.fx.write("project-sites/demo/page.html", "---\ntitle: x\n---\n<p>hi</p>")
        code, out = self.fx.run_json("check", "demo")
        self.assertEqual(code, 1)
        self.assertFalse(out["ok"])
        self.assertError(out, "front-matter", "project-sites/demo/page.html")

    def test_markdown_is_an_error(self):
        self.fx.write("project-sites/demo/notes.md", "# notes")
        code, out = self.fx.run_json("check", "demo")
        self.assertEqual(code, 1)
        self.assertError(out, "markdown", "project-sites/demo/notes.md")

    def test_paths_jekyll_skips_are_errors(self):
        skipped = ["_next/app.js", ".well-known/x.txt", "#draft.html", "old.html~", "copy.bak"]
        for rel in skipped:
            self.fx.write(f"project-sites/demo/{rel}", "x")
        code, out = self.fx.run_json("check", "demo")
        self.assertEqual(code, 1)
        for rel in skipped:
            self.assertError(out, "jekyll-skipped", f"project-sites/demo/{rel}")

    def test_git_ignored_and_pdf_are_errors(self):
        self.fx.write("project-sites/demo/paper.pdf", b"%PDF-1.4")
        self.fx.write("project-sites/demo/debug.log", "x")
        code, out = self.fx.run_json("check", "demo")
        self.assertEqual(code, 1)
        self.assertError(out, "pdf", "project-sites/demo/paper.pdf")
        self.assertError(out, "git-ignored", "project-sites/demo/paper.pdf")
        self.assertError(out, "git-ignored", "project-sites/demo/debug.log")

    def test_root_absolute_paths_are_errors(self):
        self.fx.write("project-sites/demo/index.html",
                      '<link rel="stylesheet" href="static/site.css"><a href="/">SRI Lab</a>'
                      '<img src="/static/logo.png"><script src="//cdn.example.com/x.js"></script>')
        self.fx.write("project-sites/demo/static/site.css", "body { background: url('/img/bg.png'); }")
        code, out = self.fx.run_json("check", "demo")
        self.assertEqual(code, 1)
        paths = sorted(f["path"] for f in out["errors"] if f["code"] == "root-absolute-path")
        self.assertEqual(paths, ["project-sites/demo/index.html", "project-sites/demo/static/site.css"])

    def test_size_limits(self):
        self.fx.write("project-sites/demo/index.html",
                      '<link rel="stylesheet" href="static/site.css">'
                      '<a href="static/big.bin">a</a><a href="static/mid.bin">b</a>')
        self.fx.write("project-sites/demo/static/big.bin", b"0" * 5_000_001)
        self.fx.write("project-sites/demo/static/mid.bin", b"0" * 1_000_001)
        code, out = self.fx.run_json("check", "demo")
        self.assertEqual(code, 1)
        self.assertError(out, "too-large", "project-sites/demo/static/big.bin")
        self.assertIn(("large", "project-sites/demo/static/mid.bin"), findings(out, "warnings"))
        code, out = self.fx.run_json("check", "demo", "--allow-large")
        self.assertEqual(code, 0)
        self.assertIn(("large", "project-sites/demo/static/big.bin"), findings(out, "warnings"))

    def test_unreferenced_files_are_warnings(self):
        self.fx.write("project-sites/demo/index.html",
                      '<link rel="stylesheet" href="static/site.css"><img src="static/my%20pic.png">')
        self.fx.write("project-sites/demo/static/my pic.png", b"png")
        self.fx.write("project-sites/demo/static/unused.png", b"png")
        self.fx.write("project-sites/demo/sub/index.html", "<p>sub page</p>")
        code, out = self.fx.run_json("check", "demo")
        self.assertEqual(code, 0)
        self.assertEqual(findings(out, "warnings"), {("unreferenced", "project-sites/demo/static/unused.png")})

    def test_missing_index_is_an_error(self):
        (self.fx.root / "project-sites/demo/index.html").unlink()
        code, out = self.fx.run_json("check", "demo")
        self.assertEqual(code, 1)
        self.assertError(out, "no-index", "project-sites/demo/")

    def test_usage_errors_exit_2(self):
        self.assertEqual(self.fx.run("check", "Bad_Name").returncode, 2)
        code, out = self.fx.run_json("check", "missing")
        self.assertEqual(code, 2)
        self.assertFalse(out["ok"])
        self.assertIn("does not exist", out["usage_error"])

    def test_runs_from_a_subdirectory(self):
        code, out = self.fx.run_json("check", "demo", cwd=self.fx.root / "project-sites")
        self.assertEqual(code, 0, out)

    def test_human_output_names_code_and_path(self):
        self.fx.write("project-sites/demo/notes.md", "# notes")
        proc = self.fx.run("check", "demo")
        self.assertEqual(proc.returncode, 1)
        self.assertIn("[markdown] project-sites/demo/notes.md", proc.stdout)
        self.assertIn("project-sites/README.md", proc.stdout)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python3 -m unittest script/test_project_sites.py -v`
Expected: every test FAILS or ERRORS (`can't open file '.../project_sites.py'`, then JSON decode errors).

- [ ] **Step 3: Write the implementation**

Create `script/project_sites.py`:

```python
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
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python3 -m unittest script/test_project_sites.py -v`
Expected: all 12 `CheckTests` PASS.

- [ ] **Step 5: Commit**

```bash
chmod +x script/project_sites.py
git add script/project_sites.py script/test_project_sites.py
git commit -m "Add project-sites check script"
```

---

### Task 2: `migrate` subcommand

**Files:**
- Modify: `script/project_sites.py` (imports, constants, new functions, `render`, `build_parser`, `main`)
- Test: `script/test_project_sites.py` (append `MigrateTests`)

**Interfaces:**
- Consumes: everything Task 1 produces.
- Produces: the `migrate` CLI. JSON adds `source`, `domain` (str or null), `url`, `dry_run`, `copied_files: [str]`, `pruned_files: [str]`, `changed_files: [{"path": str, "replacements": int}]`. New warning code: `no-domain`.

- [ ] **Step 1: Write the failing tests**

Append to `script/test_project_sites.py`, above `if __name__ == "__main__":`:

```python
SOURCE_FILES = {
    "index.html": ('<html><head>'
                   '<meta property="og:url" content="https://demo.org/">'
                   '<meta property="og:image" content="https://demo.org/static/img/og.png">'
                   '<link rel="stylesheet" href="static/css/site.css"></head>'
                   '<body><img src="static/img/og.png"></body></html>'),
    "static/css/site.css": "body { background: url(../img/bg.png); }",
    "static/img/og.png": b"\x89PNG og",
    "static/img/bg.png": b"\x89PNG bg",
    "static/img/unused.jpg": b"\xff\xd8 unused",
    "CNAME": "demo.org\n",
    ".nojekyll": "",
    "README.md": "# demo website",
    ".gitignore": "node_modules\n",
    ".github/workflows/pages.yml": "on: push",
    "static/.DS_Store": b"\0\0",
}
SITE_FILES = ["index.html", "static/css/site.css", "static/img/bg.png",
              "static/img/og.png", "static/img/unused.jpg"]


class MigrateTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.fx = Fixture(self._tmp.name)
        self.src = self.fx.tmp / "src"
        for rel, content in SOURCE_FILES.items():
            self.fx.write(rel, content, base=self.src)
        subprocess.run(["git", "init", "-q"], cwd=self.src, check=True)
        self.target = self.fx.root / "project-sites/demo"

    def tearDown(self):
        self._tmp.cleanup()

    def migrate(self, *extra, cwd=None):
        return self.fx.run_json("migrate", str(self.src), "demo", *extra, cwd=cwd)

    def test_copies_site_without_repo_plumbing(self):
        code, out = self.migrate()
        self.assertEqual(code, 0, out)
        copied = sorted(p.relative_to(self.target).as_posix() for p in self.target.rglob("*") if p.is_file())
        self.assertEqual(copied, SITE_FILES)
        self.assertEqual((self.target / "static/img/og.png").read_bytes(), b"\x89PNG og")
        self.assertEqual(out["copied_files"], [f"project-sites/demo/{f}" for f in SITE_FILES])
        self.assertEqual((out["domain"], out["url"], out["dry_run"]), ("demo.org", NEW, False))
        self.assertIn(("unreferenced", "project-sites/demo/static/img/unused.jpg"), findings(out, "warnings"))

    def test_rewrites_old_domain_inside_the_site(self):
        self.migrate()
        html = (self.target / "index.html").read_text(encoding="utf-8")
        self.assertIn(f'content="{NEW}"', html)
        self.assertIn(f'content="{NEW}static/img/og.png"', html)
        self.assertNotIn("//demo.org", html)

    def test_rewrites_links_in_main_site_and_other_project_sites(self):
        pub = self.fx.write("_publications/demo2024.md", "---\nwebsite: https://demo.org/\n---\n")
        card = self.fx.write("_projects/area.html", '<a href="http://www.demo.org/sub/page.html">x</a>')
        other = self.fx.write("project-sites/other/index.html", '<a href="https://demo.org#results">x</a>')
        code, out = self.migrate()
        self.assertEqual(code, 0, out)
        self.assertIn(f"website: {NEW}\n", pub.read_text(encoding="utf-8"))
        self.assertIn(f'href="{NEW}sub/page.html"', card.read_text(encoding="utf-8"))
        self.assertIn(f'href="{NEW}#results"', other.read_text(encoding="utf-8"))
        changed = {c["path"]: c["replacements"] for c in out["changed_files"]}
        self.assertEqual(changed, {"project-sites/demo/index.html": 2, "_publications/demo2024.md": 1,
                                   "_projects/area.html": 1, "project-sites/other/index.html": 1})

    def test_leaves_lookalike_domains_alone(self):
        keep = ("https://notdemo.org/ https://demo.org.cn/ https://demo.organic/ "
                "https://sub.demo.org/ mail@demo.org see ")
        page = self.fx.write("_projects/area.html", keep + "https://demo.org.")
        self.migrate()
        self.assertEqual(page.read_text(encoding="utf-8"), keep + NEW + ".")

    def test_cname_with_www_prefix(self):
        self.fx.write("CNAME", "www.demo.org\n", base=self.src)
        code, out = self.migrate()
        self.assertEqual(out["domain"], "demo.org")
        self.assertNotIn("//demo.org", (self.target / "index.html").read_text(encoding="utf-8"))

    def test_domain_flag_overrides_cname(self):
        self.fx.write("index.html", '<a href="https://old.example.com/x">x</a>', base=self.src)
        code, out = self.migrate("--domain", "https://www.old.example.com/")
        self.assertEqual(out["domain"], "old.example.com")
        self.assertIn(f'href="{NEW}x"', (self.target / "index.html").read_text(encoding="utf-8"))

    def test_missing_domain_warns_and_skips_rewrite(self):
        (self.src / "CNAME").unlink()
        code, out = self.migrate()
        self.assertEqual(code, 0, out)
        self.assertIsNone(out["domain"])
        self.assertIn(("no-domain", "project-sites/demo/"), findings(out, "warnings"))
        self.assertIn("https://demo.org/", (self.target / "index.html").read_text(encoding="utf-8"))

    def test_dry_run_writes_nothing(self):
        self.fx.write("_publications/demo2024.md", "website: https://demo.org/\n")
        before = self.fx.snapshot()
        code, out = self.migrate("--dry-run", "--prune-unreferenced")
        self.assertEqual(code, 0, out)
        self.assertEqual(self.fx.snapshot(), before)
        self.assertTrue(out["dry_run"])
        self.assertEqual(len(out["copied_files"]), 5)
        self.assertEqual(out["pruned_files"], ["project-sites/demo/static/img/unused.jpg"])
        self.assertIn("_publications/demo2024.md", {c["path"] for c in out["changed_files"]})

    def test_prune_unreferenced(self):
        self.fx.write("static/videos/sample.mp4", b"mp4", base=self.src)
        code, out = self.migrate("--prune-unreferenced")
        self.assertEqual(code, 0, out)
        self.assertEqual(out["pruned_files"], ["project-sites/demo/static/img/unused.jpg",
                                               "project-sites/demo/static/videos/sample.mp4"])
        self.assertFalse((self.target / "static/img/unused.jpg").exists())
        self.assertFalse((self.target / "static/videos").exists())
        self.assertTrue((self.target / "static/img/bg.png").exists())
        self.assertNotIn("unreferenced", {w["code"] for w in out["warnings"]})

    def test_rule_violations_are_copied_and_reported(self):
        self.fx.write("notes.md", "# notes", base=self.src)
        code, out = self.migrate()
        self.assertEqual(code, 1)
        self.assertTrue((self.target / "notes.md").exists())
        self.assertIn(("markdown", "project-sites/demo/notes.md"), findings(out, "errors"))

    def test_refuses_existing_target_bad_name_and_bad_source(self):
        self.assertEqual(self.fx.run("migrate", str(self.src), "Demo").returncode, 2)
        self.assertEqual(self.fx.run("migrate", str(self.fx.tmp / "nope"), "nope").returncode, 2)
        self.fx.write("project-sites/demo/index.html", "<p>existing</p>")
        code, out = self.migrate()
        self.assertEqual(code, 2)
        self.assertIn("already exists", out["usage_error"])

    def test_non_utf8_and_binary_files_are_copied_byte_for_byte(self):
        latin = b"caf\xe9 https://demo.org/"
        self.fx.write("static/notes.txt", latin, base=self.src)
        self.fx.write("index.html", b'<p>x</p>\r\n<a href="static/notes.txt">https://demo.org/</a>\r\n',
                      base=self.src)
        code, out = self.migrate()
        self.assertEqual(code, 0, out)
        self.assertEqual((self.target / "static/notes.txt").read_bytes(), latin)
        self.assertEqual((self.target / "static/img/og.png").read_bytes(), b"\x89PNG og")
        self.assertEqual((self.target / "index.html").read_bytes(),
                         f'<p>x</p>\r\n<a href="static/notes.txt">{NEW}</a>\r\n'.encode())

    def test_runs_from_a_subdirectory(self):
        sub = self.fx.write("_publications/x.md", "x").parent
        code, out = self.migrate(cwd=sub)
        self.assertEqual(code, 0, out)
        self.assertTrue((self.target / "index.html").exists())

    def test_human_output_summarizes_the_migration(self):
        proc = self.fx.run("migrate", str(self.src), "demo")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Copied 5 files.", proc.stdout)
        self.assertIn(NEW, proc.stdout)
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python3 -m unittest script/test_project_sites.py -v`
Expected: the 12 `CheckTests` PASS. The 14 `MigrateTests` FAIL or ERROR (argparse: `invalid choice: 'migrate'`, exit 2, empty stdout, JSON decode error).

- [ ] **Step 3: Implement migrate**

In `script/project_sites.py`:

(a) Replace the import block with:

```python
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
```

(b) Replace the `REF_EXTS` comment and line with:

```python
# Repository plumbing that is not part of a site and is never copied.
SKIP_AT_ROOT = {".git", ".github", "CNAME", ".nojekyll", ".gitignore"}
SKIP_ANYWHERE = {".DS_Store"}

# Files scanned for references (unreferenced check) and rewritten (old domain).
REF_EXTS = {".html", ".htm", ".css", ".js", ".json"}
SITE_TEXT_EXTS = REF_EXTS | {".xml", ".txt", ".svg", ".webmanifest"}
MAIN_TEXT_EXTS = {".html", ".md", ".markdown", ".yml", ".yaml"}
MAIN_DIRS = ["_publications", "_projects", "_newsposts", "_blogposts",
             "_includes", "_layouts", "_data", "_people"]
```

(c) Insert these functions after `check_site`:

```python
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
```

(d) Replace `render` with:

```python
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
```

(e) Replace `build_parser` and `main` with:

```python
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
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python3 -m unittest script/test_project_sites.py -v`
Expected: all 26 tests PASS. Also run `python3 script/project_sites.py --help` and `python3 script/project_sites.py migrate --help`. Expected: the usage text with examples.

- [ ] **Step 5: Commit**

```bash
git add script/project_sites.py script/test_project_sites.py
git commit -m "Add migrate subcommand to project-sites script"
```

---

### Task 3: Docs, agent discoverability, build excludes

**Files:**
- Modify: `_config.yml` (add `exclude:` before `# Build settings`)
- Create: `AGENTS.md`, `CLAUDE.md`, `project-sites/README.md`
- Modify: `README.md` (new "Project sites" section after "## Overview")

**Interfaces:**
- Consumes: CLI from Tasks 1 and 2 (`migrate`, `check`, flags, exit codes, error codes).
- Produces: the docs that Task 4's verification checks are absent from `_site/`.

- [ ] **Step 1: Build a baseline file list (before any change)**

```bash
S=/tmp/claude-1000/-home-robin-Documents-eth-sri-github-io/dd0f5b33-d664-4e2d-9648-f7a705a40c97/scratchpad
bundle exec jekyll build -q -d "$S/site-before" && (cd "$S/site-before" && find . -type f | sort) > "$S/before.txt"
```

- [ ] **Step 2: Add the `exclude:` list to `_config.yml`**

Insert before `# Build settings`:

```yaml
# Not part of the published site. Setting exclude replaces Jekyll 3's defaults,
# so they are restated here.
exclude:
  - Gemfile
  - Gemfile.lock
  - node_modules
  - vendor/bundle/
  - vendor/cache/
  - vendor/gems/
  - vendor/ruby/
  - AGENTS.md
  - CLAUDE.md
  - docs/
  - project-sites/README.md

```

- [ ] **Step 3: Write `AGENTS.md`**

```markdown
# AGENTS.md

Guidance for coding agents (and people) working in this repository: the SRI Lab website, https://www.sri.inf.ethz.ch.

## How the site is built

- Jekyll 3 site, built by GitHub Pages (`github-pages` gem) on every push to `master`. **A push to `master` deploys immediately.**
- Local preview: `bundle exec jekyll serve` (run `bundle install` first if gems are missing).
- Content lives in collections: `_people/`, `_publications/`, `_projects/` (research areas, served at `/research/<name>`), `_blogposts/`, `_newsposts/`, `_teaching/`, `_workshops/`, `_main/`. Layouts are in `_layouts/`, partials in `_includes/`. See `README.md` for the front matter of each type.
- PDFs, slides and other large files go on the file server (`files.sri.inf.ethz.ch`, see `README.md`), never into git (`*.pdf` is git-ignored).
- After adding room mentions such as "CAB G 56", run `python3 extract_rooms.py`.
- GitHub Pages renders Markdown files without front matter into public pages. Add non-public docs to `exclude:` in `_config.yml`.

## Project sites (`project-sites/<name>/`)

Standalone project websites, for example sites that used to have their own domain, are served verbatim (no SRI header, no Jekyll templating) at `https://www.sri.inf.ethz.ch/project-sites/<name>/`. This repo is their source of truth.

- Migrate an existing site: `python3 script/project_sites.py migrate <owner/repo or dir> <name> [--prune-unreferenced] [--dry-run] [--json]`
- Validate after any edit, or for a new site created by hand: `python3 script/project_sites.py check <name> [--json]`
- Exit codes: `0` ok, `1` rule violations (fix them, then re-run `check`), `2` usage error.
- Rules: no front matter, no Markdown, no names starting with `_` `.` `#`, relative paths only, no PDFs, no files over 5 MB.
- Full guide, including how to fix each error code: `project-sites/README.md`. Tests: `python3 -m unittest script/test_project_sites.py -v`.
```

- [ ] **Step 4: Write `CLAUDE.md`**

```markdown
@AGENTS.md
```

- [ ] **Step 5: Write `project-sites/README.md`**

```markdown
# Project sites

Standalone project websites hosted as part of the SRI Lab website. Each folder `project-sites/<name>/` is served **verbatim** (no SRI header or footer, no Jekyll templating) at

    https://www.sri.inf.ethz.ch/project-sites/<name>/

This folder is the source of truth: edit a project site here, like any other page of this repository. This README is not published.

## Migrate an existing website

For a site that lives in its own repository and domain (typically an `eth-sri/<project>-website` repo with a `CNAME` file):

1. **Preview.**

       python3 script/project_sites.py migrate eth-sri/<repo> <name> --prune-unreferenced --dry-run

   `<name>` is a short, lowercase, hyphenated project name (`baxbench`, not `baxbench-website`). The old domain is read from the repo's `CNAME`; override it with `--domain`.
2. **Review the "Pruned" list.** These are files that nothing in the site mentions by name, usually template leftovers such as sample videos and carousel images. If the site builds file names in JavaScript (`"img" + i + ".png"`), leave out `--prune-unreferenced` and delete leftovers by hand.
3. **Migrate.** Run the same command without `--dry-run`. It copies the site (without `CNAME`, `.nojekyll`, `README`, `.github/`), rewrites links to the old domain (in the site itself, in `_publications/`, `_projects/`, news, blog, and other project sites), and runs `check`.
4. **Fix errors** (table below) until `python3 script/project_sites.py check <name>` exits 0.
5. **Preview locally.** Run `bundle exec jekyll serve`, open http://localhost:4000/project-sites/<name>/ and compare with the old site.
6. **Commit** the new folder and the rewritten links, then push or open a PR. The site is live once it is on `master`.
7. **Retire the old repository.** Add a note to its README ("Moved to https://www.sri.inf.ethz.ch/project-sites/<name>/, edit it in eth-sri/eth-sri.github.io"), then archive it on GitHub. We do not set up redirects: the old domain keeps serving the old copy until it lapses or GitHub Pages is switched off for that repo.

## Create a new project site

1. Create `project-sites/<name>/index.html`. Any static HTML/CSS/JS works, including templates like Nerfies/Bulma.
2. Follow the rules below and run `python3 script/project_sites.py check <name>`.
3. Link it from the main site: the `website:` field of the publication in `_publications/`, and/or a card in the research area in `_projects/`.

## Rules

| Rule | Why |
|---|---|
| No front matter (a `---` block at the top of a file) | Jekyll would run the file through Liquid templating, which breaks `{{ }}` in JavaScript. |
| No Markdown files (`.md`, `.markdown`) | GitHub Pages renders them into pages. |
| No file or folder names starting with `_`, `.` or `#`, or ending in `~` | Jekyll leaves them out of the site without warning. |
| Relative paths only (`static/x.png`, not `/static/x.png`) | The site lives under `/project-sites/<name>/`, not at the domain root. |
| No PDFs, no files over 5 MB | Keeps the repository small. Upload to files.sri.inf.ethz.ch (see the main `README.md`) or link arXiv. |

## `check` error codes

| Code | How to fix |
|---|---|
| `front-matter` | Delete the leading `---` … `---` block. |
| `markdown` | Convert the file to HTML, or delete it. |
| `jekyll-skipped` | Rename the file or folder (e.g. `_next/` → `next/`) and update references to it, or delete it. Also raised for paths in `exclude:` in `_config.yml`. |
| `git-ignored` | The repo's `.gitignore` ignores the file (e.g. `*.pdf`), so it would never be committed. Host it elsewhere and link to it. |
| `pdf` | Upload to files.sri.inf.ethz.ch or use the arXiv version, and update the link. |
| `root-absolute-path` | Drop the leading `/` so the path is relative to the page (from a sub-page, use `../`). `href="/"` (link to the SRI homepage) is allowed. |
| `too-large` | Upload to files.sri.inf.ethz.ch and link to the absolute URL, or compress the file. `--allow-large` overrides this in exceptional cases. |
| `no-index` | Add an `index.html` at the site root. |

Warnings do not fail the check: `large` (over 1 MB, consider compressing), `unreferenced` (nothing mentions the file by name; delete it if unused), `no-domain` (`migrate` only: no `CNAME` and no `--domain`, so no links were rewritten).

## For agents and scripts

- Commands never prompt. Add `--json` for one JSON object on stdout with keys `ok`, `errors`, `warnings` (each finding is `{code, path, detail}`), plus `domain`, `url`, `dry_run`, `copied_files`, `pruned_files`, `changed_files` for `migrate`. Usage errors print `{"ok": false, "usage_error": "..."}`.
- Exit codes: `0` ok (warnings allowed), `1` check errors, `2` usage error.
- Commands work from any directory inside the repository.
- Tests: `python3 -m unittest script/test_project_sites.py -v`.
```

- [ ] **Step 6: Add a section to `README.md`**

Insert after the `## Overview` section (before `## Installation`):

```markdown
## Project sites

Standalone project websites (e.g. sites that used to have their own domain) live in [`project-sites/`](project-sites/) and are served as-is at `https://www.sri.inf.ethz.ch/project-sites/<name>/`. To migrate a site or create a new one, see [project-sites/README.md](project-sites/README.md). In short: `python3 script/project_sites.py migrate eth-sri/<repo> <name>`.

```

- [ ] **Step 7: Verify that the build output changed only by the excluded docs**

```bash
bundle exec jekyll build -q -d "$S/site-after" && (cd "$S/site-after" && find . -type f | sort) > "$S/after.txt"
diff "$S/before.txt" "$S/after.txt"
```

Expected: the diff shows only removals under `./docs/`. AGENTS.md, CLAUDE.md and project-sites/README.md were not in the baseline and are absent from `after.txt`. No other line changes.

- [ ] **Step 8: Commit**

```bash
git add _config.yml AGENTS.md CLAUDE.md project-sites/README.md README.md
git commit -m "Document project sites for people and agents; exclude docs from the build"
```

---

### Task 4: Pilot migration of llm-quantization-attack.org

**Files:**
- Create: `project-sites/llm-quantization-attack/**` (generated by the script)
- Modify: `_publications/egashira2024quantization.md` (rewritten by the script)

- [ ] **Step 1: Dry run and review the pruned list**

```bash
python3 script/project_sites.py migrate eth-sri/exploiting-llm-quantization-website llm-quantization-attack --prune-unreferenced --dry-run
```

Expected: about 30 files copied. Pruned: the carousel `.mp4`/`.jpg` files, `sample.pdf`, `bulma.css.map.txt`, the unminified `bulma-carousel.js`/`bulma-slider.js`, and `favicon.ico`. Before accepting the pruned list, confirm that each file is unused by grepping the source `index.html` and `static/js/*.js` for its name stem. Rewrites: the site's `index.html` (og:url, og:image) and `_publications/egashira2024quantization.md`. No errors.

- [ ] **Step 2: Migrate**

```bash
python3 script/project_sites.py migrate eth-sri/exploiting-llm-quantization-website llm-quantization-attack --prune-unreferenced
python3 script/project_sites.py check llm-quantization-attack; echo "exit $?"
```

Expected: `exit 0`.

- [ ] **Step 3: Production-like build and byte-identity check**

```bash
cat > "$S/ghpages.yml" <<'EOF'
plugins:
  - jekyll-feed
  - jekyll-seo-tag
  - jekyll-optional-front-matter
  - jekyll-readme-index
  - jekyll-titles-from-headings
  - jekyll-relative-links
  - jekyll-default-layout
EOF
bundle exec jekyll build -q --config _config.yml,"$S/ghpages.yml" -d "$S/site-gh"
diff -r project-sites/llm-quantization-attack "$S/site-gh/project-sites/llm-quantization-attack" && echo IDENTICAL
ls "$S/site-gh/project-sites/"   # expected: only llm-quantization-attack (no README.html / index.html)
ls "$S/site-gh" | grep -E '^(AGENTS|CLAUDE|docs)' || echo "docs excluded"
grep -o 'href="[^"]*project-sites/llm-quantization-attack/[^"]*"' "$S/site-gh/publications/egashira2024quantization.html" | head -3
```

Expected: `IDENTICAL`, `project-sites/` contains only the site folder, `docs excluded`, and the publication page links to `https://www.sri.inf.ethz.ch/project-sites/llm-quantization-attack/`.

- [ ] **Step 4: Visual comparison**

Serve `$S/site-gh` with `python3 -m http.server 8765 -d "$S/site-gh"`. Take full-page screenshots of `http://localhost:8765/project-sites/llm-quantization-attack/` and `https://llm-quantization-attack.org/` with headless Chromium/Playwright, using the same viewport (1280 wide), and compare them visually. Also confirm in the browser that no request to a site asset returns 404.

- [ ] **Step 5: Commit**

```bash
git add project-sites/llm-quantization-attack _publications/egashira2024quantization.md
git commit -m "Migrate llm-quantization-attack.org to /project-sites/llm-quantization-attack/"
```

- [ ] **Step 6: Report.** Merging `project-sites` into `master` (which deploys), and archiving `eth-sri/exploiting-llm-quantization-website`, are left to the maintainers.
