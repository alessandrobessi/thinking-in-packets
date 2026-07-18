# References — Chapter 20: What Happens When You Visit a Website

Per-chapter citation trail (blueprint.md §19).

This is a synthesis/integration chapter introducing no new mechanisms — it
cites no new standards of its own. See the reference files for Chapters
1-19, each of which carries the primary sources for the specific
mechanism it introduced that this chapter traces end to end.

## Standards cited

- RFC 7766, *DNS Transport over TCP - Implementation Requirements*, IETF, 2016 — DNS's mandatory TCP support, cited for step 5's "UDP is the common case, not a rule" correction.
- RFC 7858 (DNS over TLS) / RFC 8484 (DNS over HTTPS) / RFC 9250 (DNS over QUIC) — the encrypted-DNS transports named briefly in step 5.

## Known simplifications (may need later technical review)

- The ten-step trace presents a plausible, common-case ordering; real
  browsers issue some steps (e.g. speculative DNS prefetching, parallel
  connection warm-up) earlier or more eagerly than a strictly linear
  reading of the ten steps would suggest. The dependency *constraints*
  described in this chapter's Technical Explanation are accurate; the
  exact scheduling/eagerness of real browser implementations is
  intentionally left unspecified, as implementation detail beyond this
  chapter's scope.
