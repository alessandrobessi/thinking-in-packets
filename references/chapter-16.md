# References — Chapter 16: The Network in the Middle

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 1918, *Address Allocation for Private Internets* — defines the private IPv4 ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16).
- RFC 2663, *IP Network Address Translator (NAT) Terminology and Considerations* — NAT/PAT terminology.
- RFC 3022, *Traditional IP Network Address Translator* — traditional NAT/NAPT behavior.
- RFC 3234, *Middleboxes: Taxonomy and Issues* — the general middlebox taxonomy this chapter's terminology follows.
- RFC 4787, *NAT Behavioral Requirements for Unicast UDP* — background on NAT mapping/filtering behavior (used only for general framing, not cited for configuration detail).
- RFC 6890, *Special-Purpose IP Address Registries* — catalogues loopback, link-local, documentation, and other special-purpose ranges that are neither private nor globally reachable public, the source for this chapter's correction away from a strict private/public binary.

## Historical sources

- The IPv4 address exhaustion pressure motivating widespread NAT deployment is discussed contemporaneously in RFC 1631 (the original 1994 NAT proposal, later obsoleted by RFC 3022).

## Implementation documentation

- Common home-router NAT/firewall behavior is described in vendor documentation (e.g. consumer router manuals); this chapter deliberately avoids citing any single vendor's configuration UI as authoritative.

## Empirical claims

- None with specific dated figures in this chapter; NAT/firewall/proxy prevalence is described qualitatively, not with adoption statistics.

## Known simplifications (may need later technical review)

- The chapter does not cover NAT traversal techniques (STUN/TURN/ICE) or the varying NAT mapping/filtering behaviors (full-cone, symmetric, etc.) — these are implementation-detail concerns beyond the chapter's mechanism-level scope.
- "Stateful firewall" is presented without distinguishing host-based vs. network firewalls or next-generation/application-layer firewall features — intentionally, per blueprint §5's exclusion of vendor-specific detail from the main text.
- The full IANA special-purpose address registry (benchmarking, multicast, unspecified, NAT64/DNS64 ranges, etc.) is not enumerated — the chapter names the pattern (private/public isn't exhaustive) without listing every range.
- Provider VPN technologies that separate traffic without encrypting it (e.g. some MPLS-based or GRE-only designs) are named only briefly, not explained mechanically — the chapter's detailed walkthrough still covers the common encrypted consumer/remote-access case.
