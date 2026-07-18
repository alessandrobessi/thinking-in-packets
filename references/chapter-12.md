# References — Chapter 12: From a Host to a Process

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 6335 — *Internet Assigned Numbers Authority (IANA) Procedures for the Management of the Service Name and Transport Protocol Port Number Registry*, IETF, 2011. Documents the port-number space and its conventions (0-1023 well-known, etc.).
- RFC 9293 §3.1 — TCP's own definition of a connection as identified by a socket pair.
- RFC 3234 and common firewall/NAT literature — "five-tuple" (source IP, source port, destination IP, destination port, protocol) is the standard industry term for what this chapter calls the tuple; used consistently in place of an invented "connection tuple."

## Historical sources

(none cited — this chapter is purely mechanism-level)

## Implementation documentation

- IANA Service Name and Transport Protocol Port Number Registry — the authoritative list of conventional port assignments (e.g. 443 for HTTPS).

## Empirical claims

(none)

## Known simplifications (may need later technical review)

- Ephemeral (client-side) source port allocation ranges are not discussed by number — kept at the conceptual "the OS picks one" level.
- Port-to-process binding is presented as effectively one-to-one for clarity; kernel-level mechanisms that complicate this (e.g. `SO_REUSEPORT`/`SO_REUSEADDR` letting multiple processes or threads share one listening port, a single process holding many sockets) are named only briefly, not explained mechanically — out of scope for a first mental model of demultiplexing.
