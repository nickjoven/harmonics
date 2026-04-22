#!/usr/bin/env python3
"""
Tool #5: Fitted-correction linter.

Scans markdown and Python files for un-audited ad-hoc additive
corrections to bare K=1 identities. Patterns like `+ 8/F_10^2`,
`+ 1/228`, `+ 1/q_3^2`, `+ 8/3025` are suspicious — if they don't
have a derivation, they're fitted terms that should be explicitly
labelled (or removed).

The linter flags matches and checks whether the surrounding context
(within 40 lines) contains a retraction/status marker. Unmarked
matches exit 1.

Run:
  python3 scripts/drift/lint_fitted_corrections.py
"""

import argparse
import re
import sys
from pathlib import Path


SUSPECT_PATTERNS = [
    r"\+\s*8\s*/\s*F_?10",            # 8/F_10^2 Fibonacci-square correction
    r"\+\s*8\s*/\s*3025",             # 8/3025 (same as above, expanded)
    r"\+\s*1\s*/\s*q_?3\s*\^?2\b",    # 1/q_3^2 = 1/9 gauge correction
    r"\+\s*1\s*/\s*228\b",            # 1/228 Higgs boundary correction
    r"\b251\s*/\s*72\b",              # 27/8 + 1/9 = 251/72 shortcut form
    # Narrow: only flag "+ 1/9" when next to a sin²θ_W or α_s/α_2 cue,
    # so unrelated arithmetic like "1/18 + 4/9 + 1/9" is not matched.
    r"(?:sin[\^2²]|alpha_s|α_s|27/8|ratio)[^\n]{0,60}\+\s*1\s*/\s*9\b",
]

COMPILED = [re.compile(p, re.IGNORECASE) for p in SUSPECT_PATTERNS]

# Words that, if present in a ±CONTEXT_LINES window, indicate the
# author has explicitly marked the correction as retracted / withdrawn
# OR is actively auditing it (Class 4 = needs audit; these are
# legitimate discussions, not fresh assertions).
RETRACTION_MARKERS = (
    "retracted", "withdrawn", "declined", "removed", "fitted term",
    "not derived", "honest-null", "previously", "deprecated",
    "bare reference", "bare k=1", "class 1", "class 3", "class 4",
    "audit", "pending", "conjecture", "numerology",
)
CONTEXT_LINES = 60

# Files to scan. The suffix + directory filter is intentionally
# narrow; expand if needed.
WATCHED_EXTS = (".md", ".py")
WATCHED_DIRS = ("sync_cost", "docs", "scripts", "README.md", "RESULTS.md", "MANIFEST.yml")

# Skip scratch/exploratory directories — those contain failed
# hypotheses and intentional dead ends.
SKIP_PATH_PARTS = ("/scratch/", "/data/")

# Allowlist: specific files whose matches are known-legit enumeration
# tables (scanning many candidate expressions against a target), not
# claims of "the prediction is X + correction". Add (path, reason).
FILE_ALLOWLIST: list[tuple[str, str]] = [
    (
        "sync_cost/derivations/primitives_first.py",
        "Section 2 enumerates candidate rationals for a_1(lep); table rows, not claims",
    ),
    (
        "sync_cost/derivations/saddle_node_regularized.py",
        "candidate-enumeration table; each row is a hypothesis, not an assertion",
    ),
]


def _has_retraction_nearby(lines: list[str], idx: int) -> bool:
    lo = max(0, idx - CONTEXT_LINES)
    hi = min(len(lines), idx + CONTEXT_LINES)
    window = "\n".join(lines[lo:hi]).lower()
    return any(m in window for m in RETRACTION_MARKERS)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="repo root")
    args = parser.parse_args()
    root = Path(args.root).resolve()

    candidates: list[Path] = []
    for item in WATCHED_DIRS:
        p = root / item
        if p.is_file():
            candidates.append(p)
        elif p.is_dir():
            for ext in WATCHED_EXTS:
                candidates.extend(p.rglob(f"*{ext}"))

    unmarked: list[tuple[Path, int, str, str]] = []
    for path in sorted(set(candidates)):
        str_path = str(path)
        if any(skip in str_path for skip in SKIP_PATH_PARTS):
            continue
        rel_path = path.relative_to(root).as_posix() if path.is_absolute() else path.as_posix()
        if any(rel_path.endswith(allow) or rel_path == allow for allow, _ in FILE_ALLOWLIST):
            continue
        try:
            text = path.read_text(errors="ignore")
        except Exception:
            continue
        lines = text.splitlines()
        for i, line in enumerate(lines):
            for pat in COMPILED:
                if pat.search(line):
                    if not _has_retraction_nearby(lines, i):
                        unmarked.append((path.relative_to(root), i + 1, pat.pattern, line.strip()))

    if unmarked:
        print(f"Unmarked fitted corrections: {len(unmarked)} occurrence(s)")
        for rel, i, pat, snippet in unmarked:
            print(f"  {rel}:{i}  [/{pat}/]  {snippet}")
        print()
        print("Either (a) derive the correction in a markdown under")
        print("sync_cost/derivations/ and reference it from this location,")
        print("or (b) remove the correction and mark it retracted.")
        return 1

    print(f"OK: scanned {len(candidates)} files, 0 unmarked fitted corrections")
    return 0


if __name__ == "__main__":
    sys.exit(main())
