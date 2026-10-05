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
