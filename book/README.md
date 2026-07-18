# Thinking in Packets

*A Mental Model for Computer Networks*

This is the manuscript, organized by Part and Chapter following an
explicit concept dependency graph. Chapters are numbered globally (01–30)
and must be read in order — each chapter's vocabulary is a prerequisite
for the next.

The manuscript teaches primarily through prose — a real-world story, a
distinct worked example, precise technical explanation, and one bolded
key-takeaway sentence per chapter — with up to two inline Mermaid diagrams
per chapter where topology or sequence genuinely helps (`style-guide.md`
§4). Every chapter returns to one recurring scenario, the Packet-Journey
Checkpoint: a laptop joins café Wi-Fi and opens an HTTPS website.

Supporting project files: [`../style-guide.md`](../style-guide.md) (voice,
diagram policy, analogy registry), [`../glossary.md`](../glossary.md),
[`../misconceptions.md`](../misconceptions.md),
[`../concept-graph.md`](../concept-graph.md).

**Status:** The full manuscript, Parts I–VI (Chapters 1–30), is written —
all 155 tracked concepts marked written in `../concept-graph.md`, all
structural validators (`../scripts/validate_*.py`) passing. This is a
first complete draft, not a finished, professionally edited book.

---

## Part I — From Signals to Local Networks

1. [The Invisible Journey](part-1-signals-and-local-networks/01-the-invisible-journey.md)
   — *How can one application send information to another machine at all?*
2. [Turning Information Into Signals](part-1-signals-and-local-networks/02-turning-information-into-signals.md)
   — *Before a message can travel, how can a physical medium carry a bit?*
3. [Giving Bits Boundaries](part-1-signals-and-local-networks/03-giving-bits-boundaries.md)
   — *Once bits are moving, how does a receiver know which bits belong together?*
4. [Delivery Across One Local Network](part-1-signals-and-local-networks/04-delivery-across-one-local-network.md)
   — *Once messages have boundaries, how do they reach the correct device on a local network?*
5. [Why One Giant Network Does Not Work](part-1-signals-and-local-networks/05-why-one-giant-network-does-not-work.md)
   — *If switches can connect local devices, why not build one enormous local network?*

## Part II — Building an Internet

6. [Addresses That Describe Where to Route](part-2-building-an-internet/06-addresses-that-describe-where-to-route.md)
   — *If many local networks exist, how can a destination be identified across them?*
7. [Joining a Network](part-2-building-an-internet/07-joining-a-network.md)
   — *How does a newly connected device learn its address and its way out?*
8. [Finding the Next Device](part-2-building-an-internet/08-finding-the-next-device.md)
   — *Once it knows the destination and gateway, how does it reach the next device on the local link?*
9. [One Hop at a Time](part-2-building-an-internet/09-one-hop-at-a-time.md)
   — *Once a router receives a packet, how does it choose the next hop?*
10. [Best Effort, Limits, and Failure Signals](part-2-building-an-internet/10-best-effort-limits-and-failure-signals.md)
    — *What happens when the expected path fails or the packet cannot continue?*

## Part III — End-to-End Conversations

11. [The Internet Is a Network of Networks](part-3-end-to-end-conversations/11-the-internet-is-a-network-of-networks.md)
    — *How do independently operated networks exchange enough information to connect the world?*
12. [From a Host to a Process](part-3-end-to-end-conversations/12-from-a-host-to-a-process.md)
    — *Once a packet reaches the correct machine, how does it reach the correct application?*
13. [Sending Independent Datagrams](part-3-end-to-end-conversations/13-sending-independent-datagrams.md)
    — *What is the simplest useful service the transport layer can provide?*
14. [Building a Reliable Stream](part-3-end-to-end-conversations/14-building-a-reliable-stream.md)
    — *What if an application needs all the data, in order, despite loss?*
15. [Reliability Without Collapse](part-3-end-to-end-conversations/15-reliability-without-collapse.md)
    — *How can reliability avoid overwhelming the receiver or the network itself?*

## Part IV — Names, Trust, and the Web

16. [The Network in the Middle](part-4-names-trust-and-the-web/16-the-network-in-the-middle.md)
    — *What happens when intermediaries rewrite, filter, or relay traffic?*
17. [Naming a Moving World](part-4-names-trust-and-the-web/17-naming-a-moving-world.md)
    — *How can people use stable names instead of numerical addresses?*
18. [Establishing Trust on an Untrusted Network](part-4-names-trust-and-the-web/18-establishing-trust-on-an-untrusted-network.md)
    — *How can a client verify a server and keep the conversation private?*
19. [The Language of the Web](part-4-names-trust-and-the-web/19-the-language-of-the-web.md)
    — *Once a secure channel exists, how does the Web exchange meaningful requests and responses?*
20. [What Happens When You Visit a Website](part-4-names-trust-and-the-web/20-what-happens-when-you-visit-a-website.md)
    — *Can we now trace an entire page load without skipping any layer?*

## Part V — Speed, Scale, and Modern Protocols

21. [Where Time Goes](part-5-speed-scale-and-modern-protocols/21-where-time-goes.md)
    — *Why can two working connections feel radically different in speed and responsiveness?*
22. [Bringing Services Closer and Spreading the Work](part-5-speed-scale-and-modern-protocols/22-bringing-services-closer-and-spreading-the-work.md)
    — *How can one service respond quickly and reliably to millions of users?*
23. [Many Requests, Fewer Connections](part-5-speed-scale-and-modern-protocols/23-many-requests-fewer-connections.md)
    — *Why did the Web need multiple simultaneous exchanges over fewer connections?*
24. [Rebuilding Transport for the Modern Web](part-5-speed-scale-and-modern-protocols/24-rebuilding-transport-for-the-modern-web.md)
    — *Why move modern Web transport into QUIC instead of continuing to modify TCP?*
25. [Different Applications, Different Networks](part-5-speed-scale-and-modern-protocols/25-different-applications-different-networks.md)
    — *Why do video calls, streams, games, and messages choose different trade-offs?*

## Part VI — Networks in Production

26. [Networks Made of Software](part-6-networks-in-production/26-networks-made-of-software.md)
    — *How can physical networking be exposed as programmable virtual infrastructure?*
27. [Networking Moving Applications](part-6-networks-in-production/27-networking-moving-applications.md)
    — *How does communication work when applications move among containers and machines?*
28. [Security and Resilience Are Architectural](part-6-networks-in-production/28-security-and-resilience-are-architectural.md)
    — *How can a network remain reachable, secure, and resilient under failure or attack?*
29. [Seeing and Troubleshooting the Network](part-6-networks-in-production/29-seeing-and-troubleshooting-the-network.md)
    — *When something breaks, how can we identify the failing layer rather than guess?*
30. [How to Think About Any Network](part-6-networks-in-production/30-how-to-think-about-any-network.md)
    — *How can this mental model be used to understand whatever networking system comes next?*
