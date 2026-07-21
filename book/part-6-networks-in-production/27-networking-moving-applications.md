# Networking Moving Applications

**Part:** Part VI — Networks in Production

**Concept Level:** Level 8, per concept-graph.md

**Prerequisites:** Virtual interfaces and overlays (Ch. 26), DNS (Ch. 17), proxies (Ch. 16), load balancers (Ch. 22)

**New concepts introduced:** network namespace, pod, Container Network Interface (CNI), pod (container) address, service address and discovery, headless service, ingress and ingress controller, egress, east-west traffic, sidecar proxy, service mesh

---

## Opening Question

*How does communication work when applications move among containers and machines?*

## Real-World Story

A large company used to assign each employee a fixed desk with a labeled phone extension, and anyone wanting to reach that employee would dial their extension directly. Then the company adopted flexible seating: employees might sit at a different desk every day, or work from a different building entirely, depending on the week's needs. Dialing a specific desk's extension became useless — the person who used to answer that extension might not even be in the building today, and a different employee entirely might be sitting there instead.

The company's actual fix wasn't to abandon phone numbers. It was to give each *employee* — not each desk — a single stable number that the phone system quietly forwards to wherever that employee is currently sitting, updated automatically as their location changes. Callers keep dialing the same stable number forever; the company's phone system handles the increasingly complicated job of keeping track of where that number should currently ring.

Containerized applications move constantly — restarted after a crash, rescheduled onto a different physical machine, scaled up with new copies or down with fewer, all automatically, often without a human deciding exactly when or where. A networking model built around fixed, manually assigned addresses (the old fixed-desk-and-extension approach) breaks down immediately under that much routine, automatic movement — so container platforms build the same kind of solution the company did: stable identities that get continuously, automatically kept up to date with wherever the actual, moving instances currently are.

## Worked Example

Follow one external request — a customer hitting a company's public API — as it travels from the open Internet through to one of several constantly-changing backend instances actually capable of handling it.

The request first reaches an **ingress** point: infrastructure specifically responsible for accepting traffic arriving from outside the cluster and routing it toward the correct internal destination, functioning much like Chapter 16's reverse proxy but purpose-built for a container platform's internal topology. The rules for how it should do that are declared as configuration: which external hostname and path map to which internal **service**, named directly by its identity — not by an address, since the entire point is that this declared configuration shouldn't need to know one. The actual running proxy process that reads that configuration and does the work — the **ingress controller** — is separate infrastructure, and turning "route to this service" into an actually-delivered packet is the controller's own implementation choice: this walkthrough follows the common pattern of forwarding to the service's own stable **service address**, a fixed, published address representing "the API" regardless of which instances currently back it.

