#!/usr/bin/env python3
"""Build the problem-surface map from problem/PROBLEM_MAP.yml.

Validates every reference in the curated map against the repo's
registries, then renders docs/problem-map.md (tables + mermaid
diagram) and docs/problem-map.json.

Checks performed (each failure is a WARN line in the output ledger;
missing files / unknown claims are ERRORs and fail the build):

  1. posture / mode values come from the declared vocabularies.
  2. every entry in resolution_docs resolves to a file under
     sync_cost/derivations/ (.md or .py) or the repo root.
  3. every manifest_claims key exists in MANIFEST.yml:scorecard;
     every bare_k1_claims key exists in MANIFEST.yml:bare_k1_identities.
  4. every engines entry resolves to a script on disk.
  5. posture=forced rows: each cited scorecard claim's closure_status
     mentions Class 5 (else WARN — tier/claim mismatch).
  6. docs cited by forced rows that corpus-index marks prose-only are
     noted as articulation-grade (not an error).
  7. INDEX.md D-numbers are cross-checked against
     MANIFEST.yml:derivation_count (out-of-range D-numbers → WARN).

Usage:  python3 scripts/build_problem_map.py [--check]
        --check: validate only, exit non-zero on ERROR, write nothing.
"""

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DERIV = ROOT / "sync_cost" / "derivations"
MAP_PATH = ROOT / "problem" / "PROBLEM_MAP.yml"
MANIFEST_PATH = ROOT / "MANIFEST.yml"
CORPUS_INDEX = ROOT / "docs" / "corpus-index.json"
INDEX_MD = DERIV / "INDEX.md"
OUT_MD = ROOT / "docs" / "problem-map.md"
OUT_JSON = ROOT / "docs" / "problem-map.json"

TIER_LABELS = {
    "forced": "Tier 1 — substrate-forced (the firm lines)",
    "declined": "Tier 2 — structurally declined (the honest lines)",
    "proposed": "Tier 3 — proposed (conditional or unreconciled; testable)",
    "open": "Tier 4 — operationally open (the honest gaps)",
}


def resolve_doc(name: str):
    """Return repo-relative path for a doc/script reference, or None."""
    for cand in (
        DERIV / f"{name}.md",
        DERIV / f"{name}.py",
        DERIV / name,
        ROOT / name,
        ROOT / "scripts" / name,
    ):
        if cand.is_file():
            return cand.relative_to(ROOT).as_posix()
    return None


def check_index_dnumbers(manifest):
    """Cross-check INDEX.md D-numbers against MANIFEST derivation_count."""
    warns = []
    count = manifest.get("derivation_count")
    if not isinstance(count, int):
        return ["MANIFEST.yml derivation_count missing or non-integer"]
    text = INDEX_MD.read_text()
    mapped = {int(m) for m in re.findall(r"^\|\s*D(\d+)\s*\|", text, re.M)}
    over = sorted(d for d in mapped if d > count)
    if over:
        warns.append(
            f"INDEX.md maps D-numbers beyond MANIFEST derivation_count={count}: "
            + ", ".join(f"D{d}" for d in over)
        )
    # entries listed both in the mapping table and the "Not mapped" prose
    m = re.search(r"^- \*\*D2, ([^*]+)\*\*", text, re.M)
    if m:
        unmapped_note = "D2, " + m.group(1)
        singles = {int(x) for x in re.findall(r"D(\d+)(?![\d–-])", unmapped_note)}
        for a, b in re.findall(r"D(\d+)[–-]D(\d+)", unmapped_note):
            singles.update(range(int(a), int(b) + 1))
        both = sorted(mapped & singles)
        if both:
            warns.append(
                "INDEX.md lists D-numbers as unmapped that its own table maps: "
                + ", ".join(f"D{d}" for d in both)
            )
    return warns


