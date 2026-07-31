#!/usr/bin/env python3
"""
Check: junk-signature review queue over the claims projection (advisory).

The junk claims the 2026-07 audit cycle retired had a distributional
fingerprint before anyone read a single source line: singleton
corroboration, den-1 witnesses (years, counts, partition shares), or
decimal-artifact denominators (2^a·5^b — a rendered float sealed as an
exact rational). Legitimate claims corroborate broadly (13/19 at 25
docs) or carry structural denominators (13/264, 35/132). This check
mechanizes that fingerprint: it lists every claim matching the junk
signature so review attention lands where junk concentrates.

ADVISORY, and likely permanently so: the signature has KNOWN false
positives (w_+ = 0.9298 is a genuine empirical fit rendered decimal;
w_- = 1/1 is a genuine structural claim), so this is a ranked review
queue, never a verdict. Per the gate ladder, a predicate with
structural false positives never earns blocking authority — its job
is to schedule reads, not refuse commits.

Exit code: number of signature-flagged claims (advisory in run_all.py).
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CLAIMS = ROOT / "docs" / "claims-index.json"


def decimal_artifact(den: int) -> bool:
    """True when den is 2^a·5^b with den >= 100 — the shape a rendered
    float takes after exact rationalization (0.9298 -> 4649/5000)."""
    if den < 100:
        return False
    for p in (2, 5):
        while den % p == 0:
            den //= p
    return den == 1


def flagged_claims(claims: dict) -> list:
    out = []
    for cid, c in claims.items():
        if c.get("corroboration", 0) != 1:
            continue
        witness = c.get("witness", "")
        try:
            _, den = witness.split("/")
            den = int(den)
        except ValueError:
            continue
        if den == 1 or decimal_artifact(den):
            shape = "den-1" if den == 1 else "decimal-artifact"
            out.append((c.get("subject"), witness, shape, cid[:12]))
    return sorted(out)


def main() -> int:
    if not CLAIMS.exists():
        print(f"no claims index at {CLAIMS}")
        return 0
    claims = json.loads(CLAIMS.read_text()).get("claims", {})
    hits = flagged_claims(claims)
    if not hits:
        print(f"OK: no singleton claims match the junk signature "
              f"({len(claims)} claims scanned)")
        return 0
    print(f"NOTE: {len(hits)} singleton claim(s) match the junk signature "
          f"(advisory review queue — known false positives, see docstring):")
    for subject, witness, shape, cid in hits:
        print(f"  {subject} = {witness}  [{shape}]  {cid}")
    return 1  # count lives in stdout; exit status truncates mod 256


if __name__ == "__main__":
    sys.exit(main())
