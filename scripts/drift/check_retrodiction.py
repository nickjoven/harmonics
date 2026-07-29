#!/usr/bin/env python3
"""
Check: retrodiction shadow gate (FATAL).

Replays the 2026-04-22 bare-K1 demotion and the koide arc-close against
the current projections and scores the machinery's committed-layer
divergence signal against the #263 ruling pass's manual findings
(scripts/experiments/fixtures_263.json). The harness proved 4/4 with
zero extras when built (harmonics#314); this check pins that as a
regression invariant — a change to the graph builder, the succession
rules, or the kind table that silently degrades retrodiction now fails
here, in CI, instead of being discovered at the next audit.

Deterministic over committed projections + frozen fixtures, so it
qualifies for the FATAL tier immediately: the predicate is crisp and
its error model is the fixture set itself.

Exit code: 0 = found all expected findings with no extras; nonzero =
missed or extra findings (count), or a load failure.
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXPERIMENTS = ROOT / "scripts" / "experiments"

if __name__ == "__main__":
    sys.exit(subprocess.run(
        [sys.executable, str(EXPERIMENTS / "retrodict.py"),
         "--fixtures", str(EXPERIMENTS / "fixtures_263.json"),
         "--gate"],
    ).returncode)
