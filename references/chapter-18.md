# References — Chapter 18: Establishing Trust on an Untrusted Network

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 8446, *The Transport Layer Security (TLS) Protocol Version 1.3* — current TLS handshake, key exchange, and record protocol.
- RFC 5280, *Internet X.509 Public Key Infrastructure Certificate and CRL Profile* — certificate structure and validation.
- RFC 6066, *TLS Extensions* — defines Server Name Indication (SNI), relevant to this chapter's metadata-visibility guardrail.
- CA/Browser Forum Baseline Requirements — the industry rules governing how certificate authorities are expected to validate domain ownership before issuing certificates (cited at the concept level only, not for procedural detail).

## Historical sources

- SSL (TLS's predecessor) was introduced by Netscape in 1994-1995; TLS 1.0 (RFC 2246) followed in 1999 as an IETF standardization of the protocol — useful context for why "SSL" persists colloquially even though the protocol in use today is TLS.

## Implementation documentation

- Browser certificate-validation UI (warning pages, padlock indicators) is described generically; this chapter avoids citing any single browser vendor's specific UI as the canonical behavior, since presentation varies and changes over time.

## Empirical claims

- None with specific dated adoption figures; "most Web traffic today is HTTPS" is asserted qualitatively, consistent with widely reported industry trends, without citing a specific point-in-time percentage.

## Known simplifications (may need later technical review)

- No cryptographic mathematics (e.g. Diffie-Hellman, RSA, elliptic curves) is covered — key exchange is presented at the conceptual "shared secret from an observed exchange" level only, per blueprint §5's exclusion of mathematical treatment from the main text.
- Certificate revocation (CRLs, OCSP) and certificate transparency are not covered — validation is presented as "trusted-CA signature check plus hostname match" only.
- SNI's specific role in visible-hostname metadata is described at the concept level (§6, Technical Explanation) without covering Encrypted Client Hello or other mitigations.
