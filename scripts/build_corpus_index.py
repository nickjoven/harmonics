#!/usr/bin/env python3
"""
Generator: machine-readable corpus index (issue #263 ⓾ / #295 groundwork).

The corpus self-classifies claims Class 1–5 as honor-system inline prose
(see `numerology_inventory.md`), and doc status lives in free-text
`**Status**:` lines. `scripts/drift/lint_class_tags.py` reports the
*coverage gap*; this script goes one step further and projects the tags
themselves — per top-level derivation doc — into a single committed JSON
artifact, so "list all Class-5 claims" is a lookup instead of a 322-file
regex sweep.

Per doc it records:
  title        first `# ` heading
  classes      all Class 1–5 tags found (doc may cite several)
  coverage     classified | unclassified-quantitative | prose-only
               (same taxonomy as lint_class_tags.py)
  status_line  first `**Status**:` line, verbatim (free prose, advisory)
  has_lineage  whether a typed `## Lineage` section exists (issue #300)
  d_numbers    D-numbers mapped to this file by INDEX.md

Like `docs/derivation-graph.json`, the output is a committed projection:
regenerate after corpus edits. Deterministic (sorted) so diffs are stable.

Run:
  python3 scripts/build_corpus_index.py            # writes docs/corpus-index.json
  python3 scripts/build_corpus_index.py --check    # exit 1 if committed file is stale
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

CLASS_RE = re.compile(r"\bClass[ -]?([1-5])\b")
QUANT_RE = re.compile(r"≈|=\s*0\.\d|σ|%")
STATUS_RE = re.compile(r"^\*\*Status\*\*:\s*(.+)$", re.MULTILINE)
LINEAGE_RE = re.compile(r"^## Lineage\s*$", re.MULTILINE)
TITLE_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
# INDEX.md mapping rows: | D1 | [`born_rule.md`](born_rule.md) | ... |
INDEX_ROW_RE = re.compile(r"^\|\s*(D\d+)\s*\|\s*\[`([^`]+)`\]")

OUT_REL = "docs/corpus-index.json"


def load_dnumbers(deriv: Path) -> dict:
    """filename stem -> [D-numbers], from INDEX.md's mapping table."""
    index = deriv / "INDEX.md"
    stems = {}
    if not index.exists():
        return stems
    for line in index.read_text(errors="replace").splitlines():
        m = INDEX_ROW_RE.match(line)
        if m:
            stems.setdefault(Path(m.group(2)).stem, []).append(m.group(1))
    return stems


def build(root: Path) -> dict:
    deriv = root / "sync_cost" / "derivations"
    dnums = load_dnumbers(deriv)
    docs = {}
    totals = {"classified": 0, "unclassified-quantitative": 0, "prose-only": 0}
    for p in sorted(deriv.glob("*.md")):
        text = p.read_text(errors="replace")
        classes = sorted({int(c) for c in CLASS_RE.findall(text)})
        if classes:
            coverage = "classified"
        elif QUANT_RE.search(text):
            coverage = "unclassified-quantitative"
        else:
            coverage = "prose-only"
        totals[coverage] += 1
        status = STATUS_RE.search(text)
        title = TITLE_RE.search(text)
        docs[p.stem] = {
            "title": title.group(1).strip() if title else p.stem,
            "classes": classes,
            "coverage": coverage,
            "status_line": status.group(1).strip() if status else None,
            "has_lineage": bool(LINEAGE_RE.search(text)),
            "d_numbers": dnums.get(p.stem, []),
        }
    head = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "--short", "HEAD"],
        capture_output=True, text=True,
    ).stdout.strip()
    return {
        "generated": head,
        "generator": "scripts/build_corpus_index.py",
        "count": len(docs),
        "coverage_totals": totals,
        "docs": docs,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="repo root")
    parser.add_argument("--check", action="store_true",
                        help="exit 1 if the committed index is stale")
    args = parser.parse_args()
    root = Path(args.root).resolve()

    index = build(root)
    out = root / OUT_REL
    rendered = json.dumps(index, indent=1, ensure_ascii=False, sort_keys=True) + "\n"

    if args.check:
        if not out.exists():
            print(f"STALE: {OUT_REL} missing")
            return 1
        committed = json.loads(out.read_text())
        fresh = json.loads(rendered)
        # compare content, not the generated-at sha
        committed.pop("generated", None), fresh.pop("generated", None)
        if committed != fresh:
            print(f"STALE: {OUT_REL} does not match the corpus — regenerate")
            return 1
        print(f"OK: {OUT_REL} is fresh ({index['count']} docs)")
        return 0

    out.write_text(rendered)
    t = index["coverage_totals"]
    print(f"wrote {OUT_REL}: {index['count']} docs "
          f"(classified {t['classified']}, unclassified-quant "
          f"{t['unclassified-quantitative']}, prose-only {t['prose-only']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
