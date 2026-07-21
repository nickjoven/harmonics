#!/usr/bin/env python3
"""Retrodiction harness: the shadow gate for canon.d#11 (milestone 1).

canon.d#11 commits to a v2 substrate where surface edge kinds compile to two
primitives (DEPENDS, SUCCEEDS), the spine is the anchor set for a
grounded-closure evaluator, and a divergence projection diffs computed status
against committed status to emit a human-ruling queue. The acceptance test for
that design is retrodiction: replay the 2026-04 bare-K=1 demotion
(harmonics#263) as a weakening event and check that this machinery
rediscovers, unprompted, what the manual audit found three months later.

This script is that harness, running entirely in the evaluator zone: it READS
the committed projections (docs/derivation-graph.json, docs/corpus-index.json,
docs/spine-data.json) and never writes to the ledger or CAS (no `ket put`).

Pipeline:
  1. Compile every graph edge to primitives via kind_table.json
     (unknown kinds upcast conservatively to DEPENDS/+/proposed).
  2. Derive the anchor set from spine-data.json entries (heuristic: graph
     node ids appearing in entry source/subject/premises text), unioned
     with an optional --anchors-file override.
  3. Grounded closure: a node is GROUNDED iff it is an anchor or reaches an
     anchor via committed DEPENDS(+) edges (edges point from a doc to its
     dependency, so support flows dependency -> dependent); PROVISIONAL iff
     it reaches an anchor only when proposed-modality edges are also
     allowed; UNGROUNDED otherwise. Weakest-link semantics: one weakened
     node on the only path severs support.
  4. Weakening injection (--fixtures): demoted nodes are removed from the
     anchor set, marked weakened, and stop transmitting support; the
     closure is recomputed and the delta set (nodes whose state dropped)
     is extracted.
  5. Divergence: a delta node is DIVERGENT when its committed surface in
     corpus-index.json still asserts strength (a standalone, case-sensitive
     "Derived" in status_line, or class 5 in classes) while its computed
     state dropped. Divergent nodes are emitted as a topologically ordered
     queue (dependencies before dependents) for human ruling.

Honest limits (this scaffold exists to be falsified by the fixtures):
  * Doc-granular. v2 wants proposition-granular support; a doc here is a
    bag of claims and one stale sentence taints the whole node.
  * Weakest-link only. No product or argumentation semantics; a single
    surviving committed path keeps a node GROUNDED regardless of how much
    else collapsed.
  * Prose-status matching is a heuristic. "Derived"/class-5 detection over
    status_line text is a regex over prose, not a parsed speech act; both
    false positives and false negatives are expected.
  * Anchor derivation is a heuristic. Spine entries name concepts, not doc
    ids; substring matching recovers only a few anchors, which is why
    --anchors-file exists.

Usage:
  python3 scripts/experiments/retrodict.py --self-test
  python3 scripts/experiments/retrodict.py --report
  python3 scripts/experiments/retrodict.py --fixtures FILE --report [--json]

Exit codes: 0 on success (and self-test pass), 1 on self-test failure or
missing inputs.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import deque
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_KIND_TABLE = Path(__file__).resolve().parent / "kind_table.json"

GROUNDED = "GROUNDED"
PROVISIONAL = "PROVISIONAL"
UNGROUNDED = "UNGROUNDED"
WEAKENED = "WEAKENED"

STATE_RANK = {GROUNDED: 2, PROVISIONAL: 1, UNGROUNDED: 0}

# Minimum node-id length for the substring anchor heuristic; shorter ids
# (INDEX, ...) collide with ordinary prose.
MIN_ANCHOR_STEM = 6

DERIVED_RE = re.compile(r"\bDerived\b")  # case-sensitive, standalone


def load_json(path: Path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


# ---------------------------------------------------------------- compilation

def compile_edges(graph: dict, kind_table: dict):
    """Compile surface edges to primitive edges.

    Returns (edges, stats) where each edge is a dict with src, dst, kind,
    parent, polarity, modality. Unknown kinds upcast to DEPENDS/+/proposed
    (conservative: they can only ever make a node PROVISIONAL).
    """
    node_ids = {n["id"] for n in graph["nodes"]}
    edges = []
    stats = {"by_kind": {}, "unknown_kinds": {}, "dangling": 0}
    for node in graph["nodes"]:
        src = node["id"]
        for edge in node.get("edges", []):
            kind = edge.get("kind", "")
            dst = edge.get("target")
            if dst not in node_ids:
                stats["dangling"] += 1
                continue
            spec = kind_table.get(kind)
            if spec is None:
                stats["unknown_kinds"][kind] = stats["unknown_kinds"].get(kind, 0) + 1
                spec = {"parent": "DEPENDS", "polarity": "+", "modality": "proposed"}
            edges.append({
                "src": src,
                "dst": dst,
                "kind": kind,
                "parent": spec.get("parent", "DEPENDS"),
                "polarity": spec.get("polarity", "+"),
                "modality": spec.get("modality", "committed"),
            })
            stats["by_kind"][kind] = stats["by_kind"].get(kind, 0) + 1
    return edges, stats


# -------------------------------------------------------------------- anchors

def derive_anchors(spine: dict, node_ids: set):
    """Heuristic anchor extraction: node ids named in spine entry text.

    Spine entries describe concepts, not doc ids; we normalize the entry's
    source/subject/premises text (lowercase, hyphen->underscore) and accept
    any graph node id (len >= MIN_ANCHOR_STEM) appearing as a substring.
    Returns {anchor_id: [spine_entry_keys...]}.
    """
    anchors = {}
    lowered = {nid: nid.lower() for nid in node_ids if len(nid) >= MIN_ANCHOR_STEM}
    for key, entry in spine.get("entries", {}).items():
        parts = [entry.get("source") or "", entry.get("subject") or ""]
        parts.extend(entry.get("premises", []) or [])
        blob = " ".join(parts).lower().replace("-", "_")
        for nid, low in lowered.items():
            if low in blob:
                anchors.setdefault(nid, []).append(key)
    return anchors


def load_anchor_override(path: Path, node_ids: set):
    """Anchors file: JSON array of node ids, or {"anchors": [...]}."""
    data = load_json(path)
    if isinstance(data, dict):
        data = data.get("anchors", [])
    known, unknown = [], []
    for nid in data:
        (known if nid in node_ids else unknown).append(nid)
    return known, unknown


# -------------------------------------------------------------------- closure

def grounded_closure(node_ids: set, edges: list, anchors: set, weakened=frozenset()):
    """Compute {node: state} under weakest-link grounded-closure semantics.

    Only DEPENDS edges with polarity '+' transmit support. Edges point from
    a doc to its dependency, so support propagates in reverse: from an
    anchor to everything that (transitively) depends on a supported node
    through committed edges. Weakened nodes neither anchor nor transmit.
    """
    committed_radj = {}
    any_radj = {}
    for e in edges:
        if e["parent"] != "DEPENDS" or e["polarity"] != "+":
            continue
        any_radj.setdefault(e["dst"], []).append(e["src"])
        if e["modality"] == "committed":
            committed_radj.setdefault(e["dst"], []).append(e["src"])

    def reach(radj):
        seen = set(a for a in anchors if a in node_ids and a not in weakened)
        queue = deque(seen)
        while queue:
            u = queue.popleft()
            for s in radj.get(u, ()):
                if s not in seen and s not in weakened:
                    seen.add(s)
                    queue.append(s)
        return seen

    grounded = reach(committed_radj)
    reachable = reach(any_radj)

    states = {}
    for nid in node_ids:
        if nid in weakened:
            states[nid] = WEAKENED
        elif nid in grounded:
            states[nid] = GROUNDED
        elif nid in reachable:
            states[nid] = PROVISIONAL
        else:
            states[nid] = UNGROUNDED
    return states


def state_counts(states: dict):
    counts = {GROUNDED: 0, PROVISIONAL: 0, UNGROUNDED: 0, WEAKENED: 0}
    for state in states.values():
        counts[state] += 1
    return counts


# ------------------------------------------------------------------ weakening

def apply_fixtures(fixtures: dict):
    """Extract {node: event_label} from fixtures events[].demoted[].node."""
    demoted = {}
    for i, event in enumerate(fixtures.get("events", [])):
        label = event.get("id") or event.get("name") or f"event-{i}"
        for item in event.get("demoted", []):
            node = item.get("node")
            if node:
                demoted.setdefault(node, label)
    return demoted


def delta_set(before: dict, after: dict, demoted: dict):
    """Nodes (excluding the demoted themselves) whose state dropped."""
    dropped = []
    for nid, old in before.items():
        if nid in demoted:
            continue
        new = after[nid]
        if STATE_RANK.get(new, 0) < STATE_RANK.get(old, 0):
            dropped.append(nid)
    return dropped


# ----------------------------------------------------------------- divergence

def committed_evidence(doc_entry: dict):
    """Return a string describing asserted strength, or None if none."""
    if not doc_entry:
        return None
    reasons = []
    status_line = doc_entry.get("status_line")
    if status_line and DERIVED_RE.search(status_line):
        reasons.append(f"status_line: {status_line.strip()!r}")
    classes = doc_entry.get("classes") or []
    if 5 in classes:
        reasons.append(f"classes: {classes}")
    return "; ".join(reasons) or None


def toposort(nodes: list, edges: list):
    """Order nodes dependencies-first using DEPENDS edges among them.

    Edge src->dst means src depends on dst, so dst precedes src. Cycles
    (references are not acyclic) fall back to sorted order for the rest.
    """
    node_set = set(nodes)
    indeg = {n: 0 for n in nodes}
    fwd = {n: [] for n in nodes}  # dependency -> dependents
    for e in edges:
        if e["parent"] == "DEPENDS" and e["src"] in node_set and e["dst"] in node_set:
            fwd[e["dst"]].append(e["src"])
            indeg[e["src"]] += 1
    queue = deque(sorted(n for n in nodes if indeg[n] == 0))
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in sorted(fwd[u]):
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)
    leftovers = sorted(node_set - set(order))  # cycle fallback
    return order + leftovers


def divergence_queue(dropped: list, after: dict, corpus_docs: dict,
                     edges: list, implied_by: dict):
    """Topologically ordered queue of divergent (stale-surface) nodes."""
    divergent = {}
    for nid in dropped:
        evidence = committed_evidence(corpus_docs.get(nid))
        if evidence:
            divergent[nid] = evidence
    queue = []
    for nid in toposort(list(divergent), edges):
        queue.append({
            "doc": nid,
            "committed_evidence": divergent[nid],
            "computed_state": after[nid],
            "implied_by_event": implied_by.get(nid),
        })
    return queue


def implied_events(dropped: list, edges: list, demoted: dict):
    """Attribute each dropped node to a demotion event by reverse reach."""
    radj = {}
    for e in edges:
        if e["parent"] == "DEPENDS" and e["polarity"] == "+":
            radj.setdefault(e["dst"], []).append(e["src"])
    implied = {}
    for node, label in demoted.items():
        seen = {node}
        queue = deque([node])
        while queue:
            u = queue.popleft()
            for s in radj.get(u, ()):
                if s not in seen:
                    seen.add(s)
                    queue.append(s)
        for nid in seen:
            implied.setdefault(nid, label)
    return {nid: implied.get(nid) for nid in dropped}


# -------------------------------------------------------------------- scoring

def score_findings(expected: list, queue: list):
    """Score fixtures' expected_findings against the emitted queue."""
    flagged = {item["doc"] for item in queue}
    expected_docs = {
        item["doc"] for item in expected
        if item.get("stale", True)
    }
    return {
        "found": sorted(expected_docs & flagged),
        "missed": sorted(expected_docs - flagged),
        "extra": sorted(flagged - expected_docs),
    }


