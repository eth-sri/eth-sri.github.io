# Project Sites: Hosting Project Websites Under www.sri.inf.ethz.ch

Date: 2026-10-05
Status: Draft for review

## Goal

Several SRI projects have standalone websites on their own domains (e.g. llm-quantization-attack.org, baxbench.com, watermark-stealing.org), each in its own `eth-sri/*-website` repository. We do not want to keep these domains forever. We move the sites into this repository so they are served at `https://www.sri.inf.ethz.ch/project-sites/<name>/` and can be linked from the group website.

Success means:

1. **Visually seamless:** a migrated site looks exactly as it did on its old domain (no shared SRI header/footer, the same model as `/zkay/` and `/silq-webpage/` today), lives on the SRI domain, and the main site links to it like any internal page.
2. **Easy transition:** a project author, or an agent acting for them, migrates a site with one command, reviews the diff, and commits. A brand-new project site is just a new folder. Both people and coding agents can find the process without being told where it is.

## Decisions

| Topic | Decision |
|---|---|
| Location | Site files live in this repo. The old website repo is archived after migration. |
| URL | `https://www.sri.inf.ethz.ch/project-sites/<name>/` |
| Styling | Original site, served verbatim. No shared header/footer. |
| Source of truth | `project-sites/<name>/` in this repo. Authors edit here. No sync from old repos. |
| Old domains | No redirects. Domains lapse when the group decides. |
| Migration tooling | Written guide plus `script/project_sites.py`, built for agents and people. |
| Pilot | llm-quantization-attack.org (`eth-sri/exploiting-llm-quantization-website`) → `project-sites/llm-quantization-attack/` |

## Context (findings that shape the design)

- `www.sri.inf.ethz.ch` is an ETH proxy in front of GitHub Pages for `eth-sri.github.io`. The site is built by GitHub Pages' own Jekyll (`github-pages` gem 232, Jekyll 3.10.0).
- Candidate sites (`baxbench-website`, `exploiting-llm-quantization-website`, `watermark-stealing-website`, `dlm-watermarking-website`, `honeyval-website`, `constat.github.io`, `proofcorpus-website`) are almost all the Bulma "Nerfies" academic template: one `index.html` plus `static/`, with relative paths only. They work in a subfolder without changes. Snapshot sizes are 2.6 to 15.5 MB, and much of that is unused template leftovers (the pilot has about 9 MB of unreferenced sample videos and images).
- matharena.ai runs on its own nginx server, and lmql.ai, chatprotect.ai and constrained-diffusion.ai are built from code repos. They are out of scope for the pilot. The tooling accepts any static site.
- Jekyll copies files without front matter verbatim, which is what we want. Three traps:
  - Jekyll silently skips paths with a segment starting with `_` or `.`, and anything matching `exclude`.
  - This repo's `.gitignore` ignores `*.pdf`, so PDFs are silently not committed.
  - **GitHub Pages enables extra plugins that a plain local `jekyll build` does not**, including `jekyll-optional-front-matter` and `jekyll-readme-index`. Front-matter-less Markdown is rendered into HTML pages (verified live: `/ISSUES.md` is also served as `/ISSUES.html`), and a `README.md` becomes the index of its directory if no `index.html` exists.
- In Jekyll 3.x, setting `exclude` in `_config.yml` replaces the built-in default list instead of extending it.
- Main-site references to old domains live in `_publications/*.md` (`website:` field), `_projects/*.html` (cards), and `_newsposts/`.

## Design

### 1. Layout and conventions

```
project-sites/
  README.md                       guide for people and agents (excluded from build)
  llm-quantization-attack/        → /project-sites/llm-quantization-attack/
    index.html
    static/...
```

Rules for every project site (enforced by `check`):

- **No front matter** in any file. Front matter would put the file through Liquid and break `{{ }}` in JavaScript.
- **No Markdown files** (`.md`, `.markdown`). GitHub Pages would render them into pages.
- **No path segments starting with `_`, `.` or `#`, or ending with `~`.** Jekyll skips them.
- **Relative paths only.** No root-absolute `src="/..."`, `href="/..."` or `url(/...)`, because the site no longer sits at the domain root.
- **No PDFs, and no files over 5 MB.** These go to `files.sri.inf.ethz.ch` (see the main README) or arXiv. This keeps the repo lean and the `.gitignore` unchanged. `--allow-large` overrides the size rule for exceptional cases.
- **Folder name:** a short, lowercase, hyphenated project name (`baxbench`, not `baxbench-website`), matching `^[a-z0-9]+(-[a-z0-9]+)*$`.

