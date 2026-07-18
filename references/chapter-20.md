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
  described in this chapter's Technical Explanation are accurate for the
  conventional TCP-and-TLS path this chapter follows; the exact
  scheduling/eagerness of real browser implementations is intentionally
  left unspecified, as implementation detail beyond this chapter's scope.
- Second-pass correction: the Technical Explanation and What to Remember
  now explicitly scope the "transport before TLS, TLS before HTTP"
  ordering to this chapter's conventional TCP-and-TLS path, with a
  forward pointer to Chapter 24 (QUIC combines transport and
  cryptographic handshakes rather than keeping them strictly sequential)
  — see RFC 9000/9001, already cited in Chapter 24's own references.
- Second-pass correction: step 4 (address resolution, ARP/Neighbor
  Discovery) and step 7 (DNS resolution) were previously conflated in
  the What to Remember summary as both "resolving the destination
  address" — corrected to state they resolve different things (a local
  link-layer next hop vs. a remote IP address) at different layers,
  consistent with Chapter 8's own treatment.
- Third-pass correction: "TLS must complete before HTTP can send
  anything meaningful" was stated as universal; corrected to scope it to
  a genuinely fresh connection (this chapter's own scenario), with a
  bare forward-pointer (no mechanism explained, per style-guide's
  concept-ordering rule) noting that TLS 1.3 resumption lets a returning
  client send early data before its handshake finishes even over plain
  TCP — RFC 8446 §2.3 (already cited Ch. 18/24), the source for this
  correction.