Getting from "service" to "a specific live instance" is **service discovery**'s job: the platform's continuously updated record of which backend instances are currently healthy behind each service. Control-plane components (Chapter 9 and 11's control plane, doing the same kind of job here) watch that record and keep it reconciled as instances start, stop, or change health, then program the data plane's actual forwarding rules to match — so when a packet addressed to the service arrives, the data plane already knows which live instance to send it to, without consulting anything fresh for that specific packet. This reconciliation is continuous but not instantaneous: an instance crashing and a replacement starting are propagated to the data plane automatically, within moments rather than manually, so callers never have to learn the replacement's address themselves — but there's a real, if usually brief, window while the change works its way through the control plane and out to every forwarding rule that depends on it, during which some traffic can still be aimed at an instance that's already gone.

The request ultimately reaches one specific, currently-healthy instance's own **pod address** — the network-layer address of a *pod*, the platform's actual unit of network identity, understood to be unstable and disposable: it can, and routinely does, change the moment that particular instance is replaced. A pod can hold more than one container, and it's the pod, not each individual container inside it, that owns the **network namespace** and its address; containers sharing one pod share that same namespace and reach each other simply via `localhost`, while remaining isolated from every other pod's namespace, even on the same physical machine.

If handling this request requires the backend to call out to another internal service — a database, another microservice — that's ordinarily called **east-west traffic**: communication between services inside the cluster, as distinct from the north-south traffic (like this request) crossing the cluster's own edge. East-west and **ingress/egress** aren't rival labels for the same thing, though — they describe two different dimensions, and the second only means anything once you name a boundary. "Ingress" and "egress" are just "inbound" and "outbound" relative to whatever boundary you've picked. That backend-to-database call is east-west at the level of the whole cluster, and at the same time it's egress leaving the backend's own pod and ingress arriving at the database's — same packets, three accurate labels, because they're answering different questions about different boundaries.

## Core Intuition

Container platforms solve constant, automatic movement the same way the company solved its flexible-seating problem: give every service a single stable identity that callers can rely on permanently, and build continuously-updated infrastructure that transparently keeps that stable identity pointed at wherever the actual, individually unstable instances currently are — so nothing calling the service ever needs to track individual instances' comings and goings directly.

## Technical Explanation

A **network namespace** is an isolated view of network state — its own interfaces, its own routing table, its own view of what "localhost" means — implemented by the operating system kernel, letting many isolated groups share one physical machine's hardware while each believes it has its own private network stack, similar in spirit to how Chapter 26's virtual interfaces let many VMs share physical network hardware. In the platforms this chapter describes, a **pod** — a group of one or more tightly coupled containers, the platform's actual unit of scheduling and network identity — is what ordinarily owns one network namespace and one **pod (container) address**; every container inside that pod shares the same namespace and the same address, and reaches its pod-mates over `localhost` exactly as if they were separate processes on one machine, while remaining fully isolated from every other pod's namespace. **Container Network Interface (CNI)** names the standardized plugin specification the platform calls the moment a pod starts: a networking plugin conforming to CNI receives that call and does the actual work of creating an interface connecting the new pod's namespace to the broader network, assigning it an address, and wiring up its routing, then reverses all of it when the pod stops. CNI is the specification and the plugin doing that provisioning work — not a name for the resulting interface itself, which is simply the pod's own network interface once CNI has finished setting it up.

A pod address is deliberately treated as unstable and disposable throughout this chapter's model, since the whole point of automatic scheduling is that any given instance can be replaced at any time, and nothing durable should depend on one specific instance's address remaining valid.

A **service address**, by contrast, is a stable, durable virtual address representing a *logical service* rather than any one instance — this is the "employee's phone number" in the opening story, remaining constant even as the specific instances answering behind it come and go continuously. Other services inside the cluster typically reach it the same way Chapter 17's DNS resolution works — a service's name resolves to its address through the platform's own internal naming system — though an ingress controller sitting at the cluster boundary commonly skips that step and reads a service's assigned address directly from the platform's own control-plane state, since it already has to watch that state for other reasons. Either way, **service discovery** is the deeper mechanism making the address actually useful: the platform's continuously updated record of which instances are currently healthy behind each service, watched by control-plane components that keep the data plane's forwarding rules programmed to match. The data plane itself does the fast, per-packet work of forwarding to whichever instance those rules currently point at — it isn't looking anything up fresh per packet, it's just following rules the control plane already kept current. Most requests to a service address never enumerate individual instances at the application or ingress level at all, and typically stay pinned to one instance for the life of a connection or flow rather than being re-balanced request by request, the same connection-vs-request granularity Chapter 22 already distinguished for load balancers generally. A **headless service** is the deliberate exception — one that skips the stable virtual address entirely and lets DNS resolution return individual instance addresses directly, for the less common cases where a caller genuinely needs to reach specific instances rather than "the service" as a whole.

**Ingress** is a declared set of rules — which external host and path should route to which internal service — at a cluster's (or service's) boundary; an **ingress controller** (or gateway) is the separate, actually-running piece of infrastructure that reads those rules and does the accepting and routing work, typically incorporating reverse-proxy and load-balancing behavior (Chapters 16 and 22) purpose-built for the platform's internal service-discovery model. That declared configuration names a service as its backend; it doesn't dictate how the controller actually gets traffic there — some controllers forward to the service's own address and let the data plane handle the rest, others read service-discovery information directly and route straight to a specific instance, bypassing the service address entirely. Both satisfy the same Ingress configuration; which one happens is a property of the controller, not of "ingress" as a concept. **Ingress** and **egress** are directional labels — inbound and outbound — always relative to some named boundary, while **east-west traffic** is the separate, positional label for traffic between internal services. Those are different dimensions, not alternatives: one packet can be east-west across the whole cluster while being egress from its source pod and ingress to its destination pod at once. What matters when reasoning about either is naming the boundary out loud, since "egress" answers "leaving *what?*" — the cluster edge, or just one pod — and those are very different controls.

