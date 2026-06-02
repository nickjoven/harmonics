#!/usr/bin/env python3
"""
Tool #8: Derivation-graph acyclicity (advisory).

Loads docs/derivation-graph.json and runs an iterative Tarjan
strongly-connected-component (SCC) pass over the `depends_on` edges.
Any SCC with more than one node is a dependency cycle. A clean
derivation DAG has none.

This is an audit of a *derived artifact*: docs/derivation-graph.json is a
projection of the corpus, and a cycle in it is a defect in the projection
(or in the prose it was built from), not in the substrate. The check
re-derives the conclusion (run SCC, diff against "acyclic") rather than
trusting the graph.

Today the check is EXPECTED to report cycles and is therefore wired as
ADVISORY in run_all.py: the `depends_on` graph is built by
scripts/build_derivation_graph.py from *prose filename mentions*, so two
docs that cite each other's filenames form a reciprocal edge. That citation
mush collapses 207 of 263 nodes into one SCC. The count is a health signal,
not a gate.

To make this GATING: type the edges (see the typed-edge support in
build_derivation_graph.py — the framework's `grounds`/`derives`/`proposes`
kinds vs a bare `references`) and run this pass over only the logical
`grounds`+`derives` subgraph, which should be acyclic. The current
`depends_on` graph mixes citation edges and is cyclic by construction.
The deeper fix is to project from CID-pinned sealed content rather than
from prose at all (see ket's DESIGN.md); until then this stays advisory.

Exit codes: 0 = acyclic, 1 = cycle(s) found, 2 = environment error.

Run:
  python3 scripts/drift/check_dag_acyclic.py
  python3 scripts/drift/check_dag_acyclic.py --root path/to/repo
"""

import argparse
import json
import sys
from pathlib import Path

SAMPLE_CAP = 25


def _sccs(adj: dict) -> list:
    """Iterative Tarjan SCC. Returns list of components (lists of ids).

    Iterative (explicit stack) on purpose: the derivation graph is deep
    enough that a recursive DFS blows Python's recursion limit.
    """
    index = {}
    low = {}
    on_stack = {}
    stack = []
    counter = [0]
    out = []

    for root in adj:
        if root in index:
            continue
        work = [(root, 0)]
        while work:
            node, pi = work[-1]
            if pi == 0:
                index[node] = low[node] = counter[0]
                counter[0] += 1
                stack.append(node)
                on_stack[node] = True
            recurse = False
            neighbors = adj[node]
            for j in range(pi, len(neighbors)):
                w = neighbors[j]
                if w not in index:
                    work[-1] = (node, j + 1)
                    work.append((w, 0))
                    recurse = True
                    break
                if on_stack.get(w):
                    low[node] = min(low[node], index[w])
            if recurse:
                continue
            if low[node] == index[node]:
                comp = []
                while True:
                    w = stack.pop()
                    on_stack[w] = False
                    comp.append(w)
                    if w == node:
                        break
                out.append(comp)
            work.pop()
            if work:
                parent = work[-1][0]
                low[parent] = min(low[parent], low[node])
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="repo root")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    graph_path = Path(args.root) / "docs" / "derivation-graph.json"
    try:
        graph = json.loads(graph_path.read_text())
    except FileNotFoundError:
        print(f"error: {graph_path} not found", file=sys.stderr)
        return 2
    except (OSError, json.JSONDecodeError) as e:
        print(f"error: cannot read {graph_path}: {e}", file=sys.stderr)
        return 2

    nodes = graph.get("nodes", [])
    ids = {n["id"] for n in nodes}
    # Build adjacency over depends_on, dropping any dangling targets so a
    # malformed reference can't masquerade as (or hide) a cycle.
    adj = {
        n["id"]: [t for t in n.get("depends_on", []) if t in ids]
        for n in nodes
    }

    cyclic = [sorted(c) for c in _sccs(adj) if len(c) > 1]

    if not cyclic:
        if not args.quiet:
            print(f"OK: derivation graph is acyclic ({len(ids)} nodes)")
        return 0

    cyclic.sort(key=len, reverse=True)
    largest = len(cyclic[0])
    print(
        f"CYCLIC: {len(cyclic)} SCC(s) > 1 node; largest = {largest} nodes "
        f"({len(ids)} nodes total)"
    )
    for comp in cyclic:
        sample = comp[:SAMPLE_CAP]
        more = "" if len(comp) <= SAMPLE_CAP else f", +{len(comp) - SAMPLE_CAP} more"
        print(f"  SCC ({len(comp)} nodes): {', '.join(sample)}{more}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
