#!/usr/bin/env python3
"""
Tool: Class-tag coverage reporter (issue #263 ⓾).

Numerology claims across the corpus are self-classified Class 1–5
per `numerology_inventory.md`'s taxonomy — but the tag is honor-system
inline prose, with no machine-readable convention. This reporter makes
the coverage gap visible: it flags top-level derivation docs that carry
*quantitative* claims (near-match markers) yet carry no `Class [1-5]`
self-classification.

It is a COVERAGE SIGNAL, not a policy violation — many flagged docs
legitimately take no numerology class (a proof is Class 5 at most; an
audit doc classifies *other* claims, not itself). So it is ADVISORY in
run_all.py: the count prints for visibility and never gates a commit.
The remedy is a human/curated class judgment per doc, not a mechanical
stamp — see the ⓾ triage on issue #263.

Exit code = number of unclassified-quantitative docs (advisory; shielded
by the ADVISORY set in run_all.py). 0 when the tail is closed.

Run:
  python3 scripts/drift/lint_class_tags.py           # summary + sample
  python3 scripts/drift/lint_class_tags.py --list     # full list
"""

import argparse
import re
import sys
from pathlib import Path

# A doc is "classified" if it self-tags anywhere with Class 1–5, in any
# of the observed prose spellings ("Class 3", "Class-3", "**Class 5**").
CLASS_RE = re.compile(r"\bClass[ -]?[1-5]\b")

# A doc is "quantitative" if it carries a near-match marker: an approx
# sign, a sub-unity decimal, a sigma, or a percent. These are the
# markers a numerology near-match is expressed with; prose-only docs
# (definitions, narrative) carry none and are not expected to classify.
QUANT_RE = re.compile(r"≈|=\s*0\.\d|σ|%")


def scan(root: Path):
    deriv = root / "sync_cost" / "derivations"
    classified, unclassified_quant, unclassified_prose = [], [], []
    for p in sorted(deriv.glob("*.md")):
        text = p.read_text(errors="replace")
        if CLASS_RE.search(text):
            classified.append(p.name)
        elif QUANT_RE.search(text):
            unclassified_quant.append(p.name)
        else:
            unclassified_prose.append(p.name)
    return classified, unclassified_quant, unclassified_prose


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="repo root")
    parser.add_argument("--list", action="store_true",
                        help="print the full unclassified-quantitative list")
    args = parser.parse_args()
    root = Path(args.root).resolve()

    classified, unclass_quant, unclass_prose = scan(root)
    total = len(classified) + len(unclass_quant) + len(unclass_prose)
    if total == 0:
        print("no derivation docs found")
        return 0

    print(f"Class-tag coverage over {total} top-level derivation docs:")
    print(f"  classified (Class 1–5):        {len(classified)} "
          f"({100 * len(classified) // total}%)")
    print(f"  unclassified, quantitative:    {len(unclass_quant)}  <- coverage gap")
    print(f"  unclassified, prose-only:      {len(unclass_prose)}  (no class expected)")

    if unclass_quant:
        print()
        print(f"NOTE: {len(unclass_quant)} quantitative doc(s) carry no Class 1–5 tag "
              f"(advisory — see issue #263 ⓾):")
        show = unclass_quant if args.list else unclass_quant[:10]
        for name in show:
            print(f"  {name}")
        if not args.list and len(unclass_quant) > 10:
            print(f"  ... and {len(unclass_quant) - 10} more (--list for all)")

    return len(unclass_quant)


if __name__ == "__main__":
    sys.exit(main())
