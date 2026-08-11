#!/usr/bin/env python3
"""Reading-layer lint: docs state current truth only.

Live documents must not carry correction scar tissue — strikethrough
retractions, dated correction banners, or inline "(corrected ...)"
stamps. Corrections are integrated into the prose as a new edition
(HTML comment on line 1) and ledgered in sync_cost/derivations/ERRATA.md.
Rationale: most consumption is retrieval-augmented — a chunk containing
a struck-through claim or a caveat divorced from its target reads as
the claim itself.

Exempt: *_audit.md (point-in-time records; one-line errata pointers
allowed), ERRATA.md itself, and explicit correction-record documents.

Exit codes: 0 clean, 1 findings (advisory).
"""

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

SCAR_PATTERNS = [
    (re.compile(r"~~[^~\n]{3,}~~"), "strikethrough retraction"),
    (re.compile(r"CORRECTION NOTICE"), "correction banner"),
    (re.compile(r"STATUS CORRECTION"), "correction banner"),
    (re.compile(r"\bCORRECTION \(20\d\d"), "dated correction banner"),
    (re.compile(r"\bCorrection \(20\d\d"), "dated correction stamp"),
    (re.compile(r"\(corrected 20\d\d"), "inline corrected-stamp"),
    (re.compile(r"\bRetired \(20\d\d"), "dated retirement stamp"),
    (re.compile(r"see correction notice"), "dangling correction pointer"),
    (re.compile(r"correction banner"), "dangling banner pointer"),
]

EXEMPT = {"ERRATA.md"}


def is_exempt(path: Path) -> bool:
    if path.name in EXEMPT:
        return True
    if path.name.endswith("_audit.md"):
        return True
    if "correction" in path.name:  # explicit correction-record docs
        return True
    return False


def main() -> int:
    roots = [REPO / "sync_cost", REPO / "docs"]
    extra = [REPO / "README.md", REPO / "RESULTS.md"]
    files = [p for root in roots if root.exists() for p in root.rglob("*.md")]
    files += [p for p in extra if p.exists()]

    findings = []
    for path in sorted(files):
        if is_exempt(path):
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except OSError:
            continue
        for i, line in enumerate(lines, 1):
            for pat, label in SCAR_PATTERNS:
                if pat.search(line):
                    findings.append((path.relative_to(REPO), i, label, line.strip()[:90]))
                    break

    if not findings:
        print("reading-layer: clean (no scar tissue in live docs)")
        return 0

    print(f"reading-layer: {len(findings)} scar-tissue site(s) in live docs")
    print("policy: republish as a new edition (integrate the correction; "
          "ledger it in ERRATA.md; HTML edition comment on line 1)")
    for rel, lineno, label, text in findings:
        print(f"  {rel}:{lineno}  [{label}]  {text}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
