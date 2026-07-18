# References — Chapter 06: Addresses That Describe Where to Route

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 791, *Internet Protocol* (IPv4), IETF, 1981.
- RFC 8200, *Internet Protocol, Version 6 (IPv6) Specification*, IETF, 2017.
- RFC 4632, *Classless Inter-domain Routing (CIDR): The Internet Address Assignment and Aggregation Plan*, IETF, 2006.
- RFC 1918, *Address Allocation for Private Internets*, IETF, 1996 (source for the private IPv4 ranges named in-chapter).

## Historical sources

- The shift from classful addressing to CIDR in the early 1990s, motivated by IPv4 address-space exhaustion pressure — background context for why hierarchical, variable-length prefixes replaced fixed class boundaries.

## Implementation documentation

- Regional Internet Registries (ARIN, RIPE NCC, APNIC, LACNIC, AFRINIC) publish the top of the real-world hierarchical allocation chain referenced in-chapter.

## Empirical claims

- IPv4's ~4.3 billion address ceiling (2^32) and IPv6's 128-bit space are direct consequences of RFC 791/8200's fixed address widths, not measured claims requiring further citation.

## Known simplifications (may need later technical review)

- The chapter treats "subnet" and "broadcast domain" as roughly coincident for pedagogical simplicity; real deployments can have subnets that don't map 1:1 to a single physical broadcast domain (e.g. proxy ARP, some overlay designs covered in Part VI).
- CIDR aggregation/summarization at ISP and registry levels is described narratively; exact allocation policy varies by registry and is out of scope.
