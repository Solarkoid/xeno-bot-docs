# Xeno Bot Docs (MkDocs)

This repository contains the documentation site for Xeno Bot using MkDocs with the Dracula theme.

Requirements
- Python 3.8+ (use `python3`)
- `git` (required to install the Dracula theme from GitHub)

Local setup (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

Local preview

```bash
mkdocs serve
# if `mkdocs` is not on PATH while the venv is active:
python -m mkdocs serve
```

Build static site

```bash
mkdocs build
```

Notes
- `requirements.txt` installs `mkdocs-dracula-theme` directly from the Dracula repo and pins `mkdocs>=1.6.1,<2.0.0` which is required by the theme.
- If `pip install -r requirements.txt` fails, ensure `git` is installed (try `xcode-select --install` or install `git` via Homebrew).

Deployment

The included GitHub Actions workflow will build the site on pushes to `main` and deploy to GitHub Pages (`.github/workflows/pages.yml`).

Edit `mkdocs.yml` and the `docs/` directory to add content and customize the theme.