# ------------------------------------------------------------------- pipeline

def run_pipeline(graph, corpus, spine, kind_table, anchors_file=None,
                 fixtures=None):
    node_ids = {n["id"] for n in graph["nodes"]}
    edges, edge_stats = compile_edges(graph, kind_table)

    derived = derive_anchors(spine, node_ids)
    anchors = set(derived)
    override_known, override_unknown = [], []
    if anchors_file:
        override_known, override_unknown = load_anchor_override(anchors_file, node_ids)
        anchors |= set(override_known)

    before = grounded_closure(node_ids, edges, anchors)
    result = {
        "nodes": len(node_ids),
        "edge_stats": edge_stats,
        "anchors": {
            "count": len(anchors),
            "derived": {k: v for k, v in sorted(derived.items())},
            "override": sorted(override_known),
            "override_unknown": sorted(override_unknown),
        },
        "closure": state_counts(before),
    }

    if fixtures is not None:
        demoted = apply_fixtures(fixtures)
        unknown_demoted = sorted(set(demoted) - node_ids)
        weakened = frozenset(set(demoted) & node_ids)
        after = grounded_closure(node_ids, edges, anchors - weakened, weakened)
        dropped = delta_set(before, after, demoted)
        implied = implied_events(dropped, edges, demoted)
        queue = divergence_queue(dropped, after, corpus.get("docs", {}),
                                 edges, implied)
        result["weakening"] = {
            "demoted": {k: demoted[k] for k in sorted(demoted)},
            "unknown_demoted": unknown_demoted,
            "closure_after": state_counts(after),
            "delta": sorted(dropped),
            "queue": queue,
        }
        expected = fixtures.get("expected_findings")
        if expected:
            result["score"] = score_findings(expected, queue)
    return result


