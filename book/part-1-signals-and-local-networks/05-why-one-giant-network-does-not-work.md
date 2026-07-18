# Why One Giant Network Does Not Work

**Part:** Part I — From Signals to Local Networks

**Concept Level:** Level 2, per concept-graph.md

**Prerequisites:** Chapter 4 (switch, forwarding table, broadcast)

**New concepts introduced:** broadcast domain, failure domain, administrative boundary, internetwork

---

## Opening Question

*If switches can connect local devices, why not build one enormous local network?*

## Real-World Story

A fast-growing company starts out with one small head office. Every announcement, every delivery, every internal lookup, "who's the contact for this client," "where does this shipment go," runs through that one office, and for a while this works fine — the office is small enough that one coordinator can just know these things or find them out quickly.

The company keeps growing, but leadership decides to keep running everything through that same single office, on principle, rather than letting regional teams handle their own local matters. Every new hire anywhere in the world has their onboarding paperwork routed through the original office. Every delivery to every new regional warehouse gets scheduled by the same small coordination team. Every question a regional manager has, even a purely local one, "which supplier delivers on Tuesdays," gets forwarded to headquarters, because that's where "the answer" is assumed to live.

Within a couple of years, this collapses under its own weight. The original office is now fielding an overwhelming volume of requests, many of them purely local matters that have nothing to do with headquarters at all. A single miscommunication or system outage at that one office can now stall operations on the other side of the world, even though the underlying local business at each regional site is running fine on its own. Nobody at headquarters actually has enough context to make every regional decision well; local teams have that context, but weren't given the authority or the direct connections to act on it themselves.

The company eventually reorganizes around regional offices, each empowered to handle its own local hiring, deliveries, and questions directly, with headquarters stepping in only for the smaller number of matters that genuinely span regions. Nothing about the company's total size caused the original collapse — the same total number of people, organized around regional boundaries instead of one central bottleneck, worked fine. What failed was routing everything, including purely local matters, through one shared, ever-growing point of coordination.

## Worked Example

Compare two networks built with exactly the same switching technology described in the previous chapter: a real 20-device office LAN, and a hypothetical single LAN attempting to connect every device on Earth.

**Broadcasts.** Recall from Chapter 4 that a switch floods a frame to every port when it hasn't yet learned where the destination lives, and some traffic (a device announcing itself when it first joins, for instance) is deliberately sent to everyone on purpose. In a 20-device office, an occasional broadcast reaches 20 devices — a negligible cost. On a single worldwide LAN, every one of those same broadcasts would, in principle, have to reach every device on the planet simultaneously. Even a small, occasional amount of broadcast traffic, multiplied across billions of devices all sharing one broadcast domain, would consume enormous capacity for messages almost none of the recipients have any use for.

**Forwarding table size.** The office's switches only ever need to remember roughly 20 MAC addresses — small enough to fit trivially in memory, learned and re-learned in moments. A worldwide single-LAN switch would, over time, need to learn and retain a mapping for every device on Earth: billions of entries, constantly changing as devices join, leave, and move, on hardware that has real, finite memory.

**Failures.** If a switch fails in the 20-device office, it affects, at most, the devices plugged into that one switch — a contained, quickly diagnosable problem. On a worldwide single LAN, there is no equivalent containment: a failure or a misbehaving device anywhere on that flat network could, depending on exactly what went wrong, degrade or disrupt delivery for devices anywhere else on the same network, since they're all, in a real sense, part of the same shared system.

**Ownership and change.** The office's switches are administered by one team, who can reconfigure, replace, or troubleshoot them without needing anyone else's permission. A worldwide LAN would need to somehow be jointly administered by every organization operating a device on it, with no natural boundary indicating who is responsible for which part, or who is allowed to make which changes — considerably closer to the collapsed company from the opening story than to a functioning system.

Every one of these problems traces back to the same root cause: a flat network, where every device is a direct, undifferentiated peer of every other device with no internal boundaries, has costs, broadcast traffic, table size, blast radius of failures, that grow directly with the number of devices on it, with no natural point at which to contain that growth.

