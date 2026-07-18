#!/usr/bin/env python3
"""Validate that book/README.md's index actually matches the manuscript.

Checks:
1. Exactly one file per chapter number under book/ (no duplicates left
   behind by a rename, e.g. an old-titled file alongside its replacement).
2. Every chapter link in book/README.md resolves to a file that exists.
3. The link text in book/README.md matches the target file's actual H1
   heading (catches a renamed chapter whose index entry didn't get
   updated).

Exit code 0 if clean, 1 if any check fails.
"""
import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent


def check_one_file_per_chapter():
    errors = []
    by_number = defaultdict(list)
    for f in ROOT.glob("book/**/*.md"):
        if f.name == "README.md":
            continue
        m = re.match(r"(\d+)-", f.name)
        if m:
            by_number[int(m.group(1))].append(f)
    for num, files in sorted(by_number.items()):
        if len(files) > 1:
            errors.append(f"chapter {num:02d} has {len(files)} files: {[str(f) for f in files]}")
    return errors


def check_readme_links():
    errors = []
    readme = ROOT / "book" / "README.md"
    text = readme.read_text()
    # Matches lines like: 7. [Why Counting Is Not Enough](part-2-.../07-....md)
    link_re = re.compile(r"^\d+\.\s+\[([^\]]+)\]\(([^)]+)\)", re.MULTILINE)
    for title, path in link_re.findall(text):
        target = ROOT / "book" / path
        if not target.exists():
            errors.append(f"book/README.md links to '{path}' which does not exist")
            continue
        chapter_text = target.read_text()
        h1_match = re.search(r"^# (.+)$", chapter_text, re.MULTILINE)
        if not h1_match:
            errors.append(f"{path}: no '# Title' heading found")
            continue
        actual_title = h1_match.group(1).strip()
        if actual_title != title.strip():
            errors.append(
                f"book/README.md says '{title}' for {path}, but the file's H1 says '{actual_title}'"
            )
    return errors


def main():
    all_errors = []
    all_errors += check_one_file_per_chapter()
    all_errors += check_readme_links()

    if all_errors:
        print(f"{len(all_errors)} problem(s) found:\n")
        for e in all_errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("OK: one file per chapter, all book/README.md links and titles match.")


if __name__ == "__main__":
    main()