### 2. `_config.yml` changes

Add an `exclude` list. It restates the Jekyll 3 defaults (because setting `exclude` replaces them) and adds the new non-public files:

```yaml
exclude:
  # Jekyll 3 defaults (setting exclude replaces them)
  - Gemfile
  - Gemfile.lock
  - node_modules
  - vendor/bundle/
  - vendor/cache/
  - vendor/gems/
  - vendor/ruby/
  # repo documentation, not part of the site
  - AGENTS.md
  - CLAUDE.md
  - docs/
  - project-sites/README.md
```

Files currently published (for example `README.md` and `script/`) are left as they are. Cleaning them up is out of scope.

### 3. The script: `script/project_sites.py`

Python 3 standard library plus the `git` CLI, in the style of `extract_rooms.py`. It is non-interactive: every choice is a flag, so agents can run it unattended. Run it from the repo root (it locates the root itself via `git rev-parse --show-toplevel`).

#### `migrate <source> <name> [options]`

`<source>` is either `owner/repo` on GitHub (cloned with `--depth 1` into a temp dir) or a local directory.

1. Validate `<name>`. Refuse if `project-sites/<name>/` already exists.
2. Determine the old domain from the source's `CNAME`, or from `--domain` (which overrides it). If neither exists, skip the link rewriting and warn.
3. Copy every file into `project-sites/<name>/` except: `.git/`, `.github/`, `CNAME`, `.nojekyll`, `.gitignore`, `.DS_Store`, and `README*` at the source root. Other files that break the rules are copied anyway, so that `check` reports them and the author decides; nothing disappears silently.
4. With `--prune-unreferenced`, delete unreferenced page assets (see `check`; images, video, audio, fonts, PDF, CSS, JS, source maps) and list them. Unreferenced data, code and docs (`.json`, `.py`, `.sh`, `.txt`, …) are kept, because pages build data file names in code and authors still need their scripts.
5. Rewrite links to the old domain. The patterns are `http(s)://<domain>` and `http(s)://www.<domain>`, with or without a trailing slash and path. They become `https://www.sri.inf.ethz.ch/project-sites/<name>/<path>`. The rewrite applies to:
   - text files (`.html`, `.htm`, `.css`, `.js`, `.json`, `.xml`, `.txt`, `.svg`, `.webmanifest`) inside the new site;
   - every other published text file in the repository (`.html`, `.htm`, `.css`, `.js`, `.json`, `.xml`, `.txt`, `.svg`, `.webmanifest`, `.md`, `.markdown`, `.yml`, `.yaml`): all collections, `assets/`, root files and other folders under `project-sites/`. Skipped: hidden folders, `_site/`, `node_modules/`, `vendor/`, and paths in `exclude:` (so `docs/` and this guide are never rewritten).

   Each changed file is listed with its number of replacements.
6. Run `check <name>` and print its report.

Options: `--domain DOMAIN`, `--prune-unreferenced`, `--allow-large`, `--dry-run` (print every action without writing anything), `--json`.

#### `check <name>`

Validates `project-sites/<name>/`. Use it for migrated sites, for brand-new sites, and after edits.

Errors (exit code 1):

| Code | Condition |
|---|---|
| `front-matter` | File begins with `---` followed by a newline |
| `markdown` | `.md` / `.markdown` file |
| `jekyll-skipped` | A path segment starts with `_`, `.` or `#`, or ends with `~`, or the path matches the `exclude` list in `_config.yml` |
| `git-ignored` | `git check-ignore` reports the path as ignored (covers `*.pdf` and anything else) |
| `pdf` | `.pdf` file (reported even if a future `.gitignore` change stops ignoring it) |
| `root-absolute-path` | `src`/`href`/`action`/`poster`/`srcset="/…"` in HTML, CSS `url(/…)` in HTML/CSS, and quoted file paths with an extension in JS or inline scripts (`fetch('/static/data/x.json')`). Protocol-relative `//` is allowed, and so is an exact `href="/"` pointing at the main site. |
| `too-large` | File over 5 MB (skipped with `--allow-large`) |
| `no-index` | No `index.html` at the site root |

