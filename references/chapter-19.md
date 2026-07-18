# References — Chapter 19: The Language of the Web

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 9110, *HTTP Semantics* — current consolidated specification of methods, status codes, headers (obsoletes RFC 7230-7231's semantics portions).
- RFC 9112, *HTTP/1.1* — the specific wire format referenced for this chapter's request/response shape.
- RFC 6265, *HTTP State Management Mechanism* — cookies.
- RFC 3986, *Uniform Resource Identifier (URI): Generic Syntax* — URL/URI structure (scheme, host, path).

## Historical sources

- HTTP/0.9 and HTTP/1.0 (Berners-Lee et al., early 1990s at CERN) predate today's RFC 9110-era semantics; this chapter deliberately teaches the current, stable semantics rather than the protocol's earliest, much more limited form.

## Implementation documentation

- MDN Web Docs' HTTP reference is a commonly cited, actively maintained implementation-facing summary of methods/status codes/headers; not cited here for any single specific claim, but representative of the kind of source used to check status-code descriptions for accuracy.

## Empirical claims

- "A single page load typically triggers many separate requests" is a structural/architectural claim about how HTML documents reference external resources, not a specific measured statistic — no specific average-requests-per-page figure is cited.

## Known simplifications (may need later technical review)

- HTTP/2 and HTTP/3's differences from the HTTP/1.1-shaped request/response model shown here are deliberately deferred to Part V (Chapters 23-24) — this chapter teaches HTTP's semantics, not its wire-level framing across versions.
- Caching headers, content negotiation, and CORS are not covered here — out of scope for the mechanism-level introduction this chapter provides.
