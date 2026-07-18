# References — Chapter 21: Where Time Goes

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- Bufferbloat and its mitigation: bufferbloat.net project documentation;
  IETF RFC 8290 (*The Flow Queue CoDel Packet Scheduler and Active Queue
  Management Algorithm*, 2018) describes a deployed mitigation for the
  queueing-delay problem this chapter names conceptually.

## Historical sources

- Stuart Cheshire, "It's the Latency, Stupid" (1996 essay, widely
  reprinted) — an early, influential plain-language argument that
  bandwidth improvements alone don't fix perceived slowness, the same
  distinction this chapter builds from first principles.
- Jim Gettys and Kathleen Nichols, "Bufferbloat: Dark Buffers in the
  Internet," ACM Queue, 2011 — the paper that named and popularized
  "bufferbloat" as a distinct, diagnosable problem.

## Implementation documentation

- Google's "Web Vitals" and general CDN/browser engineering
  documentation on Round-Trip Time (RTT) and Time to First Byte (TTFB) as
  distinct, separately-optimized metrics from raw throughput.

## Empirical claims

- The geostationary-satellite propagation-delay figure (~480 ms round
  trip) is a standard physics-derived estimate (orbital altitude ~35,786
  km, speed of light in vacuum ~299,792 km/s) used consistently across
  satellite ISP documentation as of the mid-2020s; low-earth-orbit
  satellite constellations achieve substantially lower RTT by flying much
  closer to Earth, a distinction this chapter's example deliberately
  scopes to geostationary systems only.

## Known simplifications (may need later technical review)

- The performance-timeline diagram's specific millisecond values are
  illustrative, not measured — the chapter is explicit that the point is
  the decomposition into stages, not any particular link's real numbers.
- Bandwidth-delay product is introduced at the level of intuition only
  (as the blueprint's scope requires); no TCP window-sizing formula is
  derived.
