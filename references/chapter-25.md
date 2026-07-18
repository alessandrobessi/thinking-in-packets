# References — Chapter 25: Different Applications, Different Networks

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 3550 (*RTP: A Transport Protocol for Real-Time Applications*, 2003)
  — the standard underlying most real-time audio/video delivery,
  referenced conceptually for jitter-buffer behavior.
- RFC 8085 (*UDP Usage Guidelines*, 2017) — guidance for applications
  building their own reliability/timeliness trade-offs over UDP, relevant
  to this chapter's general approach without endorsing any one specific
  application protocol.

## Historical sources

- None specific to this chapter; the timeliness/completeness framing is
  a pedagogical synthesis (this book's own contribution) rather than a
  claim traceable to one primary source.

## Implementation documentation

- HTTP Live Streaming (Apple, publicly documented) and MPEG-DASH (an
  open ISO/IEC standard) are the two dominant real-world adaptive-
  bitrate approaches; referenced generically since the chapter
  deliberately stays vendor/standard-neutral at the concept level.

## Empirical claims

- None with specific numeric claims; all five worked-example applications
  are described qualitatively.

## Known simplifications (may need later technical review)

- Idempotency is introduced only at intuition level, without formal
  idempotency-key mechanics or HTTP-method-level idempotency semantics
  (safe/idempotent method classification from RFC 9110) — deliberately
  deferred as implementation detail per blueprint scope.
- Backpressure is described generically; specific mechanisms (TCP receive
  windows from Ch. 15, application-level queue limits) are not
  re-derived here, only connected conceptually.
