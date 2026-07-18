# References — Chapter 26: Networks Made of Software

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- RFC 7348 (*VXLAN*, 2014) — a widely deployed overlay-encapsulation
  standard, representative of the tunnel/overlay mechanism this chapter
  describes conceptually without naming a single specific protocol as
  canonical.
- RFC 4364 (*BGP/MPLS IP VPNs*, 2006) — an earlier, still-relevant example
  of overlay networking predating cloud-era SDN, for historical grounding.
- Open Networking Foundation's SDN architecture documentation —
  foundational, vendor-neutral description of the control-plane/data-
  plane separation this chapter generalizes from Chapter 11.

## Historical sources

- OpenFlow (first published 2008, Stanford) is broadly credited as the
  protocol that popularized practical SDN; noted for historical context,
  not covered at protocol-detail level per blueprint scope.

## Implementation documentation

- Major cloud providers' VPC documentation (route tables, security
  groups, subnet behavior) illustrates this chapter's cloud-virtual-
  network concepts generically; specific provider implementation details
  are deliberately not covered, per blueprint's "vendor documentation
  establishes how that vendor implements a feature, not a universal
  networking law" rule (§19).

## Empirical claims

- None with specific numeric claims in this chapter.

## Known simplifications (may need later technical review)

- The worked example's hypervisor-level encapsulation is a simplified,
  generic description; real implementations vary (kernel-level virtual
  switching, SmartNIC offload, etc.) and are not enumerated here.
- Security-group/firewall policy enforcement mechanics are gestured at
  only at the "customer-configurable rules" level, not derived in detail
  — stateful-firewall mechanics were already covered in Chapter 16 and
  are assumed, not re-explained.