## Core Intuition

A single flat network's costs, broadcast traffic, table size, failure impact, don't stay proportionate as more devices join; they compound, because every device remains a direct peer of every other device with nothing standing between them. The fix is not "better switches" or "more capacity" — it's introducing boundaries: dividing devices into separate, bounded local networks, each small enough to manage its own broadcast traffic, its own table sizes, and its own failures internally, and connecting those separate networks through a different mechanism entirely, rather than trying to flatten everything into one indefinitely large local network.

## Technical Explanation

The set of devices that a given broadcast (Chapter 4) actually reaches is called a **broadcast domain**. Every device within one broadcast domain shares in the cost of that domain's broadcast traffic; every device outside it does not. A single switch, or several switches connected together as in the previous chapter's worked example, form one broadcast domain — which is precisely why that domain can't simply be grown without limit: every additional device joining it adds to what every other device in that same domain has to absorb.

Closely related is the idea of a **failure domain**: the set of devices that a given failure or misbehavior can actually affect. In a well-bounded local network, a failure domain is naturally limited to that network's own devices. Collapsing many networks into one enormous flat network also collapses their failure domains into one enormous shared failure domain, exactly as the worldwide-LAN comparison showed.

An **administrative boundary** is a dividing line marking where responsibility for a network's configuration, maintenance, and troubleshooting belongs to one specific team or organization, and where it belongs to another. The office LAN has a clear administrative boundary: one team owns and can change it. A worldwide single LAN has no natural administrative boundary at all, which is exactly the governance failure the opening company's story dramatized: nobody has clear ownership of a problem that spans everyone.

The solution this chapter has been building toward is an **internetwork**: rather than one unbounded flat network, many separate, individually bounded local networks, each with its own contained broadcast domain, its own contained failure domain, and its own clear administrative boundary, connected to each other through a distinct mechanism designed specifically for crossing between networks rather than operating within one. Deliberately, this chapter does not yet say what that connecting mechanism is; that's the subject of Part II. What matters here is why it has to exist at all: hierarchy and boundaries between networks are not bureaucratic overhead layered on top of a "purer" flat design. They are what makes networking at any real scale possible in the first place, for exactly the same reason the reorganized company's regional offices, not its original single office, were what let it keep growing.

| | 20-device office LAN | Hypothetical worldwide single LAN |
|---|---|---|
| Broadcast reaches | ~20 devices | every device on the network |
| Forwarding table size | tens of entries | billions of entries, constantly changing |
| A switch failure affects | devices on that switch | potentially the whole flat network |
| Administered by | one team | no natural single owner |

## Packet-Journey Checkpoint

The café's local network, everything the previous chapter covered, is exactly one bounded broadcast domain and one bounded failure domain, administered by whoever runs the café's network, entirely separate from the visitor's HTTPS destination's own local network, wherever that server actually sits. The two networks are connected through mechanisms this book has not introduced yet, but the fact that they are separate, bounded networks in the first place, rather than one shared flat network spanning the café and the destination server, is precisely what this chapter has been explaining.

## Common Misconceptions

### *"Adding more switches can scale a LAN indefinitely."*

**Why it's wrong:** Since a single switch clearly handles more devices by adding another switch, it's tempting to assume this simply continues working at any scale, with enough equipment.

**Correct intuition:** Adding switches within one broadcast domain doesn't shrink that domain's broadcast traffic, its shared table-size pressure, or its shared failure exposure — it just adds more devices sharing all three costs, which is exactly the growth pattern this chapter showed compounding rather than staying proportionate.

**Analogy:** Hiring more staff at the original company's single head office didn't fix the underlying problem of routing every regional matter through one place; it just added more people absorbing the same structural bottleneck.

### *"Hierarchy is merely organizational bureaucracy."*

**Why it's wrong:** Boundaries, regional divisions, and layers of administration are often experienced as slow or restrictive in everyday organizational life, which makes "hierarchy" sound like something imposed for control rather than necessity.

