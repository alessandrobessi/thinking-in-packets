# References — Chapter 15: Reliability Without Collapse

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 9293 §3.8 — TCP's flow-control (receive window) mechanism.
- RFC 5681 — *TCP Congestion Control*, IETF, 2009. Defines slow start, congestion avoidance, and the fast-retransmit/fast-recovery behavior generalized here as "backoff" — also the source for duplicate-acknowledgement-triggered fast retransmit as the primary loss-detection path, with RTO as fallback.
- RFC 6675 — *A Conservative Loss Recovery Algorithm Based on Selective Acknowledgment (SACK) for TCP*, IETF, 2012.
- RFC 3168 — *The Addition of Explicit Congestion Notification (ECN) to IP*, IETF, 2001.
- RFC 8087 — *The Benefits of Using Explicit Congestion Notification (ECN)*, IETF, 2017.

## Historical sources

- Van Jacobson's 1988 paper "Congestion Avoidance and Control" — the foundational work introducing the congestion-control mechanisms RFC 5681 later standardized, following the 1986 "congestion collapse" incidents on the early Internet.

## Implementation documentation

(none beyond the RFCs themselves)

## Empirical claims

- The chapter deliberately avoids claiming a precise, dated figure for what fraction of loss is congestion-caused versus other causes (wireless corruption, route changes, policing) — the qualitative point (TCP treats loss as a congestion signal by design, and that assumption is imperfect) is made without the overstated precision blueprint §19 warns against.

## Known simplifications (may need later technical review)

- Specific congestion-control algorithms (Reno, CUBIC, BBR) are not named or compared — the chapter stays at the flow-control-vs-congestion-control mechanism level per blueprint §5's exclusion of queueing-theory/algorithm-level detail.
- ECN is introduced only as "a way to signal congestion without loss" — its requirement for both endpoints and the network path to support it, and its interaction with the congestion window, are not covered.
