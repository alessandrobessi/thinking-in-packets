# Changelog

Notable changes to the manuscript and its supporting project infrastructure.
Each chapter's own drafting pass should get an entry here.

## [Unreleased]

### Fixed

- Addressed a technical review's 12 pre-publication corrections across
  Chapters 2, 7, 10, 12, 15, 16, 17/20, 19, 22, 24, 26, and 27: GEO
  satellite round-trip latency math (Ch. 2); SLAAC/DHCPv6 DNS delivery
  via RFC 8106 router-advertisement options (Ch. 7); silent,
  congestion-caused packet loss and ICMP's non-guaranteed delivery (Ch.
  10); standard "five-tuple" terminology and port-to-process binding
  nuance (Ch. 12); duplicate-ACK/SACK-based loss detection, non-congestion
  loss causes, and ECN (Ch. 15); the private/public address false binary
  and non-universal VPN encryption (Ch. 16); DNS's mandatory TCP support
  and encrypted-DNS transports (Ch. 17/20); GET/POST semantics and the
  401-vs-403 distinction (Ch. 19); propagation delay's fixed, non-per-byte
  nature (Ch. 22); QUIC's per-packet (not always per-stream) loss,
  connection-wide congestion control, and 0-RTT replay risk (Ch. 24);
  route tables vs. security-group permission (Ch. 26); and a substantial
  Kubernetes networking model rework in Ch. 27 (pod, not container, owns
  the network namespace; CNI is a plugin specification, not an interface;
  Services resolve to a virtual address with data-plane/EndpointSlice-style
  forwarding, not per-request discovery queries; headless services;
  east-west vs. egress; Ingress object vs. ingress controller). Updated
  `glossary.md` (+5 entries), `concept-graph.yaml` (+3 concepts), and 11
  `references/chapter-NN.md` files with the primary sources (RFC 8106,
  6890, 6675, 3168, 8087, 7766, 7858/8484/9250, 9110 §§9.3/15.5, 8446 §8,
  Kubernetes official docs) backing each correction. All four structural
  validators still pass clean.

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