**Correct intuition:** In networking, hierarchy is what contains broadcast traffic, bounds forwarding-table size, limits failure impact, and gives each part a clear owner — the worked example's comparison shows these costs becoming unmanageable specifically in the absence of any dividing structure.

**Analogy:** The reorganized company's regional offices weren't bureaucratic overhead; they were what let the company keep functioning as it grew, exactly where the single-office structure had already collapsed.

### *"The Internet is one enormous Ethernet network."*

**Why it's wrong:** Because Ethernet and Wi-Fi are the technologies most people directly interact with, and the Internet feels like one continuous experience from a browser's perspective, it's natural to imagine the whole thing as one big version of the same local network from Chapter 4.

**Correct intuition:** The Internet is precisely the opposite: an internetwork of an enormous number of separately bounded, separately administered local networks, connected by mechanisms distinct from local switching, which Part II builds up from scratch.

**Analogy:** A worldwide company built from many regional offices, each running its own local operations, connected by a distinct cross-region communication mechanism, is a far more accurate picture than one single, ever-expanding head office trying to directly handle everything itself.

### *"Network boundaries exist only for security."*

**Why it's wrong:** Boundaries are frequently discussed in the context of firewalls and access control, which are genuinely security-related, making it easy to assume containment is the only reason boundaries exist.

**Correct intuition:** As this chapter demonstrated, boundaries exist first and foremost to contain broadcast traffic, bound forwarding-table size, limit failure impact, and establish clear administrative ownership — properties a network needs regardless of any security consideration at all. Security benefits from these same boundaries, but doesn't create the need for them.

**Analogy:** The reorganized company's regional offices weren't created to keep out intruders; they were created so the company could function and scale at all — security policies, if any, would be a separate decision layered on top of that same structure.

## Practical Implications

This is the pattern to recognize whenever a network design claims to be simpler by flattening boundaries away, "just put everything on one big network," or "why not skip the hierarchy." The costs this chapter walked through, broadcast domains, table growth, failure containment, administrative ownership, don't disappear because a diagram draws one big cloud instead of several connected boxes; they simply reappear, unmanaged, the moment the network actually grows. Recognizing this is also the first real argument, built from first principles rather than asserted, for why the rest of this book needs an entirely different addressing and connecting mechanism, starting in the very next chapter, layered on top of everything Part I has built so far.

## Key Takeaway

**Large-scale networking requires bounded local systems connected by a separate mechanism for crossing between them.**

## What to Remember

- A broadcast domain is the set of devices a given broadcast actually reaches; growing it without bound grows the shared cost of every broadcast along with it.
- A failure domain is the set of devices a given failure can affect; an unbounded flat network has an unbounded failure domain.
- An administrative boundary marks where responsibility for a network's configuration and troubleshooting belongs to one team versus another — a flat, unbounded network has no natural boundary of this kind at all.
- Adding more switching equipment doesn't shrink these costs; it adds more devices sharing them.
- An internetwork is many separately bounded local networks, each with contained broadcasts, contained failures, and clear ownership, connected by a distinct mechanism rather than merged into one flat network.
- Boundaries and hierarchy exist primarily for scaling and containment, not primarily for security, even though security also benefits from them.
- The Internet is the opposite of one giant Ethernet network — it is exactly the bounded, internetworked structure this chapter argues is necessary.

## The Next Obvious Question

*If many local networks exist, how can a destination be identified across them?*

---

**Glossary terms added this chapter:** broadcast domain, failure domain, administrative boundary, internetwork → append to `/glossary.md`

**Misconceptions logged this chapter:** switches-scale-lan-indefinitely, hierarchy-is-bureaucracy, internet-is-one-ethernet, boundaries-only-for-security (in-chapter coverage; `internet-is-one-ethernet` overlaps conceptually with the already-seeded `internet-one-org` from Chapter 1 but is kept distinct here since it's specifically about flat-network structure, not organizational control)

**Concept-graph entries checked off:** broadcast-domain, failure-domain, administrative-boundary, internetwork → update `/concept-graph.yaml`, regenerate `/concept-graph.md`

**Diagrams used this chapter:** none (one plain-markdown comparison table, not a Mermaid diagram)
