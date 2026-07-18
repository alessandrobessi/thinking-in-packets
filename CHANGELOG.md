# Changelog

Notable changes to the manuscript and its supporting project infrastructure.
Each chapter's own drafting pass should get an entry here.

## [Unreleased]

### Added

- Repository scaffolding: `blueprint.md` (local only, gitignored), `style-guide.md`,
  `glossary.md`, `misconceptions.md`, `concept-graph.yaml`/`concept-graph.md`,
  `templates/chapter-template.md`, `book/README.md`, `references/`, validation
  scripts, `.github/` workflows and issue templates, and the `publish/` Quarto
  project, following the same structure as the sibling project *Thinking in
  Tokens*.
- Full first-draft manuscript, Chapters 1–30 across all six parts
  (~63,100 words), each following the 11-section chapter template with
  inline Mermaid diagrams where the diagram policy calls for one.
  Concept-graph, glossary (227 terms), and misconception registry (38
  entries) fully populated and cross-checked; all four structural
  validators (`validate_concept_graph.py`, `validate_manuscript_index.py`,
  `validate_glossary_order.py`, `validate_diagram_references.py`) pass
  clean. Chapter-to-chapter narrative chaining verified verbatim across
  all 30 chapters.
- Cover art (`publish/assets/cover.png`, `cover-epub.png`), wired into
  `publish/_quarto.yml` (`cover-image`, `epub-cover-image`) and the Typst
  full-bleed cover page in `publish/typst-show.typ`. Author photo
  (`publish/assets/author.png`) reused from the sibling project
  *Thinking in Tokens* (same author) — all `publish/assets/` art now
  complete.
