#!/usr/bin/env python3
"""Premise-ledger checker. See sync_cost/derivations/PREMISES.md.

Parses `<!-- provides: name status=... -->` and
`<!-- premises: name@doc, ... -->` anchors from markdown docs and
enforces: resolution, provider uniqueness, status propagation, and
acyclicity. Ratchet: only docs that declare anchors participate.

Exit codes: 0 clean, 2 violations (gating-grade findings).
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

STATUSES = {"axiom", "definition", "proven", "derived", "imported",
            "conditional", "conjectured", "fitted"}
SETTLED = {"axiom", "definition", "proven", "derived", "imported"}
STRONG = {"proven", "derived"}

PROVIDES_RE = re.compile(
    r"<!--\s*provides:\s*([a-z0-9][a-z0-9-]*)\s+status=([a-z]+)\s*-->")
PREMISES_RE = re.compile(r"<!--\s*premises:\s*([^>]+?)\s*-->")
ENTRY_RE = re.compile(r"^([a-z0-9][a-z0-9-]*)@([A-Za-z0-9_.-]+)$")


def scan():
    provides = {}          # name -> (doc, status, line)
    premises = defaultdict(list)  # doc -> [(name, provider_doc, line)]
    errors = []
    docs = sorted((ROOT / "sync_cost").rglob("*.md"))
    for path in docs:
        doc = path.stem
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            for m in PROVIDES_RE.finditer(line):
                name, status = m.group(1), m.group(2)
                if status not in STATUSES:
                    errors.append(f"{doc}:{i}: unknown status '{status}' for '{name}'")
                    continue
                if name in provides:
                    other = provides[name]
                    errors.append(
                        f"{doc}:{i}: duplicate provider for '{name}' "
                        f"(also provided by {other[0]}:{other[2]}) — one name, one doc")
                    continue
                provides[name] = (doc, status, i)
            for m in PREMISES_RE.finditer(line):
                for raw in m.group(1).split(","):
                    raw = raw.strip()
                    if not raw:
                        continue
                    e = ENTRY_RE.match(raw)
                    if not e:
                        errors.append(f"{doc}:{i}: unparseable premise entry '{raw}'")
                        continue
                    premises[doc].append((e.group(1), Path(e.group(2)).stem, i))
    return provides, premises, errors


def main() -> int:
    provides, premises, errors = scan()

    # 1. resolution
    for doc, entries in premises.items():
        for name, pdoc, line in entries:
            if name not in provides:
                errors.append(f"{doc}:{line}: premise '{name}' has no provider anywhere")
            elif provides[name][0] != pdoc:
                errors.append(
                    f"{doc}:{line}: premise '{name}' attributed to {pdoc}, "
                    f"but its provider is {provides[name][0]}")

    # build doc-level graph: doc -> premise provider docs
    graph = {doc: {provides[n][0] for n, _, _ in entries if n in provides}
             for doc, entries in premises.items()}

    # 2. effective status: a doc's weakest premise taints its strong provides
    def weakest_reachable(doc, seen):
        worst = "settled"
        for name, _, _ in premises.get(doc, []):
            if name not in provides:
                continue
            pdoc, status, _ = provides[name]
            if status not in SETTLED:
                return "unsettled"
            if pdoc not in seen:
                seen.add(pdoc)
                if weakest_reachable(pdoc, seen) == "unsettled":
                    return "unsettled"
        return worst

    for name, (doc, status, line) in sorted(provides.items()):
        if status in STRONG and weakest_reachable(doc, {doc}) == "unsettled":
            errors.append(
                f"{doc}:{line}: provides '{name}' status={status}, but a premise "
                f"resolves (transitively) to conjectured/fitted/conditional — "
                f"strongest allowed is 'conditional'")

    # 3. cycles
    WHITE, GRAY, BLACK = 0, 1, 2
    color = defaultdict(int)

    def dfs(d, stack):
        color[d] = GRAY
        for nxt in graph.get(d, ()):
            if color[nxt] == GRAY:
                cyc = stack[stack.index(nxt):] + [nxt] if nxt in stack else [d, nxt]
                errors.append("premise cycle: " + " -> ".join(cyc))
            elif color[nxt] == WHITE:
                dfs(nxt, stack + [nxt])
        color[d] = BLACK

    for d in graph:
        if color[d] == WHITE:
            dfs(d, [d])

    n_anchor = len(provides)
    n_edge = sum(len(v) for v in premises.values())
    if errors:
        print(f"premise-ledger: {len(errors)} violation(s) "
              f"({n_anchor} anchors, {n_edge} premise edges)")
        for e in errors:
            print("  " + e)
        return 2
    print(f"premise-ledger: clean ({n_anchor} anchors, {n_edge} premise edges, "
          f"{len(graph)} citing docs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
