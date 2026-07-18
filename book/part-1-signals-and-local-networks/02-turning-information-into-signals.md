# Turning Information Into Signals

**Part:** Part I — From Signals to Local Networks

**Concept Level:** Level 1, per concept-graph.md

**Prerequisites:** Chapter 1 (message, network, protocol)

**New concepts introduced:** bit, signal, encoding, physical medium, noise, bandwidth, propagation latency

---

## Opening Question

*Before a message can travel, how can a physical medium carry a bit?*

## Real-World Story

Two friends, camping on opposite hills, want to talk after dark with no phones and no line of sight for shouting. They have one flashlight between them. Before splitting up, they agree on a simple code: one short flash means "yes," one long flash means "no," and two short flashes means "come back to camp."

Later that night, one of them flashes: short, short. The other sees it and starts walking back.

Notice what actually crossed the valley between the two hills. It wasn't the *meaning* "come back to camp" — meaning isn't the kind of thing that can travel through open air. What crossed the valley was light: photons, physically real, physically detectable, arriving as a pattern of brightness over time. The meaning only exists because both people had already agreed, beforehand, on how to interpret that pattern. A third camper on a nearby hill, seeing the exact same flashes, would see only light — two brief flashes and then darkness — with no idea it meant anything at all, because they weren't part of the agreement.

This is the entire relationship between information and physical reality, and it never really goes away, no matter how sophisticated networking gets. Something physical — light, electricity, radio waves — has to change, over time, in a way a receiver can detect. And separately, sender and receiver have to agree in advance on what those changes are supposed to mean. Neither piece works alone: physical change with no agreed interpretation is just noise, and an agreed interpretation with no physical change to carry it is just an idea, stuck in one person's head.

## Worked Example

To see why "how much a link can carry" and "how quickly a link responds" are two entirely separate properties, compare two very different physical connections carrying the exact same request.

**Link A: a satellite internet connection.** A ground station beams a signal up roughly 22,000 miles to a satellite in geostationary orbit, which beams it back down to a receiver on the other side of the world — one leg of the journey, about 44,000 miles of travel, one way. This link can actually carry a substantial amount of data every second — modern satellite links are not narrow. But light itself, however fast, still takes a measurable amount of time to cover that distance: roughly a quarter of a second for the signal to arrive at all, before any equipment processing time is even added in. Send one tiny request — "give me the current time" — and the answer has to make that same up-and-down journey a second time, in the opposite direction, before it can reach you: roughly half a second in total, for a request that carried almost no data. The link's *capacity* was barely touched; its *unavoidable delay* was the entire story.

**Link B: a short cable between two machines sitting in the same server rack.** This link might carry a comparable, even smaller, amount of data per second than the satellite link. But the physical distance the signal has to cross is measured in inches, not tens of thousands of miles. Send that same tiny request, and the answer comes back in a small fraction of a millisecond — not because this link is somehow "faster" in the way a faster processor is faster, but because there's almost no distance for the signal to cross before someone can respond.

Now send something large over each link instead — say, a multi-gigabyte file. Here the story flips. The satellite link's quarter-second delay barely matters anymore, because it only gets paid once, at the start; what dominates the total time is how many bits per second the link can physically push through, sustained over the whole transfer. The short in-rack cable, despite its tiny delay, might take just as long, or even longer, to move that same file if its actual carrying capacity happens to be lower.

Two completely different properties were on display: how long a signal takes to physically arrive at all (dominated the tiny request), and how much the link can carry per second once data is flowing (dominated the large file). A link can be high-capacity and slow-to-respond, like the satellite; or lower-capacity and near-instant to respond, like the short cable. Neither property predicts the other.

## Core Intuition

A network link doesn't move bits the way a conveyor belt moves boxes. It moves a physical signal — a voltage that rises and falls, a light pulse that turns on and off, a radio wave whose properties shift — and a bit only exists because sender and receiver have agreed, in advance, on a specific way of turning "0" and "1" into physical changes, and back again. The signal is real and physical. The bit is an agreed-upon interpretation of that physical reality, exactly like the flashlight code: light crossed the valley; "come back to camp" existed only in two people's shared understanding of what that light meant.

## Technical Explanation

A **bit** is the smallest unit of digital information: a single 0 or a single 1. A bit, by itself, is not a physical thing — it's an abstract value that has to be represented by something physical before it can move anywhere.

A **signal** is that physical representation: a voltage level on a copper wire, a pulse of light in a fiber-optic cable, a radio wave's amplitude or frequency, a pulse from a flashlight. A signal is whatever a **physical medium** — copper cable, fiber-optic glass, open air, in the case of wireless links — is actually capable of carrying and a receiver is actually capable of detecting.

**Encoding** is the agreed-upon scheme for turning bits into signal changes, and signal changes back into bits — the flashlight friends' "short flash means yes" is a two-symbol encoding scheme; real network links use encoding schemes that are far more elaborate, packing many bits into each physical change, but the underlying idea is identical: an agreement about what a given physical pattern is supposed to represent.

No physical medium is perfectly clean. **Noise** is any unwanted physical interference — electrical interference near a copper cable, other radio transmissions overlapping a wireless signal, physical imperfections in a fiber connector — that can distort a signal enough that the receiver misreads what was actually sent. Every real link has to be built with the expectation that some of what arrives will be corrupted by noise; later chapters cover how networks detect, and sometimes correct, exactly this problem.

Two properties of a link matter enormously and are easy to conflate, so it's worth stating both precisely, using what the worked example already demonstrated.

**Bandwidth** is how much data a link can carry per unit of time, once data is actually flowing — its carrying capacity, typically measured in bits per second. A higher-bandwidth link can sustain a higher rate of data transfer.

