# References — Chapter 08: Finding the Next Device

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 826, *An Ethernet Address Resolution Protocol* (ARP), IETF, 1982.
- RFC 4861, *Neighbor Discovery for IP version 6 (IPv6)*, IETF, 2007.
- RFC 5227, *IPv4 Address Conflict Detection*, IETF, 2008 (background on duplicate-address detection referenced briefly).

## Historical sources

## Implementation documentation

## Empirical claims

## Known simplifications (may need later technical review)

- ARP cache poisoning / spoofing (a real attack surface exploiting the trust ARP's broadcast-reply mechanism places in any responder) is not covered here — this chapter is scoped to normal operation; Chapter 28 covers network security more broadly.
- Gratuitous ARP and proxy ARP (used in some failover and virtualization designs) are out of scope as edge-case variants of the base mechanism described.
