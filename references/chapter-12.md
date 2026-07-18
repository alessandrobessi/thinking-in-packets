# References — Chapter 12: From a Host to a Process

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 6335 — *Internet Assigned Numbers Authority (IANA) Procedures for the Management of the Service Name and Transport Protocol Port Number Registry*, IETF, 2011. Documents the port-number space and its conventions (0-1023 well-known, etc.).
- RFC 9293 §3.1 — TCP's own definition of a connection as identified by a socket pair.

## Historical sources

(none cited — this chapter is purely mechanism-level)

## Implementation documentation

- IANA Service Name and Transport Protocol Port Number Registry — the authoritative list of conventional port assignments (e.g. 443 for HTTPS).

## Empirical claims

(none)

## Known simplifications (may need later technical review)

- Ephemeral (client-side) source port allocation ranges are not discussed by number — kept at the conceptual "the OS picks one" level.
