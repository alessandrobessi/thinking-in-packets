# Style Guide

Shared conventions for prose and voice across every chapter. This file is
written once and reused unchanged across all 30 chapters — do not fork
per-part variants. The only things that grow chapter by chapter are the
analogy registry (§3) and the diagram log implicit in each chapter's own
`## Diagram` sections.

Unlike the sibling project *Thinking in Tokens*, this book uses diagrams
selectively — see §4, Diagram Policy (from `blueprint.md` §13) — because
networking has spatial topology and temporal exchange patterns that prose
alone can make unnecessarily difficult. The manuscript must still remain
understandable without them.

---

## 1. Voice

- Write to an intelligent, curious, technically-adjacent reader — a
  developer, DevOps/platform engineer, product leader, student, or
  lifelong learner — who has no formal networking background. Never
  assume certification study, systems programming, electrical engineering,
  or command-line fluency.
- Intuition before terminology: introduce the idea in plain language,
  *then* attach the technical name to it, never the reverse.
- One load-bearing idea per chapter. A chapter may use several terms, but
  it must answer one central question (blueprint §7). If a paragraph needs
  a reader to hold two new mechanisms at once, split it.
- Every idea gets two concrete groundings before moving on — the opening
  story plus the worked example, at minimum (template §2/§3). One telling
  is a claim; a second telling from a different angle is what actually
  makes it stick.
- Prefer short, concrete sentences over qualified, abstract ones. Cut
  hedges.
- A technical explanation must still be *correct* — simplify by omitting
  detail, never by replacing the mechanism with a false statement
  (blueprint §7, "Precise simplification").
- No false anthropomorphism (blueprint §6.6): routers do not "know the
  Internet," DNS does not "know where every website lives." Whenever an
  explanation uses *knows*, *asks*, *trusts*, or *chooses*, the next
  sentence must identify the actual table, message, rule, state, or
  algorithm performing that function.
- Treat the network as fallible from the beginning (blueprint §6.4):
  packets may be lost, delayed, duplicated, reordered, corrupted,
  fragmented, filtered, or misrouted — these are the conditions under
  which networking was designed, not advanced exceptions.
- Reuse analogies deliberately (see §3, Analogy Registry). Introducing a
  new analogy for a concept that already has one elsewhere in the book is
  a bug, not a stylistic choice — check the registry before writing one.

## 2. Chapter Mechanics

- Every chapter must substantively cover all 11 elements of
  `templates/chapter-template.md`, in order, using the visible headers
  verbatim — this makes completeness trivial to verify chapter by chapter
  across a 30-chapter manuscript.
- §3 (Worked Example) is a second, fully-written concrete example distinct
  from the opening story, not a recap of it — it must expose the same
  mechanism from another angle (blueprint §7).
- §9 (Key Takeaway) is one bolded sentence, not a paragraph.
- Every chapter answers exactly one question from the Narrative Graph
  (`blueprint.md` §9) and ends by provoking the next. §11 of chapter N and
  §1 of chapter N+1 must express the same question, ideally verbatim.
