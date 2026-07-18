# References — Chapter 17: Naming a Moving World

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 1034, *Domain Names — Concepts and Facilities* — the foundational DNS architecture (hierarchy, delegation).
- RFC 1035, *Domain Names — Implementation and Specification* — record types (A, CNAME), message format, caching/TTL behavior.
- RFC 3596, *DNS Extensions to Support IP Version 6* — defines the AAAA record.
- RFC 8499, *DNS Terminology* — current, consolidated terminology reference (authoritative server, recursive resolver, etc.), used to keep this chapter's terms aligned with modern usage.
- RFC 1034 §4.3.1-4.3.2 (already cited above for foundational architecture) — also the source for this chapter's second-pass correction that a resolver caches NS delegation records (and their glue addresses) independently of the final answer records they lead to, each with its own TTL, so an expired answer doesn't necessarily mean an expired delegation.

## Historical sources

- DNS was introduced by Paul Mockapetris in 1983 (RFC 882/883, later superseded by RFC 1034/1035), replacing the earlier single, centrally-maintained HOSTS.TXT file — a useful historical contrast for *why* a delegated hierarchy replaced a flat, centrally-updated list as the Internet grew.

## Implementation documentation

- Public resolver documentation (e.g. major public DNS resolver operators' own explainers) describes typical resolver cache behavior; this chapter avoids citing any single provider's specific defaults as universal.

## Empirical claims

- None with specific dated figures; caching/propagation behavior is described structurally (via TTL mechanics), not with measured propagation-time statistics.

## Known simplifications (may need later technical review)

- DNSSEC (cryptographic authentication of DNS answers) is not covered — it's a distinct, optional layer on top of the core hierarchy/delegation/caching mechanism this chapter teaches.
- Negative caching, DNS-over-HTTPS/TLS, and split-horizon/internal DNS are out of scope at this mechanism-level treatment.
- The chapter's second-pass correction (cached delegation can outlive a cached answer) is stated qualitatively; it doesn't derive exactly which records get cached at which step or typical real-world NS/glue TTL values, which vary by zone operator.
