# References — Chapter 05: Why One Giant Network Does Not Work

Per-chapter citation trail (blueprint.md §19).

## Standards cited

- IEEE 802.1D (MAC Bridges) — defines broadcast/flooding behavior within
  one bridged network, underlying this chapter's "broadcast domain"
  concept as the direct continuation of Chapter 4's switch behavior.

## Historical sources

- Radia Perlman, *Interconnections: Bridges, Routers, Switches, and
  Internetworking Protocols*, 2nd ed. (Addison-Wesley, 2000) — discusses
  the scaling limits of large bridged (flat) networks that motivate
  routed internetworking, directly supporting this chapter's argument.

## Implementation documentation

## Empirical claims

- No specific measured figures are used; the "20-device office" vs.
  "worldwide LAN" comparison is an illustrative thought experiment, not
  an empirical measurement, and is presented as such in-chapter.

## Known simplifications (may need later technical review)

- This chapter argues from first principles (broadcast domain growth,
  forwarding-table growth, failure containment, administrative ownership)
  rather than citing a specific historical incident of flat-network
  collapse; a real, documented case study (e.g. a large enterprise VLAN
  broadcast storm) could strengthen this chapter in a later editorial
  pass.
