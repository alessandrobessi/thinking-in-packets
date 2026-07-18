# Best Effort, Limits, and Failure Signals

**Part:** Part II — Building an Internet

**Concept Level:** Level 4, per concept-graph.md

**Prerequisites:** forwarding, routing table (Ch. 9), IP packet (Ch. 6)

**New concepts introduced:** best-effort delivery, TTL, Hop Limit, ICMP, MTU, Path MTU, fragmentation, packet loss

---

## Opening Question

*What happens when the expected path fails or the packet cannot continue?*

## Real-World Story

A courier company's standard terms are honest about what they actually promise: they will make a genuine attempt to deliver a parcel, using their best available route. They do not promise the parcel will arrive. They do not promise it will arrive only once. They do not promise it will be the first of several copies to arrive, if a mistake causes it to be sent twice. If a parcel is too large for a particular delivery van, they don't simply crush it to fit — they either use a different vehicle or refuse the shipment and say so. None of this makes the courier company unreliable in a meaningful sense; it makes their promise precise, and it means anyone who actually needs guaranteed, in-order, exactly-once delivery has to build that guarantee themselves, on top of the courier's honest best-effort service.

Every chapter so far has shown packets successfully reaching their next hop. But Chapter 9's picture — one router making one local decision, then handing off to the next — has an obvious gap: what if a router's table is wrong, or a link is down, or the packet is simply too big for the next link to carry? Chapter 5 already insisted the network be treated as fallible from the start; this chapter is where IP's actual contract for failure gets made explicit.

## Worked Example

Follow two packets that don't arrive cleanly, and see what actually happens to each.

**A routing loop.** Suppose a misconfiguration causes Router X to send packets destined for a certain prefix to Router Y, while Router Y's table sends packets for that same prefix back to Router X. A packet destined there bounces between X and Y indefinitely — with nothing to stop it, it would consume link capacity and router processing forever, for a destination it will never actually reach. Every IP packet carries a **TTL** (IPv4) or **Hop Limit** (IPv6) — a number, decremented by one at every router it passes through. When that value reaches zero, the router holding it discards the packet immediately, rather than forwarding it — and to be genuinely useful rather than silently discarding a legitimate but slow-to-arrive packet, that router also sends back an **ICMP** "Time Exceeded" message to the original sender, using the sender's address recorded in the packet's own header. The loop stops consuming resources forever, and — critically — the sender actually finds out something went wrong instead of just waiting silently.

**An oversized packet.** Suppose a packet built on a network segment with a large **MTU** (Maximum Transmission Unit — the largest frame a given link can carry) needs to cross a link further along its path with a smaller MTU. In IPv4, a router facing this mismatch has two options depending on the packet's flags: split the packet into smaller pieces (**fragmentation**) that get reassembled at the final destination, or, if the packet is marked "don't fragment," discard it and send back an ICMP "Fragmentation Needed" message instead. IPv6 takes a firmer position: routers never fragment packets in transit at all — only the sending endpoint is allowed to size packets appropriately in the first place, informed by ICMPv6 "Packet Too Big" messages if an oversized packet is rejected along the path. Both approaches share the same underlying idea as the TTL case: a failure that would otherwise happen silently instead produces an explicit signal back to whoever needs to know about it.

Neither packet "just disappears" for no reason. Each is a case where the network hit a real, explainable limit — an unreachable destination via a broken table, or a link too small to carry a packet — and responded with a specific, informative failure signal rather than either pretending to succeed or vanishing with no trace.

## Core Intuition

IP promises to make a genuine attempt at delivery, using whatever path a router's current table indicates — nothing more. Packets can be lost, delayed, duplicated, or arrive out of order, and none of that violates IP's actual contract. What IP does provide, on top of that honest best-effort promise, are limits that prevent failures from consuming resources forever, and control messages that turn otherwise-silent failures into signals the sender can actually act on.

## Technical Explanation

