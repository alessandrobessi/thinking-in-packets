#!/usr/bin/env python3
"""Validate concept-graph.yaml's internal consistency.

Checks:
1. Every prerequisite id actually exists as a concept.
2. No concept is introduced in a chapter earlier than any of its own
   prerequisites (the book's own "non-negotiable rule").
3. No dependency cycles.
4. Every misconception_id exists as a row in misconceptions.md.
5. written: true concepts have a chapter file that actually exists under
   book/, and that file has a heading whose GitHub-style anchor matches
   the concept's key_takeaway anchor (when set) -- not just that the file
   exists; written: false concepts should not have a key_takeaway set.
6. introduced_in is within the valid chapter range (1-30).

Exit code is 0 if clean, 1 if any check fails, so this can gate a commit.
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def load_concepts():
    data = yaml.safe_load((ROOT / "concept-graph.yaml").read_text())
    return data["concepts"]


def load_misconception_ids():
    text = (ROOT / "misconceptions.md").read_text()
    return set(re.findall(r"`([a-z0-9-]+)`", text))


def find_chapter_file(chapter_num):
    matches = list(ROOT.glob(f"book/**/{chapter_num:02d}-*.md"))
    return matches[0] if matches else None


def github_heading_slug(heading_text):
    """Approximate GitHub's Markdown heading-anchor algorithm: lowercase,
    drop anything that isn't a word character/space/hyphen, spaces -> hyphens."""
    slug = heading_text.strip().lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    return slug


def chapter_heading_anchors(chapter_file):
    text = chapter_file.read_text()
    return {github_heading_slug(h) for h in re.findall(r"^##\s+(.+)$", text, re.MULTILINE)}


def check_prerequisite_ids_exist(concepts, by_id):
    errors = []
    for c in concepts:
        for p in c["prerequisites"]:
            if p not in by_id:
                errors.append(f"{c['id']}: prerequisite '{p}' does not exist")
    return errors


def check_chapter_order(concepts, by_id):
    errors = []
    for c in concepts:
        for p in c["prerequisites"]:
            pre = by_id.get(p)
            if pre and pre["introduced_in"] > c["introduced_in"]:
                errors.append(
                    f"{c['id']} (ch{c['introduced_in']}) depends on "
                    f"{p} (ch{pre['introduced_in']}) -- introduced later"
                )
    return errors


def check_no_cycles(concepts, by_id):
    errors = []
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {c["id"]: WHITE for c in concepts}

    def visit(cid, path):
        color[cid] = GRAY
        for p in by_id[cid]["prerequisites"]:
            if color.get(p) == GRAY:
                errors.append(f"cycle: {' -> '.join(path + [cid, p])}")
            elif color.get(p) == WHITE:
                visit(p, path + [cid])
        color[cid] = BLACK

    for c in concepts:
        if color[c["id"]] == WHITE:
            visit(c["id"], [])
    return errors


def check_misconception_ids(concepts, known_ids):
    errors = []
    for c in concepts:
        for m in c.get("misconception_ids", []):
            if m not in known_ids:
                errors.append(f"{c['id']}: misconception_id '{m}' not found in misconceptions.md")
    return errors


def check_written_status(concepts):
    errors = []
    for c in concepts:
        chapter_file = find_chapter_file(c["introduced_in"])
        if c["written"]:
            if chapter_file is None:
                errors.append(f"{c['id']}: written=true but no chapter {c['introduced_in']:02d} file exists")
            elif c.get("key_takeaway"):
                anchor_file, _, anchor = c["key_takeaway"].partition("#")
                full_path = ROOT / anchor_file
                if not full_path.exists():
                    errors.append(f"{c['id']}: key_takeaway file '{anchor_file}' does not exist")
                elif anchor not in chapter_heading_anchors(full_path):
                    errors.append(
                        f"{c['id']}: key_takeaway anchor '#{anchor}' has no matching "
                        f"heading in '{anchor_file}'"
                    )
        else:
            if c.get("key_takeaway"):
                errors.append(f"{c['id']}: written=false but key_takeaway is set (should be null)")
    return errors


def check_chapter_range(concepts):
    errors = []
    for c in concepts:
        if not (1 <= c["introduced_in"] <= 30):
            errors.append(f"{c['id']}: introduced_in={c['introduced_in']} out of range 1-30")
    return errors


def main():
    concepts = load_concepts()
    by_id = {c["id"]: c for c in concepts}
    known_misconceptions = load_misconception_ids()

    all_errors = []
    all_errors += check_prerequisite_ids_exist(concepts, by_id)
    all_errors += check_chapter_order(concepts, by_id)
    all_errors += check_no_cycles(concepts, by_id)
    all_errors += check_misconception_ids(concepts, known_misconceptions)
    all_errors += check_written_status(concepts)
    all_errors += check_chapter_range(concepts)

    if all_errors:
        print(f"{len(all_errors)} problem(s) found:\n")
        for e in all_errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print(f"OK: {len(concepts)} concepts, no issues found.")


if __name__ == "__main__":
    main()
