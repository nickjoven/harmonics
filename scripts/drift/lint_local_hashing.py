#!/usr/bin/env python3
"""
Tool #3: Lint for local hashing that could drift from BLAKE3.

Scans scripts/, seed/, and .ket/ for direct use of hashlib.sha256
(or md5, sha1, sha512). These are fine in most contexts — but if
they're being used to compute CAS CIDs, that's the drift bug that
corrupted entries on 2026-04-22.

The rule: any hashing that produces a string of the form
`[0-9a-f]{64}` and is used as a CAS filename must go through BLAKE3.
This linter is deliberately blunt: it flags all hashlib usage in
the watched directories and expects an allowlist for legitimate
uses (currently empty).

Run:
  python3 scripts/drift/lint_local_hashing.py
"""

import argparse
import re
import sys
from pathlib import Path

# Paths under the repo root that we care about. Each is resolved
# relative to --root.
WATCHED_DIRS = ("scripts", "seed", ".ket")

# Suspect patterns are only flagged if they look like CODE — the
# function-call forms `hashlib.sha256(...)` and import statements.
# Docstring mentions don't count.
SUSPECT_PATTERNS = (
    re.compile(r"\bhashlib\.(sha256|sha1|md5|sha512|sha224|sha384)\s*\("),
    re.compile(r"^\s*import\s+hashlib\b", re.MULTILINE),
    re.compile(r"^\s*from\s+hashlib\s+import\b", re.MULTILINE),
)

# Allowlist: (path_substring, reason). If a matching line contains
# path_substring in its file path, the finding is suppressed.
ALLOWLIST: list[tuple[str, str]] = [
    ("scripts/drift/lint_local_hashing.py", "the linter itself documents the patterns it watches for"),
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="repo root")
    args = parser.parse_args()
    root = Path(args.root).resolve()

    findings: list[tuple[Path, int, str]] = []
    for d in WATCHED_DIRS:
        for path in (root / d).rglob("*"):
            if not path.is_file():
                continue
            if path.suffix not in (".py", ".rs"):
                continue
            try:
                text = path.read_text(errors="ignore")
            except Exception:
                continue
            for i, line in enumerate(text.splitlines(), 1):
                if any(p.search(line) for p in SUSPECT_PATTERNS):
                    rel = path.relative_to(root)
                    allowed = any(sub in str(rel) for sub, _ in ALLOWLIST)
                    if not allowed:
                        findings.append((rel, i, line.strip()))

    if findings:
        print(f"Suspect local hashing: {len(findings)} line(s)")
        for rel, i, snippet in findings:
            print(f"  {rel}:{i}  {snippet}")
        print()
        print("If these are legitimate (non-CID) uses, add them to ALLOWLIST")
        print("in scripts/drift/lint_local_hashing.py with a reason string.")
        return 1

    print(f"OK: no suspect hashlib usage under {list(WATCHED_DIRS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
