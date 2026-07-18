# References — Chapter 24: Rebuilding Transport for the Modern Web

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 9000 (*QUIC: A UDP-Based Multiplexed and Secure Transport*, 2021) —
  the core QUIC specification: connection IDs, streams, connection
  migration.
- RFC 9001 (*Using TLS to Secure QUIC*, 2021) — how QUIC integrates TLS
  1.3 into its handshake.
- RFC 9002 (*QUIC Loss Detection and Congestion Control*, 2021) — QUIC's
  own congestion-control mechanism, referenced conceptually.
- RFC 9114 (*HTTP/3*, 2022) — HTTP semantics carried over QUIC.
- RFC 8446 (*TLS 1.3*, 2018) §8, *0-RTT and Anti-Replay* — the source for this chapter's 0-RTT replay-vulnerability correction: 0-RTT data lacks the forward-secrecy/freshness guarantee of data sent after a full handshake, so applications must restrict it to operations safe to (potentially) execute more than once.

## Historical sources

- QUIC originated as a Google experimental protocol (publicly documented
  from 2013) before IETF standardization completed in 2021 — noted for
  historical accuracy; the chapter itself describes the standardized
  protocol, not Google's original pre-standard variant.

## Implementation documentation

- Major browser and CDN engineering blogs documenting real-world QUIC/
  HTTP-3 deployment experience (connection migration on mobile networks,
  UDP-blocking fallback behavior) — cited generically since findings are
  vendor- and date-specific.

## Empirical claims

- The chapter's claim about some networks blocking or throttling UDP
  more aggressively than TCP reflects widely-documented middlebox
  behavior discussed in QUIC deployment literature; no specific
  prevalence percentage is asserted.

## Known simplifications (may need later technical review)

- 0-RTT resumption's replay-attack risk is named and its practical
  consequence (applications restrict which requests may use it) is
  stated, but the underlying cryptographic mechanics (session tickets,
  PSK binders, anti-replay windows) are not explained — intuition level
  only, per blueprint scope.
- QUIC congestion control is described as "conceptually similar in
  spirit" to TCP's without asserting a specific algorithm (e.g. CUBIC,
  BBR) is used, since QUIC implementations vary. Its connection-wide
  (not per-stream) scope is now stated explicitly per the technical
  review's correction, but the interaction between per-stream flow
  control and connection-wide congestion control is not derived in
  detail.
- The chapter notes that a single QUIC packet can carry frames from more
  than one stream (so loss isn't always perfectly contained to one
  stream) without describing QUIC's actual frame-packing/coalescing
  behavior mechanically — RFC 9000 §12.4 covers this in full.