**Propagation latency** is how long it takes a signal to physically travel from one end of a link to the other, mostly governed by distance and the physical speed at which the signal moves through that particular medium (light in fiber travels only slightly slower than light in a vacuum; electrical signals in copper are somewhat slower still). Propagation latency is paid once per trip, essentially regardless of how much data is being sent, because it's a property of distance and physics, not of data volume.

These two properties are independent, which is exactly what the satellite-versus-rack-cable example showed: a link can have generous bandwidth and still have substantial propagation latency, because a longer physical distance simply takes light or electricity longer to cross, no matter how wide the "pipe" is. Conflating the two, treating "bandwidth" and "speed" as synonyms, is one of the most common sources of confusion in networking, and this book will keep them carefully separate throughout.

## Packet-Journey Checkpoint

The café visitor's laptop connects to the café's access point over Wi-Fi: a real physical medium, in this case radio waves rather than a cable, subject to noise from other devices sharing the same frequencies, and constrained by both a maximum bandwidth and a small but real propagation latency between laptop and access point. Every later step of that visitor's page load, no matter how abstract it will eventually sound in terms of packets, requests, and responses, ultimately rests on some physical medium somewhere actually carrying a changing signal that both ends have agreed on how to interpret. That dependency never disappears; it just becomes invisible once enough layers are stacked on top of it.

## Common Misconceptions

### *"Bits physically travel as tiny zeros and ones."*

**Why it's wrong:** Because software represents everything as 0s and 1s, and because that abstraction is so convenient and so consistent, it's easy to imagine some tiny physical "0" or "1" object actually flowing down a cable.

**Correct intuition:** What actually travels is a continuously changing physical signal — a voltage, a light pulse, a radio wave. "0" and "1" are the agreed-upon interpretation applied to specific patterns in that signal, not physical objects in their own right.

**Analogy:** In the flashlight code, no physical "yes" or "no" crossed the valley — only light, in a pattern two people had already agreed to interpret as yes or no.

### *"Bandwidth and latency are the same thing."*

**Why it's wrong:** Both properties get casually described as "how fast" a connection is, which makes them easy to merge into one vague idea.

**Correct intuition:** Bandwidth is carrying capacity — how much can flow per second once it's flowing. Propagation latency is trip time — how long one signal takes to physically arrive at all. A link can score high on one and low on the other, as the satellite and rack-cable example showed directly.

**Analogy:** The satellite link and the rack cable from the worked example above: one had generous carrying capacity but a long, physics-bound trip time; the other had a tiny trip time regardless of its capacity — direct proof that the two properties vary independently of each other.

### *"Wireless communication has no medium."*

**Why it's wrong:** Because there's no visible cable, it's easy to assume Wi-Fi and cellular signals travel through nothing at all.

**Correct intuition:** Radio waves are a physical medium exactly like copper or fiber — they're electromagnetic signals propagating through space (or air), subject to distance, interference, and noise from other transmissions, just like any other physical carrier.

**Analogy:** The flashlight beam itself is "wireless" in exactly this sense — no wire connects the two hills — but it is still unmistakably physical: block it, and the message doesn't arrive.

### *"A stronger signal automatically means more application throughput."*

**Why it's wrong:** A strong, clear signal certainly helps, and weak signal strength is a common real-world cause of poor performance, which makes it tempting to treat signal strength as the entire story.

**Correct intuition:** Once a signal is strong enough to be reliably detected above the noise floor, additional strength does not by itself raise a link's bandwidth; actual throughput depends on the link's encoding scheme, its available bandwidth, competing traffic sharing the same medium, and, as later chapters will show, plenty of behavior far above the physical layer.

**Analogy:** Shouting louder doesn't let you say more words per minute; past the point where you can already be clearly heard, extra volume adds nothing to how much information gets across.

## Practical Implications

This distinction pays off immediately when reading any connectivity spec sheet or complaint. "High-bandwidth" and "low-latency" are separate marketing claims, and a product can genuinely deliver one without the other — a satellite link can be marketed as high-bandwidth while still being unsuitable for anything latency-sensitive, like a video call or competitive game. When someone says a connection "feels slow" for a task involving many small back-and-forth exchanges, suspect latency before suspecting bandwidth; when a large download crawls despite a good ping time, suspect the reverse. Keeping the two separate turns a vague complaint into a specific, checkable hypothesis.

## Key Takeaway

**A link carries changing physical signals; bits exist because sender and receiver agree on how to interpret those changes.**

## What to Remember

- A bit is an abstract value; a signal is the physical change (electrical, optical, or radio) that actually represents it on a real medium.
- Encoding is the agreed-upon scheme for translating bits into signal changes and back again — an agreement, not a law of physics.
- Every physical medium is subject to noise, which can distort a signal enough to be misread.
- Bandwidth measures carrying capacity (data per second, once flowing); propagation latency measures trip time (how long one signal takes to physically arrive).
- Bandwidth and latency are independent properties — a link can be high on one and low on the other.
- Wireless links use a physical medium (radio waves) exactly as real, and exactly as subject to interference, as any cable.
- Signal strength matters up to reliable detection, but beyond that point it doesn't by itself increase throughput.

## The Next Obvious Question

*Once bits are moving, how does a receiver know which bits belong together?*

---

**Glossary terms added this chapter:** bit, signal, encoding, physical medium, noise, bandwidth, propagation latency → append to `/glossary.md`

**Misconceptions logged this chapter:** `bandwidth-equals-latency` → already seeded in `/misconceptions.md`

**Concept-graph entries checked off:** bit, signal, encoding, physical-medium, noise, bandwidth, propagation-latency → update `/concept-graph.yaml`, regenerate `/concept-graph.md`

**Diagrams used this chapter:** none
