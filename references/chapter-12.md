# References — Chapter 12: From a Host to a Process

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 6335 — *Internet Assigned Numbers Authority (IANA) Procedures for the Management of the Service Name and Transport Protocol Port Number Registry*, IETF, 2011. Documents the port-number space and its conventions (0-1023 well-known, etc.).
- RFC 9293 §3.1 — TCP's own definition of a connection as identified by a socket pair; also the source for this chapter's second-pass correction that a listening socket (§3.3.1, LISTEN state) is bound to a local address/port only, with no remote endpoint yet — the narrower "one endpoint of a five-tuple" framing only describes an established connection's socket.
- RFC 768 (already cited Ch. 13) — UDP's connectionless model, the source for this chapter's note that a UDP socket may remain unconnected, with no fixed remote endpoint at all.
- RFC 3234 and common firewall/NAT literature — "five-tuple" (source IP, source port, destination IP, destination port, protocol) is the standard industry term for what this chapter calls the tuple; used consistently in place of an invented "connection tuple."
- RFC 792 (already cited Ch. 10) — the source for this chapter's third-pass correction that ports are specifically a UDP/TCP concept, not a universal property of everything above IP: ICMP carries no port numbers at all.

## Historical sources

(none cited — this chapter is purely mechanism-level)

## Implementation documentation

- IANA Service Name and Transport Protocol Port Number Registry — the authoritative list of conventional port assignments (e.g. 443 for HTTPS).

## Empirical claims

(none)

## Known simplifications (may need later technical review)

- Ephemeral (client-side) source port allocation ranges are not discussed by number — kept at the conceptual "the OS picks one" level.
- Port-to-process binding is presented as effectively one-to-one for clarity; kernel-level mechanisms that complicate this (e.g. `SO_REUSEPORT`/`SO_REUSEADDR` letting multiple processes or threads share one listening port, a single process holding many sockets) are named only briefly, not explained mechanically — out of scope for a first mental model of demultiplexing.
- How a browser internally routes a delivered reply to the correct tab or request (event loop, request IDs, per-tab process isolation in multi-process browser architectures) is named only as "the application's own job," not explained mechanically — that's browser-internal behavior beyond this chapter's OS-level demultiplexing scope.
- Listening-socket demultiplexing is described as depending on port, protocol, and (optionally) local address; the kernel's actual longest-match binding-precedence rules (a socket bound to one specific address taking priority over one bound to all addresses on the same port) are not derived.
