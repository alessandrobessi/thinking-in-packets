# References — Chapter 14: Building a Reliable Stream

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 9293 — *Transmission Control Protocol (TCP)*, IETF, 2022. The current consolidated TCP specification, obsoleting the original RFC 793 (1981).

## Historical sources

- RFC 793 (1981) — original TCP specification, for historical grounding of the handshake/sequence-number design predating RFC 9293's consolidation.

## Implementation documentation

(none beyond the RFCs themselves)

## Empirical claims

(none)

## Known simplifications (may need later technical review)

- Selective acknowledgement (SACK, RFC 2018) is not covered — the chapter describes cumulative acknowledgement only, which is sufficient for the mechanism-level goal.
- Connection teardown (FIN/RST) is mentioned only implicitly ("formally closes it afterward"), not walked through step by step.
