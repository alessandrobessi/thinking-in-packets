# What Happens When You Visit a Website

**Part:** Part IV — Names, Trust, and the Web

**Concept Level:** Integration chapter — consolidates Levels 0-6, per concept-graph.md

**Prerequisites:** Chapters 1-19 in full

**New concepts introduced:** none; integration is the chapter's purpose

---

## Opening Question

*Can we now trace an entire page load without skipping any layer?*

## Real-World Story

The café laptop from Chapter 1 — the one whose message to a coworker four feet away turned out to travel through a chain of independently owned equipment — now opens this book's own website. Nineteen chapters ago, that journey was a deliberately vague gesture at "layered cooperation," a promise that the rest of the book would fill in. Every piece has now actually been built: signals and frames, addresses and forwarding, transport and reliability, middleboxes, naming, trust, and application meaning. This chapter spends its entire length redeeming that opening promise, in order, using nothing invented for the occasion.

## Worked Example

Trace the full journey, step by step, using only mechanisms already built in Chapters 1-19.

**1. Joining Wi-Fi.** The laptop associates with the café's access point over a shared radio medium (Ch. 2, Ch. 4) — signals become frames, addressed at the link layer using MAC addresses the access point and laptop exchange directly.

**2. Obtaining local configuration.** Once associated, the laptop still has no IP address, no default gateway, and no DNS resolver address. It obtains all three via DHCP (IPv4) and/or SLAAC plus router advertisements (IPv6) — Chapter 7's local configuration exchange, itself carried as ordinary frames on the link just joined.

**3. Deciding local versus remote.** The laptop knows this book's website's hostname, not yet its address, and in any case, a hostname isn't something the link layer or IP layer forwards by — Chapter 8 established that the very first decision for any outbound traffic is whether the destination is on-link or must go through a gateway. The DNS resolver's own address, just obtained in step 2, is itself somewhere the laptop must reach — almost always off-link, so this local-versus-remote decision happens immediately, before resolution can even begin.

**4. Resolving neighbors.** To reach the gateway (an off-link destination in general, but the gateway itself is always on-link by definition), the laptop needs the gateway's link-layer address — ARP for IPv4, Neighbor Discovery for IPv6 (Ch. 8). Every packet the laptop sends toward any off-link destination, for the rest of this journey, gets framed to this same gateway's link-layer address, not to the final destination's.

**5. Sending the DNS query.** With the gateway's link-layer address resolved, the laptop can now actually reach its DNS resolver, itself possibly several hops away. Assume, for this walkthrough, a conventional query over UDP (Ch. 13) — a single small question-and-answer exchange that doesn't need TCP's ordered byte stream. That's the common case, not a rule: DNS is required to support TCP as well (for responses too large for one UDP datagram, and for zone transfers between servers), and is increasingly carried over TLS, HTTPS, or QUIC for privacy — UDP is DNS's traditional default, not something inherent to how naming resolution works.

**6. Forwarding through gateways and autonomous systems.** Each packet along the way — the DNS query, and later, every packet of the actual connection — gets forwarded hop by hop, each router along the path consulting its own routing table and making one local next-hop decision via longest-prefix matching (Ch. 9), tolerating the possibility of loss, TTL expiry, or an ICMP error at any point (Ch. 10). If the resolver or the eventual server sits outside the café's own network, that forwarding likely crosses autonomous system boundaries, governed by the route information those independently operated networks have exchanged via BGP (Ch. 11).

**7. Resolving the hostname.** The recursive resolver performs its own delegation walk — root, then the relevant top-level domain, then this site's authoritative servers — or serves a cached answer if it already holds one within its TTL (Ch. 17). The laptop receives back an IP address.

**8. Creating transport state.** With an address in hand, the laptop's operating system opens a TCP connection to port 443 on that address: a three-way handshake establishes shared sequence-number state between the two ends (Ch. 12, Ch. 14), and from here on, flow control and congestion control (Ch. 15) govern how much data can safely be in flight. Somewhere along this path, the connection may pass through NAT at the café's own router, translating the laptop's private address, and possibly a reverse proxy at the hosting end (Ch. 16).

