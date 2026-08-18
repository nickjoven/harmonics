#!/usr/bin/env python3
"""Owner action: seal the 2026-08-05 continuity audit's stale-arc
successions into the ledger, retire the in-doc banner mechanism, and
verify — one command, idempotent.

Run via `make owner-successions` (the canonical interface). Writes the
seal-enforced successions ledger through the same code path as the MCP
declare_succession tool (validate -> atomic append -> ket put reseal),
so it is an OWNER action: agents were classifier-blocked from running
it directly (2026-08-17), by design.

What it does, in order:
  1. Declares 18 committed SUCCEEDS records (skipping any already in
     the ledger), grouped in the audit's arcs:
       - koide iterations 6/10/11/12/13 -> iteration_14 (the #263
         arc-closing ruling recorded at iteration_5.md:215-219)
       - dark_twin_correction, explicit_4x4_reduction,
         orthogonal_kink_interaction, nonperturbative_phase3
         -> discrete_reduction_computed (S_v arc, :18-21)
       - session_audit, gap1_theorem, gap2_step4_farey_laplacian,
         gap_2_spatial_diffusion, gap_1_christoffel,
         gap1_analytic_proof -> gap2_sub_e_status_reconciled +
         k_critical_phase_b (gap1/gap2 status fork)
       - e_cross_calc -> discrete_reduction_computed,
         spectral_tilt -> spectral_tilt_reframed,
         f2_scoping -> gauge_sector_lovelock +
         discrete_gauge_resolution (migration of the three in-doc
         declared banners; ledger becomes source of record)
  2. Removes the two blockquote banners (e_cross_calc, spectral_tilt),
     leaving one plain-prose truth line each. Runs ONLY after the
     ledger records exist, so the frontier never loses an edge.
     (f2_scoping's succession is narrative Status prose, not a banner;
     it stays.)
  3. Regenerates docs/corpus-index.json and verifies: successions
     validator, enforced coverage, graph seal, and that every declared
     old resolves to the expected frontier heads.

Deliberately NOT declared (from the audit's stale-site list):
  - axial_trajectory_conservation_audit, klein_z2_decomposition_falsifier:
    closed audits with honest verdicts in their own Status; no
    successor doc exists, so succession does not apply.
  - salpeter_gate_disposition:37-39, ansatz_audit_policy:117: line
    sites in live docs — line edits, not whole-doc successions.
  - problem/sin2_theta_w context/gaps files: not derivation docs; the
    ledger validator rejects them. The folder's status.md already
    closes the folder.
"""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "mcp"))

AUDIT = "2026-08-05 continuity audit stale-arc batch (owner-directed 2026-08-17)"

ARCS = [
    (["koide_form_substrate_iteration_6", "koide_form_substrate_iteration_10",
      "koide_form_substrate_iteration_11", "koide_form_substrate_iteration_12",
      "koide_form_substrate_iteration_13"],
     ["koide_form_substrate_iteration_14"],
     "Koide arc 1-13 closed as productive null at iteration 14 (#263 "
     "arc-closing ruling 2026-07-19, recorded at "
     "koide_form_substrate_iteration_5.md:215-219). " + AUDIT),
    (["dark_twin_correction", "explicit_4x4_reduction",
      "orthogonal_kink_interaction", "nonperturbative_phase3"],
     ["discrete_reduction_computed"],
     "S_v arc: discrete_reduction_computed.md:18-21 supersedes every "
     "prior S_v value (16, 13, 0<S_v<16, ~16). " + AUDIT),
    (["session_audit", "gap1_theorem", "gap2_step4_farey_laplacian",
      "gap_2_spatial_diffusion", "gap_1_christoffel", "gap1_analytic_proof"],
     ["gap2_sub_e_status_reconciled", "k_critical_phase_b"],
     "gap1/gap2 status fork reconciled by gap2_sub_e_status_reconciled.md "
     "and k_critical_phase_b.md. " + AUDIT),
    (["e_cross_calc"], ["discrete_reduction_computed"],
     "Migration of the in-doc declared banner to the sealed ledger "
     "(source of record). " + AUDIT),
    (["spectral_tilt"], ["spectral_tilt_reframed"],
     "Migration of the in-doc declared banner to the sealed ledger; the "
     "banner also carried the falsified phi^2 self-similarity claim "
     "(measured: Shenker delta ~ 2.834). " + AUDIT),
    (["f2_scoping"], ["gauge_sector_lovelock", "discrete_gauge_resolution"],
     "Migration of the in-doc declared succession to the sealed ledger "
     "(source of record). " + AUDIT),
]

