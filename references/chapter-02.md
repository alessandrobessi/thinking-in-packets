# References — Chapter 02: Turning Information Into Signals

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- IEEE 802.3 (Ethernet), current edition — physical-layer signaling and
  encoding over copper/fiber, underlying this chapter's "signal" and
  "encoding" concepts for wired links.
- IEEE 802.11 (Wi-Fi), current edition — radio-based physical-layer
  signaling, underlying this chapter's wireless "shared medium" framing
  (fully introduced in Chapter 4).

## Historical sources

- Claude E. Shannon, "A Mathematical Theory of Communication," *Bell
  System Technical Journal*, 1948 — foundational source for the
  bandwidth/noise/capacity relationship this chapter simplifies (the
  Shannon–Hartley theorem is not named or derived in-chapter, per
  blueprint.md's "not a mathematical treatment of information theory"
  scope note, §5).

## Implementation documentation

- Geostationary satellite link latency (~500-600 ms round trip,
  dominated by the ~44,700-mile round-trip distance at the speed of
  light) is a widely documented, physics-bound figure — see any current
  satellite ISP technical FAQ (e.g. Viasat, Hughesnet) for representative
  measured figures; this chapter's "roughly a quarter of a second" is a
  simplified, order-of-magnitude figure for one-way propagation, not a
  precise measured claim.

## Empirical claims

- Geostationary orbit altitude (~22,000 miles / ~35,786 km) — standard,
  stable physical constant, not dated.

## Known simplifications (may need later technical review)

- "Encoding" is described only at the conceptual level (an agreed scheme
  for representing bits as signal changes); no specific line-encoding
  scheme (e.g. 8b/10b, PAM4) is named, per blueprint.md's guidance to
  keep configuration/implementation detail out of the main text.
