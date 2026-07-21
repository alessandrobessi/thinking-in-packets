# References — Chapter 24: Rebuilding Transport for the Modern Web

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 9000 (*QUIC: A UDP-Based Multiplexed and Secure Transport*, 2021) —
  the core QUIC specification: connection IDs, streams, connection
  migration.
- RFC 9001 (*Using TLS to Secure QUIC*, 2021) — how QUIC integrates TLS
  1.3 into its handshake.
- RFC 9002 (*QUIC Loss Detection and Congestion Control*, 2021) — QUIC's
  own congestion-control mechanism, referenced conceptually; also the
  source for this chapter's second-pass correction that loss detection
  operates on QUIC packet numbers at the connection level, with only
  stream *data* retransmission (via new STREAM frames) happening per
  affected stream.
- RFC 9000 §12.4 (*Frames and Frame Types*) — confirms multiple STREAM
  frames from different streams may be coalesced into one QUIC packet,
  the source for this chapter's correction that a lost packet can affect
  more than one stream.
- RFC 9114 (*HTTP/3*, 2022) — HTTP semantics carried over QUIC.
- RFC 9308 (*Applicability of the QUIC Transport Protocol*, 2022) §3 —
  notes user-space implementation as QUIC's common deployment pattern
  rather than a requirement of the specification itself, the source for
  this chapter's "commonly implemented as user-space" correction (a
  kernel-level QUIC implementation is possible and not excluded by RFC 9000).
- RFC 8446 (*TLS 1.3*, 2018) §8, *0-RTT and Anti-Replay* — the source for this chapter's 0-RTT replay-vulnerability correction: 0-RTT data lacks the forward-secrecy/freshness guarantee of data sent after a full handshake, so applications must restrict it to operations safe to (potentially) execute more than once.
- RFC 8446 §2.3, *0-RTT Data* — the source for this chapter's third-pass correction that 0-RTT early-data resumption is itself a TLS 1.3 capability, usable over plain TCP, not something QUIC invented by combining its handshake steps.
- RFC 9002 §5 (*Congestion Control*, already cited above) — the specific source for this chapter's third-pass correction that a stream being "not blocked" by an unrelated stream's loss is narrower than "unaffected": a shrinking connection-wide congestion window after loss can still reduce every stream's available sending rate.
- RFC 9000 §2 (*Streams*) — the source for this chapter's fourth-pass correction that QUIC provides independent per-stream *ordering and delivery*, not independent per-stream *loss recovery*; loss detection and retransmission scheduling remain connection-wide (RFC 9002), only the resulting stream data delivery is independent.

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
- Sixth-pass correction: the Packet-Journey Checkpoint previously said
  migration "lets that same QUIC connection continue uninterrupted,"
  which overstated an optional, negotiable capability. RFC 9000 §9
  (Connection Migration) and §9.6 (`disable_active_migration` transport
  parameter) establish that a peer can decline active migration, that
  migration requires path validation (§8.2) and a usable non-zero-length
  connection ID, and that congestion controller and RTT state are reset
  for the new path (§9.4) — so migration is a capability QUIC "can" use
  under the right conditions, not an unconditional guarantee, and can
  carry a brief performance cost even when it succeeds. The checkpoint
  now says "can preserve... provided both ends support it and the new
  path checks out," with the reset noted as a possible brief slowdown.
  The transport-parameter and path-validation mechanics themselves are
  not explained, per blueprint scope.
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
- The worked example's video-call scenario was revised (second review
  pass) so the diagram and prose no longer contradict the Technical
  Explanation's multi-stream-per-packet nuance; the underlying frame/
  packet-number accounting (RFC 9000 §13) is still not derived
  mechanically, per blueprint scope.
- Fifth-pass correction: two more instances of "independent loss
  recovery" survived earlier passes' fixes — one in the congestion-
  control misconception ("streams get independent loss recovery"), one
  in the HTTP/3-isn't-always-faster misconception's parenthetical list.
  Both now say "independent ordering and delivery" / "removing
  cross-stream head-of-line blocking," matching RFC 9000 §2's actual
  guarantee and the correction already applied elsewhere in this
  chapter — a reminder that fixing a phrase in one place doesn't fix it
  everywhere it was typed.
- Fifth-pass correction: the Packet-Journey Checkpoint's connection-
  migration example (Wi-Fi access-point handoff) didn't actually
  demonstrate the need for migration — roaming between access points on
  one network commonly keeps the same IP address, in which case an
  ordinary TCP connection survives too. Replaced with a Wi-Fi-to-
  cellular handoff, which genuinely changes the client's address.
- Fourth-pass deviation from blueprint.md §11: this chapter's Key
  Takeaway sentence has been edited from the blueprint's original
  verbatim wording ("...so it can evolve faster and isolate loss between
  application streams") to "...so it can evolve faster and keep one
  stream's loss from blocking delivery on unrelated streams," and drops
  "in user space" (already softened elsewhere in this chapter to
  "commonly implemented in user space," not a defining property). Three
  successive technical reviews converged on "isolate loss" as a
  persistent overclaim even after every surrounding section was
  corrected; leaving the chapter's single most memorable sentence
  technically imprecise while the rest of the chapter carefully hedges
  the same claim was judged worse than a one-sentence departure from
  verbatim blueprint wording. This is the only Key Takeaway in the
  manuscript altered from its blueprint source; style-guide.md §2's
  "match blueprint.md §11" rule should be read as taking a back seat to
  technical accuracy in cases like this one.