A **sidecar proxy** is a proxy process deployed alongside — not instead of — an application's own container, as an additional container sharing that same pod and therefore that same network namespace, mediating traffic for the pod as a whole rather than for any one container inside it individually, to add cross-cutting behavior (encryption, retries, observability, policy enforcement) without the application's own code needing to implement any of it directly. A **service mesh** is a coordinated system giving operators uniform control over how every service's traffic is secured, observed, and routed — built on top of, not replacing, the ordinary networking (namespaces, pod addresses, service discovery) already described in this chapter. The traditional way to build one deploys exactly the per-pod sidecar proxies just described, consistently across a whole platform; newer "sidecarless" or ambient designs achieve the same uniform control through shared node-level or infrastructure-level proxies instead of a dedicated proxy container per pod. Both are meshes in the sense that matters here — uniform, centrally-controlled traffic policy layered on top of the platform's existing networking — even though "a service mesh is just a lot of sidecars" is only true of the traditional design, not the category as a whole.

```mermaid
sequenceDiagram
    participant C as External client
    participant IC as Ingress controller
    participant CP as Control plane
    participant DP as Data plane
    participant PB as Pod (currently healthy)
    Note over IC: One common controller pattern —<br/>others route straight to pods instead
    C->>IC: Request for the API's hostname
    IC->>DP: Send to the address obtained for the declared Service backend
    Note over CP,DP: Control plane continuously watches instance health<br/>and keeps the data plane's forwarding rules programmed to match
    DP->>PB: Forward using already-current rules — no per-packet lookup
```

*Alt text: A sequence diagram showing one common ingress-controller pattern: the controller's configuration declares a Service backend by name and port, the controller obtains that Service's stable address from platform control-plane state, and sends traffic there. Separately, and continuously rather than per packet, a control plane watches which instances are healthy and keeps the data plane's forwarding rules current; the data plane then forwards each arriving packet using those already-programmed rules, with no fresh lookup on that packet's behalf. A labeled note flags this as one real controller pattern, not the only one — some ingress controllers instead read service-discovery information directly and route straight to a specific pod, bypassing the service address entirely.*

## Packet-Journey Checkpoint

If `example.net`'s article service runs on a container platform, the café laptop's HTTPS request from Chapter 20, after reaching the provider's infrastructure (Chapter 26's virtual networking), would pass through an ingress point and be resolved via service discovery to a currently healthy pod instance. Exactly where the request's external TLS actually terminates, and whether a mesh proxy is involved for the internal hop from there to the article service's own pod, are deployment choices — sometimes the ingress gateway itself terminates external TLS and the mesh separately secures only the internal leg; if the platform uses a traditional sidecar-based mesh, that internal leg's security and routing may be handled transparently by a sidecar proxy rather than the article service's own application code.

## Common Misconceptions

### *A container is simply a tiny virtual machine*

**Why it's wrong:** Containers and VMs are both used to run isolated workloads, so they can appear to be different sizes of the same thing.

