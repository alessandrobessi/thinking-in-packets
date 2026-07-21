# References — Chapter 10: Best Effort, Limits, and Failure Signals

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 792, *Internet Control Message Protocol* (ICMP), IETF, 1981.
- RFC 4443, *Internet Control Message Protocol (ICMPv6)*, IETF, 2006.
- RFC 791, *Internet Protocol* (source of the IPv4 TTL field and in-transit fragmentation behavior; already cited Ch. 6).
- RFC 8200, *Internet Protocol, Version 6* (source of the IPv6 Hop Limit field and the no-in-transit-fragmentation rule; already cited Ch. 6).
- RFC 1191, *Path MTU Discovery* (IPv4), IETF, 1990 — §1 defines MTU as a property of the largest IP datagram a link can carry, the source for this chapter's frame-vs-packet MTU correction.
- RFC 8201, *Path MTU Discovery for IP version 6*, IETF, 2017.
- RFC 894, *A Standard for the Transmission of IP Datagrams over Ethernet Networks* — illustrates that a 1500-byte Ethernet MTU describes the IP datagram's maximum size, with the Ethernet frame itself (header plus that payload) being correspondingly larger.
- RFC 4732, *Internet Denial-of-Service Considerations* §3 — background on ICMP rate-limiting as deliberate router/OS behavior, cited for this chapter's correction that ICMP generation is neither universal nor guaranteed to arrive.
- RFC 1812 §4.3.2.7 — router requirements around silently discarding packets under queue exhaustion, the source for this chapter's added third worked-example case (congestion-caused loss produces no ICMP message).
- RFC 791 §3.2 / RFC 8200 §4 (already cited above) — TTL/Hop Limit is defined and decremented per hop traversed, not per unit of elapsed time; the source for a compression-regression correction below.

## Historical sources

## Implementation documentation

- Common firewall/security-appliance documentation on ICMP filtering practices and their side effects on Path MTU Discovery — referenced narratively under Practical Implications.

## Empirical claims

## Known simplifications (may need later technical review)

- The chapter does not cover IPv4 fragmentation's specific security/performance drawbacks (a real, well-documented motivation for IPv6's design choice) in technical depth — only the behavioral difference itself.
- "Black-holed" Path MTU Discovery (where ICMP is filtered so thoroughly that neither fragmentation nor a proper error ever occurs) is mentioned only implicitly under Practical Implications, not as its own named failure mode.
- The chapter's correction (congestion-caused packet loss generates no ICMP message, and even well-defined ICMP cases can be rate-limited or filtered) stays qualitative — no specific rate-limiting thresholds or vendor defaults are cited, consistent with blueprint §19's caution against overstating precision.
- Compression-regression correction: the routing-loop worked example's phrase "a legitimate but slow-to-arrive packet" implied TTL expiry is chiefly about elapsed travel time, when it's actually a per-hop counter, indifferent to how long any individual hop took — corrected to name the hop-count mechanism explicitly. The Packet-Journey Checkpoint separately re-acquired an unqualified "would... report the failure back to the laptop," restating as fact the same ICMP-isn't-guaranteed point the Technical Explanation and Worked Example both already carefully hedge — corrected to distinguish the loop being bounded (reliable) from the sender being told why (not reliable), with an explicit pointer back to the Technical Explanation rather than re-arguing it.
