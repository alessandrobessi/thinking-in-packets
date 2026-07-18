# References — Chapter 07: Joining a Network

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 2131, *Dynamic Host Configuration Protocol*, IETF, 1997.
- RFC 8415, *Dynamic Host Configuration Protocol for IPv6 (DHCPv6)*, IETF, 2018.
- RFC 4861, *Neighbor Discovery for IP version 6 (IPv6)*, IETF, 2007 (source for router advertisements referenced in-chapter).
- RFC 4862, *IPv6 Stateless Address Autoconfiguration*, IETF, 2007.

## Historical sources

## Implementation documentation

- Major OS vendor documentation (Android, iOS, Windows, major Linux distributions) on DHCP client behavior and IPv6 SLAAC/privacy-extension address generation (RFC 8981 covers the privacy-extension mechanism referenced in-chapter).

## Empirical claims

## Known simplifications (may need later technical review)

- The chapter describes SLAAC's duplicate-address detection only briefly as "a quick check," deferring the actual mechanism (Neighbor Solicitation) to Chapter 8.
- DHCP relay agents (for DHCP servers not on the same local network as the client) are out of scope — the chapter assumes a directly-reachable DHCP server, the common case on a small network like the café example.
