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

The request first reaches an **ingress** point: infrastructure specifically responsible for accepting traffic arriving from outside the cluster and routing it toward the correct internal destination, functioning much like Chapter 16's reverse proxy but purpose-built for a container platform's internal topology. The rules for how it should do that — which external hostname and path map to which internal service — are declared as configuration; the actual running proxy process that reads those rules and does the work is a separate piece of infrastructure. Ingress doesn't know or care about individual pod instances directly — it routes based on a stable **service address**: a fixed, published address representing "the API," regardless of which specific backend instances are currently running behind it.

Resolving that service address happens the same way Chapter 17's DNS resolution does — a name resolves to an address — except what it resolves to is itself a stable, virtual address representing the service as a whole, not any one instance. The genuinely new mechanism sits one level below that: **service discovery** is the container platform's continuously updated internal directory tracking exactly which backend instances are currently healthy and ready to receive traffic behind that virtual address, updated the instant conditions change, not a static list decided once at deployment time. If one instance crashed thirty seconds ago and a replacement started ten seconds ago, that directory already reflects it — and it's the platform's own data-plane machinery, not the ingress point itself, that continuously reads this directory and keeps traffic to the virtual address actually flowing to the right live instances.

The request ultimately reaches one specific, currently-healthy instance's own **pod address** — the network-layer address of a *pod*, the platform's actual unit of network identity, understood to be unstable and disposable: it can, and routinely does, change the moment that particular instance is replaced. A pod can hold more than one container, and it's the pod, not each individual container inside it, that owns the **network namespace** and its address; containers sharing one pod share that same namespace and reach each other simply via `localhost`, while remaining isolated from every other pod's namespace, even on the same physical machine.

If handling this request requires the backend to call out to another internal service — a database, another microservice — that's ordinarily called **east-west traffic**: communication between services inside the same cluster or boundary, as distinct from the north-south traffic (like this request) crossing in from outside. That internal call only becomes **egress** in the specific sense this chapter uses the term if it actually leaves the boundary being discussed — reaching out to a service in a different cluster, a different cloud, or the public Internet — often subject to its own separate policy and routing, mirroring ingress's inbound role for traffic actually crossing that outer boundary.

## Core Intuition

Container platforms solve constant, automatic movement the same way the company solved its flexible-seating problem: give every service a single stable identity that callers can rely on permanently, and build continuously-updated infrastructure that transparently keeps that stable identity pointed at wherever the actual, individually unstable instances currently are — so nothing calling the service ever needs to track individual instances' comings and goings directly.

## Technical Explanation

A **network namespace** is an isolated view of network state — its own interfaces, its own routing table, its own view of what "localhost" means — implemented by the operating system kernel, letting many isolated groups share one physical machine's hardware while each believes it has its own private network stack, similar in spirit to how Chapter 26's virtual interfaces let many VMs share physical network hardware. In the platforms this chapter describes, a **pod** — a group of one or more tightly coupled containers, the platform's actual unit of scheduling and network identity — is what ordinarily owns one network namespace and one **pod (container) address**; every container inside that pod shares the same namespace and the same address, and reaches its pod-mates over `localhost` exactly as if they were separate processes on one machine, while remaining fully isolated from every other pod's namespace. **Container Network Interface (CNI)** names the standardized plugin specification the platform calls the moment a pod starts: a networking plugin conforming to CNI receives that call and does the actual work of creating an interface connecting the new pod's namespace to the broader network, assigning it an address, and wiring up its routing, then reverses all of it when the pod stops. CNI is the specification and the plugin doing that provisioning work — not a name for the resulting interface itself, which is simply the pod's own network interface once CNI has finished setting it up.

A pod address is deliberately treated as unstable and disposable throughout this chapter's model, since the whole point of automatic scheduling is that any given instance can be replaced at any time, and nothing durable should depend on one specific instance's address remaining valid.

A **service address**, by contrast, is a stable, durable virtual address representing a *logical service* rather than any one instance — this is the "employee's phone number" in the opening story, remaining constant even as the specific instances answering behind it come and go continuously. Resolving a service's name to that virtual address is ordinary DNS-style resolution (Chapter 17); what makes it work for a constantly-changing set of backends is a separate layer underneath. **Service discovery** is the platform's continuously updated internal directory — conceptually a set of currently-healthy pod addresses, kept in sync with which instances actually are healthy right now — that the platform's own data-plane machinery (not the DNS answer itself, and not the ingress point) consults to actually deliver traffic sent to that virtual address to a live instance. Most requests to a service address never enumerate individual pods at the application or ingress level at all; the data plane just forwards to the service's virtual address, and the platform transparently spreads that traffic across whichever instances discovery currently lists as healthy — typically choosing a specific instance once per connection or flow, the same connection-vs-request granularity Chapter 22 already distinguished for load balancers generally, with everything sent over that same connection afterward continuing to the same instance rather than being re-balanced request by request. A **headless service** is the deliberate exception — one that skips the stable virtual address entirely and lets DNS resolution return individual pod addresses directly, for the less common cases where a caller genuinely needs to reach specific instances rather than "the service" as a whole.