# ------------------------------------------------------------------ reporting

def print_report(result):
    print("retrodiction harness (canon.d#11 shadow gate)")
    print(f"  nodes: {result['nodes']}")
    stats = result["edge_stats"]
    kinds = ", ".join(f"{k}={v}" for k, v in sorted(stats["by_kind"].items()))
    print(f"  edges compiled: {kinds}")
    if stats["unknown_kinds"]:
        print(f"  unknown kinds (upcast to DEPENDS/+/proposed): {stats['unknown_kinds']}")
    if stats["dangling"]:
        print(f"  dangling edges skipped: {stats['dangling']}")
    a = result["anchors"]
    print(f"  anchors: {a['count']} "
          f"(derived from spine: {sorted(a['derived'])}; override: {a['override']})")
    if a["override_unknown"]:
        print(f"  WARNING anchors not in graph: {a['override_unknown']}")
    c = result["closure"]
    print(f"  closure: grounded={c[GROUNDED]} provisional={c[PROVISIONAL]} "
          f"ungrounded={c[UNGROUNDED]}")
    weak = result.get("weakening")
    if weak:
        print(f"  demoted: {sorted(weak['demoted'])}")
        if weak["unknown_demoted"]:
            print(f"  WARNING demoted nodes not in graph: {weak['unknown_demoted']}")
        c2 = weak["closure_after"]
        print(f"  closure after weakening: grounded={c2[GROUNDED]} "
              f"provisional={c2[PROVISIONAL]} ungrounded={c2[UNGROUNDED]} "
              f"weakened={c2[WEAKENED]}")
        print(f"  delta (state dropped): {len(weak['delta'])} nodes")
        print(f"  divergence queue ({len(weak['queue'])} docs, dependencies first):")
        for item in weak["queue"]:
            print(f"    - {item['doc']}: computed={item['computed_state']}, "
                  f"event={item['implied_by_event']}")
            print(f"      committed: {item['committed_evidence']}")
    score = result.get("score")
    if score:
        print(f"  score vs expected_findings: found={len(score['found'])} "
              f"missed={len(score['missed'])} extra={len(score['extra'])}")
        for label in ("found", "missed", "extra"):
            if score[label]:
                print(f"    {label}: {score[label]}")


