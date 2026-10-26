# Project instructions

## Repository and deployment model

- This repository contains Jerry Chi's Pelican website at https://jerrychi.com.
- `main` contains the project source, configuration, helper scripts, theme backups,
  and tracked generated files under `output/`. It also contains files that do not
  belong on the public website.
- `gh-pages` contains the generated site's files at the branch root. GitHub Pages
  serves this branch; updating `main` alone does not update the website.
- The remote is `origin` (`https://github.com/peacej/blog6.git`). The local
  `origin/HEAD` currently points to `origin/gh-pages`; do not mistake that default
  for the source branch or change it without authorization.
- This project uses direct commits and pushes to `main`; pull requests (PRs) are
  not required. Never merge the source tree into `gh-pages`, or import generated
  output into `main`.

## Required GitHub push workflow

- Whenever pushing this project to GitHub, use `buildpush.sh` or explicitly
  replicate its logic so both `main` and `gh-pages` are updated from the same
  intended source state. Do not treat a push to only one branch as complete.
- Ask Jerry before pushing unless the current request explicitly authorizes that
  action. Local preparation and checks may proceed. Do not open PRs as part of
  the normal workflow.
- If the deployment approach is uncertain, explain the uncertainty to Jerry
  before choosing an approach or pushing. Do not silently substitute a workflow
  that updates only one branch.
- Before deploying, inspect the working tree, staged diff, current branch, and
  remote branch state. Preserve unrelated changes. Bring the intended source
  changes onto `main` before running this script.
- When Jerry explicitly requests synchronization without changing the website,
  commit the intended local source/backup changes on `main` and push both branch
  refs while preserving the existing `gh-pages` commit and tree. Skip rebuilding
  and importing output for that operation: local `output/` may differ from the
  published files. Verify the remote `gh-pages` commit is unchanged. An already
  up-to-date deployment branch satisfies this content-preserving synchronization.

Run from the repository root in the configured Linux/WSL environment, with the
virtual environment activated:

```bash
source .venv/bin/activate
bash buildpush.sh
```

The script currently performs these steps in order:

1. Copy `../../pelican-themes/Flex` into `./pelican-themes-backup`.
2. Build with production settings: `pelican content -s publishconf.py`.
3. Stage everything with `git add .`, commit with message `update content`, and
   push the source branch with `git push origin main`.
4. Import the contents of `output/` into the local deployment branch using
   `ghp-import output -b gh-pages --cname=jerrychi.com`.
5. Check out `gh-pages`, push it with `git push origin gh-pages`, then return to
   `main`.

An equivalent workflow must preserve the theme backup, production build, intended
source/generated changes on `main`, generated-site-only tree on `gh-pages`, and
deployment `CNAME` containing `jerrychi.com`. `ghp-import` updates the local branch
without requiring a checkout; an equivalent workflow can push that branch
directly and keep the source checkout in place.

### Script limitations and deployment checks

- `buildpush.sh` neither activates `.venv` nor verifies the current branch. Start
  on `main` with the correct tools on `PATH`.
- It has no fail-fast handling: a failed copy, build, commit, checkout, or push
  can be followed by later commands. Use a fail-fast equivalent or supervise each
  step and stop on unexpected failures; never publish stale or incomplete output.
- Its `git add .` stages unrelated edits, deletions, and untracked files. Only run
  it when all changes it would stage are intended. Otherwise use an equivalent
  workflow with explicit staging of the intended files.
- Theme backup directory names have included a carriage return and its Windows
  filesystem representation (U+F00D). Inspect apparent bulk deletions alongside
  similarly named untracked directories: these may represent a path change.
  Preserve the backup contents and do not absorb unrelated changes without
  authorization.
- `publishconf.py` sets `DELETE_OUTPUT_DIRECTORY = True`; a production build
  replaces the generated output. Make changes in source rather than hand-editing
  `output/` or the deployment branch.
- Check the generated homepage, changed pages, theme assets, feeds, and
  `search-index.st` before publishing. Preserve `CNAME` during the import (the
  script's `--cname=jerrychi.com` creates it on `gh-pages`).
- After an authorized deployment, verify both remote branches match the intended
  local commits and check the Pages deployment/live site. If only one push
  succeeds, report the partial deployment and resolve the remaining step; do not
  claim completion. Do not force-push as a routine workaround.

## Build environment

- `.venv` is a Linux virtual environment created under Windows Subsystem for
  Linux (WSL), not a native Windows Python environment. Its recorded interpreter
  is `/usr/bin/python3.12`, and its scripts use absolute paths under
  `/mnt/c/Users/user/git/blog6/.venv`. Use it from WSL; relocation can break those
  paths. Do not replace it or upgrade dependencies incidentally.
- Verified versions at initial inspection: Python 3.12.3, Pelican 4.8.0,
  `ghp-import` 2.1.0, `pelican-search` 1.0.1, and `disqus-python` 0.4.2.
  Compare the active runtime and packages with these and `requirements.txt`
  before testing or rebuilding. GitHub Pages serves static files, so the local
  build environment determines the generated site's behavior.
- `requirements.txt` pins the Python dependencies but comments out
  `disqus-python`. The installed Disqus package came from the GitHub
  `disqus/disqus-python` master ZIP, as described in `README.md`; installing only
  the requirements file does not reproduce this dependency.
- Search requires the separate `stork` executable on `PATH`. WSL currently has
  Stork 1.6.0 at `/home/user/.cargo/bin/stork`; `STORK_VERSION = "1.5.0"` in
  `pelicanconf.py` selects the browser-side assets. These are distinct settings;
  preserve them unless deliberately changing and validating search compatibility.
- `pelicanconf.py` uses the external Flex theme at
  `/mnt/c/Users/user/pelican-themes/Flex`, which matches the script's relative
  copy source when run from this checkout. The in-repository backup is not the
  configured active theme. Account for both the active theme and its backup when
  making theme changes.
- Plugins are `plugins/disqus_static.py` and `pelican.plugins.search`. The Disqus
  plugin makes API requests at build time, so a full build requires network/API
  access as well as the local dependencies. Do not reproduce credential values
  from configuration in logs or documentation.
- `.venv` is ignored by Git, but the existing `.venv_backup20250104` has tracked
  files. Do not add environments or perform incidental cleanup of that backup.

## Conflicting helper commands

- `README.md` describes the correct `main` / `gh-pages` separation and recommends
  `buildpush.sh`.
- `Makefile` sets `GITHUB_PAGES_BRANCH=main`, and `tasks.py` sets
  `github_pages_branch` to `main`. Their `make github` / `invoke gh-pages`
  commands would import generated files into the source branch and do not
  implement the required two-branch workflow. Do not use them for deployment in
  their current form. Follow `buildpush.sh` and the instructions above.
- Local-only builds can use Pelican directly; use `publishconf.py` to validate
  production URLs, feeds, and output before deployment. A build-only check does
  not authorize a push.
