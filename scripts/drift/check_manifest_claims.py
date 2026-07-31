#!/usr/bin/env python3
"""
Check: MANIFEST scorecard values vs the claims projection (advisory).

MANIFEST.yml records what the framework claims; docs/claims-index.json
records what the corpus's prose actually asserts, with frontier state.
Nothing previously joined them — the coupling_scales failure shape (two
correct records, no scheduled read across them) one layer up: a
scorecard row could quietly diverge from what any frontier doc says,
and only a human sweep would notice.

For each mapped row, every rational the row commits to (leading "N/M"
in `computed` and `computed_single_w`) must exist in the claims
projection under the row's subject with frontier corroboration >= 1.
The mapping is an explicit table — only rows whose subject the ingest
lexicon knows are joinable; the rest of the scorecard stays under
check_manifest.py's structural checks.

ADVISORY while its false-positive rate accumulates (the ladder's
apprenticeship): a legitimate MANIFEST edit ahead of a corpus re-ingest
would flag here for one bot-cycle. Promote to FATAL after four weeks
of clean runs with no such transient (criterion set 2026-07-29).

Exit code: number of divergent row values (advisory in run_all.py).
"""

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]

# manifest row key -> (claims subject, fields carrying committed values)
MAPPED = {
    "dark_energy": ("omega_lambda", ["computed"]),
    "dark_energy_fraction_two_component":
        ("omega_lambda", ["computed", "computed_single_w"]),
    "dark_matter_fraction": ("omega_dm", ["computed", "computed_single_w"]),
    "baryon_fraction": ("omega_b", ["computed", "computed_single_w"]),
}

LEADING_RATIONAL = re.compile(r"^\s*(\d+)\s*/\s*(\d+)\b")


def find_rows(node, out):
    """Collect MAPPED rows wherever they nest in the MANIFEST tree."""
    if isinstance(node, dict):
        for key, val in node.items():
            if key in MAPPED and isinstance(val, dict):
                out[key] = val
            else:
                find_rows(val, out)


def main() -> int:
    manifest = yaml.safe_load((ROOT / "MANIFEST.yml").read_text())
    claims = json.loads(
        (ROOT / "docs" / "claims-index.json").read_text()).get("claims", {})

    # (subject, witness) -> frontier corroboration
    frontier = {(c.get("subject"), c.get("witness")):
                c.get("corroboration_frontier", 0) for c in claims.values()}

    rows = {}
    find_rows(manifest, rows)
    divergent = []
    for key, (subject, fields) in MAPPED.items():
        row = rows.get(key)
        if row is None:
            divergent.append((key, "-", "row missing from MANIFEST.yml"))
            continue
        for field in fields:
            text = str(row.get(field, ""))
            m = LEADING_RATIONAL.match(text)
            if not m:
                continue  # a non-rational value is not this check's business
            num, den = int(m.group(1)), int(m.group(2))
            # reduce, mirroring the ingest witness form
            a, b = num, den
            while b:
                a, b = b, a % b
            witness = f"{num // a}/{den // a}"
            if frontier.get((subject, witness), 0) < 1:
                divergent.append(
                    (key, field,
                     f"{subject} = {witness} has no frontier corroboration "
                     f"in the claims projection"))

    if divergent:
        print(f"NOTE: {len(divergent)} MANIFEST value(s) diverge from the "
              f"claims projection (advisory — see docstring):")
        for key, field, why in divergent:
            print(f"  {key}.{field}: {why}")
        return 1  # never a count: exit status truncates mod 256
    checked = sum(len(f) for _, f in MAPPED.values())
    print(f"OK: {len(MAPPED)} scorecard rows ({checked} fields) "
          f"frontier-corroborated in the claims projection")
    return 0


if __name__ == "__main__":
    sys.exit(main())