**Best-effort delivery** is IP's core contract: every router along a path makes a genuine, honest attempt to forward each packet toward its destination using its current routing table, but nothing in IP itself guarantees the packet will arrive, will arrive only once, or will arrive in the order it was sent. This isn't a flaw to be patched — it's a deliberate design choice that keeps the network layer itself simple, leaving stronger guarantees, where an application actually needs them, to be built at the transport layer (Chapters 13-15).

**TTL** (Time to Live, IPv4) and **Hop Limit** (IPv6, functionally identical despite the different name) are a field in every packet's header, set by the sender to some starting value and decremented by exactly one at every router that forwards it. A router that would decrement this value to zero discards the packet instead of forwarding it — bounding, absolutely, how many hops any single packet can traverse before being removed from the network, which is what actually stops a routing loop (Chapter 9's forwarding mechanism has no mechanism of its own to detect one) from consuming resources indefinitely.

**ICMP** (Internet Control Message Protocol, with a parallel ICMPv6 for IPv6) is the mechanism IP uses to report exactly this kind of failure back to a packet's original sender — messages like "Time Exceeded" (TTL/Hop Limit reached zero), "Destination Unreachable" (no route exists, or the destination refuses the packet), and "Fragmentation Needed" / "Packet Too Big" (the MTU problem below). ICMP is carried directly over IP, the same way any other packet is, and its whole purpose is turning failures that would otherwise be silent into something the sender can observe and, if the application above it cares to, act on.

**MTU** is the largest frame size a given link can carry — a physical or configured limit of that specific link, not a property of IP itself. A path from source to destination typically crosses several links, potentially with different MTUs, and the smallest MTU anywhere along that path constrains how large a packet can travel the whole way without running into trouble — informally, the **Path MTU**. **Fragmentation** is IPv4's in-transit solution when a packet exceeds the MTU of a link it needs to cross: a router splits it into smaller pieces, each with enough header information to be reassembled at the final destination. IPv6 deliberately removed in-transit fragmentation from routers entirely — only the sending endpoint may fragment (by choosing an appropriately small packet size up front, informed by Path MTU Discovery's ICMPv6 feedback), pushing the size-limiting work to the edge of the network rather than every router along the path.

```mermaid
sequenceDiagram
    participant S as Sender
    participant R1 as Router (TTL 1→0)
    S->>R1: Packet, TTL = 1
    R1->>R1: Decrement TTL: reaches 0, discard
    R1-->>S: ICMP Time Exceeded
    Note over S: Sender learns the packet<br/>never reached its destination
```

*Alt text: A sequence diagram showing a sender's packet arriving at a router with a TTL that would reach zero, the router discarding it instead of forwarding, and the router sending an ICMP Time Exceeded message back to the original sender — turning a silent drop into an observable signal.*

Together, TTL/Hop Limit, ICMP, and MTU handling are what keep best-effort delivery from meaning "unaccountable" delivery: packets that can't continue are bounded in how much damage they can do, and — wherever practical — someone finds out.

## Packet-Journey Checkpoint

Every packet the café laptop sends toward `example.net` carries a TTL or Hop Limit that's decremented at every router from Chapter 9's forwarding chain; if a misconfigured route ever created a loop somewhere upstream, that value — not any cleverness in the routers themselves — is what would eventually stop the packet and report the failure back to the laptop, rather than the request simply hanging forever with no explanation.

## Common Misconceptions

### *IP guarantees delivery.*

**Why it's wrong:** Because web pages and downloads usually arrive completely and correctly, it's easy to assume something in the network itself is guaranteeing that outcome.

**Correct intuition:** IP is explicitly best-effort — no delivery, ordering, or single-delivery guarantee exists at this layer. Reliable delivery, where it exists, is built by the transport layer on top (Chapters 13-15), not provided by IP itself.

**Analogy:** A courier's honest terms promise a genuine attempt, not a guarantee — anyone needing a stronger guarantee (proof of delivery, insurance) has to arrange that separately, on top of the base shipping service.

### *ICMP is only used by `ping`.*

**Why it's wrong:** `ping` is most people's only conscious encounter with ICMP, so it's easy to assume that's ICMP's whole purpose.

