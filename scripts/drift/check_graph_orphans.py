#!/usr/bin/env python3
"""
Tool #6: Dependency-graph orphan + source-reference check.

Loads docs/derivation-graph.json and flags:
  (a) nodes with zero inbound AND outbound edges (unless in an
      explicit roots allowlist — currently just PROOF_A / PROOF_B);
  (b) files referenced in MANIFEST.yml:scorecard.*.source that are
      absent from the graph (missing node);
  (c) scorecard sources whose graph node's direct dependencies
      include any file in numerology_inventory.md Class 1/3 —
      that's a scorecard entry leaning on withdrawn content.

Exits 1 if any finding.

Run:
  python3 scripts/drift/check_graph_orphans.py
"""

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("error: pyyaml required. pip install --user pyyaml", file=sys.stderr)
    sys.exit(2)


# Top-level proof documents that are legitimate roots even though
# they have no inbound edges.
ROOT_ALLOWLIST = {
    "PROOF_A_gravity",
    "PROOF_B_quantum",
    "FRAMEWORK_TOPOLOGY",
    "README",
}


def _resolve_source_id(name: str) -> str:
    """Map a scorecard source to a derivation-graph node id."""
    if name.endswith(".md"):
        name = name[:-3]
    # D-numbers can't be resolved without INDEX.md — let the
    # missing-node check catch them.
    return name


def _class_1_3_files(path: Path) -> set[str]:
    if not path.exists():
        return set()
    text = path.read_text()
    current = None
    files: set[str] = set()
    for line in text.splitlines():
        m = re.match(r"^## Class (\d)", line)
        if m:
            current = int(m.group(1))
            continue
        if current in (1, 3):
            for fn in re.findall(r"`([a-z_0-9]+\.md)`", line):
                files.add(fn[:-3])  # strip .md to match graph ids
    return files


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="repo root")
    args = parser.parse_args()
    root = Path(args.root).resolve()

    graph_path = root / "docs" / "derivation-graph.json"
    manifest_path = root / "MANIFEST.yml"
    numerology_path = root / "sync_cost" / "derivations" / "numerology_inventory.md"

    graph = json.loads(graph_path.read_text())
    manifest = yaml.safe_load(manifest_path.read_text())
    bad_classes = _class_1_3_files(numerology_path)
    scorecard = manifest.get("scorecard", {})

    by_id = {n["id"]: n for n in graph["nodes"]}

    findings: list[str] = []
    d_number_refs: list[str] = []

    # (a) orphan nodes
    for n in graph["nodes"]:
        has_in = bool(n.get("depended_on_by"))
        has_out = bool(n.get("depends_on"))
        if not has_in and not has_out and n["id"] not in ROOT_ALLOWLIST:
            findings.append(f"orphan node: {n['id']} (no edges in either direction)")

    # (b) scorecard sources missing from graph
    for entry_key, entry in scorecard.items():
        for s in entry.get("source") or []:
            node_id = _resolve_source_id(s)
            if node_id.startswith("D") and node_id[1:].isdigit():
                d_number_refs.append(
                    f"scorecard.{entry_key}.source='{s}' (needs INDEX.md to resolve)"
                )
            elif node_id not in by_id:
                findings.append(
                    f"missing node: scorecard.{entry_key}.source='{s}' "
                    f"(resolved to '{node_id}') not in derivation graph"
                )

    # (c) scorecard sources depending on Class 1/3 files
    for entry_key, entry in scorecard.items():
        for s in entry.get("source") or []:
            node_id = _resolve_source_id(s)
            node = by_id.get(node_id)
            if not node:
                continue
            for dep in node.get("depends_on", []):
                if dep in bad_classes:
                    findings.append(
                        f"bad dependency: scorecard.{entry_key}.source='{s}' "
                        f"depends on Class 1/3 node '{dep}'"
                    )

    if d_number_refs:
        print(f"NOTE: {len(d_number_refs)} D-number reference(s) unresolvable without INDEX.md:")
        for ref in d_number_refs[:3]:
            print(f"  {ref}")
        if len(d_number_refs) > 3:
            print(f"  ... and {len(d_number_refs) - 3} more")
        print()

    if findings:
        print(f"Graph inconsistencies: {len(findings)}")
        for f in findings:
            print(f"  - {f}")
        return 1

    print(f"OK: {len(graph['nodes'])} nodes, {len(scorecard)} scorecard entries consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
