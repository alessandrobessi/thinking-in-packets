# References — Chapter 11: The Internet Is a Network of Networks

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 4271 — *A Border Gateway Protocol 4 (BGP-4)*, IETF, 2006. Defines the route-advertisement/withdrawal mechanism and AS-path attribute described at the mechanism level in this chapter.
- RFC 1930 — *Guidelines for creation, selection, and registration of an Autonomous System (AS)*, IETF, 1996. Defines what an autonomous system is administratively.

## Historical sources

- The railway-companies analogy is original to this book, not drawn from a specific historical source.

## Implementation documentation

- Internet Assigned Numbers Authority (IANA), Autonomous System Number registry — public record of AS number allocation.

## Empirical claims

- Route-convergence timescales (seconds to minutes) are a widely-documented, general characteristic of BGP; no single number is cited in-chapter, deliberately, since actual convergence time varies enormously by topology and event type.

## Known simplifications (may need later technical review)

- The chapter does not cover BGP path-selection attributes (LOCAL_PREF, MED, AS-path prepending) by name — it stays at "policy decides" per blueprint §5's explicit non-goal of avoiding a configuration guide.
- Route-origin validation mechanisms (like RPKI) are gestured at only through the "reachable prefix ≠ legitimate origin" misconception, not explained as a named defense.
