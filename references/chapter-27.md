# References — Chapter 27: Networking Moving Applications

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- Container Network Interface (CNI) specification (Cloud Native Computing
  Foundation, actively maintained) — the de facto standard interface
  this chapter's "container network interface" concept generalizes from.
- Kubernetes official documentation on Services, Ingress, and DNS-based
  service discovery — the most widely deployed real implementation of
  this chapter's service-address/service-discovery model.
- Linux kernel `namespaces(7)` man page — the underlying OS mechanism
  implementing network namespaces.

## Historical sources

- Docker's 2013 popularization of application containers, and Kubernetes'
  2014 release building orchestration on top of that model, are the
  historical starting point for the problem this chapter addresses; not
  narrated in the chapter body per blueprint's "mechanisms over trivia"
  rule.

## Implementation documentation

- Istio and Linkerd (two widely used open-source service mesh
  implementations) documentation illustrates sidecar-proxy architecture
  generically; the chapter deliberately doesn't endorse or describe one
  specific implementation's configuration.

## Empirical claims

- None with specific numeric claims in this chapter.

## Known simplifications (may need later technical review)

- "Service discovery" is described as DNS-like but more frequently
  updated than traditional DNS's caching model would tolerate — real
  implementations vary (some use DNS directly with very short TTLs, some
  use a separate API-based mechanism); the chapter stays at the
  conceptual level rather than picking one.
- Sidecar proxy traffic interception mechanics (iptables rules, eBPF,
  etc.) are not covered — out of scope per blueprint's "not a Linux
  networking command cookbook" exclusion (§5).
