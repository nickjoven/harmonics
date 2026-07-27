#!/usr/bin/env python3
"""
Generator: claims projection from a canon.d intake report.

The clean-ingest artifact (2026-07-22): the corpus's quantitative
claims and their support structure, keyed by proposition CID, so that
discussion can cite stable content addresses instead of prose held in
context. "Context rot" dies here: a claim's record carries WHICH docs
assert it and whether each is on the frontier, so corroboration is
split into frontier vs superseded counts — a claim propped up mainly
by superseded docs announces itself.

Inputs:
  sync_cost/ingest/report.json   canon-demo intake-corpus --json output
                                 (also the --prior-heads input for the
                                 next ingest run — the head chain)
  docs/corpus-index.json         frontier state per doc

Output: docs/claims-index.json
  {generated, ingest: {annotator, telemetry, canon_rev?}, claims: {
     <proposition_cid>: {subject, witness, routes,
                         corroboration, corroboration_docs,
                         corroboration_frontier,
                         docs: [{doc, frontier}], assertion_cids: n}},
   edges: [{from, to, kind, annotation_cid}],
   terms: {term: {home, cid?}}}

Corroboration counts INDEPENDENT witnesses (#328 Card 2): docs joined
by succession edges are one witness — the 13 koide iteration drafts
plus their canonical head are one document's history, not 14
corroborating sources. `corroboration` and `corroboration_frontier`
are succession-chain-deduped; `corroboration_docs` keeps the raw doc
count for transparency.

Regeneration is manual for now (requires the canon-demo binary,
prose features, pre-integration branch); the report is committed so
the projection is reproducible and the chain is unbroken.

Run:
  python3 scripts/build_claims_index.py
  python3 scripts/build_claims_index.py --check
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "sync_cost" / "ingest" / "report.json"
INDEX = ROOT / "docs" / "corpus-index.json"
OUT = ROOT / "docs" / "claims-index.json"


def succession_resolver(corpus: dict):
    """doc_id -> a stable id for its succession chain (union-find over
    superseded_by edges, path-compressed). Two docs share a chain id iff
    they are connected through supersession — a draft and its successor,
    however long the ladder. A doc with no succession edges is its own
    chain."""
    parent: dict = {}

    def find(x: str) -> str:
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for doc, meta in corpus.items():
        for succ in meta.get("superseded_by", []):
            parent[find(doc)] = find(succ)
    return find


def build() -> dict:
    report = json.loads(REPORT.read_text())
    corpus = json.loads(INDEX.read_text())["docs"]
    chain = succession_resolver(corpus)

    def frontier(doc_id: str) -> bool:
        return "superseded_by" not in corpus.get(doc_id, {})

    claims = {}
    edges = []
    terms = {}
    for r in report.get("reports", []):
        doc = r.get("doc_id")
        for p in r.get("propositions", []):
            cid = p.get("proposition_cid")
            if not cid:
                continue
            c = claims.setdefault(cid, {
                "subject": p.get("subject"),
                "witness": p.get("witness"),
                "routes": [],
                "docs": [],
                "assertion_cids": 0,
            })
            for route in p.get("routes", []):
                if route not in c["routes"]:
                    c["routes"].append(route)
            if doc not in [d["doc"] for d in c["docs"]]:
                c["docs"].append({"doc": doc, "frontier": frontier(doc)})
            c["assertion_cids"] += 1
        for e in r.get("edges", []):
            edges.append({k: e[k] for k in ("from", "to", "kind")
                          if k in e} | (
                {"annotation_cid": e["annotation_cid"]}
                if "annotation_cid" in e else {}))
        for t in r.get("terms", []):
            name = t.get("term") or t.get("name")
            if name and name not in terms:
                terms[name] = {k: v for k, v in t.items()
                               if k not in ("term", "name")}

    for c in claims.values():
        # Independent witnesses, not raw docs (#328 Card 2): a succession
        # chain's drafts all repeating a value is one witness. K_lepton=2/3
        # showed corroboration 19 where 13 of the docs were iterations of
        # ONE koide document.
        c["corroboration"] = len({chain(d["doc"]) for d in c["docs"]})
        c["corroboration_docs"] = len(c["docs"])
        c["corroboration_frontier"] = len(
            {chain(d["doc"]) for d in c["docs"] if d["frontier"]})
        c["docs"].sort(key=lambda d: (not d["frontier"], d["doc"]))

    import subprocess
    head = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short",
                           "HEAD"], capture_output=True, text=True).stdout.strip()
    return {
        "generated": head,
        "generator": "scripts/build_claims_index.py",
        "ingest": {
            "annotator": (report.get("reports") or [{}])[0].get("annotator")
                         or report.get("annotator"),
            "telemetry": report.get("telemetry", {}),
        },
        "claim_count": len(claims),
        "claims": dict(sorted(claims.items())),
        "edges": edges,
        "terms": dict(sorted(terms.items())),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not REPORT.exists():
        print(f"no ingest report at {REPORT}; run canon-demo intake-corpus "
              f"--json first")
        return 1
    index = build()
    rendered = json.dumps(index, indent=1, ensure_ascii=False,
                          sort_keys=False) + "\n"
    if args.check:
        if not OUT.exists():
            print("STALE: claims-index missing")
            return 1
        a = json.loads(OUT.read_text())
        b = json.loads(rendered)
        a.pop("generated", None), b.pop("generated", None)
        if a != b:
            print("STALE: claims-index does not match the ingest report")
            return 1
        print(f"OK: claims-index fresh ({index['claim_count']} claims)")
        return 0
    OUT.write_text(rendered)
    t = index["ingest"]["telemetry"]
    print(f"wrote docs/claims-index.json: {index['claim_count']} claims, "
          f"{len(index['edges'])} typed edges, {len(index['terms'])} terms "
          f"(from {t.get('docs')} docs, {t.get('corroborated')} corroborated)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
