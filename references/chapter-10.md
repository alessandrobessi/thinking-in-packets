# References — Chapter 10: Best Effort, Limits, and Failure Signals

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 792, *Internet Control Message Protocol* (ICMP), IETF, 1981.
- RFC 4443, *Internet Control Message Protocol (ICMPv6)*, IETF, 2006.
- RFC 791, *Internet Protocol* (source of the IPv4 TTL field and in-transit fragmentation behavior; already cited Ch. 6).
- RFC 8200, *Internet Protocol, Version 6* (source of the IPv6 Hop Limit field and the no-in-transit-fragmentation rule; already cited Ch. 6).
- RFC 1191, *Path MTU Discovery* (IPv4), IETF, 1990.
- RFC 8201, *Path MTU Discovery for IP version 6*, IETF, 2017.

## Historical sources

## Implementation documentation

- Common firewall/security-appliance documentation on ICMP filtering practices and their side effects on Path MTU Discovery — referenced narratively under Practical Implications.

## Empirical claims

## Known simplifications (may need later technical review)

- The chapter does not cover IPv4 fragmentation's specific security/performance drawbacks (a real, well-documented motivation for IPv6's design choice) in technical depth — only the behavioral difference itself.
- "Black-holed" Path MTU Discovery (where ICMP is filtered so thoroughly that neither fragmentation nor a proper error ever occurs) is mentioned only implicitly under Practical Implications, not as its own named failure mode.