- Never introduce a concept before its prerequisites (`blueprint.md` §10,
  Concept Dependency Graph). The test: does the sentence require the
  reader to already understand *how* the later concept works to parse it
  correctly? If yes, that's a violation, even if the concept's name is
  never used. A bare forward-pointer is fine ("that's the subject of
  Chapter 24") as long as no claim rests on the reader already grasping
  how it works.
- Teach IPv4 and IPv6 together wherever a mechanism has both (blueprint
  §6.2) — address/prefix notation, DHCP/SLAAC, ARP/Neighbor Discovery,
  private/global addressing, NAT pressure vs. translation's different
  role, A/AAAA records, fragmentation, TTL/Hop Limit. Do not relegate IPv6
  to a single "future protocol" chapter.
- Separate data plane, control plane, and management plane explicitly
  wherever the distinction is live (blueprint §6.5), but only once the
  reader has already encountered the underlying mechanism the terms name.
- After finishing a chapter, immediately: add its new terms to
  `glossary.md`, its misconceptions to `misconceptions.md`, check off its
  concepts in `concept-graph.yaml` (`written: true`, set `key_takeaway`)
  and regenerate `concept-graph.md`, add any new analogy to the registry
  below, and fill in its `references/chapter-NN.md` stub. Do this per
  chapter, not batched — batching is how these files silently drift.

## 3. Analogy Registry

One analogy per concept, reused everywhere that concept reappears. Check
this table before writing a new analogy — if the concept already has one,
reuse it. Seeded directly from `blueprint.md` §15; append a row only when
no existing analogy can carry a new concept without distortion.

| Analogy | Concept | First use | Important limit |
|---|---|---:|---|
| Texting a coworker across the desk, routed through distant infrastructure | Layered/indirect communication between endpoints | Ch. 1 | The office story is single-owner (one company's equipment); the real Internet's chain spans thousands of independently owned networks — a difference the chapter calls out explicitly. |
| One head office routing every regional matter, versus bounded regional offices | Scaling limits of a flat/unbounded network; need for internetworking | Ch. 5 | An organizational analogy for a technical scaling problem (broadcast domains, table growth, failure containment) — don't let it imply networking hierarchy is about management style rather than broadcast/failure/ownership costs. |
| Flashlight signals across a field | Physical encoding | Ch. 2 | Real links use much richer modulation and synchronization. |
| Continuous digits separated into groups | Framing | Ch. 3 | Frames are defined by protocol mechanisms, not human pauses. |
| Building mailroom and corridors | Switching | Ch. 4 | Switches learn from observed frames; they do not understand residents or content. |
| Hierarchical postal address | IP prefixes | Ch. 6 | IP routing is policy-driven and dynamic, not a fixed postal hierarchy. |
| Conference badge, room, map, help desk | Host configuration | Ch. 7 | DHCP and SLAAC are protocol exchanges, not a human authority assigning every fact. |
| Office number and door lookup | ARP or Neighbor Discovery | Ch. 8 | Resolution is link-local and does not find remote hosts. |
| Parcel-sorting center | Router forwarding | Ch. 9 | Internet routes are not necessarily physical shortest paths. |
| Independent railway companies | BGP and interdomain routing | Ch. 11 | Networks exchange reachability and policy, not complete timetables for every packet. |
| Apartment number inside a building | Ports | Ch. 12 | Ports identify transport endpoints, not users or permanent applications. |
| Postcards | UDP | Ch. 13 | UDP still uses checksums and may be part of a reliable higher-level protocol. |
| Numbered document pages | TCP reliability | Ch. 14 | TCP exposes bytes, not page-shaped application messages. |
| Warehouse capacity versus road congestion | Flow versus congestion control | Ch. 15 | Real congestion inference is algorithmic and probabilistic. |
| Company mailroom transformations | NAT, firewall, proxy, tunnel | Ch. 16 | The mechanisms differ sharply; the analogy must not merge them. |
| Delegated organizational directory | DNS | Ch. 17 | DNS is not merely a phonebook and supports many record types and policies. |
| Private conversation through a hostile courier | TLS | Ch. 18 | Cryptographic verification depends on keys, algorithms, and trust anchors. |
| Structured customer order | HTTP | Ch. 19 | HTTP is more general than commerce and can stream in both directions through extensions. |
| Highway width and travel distance | Bandwidth versus latency | Ch. 21 | Networks carry packets, not cars, and congestion dynamics differ. |
| Local warehouses and dispatchers | CDN and load balancing | Ch. 22 | Cached and dynamically generated work have different constraints. |
| Labeled orders sharing checkout lanes | Multiplexing | Ch. 23 | Shared lower-layer loss can still affect multiple logical streams. |
| Public roads vs. a privately run shuttle service | QUIC vs. TCP (user-space transport evolving independently of shared kernel infrastructure) | Ch. 24 | The shuttle still obeys traffic law and drives on the same roads — QUIC still rides on UDP and real network infrastructure, it hasn't escaped it. |
| A late newspaper, a late warning, a missing bank transfer | Differing application tolerance for delay vs. loss vs. completeness | Ch. 25 | The three failure severities are illustrative extremes; most real applications sit somewhere between them, not at one pole. |
| Transit maps over common streets | Overlays | Ch. 26 | Overlays consume underlay capacity and inherit its failures. |
| Stable reception number for moving workers | Container services | Ch. 27 | Service identity still depends on actively maintained control-plane state. |
| Controlled doors, not one wall | Zero trust, segmentation, and layered resilience vs. a single perimeter | Ch. 28 | Security is the combined property of many independent, modest measures, not any single strong control point. |
| Medical differential diagnosis | Troubleshooting | Ch. 29 | Network evidence can be incomplete, asymmetric, and altered by observation. |

(Table grows chapter by chapter; append immediately after finishing a
chapter that introduces a new analogy — see §2.)

## 4. Diagram Policy

From `blueprint.md` §13. Diagrams are inline **Mermaid** code blocks
embedded directly in chapter markdown (no separate image-rendering
pipeline — GitHub, Quarto, and most Markdown viewers render Mermaid
natively).

**Allowed diagram types:** topology (which components connect and where
boundaries sit), sequence (message order), encapsulation (what one layer
wraps around another's data), state snapshots (a small switch table,
route table, neighbor cache, NAT mapping, socket tuple), performance
timelines (where propagation, queueing, handshake, and processing time
accumulate).

**Rules:**

- Maximum two primary diagrams per chapter, placed within or immediately
  after §5 Technical Explanation.
- A diagram must teach one idea, not summarize the entire chapter.
- Every arrow must have a precise meaning; every boundary must be
  labeled.
- Do not combine topology and sequence into one crowded diagram.
- Do not reproduce protocol headers field by field unless one field is
  essential to the mechanism being taught.
- Every diagram must be immediately preceded or followed by a prose
  paragraph that carries the same idea unaided, plus a one-line
  italicized alt-text description (`*Alt text: ...*`) directly under the
  Mermaid block — `scripts/validate_diagram_references.py` checks for
  this pairing.
- IPv4-only diagrams require an explicit reason (a one-line note on why
  IPv6 isn't shown) — see §2's IPv4/IPv6 rule above.
- Most chapters need zero or one diagram, not two; add a second only when
  a single diagram would otherwise have to carry two unrelated ideas.