# ------------------------------------------------------------------ self-test

def self_test():
    """Synthetic 5-node chain: A (anchor) <- B <- C <- D, E isolated.

    Demote B; C and D must be flagged (their committed surfaces assert
    strength), E must be untouched.
    """
    graph = {"nodes": [
        {"id": "A", "edges": []},
        {"id": "B", "edges": [{"kind": "derives", "target": "A"}]},
        {"id": "C", "edges": [{"kind": "derives", "target": "B"}]},
        {"id": "D", "edges": [{"kind": "derives", "target": "C"}]},
        {"id": "E", "edges": []},
    ]}
    corpus = {"docs": {
        "C": {"status_line": "Derived. Synthetic status.", "classes": [5]},
        "D": {"status_line": None, "classes": [5]},
        "E": {"status_line": "Derived. Should never surface.", "classes": [5]},
    }}
    spine = {"entries": {}}  # anchors injected via override below
    kind_table = load_json(DEFAULT_KIND_TABLE)
    fixtures = {
        "events": [{"id": "synthetic-demotion", "demoted": [{"node": "B"}]}],
        "expected_findings": [
            {"doc": "C", "stale": True, "implied_by": "synthetic-demotion"},
            {"doc": "D", "stale": True, "implied_by": "synthetic-demotion"},
        ],
    }

    node_ids = {n["id"] for n in graph["nodes"]}
    edges, _ = compile_edges(graph, kind_table)
    anchors = {"A"}

    failures = []

    def check(cond, msg):
        if not cond:
            failures.append(msg)

    before = grounded_closure(node_ids, edges, anchors)
    check(before == {"A": GROUNDED, "B": GROUNDED, "C": GROUNDED,
                     "D": GROUNDED, "E": UNGROUNDED},
          f"baseline closure wrong: {before}")

    demoted = apply_fixtures(fixtures)
    weakened = frozenset(demoted)
    after = grounded_closure(node_ids, edges, anchors - weakened, weakened)
    check(after["B"] == WEAKENED, f"B not weakened: {after['B']}")
    check(after["E"] == UNGROUNDED, f"E state changed: {after['E']}")

    dropped = delta_set(before, after, demoted)
    check(set(dropped) == {"C", "D"}, f"delta wrong: {dropped}")
    check("E" not in dropped, "E incorrectly in delta")

    implied = implied_events(dropped, edges, demoted)
    queue = divergence_queue(dropped, after, corpus["docs"], edges, implied)
    docs = [item["doc"] for item in queue]
    check(docs == ["C", "D"], f"queue wrong or misordered: {docs}")
    check(all(item["implied_by_event"] == "synthetic-demotion" for item in queue),
          f"event attribution wrong: {queue}")

    score = score_findings(fixtures["expected_findings"], queue)
    check(score == {"found": ["C", "D"], "missed": [], "extra": []},
          f"score wrong: {score}")

    if failures:
        print("SELF-TEST FAIL")
        for msg in failures:
            print(f"  - {msg}")
        return 1
    print("SELF-TEST PASS (5-node chain: demoting B flags C and D, "
          "queue dependency-ordered, E untouched)")
    return 0


