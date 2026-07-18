# Changelog

Notable changes to the manuscript and its supporting project infrastructure.
Each chapter's own drafting pass should get an entry here.

## [Unreleased]

### Fixed

- Addressed a second-pass technical review's 9 remaining corrections
  across Chapters 10, 12, 16, 17, 19, 20, 22, 24, and 27: MTU redefined
  as the largest IP packet a link carries, not the largest frame, plus
  softening a residual "signals reliably arrive" overclaim (Ch. 10);
  broadened the socket definition to cover listening/unconnected
  sockets, and corrected "the reply finds its way to the browser tab"
  to stop at the process level (Ch. 12); scoped VPN-server visibility to
  metadata, not content still separately protected by an inner TLS
  layer (Ch. 16); corrected DNS delegation-chain caching so an expired
  answer doesn't imply a full root-to-authoritative re-walk (Ch. 17);
  relabeled HTTP as an application-layer protocol rather than a
  "transport-and-structure layer," and decoupled 403 from identity
  specifically (Ch. 19); scoped the page-load dependency chain to its
  conventional TCP-and-TLS path with a forward pointer to QUIC, and
  separated DNS's remote-address resolution from ARP/NDP's local
  next-hop resolution (Ch. 20); distinguished per-request vs.
  per-connection load-balancer granularity, and narrowed session
  affinity's actual guarantee (instance-local state for one user, not
  cross-replica consistency) (Ch. 22); fixed a residual contradiction
  where Chapter 24's worked example and diagram still claimed QUIC loss
  is always contained to one stream, reworded "independent
  loss-recovery state" to reflect connection-level loss detection with
  per-stream delivery, and softened "user-space transport" from a
  requirement to QUIC's common deployment pattern (Ch. 24); and
  corrected sidecar proxies to mediate a pod's traffic rather than one
  container's, and acknowledged sidecarless/ambient service-mesh
  architectures alongside the traditional sidecar model (Ch. 27). Also
  fixed a leftover "connection tuple" glossary reference missed by the
  first pass's rename to "five-tuple." Updated `glossary.md` and 9
  `references/chapter-NN.md` files with primary sources (RFC 1191, 894,
  9293, 768, 1034, 8446, RFC 9110 §§1/3, RFC 9000 §12.4/9308, Istio
  ambient-mode docs, cloud L4/L7 load-balancer docs) backing each
  correction. All four structural validators still pass clean.

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
