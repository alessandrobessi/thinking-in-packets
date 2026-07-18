# References — Chapter 27: Networking Moving Applications

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- Container Network Interface (CNI) specification (Cloud Native Computing
  Foundation, actively maintained) — the actual plugin specification this
  chapter's corrected CNI definition describes; the source for
  distinguishing the specification/plugin from the interface it
  provisions.
- Kubernetes official documentation, *Pods* (kubernetes.io/docs/concepts/workloads/pods/)
  — source for pod-as-network-identity-owner: "each Pod is assigned a
  unique IP address for each address family... containers within the
  Pod share the network namespace, including the IP address."
- Kubernetes official documentation, *Virtual IPs and Service Proxies*
  (kubernetes.io/docs/reference/networking/virtual-ips/) — source for the
  Service-resolves-to-virtual-IP-plus-EndpointSlices-driven-data-plane
  correction in this chapter's worked example and technical explanation.
- Kubernetes official documentation, *Service* — *Headless Services*
  section — source for this chapter's headless-service addition.
- Kubernetes official documentation, *Ingress* and *Ingress Controllers*
  (kubernetes.io/docs/concepts/services-networking/ingress/,
  .../ingress-controllers/) — source for the Ingress-object-vs.-
  ingress-controller distinction.
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
- Istio's *Sidecars and Ambient* / dataplane-modes documentation
  (istio.io/latest/docs/overview/dataplane-modes/) — source for this
  chapter's second-pass correction that sidecarless/ambient mesh
  architectures exist alongside the traditional per-pod sidecar model,
  both achieving the same uniform-control category through different
  proxy placement.

## Empirical claims

- None with specific numeric claims in this chapter.

## Known simplifications (may need later technical review)

- "Service discovery" and "data plane" are described generically as
  platform-internal directory-plus-forwarding machinery; Kubernetes'
  specific implementation (kube-proxy modes — iptables, IPVS — or an
  eBPF-based alternative, reconciling against the EndpointSlice API) is
  not named or explained mechanically, per blueprint's "not a Linux
  networking command cookbook" exclusion (§5). The chapter's corrected
  model (DNS resolves to a stable virtual address; a separate data-plane
  layer forwards to healthy endpoints) is the accurate shape of the
  mechanism without committing to one implementation's internals.
- "Pod" is introduced as this chapter's unit of network identity without
  fully deriving why a pod (rather than a container) is that unit — the
  container-runtime and scheduling reasons behind that design choice are
  out of scope.
- Sidecar proxy traffic interception mechanics (iptables rules, eBPF,
  etc.) are not covered — out of scope per blueprint's "not a Linux
  networking command cookbook" exclusion (§5).
- East-west/north-south and Ingress-object/ingress-controller terminology
  is presented as this chapter's own generalization rather than tied to
  one specific platform's exact API naming (Kubernetes' `Ingress` object
  is the concrete example, but the object/controller split generalizes to
  other platforms using different names).
- Ambient/sidecarless mesh architectures are named and distinguished from
  the traditional sidecar model at the conceptual level only — their
  actual mechanics (shared node-level proxies, per-pod traffic redirection
  without a dedicated sidecar container) are not explained.