# (path, exact old text, replacement) — asserts exact match before writing.
BANNER_TRIMS = [
    (ROOT / "sync_cost" / "derivations" / "e_cross_calc.md",
     "> **SUPERSEDED — historical artifact (continuum-route attempt).**\n"
     "> Current value: `discrete_reduction_computed.md` (canonical).\n"
     "> Lineage: `thread_chronology.md`. The body below is left\n"
     "> unedited as the recorded dead end; do not read its numbers as\n"
     "> current.\n",
     "Historical artifact: the continuum-route attempt below is a "
     "recorded dead end (see the successions ledger; current value in "
     "`discrete_reduction_computed.md`, lineage in "
     "`thread_chronology.md`). The body is left unedited — do not read "
     "its numbers as current.\n"),
    (ROOT / "sync_cost" / "derivations" / "spectral_tilt.md",
     "> **Superseded by [spectral_tilt_reframed.md](spectral_tilt_reframed.md).**\n"
     "> The cost function approach below produces the correct tilt but always\n"
     "> gives wrong-sign running (positive instead of negative). A systematic\n"
     "> scan (`cost_function_scan.py`) proved this is a theorem, not a fitting\n"
     "> problem. The reframed derivation replaces the cost function with the\n"
     "> devil's staircase of the circle map, which resolves the running sign\n"
     "> and leads to the φ² self-similarity result.\n",
     "Historical artifact: the cost-function approach below produces the "
     "correct tilt magnitude but wrong-sign running — a theorem, not a "
     "fitting problem (`cost_function_scan.py`). The current derivation "
     "is `spectral_tilt_reframed.md` (see the successions ledger).\n"),
]


def existing_records(ledger: Path) -> set:
    seen = set()
    if not ledger.exists():
        return seen
    for line in ledger.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if rec.get("kind") != "SUCCEEDS" or rec.get("modality") != "committed":
            continue
        new = rec.get("new")
        new = new if isinstance(new, list) else [new]
        seen.add((rec.get("old"), tuple(sorted(new))))
    return seen


def main() -> int:
    import harmonics_mcp as mcp

    ledger = ROOT / "sync_cost" / "successions.jsonl"
    already = existing_records(ledger)
    declared = skipped = failed = 0

    for olds, news, reason in ARCS:
        for old in olds:
            if (old, tuple(sorted(news))) in already:
                print(f"  skip (already in ledger): {old}")
                skipped += 1
                continue
            out = mcp._tool_declare_succession(
                {"old": old, "new": news, "reason": reason})
            if "error" in out:
                print(f"  ERROR {old}: {out['error']}")
                failed += 1
                continue
            sealed = "sealed" if out.get("sealed_cid") else "SEAL FAILED"
            print(f"  declared: {old} -> {news} [{sealed}]")
            for w in out.get("warnings", []):
                print(f"    warning: {w}")
            declared += 1

    print(f"\n{declared} declared, {skipped} already present, {failed} failed")
    if failed:
        return 2

    # Banner trims only once every record is in the ledger.
    for path, old_text, new_text in BANNER_TRIMS:
        text = path.read_text(encoding="utf-8")
        if old_text not in text:
            if new_text.rstrip("\n") in text:
                print(f"  banner already trimmed: {path.name}")
                continue
            print(f"  ERROR: expected banner not found in {path.name}")
            return 2
        path.write_text(text.replace(old_text, new_text), encoding="utf-8")
        print(f"  banner trimmed: {path.name}")

    print("\nregenerating corpus index…")
    r = subprocess.run([sys.executable, "scripts/build_corpus_index.py"],
                       cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout + r.stderr)
        return 2

    print("verifying…")
    rc = 0
    for check in ("check_successions.py", "check_enforced_coverage.py",
                  "check_graph_sealed.py"):
        p = subprocess.run([sys.executable, f"scripts/drift/{check}"],
                           cwd=ROOT, capture_output=True, text=True)
        tail = (p.stdout + p.stderr).strip().splitlines()
        print(f"  {check}: rc={p.returncode}"
              + (f"  {tail[-1]}" if tail else ""))
        rc = max(rc, p.returncode)

    # Frontier assertions: every declared old must resolve away from itself.
    mcp._cache.pop("docs_overlaid", None)
    bad = []
    for olds, news, _ in ARCS:
        for old in olds:
            heads, _chain = mcp._frontier_head(old)
            if old in heads:
                bad.append(f"{old} still a frontier head")
    if bad:
        print("FRONTIER ERRORS:")
        for b in bad:
            print(f"  {b}")
        return 2
    print("  frontier: all declared olds resolve to successors")

    if rc == 0:
        print("\nDONE — remember to commit: successions.jsonl, .ket, the two "
              "trimmed docs, docs/corpus-index.json")
    return rc


if __name__ == "__main__":
    sys.exit(main())
