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