**Ingress** is a declared set of rules — which external host and path should route to which internal service — at a cluster's (or service's) boundary; an **ingress controller** (or gateway) is the separate, actually-running piece of infrastructure that reads those rules and does the accepting and routing work, typically incorporating reverse-proxy and load-balancing behavior (Chapters 16 and 22) purpose-built for the platform's internal service-discovery model. **Egress**, in this chapter's sense, is the mirrored concept for outbound traffic actually leaving that same outer boundary — not every internal, service-to-service call, which is ordinarily **east-west traffic** rather than egress, reserving that term for traffic crossing the boundary under discussion.

A **sidecar proxy** is a proxy process deployed alongside — not instead of — an application's own container, as an additional container sharing that same pod and therefore that same network namespace, mediating traffic for the pod as a whole rather than for any one container inside it individually, to add cross-cutting behavior (encryption, retries, observability, policy enforcement) without the application's own code needing to implement any of it directly. A **service mesh** is a coordinated system giving operators uniform control over how every service's traffic is secured, observed, and routed — built on top of, not replacing, the ordinary networking (namespaces, pod addresses, service discovery) already described in this chapter. The traditional way to build one deploys exactly the per-pod sidecar proxies just described, consistently across a whole platform; newer "sidecarless" or ambient designs achieve the same uniform control through shared node-level or infrastructure-level proxies instead of a dedicated proxy container per pod. Both are meshes in the sense that matters here — uniform, centrally-controlled traffic policy layered on top of the platform's existing networking — even though "a service mesh is just a lot of sidecars" is only true of the traditional design, not the category as a whole.

```mermaid
sequenceDiagram
    participant C as External client
    participant IC as Ingress controller
    participant DNS as Service DNS
    participant DP as Data plane
    participant PA as Pod A
    participant PB as Pod B (just started)
    C->>IC: Request for the API's hostname
    IC->>DNS: Resolve service name
    DNS-->>IC: Stable virtual service address
    IC->>DP: Send to virtual service address
    Note over DP: Continuously kept in sync<br/>by service discovery
    DP->>PB: Forward to a currently healthy pod
    Note over PA,PB: Pod addresses change as instances restart/scale;<br/>the virtual service address never does
```

*Alt text: A sequence diagram showing an ingress controller resolving a service name via DNS to a stable virtual service address, then sending traffic to that address; the platform's data plane, kept continuously in sync by service discovery, forwards it to whichever specific pod is currently healthy — illustrating that DNS resolves to a stable virtual address, not directly to a live pod, and that a separate data-plane layer does the actual forwarding (commonly per connection or flow, as Chapter 22 already distinguished for load balancers generally — the same granularity choice applies here, not a guarantee of fresh-per-request selection).*

## Packet-Journey Checkpoint

If `example.net`'s article service runs on a container platform, the café laptop's HTTPS request from Chapter 20, after reaching the provider's infrastructure (Chapter 26's virtual networking), would pass through an ingress point, be resolved via service discovery to a currently healthy pod instance, and — if the platform uses a service mesh — have parts of its TLS termination and routing handled transparently by a sidecar proxy rather than the article service's own application code.

## Common Misconceptions

### *A container is simply a tiny virtual machine*

**Why it's wrong:** Containers and VMs are both used to run isolated workloads, so they can appear to be different sizes of the same thing.

**Correct intuition:** A container shares the host machine's kernel rather than virtualizing an entire separate operating system the way a VM does (Chapter 26) — isolation happens at a different level, with different networking mechanics (namespaces and CNI-provisioned interfaces) than a VM's virtual interfaces. It's also worth being precise about which unit actually owns that isolation: the *pod*, not each individual container, is what owns one network namespace and one address — containers sharing a pod share that namespace too, reaching each other over `localhost`.

**Analogy:** Stable reception number for moving workers (Chapter 27) — the mechanism this chapter builds is about identity and discovery for moving workloads, a different problem than how much a workload is isolated.

### *A Kubernetes Service is a permanently running proxy process*

**Why it's wrong:** "Service" sounds like it should name one continuously running piece of software actually handling traffic.

**Correct intuition:** A Service is continuously-programmed routing and discovery state — a stable virtual address, plus a continuously updated record of which instances are currently healthy behind it — not a single running process itself. Resolving the Service's name gets a caller the stable virtual address; a separate data-plane layer, kept in sync with that healthy-instance record, is what actually forwards traffic to a live instance — commonly selecting that instance once per connection or flow rather than fresh for every individual request, the same connection-vs-request granularity distinction Chapter 22 already drew for load balancers generally; an application-layer proxy sitting in front of the Service can choose to select per request instead, but that's a property of that proxy, not something the Service abstraction itself guarantees.

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

