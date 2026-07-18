# Contributing

This is an actively-drafted manuscript, not a finished book, and not
primarily a code project — there is no build to run or tests to pass in
the ordinary sense (though `scripts/` does gate structural consistency).
The most valuable contribution right now is careful reading.

## What's useful

- **Technical corrections.** If a chapter states something that is
  factually wrong, outdated, or misleading about how computer networks
  actually work, open an issue using the "Technical correction" template.
- **Reader confusion.** If an explanation didn't land — an analogy that
  didn't click, a jump that felt too fast, a term used before it was
  defined — open an issue using the "Reader confusion" template. This
  book's whole premise is that every concept has an explicit prerequisite
  chain (see `concept-graph.md`); a confusion report that traces back to a
  missing prerequisite is exactly the signal this project needs.
- **Broken internal links** between chapters or to project files.

## What's not being accepted right now

- Full chapter rewrites or new chapters — the manuscript is being drafted
  sequentially against the concept dependency graph, and out-of-order
  contributions would violate that ordering.
- Structural changes to the book's own infrastructure (`style-guide.md`,
  `templates/chapter-template.md`, `concept-graph.md`/`.yaml`) without prior
  discussion — these are load-bearing for keeping 30 chapters consistent
  across multiple writing passes.

## Process

1. Check `glossary.md`, `misconceptions.md`, and `concept-graph.md` /
   `concept-graph.yaml` before reporting — your concern may already be
   tracked.
2. Open an issue with the relevant template.
3. For technical corrections, include a source if you have one — this
   project is trying to build a lightweight citation trail (see
   `references/`).
