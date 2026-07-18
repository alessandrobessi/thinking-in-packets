#!/usr/bin/env python3
"""Validate inline Mermaid diagrams against blueprint.md §13's Diagram Policy.

Checks, per chapter file under book/:
1. At most two ```mermaid fenced code blocks (max two primary diagrams
   per chapter).
2. Every ```mermaid block is followed, within the next 3 non-blank lines,
   by an italic alt-text line matching "*Alt text: ...*" (every diagram
   must have alt text and a prose equivalent nearby).
3. The alt-text line is non-trivial (more than a few characters), so an
   empty "*Alt text:*" placeholder doesn't silently pass.

Exit code 0 if clean, 1 if any check fails.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MERMAID_BLOCK_RE = re.compile(r"```mermaid\n.*?\n```", re.DOTALL)
ALT_TEXT_RE = re.compile(r"^\*Alt text:\s*(.+?)\*\s*$")
MAX_DIAGRAMS_PER_CHAPTER = 2
MIN_ALT_TEXT_LENGTH = 15


def check_file(path):
    errors = []
    text = path.read_text()
    blocks = list(MERMAID_BLOCK_RE.finditer(text))

    if len(blocks) > MAX_DIAGRAMS_PER_CHAPTER:
        errors.append(
            f"{path.relative_to(ROOT)}: {len(blocks)} mermaid diagrams, "
            f"exceeds the max of {MAX_DIAGRAMS_PER_CHAPTER} per chapter"
        )

    for block in blocks:
        after = text[block.end():]
        # Look at the next few non-blank lines after the closing ``` fence.
        following_lines = [ln for ln in after.splitlines() if ln.strip()][:3]
        alt_line = next((ln for ln in following_lines if ALT_TEXT_RE.match(ln.strip())), None)
        if alt_line is None:
            snippet = text[max(0, block.start() - 40):block.start()].strip()
            errors.append(
                f"{path.relative_to(ROOT)}: mermaid block near \"...{snippet}\" has no "
                f"'*Alt text: ...*' line within 3 lines after it"
            )
            continue
        alt_content = ALT_TEXT_RE.match(alt_line.strip()).group(1).strip()
        if len(alt_content) < MIN_ALT_TEXT_LENGTH:
            errors.append(
                f"{path.relative_to(ROOT)}: alt text '{alt_content}' is too short "
                f"(< {MIN_ALT_TEXT_LENGTH} chars) to be a real description"
            )

    return errors


def main():
    all_errors = []
    for f in sorted(ROOT.glob("book/**/*.md")):
        if f.name == "README.md":
            continue
        all_errors += check_file(f)

    if all_errors:
        print(f"{len(all_errors)} problem(s) found:\n")
        for e in all_errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("OK: all diagrams are within limits and have paired alt text.")


if __name__ == "__main__":
    main()
