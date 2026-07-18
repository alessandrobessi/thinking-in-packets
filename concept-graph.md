# Concept Dependency Tracker

Checklist over the 10-level (0-9) Concept Dependency Graph in
blueprint.md §10. A concept is checked off once the chapter that
introduces it is written. No concept may be used in prose before its
own checkbox (or an earlier level's) is checked.

**This file is generated from [`concept-graph.yaml`](concept-graph.yaml) —
do not hand-edit it.** Run `python3 scripts/generate_concept_graph_md.py`
after any change to the YAML and commit both files together.

## Level 0 — Network, Endpoint, Message, Protocol, Intermediary, Failure, Layered cooperation

| Concept | Status | Chapter | Prerequisites | Misconceptions | Key Takeaway |
|---|---|---|---|---|---|
| Network | ✅ written | Ch. 1 | — | 1 | [link](book/part-1-signals-and-local-networks/01-the-invisible-journey.md#key-takeaway) |
| Endpoint | ✅ written | Ch. 1 | — | 0 | [link](book/part-1-signals-and-local-networks/01-the-invisible-journey.md#key-takeaway) |
| Message | ✅ written | Ch. 1 | — | 0 | [link](book/part-1-signals-and-local-networks/01-the-invisible-journey.md#key-takeaway) |
| Protocol | ✅ written | Ch. 1 | message | 0 | [link](book/part-1-signals-and-local-networks/01-the-invisible-journey.md#key-takeaway) |
| Intermediary | ✅ written | Ch. 1 | endpoint | 1 | [link](book/part-1-signals-and-local-networks/01-the-invisible-journey.md#key-takeaway) |
| Failure (as a normal condition) | ✅ written | Ch. 1 | — | 0 | [link](book/part-1-signals-and-local-networks/01-the-invisible-journey.md#key-takeaway) |
| Layered cooperation | ✅ written | Ch. 1 | protocol, intermediary | 0 | [link](book/part-1-signals-and-local-networks/01-the-invisible-journey.md#key-takeaway) |

## Level 1 — Bit, Signal, Encoding, Physical medium, Noise, Bandwidth, Propagation latency, Frame, Header/Payload, Checksum, Encapsulation

| Concept | Status | Chapter | Prerequisites | Misconceptions | Key Takeaway |
|---|---|---|---|---|---|
| Bit | ✅ written | Ch. 2 | message | 0 | [link](book/part-1-signals-and-local-networks/02-turning-information-into-signals.md#key-takeaway) |
| Signal | ✅ written | Ch. 2 | bit | 0 | [link](book/part-1-signals-and-local-networks/02-turning-information-into-signals.md#key-takeaway) |
| Encoding | ✅ written | Ch. 2 | signal | 0 | [link](book/part-1-signals-and-local-networks/02-turning-information-into-signals.md#key-takeaway) |
| Physical medium | ✅ written | Ch. 2 | signal | 0 | [link](book/part-1-signals-and-local-networks/02-turning-information-into-signals.md#key-takeaway) |
| Noise | ✅ written | Ch. 2 | signal | 0 | [link](book/part-1-signals-and-local-networks/02-turning-information-into-signals.md#key-takeaway) |
| Bandwidth | ✅ written | Ch. 2 | physical-medium | 1 | [link](book/part-1-signals-and-local-networks/02-turning-information-into-signals.md#key-takeaway) |
| Propagation latency | ✅ written | Ch. 2 | physical-medium | 1 | [link](book/part-1-signals-and-local-networks/02-turning-information-into-signals.md#key-takeaway) |
| Frame | ✅ written | Ch. 3 | bit, encoding | 0 | [link](book/part-1-signals-and-local-networks/03-giving-bits-boundaries.md#key-takeaway) |
| Header and payload | ✅ written | Ch. 3 | frame | 0 | [link](book/part-1-signals-and-local-networks/03-giving-bits-boundaries.md#key-takeaway) |
| Trailer | ✅ written | Ch. 3 | frame | 0 | [link](book/part-1-signals-and-local-networks/03-giving-bits-boundaries.md#key-takeaway) |
| Checksum / error detection | ✅ written | Ch. 3 | frame | 0 | [link](book/part-1-signals-and-local-networks/03-giving-bits-boundaries.md#key-takeaway) |
| Encapsulation | ✅ written | Ch. 3 | header-and-payload | 0 | [link](book/part-1-signals-and-local-networks/03-giving-bits-boundaries.md#key-takeaway) |

## Level 2 — Network interface, MAC address, Ethernet/Wi-Fi, Switch, Forwarding table, Broadcast domain, Failure domain, Internetwork

| Concept | Status | Chapter | Prerequisites | Misconceptions | Key Takeaway |
|---|---|---|---|---|---|
| Network interface | ✅ written | Ch. 4 | endpoint | 0 | [link](book/part-1-signals-and-local-networks/04-delivery-across-one-local-network.md#key-takeaway) |
| MAC address | ✅ written | Ch. 4 | network-interface, frame | 1 | [link](book/part-1-signals-and-local-networks/04-delivery-across-one-local-network.md#key-takeaway) |
| Ethernet and Wi-Fi | ✅ written | Ch. 4 | physical-medium, frame | 0 | [link](book/part-1-signals-and-local-networks/04-delivery-across-one-local-network.md#key-takeaway) |
| Shared medium | ✅ written | Ch. 4 | ethernet-wifi | 0 | [link](book/part-1-signals-and-local-networks/04-delivery-across-one-local-network.md#key-takeaway) |
| Switch | ✅ written | Ch. 4 | mac-address, ethernet-wifi | 1 | [link](book/part-1-signals-and-local-networks/04-delivery-across-one-local-network.md#key-takeaway) |
| Forwarding table (switch) | ✅ written | Ch. 4 | switch | 0 | [link](book/part-1-signals-and-local-networks/04-delivery-across-one-local-network.md#key-takeaway) |
| Broadcast | ✅ written | Ch. 4 | switch | 0 | [link](book/part-1-signals-and-local-networks/04-delivery-across-one-local-network.md#key-takeaway) |
| Broadcast domain | ✅ written | Ch. 5 | broadcast | 0 | [link](book/part-1-signals-and-local-networks/05-why-one-giant-network-does-not-work.md#key-takeaway) |
| Failure domain | ✅ written | Ch. 5 | broadcast-domain | 0 | [link](book/part-1-signals-and-local-networks/05-why-one-giant-network-does-not-work.md#key-takeaway) |
| Administrative boundary | ✅ written | Ch. 5 | broadcast-domain | 0 | [link](book/part-1-signals-and-local-networks/05-why-one-giant-network-does-not-work.md#key-takeaway) |
| Internetwork | ✅ written | Ch. 5 | broadcast-domain, administrative-boundary | 0 | [link](book/part-1-signals-and-local-networks/05-why-one-giant-network-does-not-work.md#key-takeaway) |

## Level 3 — IP packet, IPv4/IPv6 address, Prefix/subnet, DHCP, SLAAC, Default gateway, ARP, Neighbor Discovery, Address resolution

| Concept | Status | Chapter | Prerequisites | Misconceptions | Key Takeaway |
|---|---|---|---|---|---|
| IP packet | ✅ written | Ch. 6 | internetwork, header-and-payload | 0 | [link](book/part-2-building-an-internet/06-addresses-that-describe-where-to-route.md#key-takeaway) |
| IPv4 and IPv6 address | ✅ written | Ch. 6 | ip-packet | 1 | [link](book/part-2-building-an-internet/06-addresses-that-describe-where-to-route.md#key-takeaway) |
| Prefix and subnet | ✅ written | Ch. 6 | ipv4-ipv6-address | 1 | [link](book/part-2-building-an-internet/06-addresses-that-describe-where-to-route.md#key-takeaway) |
| Network and host portions | ✅ written | Ch. 6 | prefix-and-subnet | 0 | [link](book/part-2-building-an-internet/06-addresses-that-describe-where-to-route.md#key-takeaway) |
| Hierarchical address allocation | ✅ written | Ch. 6 | prefix-and-subnet | 0 | [link](book/part-2-building-an-internet/06-addresses-that-describe-where-to-route.md#key-takeaway) |
| Interface configuration | ✅ written | Ch. 7 | ipv4-ipv6-address, network-interface | 0 | [link](book/part-2-building-an-internet/07-joining-a-network.md#key-takeaway) |
| DHCP | ✅ written | Ch. 7 | interface-configuration | 0 | [link](book/part-2-building-an-internet/07-joining-a-network.md#key-takeaway) |
| SLAAC | ✅ written | Ch. 7 | interface-configuration | 0 | [link](book/part-2-building-an-internet/07-joining-a-network.md#key-takeaway) |
| Default gateway | ✅ written | Ch. 7 | interface-configuration | 0 | [link](book/part-2-building-an-internet/07-joining-a-network.md#key-takeaway) |
| DNS resolver address (local config) | ✅ written | Ch. 7 | interface-configuration | 0 | [link](book/part-2-building-an-internet/07-joining-a-network.md#key-takeaway) |
| Lease (DHCP) | ✅ written | Ch. 7 | dhcp | 0 | [link](book/part-2-building-an-internet/07-joining-a-network.md#key-takeaway) |
| Next hop | ✅ written | Ch. 8 | default-gateway | 0 | [link](book/part-2-building-an-internet/08-finding-the-next-device.md#key-takeaway) |
| Local-versus-remote decision | ✅ written | Ch. 8 | prefix-and-subnet, default-gateway | 0 | [link](book/part-2-building-an-internet/08-finding-the-next-device.md#key-takeaway) |
| ARP | ✅ written | Ch. 8 | mac-address, ipv4-ipv6-address, local-vs-remote-decision | 1 | [link](book/part-2-building-an-internet/08-finding-the-next-device.md#key-takeaway) |
| IPv6 Neighbor Discovery | ✅ written | Ch. 8 | mac-address, ipv4-ipv6-address, local-vs-remote-decision | 1 | [link](book/part-2-building-an-internet/08-finding-the-next-device.md#key-takeaway) |
| Neighbor/ARP cache | ✅ written | Ch. 8 | arp, neighbor-discovery | 0 | [link](book/part-2-building-an-internet/08-finding-the-next-device.md#key-takeaway) |
| Address resolution (general) | ✅ written | Ch. 8 | arp, neighbor-discovery | 0 | [link](book/part-2-building-an-internet/08-finding-the-next-device.md#key-takeaway) |

## Level 4 — Router, Routing table, Longest-prefix match, Data plane, Best-effort delivery, TTL/Hop Limit, ICMP, MTU, Fragmentation, Autonomous systems, BGP, Control plane

| Concept | Status | Chapter | Prerequisites | Misconceptions | Key Takeaway |
|---|---|---|---|---|---|
| Router | ✅ written | Ch. 9 | next-hop, switch | 1 | [link](book/part-2-building-an-internet/09-one-hop-at-a-time.md#key-takeaway) |
| Routing table | ✅ written | Ch. 9 | router | 0 | [link](book/part-2-building-an-internet/09-one-hop-at-a-time.md#key-takeaway) |
| Longest-prefix matching | ✅ written | Ch. 9 | routing-table, prefix-and-subnet | 0 | [link](book/part-2-building-an-internet/09-one-hop-at-a-time.md#key-takeaway) |
| Default route | ✅ written | Ch. 9 | routing-table | 0 | [link](book/part-2-building-an-internet/09-one-hop-at-a-time.md#key-takeaway) |
| Data plane | ✅ written | Ch. 9 | router | 1 | [link](book/part-2-building-an-internet/09-one-hop-at-a-time.md#key-takeaway) |
| Best-effort delivery | ✅ written | Ch. 10 | ip-packet | 1 | [link](book/part-2-building-an-internet/10-best-effort-limits-and-failure-signals.md#key-takeaway) |
| TTL and Hop Limit | ✅ written | Ch. 10 | best-effort-delivery, routing-table | 0 | [link](book/part-2-building-an-internet/10-best-effort-limits-and-failure-signals.md#key-takeaway) |
| ICMP | ✅ written | Ch. 10 | best-effort-delivery | 0 | [link](book/part-2-building-an-internet/10-best-effort-limits-and-failure-signals.md#key-takeaway) |
| MTU | ✅ written | Ch. 10 | frame, ip-packet | 0 | [link](book/part-2-building-an-internet/10-best-effort-limits-and-failure-signals.md#key-takeaway) |
| Path MTU discovery | ✅ written | Ch. 10 | mtu, icmp | 0 | [link](book/part-2-building-an-internet/10-best-effort-limits-and-failure-signals.md#key-takeaway) |
| Fragmentation | ✅ written | Ch. 10 | mtu | 0 | [link](book/part-2-building-an-internet/10-best-effort-limits-and-failure-signals.md#key-takeaway) |
| Packet loss | ✅ written | Ch. 10 | best-effort-delivery | 0 | [link](book/part-2-building-an-internet/10-best-effort-limits-and-failure-signals.md#key-takeaway) |
| Autonomous system | ✅ written | Ch. 11 | routing-table, administrative-boundary | 1 | [link](book/part-3-end-to-end-conversations/11-the-internet-is-a-network-of-networks.md#key-takeaway) |
| ISP | ✅ written | Ch. 11 | autonomous-system | 0 | [link](book/part-3-end-to-end-conversations/11-the-internet-is-a-network-of-networks.md#key-takeaway) |
| Peering and transit | ✅ written | Ch. 11 | autonomous-system | 0 | [link](book/part-3-end-to-end-conversations/11-the-internet-is-a-network-of-networks.md#key-takeaway) |
| Route advertisement | ✅ written | Ch. 11 | autonomous-system, routing-table | 0 | [link](book/part-3-end-to-end-conversations/11-the-internet-is-a-network-of-networks.md#key-takeaway) |
| Control plane | ✅ written | Ch. 11 | data-plane, route-advertisement | 0 | [link](book/part-3-end-to-end-conversations/11-the-internet-is-a-network-of-networks.md#key-takeaway) |
| BGP | ✅ written | Ch. 11 | route-advertisement, peering-and-transit | 1 | [link](book/part-3-end-to-end-conversations/11-the-internet-is-a-network-of-networks.md#key-takeaway) |
| Routing policy | ✅ written | Ch. 11 | bgp | 0 | [link](book/part-3-end-to-end-conversations/11-the-internet-is-a-network-of-networks.md#key-takeaway) |
| Route convergence | ✅ written | Ch. 11 | bgp | 0 | [link](book/part-3-end-to-end-conversations/11-the-internet-is-a-network-of-networks.md#key-takeaway) |

## Level 5 — Process/port, Socket, UDP, TCP, Handshake, Sequence numbers/acknowledgement, Retransmission, Flow control, Congestion control

| Concept | Status | Chapter | Prerequisites | Misconceptions | Key Takeaway |
|---|---|---|---|---|---|
| Process and port | ✅ written | Ch. 12 | endpoint, ip-packet | 1 | [link](book/part-3-end-to-end-conversations/12-from-a-host-to-a-process.md#key-takeaway) |
| Socket and connection tuple | ✅ written | Ch. 12 | process-and-port, ipv4-ipv6-address | 0 | [link](book/part-3-end-to-end-conversations/12-from-a-host-to-a-process.md#key-takeaway) |
| Multiplexing (transport-layer) | ✅ written | Ch. 12 | socket | 0 | [link](book/part-3-end-to-end-conversations/12-from-a-host-to-a-process.md#key-takeaway) |
| UDP | ✅ written | Ch. 13 | socket | 1 | [link](book/part-3-end-to-end-conversations/13-sending-independent-datagrams.md#key-takeaway) |
| Datagram | ✅ written | Ch. 13 | udp | 0 | [link](book/part-3-end-to-end-conversations/13-sending-independent-datagrams.md#key-takeaway) |
| Connectionless communication | ✅ written | Ch. 13 | udp | 0 | [link](book/part-3-end-to-end-conversations/13-sending-independent-datagrams.md#key-takeaway) |
| Application-managed reliability | ✅ written | Ch. 13 | connectionless-communication | 0 | [link](book/part-3-end-to-end-conversations/13-sending-independent-datagrams.md#key-takeaway) |
| TCP | ✅ written | Ch. 14 | socket, best-effort-delivery | 1 | [link](book/part-3-end-to-end-conversations/14-building-a-reliable-stream.md#key-takeaway) |
| TCP handshake | ✅ written | Ch. 14 | tcp | 0 | [link](book/part-3-end-to-end-conversations/14-building-a-reliable-stream.md#key-takeaway) |
| Byte stream | ✅ written | Ch. 14 | tcp | 1 | [link](book/part-3-end-to-end-conversations/14-building-a-reliable-stream.md#key-takeaway) |
| Sequence numbers and acknowledgement | ✅ written | Ch. 14 | byte-stream | 0 | [link](book/part-3-end-to-end-conversations/14-building-a-reliable-stream.md#key-takeaway) |
| Retransmission | ✅ written | Ch. 14 | sequence-and-ack | 1 | [link](book/part-3-end-to-end-conversations/14-building-a-reliable-stream.md#key-takeaway) |
| Ordering and duplicate detection | ✅ written | Ch. 14 | sequence-and-ack | 0 | [link](book/part-3-end-to-end-conversations/14-building-a-reliable-stream.md#key-takeaway) |
| Flow control / receive window | ✅ written | Ch. 15 | byte-stream | 1 | [link](book/part-3-end-to-end-conversations/15-reliability-without-collapse.md#key-takeaway) |
| Congestion control / congestion window | ✅ written | Ch. 15 | flow-control, packet-loss | 1 | [link](book/part-3-end-to-end-conversations/15-reliability-without-collapse.md#key-takeaway) |
| Acknowledgement clocking | ✅ written | Ch. 15 | congestion-control | 0 | [link](book/part-3-end-to-end-conversations/15-reliability-without-collapse.md#key-takeaway) |
| Retransmission timeout | ✅ written | Ch. 15 | retransmission | 0 | [link](book/part-3-end-to-end-conversations/15-reliability-without-collapse.md#key-takeaway) |
| Fairness and backoff | ✅ written | Ch. 15 | congestion-control | 0 | [link](book/part-3-end-to-end-conversations/15-reliability-without-collapse.md#key-takeaway) |

## Level 6 — Private/public addressing, NAT, Firewalls, Proxies, VPN, DNS, TLS, HTTP

| Concept | Status | Chapter | Prerequisites | Misconceptions | Key Takeaway |
|---|---|---|---|---|---|
| Private and public addressing | ✅ written | Ch. 16 | ipv4-ipv6-address | 0 | [link](book/part-4-names-trust-and-the-web/16-the-network-in-the-middle.md#key-takeaway) |
| NAT and port translation | ✅ written | Ch. 16 | private-public-address, process-and-port | 2 | [link](book/part-4-names-trust-and-the-web/16-the-network-in-the-middle.md#key-takeaway) |
| Stateful firewall | ✅ written | Ch. 16 | socket | 1 | [link](book/part-4-names-trust-and-the-web/16-the-network-in-the-middle.md#key-takeaway) |
| Forward and reverse proxy | ✅ written | Ch. 16 | tcp | 0 | [link](book/part-4-names-trust-and-the-web/16-the-network-in-the-middle.md#key-takeaway) |
| VPN tunnel | ✅ written | Ch. 16 | encapsulation, tcp | 1 | [link](book/part-4-names-trust-and-the-web/16-the-network-in-the-middle.md#key-takeaway) |
| Middlebox | ✅ written | Ch. 16 | nat, stateful-firewall, proxy | 0 | [link](book/part-4-names-trust-and-the-web/16-the-network-in-the-middle.md#key-takeaway) |
| Domain name | ✅ written | Ch. 17 | ipv4-ipv6-address | 0 | [link](book/part-4-names-trust-and-the-web/17-naming-a-moving-world.md#key-takeaway) |
| DNS hierarchy, root, TLD | ✅ written | Ch. 17 | domain-name, hierarchical-allocation | 1 | [link](book/part-4-names-trust-and-the-web/17-naming-a-moving-world.md#key-takeaway) |
| Authoritative and recursive resolvers | ✅ written | Ch. 17 | dns-hierarchy | 1 | [link](book/part-4-names-trust-and-the-web/17-naming-a-moving-world.md#key-takeaway) |
| DNS delegation | ✅ written | Ch. 17 | dns-hierarchy | 0 | [link](book/part-4-names-trust-and-the-web/17-naming-a-moving-world.md#key-takeaway) |
| DNS record types (A, AAAA, CNAME) | ✅ written | Ch. 17 | dns-hierarchy | 0 | [link](book/part-4-names-trust-and-the-web/17-naming-a-moving-world.md#key-takeaway) |
| DNS caching and TTL | ✅ written | Ch. 17 | authoritative-recursive-resolver | 1 | [link](book/part-4-names-trust-and-the-web/17-naming-a-moving-world.md#key-takeaway) |
| Encryption, integrity, authentication | ✅ written | Ch. 18 | message | 0 | [link](book/part-4-names-trust-and-the-web/18-establishing-trust-on-an-untrusted-network.md#key-takeaway) |
| Certificate and certificate authority | ✅ written | Ch. 18 | encryption-integrity-authentication | 1 | [link](book/part-4-names-trust-and-the-web/18-establishing-trust-on-an-untrusted-network.md#key-takeaway) |
| Key exchange | ✅ written | Ch. 18 | encryption-integrity-authentication | 0 | [link](book/part-4-names-trust-and-the-web/18-establishing-trust-on-an-untrusted-network.md#key-takeaway) |
| TLS session | ✅ written | Ch. 18 | certificate-and-ca, key-exchange, tcp | 1 | [link](book/part-4-names-trust-and-the-web/18-establishing-trust-on-an-untrusted-network.md#key-takeaway) |
| URL | ✅ written | Ch. 19 | domain-name | 0 | [link](book/part-4-names-trust-and-the-web/19-the-language-of-the-web.md#key-takeaway) |
| HTTP request and response | ✅ written | Ch. 19 | url, tls-session | 1 | [link](book/part-4-names-trust-and-the-web/19-the-language-of-the-web.md#key-takeaway) |
| HTTP method, status code, header, body | ✅ written | Ch. 19 | http-request-response | 0 | [link](book/part-4-names-trust-and-the-web/19-the-language-of-the-web.md#key-takeaway) |
| Cookie and session (HTTP) | ✅ written | Ch. 19 | http-request-response | 0 | [link](book/part-4-names-trust-and-the-web/19-the-language-of-the-web.md#key-takeaway) |
| Stateless protocol | ✅ written | Ch. 19 | http-request-response | 1 | [link](book/part-4-names-trust-and-the-web/19-the-language-of-the-web.md#key-takeaway) |

## Level 7 — Throughput, Latency components, Jitter, Caching, CDN, Load balancing, HTTP/2, QUIC, HTTP/3, Real-time media trade-offs

| Concept | Status | Chapter | Prerequisites | Misconceptions | Key Takeaway |
|---|---|---|---|---|---|
| Throughput | ✅ written | Ch. 21 | bandwidth | 1 | [link](book/part-5-speed-scale-and-modern-protocols/21-where-time-goes.md#key-takeaway) |
| Serialization delay | ✅ written | Ch. 21 | bandwidth | 0 | [link](book/part-5-speed-scale-and-modern-protocols/21-where-time-goes.md#key-takeaway) |
| Processing and queueing delay | ✅ written | Ch. 21 | router | 0 | [link](book/part-5-speed-scale-and-modern-protocols/21-where-time-goes.md#key-takeaway) |
| Round-trip time | ✅ written | Ch. 21 | propagation-latency, serialization-delay | 0 | [link](book/part-5-speed-scale-and-modern-protocols/21-where-time-goes.md#key-takeaway) |
| Jitter | ✅ written | Ch. 21 | round-trip-time | 0 | [link](book/part-5-speed-scale-and-modern-protocols/21-where-time-goes.md#key-takeaway) |
| Buffering and bufferbloat | ✅ written | Ch. 21 | processing-and-queueing-delay | 1 | [link](book/part-5-speed-scale-and-modern-protocols/21-where-time-goes.md#key-takeaway) |
| Caching | ✅ written | Ch. 22 | http-request-response | 0 | [link](book/part-5-speed-scale-and-modern-protocols/22-bringing-services-closer-and-spreading-the-work.md#key-takeaway) |
| CDN and edge location | ✅ written | Ch. 22 | caching, dns-hierarchy | 1 | [link](book/part-5-speed-scale-and-modern-protocols/22-bringing-services-closer-and-spreading-the-work.md#key-takeaway) |
| Load balancer | ✅ written | Ch. 22 | socket | 0 | [link](book/part-5-speed-scale-and-modern-protocols/22-bringing-services-closer-and-spreading-the-work.md#key-takeaway) |
| Health check | ✅ written | Ch. 22 | load-balancer | 0 | [link](book/part-5-speed-scale-and-modern-protocols/22-bringing-services-closer-and-spreading-the-work.md#key-takeaway) |
| Replication and session affinity | ✅ written | Ch. 22 | load-balancer | 0 | [link](book/part-5-speed-scale-and-modern-protocols/22-bringing-services-closer-and-spreading-the-work.md#key-takeaway) |
| Connection reuse | ✅ written | Ch. 23 | tcp-handshake | 0 | [link](book/part-5-speed-scale-and-modern-protocols/23-many-requests-fewer-connections.md#key-takeaway) |
| Stream multiplexing (HTTP/2) | ✅ written | Ch. 23 | connection-reuse, http-request-response | 1 | [link](book/part-5-speed-scale-and-modern-protocols/23-many-requests-fewer-connections.md#key-takeaway) |
| Header compression | ✅ written | Ch. 23 | multiplexing-http2 | 0 | [link](book/part-5-speed-scale-and-modern-protocols/23-many-requests-fewer-connections.md#key-takeaway) |
| Head-of-line blocking | ✅ written | Ch. 23 | multiplexing-http2, byte-stream | 0 | [link](book/part-5-speed-scale-and-modern-protocols/23-many-requests-fewer-connections.md#key-takeaway) |
| QUIC | ✅ written | Ch. 24 | udp, tls-session, head-of-line-blocking | 1 | [link](book/part-5-speed-scale-and-modern-protocols/24-rebuilding-transport-for-the-modern-web.md#key-takeaway) |
| HTTP/3 | ✅ written | Ch. 24 | quic, multiplexing-http2 | 0 | [link](book/part-5-speed-scale-and-modern-protocols/24-rebuilding-transport-for-the-modern-web.md#key-takeaway) |
| Connection migration (QUIC connection ID) | ✅ written | Ch. 24 | quic | 0 | [link](book/part-5-speed-scale-and-modern-protocols/24-rebuilding-transport-for-the-modern-web.md#key-takeaway) |
| Zero-round-trip resumption (intuition) | ✅ written | Ch. 24 | quic | 0 | [link](book/part-5-speed-scale-and-modern-protocols/24-rebuilding-transport-for-the-modern-web.md#key-takeaway) |
| Timeliness vs. completeness | ✅ written | Ch. 25 | udp, tcp | 0 | [link](book/part-5-speed-scale-and-modern-protocols/25-different-applications-different-networks.md#key-takeaway) |
| Jitter buffer | ✅ written | Ch. 25 | jitter, timeliness-vs-completeness | 0 | [link](book/part-5-speed-scale-and-modern-protocols/25-different-applications-different-networks.md#key-takeaway) |
| Adaptive bitrate | ✅ written | Ch. 25 | timeliness-vs-completeness | 0 | [link](book/part-5-speed-scale-and-modern-protocols/25-different-applications-different-networks.md#key-takeaway) |
| Real-time media trade-offs | ✅ written | Ch. 25 | jitter-buffer, adaptive-bitrate | 0 | [link](book/part-5-speed-scale-and-modern-protocols/25-different-applications-different-networks.md#key-takeaway) |
| Backpressure | ✅ written | Ch. 25 | flow-control | 0 | [link](book/part-5-speed-scale-and-modern-protocols/25-different-applications-different-networks.md#key-takeaway) |

## Level 8 — Virtual interfaces, Tunnels/overlays, Software-defined networking, Cloud VPCs, Container namespaces, Service discovery, Service mesh

| Concept | Status | Chapter | Prerequisites | Misconceptions | Key Takeaway |
|---|---|---|---|---|---|
| Virtual interface | ✅ written | Ch. 26 | network-interface | 0 | [link](book/part-6-networks-in-production/26-networks-made-of-software.md#key-takeaway) |
| Bridge (virtual) | ✅ written | Ch. 26 | virtual-interface, switch | 0 | [link](book/part-6-networks-in-production/26-networks-made-of-software.md#key-takeaway) |
| Tunnel and overlay | ✅ written | Ch. 26 | encapsulation, virtual-interface | 0 | [link](book/part-6-networks-in-production/26-networks-made-of-software.md#key-takeaway) |
| Underlay vs. overlay | ✅ written | Ch. 26 | tunnel-and-overlay | 1 | [link](book/part-6-networks-in-production/26-networks-made-of-software.md#key-takeaway) |
| Software-defined networking | ✅ written | Ch. 26 | control-plane, data-plane | 0 | [link](book/part-6-networks-in-production/26-networks-made-of-software.md#key-takeaway) |
| Cloud virtual network (VPC) | ✅ written | Ch. 26 | sdn, underlay-vs-overlay | 0 | [link](book/part-6-networks-in-production/26-networks-made-of-software.md#key-takeaway) |
| Virtual route table / security group | ✅ written | Ch. 26 | cloud-virtual-network, routing-table | 0 | [link](book/part-6-networks-in-production/26-networks-made-of-software.md#key-takeaway) |
| Network namespace | ✅ written | Ch. 27 | virtual-interface | 0 | [link](book/part-6-networks-in-production/27-networking-moving-applications.md#key-takeaway) |
| Container network interface | ✅ written | Ch. 27 | network-namespace | 0 | [link](book/part-6-networks-in-production/27-networking-moving-applications.md#key-takeaway) |
| Pod/container address | ✅ written | Ch. 27 | container-network-interface | 1 | [link](book/part-6-networks-in-production/27-networking-moving-applications.md#key-takeaway) |
| Service address and discovery | ✅ written | Ch. 27 | pod-address, dns-hierarchy | 1 | [link](book/part-6-networks-in-production/27-networking-moving-applications.md#key-takeaway) |
| Ingress and egress | ✅ written | Ch. 27 | service-address-and-discovery, proxy | 0 | [link](book/part-6-networks-in-production/27-networking-moving-applications.md#key-takeaway) |
| Sidecar proxy | ✅ written | Ch. 27 | proxy, network-namespace | 0 | [link](book/part-6-networks-in-production/27-networking-moving-applications.md#key-takeaway) |
| Service mesh | ✅ written | Ch. 27 | sidecar-proxy, service-address-and-discovery | 0 | [link](book/part-6-networks-in-production/27-networking-moving-applications.md#key-takeaway) |

## Level 9 — Segmentation, Zero trust, Denial of service, Redundancy, Systematic troubleshooting

| Concept | Status | Chapter | Prerequisites | Misconceptions | Key Takeaway |
|---|---|---|---|---|---|
| Attack surface | ✅ written | Ch. 28 | endpoint | 0 | [link](book/part-6-networks-in-production/28-security-and-resilience-are-architectural.md#key-takeaway) |
| Segmentation and least privilege | ✅ written | Ch. 28 | administrative-boundary, stateful-firewall | 0 | [link](book/part-6-networks-in-production/28-security-and-resilience-are-architectural.md#key-takeaway) |
| Zero trust | ✅ written | Ch. 28 | segmentation-least-privilege | 1 | [link](book/part-6-networks-in-production/28-security-and-resilience-are-architectural.md#key-takeaway) |
| Denial of service | ✅ written | Ch. 28 | attack-surface | 0 | [link](book/part-6-networks-in-production/28-security-and-resilience-are-architectural.md#key-takeaway) |
| Redundancy and failover | ✅ written | Ch. 28 | failure-domain | 1 | [link](book/part-6-networks-in-production/28-security-and-resilience-are-architectural.md#key-takeaway) |
| Graceful degradation | ✅ written | Ch. 28 | redundancy-and-failover | 0 | [link](book/part-6-networks-in-production/28-security-and-resilience-are-architectural.md#key-takeaway) |
| Hypothesis-driven troubleshooting | ✅ written | Ch. 29 | layered-cooperation | 0 | [link](book/part-6-networks-in-production/29-seeing-and-troubleshooting-the-network.md#key-takeaway) |
| Active probes and passive observation | ✅ written | Ch. 29 | hypothesis-driven-troubleshooting, icmp | 2 | [link](book/part-6-networks-in-production/29-seeing-and-troubleshooting-the-network.md#key-takeaway) |
| Logs, metrics, and traces | ✅ written | Ch. 29 | hypothesis-driven-troubleshooting | 0 | [link](book/part-6-networks-in-production/29-seeing-and-troubleshooting-the-network.md#key-takeaway) |
| Packet capture | ✅ written | Ch. 29 | frame, tls-session | 0 | [link](book/part-6-networks-in-production/29-seeing-and-troubleshooting-the-network.md#key-takeaway) |
| Systematic troubleshooting method | ✅ written | Ch. 29 | active-passive-observation, logs-metrics-traces, packet-capture | 0 | [link](book/part-6-networks-in-production/29-seeing-and-troubleshooting-the-network.md#key-takeaway) |
