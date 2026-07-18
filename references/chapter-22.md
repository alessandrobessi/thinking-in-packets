# References — Chapter 22: Bringing Services Closer and Spreading the Work

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 9111 (*HTTP Caching*, 2022, obsoletes RFC 7234) — the standard
  governing freshness, validation, and cache-control semantics referenced
  conceptually in this chapter.
- RFC 1546 (*Host Anycasting Service*, 1993) — the original conceptual
  proposal for anycast; modern deployment is BGP-based and described in
  RFC 4786 (*Operation of Anycast Services*, 2006).

## Historical sources

- Early CDN architecture is generally credited to Akamai's founding
  (1998), commercializing edge-caching research from MIT; this chapter
  deliberately stays vendor-neutral rather than describing any one
  provider's implementation.

## Implementation documentation

- Major cloud providers' load-balancer documentation (health check
  configuration, session-affinity/sticky-session options) illustrates the
  concepts this chapter covers generically — implementation specifics
  (probe intervals, affinity cookie mechanics) vary by vendor and are
  intentionally not covered here.
- Major cloud providers' Layer 4 vs. Layer 7 load-balancer documentation
  (e.g. "network load balancer" vs. "application load balancer" product
  lines) — source for this chapter's second-pass correction that
  per-connection/flow selection, not per-request selection, is the
  common case for transport-layer load balancers; application-layer
  balancers are the ones that can genuinely pick fresh per HTTP request.

## Empirical claims

- None beyond the general, widely-documented existence of CDN/load-
  balancing architecture patterns; no specific performance numbers are
  claimed in this chapter.

## Known simplifications (may need later technical review)

- The corrected large-transfer explanation (RTT/bandwidth-delay-product effects on how quickly a connection reaches full throughput, rather than "propagation delay per byte") stays at intuition level, deliberately not deriving the bandwidth-delay product or slow-start's ramp curve quantitatively — that arithmetic is left to Chapter 21's own scope.
- Anycast is presented at intuition level only, per blueprint scope — no
  BGP-policy detail on how "closest" is actually determined at the
  routing-protocol level, which can diverge from geographic proximity.
- Cache-consistency and replica-consistency models (eventual vs. strong
  consistency) are gestured at through the "briefly diverge" language but
  not formally defined — that's deliberately out of this book's scope per
  blueprint §5 (not a distributed-systems consistency text).
- Second-pass correction: session affinity was previously framed as a
  general fix for replica divergence; corrected to scope it specifically
  to instance-local state for one user's own traffic, explicit that it
  does not create cross-replica consistency for shared data — the actual
  mechanisms that would (consensus, shared/replicated stores, etc.) are
  named as out of scope, not explained.
- Third-pass correction: "load balancing depends on replication" was
  stated unconditionally; corrected to scope that dependency to load
  balancing across equivalent, interchangeable replicas specifically
  (this chapter's running case), noting that load balancers distributing
  traffic across heterogeneous or partitioned backends are a different,
  unnamed-here pattern that doesn't presuppose replication.
