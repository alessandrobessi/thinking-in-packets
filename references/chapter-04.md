# References — Chapter 04: Delivery Across One Local Network

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- IEEE 802.1D (MAC Bridges) — the standard formalizing switch/bridge
  learning and forwarding behavior this chapter's worked example
  dramatizes (learn source addresses from observed traffic; flood
  unknown destinations).
- IEEE 802-2014 — defines the 48-bit MAC address (EUI-48) format
  underlying this chapter's "MAC address" concept.
- IEEE 802.3 (Ethernet) and IEEE 802.11 (Wi-Fi) — the two link-layer
  technologies named in this chapter as delivering MAC-addressed frames
  over different physical media (Chapter 2).

## Historical sources

- Radia Perlman, *Interconnections: Bridges, Routers, Switches, and
  Internetworking Protocols*, 2nd ed. (Addison-Wesley, 2000) —
  authoritative secondary source on switch learning/flooding behavior and
  the switch-vs-router distinction this chapter's misconceptions section
  addresses.

## Implementation documentation

## Empirical claims

## Known simplifications (may need later technical review)

- MAC address randomization (used by many modern OSes for privacy on
  Wi-Fi) is mentioned only briefly in the misconceptions section as a
  reason MAC addresses aren't permanent identities; the mechanism itself
  is out of scope for this chapter.
- Spanning Tree Protocol (which prevents forwarding loops when switches
  are connected redundantly) is not introduced — the worked example uses
  a simple, loop-free two-switch topology deliberately.
