#!/usr/bin/env python3
"""Generate concept-graph.md from concept-graph.yaml.

concept-graph.yaml is the source of truth. This script regenerates
concept-graph.md as an actual mirror of it (status, chapter, prerequisites,
misconception count, key-takeaway link) instead of a hand-maintained file
that can drift out of sync. Run this after any edit to concept-graph.yaml:

    python3 scripts/generate_concept_graph_md.py

Then commit both files together.
"""
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

LEVEL_DESCRIPTIONS = {
    0: "Network, Endpoint, Message, Protocol, Intermediary, Failure, Layered cooperation",
    1: "Bit, Signal, Encoding, Physical medium, Noise, Bandwidth, Propagation latency, Frame, Header/Payload, Checksum, Encapsulation",
    2: "Network interface, MAC address, Ethernet/Wi-Fi, Switch, Forwarding table, Broadcast domain, Failure domain, Internetwork",
    3: "IP packet, IPv4/IPv6 address, Prefix/subnet, DHCP, SLAAC, Default gateway, ARP, Neighbor Discovery, Address resolution",
    4: "Router, Routing table, Longest-prefix match, Data plane, Best-effort delivery, TTL/Hop Limit, ICMP, MTU, Fragmentation, Autonomous systems, BGP, Control plane",
    5: "Process/port, Socket, UDP, TCP, Handshake, Sequence numbers/acknowledgement, Retransmission, Flow control, Congestion control",
    6: "Private/public addressing, NAT, Firewalls, Proxies, VPN, DNS, TLS, HTTP",
    7: "Throughput, Latency components, Jitter, Caching, CDN, Load balancing, HTTP/2, QUIC, HTTP/3, Real-time media trade-offs",
    8: "Virtual interfaces, Tunnels/overlays, Software-defined networking, Cloud VPCs, Container namespaces, Service discovery, Service mesh",
    9: "Segmentation, Zero trust, Denial of service, Redundancy, Systematic troubleshooting",
}


def main():
    data = yaml.safe_load((ROOT / "concept-graph.yaml").read_text())
    concepts = data["concepts"]

    by_level = defaultdict(list)
    for c in concepts:
        by_level[c["level"]].append(c)

    lines = [
        "# Concept Dependency Tracker",
        "",
        "Checklist over the 10-level (0-9) Concept Dependency Graph in",
        "blueprint.md §10. A concept is checked off once the chapter that",
        "introduces it is written. No concept may be used in prose before its",
        "own checkbox (or an earlier level's) is checked.",
        "",
        "**This file is generated from [`concept-graph.yaml`](concept-graph.yaml) —",
        "do not hand-edit it.** Run `python3 scripts/generate_concept_graph_md.py`",
        "after any change to the YAML and commit both files together.",
        "",
    ]

    for level in sorted(by_level):
        lines.append(f"## Level {level} — {LEVEL_DESCRIPTIONS[level]}")
        lines.append("")
        lines.append("| Concept | Status | Chapter | Prerequisites | Misconceptions | Key Takeaway |")
        lines.append("|---|---|---|---|---|---|")
        for c in by_level[level]:
            status = "✅ written" if c["written"] else "☐ planned"
            chapter = f"Ch. {c['introduced_in']}"
            prereqs = ", ".join(c["prerequisites"]) if c["prerequisites"] else "—"
            n_misconceptions = len(c.get("misconception_ids", []))
            if c["written"] and c.get("key_takeaway"):
                takeaway_link = f"[link]({c['key_takeaway']})"
            else:
                takeaway_link = "—"
            lines.append(
                f"| {c['name']} | {status} | {chapter} | {prereqs} | {n_misconceptions} | {takeaway_link} |"
            )
        lines.append("")

    (ROOT / "concept-graph.md").write_text("\n".join(lines).rstrip() + "\n")
    print(f"Generated concept-graph.md from {len(concepts)} concepts across {len(by_level)} levels.")


if __name__ == "__main__":
    main()