**9. Establishing TLS.** Inside that TCP connection, the browser and server negotiate encryption, the server presents a certificate the browser validates against a trusted certificate authority and the requested hostname, and both sides derive a shared secret via key exchange (Ch. 18). From this point on, everything is encrypted and integrity-protected.

**10. Sending HTTP requests and receiving the response.** Inside the now-protected channel, the browser sends a `GET` request for the page's path, with appropriate headers; the server responds with a status code and a body (Ch. 19). If this is the article page, the returned HTML itself references a stylesheet, a handful of images, and perhaps a script — each one triggering its own separate HTTP request, possibly its own separate TCP connection and TLS session, following this exact same chain from step 8 onward, before the page the user actually sees is fully assembled.

Every one of these ten steps used a mechanism built in an earlier chapter. Nothing here was new.

## Core Intuition

A page load is not one action. It is a long, ordered chain of smaller mechanisms — link association, local configuration, address resolution, hop-by-hop forwarding, name resolution, transport-state establishment, encryption negotiation, and structured application exchange — each one solving a distinct problem this book built up over nineteen chapters, cooperating without any single component holding the whole picture at once.

## Technical Explanation

There is no new mechanism to explain here — that is the point of this chapter. What's worth being explicit about is the *shape* of the dependency chain, because it's not a strict, always-identical sequence for every request, and even its ordering constraints describe the conventional TCP-and-TLS path this chapter follows, not a universal law every possible design obeys. For that conventional path: local configuration (step 2) genuinely must happen before anything else. DNS resolution (steps 3-7) must happen before transport state can be created, because transport needs a destination address, not just a hostname. Transport state (step 8) must exist before TLS (step 9) can run, since TLS here is layered on top of an already-established TCP connection. On a genuinely fresh connection to a server the browser has no prior relationship with — this chapter's own scenario — the TLS handshake has to complete before the client sends anything HTTP considers meaningful, since that request is itself protected data inside the session Chapter 18 built. That's the case this chapter walks through, not a universal law: a client returning to a server it recently talked to can, under conditions Chapter 24 covers in full, send early application data before its handshake has actually finished — a resumption capability that exists independent of QUIC, on an ordinary TCP-and-TLS connection, not just the QUIC case Chapter 24 leads with. The underlying dependency logic doesn't disappear even then — data still can't be meaningfully protected before appropriate cryptographic state exists, whether that state comes from completing a fresh handshake or resuming a previous one — but "transport step, then a separate, fully-completed TLS step, then HTTP" is this chapter's conventional first-visit path, not the only way to satisfy that logic.

But within that dependency structure, real variation is normal, not exceptional: much of steps 2-4 may be skipped entirely if the laptop already holds valid configuration and cached neighbor information from moments earlier; step 7's DNS resolution may return instantly from cache rather than performing a fresh delegation walk; and step 10 in particular fans out into many parallel repetitions of steps 8-10 for the page's various embedded resources, not one single pass through the whole chain. The chain's *ordering constraints* are fixed; how much of the chain actually executes, and how many times, depends on what's already cached or already open.

## Packet-Journey Checkpoint

This chapter *is* the checkpoint — there is no further scenario to return to beyond the one just traced in full above.

## Common Misconceptions

### *The steps always occur in one fixed, fully serialized order.*

**Why it's wrong:** A numbered ten-step list, read start to finish, looks like it must always execute start to finish, in full, every time.

**Correct intuition:** For this chapter's conventional TCP-and-TLS path, the dependency ordering (configuration before resolution, resolution before transport, transport before TLS, TLS before HTTP) holds, but many steps are conditionally skipped when cached state already satisfies them, step 10 in particular repeats many times in parallel for a page's various resources, and — as Chapter 24 shows — not every transport design even keeps transport and TLS as two strictly separate sequential steps to begin with.

**Analogy:** A recipe's steps have a fixed dependency order (you can't frost a cake before baking it), but a baker who already has batter prepared skips straight past the steps that produced it.

