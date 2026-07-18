# References — Chapter 09: One Hop at a Time

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 1812, *Requirements for IP Version 4 Routers*, IETF, 1995 (general router forwarding-behavior baseline, including longest-prefix-match requirements).
- RFC 4632, *Classless Inter-domain Routing (CIDR)* (already cited Ch. 6; longest-prefix matching is CIDR's direct consequence).

## Historical sources

## Implementation documentation

## Empirical claims

## Known simplifications (may need later technical review)

- The worked example uses a small, hand-picked routing table for clarity; production routers (especially Internet backbone routers) hold hundreds of thousands of prefixes and use specialized data structures (e.g. tries) for fast longest-prefix-match lookups — an implementation detail deliberately kept out of the main text per blueprint.md's scope.
- Equal-cost multi-path (ECMP) routing, where a router load-balances across multiple equally-specific, equally-good routes, is not covered — the chapter assumes one best match per destination for pedagogical simplicity.