**Correct intuition:** A container shares the host machine's kernel rather than virtualizing an entire separate operating system the way a VM does (Chapter 26) — isolation happens at a different level, with different networking mechanics (namespaces and CNI-provisioned interfaces) than a VM's virtual interfaces. It's also worth being precise about which unit actually owns that isolation: the *pod*, not each individual container, is what owns one network namespace and one address — containers sharing a pod share that namespace too, reaching each other over `localhost`.

**Analogy:** Stable reception number for moving workers (Chapter 27) — the mechanism this chapter builds is about identity and discovery for moving workloads, a different problem than how much a workload is isolated.

### *A Kubernetes Service is a permanently running proxy process*

**Why it's wrong:** "Service" sounds like it should name one continuously running piece of software actually handling traffic.

**Correct intuition:** A Service is continuously-programmed routing and discovery state — a stable virtual address, plus a continuously updated record of which instances are currently healthy behind it — not a single running process itself. A control plane watches that record and programs the data plane's forwarding rules to match; the data plane then forwards traffic using those rules, commonly staying with one selected instance for the life of a connection or flow rather than re-selecting for every individual request, the same connection-vs-request granularity distinction Chapter 22 already drew for load balancers generally. An application-layer proxy sitting in front of the Service can choose to select per request instead, but that's a property of that proxy, not something the Service abstraction itself guarantees.

**Analogy:** The phone system's forwarding record isn't itself a person answering calls — it's the continuously updated instruction for where to send them.

### *Pod IP addresses are stable application identities*

**Why it's wrong:** An IP address elsewhere in this book (Chapter 6) has generally been treated as at least session-durable, so it's natural to expect the same here.

**Correct intuition:** A pod address is deliberately treated as unstable and disposable — nothing should depend on a specific instance's address remaining valid, which is exactly why service addresses and discovery exist as a separate, stable layer.

**Analogy:** The specific desk an employee sits at today isn't their identity — their phone number is.

### *Service discovery eliminates routing*

**Why it's wrong:** Resolving a service address to a specific healthy instance can feel like the entire routing problem is solved right there.

**Correct intuition:** Service discovery answers "which instance," but ordinary routing and forwarding (Chapters 9, 26) still has to actually deliver packets to whichever instance was chosen — discovery and delivery remain separate steps.

**Analogy:** Knowing an employee's current desk number doesn't walk the mail there by itself — the building's own delivery route still has to do that part.

### *A service mesh replaces the network beneath it*

**Why it's wrong:** A service mesh's proxies touch so much of a service's traffic that it can feel like the mesh has become the entire network.

**Correct intuition:** A service mesh is built on top of the platform's existing namespaces, pod addressing, and service discovery — it adds uniform cross-cutting control, but the underlying networking this chapter describes is still what actually carries every packet.

**Analogy:** Transit maps over common streets (Chapter 26) — a service mesh is another map layered on the same underlying infrastructure, not a replacement for the streets themselves.

### *"Egress" and "east-west" are two names for the same distinction*

**Why it's wrong:** Both come up when people discuss internal traffic, so it's tempting to treat "east-west" and "not-egress" as synonyms — as if a call either leaves the cluster (egress) or stays inside (east-west), one or the other.

**Correct intuition:** They answer different questions. **East-west** is positional — traffic between internal services, versus north-south traffic crossing the cluster edge. **Ingress/egress** is directional — inbound versus outbound relative to whatever boundary you've named. A backend calling a database is east-west across the whole cluster *and*, at the same time, egress from the backend's pod and ingress to the database's pod. Which of those you mean depends entirely on the boundary you're pointing at, so the useful discipline is to always name it: a cluster-edge egress control and a per-pod egress control are both "egress," and they do completely different jobs.

**Analogy:** A colleague walking from one office to another is "leaving their own office" and "entering the other" and "still inside the building" all at once — none of those contradict each other, they're just measured against different doorways.

### *"Ingress" names one running piece of software*

**Why it's wrong:** The worked example talks about a request "reaching an ingress point," which sounds like it's naming one concrete running thing.