Warnings (do not affect the exit code):

| Code | Condition |
|---|---|
| `large` | File over 1 MB |
| `unreferenced` | The file's basename (or its URL-encoded form) appears in no text file of the site (`.html`, `.htm`, `.css`, `.js`, `.json`, `.xml`, `.txt`, `.svg`, `.webmanifest`). `index.html` files are exempt. This is a heuristic. |

#### Output and exit codes

- Human-readable by default: grouped sections, one line per finding, with the path relative to the repo root.
- `--json` prints a single JSON object to stdout:
  ```json
  {"command": "check", "name": "...", "ok": true,
   "errors": [{"code": "...", "path": "...", "detail": "..."}],
   "warnings": [...], "changed_files": [...], "pruned_files": [...]}
  ```
- Exit codes: `0` OK (warnings allowed), `1` check errors, `2` usage error or failed precondition (bad name, folder exists, clone failed).
- `--help` on the script and on each subcommand gives full usage with examples.

### 4. Discoverability for people and agents

- **`AGENTS.md`** (new, repo root): a short orientation to the repo (Jekyll on GitHub Pages, content collections, where large files go, the room-extraction script), plus a "Project sites" section with the rules, the command, and a pointer to `project-sites/README.md`.
- **`CLAUDE.md`** (new): contains `@AGENTS.md`, so Claude Code loads the same file. This is always in context, so no separate Claude skill is needed.
- **`project-sites/README.md`**: the full guide.
  - Migrating an existing site: the command, reviewing the diff, committing.
  - Starting a new site: create the folder, then run `check`.
  - Retiring the old repo: add a "moved to …" note to its README, archive it, let the domain lapse at will.
  - Every `check` error code and how to fix it.
- **`README.md`** (main): a short "Project sites" section pointing to the guide.

### 5. Testing

`script/test_project_sites.py`, using `unittest` (standard library). Each test builds a fixture "repo root" in a temp directory: a minimal `_config.yml`, `.gitignore`, `git init`, and a fixture source site. The tests cover:

- copy exclusions (`.git`, `CNAME`, `.nojekyll`, root `README.md`, etc.);
- the domain rewrite (with and without `www.`, `http`/`https`, with a path, inside the site and in main-site sources);
- every check error and warning code, and the exit codes;
- `--dry-run` writing nothing;
- `--prune-unreferenced`;
- `--json` output shape;
- refusing an existing target folder or an invalid name.

Tests are written before the implementation (TDD).

### 6. Pilot: llm-quantization-attack.org

1. `python3 script/project_sites.py migrate eth-sri/exploiting-llm-quantization-website llm-quantization-attack --prune-unreferenced`. Review the pruned list by hand (expected: template carousel videos and images, `sample.pdf`, `bulma.css.map.txt`, the unminified carousel/slider JS).
2. Expected rewrites: `og:url`/`og:image` in the site's `index.html`, and `website:` in `_publications/egashira2024quantization.md`.
3. Verify:
   - **Production-like build:** `bundle exec jekyll build` with an extra config that enables GitHub Pages' default plugins (`jekyll-optional-front-matter`, `jekyll-readme-index`, `jekyll-titles-from-headings`, `jekyll-relative-links`, `jekyll-default-layout`). Confirm that every file in `project-sites/llm-quantization-attack/` appears byte-identical in `_site/`, and that `project-sites/README.md`, `AGENTS.md`, `CLAUDE.md` and `docs/` are absent from `_site/`.
   - **Visual:** serve locally and compare screenshots of `/project-sites/llm-quantization-attack/` against the live llm-quantization-attack.org.
   - **Links:** the publication page's "website" link points to the new URL.
   - **Check:** `check llm-quantization-attack` exits 0.
4. Work happens on the `project-sites` branch. Merging to `master` (which deploys), and archiving `eth-sri/exploiting-llm-quantization-website`, are left to the maintainers.

## Out of scope

- Redirects from old domains.
- Migrating sites other than the pilot (each author runs the script).
- A `/project-sites/` index or listing page.
- CI that runs `check` on every push (a cheap follow-up once the script exists).
- Cleaning up files the main site currently publishes by accident.
- Dynamic or non-GitHub-Pages sites (matharena.ai) and docs sites built from code repos (lmql.ai, zkay).
