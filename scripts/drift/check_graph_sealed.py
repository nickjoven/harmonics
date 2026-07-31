#!/usr/bin/env python3
"""
Tool #9: Derivation-graph sealed-projection audit (advisory).

Checks that the derivation graph is a faithful *projection of sealed
substrate content*: every node's source file should be sealed into the
.ket CAS (present in .ket/log), and its working-tree content should still
match that sealed CID.

Reports three classes:
  - drifted : node is sealed but its file content no longer matches the
              last-logged CID (edited without re-`ket put`).
  - missing : node is sealed but the file is gone from the tree.
  - unsealed: node's source was never sealed (not in .ket/log) — it lives
              in the graph but not in the substrate. A coverage signal.

This is the graph-level dual of check_working_tree.py: that gates the
curated spine; this ties drift and seal-coverage to graph membership, so
"is the graph a real projection of the substrate?" becomes measurable.

Exit: 0 = every sealed node matches (drift-free), 1 = drifted/missing
nodes, 2 = environment error (no hashing backend). Unsealed nodes are
reported as a NOTE and do not by themselves set a nonzero exit — the
corpus legitimately carries un-sealed working docs.

Advisory in run_all.py: the graph is only partially sealed today, so a
gating check would block routine work. The coverage percentage is the
signal to watch; promote to gating once the corpus is fully sealed.

Run:
  python3 scripts/drift/check_graph_sealed.py
  python3 scripts/drift/check_graph_sealed.py --root path/to/repo
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _hash import hash_file, HashingUnavailable

from _ketlog import read_log  # the one put-line grammar (review 2026-07-30)

SAMPLE_CAP = 25


def load_sealed(log_path: Path) -> dict:
    """Map repo-relative path -> last-sealed CID from .ket/log (last wins)."""
    if not log_path.exists():
        return {}
    return read_log(log_path).last_cid


def _sample(ids: list) -> None:
    for i in sorted(ids)[:SAMPLE_CAP]:
        print(f"  {i}")
    if len(ids) > SAMPLE_CAP:
        print(f"  ... and {len(ids) - SAMPLE_CAP} more")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="repo root")
    parser.add_argument("--home", default=".ket", help="path to .ket dir")
    parser.add_argument("--graph", default="docs/derivation-graph.json")
    args = parser.parse_args()
    root = Path(args.root).resolve()

    graph_path = root / args.graph
    if not graph_path.exists():
        print(f"(no graph at {graph_path}, nothing to check)")
        return 0
    nodes = json.loads(graph_path.read_text()).get("nodes", [])
    sealed = load_sealed(root / args.home / "log")

    drifted: list = []
    missing: list = []
    unsealed: list = []
    try:
        for n in nodes:
            path = n.get("path")
            if not path:
                continue
            if path not in sealed:
                unsealed.append(n["id"])
                continue
            abs_path = root / path
            if not abs_path.exists():
                missing.append(n["id"])
                continue
            if hash_file(abs_path) != sealed[path]:
                drifted.append(n["id"])
    except HashingUnavailable as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    total = len(nodes)
    sealed_n = total - len(unsealed)
    pct = (100 * sealed_n // total) if total else 0
    print(f"Graph sealed-projection: {sealed_n}/{total} nodes CID-pinned ({pct}%)")

    if unsealed:
        print(
            f"NOTE: {len(unsealed)} unsealed node(s) — present in the graph, "
            f"absent from the substrate:"
        )
        _sample(unsealed)

    rc = 0
    if drifted:
        rc = 1
        print(
            f"DRIFTED: {len(drifted)} sealed node(s) whose content moved "
            f"since the last put:"
        )
        _sample(drifted)
        print("Re-`ket put` these to re-seal, preserving lineage.")
    if missing:
        rc = 1
        print(f"MISSING: {len(missing)} sealed node(s) whose file is gone from the tree:")
        _sample(missing)

    if rc == 0 and not unsealed:
        print("OK: every graph node is sealed and drift-free")
    elif rc == 0:
        print("OK: every sealed node is drift-free (see unsealed NOTE above)")
    return rc


if __name__ == "__main__":
    sys.exit(main())
