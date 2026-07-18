# References — Chapter 03: Giving Bits Boundaries

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- IEEE 802.3 (Ethernet), current edition, §3 — defines the real Ethernet
  frame format (preamble, destination/source MAC, length/type, payload,
  Frame Check Sequence), which this chapter's fictional
  destination/source/length/payload/checksum frame deliberately
  simplifies without misstating the underlying pattern.
- IEEE 802.3, Frame Check Sequence (FCS) — the real-world CRC-32 checksum
  mechanism this chapter's "integrity check" trailer generalizes from.

## Historical sources

## Implementation documentation

- MDN Web Docs, "Ethernet frames, the ethertype and the 802.1Q tag" —
  accessible secondary explanation of real header field ordering, useful
  for verifying this chapter's simplified frame doesn't misstate the
  general header-then-payload-then-trailer structure.

## Empirical claims

## Known simplifications (may need later technical review)

- The worked example's frame format (destination, source, length,
  payload, integrity check) is fictional and simplified — no VLAN
  tagging, no preamble/start-frame-delimiter, no distinction between
  "length" and "EtherType" fields, per blueprint.md's guidance that
  protocol field detail belongs only when it reveals the mechanism.
- "Checksum" here is treated generically; the distinction between simple
  checksums and CRC (used by real Ethernet) is deferred as unnecessary
  detail for this chapter's purpose.
