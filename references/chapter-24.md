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

- 0-RTT resumption's replay-attack risk (a known, real security
  consideration for 0-RTT data) is not covered — the chapter stays at
  the "under specific conditions" intuition level per blueprint scope,
  deferring security nuance to avoid overclaiming 0-RTT as strictly
  better with no trade-off.
- QUIC congestion control is described as "conceptually similar in
  spirit" to TCP's without asserting a specific algorithm (e.g. CUBIC,
  BBR) is used, since QUIC implementations vary.
