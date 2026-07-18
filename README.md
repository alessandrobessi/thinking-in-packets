# Thinking in Packets

### A Mental Model for Computer Networks

A conceptual introduction to how computer networks actually work —
signals, frames, IP addressing, routing, TCP/UDP, DNS, TLS, HTTP,
performance, cloud and container networking, and production
troubleshooting — written for curious, technically-adjacent readers with
**no networking certification, no systems-programming background, and no
prior familiarity with the OSI model**.

Most introductions to networking begin with a stack of acronyms, a
seven-layer diagram, or a list of protocols to memorize. This project
takes the opposite approach: it builds one cumulative mental model,
beginning with the smallest possible problem — moving information
between two machines — and following that problem outward until it
becomes the Internet, the Web, cloud networking, container networking,
and production troubleshooting.

## Who this is for

Software developers who can build applications but find networking
opaque; DevOps, platform, and cloud practitioners who know commands but
want a deeper model; product managers, founders, consultants, and
technical leaders; cybersecurity and data professionals who need
networking foundations; students approaching distributed systems or cloud
computing; and lifelong learners who want to understand what actually
happens when one machine talks to another.

## What readers come away with

By the end, a reader should be able to explain, in order, what happens
when a browser opens an HTTPS website; distinguish a signal, frame,
packet, segment, and stream; explain what switches, routers, NAT devices,
firewalls, proxies, load balancers, and CDNs actually do; reason about
IPv4 and IPv6 together rather than treating IPv6 as an appendix; approach
an outage by narrowing the failing layer instead of guessing; and
evaluate claims like "zero trust" or "serverless networking" with
informed skepticism.

## A preview

Every chapter builds understanding through a story, a worked example, and
precise technical explanation, returns to one recurring scenario — a
laptop joining café Wi-Fi and opening an HTTPS website — and ends with one
bolded, memorable sentence that distills its core idea. From Chapter 9,
on routing:

> **A router forwards a packet by making one local next-hop decision from
> the most specific route it currently knows.**

See it in full context, with the story and worked example that build up
to it, in
[`09-one-hop-at-a-time.md`](book/part-2-building-an-internet/09-one-hop-at-a-time.md#key-takeaway).

## Status

**The full manuscript, Parts I–VI (Chapters 1–30), is written** —
From Signals to Local Networks, Building an Internet, End-to-End
Conversations, Names/Trust/the Web, Speed/Scale/Modern Protocols, and
Networks in Production. This is a first complete draft, not a finished,
fully-validated book — see "Editorial status and contributions" below.
See [`book/README.md`](book/README.md) for the full chapter-by-chapter
index, and [`concept-graph.md`](concept-graph.md) for per-concept
tracking.

## How the project is organized

| | |
|---|---|
| [`book/`](book/) | The manuscript itself, one file per chapter. Start at [`book/README.md`](book/README.md). |
| [`style-guide.md`](style-guide.md) | Voice conventions, diagram policy, and the analogy registry (so an analogy is never reinvented under a different name in a later chapter). |
| [`templates/chapter-template.md`](templates/chapter-template.md) | The 11-section template every chapter is drafted against. |
| [`glossary.md`](glossary.md) | Running index of every term, in order of first appearance. |
| [`misconceptions.md`](misconceptions.md) | The misconception graph: one row per concept, its common misconception, and the correct intuition. |
| [`concept-graph.md`](concept-graph.md) / [`concept-graph.yaml`](concept-graph.yaml) | Checklist tracker over the blueprint's 10-level (0–9) concept dependency graph — a concept may never appear in prose before its own level is checked off. The `.yaml` is the machine-readable source of truth; the `.md` is its generated, human-readable mirror. |
| [`references/`](references/) | Lightweight per-chapter citation trail for empirical/historical claims (RFCs, IEEE standards, vendor docs), plus a master `bibliography.md`. |
| [`scripts/`](scripts/) | `validate_concept_graph.py`, `validate_manuscript_index.py`, `validate_glossary_order.py`, and `validate_diagram_references.py` gate structural consistency; `generate_concept_graph_md.py` and `prepare_manuscript_for_publish.py` support the build. |
| [`publish/`](publish/) | A local Quarto book project rendering the manuscript to HTML, EPUB, and PDF. See "Building the book" below. |

## Building the book locally

Requires [Quarto](https://quarto.org) and [Typst](https://typst.app)
(`brew install --cask quarto && brew install typst`). All cover and
author art is in place (`publish/assets/`). From the repo root:

```sh
pip install -r requirements.txt
python3 scripts/prepare_manuscript_for_publish.py
cd publish && quarto render
```

Output lands in `publish/_book/` (an HTML site, an EPUB, and a PDF).
Nothing under `publish/chapters/` or `publish/_book/` is committed — both
are regenerated from `book/` on every run.

## Validating the manuscript

```sh
pip install -r requirements.txt
python3 scripts/validate_concept_graph.py
python3 scripts/validate_manuscript_index.py
python3 scripts/validate_glossary_order.py
python3 scripts/validate_diagram_references.py
```

## Editorial status and contributions

This is an early-stage, actively-drafted manuscript, not a finished book.
Expect factual claims, framing, and even structure to be revised as the
project gets feedback from real readers. If you spot a technical error, a
confusing explanation, or a broken internal link, please open an issue —
see [`CONTRIBUTING.md`](CONTRIBUTING.md) for what's useful to report right
now and what isn't yet being accepted.

## License

See [`LICENSE`](LICENSE) — currently a provisional, all-rights-reserved
placeholder. Do not assume any reuse rights based on its current state.
