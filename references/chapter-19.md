# References — Chapter 19: The Language of the Web

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 9110, *HTTP Semantics* — current consolidated specification of methods, status codes, headers (obsoletes RFC 7230-7231's semantics portions). §1 (Scope) and §3 (Terminology, "HTTP is a stateless application-level protocol") are the source for this chapter's second-pass correction placing HTTP at the application layer, not a "transport-and-structure" layer of its own. §9.3.1 (GET) and §9.3.3 (POST) are the source for this chapter's method-semantics correction (safe/read-only vs. processing-with-side-effects, not merely body presence); §15.5.2 (401 Unauthorized) and §15.5.4 (403 Forbidden) are the source for this chapter's status-code correction — RFC 9110 itself notes 401's name is a historical misnomer for what is actually an authentication failure, and defines 403 generically as "the server understood the request but refuses to fulfill it," explicitly not limited to identity-based refusal.
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
- Third-pass correction: the 401/403 analogy previously described 403 as "a door that recognizes your specific keycard and still won't open" — still identity-framed despite the surrounding prose's correction. Replaced with an analogy naming identity as only one possible reason among several (a rule against the request itself, a resource-level restriction, a policy refusing anyone), consistent with RFC 9110 §15.5.4's generic, non-identity-specific definition already cited above.
