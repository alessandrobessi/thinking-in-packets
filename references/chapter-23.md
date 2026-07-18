# References — Chapter 23: Many Requests, Fewer Connections

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 9113 (*HTTP/2*, 2022, obsoletes RFC 7540) — the current HTTP/2
  specification, defining streams, multiplexing, and frame-level
  interleaving referenced conceptually in this chapter.
- RFC 7541 (*HPACK: Header Compression for HTTP/2*, 2015) — the specific
  header-compression mechanism this chapter describes at intuition level.
- RFC 2616 §8.1.2.2 (obsolete, historical) documented HTTP/1.1
  pipelining, which this chapter contrasts with true multiplexing.

## Historical sources

- SPDY, Google's experimental protocol (publicly documented starting
  2009), is the direct predecessor whose multiplexing design HTTP/2 was
  standardized from — noted here for historical accuracy though not
  covered in the chapter body, which stays protocol-neutral per
  blueprint §5's "mechanisms over protocol trivia" rule.

## Implementation documentation

- Browser networking documentation (e.g. Chrome DevTools' "Protocol"
  column, Firefox's about:networking) shows HTTP/2 stream multiplexing
  directly observable on real page loads.

## Empirical claims

- The "fifty or more resources" figure for a typical page is a rough,
  widely-cited order-of-magnitude figure from HTTP Archive-style page-
  weight studies rather than a precise measured constant; treated here as
  illustrative only.

## Known simplifications (may need later technical review)

- TCP head-of-line blocking is described qualitatively; no packet-loss
  probability math or specific retransmission-timeout mechanics are
  derived (those live conceptually in Chapter 15).
- Server push, a since-deprecated HTTP/2 feature, is deliberately omitted
  as it never became a durable mechanism worth building the chapter's
  model around.
