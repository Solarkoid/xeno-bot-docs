---
title: Contributing
description: Thank you for helping improve the docs and project. This file explains the recommended workflow for proposing documentation and code changes, how to run the docs locally, and how to get help.
tags: [contributing, development, guidelines]
keywords: [xeno, bot, contributing, documentation]
author: Devvyyxyz
image: assets/images/faq-og.png
date: 2026-03-04
permalink: /contributing/
toc: true
icon: mdi:help-circle
aliases: [/contributing/, /contributing-guidelines/]
---

Thank you for helping improve the docs and project. This file explains the recommended workflow for proposing documentation and code changes, how to run the docs locally, and how to get help.

----
## Suggested workflow

- Use the **Edit this page** link on any documentation page to propose documentation changes. That opens the source file on GitHub — make an edit and submit a pull request.
- For large or code changes, fork the repo, create a branch named `fix/<short-description>` or `feat/<short-description>`, make your changes, then open a pull request against `main`.
- Include a clear PR description with what you changed and why, and link any relevant issues.

## Pull request guidelines

- Target branch: `main`.
- Use descriptive, imperative commit messages (e.g., "Fix broken command example").
- If your change affects behavior or API, add tests or instructions for reviewers to verify.

## Editing docs locally

- Use the page template at [Page Template](Page Template.md) when creating a new documentation page.

1. Create and activate a Python venv in the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

3. Build or serve the docs locally:

```bash
python -m mkdocs build
# or for live reload
mkdocs serve
```

4. After editing Markdown files, run `mkdocs build` to check the site builds and review changes at `http://127.0.0.1:8000` when using `mkdocs serve`.

## Coding style & tests

- Follow existing code style in the repository. Keep changes minimal and focused.
- Run existing tests where applicable and include instructions in your PR if special steps are needed.

## Reporting issues or requesting help

- Open an issue at: {{ config.repo_url }}/issues
- Join the support Discord (see the Links page) if you need live help.

## License and contributor agreement

By submitting a pull request you agree to the repository's license and that your contribution will be made available under the same license.