**Why it's wrong:** A service mesh's sidecar proxies touch so much of a service's traffic that it can feel like the mesh has become the entire network.

**Correct intuition:** A service mesh is built on top of the platform's existing namespaces, pod addressing, and service discovery — it adds uniform cross-cutting control, but the underlying networking this chapter describes is still what actually carries every packet.

**Analogy:** Transit maps over common streets (Chapter 26) — a service mesh is another map layered on the same underlying infrastructure, not a replacement for the streets themselves.

### *Any call from one internal service to another counts as egress*

**Why it's wrong:** "Egress" and "leaving" both sound like they should describe any traffic headed toward some other destination, internal or not.

**Correct intuition:** Ordinary service-to-service traffic within the same cluster or boundary — the backend calling a database, one microservice calling another — is usually called **east-west traffic**, distinct from the north-south traffic (a request arriving from, or a response returning to, outside that boundary). Egress specifically names traffic actually crossing the outer boundary under discussion outbound — reaching a different cluster, a different cloud, or the public Internet — not every internal hop a request happens to take.

**Analogy:** Colleagues walking between offices on the same floor aren't "leaving the building" just because they're moving — egress is what happens at the building's own front door, not at every internal doorway.

### *"Ingress" names one running piece of software*

**Why it's wrong:** The worked example talks about a request "reaching an ingress point," which sounds like it's naming one concrete running thing.

**Correct intuition:** Ingress, in the platforms this chapter describes, is ordinarily a declared set of routing rules — which external host and path map to which internal service — configuration, not a process. An **ingress controller** (or gateway) is the separate, actually-running proxy infrastructure that reads those declared rules and does the real work of accepting and routing traffic; the rules and the thing executing them are two different pieces, provided by two different layers.

**Analogy:** A building directory listing which company occupies which floor isn't the security desk that actually checks visitors in and sends them there — one is the posted rule, the other is the staff enforcing it.

## Practical Implications

When reading a container-platform architecture diagram, distinguish a stable service address from any specific pod's address — troubleshooting "the service is unreachable" is a different investigation from troubleshooting "this one instance is unhealthy," and from "the ingress controller itself is misconfigured or down," a third, separate possibility. When evaluating a service mesh, remember its sidecar proxies add real behavior (retries, encryption, policy) at a real network hop, not a purely abstract control-plane concept. And when reasoning about internal traffic patterns or writing egress policy, keep east-west (service-to-service, inside the boundary) and true egress (actually crossing it) separate — a policy meant to restrict what leaves the cluster is the wrong tool for controlling which internal services can call which other internal services.

## Key Takeaway

**Container platforms separate unstable workload locations from stable service identities by continuously programming routing, translation, discovery, and proxy behavior.**

## What to Remember

- A pod, not each individual container, owns one network namespace and one address; containers sharing a pod reach each other over `localhost`.
- CNI is the plugin specification the platform calls to provision a pod's network interface, address, and routing — not a name for the resulting interface itself.
- A pod address is deliberately unstable and disposable, tied to one specific, replaceable instance.
- A service address is a stable virtual address representing a logical service; resolving its name is ordinary DNS, but a separate data-plane layer, kept in sync by service discovery, does the actual forwarding to a healthy instance — commonly per connection or flow, not necessarily fresh per individual request (Chapter 22's granularity distinction applies here too).
- Ingress is declared routing configuration; an ingress controller (or gateway) is the separate running infrastructure that reads it and does the work.
- Service-to-service traffic inside a boundary is east-west traffic; egress specifically means traffic actually crossing that boundary outbound.
- A sidecar proxy adds cross-cutting behavior to one pod's traffic (not one individual container's) without changing its application code.
- A service mesh gives uniform, centrally-controlled traffic policy platform-wide, built on top of existing networking, not replacing it — traditionally via per-pod sidecars, though newer sidecarless/ambient designs use shared node-level proxies instead.

## The Next Obvious Question

*How can a network remain reachable, secure, and resilient under failure or attack?*

---

**Glossary terms added this chapter:** Network namespace, Pod, Container Network Interface (CNI), Pod (container) address, Service address, Service discovery, Headless service, Ingress, Ingress controller, Egress, East-west traffic, Sidecar proxy, Service mesh → append to `/glossary.md`

**Misconceptions logged this chapter:** k8s-service-stable-instance (enriched, see `/misconceptions.md`); two new in-chapter-only misconceptions added (east-west vs. egress conflation, Ingress-as-one-process) — not added to the master registry, following the established pattern for supplementary chapter-specific misconceptions

**Concept-graph entries checked off:** network-namespace, pod, container-network-interface, pod-address, service-address-and-discovery, headless-service, ingress-egress, east-west-traffic, sidecar-proxy, service-mesh → update `/concept-graph.yaml`, regenerate `/concept-graph.md`

**Diagrams used this chapter:** sequence (request resolving through ingress and service discovery to a live pod instance) → satisfies style-guide.md §4
