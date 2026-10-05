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
