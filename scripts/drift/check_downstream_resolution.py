#!/usr/bin/env python3
"""
Check: downstream-resolution divergence (issue #294; advisory).

The failure class this kills: a doc keeps asserting strength after the
ground it committed to has weakened, silently, until a manual audit
notices (the coupling_scales rows survived the 2026-04 demotion for 88
days; the F1/F2/O1/O2 postmortem is the same failure with the sign
flipped). The mechanism was validated by the canon.d#11 retrodiction
gate (harmonics#314, 4/4 with zero extras): the divergence signal is
edge-local to the COMMITTED layer, not global to the closure.

Weak grounds are read from STRUCTURED surfaces only (owner ruling,
2026-07-21; no prose regex taxonomy):
  - docs the corpus index marks superseded (computed succession)
  - docs whose structured class projection contains Class 1

A doc diverges when a committed support edge (grounds/derives, from its
## Lineage block) lands on a weak ground while its own surface still
asserts strength (Class 5, or a "Derived" status line that does not
acknowledge a rescope/supersession). Succession divergence: a
superseded doc whose surface does not name its successor.

Destination: this becomes a query over sealed claim quanta in the Dolt
projection once canon.d#6/#11 land; this file is the projection-level
interim. ADVISORY in run_all.py until the false-positive record argues
for promotion. Promotion criterion (set 2026-07-29, per the gate
ladder): FATAL after four consecutive weeks of CI runs with zero false
positives dating from the Card 8 fix (#327, 2026-07-24) — i.e.
promote on the first run_all touch after 2026-08-21 if the record
stays clean. One false positive resets the clock and returns the
predicate to apprenticeship.

Exit code = number of divergent docs (advisory).
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

DERIVED_RE = re.compile(r"\bDerived\b")
ACK_RE = re.compile(r"rescoped|superseded|historical", re.IGNORECASE)
COMMITTED_KINDS = {"grounds", "derives"}


def main() -> int:
    graph = json.loads((ROOT / "docs/derivation-graph.json").read_text())
    index = json.loads((ROOT / "docs/corpus-index.json").read_text())["docs"]

    # Class membership must be SELF-DECLARED (the doc's own status line or
    # Status-section bold), never the corpus-index `classes` scrape — that
    # field records every prose MENTION, so reference docs that discuss
    # Class 1 (glossary, cross-reference atlas) carry classes=[1,2,4,5]
    # without being any of them. First audit session's Card 8 was this
    # false positive (2026-07-24); the audit misdiagnosed it as an edge-
    # direction bug, but direction was correct — membership was polluted.
    def self_status(m):
        return " ".join(filter(None, [m.get("status_line"),
                                      m.get("status_bold")]))

    CLASS1_RE = re.compile(r"\bClass[ -]?1\b")
    weak = {d for d, m in index.items()
            if "superseded_by" in m or CLASS1_RE.search(self_status(m))}

    divergent = []
    for node in graph["nodes"]:
        doc_id = node["id"]
        meta = index.get(doc_id, {})
        committed_weak = sorted(
            e["target"] for e in node.get("edges", [])
            if e["kind"] in COMMITTED_KINDS and e["target"] in weak)
        if committed_weak:
            # status_bold covers section-style statuses ('## Status' +
            # bold verdict) that have no inline '**Status**:' line —
            # coupling_scales, this check's motivating doc, is one
            # (review finding 5, 2026-07-21).
            status = self_status(meta)
            asserts = (re.search(r"\bClass[ -]?5\b", status)
                       or (DERIVED_RE.search(status)
                           and not ACK_RE.search(status)))
            if asserts:
                divergent.append(
                    (doc_id, f"committed support on weak ground(s) "
                             f"{committed_weak}, surface asserts strength"))
        if "superseded_by" in meta:
            # basis "declared" means the doc self-declares its supersession
            # (RULES 0-8 harvest), which is acknowledgment by definition.
            # basis "quantum" is a sealed committed SUCCEEDS declaration in
            # sync_cost/successions.jsonl — acknowledgment in the envelope,
            # STRONGER than prose (commitment 8: provenance lives in the
            # envelope, never in content), so demanding a surface banner on
            # top would re-litigate the koide arc's banner removal (#319).
            # This branch remains for genuinely un-acknowledged bases
            # (e.g. a future inferred supersession).
            if str(meta.get("superseded_basis", "")) not in (
                    "declared", "quantum"):
                successors = meta["superseded_by"]
                status = meta.get("status_line") or ""
                if (not any(s in status for s in successors)
                        and not ACK_RE.search(status)):
                    divergent.append(
                        (doc_id, f"superseded by {successors}, surface "
                                 f"does not acknowledge it"))

    if divergent:
        print(f"NOTE: {len(divergent)} downstream-resolution divergence(s) "
              f"(advisory — see issue #294):")
        for doc_id, why in divergent:
            print(f"  {doc_id}: {why}")
        return 1  # never a count: exit status truncates mod 256
    print(f"OK: no committed support on weak grounds "
          f"({len(weak)} weak-ground docs tracked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
