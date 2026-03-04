---
title: Frequently asked questions and answers
description: Short answers and troubleshooting for Xeno Bot docs (FAQ).
tags: [faq, questions, answers]
keywords: [xeno, bot, faq, documentation]
author: Xeno Docs Team
image: assets/images/faq-og.png
date: 2026-03-04
permalink: /faq/
toc: true
search: true
aliases: [/faq-old/]
---

<!--- FAQ page demonstrating usage of site plugins: admonitions, tasklists,
		 mermaid diagrams, mkdocstrings, tags, and code highlighting. --->

## Quick Answers

> **Q: Where do I edit the docs?**

Edit Markdown files under the `docs/` directory (for example, `docs/FAQ.md`).
Push your changes and the site will be automatically rebuilt and deployed.

> **Q: How do I preview locally?**

Run the local dev server in your Python venv:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
# open http://127.0.0.1:8000
```

## Installation & Setup

If something goes wrong during install, check the virtualenv, `pip` and
that `git` is available on your system. The repo includes a `requirements.txt`
that pins compatible plugin versions.

### Common Install Errors

!!! warning "OpenSSL / LibreSSL"
		If you see a `NotOpenSSLWarning` referencing LibreSSL when installing
		requests/urllib3, consider upgrading your system OpenSSL or ignore the
		warning if the rest of the build succeeds. macOS users can run:

		```bash
		xcode-select --install
		brew install openssl
		```

## Commands

Use these quick command snippets when working with docs.

```bash
# Activate venv
source .venv/bin/activate

# Serve locally (live reload)
mkdocs serve

# Build static site
mkdocs build
```

## How Obsidian edits get published

This site is configured to auto-build when files under `docs/` are pushed to
`main`. The workflow triggers on `docs/**`, `mkdocs.yml`, and `requirements.txt`.

Here is a simple flowchart of the process:

```mermaid
flowchart LR
	U[Obsidian (local)] --> G[Git commit & push]
	G --> H[GitHub Actions (pages.yml)]
	H --> B[Build site (mkdocs build)]
	B --> P[gh-pages branch]
	P --> S[GitHub Pages serves site]
```

## Contributing & Editing

If you're editing docs:

- Use short, focused PRs.
- Run `mkdocs build` locally to verify the site builds.
- Add `tags:` in the page front-matter to categorize pages — the tags plugin
	will collect and index them automatically.

Example front-matter with tags:

```yaml
---
title: Example Page
tags: [howto, api]
---
```

## API / Reference (mkdocstrings example)

If you publish Python API docs, `mkdocstrings` can render docstrings inline.
Below is an example directive (replace with your package path):

```yaml
::: mypackage.client.Client
		rendering:
			show_root_heading: false
```

> Note: `mkdocstrings` requires the referenced package to be importable in the
> build environment.

## Troubleshooting

### Search not returning results

- Ensure `mkdocs build` completes and the `site/search/search_index.json`
	file is generated.

### Comments (Giscus) not appearing

- Confirm GitHub Discussions is enabled for the repo and the Giscus GitHub App
	is installed for this repository.
- Confirm the `data-category` and `data-category-id` in `overrides/partials/comments.html`
	match a real Discussions category.

## Tasks & Follow-ups

- [ ] Verify Discussions + Giscus app installation
- [ ] Add tags to key pages for better discoverability

## Examples and includes

You can include other Markdown snippets using the include plugin. Example:

```
{! links.md !}
```

This will inline the contents of `docs/links.md` into the page at build time.

---

Last updated: see page footer for Git metadata.


