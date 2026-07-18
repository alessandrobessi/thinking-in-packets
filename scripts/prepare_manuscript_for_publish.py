#!/usr/bin/env python3
"""Transform book/*.md into reader-facing copies for the Quarto build.

Each chapter file has three parts: a front-matter block (H1 title + bold
Part/Concept Level/Prerequisites/New concepts metadata), the body (11
numbered sections), and a footer bookkeeping block (glossary/
misconceptions/concept-graph notes), the last two separated by a "---"
rule. Only the title and body are reader-facing; the rest is authoring
scaffolding that keeps the supporting files in sync and was never meant
to be read.

Boundaries are found by anchoring on known markers (the first "---" rule
for the end of front matter, the footer's own distinctive bookkeeping
text for the start of the footer) rather than by counting "---"
occurrences -- a chapter that ever uses "---" as an in-prose rule
wouldn't silently miscount.

This script never touches book/ -- it writes stripped copies to
publish/chapters/, mirroring book/'s Part directory structure, for Quarto
to render. The output directory is cleared before each run so a renamed
or deleted source chapter can't leave a stale generated file behind.

    python3 scripts/prepare_manuscript_for_publish.py
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK_DIR = ROOT / "book"
OUT_DIR = ROOT / "publish" / "chapters"
FRONTMATTER_RULE = "\n---\n"
FOOTER_MARKER = "**Glossary terms added this chapter:**"


def strip_chapter(text: str, path: Path) -> str:
    first_rule = text.find(FRONTMATTER_RULE)
    if first_rule == -1:
        raise ValueError(f"{path}: no front-matter '---' rule found")
    frontmatter = text[:first_rule]
    rest = text[first_rule + len(FRONTMATTER_RULE):]

    footer_idx = rest.find(FOOTER_MARKER)
    if footer_idx == -1:
        raise ValueError(f"{path}: footer marker {FOOTER_MARKER!r} not found")
    # Trim the "---" rule that precedes the footer marker too.
    body = rest[:footer_idx].rsplit(FRONTMATTER_RULE, 1)[0]

    title_line = frontmatter.strip().splitlines()[0]
    return f"{title_line}\n\n{body.strip()}\n"


def main():
    chapter_files = sorted(BOOK_DIR.glob("part-*/*.md"))
    if not chapter_files:
        raise SystemExit(f"no chapter files found under {BOOK_DIR}")

    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)

    for src in chapter_files:
        part_dir = src.parent.name
        dest = OUT_DIR / part_dir / src.name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(strip_chapter(src.read_text(), src))
        print(f"wrote {dest.relative_to(ROOT)}")

    print(f"\n{len(chapter_files)} chapters prepared in {OUT_DIR.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
