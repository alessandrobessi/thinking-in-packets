# References — Chapter 15: Reliability Without Collapse

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 9293 §3.8 — TCP's flow-control (receive window) mechanism.
- RFC 5681 — *TCP Congestion Control*, IETF, 2009. Defines slow start, congestion avoidance, and the fast-retransmit/fast-recovery behavior generalized here as "backoff."

## Historical sources

- Van Jacobson's 1988 paper "Congestion Avoidance and Control" — the foundational work introducing the congestion-control mechanisms RFC 5681 later standardized, following the 1986 "congestion collapse" incidents on the early Internet.

## Implementation documentation

(none beyond the RFCs themselves)

## Empirical claims

- "The overwhelming majority of packet loss comes from congestion, not physical faults" is a widely accepted characterization in modern wired/data-center networking; a precise, dated figure is deliberately not cited here to avoid overstating precision blueprint §19 warns against.

## Known simplifications (may need later technical review)

- Specific congestion-control algorithms (Reno, CUBIC, BBR) are not named or compared — the chapter stays at the flow-control-vs-congestion-control mechanism level per blueprint §5's exclusion of queueing-theory/algorithm-level detail.
