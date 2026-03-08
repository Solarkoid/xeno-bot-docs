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
icon: material/github
aliases: [/contributing/, /contributing-guidelines/]
---

Thank you for helping improve the docs and project. This file explains the recommended workflow for proposing documentation and code changes, how to run the docs locally, and how to get help.

----

# Using Obsidian For Contribution

!!! note

    Using Obsidian is the recommended method for contributing to this site.

Obsidian is an excellent tool for contributing to the documentation — it provides a streamlined, Markdown-focused interface that allows you to concentrate on content creation. Whether you're on mobile or desktop, you can use Obsidian with community plugins to enhance the workflow.

----

## Using Obsidian On Mobile

To contribute using Obsidian on mobile:

1. **Download Obsidian**:
   - Download Obsidian from your app store ([iOS or Android](https://obsidian.md)).

2. **Set Up Community Plugins**:
   - Open Obsidian and click on `Settings` (gear icon).
   - Enable third-party plugins:
     - Go to `Options` > `Community Plugins` and enable the feature.
   - Install the following plugins:
     - **Git**: Allows you to push and pull changes to the repository.
     - **Templates**: Enables you to create consistent content using predefined templates.

3. **Clone the Repository**:
   - Use the Git plugin to clone the docs repository. Add your repository URL during setup.
   - Assign the cloned repository to a vault in Obsidian.

4. **Contribute**:
   - Open the Markdown file(s) you want to edit within your Obsidian vault.
   - Use the Templates plugin to insert the page template or other predefined snippets.
   - Make your changes, then save.

5. **Commit and Push**:
   - Use the Git plugin to commit your changes with a descriptive message.
   - Push your changes upstream to submit a pull request via GitHub.

----

## Using Obsidian On Desktop

To contribute using Obsidian on desktop:

1. **Download and Install Obsidian**:
   - Download the Obsidian desktop app from [Obsidian's website](https://obsidian.md/).

2. **Set Up Community Plugins**:
   - Open Obsidian and navigate to `Settings` (gear icon).
   - Enable third-party plugins:
     - Go to `Community Plugins` and toggle the feature on.
   - Install the necessary plugins:
     - **Git**: Push and pull changes directly from Obsidian.
     - **Templates**: Use preformatted templates for consistency in your contributions.

3. **Clone the Repository**:
   - If you already have Git installed:
     - Clone the repository:
       ```bash
       git clone <repo_url>
       ```
     - Open the cloned folder as an Obsidian vault.
   - Alternatively, use the Git plugin to clone the repository directly in Obsidian.

4. **Create or Edit Content**:
   - Navigate to the Markdown files you want to edit.
   - Use the Templates plugin to insert the required structure for pages or content.

5. **Review Changes Locally**:
   - Use the `mkdocs` commands provided in the "Editing Docs Locally" section to build and preview your changes.

6. **Commit and Push**:
   - Commit your changes with a descriptive message using the Git plugin.
   - Push to your branch and open a pull request on GitHub.

----

## Why Use Obsidian With These Plugins?

- **Git Plugin**: Simplifies the process of keeping your local edits synced with the repository.
- **Templates Plugin**: Ensures consistency in the format and style of your contributions by using the templates fokder.

By leveraging Obsidian and these two plugins, you can create a smooth editing experience that integrates seamlessly with the documentation workflow.

----

## Suggested workflow (Without Obsidian)

!!! warning

    This method of contributing to the site is not preferred, may lead to issues, and is only accessible on desktop devices.

- Use the **Edit this page** link on any documentation page to propose documentation changes. That opens the source file on GitHub — make an edit and submit a pull request.
- For large or code changes, fork the repo, create a branch named `fix/<short-description>` or `feat/<short-description>`, make your changes, then open a pull request against `main`.
- Include a clear PR description with what you changed and why, and link any relevant issues.

## Pull request guidelines

- Target branch: `main`.
- Use descriptive, imperative commit messages (e.g., "Fix broken command example").
- If your change affects behavior or API, add tests or instructions for reviewers to verify.

## Editing docs locally

- Use the page template at [basic-template](basic-template.md)ting a new documentation page.

----

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

## Contributors

{{ read_raw('docs/_generated/contributors_auto.md') }}