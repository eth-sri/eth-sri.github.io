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

    def test_root_absolute_file_paths_in_scripts_are_errors(self):
        self.fx.write("project-sites/demo/index.html",
                      '<link rel="stylesheet" href="static/site.css"><script src="static/app.js"></script>'
                      '<script>fetch("/static/data/inline.json")</script>')
        self.fx.write("project-sites/demo/static/app.js",
                      "fetch('/static/data/scores.json'); logo = `/static/img/logo.png`;\n"
                      's.replace(/"/g,"&quot;"); route(\'/buy_order\'); url = "//cdn.example.com/x.js";\n')
        code, out = self.fx.run_json("check", "demo")
        self.assertEqual(code, 1)
        found = sorted((f["path"], f["detail"].split('"')[1])
                       for f in out["errors"] if f["code"] == "root-absolute-path")
        self.assertEqual(found, [("project-sites/demo/index.html", "/static/data/inline.json"),
                                 ("project-sites/demo/static/app.js", "/static/data/scores.json"),
                                 ("project-sites/demo/static/app.js", "/static/img/logo.png")])

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

    def test_references_from_svg_xml_and_manifests_count(self):
        self.fx.write("project-sites/demo/index.html",
                      '<link rel="stylesheet" href="static/site.css"><link rel="manifest" href="site.webmanifest">'
                      '<meta name="msapplication-config" content="browserconfig.xml"><img src="static/figure.svg">')
        self.fx.write("project-sites/demo/site.webmanifest", '{"icons": [{"src": "static/android-192.png"}]}')
        self.fx.write("project-sites/demo/browserconfig.xml", '<square150x150logo src="static/mstile-150.png"/>')
        self.fx.write("project-sites/demo/static/figure.svg", '<svg><image href="photo.jpg"/></svg>')
        for name in ["android-192.png", "mstile-150.png", "photo.jpg"]:
            self.fx.write(f"project-sites/demo/static/{name}", b"img")
        code, out = self.fx.run_json("check", "demo")
        self.assertEqual(code, 0, out)
        self.assertEqual(out["warnings"], [])

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

    def test_prune_keeps_data_code_and_docs(self):
        kept = ["static/data/scores_easy.json", "static/data/convert.py", "static/data/update.sh",
                "static/data/notes.txt"]
        for rel in kept:
            self.fx.write(rel, "x", base=self.src)
        code, out = self.migrate("--prune-unreferenced")
        self.assertEqual(code, 0, out)
        self.assertEqual(out["pruned_files"], ["project-sites/demo/static/img/unused.jpg"])
        for rel in kept:
            self.assertTrue((self.target / rel).exists(), rel)
        self.assertIn(("unreferenced", "project-sites/demo/static/data/convert.py"), findings(out, "warnings"))

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

    def test_rewrites_every_published_source_but_not_unpublished_ones(self):
        published = ["_main/page.html", "_teaching/course.html", "popl2022/artifact.html",
                     "assets/blog/post.html", "index.md"]
        unpublished = ["_site/page.html", ".history/page.html", "node_modules/pkg/index.html",
                       "project-sites/README.md"]
        for rel in published + unpublished:
            self.fx.write(rel, "see https://demo.org/ for details")
        code, out = self.migrate()
        self.assertEqual(code, 0, out)
        for rel in published:
            self.assertEqual((self.fx.root / rel).read_text(encoding="utf-8"), f"see {NEW} for details", rel)
        for rel in unpublished:
            self.assertIn("https://demo.org/", (self.fx.root / rel).read_text(encoding="utf-8"), rel)

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


if __name__ == "__main__":
    unittest.main()
