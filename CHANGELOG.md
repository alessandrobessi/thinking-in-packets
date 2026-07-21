# Changelog

Notable changes to the manuscript and its supporting project infrastructure.
Each chapter's own drafting pass should get an entry here.

## [Unreleased]

### Fixed

- Addressed a sixth-pass technical review's 6 remaining findings across
  Chapters 12, 24, and 27: fixed a stale "differs by client IP" sentence
  in Chapter 12's one-client-per-port misconception (still assumed
  distinct source IPs, false behind NAT); softened Chapter 24's QUIC
  connection-migration checkpoint from an unconditional "continue
  uninterrupted" to a capability ("can preserve... provided both ends
  support it and the new path checks out," noting a server can decline
  and a brief post-migration slowdown); and made three Chapter 27
  corrections — reframing east-west and ingress/egress as different
  dimensions (positional vs. directional-relative-to-a-named-boundary)
  rather than mutually exclusive labels, since a single internal call is
  east-west across the cluster *and* egress from its source pod *and*
  ingress to its destination pod at once (the old framing would have
  misled anyone writing Kubernetes NetworkPolicy, whose egress rules
  select internal destinations); removing an unsupported per-packet
  convergence timing guarantee ("forwarding rules already reflect it by
  the time the next packet arrives") in favor of "continuous but not
  instantaneous" with an explicit brief-window caveat; and fixing two
  residual all-meshes-have-sidecars phrasings plus the Ingress diagram
  label (the declared backend is a Service name/port, from which the
  controller obtains an address — not the address itself). Updated
  `glossary.md` (service discovery, from the fifth pass) and 2
  `references/chapter-NN.md` files with primary sources (RFC 9000 §9/§9.4/§9.6,
  Kubernetes NetworkPolicy docs) backing each correction. All four
  structural validators still pass clean.

- Addressed a fifth-pass technical review's 8 remaining findings across
  Chapters 12, 24, and 27, with an emphasis on consolidating rather than
  further qualifying (per the review's own editorial note that some
  passages were accumulating nested caveats): fixed two more stray
  "independent loss recovery" phrases in Chapter 24's misconceptions,
  and replaced its Packet-Journey Checkpoint's Wi-Fi-access-point-
  roaming migration example (roaming often keeps the same IP, so
  wouldn't need migration) with a genuine Wi-Fi-to-cellular handoff;
  rewrote Chapter 27's Ingress/service-discovery explanation from
  scratch rather than patching it further — Ingress configuration now
  correctly declares a service by *name*, not a resolved address; the
  chapter now distinguishes control-plane components (which watch
  service health and program forwarding rules) from the data plane
  (which just follows those rules per packet, doing no per-packet
  lookup), instead of describing the data plane as "consulting" service
  discovery directly; and the service-mesh Packet-Journey Checkpoint no
  longer assumes every mesh terminates external TLS at a sidecar,
  since that's a deployment choice, not a fixed property; fixed Chapter
  12's "each client has a different source IP" claim, false behind NAT,
  and its demultiplexing summary bullet, which still contradicted the
  chapter's own corrected body text; and corrected two wrong RFC 9293
  section citations in Chapter 12's references (§3.1 is TCP's header
  format, not connection identity — §3.4.1/§4 and §3.10.1 are correct).
  Updated `glossary.md` (service discovery) and 3
  `references/chapter-NN.md` files with primary sources (RFC 9293
  §3.4.1/§3.10.1, Kubernetes Ingress resource docs, ingress-nginx docs,
  Istio ingress-gateway docs) backing each correction, including a
  rationale entry for one prior suggestion (Chapter 27's "healthy" →
  "ready") that was reviewed again and still not adopted. All four
  structural validators still pass clean.

- Addressed a fourth-pass technical review's 6 remaining findings across
  Chapters 12, 20, 24, and 27: fixed a What to Remember bullet in
  Chapter 12 that still stated the exact "every transport-layer packet
  has ports" overgeneralization its own corrected body text had already
  removed, and softened the five-tuple's uniqueness claim to account for
  UDP's connectionless model (a five-tuple identifies one established
  connection precisely for TCP, but can carry more than one independent
  UDP exchange without anything having "ended" first); scoped Chapter
  20's "everything is encrypted and integrity-protected" after TLS setup
  to the HTTP data specifically, consistent with Chapter 18's own
  metadata-visibility treatment; replaced Chapter 24's two remaining
  "independent per-stream loss recovery" / "isolate loss between
  application streams" phrases (in the HTTP/3 paragraph, the diagram/
  footer description, and — after three review passes kept finding this
  exact phrase — the chapter's own Key Takeaway sentence, the one
  deliberate departure from blueprint.md's verbatim wording in the
  manuscript, documented as such in the chapter's references file) with
  language matching the corrected mechanism: independent stream
  *ordering and delivery*, not independent *loss recovery*; and reworked
  Chapter 27's Ingress worked example, technical explanation, diagram,
  and alt text to stop presenting one controller implementation
  (routing through a Service's virtual address) as the only path real
  ingress controllers take — some, like ingress-nginx, route straight to
  pod endpoints instead, bypassing the virtual address entirely. Updated
  `glossary.md` (five-tuple) and 4 `references/chapter-NN.md` files with
  primary sources (RFC 9293 §3.3.1, RFC 768 §2, RFC 9000 §2, ingress-nginx
  docs) backing each correction, including an explicit rationale entry
  for the Chapter 24 blueprint deviation and for declining one suggested
  "healthy"→"ready" terminology change in Chapter 27 (judged more
  Kubernetes-specific, not less, for a deliberately platform-agnostic
  chapter). All four structural validators still pass clean.

- Addressed a third-pass technical review's 8 remaining findings across
  Chapters 10, 12, 19, 20, 22, 24, and 27: IPv6's sending-endpoint
  fragmentation clarified as a real (if rarely used) capability via the
  Fragment extension header, not just packet-size avoidance (Ch. 10);
  scoped "every transport-layer packet has ports" to UDP/TCP
  specifically (ICMP has none), and corrected listening-socket
  demultiplexing to depend on port+protocol+local-address, not
  destination port alone (Ch. 12); replaced a still-identity-tied 403
  analogy ("recognizes your keycard") with one naming identity as only
  one possible refusal reason among several (Ch. 19); scoped
  "TLS must complete before HTTP" to a genuinely fresh connection, with
  a bare forward-pointer (no mechanism explained) noting TLS 1.3
  resumption lets a returning client send early data over plain TCP,
  independent of QUIC (Ch. 20); scoped "load balancing depends on
  replication" to load balancing across equivalent replicas specifically
  (Ch. 22); added the connection-wide congestion-window caveat QUIC's
  worked example, diagram, and What to Remember were still missing —
  "not blocked" by an unrelated stream's loss is narrower than "not
  affected," since a shrinking shared congestion window can still slow
  every stream's sending rate — and clarified 0-RTT resumption as a TLS
  1.3 capability QUIC reuses, not something QUIC invented (Ch. 24); and
  aligned Chapter 27's Service data-plane forwarding language with
  Chapter 22's own connection/flow-vs-request granularity distinction,
  removing an internal inconsistency between the two chapters (Ch. 27).
  Updated `glossary.md` (QUIC, independent streams, 0-RTT, demultiplexing,
  service discovery, service address entries) and 7
  `references/chapter-NN.md` files with primary sources (RFC 8446 §2.3,
  RFC 9002 §5, RFC 792, Kubernetes kube-proxy connection-tracking docs)
  backing each correction. All four structural validators still pass
  clean.

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