**Correct intuition:** ICMP carries a range of control and error messages — Time Exceeded, Destination Unreachable, Fragmentation Needed/Packet Too Big — used continuously by the network to report failures, entirely independent of whether anyone is running `ping`.

**Analogy:** A courier's tracking-and-exception system does far more than answer "are you still there?" pings — it's the same infrastructure that reports "undeliverable," "package too large for this route," and other real delivery problems.

### *A packet can be arbitrarily large.*

**Why it's wrong:** Application data — a file, a page of text — has no inherent size limit, which can make it feel like packets shouldn't either.

**Correct intuition:** Every link a packet crosses has a maximum frame size (MTU), and a packet exceeding the smallest MTU on its path either gets fragmented (IPv4) or rejected with a signal to size it down (IPv6, and IPv4 packets marked "don't fragment").

**Analogy:** A delivery van has a maximum cargo size regardless of how much a customer wants shipped in one box — oversized shipments get split into multiple boxes or rejected, not force-fit.

### *Fragmentation behaves identically in IPv4 and IPv6.*

**Why it's wrong:** Both use the same word and solve the same underlying MTU-mismatch problem, which can suggest the mechanism itself is identical.

**Correct intuition:** IPv4 allows routers to fragment packets in transit. IPv6 does not — only the sending endpoint may fragment, guided by ICMPv6 feedback from Path MTU Discovery, pushing size-limiting work to the edges rather than every router along the path.

**Analogy:** One courier network lets any depot along the route repack an oversized shipment into smaller boxes; a stricter courier network insists the sender package everything correctly before it ever leaves the origin warehouse.

## Practical Implications

An application that silently hangs rather than erroring out on an unreachable destination is often a sign that ICMP messages are being filtered somewhere along the path — a common, sometimes well-intentioned firewall practice that has the side effect of destroying the very failure signals this chapter describes, including the ones Path MTU Discovery depends on to work at all. Recognizing best-effort delivery as IP's actual, deliberate contract — not a shortcoming — also reframes what "the network dropped my packet" means in a postmortem: a drop within IP's own best-effort promise isn't necessarily a bug anywhere; it's what happens when a link or router genuinely can't continue, and the real question is whether the failure was at least reported.

## Key Takeaway

**IP moves packets on a best-effort basis, using limits and control messages to prevent failures from remaining completely invisible.**

## What to Remember

- IP's actual contract is best-effort: a genuine attempt at delivery, with no guarantee of arrival, single delivery, or order.
- TTL (IPv4) / Hop Limit (IPv6) bounds how many hops a packet can traverse, stopping routing loops from consuming resources forever.
- ICMP reports failures — like TTL expiry or an unreachable destination — back to the original sender, turning silent drops into observable signals.
- MTU is a property of a specific link; the smallest MTU on a path constrains how large a packet can travel that whole path.
- IPv4 allows in-transit fragmentation by routers; IPv6 does not — only the sending endpoint fragments, guided by Path MTU Discovery.
- Disabling or filtering ICMP can silently break Path MTU Discovery and other failure-reporting mechanisms this chapter describes.

## The Next Obvious Question

*How do independently operated networks exchange enough information to connect the world?*

---

**Glossary terms added this chapter:** best-effort delivery, TTL, Hop Limit, ICMP, MTU, Path MTU, fragmentation, packet loss → append to `/glossary.md`

**Misconceptions logged this chapter:** ip-guarantees-delivery (pre-seeded row, enriched below), icmp-only-for-ping, packet-arbitrarily-large, fragmentation-identical-ipv4-ipv6 (in-chapter coverage) → append to `/misconceptions.md`

**Concept-graph entries checked off:** best-effort-delivery, ttl-hop-limit, icmp, mtu, path-mtu, fragmentation, packet-loss → update `/concept-graph.yaml`, regenerate `/concept-graph.md`

**Diagrams used this chapter:** sequence (TTL expiry and ICMP Time Exceeded, Mermaid)