### *Every page load creates all of this state from scratch.*

**Why it's wrong:** Since the full chain is capable of running from a cold start, it's easy to assume it always does.

**Correct intuition:** DHCP leases, DNS cache entries, TCP connections, and TLS sessions can all be reused across multiple requests when their respective validity conditions (lease time, TTL, still-open connection, still-valid session) hold — reuse, not fresh creation, is the common case for a browser actively used for a while.

**Analogy:** A commuter who already has a transit pass in hand doesn't repeat the entire process of buying one for every single ride.

### *The browser has complete visibility into every intermediate hop.*

**Why it's wrong:** The browser clearly knows the final result — the page rendered or an error shown — which can feel like it implies visibility into everything that produced that result.

**Correct intuition:** The browser and operating system see their own local steps (DHCP, DNS query and answer, TCP and TLS state) directly, but the actual hop-by-hop forwarding across routers and autonomous systems (steps 6) is invisible to them by design — Chapter 9 established that no single component holds the whole path.

**Analogy:** A customer who mails a letter knows it was accepted at the post office and knows it arrived — the specific sorting facilities and trucks it passed through in between are not visible to them at all.

## Practical Implications

When troubleshooting "the site won't load," this ten-step chain is a genuinely usable checklist, not just a teaching device: is there link-layer connectivity at all; does the device have valid local configuration; does DNS resolution succeed; does a TCP connection to the resolved address establish; does TLS validate; does the HTTP request return a success status. Each step corresponds to a specific, narrow class of failure, and Chapter 29 turns exactly this chain into a formal troubleshooting method. For now, the practical value is simpler: the next time "loading a webpage" looks instantaneous and effortless, it's worth remembering it's actually the tail end of nineteen chapters' worth of cooperating mechanisms, most of them invisible specifically because they worked.

## Key Takeaway

**A page load is not one operation but a coordinated sequence of cached decisions, local lookups, packet forwarding, transport state, cryptographic negotiation, and application exchanges.**

## What to Remember

- Local configuration (Ch. 7) must exist before anything else in the chain can run.
- DNS resolution (Ch. 17) discovers the *remote* destination's IP address; address resolution (Ch. 8, ARP/Neighbor Discovery) separately discovers the *local* gateway's link-layer address — two different questions at two different layers, not the same lookup twice. Address resolution has to happen just to reach the gateway at all, even to send the DNS query itself; both may be served from cache rather than freshly performed.
- Hop-by-hop forwarding (Ch. 9-11) happens for every packet in the exchange, invisibly to the browser, one local next-hop decision at a time.
- Transport state (Ch. 12, 14-15) must be established before TLS (Ch. 18) can run on top of it.
- On a genuinely fresh connection, TLS must complete before HTTP (Ch. 19) can send anything meaningful, since HTTP's request is itself protected data inside the session — but a returning client can resume a prior session and send early data before the handshake finishes, over plain TCP, independent of whether QUIC is involved at all (Chapter 24 covers this in full).
- A single perceived page load fans out into many parallel repetitions of the transport-through-HTTP steps for its embedded resources.
- This chain's dependency order describes the conventional TCP-and-TLS path; how much of it actually executes on a given request depends heavily on what's already cached, leased, or still open, and Chapter 24 shows a design (QUIC) that combines steps this chapter treats as strictly sequential.

## The Next Obvious Question

*Why can two working connections feel radically different in speed and responsiveness?*

---

**Glossary terms added this chapter:** none — this chapter introduces no new terms, only integrates Chapters 1-19's existing vocabulary.

**Misconceptions logged this chapter:** none new — see "Common Misconceptions" above, which are integration-specific framings rather than new registry entries.

**Concept-graph entries checked off:** none — no concepts are assigned `introduced_in: 20` in concept-graph.yaml, by design.

**Diagrams used this chapter:** none — a single diagram covering all ten steps would summarize the entire chapter rather than teaching one idea, which the diagram policy (style-guide.md §4) rules out; the numbered prose trace carries the full journey instead.
