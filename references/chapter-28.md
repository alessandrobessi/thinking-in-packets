# References — Chapter 28: Security and Resilience Are Architectural

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- NIST SP 800-207 (*Zero Trust Architecture*, 2020) — the authoritative
  government-standards definition of zero trust this chapter's treatment
  is aligned with, explicitly distinguishing it from "trust nobody."
- NIST SP 800-53 — control families for least privilege and segmentation,
  referenced conceptually rather than as a compliance checklist.

## Historical sources

- The "castle-and-moat" security model is the standard historical name
  for the single-perimeter approach this chapter opens by critiquing;
  its inadequacy became widely discussed following high-profile lateral-
  movement breaches through the 2010s, which this chapter references
  only generically rather than naming specific incidents.

## Implementation documentation

- Cloud providers' documentation on availability zones and multi-zone
  deployment illustrates the failure-domain/failover concepts generically.

## Empirical claims

- None with specific numeric claims (e.g. attack volumes, cost figures)
  in this chapter — DoS/DDoS scale claims are highly time-sensitive and
  deliberately omitted rather than risk staleness, per blueprint §19's
  dating requirement for adoption/performance claims.

## Known simplifications (may need later technical review)

- DDoS mitigation techniques (scrubbing centers, rate limiting, SYN
  cookies) are gestured at only as "upstream filtering," not detailed —
  out of scope per blueprint §5 (not a security operations handbook).
- Zero trust is presented as a design philosophy/principle, not a
  specific product category, per blueprint §17's terminology rule
  explicitly warning against treating it as a product category.