# ----------------------------------------------------------------------- main

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Grounded-closure retrodiction harness (canon.d#11 shadow gate)")
    parser.add_argument("--root", type=Path, default=REPO_ROOT,
                        help="repo root containing docs/ projections")
    parser.add_argument("--kind-table", type=Path, default=DEFAULT_KIND_TABLE)
    parser.add_argument("--anchors-file", type=Path,
                        help="JSON list (or {'anchors': [...]}) of extra anchor ids")
    parser.add_argument("--fixtures", type=Path,
                        help="JSON weakening fixtures (events[].demoted[].node)")
    parser.add_argument("--report", action="store_true",
                        help="print human-readable summary (default unless --json)")
    parser.add_argument("--json", action="store_true", dest="as_json",
                        help="print machine-readable JSON result")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()

    try:
        graph = load_json(args.root / "docs" / "derivation-graph.json")
        corpus = load_json(args.root / "docs" / "corpus-index.json")
        spine = load_json(args.root / "docs" / "spine-data.json")
        kind_table = load_json(args.kind_table)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR loading inputs: {exc}", file=sys.stderr)
        return 1

    fixtures = None
    if args.fixtures:
        try:
            fixtures = load_json(args.fixtures)
        except (OSError, json.JSONDecodeError) as exc:
            print(f"ERROR loading fixtures: {exc}", file=sys.stderr)
            return 1

    result = run_pipeline(graph, corpus, spine, kind_table,
                          anchors_file=args.anchors_file, fixtures=fixtures)

    if args.as_json:
        print(json.dumps(result, indent=2, sort_keys=True))
    if args.report or not args.as_json:
        if args.as_json:
            print()
        print_report(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
