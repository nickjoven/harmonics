#!/usr/bin/env python3
"""
Check: successions ledger integrity (FATAL).

sync_cost/successions.jsonl carries committed SUCCEEDS declarations —
owner rulings sealed through declare_succession. The MCP tool validates
at write time (targets exist, no cycles, dedup), but nothing
re-validated the ledger as a READER: a hand edit, a bad merge
resolution, or a partial recovery would pass every existing gate while
frontier computation quietly consumed garbage. (This check's sibling,
check_enforced_coverage.py, exists because the ledger itself was lost
off main for a week, 2026-07-29 — write-time validation is worthless
against history-level accidents.)

Validates, for every SUCCEEDS record: JSON well-formedness, required
fields (old, new, agent, time, modality), old/new naming real
derivation docs, and global acyclicity of the old -> new graph.
Unknown `kind` values are ignored (forward-compatible: new record
kinds must not fail an old validator) but counted in the output.

FATAL from birth per the gate ladder: the predicate is structural
validity, crisp and cheap, and the error model is exact — nothing
about a malformed committed record is a matter of interpretation.

Exit code: number of violations.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "sync_cost" / "successions.jsonl"
DERIVATIONS = ROOT / "sync_cost" / "derivations"

REQUIRED = ("old", "new", "agent", "time", "modality")


def main() -> int:
    if not LEDGER.exists():
        # existence is check_enforced_coverage.py's job; absence here is
        # reported once, not double-counted.
        print(f"(no ledger at {LEDGER} — enforced-coverage check owns "
              f"existence)")
        return 0

    violations = []
    edges = []
    other_kinds = 0
    for n, line in enumerate(LEDGER.read_text().splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError as e:
            violations.append(f"line {n}: unparseable JSON ({e})")
            continue
        if rec.get("kind") != "SUCCEEDS":
            other_kinds += 1
            continue
        missing = [f for f in REQUIRED if not rec.get(f)]
        if missing:
            violations.append(f"line {n}: missing field(s) {missing}")
            continue
        old = rec["old"]
        new = rec["new"] if isinstance(rec["new"], list) else [rec["new"]]
        for doc in [old, *new]:
            if not (DERIVATIONS / f"{doc}.md").exists():
                violations.append(
                    f"line {n}: `{doc}` names no derivation doc")
        for target in new:
            if target == old:
                violations.append(f"line {n}: `{old}` succeeds itself")
            edges.append((old, target))

    # Acyclicity over the full declared graph (multi-record cycles that
    # no single write could see).
    adj = {}
    for a, b in edges:
        adj.setdefault(a, set()).add(b)
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {}

    def cyclic(node) -> bool:
        color[node] = GRAY
        for nxt in adj.get(node, ()):
            c = color.get(nxt, WHITE)
            if c == GRAY or (c == WHITE and cyclic(nxt)):
                return True
        color[node] = BLACK
        return False

    for node in list(adj):
        if color.get(node, WHITE) == WHITE and cyclic(node):
            violations.append(f"cycle through `{node}` in the succession "
                              f"graph")
            break

    if violations:
        print(f"FATAL: {len(violations)} successions-ledger violation(s):")
        for v in violations:
            print(f"  {v}")
        return 1  # never a count: exit status truncates mod 256
    note = f", {other_kinds} non-SUCCEEDS record(s) ignored" \
        if other_kinds else ""
    print(f"OK: {len(edges)} SUCCEEDS edge(s) well-formed, targets "
          f"resolve, acyclic{note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
