#!/usr/bin/env python3
"""Refresh GitHub star counts in the profile README.

Rewrites the FreePeak project table (between the STARS markers) and the
upstream heading counts, re-sorting table rows by stars, descending.
Stdlib only.
"""
import argparse
import json
import os
import re
import sys
import urllib.request

START = "<!-- STARS:START -->"
END = "<!-- STARS:END -->"
API_URL = "https://api.github.com/repos/{}"

ROW_RE = re.compile(r"^\|\s*\[`[^`]+`\]\(https://github\.com/([^/\s)]+/[^/\s)]+)\)")
UPSTREAM_RE = re.compile(
    r"^(#### \[`([^`]+)`\]\([^)]+\) — ★ )([\d,]+)$", re.MULTILINE
)


def split_region(text):
    lines = text.split("\n")
    if START not in lines or END not in lines:
        raise ValueError("STARS markers not found in README")
    start, end = lines.index(START), lines.index(END)
    if end < start:
        raise ValueError("STARS:END appears before STARS:START")
    return lines, start, end


def table_rows(lines, start, end):
    """Return (line index, owner/repo) for each project row inside the markers."""
    return [
        (i, m.group(1))
        for i in range(start + 1, end)
        if (m := ROW_RE.match(lines[i]))
    ]


def repos_in(text):
    lines, start, end = split_region(text)
    repos = [repo for _, repo in table_rows(lines, start, end)]
    repos += [m.group(2) for m in UPSTREAM_RE.finditer(text)]
    return repos


def read_counts(text):
    """Current star count per repo, as written in the README."""
    lines, start, end = split_region(text)
    counts = {}
    for i, repo in table_rows(lines, start, end):
        counts[repo] = int(lines[i].split("|")[-2].strip().strip("*"))
    for m in UPSTREAM_RE.finditer(text):
        counts[m.group(2)] = int(m.group(3).replace(",", ""))
    return counts


def apply_counts(text, stars):
    """Return text with star counts applied; only the table region and upstream headings change."""
    lines, start, end = split_region(text)
    rows = table_rows(lines, start, end)
    entries = []
    for i, repo in rows:
        cells = lines[i].split("|")
        cells[-2] = f" **{stars[repo]}** "
        entries.append((stars[repo], "|".join(cells)))
    entries.sort(key=lambda entry: -entry[0])  # stable: ties keep existing order
    for (i, _), (_, line) in zip(rows, entries):
        lines[i] = line
    updated = "\n".join(lines)
    return UPSTREAM_RE.sub(lambda m: f"{m.group(1)}{stars[m.group(2)]:,}", updated)


def fetch_stars(owner_repo):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "readme-star-sync",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(API_URL.format(owner_repo), headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return int(json.load(response)["stargazers_count"])


def fetch_all(repos, fetch):
    return {repo: fetch(repo) for repo in dict.fromkeys(repos)}


def sync_file(path, fetch):
    """Update the README at path in place. Writes only when content changed."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    stars = fetch_all(repos_in(text), fetch)
    old = read_counts(text)
    updated = apply_counts(text, stars)
    if updated == text:
        return "no star count changes"
    with open(path, "w", encoding="utf-8") as f:
        f.write(updated)
    changed = sum(1 for repo, count in stars.items() if old.get(repo) != count)
    return f"updated {changed} star count(s) across {len(stars)} repo(s)"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("path", nargs="?", default="README.md")
    args = parser.parse_args(argv)
    try:
        print(sync_file(args.path, fetch_stars))
    except Exception as exc:  # any fetch or parse failure: leave README untouched
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