**Correct intuition:** Ingress, in the platforms this chapter describes, is ordinarily a declared set of routing rules — which external host and path map to which internal service — configuration, not a process. An **ingress controller** (or gateway) is the separate, actually-running proxy infrastructure that reads those declared rules and does the real work of accepting and routing traffic; the rules and the thing executing them are two different pieces, provided by two different layers.

**Analogy:** A building directory listing which company occupies which floor isn't the security desk that actually checks visitors in and sends them there — one is the posted rule, the other is the staff enforcing it.

## Practical Implications

When reading a container-platform architecture diagram, distinguish a stable service address from any specific pod's address — troubleshooting "the service is unreachable" is a different investigation from troubleshooting "this one instance is unhealthy," and from "the ingress controller itself is misconfigured or down," a third, separate possibility. When evaluating a service mesh, remember its proxies — whether per-pod sidecars or shared infrastructure — add real behavior (retries, encryption, policy) at a real network hop, not a purely abstract control-plane concept. And when writing traffic policy, state the boundary explicitly, because "egress policy" can mean two very different things: a control on what leaves the *cluster edge* is a different rule, at a different boundary, from a per-*workload* egress control that restricts which internal services a given pod is even allowed to call. Both are legitimately "egress"; conflating them — assuming the word alone tells you which boundary is meant — is how a policy ends up governing the wrong traffic.

## Key Takeaway

**Container platforms separate unstable workload locations from stable service identities by continuously programming routing, translation, discovery, and proxy behavior.**

## What to Remember

- A pod, not each individual container, owns one network namespace and one address; containers sharing a pod reach each other over `localhost`.
- CNI is the plugin specification the platform calls to provision a pod's network interface, address, and routing — not a name for the resulting interface itself.
- A pod address is deliberately unstable and disposable, tied to one specific, replaceable instance.
- A service address is a stable virtual address representing a logical service, obtained from the platform's own declared configuration (or, for other internal callers, via DNS). A control plane watches which instances are healthy and keeps the data plane's forwarding rules current; the data plane just follows those rules, commonly staying with one instance per connection or flow rather than re-selecting per request (Chapter 22's granularity distinction applies here too).
- Ingress is declared routing configuration; an ingress controller (or gateway) is the separate running infrastructure that reads it and does the work — and different controllers genuinely implement that work differently, some routing through a service's own address, others straight to specific healthy pods.
- East-west (positional: between internal services) and ingress/egress (directional: relative to a named boundary) are different dimensions, not alternatives — one internal call is east-west across the cluster while also being egress from its source pod and ingress to its destination; always name the boundary "egress" is measured against.
- A sidecar proxy adds cross-cutting behavior to one pod's traffic (not one individual container's) without changing its application code.
- A service mesh gives uniform, centrally-controlled traffic policy platform-wide, built on top of existing networking, not replacing it — traditionally via per-pod sidecars, though newer sidecarless/ambient designs use shared node-level proxies instead.

## The Next Obvious Question

*How can a network remain reachable, secure, and resilient under failure or attack?*

---

**Glossary terms added this chapter:** Network namespace, Pod, Container Network Interface (CNI), Pod (container) address, Service address, Service discovery, Headless service, Ingress, Ingress controller, Egress, East-west traffic, Sidecar proxy, Service mesh → append to `/glossary.md`

**Misconceptions logged this chapter:** k8s-service-stable-instance (enriched, see `/misconceptions.md`); two new in-chapter-only misconceptions added (east-west and egress as different dimensions rather than rival labels, Ingress-as-one-process) — not added to the master registry, following the established pattern for supplementary chapter-specific misconceptions

**Concept-graph entries checked off:** network-namespace, pod, container-network-interface, pod-address, service-address-and-discovery, headless-service, ingress-egress, east-west-traffic, sidecar-proxy, service-mesh → update `/concept-graph.yaml`, regenerate `/concept-graph.md`

**Diagrams used this chapter:** sequence (request resolving through ingress and service discovery to a live pod instance) → satisfies style-guide.md §4
