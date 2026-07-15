#!/usr/bin/env python3
"""
Check: docs/corpus-index.json freshness (advisory).

Thin wrapper so run_all.py can invoke the generator's --check mode from
this directory. The index is a committed projection of the corpus
(scripts/build_corpus_index.py); like the derivation graph it is
CI-regenerated, so staleness on a working tree is a benign, mechanically
healing state — reported for visibility, never gating.

Exit code: 0 fresh, 1 stale/missing (advisory in run_all.py).
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

if __name__ == "__main__":
    sys.exit(subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_corpus_index.py"),
         "--check", "--root", str(ROOT)],
    ).returncode)
