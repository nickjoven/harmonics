#!/usr/bin/env python3
"""
Check: docs/claims-index.json freshness (advisory).

Thin wrapper so run_all.py can invoke the generator's --check mode from
this directory — the same pattern as check_corpus_index.py. The claims
index is a committed projection of the ingest report
(scripts/build_claims_index.py); regen-claims.yml owns it in CI, so
staleness on a working tree is a benign, mechanically healing state —
reported for visibility, never gating. What this catches: the report
and the projection moving independently (a hand edit, a partial
commit), which is the two-records-nobody-joins failure shape one layer
down from the corpus itself.

Exit code: 0 fresh, 1 stale/missing (advisory in run_all.py).
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

if __name__ == "__main__":
    sys.exit(subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_claims_index.py"),
         "--check"],
    ).returncode)
