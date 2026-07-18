# References — Chapter 29: Seeing and Troubleshooting the Network

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 792 / RFC 4443 (ICMP / ICMPv6, already cited in Chapter 10's
  references) — the mechanism underlying `ping`'s reachability probe,
  and the reason ICMP filtering can produce misleading `ping` failures.
- OpenTelemetry specification (CNCF, actively maintained) — the leading
  vendor-neutral standard for logs, metrics, and traces as distinct
  observability signal types, matching this chapter's three-way
  distinction.

## Historical sources

- Differential diagnosis as a formal clinical reasoning method has a long
  medical-education history; this chapter borrows the general reasoning
  pattern (not any specific clinical protocol) as a pedagogical analogy,
  not a medical claim.

## Implementation documentation

- Standard networking diagnostic tools' own documentation (`ping`,
  `traceroute`/`tracert`, `dig`, `curl -v`, `openssl s_client`) each
  illustrate one narrowly-scoped hypothesis test from this chapter's
  worked example; command syntax itself is deliberately not covered in
  the chapter body per blueprint §5 ("not a Linux networking command
  cookbook").

## Empirical claims

- None with specific numeric claims in this chapter.

## Known simplifications (may need later technical review)

- Path asymmetry and ECMP (equal-cost multi-path) load balancing are
  gestured at only as reasons traceroute output can vary, not derived in
  routing-protocol detail (already covered conceptually in Chapters 9
  and 11).
- TLS decryption for packet capture (e.g. via a configured key log file)
  is not mentioned — out of scope as an operational/tooling detail per
  blueprint §5.
