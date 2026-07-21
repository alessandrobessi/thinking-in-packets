# Glossary

A running index of every term introduced in the book, in order of first
appearance. This table is a thin index, not a duplicate of chapter prose —
the real explanation lives in the chapter itself.

| Term | One-line definition | First introduced |
|---|---|---|
| Network | A collection of endpoints and the equipment connecting them, capable of exchanging messages according to shared rules. | Ch. 1 |
| Endpoint | A machine, or a running piece of software on a machine, that originates or ultimately receives information. | Ch. 1 |
| Message | The unit of information one endpoint wants to get to another (a loose, informal term at this stage). | Ch. 1 |
| Protocol | A shared rule set, followed by every participant, about how a message should be formatted and handled. | Ch. 1 |
| Intermediary | A device that is not the ultimate source or destination of a message but participates in moving it along. | Ch. 1 |
| Failure | A normal condition every networked component must be built to expect, not a rare exception. | Ch. 1 |
| Layered cooperation | Many independently operating components, each following shared rules and doing a small local job, producing a networked result with no single component aware of the whole journey. | Ch. 1 |
| Bit | The smallest unit of digital information — a single 0 or 1, not itself a physical thing. | Ch. 2 |
| Signal | The physical representation of bits — a changing voltage, light pulse, or radio wave — that a medium actually carries. | Ch. 2 |
| Encoding | The agreed-upon scheme for turning bits into signal changes and back again. | Ch. 2 |
| Physical medium | Whatever a link is actually capable of carrying a signal through — copper, fiber, or open air. | Ch. 2 |
| Noise | Unwanted physical interference that can distort a signal enough that a receiver misreads it. | Ch. 2 |
| Bandwidth | How much data a link can carry per unit of time once data is flowing — carrying capacity. | Ch. 2 |
| Propagation latency | How long a signal takes to physically travel from one end of a link to the other, paid once per trip. | Ch. 2 |
| Frame | The unit created by wrapping content in a header (and sometimes a trailer) at the link layer, giving it a defined boundary. | Ch. 3 |
| Boundary | A defined start and end for a transmitted unit, letting a receiver separate it from surrounding traffic. | Ch. 3 |
| Header | The wrapping information placed before a unit's actual content, carrying what's needed to interpret and deliver it. | Ch. 3 |
| Payload | The actual content being carried by a frame (or later, any encapsulated unit), from that layer's perspective. | Ch. 3 |
| Trailer | Wrapping information placed after a unit's payload, often an integrity check. | Ch. 3 |
| Checksum | A value computed from content, included with it, that lets a receiver detect (not repair) whether it was altered in transit. | Ch. 3 |
| Encapsulation | The pattern of wrapping a unit of content with a header (and sometimes a trailer) carrying exactly what the current layer needs. | Ch. 3 |
| Network interface | The point where a device physically connects to a network. | Ch. 4 |
| MAC address | A link-scoped identifier assigned to a network interface, used to address frames within one local network. | Ch. 4 |
| Ethernet | A common local-network technology, typically over cable, delivering MAC-addressed frames. | Ch. 4 |
| Wi-Fi | A common local-network technology over radio, delivering MAC-addressed frames across a shared medium. | Ch. 4 |
| Shared medium | A physical medium, like Wi-Fi's radio airspace, where multiple devices transmit into and listen on the same space. | Ch. 4 |
| Switch | The device that delivers frames within a local network, learning MAC-address locations from observed traffic. | Ch. 4 |
| Forwarding table | A switch's record mapping observed MAC addresses to the port they were last seen arriving from. | Ch. 4 |
| Broadcast | A frame flooded out every port except the one it arrived on, used before a destination's location is learned or when addressed to everyone. | Ch. 4 |
| Broadcast domain | The set of devices a given broadcast actually reaches. | Ch. 5 |
| Failure domain | The set of devices a given failure or misbehavior can actually affect. | Ch. 5 |
| Administrative boundary | A dividing line marking where responsibility for a network's configuration and maintenance belongs to one team versus another. | Ch. 5 |
| Internetwork | Many separately bounded local networks, each with contained broadcasts and failures, connected by a distinct cross-network mechanism. | Ch. 5 |
| IP packet | The unit that moves between networks, built by wrapping a payload in a header meant to stay meaningful across many hops, not just one link. | Ch. 6 |
| IPv4 | The 32-bit version of the Internet Protocol's addressing scheme, conventionally written as four dotted decimal numbers. | Ch. 6 |
| IPv6 | The 128-bit version of the Internet Protocol's addressing scheme, written as groups of hexadecimal digits separated by colons. | Ch. 6 |
| Address (IP) | A value identifying an interface's position within a hierarchical routing scheme. | Ch. 6 |
| Prefix | The leading portion of an IP address (written `/N`) that identifies which network an address belongs to. | Ch. 6 |
| Subnet | A block of addresses sharing one prefix, treated as one local network for addressing and routing purposes. | Ch. 6 |
| Network portion | The prefix bits of an address — the part identifying which subnet it belongs to. | Ch. 6 |
| Host portion | The bits of an address left over after the prefix, identifying a specific interface within its subnet. | Ch. 6 |
| Hierarchical allocation | The practice of allocating large address blocks to registries, then progressively smaller blocks downward, so each level only needs to understand blocks one step more specific than its own. | Ch. 6 |
| Private address (preview) | An address block meaningful only within one organization's own network, not routable from the wider Internet without translation (full treatment in Chapter 16). | Ch. 6 |
| Interface configuration | The set of network-specific facts (address, prefix, gateway, DNS resolver) an interface needs before it can meaningfully participate in a network. | Ch. 7 |
| DHCP | A request-and-reply protocol where a device broadcasts a request and a server replies with an address and other configuration, bundled with a time-limited lease. | Ch. 7 |
| SLAAC | Stateless Address Autoconfiguration — an IPv6 mechanism where a device constructs its own address from a router-advertised prefix, with no server tracking who holds it. | Ch. 7 |
| Default gateway | The address of the local router a host hands packets to whenever a destination lies outside its own subnet. | Ch. 7 |
| DNS resolver address | The address of the service a device will later query to turn names into addresses. | Ch. 7 |
| Lease | The time-limited validity period attached to a DHCP-assigned address. | Ch. 7 |
| Local configuration state | Facts specific to the current network that a device needs but doesn't inherently know. | Ch. 7 |
| Next hop | The device responsible for forwarding a packet onward, whether that's the final destination (local) or a router toward it (remote). | Ch. 8 |
| Local-versus-remote decision | The comparison of a destination's IP address against a device's own prefix, determining whether the destination's own MAC address or the next hop's must be resolved. | Ch. 8 |
| ARP | Address Resolution Protocol — IPv4's link-local broadcast mechanism for resolving an IP address to a MAC address. | Ch. 8 |
| Neighbor Discovery | IPv6's mechanism (via multicast Neighbor Solicitation/Advertisement) for resolving an IP address to a MAC address, and for router advertisements. | Ch. 8 |
| Neighbor cache | A device's stored mapping of resolved IP-to-MAC address pairs, avoiding repeated resolution for the same address. | Ch. 8 |
| Address resolution | The general process of turning an IP address into the MAC address needed to frame a packet toward it. | Ch. 8 |
| Router | A device that forwards IP packets between networks using IP addressing, as opposed to a switch's link-local MAC-based forwarding. | Ch. 9 |
| Forwarding | The act of receiving a packet, consulting a routing table, and sending it toward the chosen next hop. | Ch. 9 |
| Routing table | A router's table mapping address prefixes to next hops. | Ch. 9 |
| Longest-prefix match | The rule that, among all routing-table entries matching a destination, the one with the longest (most specific) prefix is chosen. | Ch. 9 |
| Default route | A routing-table entry matching every destination but with the shortest possible prefix, used only when nothing more specific matches. | Ch. 9 |
| Data plane | The per-packet work of forwarding: consulting a table and sending a packet on, as opposed to the mechanisms that populate that table. | Ch. 9 |
| Best-effort delivery | IP's core contract: a genuine attempt at delivery, with no guarantee of arrival, single delivery, or order. | Ch. 10 |
| TTL / Hop Limit | A packet-header field decremented at every router hop, causing the packet to be discarded once it reaches zero. | Ch. 10 |
| ICMP | Internet Control Message Protocol — the mechanism IP uses to report failures (like TTL expiry or unreachable destinations) back to a packet's sender. | Ch. 10 |
| MTU | Maximum Transmission Unit — the largest IP packet a given link can carry without IP-layer fragmentation. | Ch. 10 |
| Path MTU | The smallest MTU among all the links on a packet's path, constraining how large a packet can travel that whole path. | Ch. 10 |
| Fragmentation | Splitting a packet into smaller pieces to fit a link's MTU; performed by routers in transit in IPv4, only by the sending endpoint in IPv6. | Ch. 10 |
| Packet loss | A packet failing to reach its destination — an expected, normal possibility under IP's best-effort contract. | Ch. 10 |
| Autonomous system (AS) | A network under one organization's administrative control, presenting one coherent routing face to the outside world. | Ch. 11 |
| ISP | Internet service provider — an autonomous system in the business of carrying other networks' traffic. | Ch. 11 |
| Transit | A paid relationship where one autonomous system carries another's traffic onward to the rest of the Internet. | Ch. 11 |
| Peering | A relationship where two autonomous systems exchange traffic destined for each other's own customers directly, typically without payment. | Ch. 11 |
| Route advertisement | The mechanism by which an autonomous system tells its neighbors which address blocks it can deliver traffic to. | Ch. 11 |
| BGP | Border Gateway Protocol — the protocol autonomous systems use to exchange route advertisements. | Ch. 11 |
| Policy (routing) | An autonomous system's own business and technical preferences governing which routes it accepts, prefers, and advertises onward. | Ch. 11 |
| Control plane | The exchange of information and decisions about how traffic should flow, as distinct from the data plane's job of actually forwarding packets. | Ch. 11 |
| Route convergence | The process by which the Internet's collective view of reachability updates, hop by hop, after an advertisement or withdrawal. | Ch. 11 |
| Process | A running instance of a program, capable of independently sending and receiving network traffic. | Ch. 12 |
| Port | A number identifying a specific transport-layer communication endpoint on a host. | Ch. 12 |
| Source port | The port number a sending process used, carried in a transport-layer packet header. | Ch. 12 |
| Destination port | The port number a receiving process is expected to be listening on, carried in a transport-layer packet header. | Ch. 12 |
| Five-tuple | The combination of source IP, source port, destination IP, destination port, and protocol that identifies one transport flow — and, for TCP, one established connection — within a given network context at a given moment. | Ch. 12 |
| Socket | The operating system's handle for a transport-layer endpoint — a full five-tuple's worth once a TCP conversation is established, but not every socket has a fixed remote endpoint (a listening TCP socket or unconnected UDP socket doesn't). | Ch. 12 |
| Demultiplexing | Using an incoming packet's five-tuple (or, for a listening socket with no five-tuple yet, its port/protocol/local-address binding) to determine which process should receive it. | Ch. 12 |
| UDP | User Datagram Protocol — a minimal, connectionless transport protocol that sends independent datagrams with no delivery guarantees. | Ch. 13 |
| Datagram | One self-contained unit of data sent independently by UDP, with no relationship tracked to any other datagram. | Ch. 13 |
| Message boundary | The edges of one application-level send, preserved intact by UDP but not by TCP's byte stream. | Ch. 13 |
| Connectionless communication | A transport model, like UDP's, with no setup, teardown, or ongoing session state between sends. | Ch. 13 |
| Application-managed reliability | Reliability, ordering, or pacing logic implemented by the application itself, above a transport layer (like UDP) that doesn't provide it. | Ch. 13 |
| TCP | Transmission Control Protocol — a connection-oriented transport protocol providing an ordered, reliable byte stream. | Ch. 14 |
| Connection (TCP) | Coordinated, shared state maintained by two endpoints over the life of a TCP exchange. | Ch. 14 |
| Handshake | The message exchange (SYN, SYN-ACK, ACK) that establishes a TCP connection and agreed starting sequence numbers before data flows. | Ch. 14 |
| Byte stream | TCP's delivery model: a continuous, ordered sequence of bytes with no preserved application message boundaries. | Ch. 14 |
| Sequence number | A per-byte counter letting a TCP receiver place incoming data at its correct position in the stream. | Ch. 14 |
| Acknowledgement | A TCP receiver's confirmation of which sequence numbers it has successfully received. | Ch. 14 |
| Retransmission | A TCP sender resending data after failing to receive its acknowledgement in time. | Ch. 14 |
| Duplicate detection | A TCP receiver recognizing and discarding a retransmitted segment it has already received. | Ch. 14 |
| Receive window | The amount of additional data a TCP receiver is currently willing and able to buffer, advertised with every acknowledgement. | Ch. 15 |
| Flow control | TCP's mechanism for keeping a sender from overwhelming the receiver's own buffering capacity. | Ch. 15 |
| Congestion | The condition where combined traffic exceeds what a shared network link or device can carry, causing queuing and loss. | Ch. 15 |
| Congestion window | A TCP sender's own inferred estimate of how much data it can safely have in flight without contributing to network congestion. | Ch. 15 |
| Acknowledgement clocking | The pattern where the steady rhythm of incoming acknowledgements paces how quickly a sender grows its congestion window. | Ch. 15 |
| Retransmission timeout | The interval after which, absent an acknowledgement, a TCP sender infers loss and retransmits. | Ch. 15 |
| Fairness (congestion control) | The property that no single connection should indefinitely starve others sharing the same congested path. | Ch. 15 |
| Backoff | A sender's sharp reduction of its congestion window upon detecting loss, before cautiously growing again. | Ch. 15 |
| Explicit Congestion Notification (ECN) | A mechanism letting a congested router mark a packet instead of dropping it, delivering a congestion signal without any loss. | Ch. 15 |
| Private address | An address from a reserved range (e.g. RFC 1918) meaningful only within one local network, never forwarded on the public Internet. | Ch. 16 |
| Public address | A globally unique address, potentially reachable from anywhere on the Internet. | Ch. 16 |
| NAT (Network Address Translation) | Rewriting a packet's source (and often port) at a network boundary so multiple private addresses can share one public one, using a remembered per-connection translation table. | Ch. 16 |
| Port translation | NAT's common practice of rewriting the source port alongside the source address, so many internal connections can share one public address. | Ch. 16 |
| Stateful firewall | A device enforcing traffic policy that remembers already-approved connections so it need not re-check every packet against the full rule set. | Ch. 16 |
| Forward proxy | An intermediary that relays outbound requests on a client's behalf; the destination sees the proxy's address, not the original client's. | Ch. 16 |
| Reverse proxy | An intermediary that accepts inbound connections appearing to be the final destination, then relays them to whichever real backend should handle them. | Ch. 16 |
| Tunnel | Carrying one packet, header and payload, encapsulated inside another packet's payload, to cross a network that wouldn't otherwise carry it directly. | Ch. 16 |
| VPN | A tunnel combined with encryption to a trusted VPN server, which decrypts and forwards the original traffic onward. | Ch. 16 |
| Middlebox | Any device on a network path that does something to traffic beyond plain, unmodified forwarding toward its destination. | Ch. 16 |
| Domain name | A human-readable hierarchical name (e.g. www.example.net), read right to left from top-level domain to specific host. | Ch. 17 |
| DNS hierarchy | The delegated tree of responsibility for domain names, from the root down through top-level domains to individual domains. | Ch. 17 |
| Root (DNS) | The small set of well-known servers at the top of the DNS hierarchy, which know which servers are authoritative for every top-level domain. | Ch. 17 |
| Top-level domain (TLD) | The rightmost label of a domain name (e.g. .net), delegated by the root to its own set of servers. | Ch. 17 |
| Authoritative server | The server(s) actually designated to hold the final, real answers for a specific domain. | Ch. 17 |
| Recursive resolver | The component that performs the multi-step DNS delegation walk on a client's behalf, returning one final answer. | Ch. 17 |
| Delegation (DNS) | One level of the DNS hierarchy designating which servers are responsible for a more specific portion of the naming space. | Ch. 17 |
| Record (DNS) | A specific answer an authoritative server holds for a name, such as an address or an alias. | Ch. 17 |
| TTL (DNS) | The number of seconds a resolver may cache a DNS record before treating it as stale and re-fetching it. | Ch. 17 |
| Cache (DNS) | A resolver's local, temporary store of previously learned DNS answers, served directly while still within their TTL. | Ch. 17 |
| A record | A DNS record mapping a name to an IPv4 address. | Ch. 17 |
| AAAA record | A DNS record mapping a name to an IPv6 address. | Ch. 17 |
| CNAME record | A DNS record mapping one name to another name, rather than directly to an address. | Ch. 17 |
| Plaintext | The original, readable content before any encryption is applied. | Ch. 18 |
| Ciphertext | Content after encryption — unreadable without the corresponding key. | Ch. 18 |
| Encryption | The transformation of plaintext into ciphertext, and back again with the right key. | Ch. 18 |
| Integrity (cryptographic) | The property that lets a receiver detect whether a message was altered in transit, independent of whether it's also encrypted. | Ch. 18 |
| Authentication | Verifying that a party genuinely is who it claims to be, before trusting anything else it says. | Ch. 18 |
| Certificate | A signed statement binding a domain name to a public key, issued by a certificate authority. | Ch. 18 |
| Certificate authority (CA) | An organization whose signature browsers and operating systems are configured, in advance, to trust when validating certificates. | Ch. 18 |
| Key exchange | A method letting two parties derive a shared secret over a fully observed channel, without an observer being able to reconstruct that secret. | Ch. 18 |
| TLS session | The stateful, protected channel two endpoints maintain after a successful handshake, using keys derived from their shared secret. | Ch. 18 |
| URL | A Uniform Resource Locator, identifying a scheme, a host, and a path locating a specific resource. | Ch. 19 |
| HTTP request | A structured message naming a method and a path, carrying headers and (often) a body, sent to a server. | Ch. 19 |
| Method (HTTP) | The action an HTTP request asks the server to perform, such as GET (safe, read-only retrieval) or POST (process submitted data, possibly with side effects) — defined by intended semantics, not merely by whether a body is present. | Ch. 19 |
| Path (HTTP) | The part of a URL identifying a specific resource on a host. | Ch. 19 |
| Header (HTTP) | Metadata attached to an HTTP request or response, such as content type, cookies, or caching directives. | Ch. 19 |
| Body (HTTP) | The data payload carried by an HTTP request or response, distinct from its headers. | Ch. 19 |
| Response (HTTP) | The structured reply to an HTTP request, carrying a status code, headers, and usually a body. | Ch. 19 |
| Status code | A three-digit number in an HTTP response indicating the outcome of a request (e.g. 200 success, 404 not found, 500 server error). | Ch. 19 |
| Cookie | A small piece of data a server asks a browser to store and automatically resend with future requests to that site. | Ch. 19 |
| Session (HTTP) | Server-side state, often keyed by a cookie value, letting a server recognize a sequence of requests as one ongoing interaction. | Ch. 19 |
| Stateless protocol | A protocol, like HTTP, in which nothing built into the protocol itself links one request to any previous request. | Ch. 19 |
| Throughput | How much data actually moves across a connection per unit of time once transfer is under way. | Ch. 21 |
| Serialization delay | The time a sending device takes to push all of a unit's bits onto the link, based on the unit's size and the link's capacity. | Ch. 21 |
| Propagation delay | The physical travel time for a signal to cross a link, bounded by the speed of light through that medium. | Ch. 21 |
| Processing delay | Time a device spends actually handling a unit once it arrives — inspecting a header, making a decision. | Ch. 21 |
| Queueing delay | Time a unit spends waiting in line behind other traffic before a device processes or forwards it. | Ch. 21 |
| Round-trip time (RTT) | The total delay for a request to go out and its reply to come back, summing serialization, propagation, processing, and queueing delay both ways. | Ch. 21 |
| Jitter | Variation in delay from one packet to the next, distinct from the average delay itself. | Ch. 21 |
| Buffering | A device holding a small queue of units waiting to be sent, absorbing brief bursts of traffic. | Ch. 21 |
| Bufferbloat | Excess buffering that lets an overloaded link's backlog grow instead of signaling overload quickly, producing climbing queueing delay. | Ch. 21 |
| Bandwidth-delay product | Capacity multiplied by round-trip time, describing roughly how much data can be usefully in flight on a path at once. | Ch. 21 |
| Cache | A stored copy of a response used to answer a later, matching request without repeating the original work. | Ch. 22 |
| Freshness | How a cache decides whether a stored copy is still safe to reuse or has gone stale. | Ch. 22 |
| CDN (content delivery network) | Globally distributed infrastructure that caches content near users and shields the origin from most traffic. | Ch. 22 |
| Edge location | A point of presence, physically near a cluster of users, that holds cached copies of content on a CDN's behalf. | Ch. 22 |
| Origin | The server that actually owns, and when needed generates, the content a CDN's edge locations cache. | Ch. 22 |
| Load balancer | A component that sits in front of a pool of interchangeable backend servers and decides which one handles incoming work — per request at the application layer, or more commonly per connection/flow at the transport layer. | Ch. 22 |
| Health check | A load balancer's periodic probe that removes a failing or overloaded backend from rotation automatically. | Ch. 22 |
| Replication | Running multiple copies of a service or its data, for both capacity and resilience. | Ch. 22 |
| Affinity (session stickiness) | A load-balancing policy that routes a given user's repeated requests to the same backend, so instance-local state stays reachable — it sidesteps cross-replica inconsistency for that user's traffic, it doesn't create consistency across replicas generally. | Ch. 22 |
| Anycast | A routing technique where the same IP address is announced from multiple locations, and routing delivers each user to the closest one. | Ch. 22 |
| Connection reuse | Sending more than one request over a single already-established connection instead of opening a new one per request. | Ch. 23 |
| Pipelining (intuition) | An earlier technique of sending several requests on a reused connection without waiting for each response, still constrained to in-order responses. | Ch. 23 |
| Multiplexing | Letting multiple independent, concurrent exchanges share one underlying connection, interleaved rather than strictly sequential. | Ch. 23 |
| Stream (HTTP/2) | An independent, bidirectional sequence of messages within an HTTP/2 connection, identified by its own stream number. | Ch. 23 |
| HTTP/2 | The version of HTTP built around multiplexing multiple concurrent streams over one connection. | Ch. 23 |
| Header compression | Shared compression state across an HTTP/2 connection's lifetime, letting repeated header metadata be sent far more compactly. | Ch. 23 |
| Head-of-line blocking | A lost or delayed unit blocking delivery of unrelated data queued behind it in the same ordered stream. | Ch. 23 |
| QUIC | A transport protocol implementing reliable, ordered, congestion-controlled delivery over UDP, commonly implemented in user space (not a strict requirement). | Ch. 24 |
| HTTP/3 | The version of HTTP built to run over QUIC instead of TCP. | Ch. 24 |
| User-space transport | Transport logic running as ordinary application-level software rather than inside the operating system kernel — QUIC's common, but not strictly required, deployment style. | Ch. 24 |
| Connection ID | A value QUIC endpoints choose to identify a connection, independent of IP address or port. | Ch. 24 |
| Connection migration | A QUIC connection continuing across a network change (e.g. Wi-Fi to cellular) without being torn down and rebuilt. | Ch. 24 |
| Independent streams (QUIC) | Multiple concurrent streams within one QUIC connection, each with its own delivery order at the transport layer, so a stream is never blocked behind another's missing bytes — though loss detection and congestion response operate at the connection level, so a shrinking shared congestion window can still briefly slow every stream's sending rate after loss. | Ch. 24 |
| Encrypted transport metadata | Transport-level control information QUIC encrypts alongside application payload, beyond what TCP traditionally protects. | Ch. 24 |
| Zero-round-trip (0-RTT) resumption | A returning client sending application data immediately alongside its first handshake message, under specific prior-connection conditions; inherited from TLS 1.3 (usable over plain TCP too, not just QUIC). That first flight is more vulnerable to replay than data sent after a full handshake. | Ch. 24 |
| Timeliness | How much a piece of data's usefulness depends on arriving promptly. | Ch. 25 |
| Completeness | How much an application needs every piece of data to actually arrive, with nothing missing. | Ch. 25 |
| Jitter buffer | A small holding area that briefly delays incoming data to smooth out uneven arrival caused by jitter. | Ch. 25 |
| Adaptive bitrate | A technique where a client matches requested content quality to its currently available throughput in real time. | Ch. 25 |
| State synchronization | Sending periodic snapshots of current state where a newer snapshot supersedes an older one, instead of guaranteeing strict message-by-message delivery. | Ch. 25 |
| Idempotency (intuition) | A property of an operation producing the same correct result whether it happens once or is accidentally repeated. | Ch. 25 |
| Backpressure | A signal from a receiver or downstream component telling a sender to slow down before capacity is exceeded. | Ch. 25 |
| Virtual interface | A software-implemented network interface with no dedicated physical hardware behind it. | Ch. 26 |
| Bridge (virtual) | A software equivalent of a switch, connecting multiple virtual (or virtual and physical) interfaces as one local link. | Ch. 26 |
| Tunnel | Wrapping one network's traffic entirely inside another network's packets so it can cross unaware infrastructure. | Ch. 26 |
| Overlay | A logical network built from tunnels, layered on top of a physical underlay. | Ch. 26 |
| Underlay | The real, physical network an overlay's tunneled traffic actually travels across. | Ch. 26 |
| Software-defined networking (SDN) | Centralizing forwarding-policy computation in a control-plane system that programs distributed data-plane devices. | Ch. 26 |
| Cloud virtual network (VPC) | A customer-defined logical network within a cloud provider's shared physical infrastructure, built through SDN. | Ch. 26 |
| Virtual route table | The cloud-virtual-network equivalent of a routing table, customer-configurable within a VPC's logical topology — controls where traffic goes, not whether it's permitted (a separate job for security groups/firewall policy). | Ch. 26 |
| Network namespace | An isolated view of network state — its own interfaces and routing table — on a shared kernel. | Ch. 27 |
| Pod | A group of one or more tightly coupled containers, the platform's actual unit of scheduling and network identity; owns one network namespace and address, shared by every container inside it. | Ch. 27 |
| Container Network Interface (CNI) | The standardized plugin specification a platform calls to provision a new pod's network interface, address, and routing — names the specification and plugin, not the resulting interface. | Ch. 27 |
| Pod (container) address | The network-layer address of a specific running pod, deliberately treated as unstable and disposable. | Ch. 27 |
| Service address | A stable, durable virtual address representing a logical service rather than any one instance behind it. | Ch. 27 |
| Service discovery | The platform's continuously updated record of currently healthy pod addresses, watched by control-plane components that keep the data plane's forwarding rules programmed to match — the data plane itself just follows those rules per packet, commonly staying with one instance per connection/flow rather than re-selecting per request. | Ch. 27 |
| Headless service | A service that skips the stable virtual address and lets DNS resolution return individual pod addresses directly. | Ch. 27 |
| Ingress | Declared routing configuration — which external host/path maps to which internal service — at a cluster's boundary, distinct from the ingress controller that executes it. | Ch. 27 |
| Ingress controller | The running proxy infrastructure that reads Ingress configuration and does the actual work of accepting and routing external traffic inward. | Ch. 27 |
| Egress | Traffic actually crossing a cluster's or service's outer boundary outbound, often subject to its own policy and routing — distinct from east-west traffic. | Ch. 27 |
| East-west traffic | Service-to-service traffic within the same boundary, as distinct from north-south traffic crossing that boundary (ingress/egress). | Ch. 27 |
| Sidecar proxy | A proxy deployed alongside one pod's application container(s) to add cross-cutting network behavior without changing their code. | Ch. 27 |
| Service mesh | Uniform, centrally-controlled traffic security, observability, and routing layered platform-wide — traditionally via per-pod sidecar proxies, though newer sidecarless/ambient designs use shared node-level proxies instead. | Ch. 27 |
| Attack surface | The total set of points where an unauthorized actor could attempt to interact with a system. | Ch. 28 |
| Segmentation | Dividing a network into smaller zones with policy enforcing what traffic may cross between them. | Ch. 28 |
| Least privilege | Granting each component, service, or user only the specific access genuinely required for its function. | Ch. 28 |
| Zero trust | Treating network location as insufficient evidence of trust, verifying access based on identity and context instead. | Ch. 28 |
| Denial of service (DoS/DDoS) | Deliberately sending traffic to exhaust a system's capacity, from one source (DoS) or many simultaneously (DDoS). | Ch. 28 |
| Redundancy | Maintaining more capacity or independent copies than strictly required, so some can be lost without total failure. | Ch. 28 |
| Failure domain (production sense) | The boundary within which a given failure can propagate, used to judge whether redundant components are genuinely independent. | Ch. 28 |
| Failover | The mechanism that detects a failed component and redirects traffic to a healthy one. | Ch. 28 |
| Graceful degradation | A system deliberately shedding lower-priority work under stress to protect its core function. | Ch. 28 |
| Symptom | The vague, user-visible observation that triggers a troubleshooting investigation. | Ch. 29 |
| Hypothesis (troubleshooting) | A specific, falsifiable claim about where a failure actually lives, narrow enough for one small test to confirm or rule out. | Ch. 29 |
| Scope (troubleshooting) | The deliberate boundary of what a given hypothesis and test are actually checking. | Ch. 29 |
| Active probe | Deliberately generated test traffic sent specifically to check something. | Ch. 29 |
| Passive observation | Examining evidence already produced by normal operation without generating new traffic. | Ch. 29 |
| Logs | Records of discrete events, like a request being received or an error occurring. | Ch. 29 |
| Metrics | Aggregated numerical measurements over time, like request rate or error percentage. | Ch. 29 |
| Traces | Records connecting the individual steps of one specific request as it moved through multiple systems. | Ch. 29 |
| Packet capture | Recording the actual frames and packets crossing a specific point on the network. | Ch. 29 |
| Systematic troubleshooting method | Narrowing a vague symptom to a specific failing layer through ordered, targeted hypotheses and the smallest test that can confirm or rule out each one. | Ch. 29 |
