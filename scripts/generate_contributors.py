#!/usr/bin/env python3
"""Generate a contributors markdown fragment for the docs from GitHub's contributors API.

Usage:
  GITHUB_TOKEN=... python scripts/generate_contributors.py

Writes: docs/_generated/contributors_auto.md
"""
import os
import sys
import requests

OWNER = "devvyyxyz"
REPO = "xeno-bot-docs"
OUT_DIR = os.path.join("docs", "_generated")
OUT_FILE = os.path.join(OUT_DIR, "contributors_auto.md")


def get_headers():
    token = os.environ.get("GITHUB_TOKEN")
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"token {token}"
    return headers


def fetch_contributors():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contributors"
    headers = get_headers()
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()


def fetch_user(login):
    url = f"https://api.github.com/users/{login}"
    headers = get_headers()
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        return {}
    return resp.json()


def ensure_out_dir():
    os.makedirs(OUT_DIR, exist_ok=True)


def write_markdown(contributors):
    ensure_out_dir()
    lines = []
    lines.append("<div style=\"display:flex;flex-wrap:wrap;align-items:flex-start\">")
    for c in contributors:
        login = c.get("login")
        avatar = c.get("avatar_url")
        html_url = c.get("html_url")
        user = fetch_user(login)
        name = user.get("name") or login
        block = (
            f"<div style=\"width:130px;text-align:center;display:inline-block;margin:6px\">"
            f"<a href=\"{html_url}\" target=\"_blank\" rel=\"noopener\">"
            f"<img src=\"{avatar}&s=128\" alt=\"{login}\" style=\"border-radius:50%;width:72px;height:72px;\"></a><br>"
            f"<div style=\"font-size:0.95em;margin-top:6px\">{name}<br><a href=\"{html_url}\" target=\"_blank\">@{login}</a></div>"
            f"</div>"
        )
        lines.append(block)
    lines.append("</div>")
    with open(OUT_FILE, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


def main():
    try:
        contributors = fetch_contributors()
    except Exception as e:
        print("Failed to fetch contributors:", e, file=sys.stderr)
        sys.exit(1)
    write_markdown(contributors)
    print("Wrote", OUT_FILE)


if __name__ == "__main__":
    main()
