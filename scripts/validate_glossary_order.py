#!/usr/bin/env python3
"""Validate glossary.md: chapter order and coverage of new concepts.

Checks:
1. glossary.md's "First introduced" column is non-decreasing top to
   bottom (blueprint.md §21 item 6: "every introduced term appears in the
   glossary" implies the glossary reflects first-appearance order, not an
   arbitrary or alphabetical one).
2. Every "Ch. N" value parses to a valid chapter number (1-30).
3. Every chapter file's front-matter "New concepts introduced:" list has
   at least one glossary entry citing that same chapter (a weak coverage
   check -- exact term-matching is left to human review since the same
   idea is often phrased differently in the front matter vs. the
   glossary's one-line definition).

Exit code 0 if clean, 1 if any check fails.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_glossary_rows():
    text = (ROOT / "glossary.md").read_text()
    rows = []
    for line in text.splitlines():
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != 3 or cells[0] == "Term":
            continue
        rows.append(cells)
    return rows


def check_chapter_order(rows):
    errors = []
    last_chapter = 0
    for term, _definition, first_intro in rows:
        m = re.match(r"Ch\.\s*(\d+)", first_intro)
        if not m:
            errors.append(f"glossary.md: '{term}' has unparseable 'First introduced' value '{first_intro}'")
            continue
        chapter = int(m.group(1))
        if not (1 <= chapter <= 30):
            errors.append(f"glossary.md: '{term}' cites out-of-range chapter {chapter}")
        if chapter < last_chapter:
            errors.append(
                f"glossary.md: '{term}' (Ch. {chapter}) appears after a later-chapter "
                f"entry (Ch. {last_chapter}) -- glossary must stay in first-appearance order"
            )
        last_chapter = max(last_chapter, chapter)
    return errors


def check_new_concepts_coverage(rows):
    errors = []
    cited_chapters = set()
    for _term, _definition, first_intro in rows:
        m = re.match(r"Ch\.\s*(\d+)", first_intro)
        if m:
            cited_chapters.add(int(m.group(1)))

    for chapter_file in sorted(ROOT.glob("book/**/*.md")):
        if chapter_file.name == "README.md":
            continue
        m = re.match(r"(\d+)-", chapter_file.name)
        if not m:
            continue
        chapter_num = int(m.group(1))
        text = chapter_file.read_text()
        nc_match = re.search(r"\*\*New concepts introduced:\*\*\s*(.+)", text)
        if not nc_match:
            continue
        new_concepts = nc_match.group(1).strip()
        if new_concepts.lower().startswith("none") or new_concepts.lower().startswith("no major"):
            continue
        if chapter_num not in cited_chapters:
            errors.append(
                f"{chapter_file.relative_to(ROOT)}: front matter lists new concepts "
                f"but glossary.md has no 'Ch. {chapter_num}' entry"
            )
    return errors


def main():
    rows = load_glossary_rows()
    all_errors = []
    all_errors += check_chapter_order(rows)
    all_errors += check_new_concepts_coverage(rows)

    if all_errors:
        print(f"{len(all_errors)} problem(s) found:\n")
        for e in all_errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print(f"OK: {len(rows)} glossary entries, chapter order and coverage look consistent.")


if __name__ == "__main__":
    main()