def main():
    check_only = "--check" in sys.argv
    errors, warns, notes = [], [], []

    spec = yaml.safe_load(MAP_PATH.read_text())
    manifest = yaml.safe_load(MANIFEST_PATH.read_text())
    corpus = json.loads(CORPUS_INDEX.read_text()).get("docs", {})

    postures = set(spec.get("posture_vocab", []))
    modes = set(spec.get("mode_vocab", []))
    scorecard = manifest.get("scorecard", {})
    bare_k1 = manifest.get("bare_k1_identities", {})

    problems = spec["problems"]
    seen_ids = set()
    for p in problems:
        pid = p.get("id", "<missing id>")
        if pid in seen_ids:
            errors.append(f"{pid}: duplicate id")
        seen_ids.add(pid)
        if p.get("posture") not in postures:
            errors.append(f"{pid}: posture {p.get('posture')!r} not in {sorted(postures)}")
        if p.get("mode") not in modes:
            errors.append(f"{pid}: mode {p.get('mode')!r} not in {sorted(modes)}")

        p["_doc_paths"] = {}
        for d in p.get("resolution_docs", []):
            path = resolve_doc(d)
            if path is None:
                errors.append(f"{pid}: resolution doc {d!r} not found on disk")
            else:
                p["_doc_paths"][d] = path
                rec = corpus.get(d)
                if rec and p.get("posture") == "forced" and rec.get("coverage") == "prose-only":
                    notes.append(f"{pid}: cited doc {d} is prose-only (articulation-grade)")

        for c in p.get("manifest_claims", []):
            if c not in scorecard:
                errors.append(f"{pid}: manifest claim {c!r} not in MANIFEST.yml:scorecard")
            elif p.get("posture") == "forced":
                status = str(scorecard[c].get("closure_status", ""))
                if "Class 5" not in status:
                    warns.append(
                        f"{pid}: forced-tier row cites scorecard claim {c!r} "
                        f"whose closure_status is not Class 5: {status[:80]!r}"
                    )
        for c in p.get("bare_k1_claims", []):
            if c not in bare_k1:
                errors.append(f"{pid}: bare-K=1 claim {c!r} not in MANIFEST.yml:bare_k1_identities")
        for s in p.get("engines", []):
            if resolve_doc(s.removesuffix(".py")) is None and resolve_doc(s) is None:
                errors.append(f"{pid}: engine/script {s!r} not found on disk")

    warns.extend(check_index_dnumbers(manifest))

    for line in errors:
        print(f"ERROR {line}", file=sys.stderr)
    for line in warns:
        print(f"WARN  {line}")
    for line in notes:
        print(f"note  {line}")
    if errors:
        sys.exit(1)
    if check_only:
        print(f"ok: {len(problems)} problems validated")
        return

    # ---- render ----------------------------------------------------
    by_tier = {t: [p for p in problems if p["posture"] == t] for t in TIER_LABELS}

    def doc_links(p):
        parts = []
        for d, path in p["_doc_paths"].items():
            parts.append(f"[`{d}`](../{path})")
        return ", ".join(parts)

    lines = [
        "# Problem-surface map",
        "",
        "What named problems of physics this repository takes a defensible",
        "position on, tiered by the possibility-discipline discriminator",
        "(`canonical_glossary.md` §8). Generated by",
        "`scripts/build_problem_map.py` from `problem/PROBLEM_MAP.yml`;",
        "every doc, claim, and script reference below is machine-checked",
        "against `MANIFEST.yml`, the derivations directory, and",
        "`docs/corpus-index.json`. Do not edit by hand.",
        "",
    ]

    for tier, label in TIER_LABELS.items():
        rows = by_tier[tier]
        if not rows:
            continue
        lines += [f"## {label}", ""]
        for p in rows:
            moniker = f" — *{p['moniker']}*" if p.get("moniker") else ""
            lines += [f"### {p['title']}{moniker}", ""]
            lines += [p["statement"].strip(), ""]
            claims = p.get("manifest_claims", []) + p.get("bare_k1_claims", [])
            if claims:
                lines += ["**MANIFEST claims:** " + ", ".join(f"`{c}`" for c in claims), ""]
            lines += ["**Docs:** " + doc_links(p), ""]
            if p.get("engines"):
                lines += ["**Scripts:** " + ", ".join(f"`{s}`" for s in p["engines"]), ""]
            if p.get("test"):
                lines += ["**Test / falsifier:** " + p["test"].strip(), ""]
            if p.get("caveats"):
                lines += ["**Caveat:** " + p["caveats"].strip(), ""]

    # mermaid overview: problems grouped by tier, edge to primary doc
    lines += ["## Overview diagram", "", "```mermaid", "flowchart LR"]
    for tier, label in TIER_LABELS.items():
        rows = by_tier[tier]
        if not rows:
            continue
        lines.append(f'  subgraph {tier}["{label}"]')
        for p in rows:
            lines.append(f'    {p["id"]}["{p["title"]}"]')
        lines.append("  end")
    for tier, rows in by_tier.items():
        for p in rows:
            docs = list(p["_doc_paths"])
            if docs:
                primary = docs[0]
                lines.append(f'  {p["id"]} --> doc_{primary}(["{primary}.md"])')
    lines += ["```", ""]

    if warns or notes:
        lines += ["## Mechanical consistency ledger", "",
                  "Warnings raised by the generator on the current tree:", ""]
        lines += [f"- WARN: {w}" for w in warns]
        lines += [f"- note: {n}" for n in notes]
        lines += [""]

    counts = {t: len(by_tier[t]) for t in TIER_LABELS}
    lines += [
        "---",
        "",
        f"Problems: {len(problems)} "
        f"(forced {counts['forced']}, declined {counts['declined']}, "
        f"proposed {counts['proposed']}, open {counts['open']}). "
        "Source of truth for quantities: `MANIFEST.yml`; for status:",
        "`framework_status.md`. This map is a view, not a registry.",
    ]

    OUT_MD.write_text("\n".join(lines) + "\n")

    payload = {
        "generator": "scripts/build_problem_map.py",
        "source": "problem/PROBLEM_MAP.yml",
        "problems": [
            {k: v for k, v in p.items() if not k.startswith("_")} | {
                "doc_paths": p["_doc_paths"],
            }
            for p in problems
        ],
        "warnings": warns,
        "notes": notes,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUT_MD.relative_to(ROOT)} and {OUT_JSON.relative_to(ROOT)} "
          f"({len(problems)} problems)")


if __name__ == "__main__":
    main()
