#!/usr/bin/env python3
"""
Tool: Negation-seal linter (prototype, Wave-1 step 1 spinoff).

The dual of drift: drift catches when sealed content has MOVED from its
last-recorded address; negation seals catch when explicitly retracted /
superseded content RE-APPEARS in fresh writing. The substrate already
records supersession in lineage; this linter enforces that working-tree
prose cites the superseded value as historical rather than asserting it
fresh.

Each seal lists:
  - id              short slug for messages
  - pattern         regex of the retracted literal
  - context_markers words whose presence within +/-CONTEXT_LINES marks
                    a match as a historical citation (allowed)
  - description     why the value was retracted, what supersedes it

A pattern hit with no marker in its window is flagged. Run:

  python3 scripts/drift/lint_negation_seals.py

Exit 0 = clean; 1 = at least one unmarked occurrence. Not yet wired into
run_all.py - keep standalone until the seal list is stable.
"""

import argparse
import re
import sys
from pathlib import Path


NEGATION_SEALS = [
    {
        "id": "cadence_0_0365_naked",
        "pattern": re.compile(r"\b0\.0365\b"),
        "context_markers": (
            # Explicit supersession / historical-citation cues.
            "supersed", "earlier", "previously", "former", "deprecated",
            "historical", "old", "obsolete",
            # Frame disclaimers - "n_s-anchored" / "observed n_s rate"
            # are the canonical phrasings that name the retracted frame.
            "n_s-anchored", "n_s anchored", "anchored",
            "observed n_s rate", "n_s rate",
            # Substrate-forced citations.
            "pr #178", "pr #179", "2/57",
            # The fitted-corrections linter uses "target" similarly:
            # "Target tilt: -0.0365" is an explicit comparison, not a
            # fresh assertion.
            "target",
        ),
        "description": (
            "Retracted cadence value 0.0365 (n_s-anchored rate). "
            "Substrate-forced cadence is 2/57 = 0.0351 per PRs "
            "#178/#179; see minimum_alphabet.md sec.3. Cite the old "
            "value as historical (with 'superseded' / 'n_s-anchored' "
            "/ 'earlier' nearby) or replace it with 2/57."
        ),
    },
]

CONTEXT_LINES = 8

WATCHED_EXTS = (".md", ".py")
WATCHED_DIRS = (
    "sync_cost", "docs", "scripts", "README.md", "RESULTS.md", "MANIFEST.yml",
)

# Skip:
#   .ket/cas/  - raw sealed blobs (would flag history at face value)
#   scratch/   - exploratory dead ends
#   data/      - external fixtures
SKIP_PATH_PARTS = ("/.ket/", "/scratch/", "/data/")


def _has_marker_nearby(lines: list[str], idx: int, markers: tuple) -> bool:
    lo = max(0, idx - CONTEXT_LINES)
    hi = min(len(lines), idx + CONTEXT_LINES + 1)
    window = "\n".join(lines[lo:hi]).lower()
    return any(m in window for m in markers)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="repo root")
    parser.add_argument(
        "--verbose", action="store_true",
        help="print each seal's marker hits as well as misses",
    )
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

    flagged: list[tuple[Path, int, str, str]] = []
    marked: list[tuple[Path, int, str]] = []
    for path in sorted(set(candidates)):
        str_path = str(path)
        if any(skip in str_path for skip in SKIP_PATH_PARTS):
            continue
        try:
            text = path.read_text(errors="ignore")
        except Exception:
            continue
        lines = text.splitlines()
        for i, line in enumerate(lines):
            for seal in NEGATION_SEALS:
                if seal["pattern"].search(line):
                    rel = path.relative_to(root)
                    if _has_marker_nearby(lines, i, seal["context_markers"]):
                        marked.append((rel, i + 1, seal["id"]))
                    else:
                        flagged.append((rel, i + 1, seal["id"], line.strip()))

    if args.verbose and marked:
        print(f"Cited (allowed) occurrences: {len(marked)}")
        for rel, i, sid in marked:
            print(f"  {rel}:{i}  [{sid}]")
        print()

    if flagged:
        print(f"Unmarked negation-seal violations: {len(flagged)}")
        for rel, i, sid, snippet in flagged:
            print(f"  {rel}:{i}  [{sid}]  {snippet}")
        print()
        for seal in NEGATION_SEALS:
            print(f"  [{seal['id']}] {seal['description']}")
        print()
        print("Either cite the retracted value as historical (include one")
        print("of the seal's context_markers nearby) or replace it.")
        return 1

    print(
        f"OK: scanned {len(candidates)} files; "
        f"{len(NEGATION_SEALS)} negation seal(s); "
        f"{len(marked)} cited occurrence(s); 0 violations"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
