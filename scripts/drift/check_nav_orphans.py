#!/usr/bin/env python3
"""
Check: docs-site nav orphans (advisory).

Thin wrapper so run_all.py can invoke scripts/site_nav_audit.py from
this directory. Flags pages with zero inbound links that are not in the
audit's DELIBERATE_ORPHANS allowlist — the "landed a page, forgot to
link it" slip. Advisory: an unlinked page is a coverage gap, not an
integrity violation.

Exit code: number of unexpected orphans (0 = tree, modulo allowlist).
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

if __name__ == "__main__":
    sys.exit(subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "site_nav_audit.py")],
    ).returncode)
