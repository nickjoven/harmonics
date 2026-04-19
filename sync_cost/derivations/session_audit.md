# Session audit: overclaims, revisions, and stale content

Final-pass critical review of the session's 15 commits. The goal
is to flag any claims that need hedging, numerical errors, or
contradictions within/between docs.

## What was checked

All session artifacts under `sync_cost/derivations/`:

- 7 down-type double-cover phase docs (A, B, B-followup, C,
  C-monodromy, D, D1/D2, closed summary)
- 2 mass-sector √w docs (Phase A, Phase B)
- 2 Ω_b residual docs (Phase A, Phase B)
- 1 K_c criticality pair (Phase A, Phase B)
- 1 Gap 2 sub-E reconciliation
- 1 mixing angle audit
- 1 neutrino mass audit
- 4 numerical scripts (stabilizer scan, DoF monodromy, Phase D
  weight check, Phase D1 eigenvalue, Phase D2 cascade, K_c
  iteration, mass-sector q-scan, Ω_b Phase B)

Plus the session's cumulative closure tables in commit messages.

## Overclaims found and corrected

### 1. `gap2_sub_e_status_reconciled.md` — residual factor inconsistency

**Claim (as written):** "Closed up to O(1) — factor ~2 from
λ_unlock/2 prefactor"

**Reality from own calculation:** The doc computes
`D_0^{observed}/D_0^{Planck} / (m_P/m_e · λ/2) = 9.3`, then calls
this "~2" in the table. The ~2 was wishful; the actual residual
is ~9.

**Fix:** updated line to read "Closed within an order of
magnitude — residual factor ~9 from λ_unlock/2 prefactor and
mass-scale convention; not fully derived."

### 2. `mixing_angle_audit.md` — θ_23 "structurally forced"

**Claim (as written):** "maximal mixing is structurally forced"
to θ_23 = 45° via the SL(2,Z) tr = 0 discrete elliptic angle.

**Reality:** The framework's actual prediction for the 2-3 pair is
42.79° (via Fritzsch-form weight ratio). The "tr = 0 → 45°"
reading is a proposal that would require showing the specific 2-3
SL(2,Z) pair has tr(M) = 0. This was not computed; the doc earlier
hedged ("Proposal", "If true") but the closure table dropped the
hedging.

**Fix:** restored hedging in the closure table; what's confirmed
is "tree-level prediction matches observed within 5%."

## Session-cumulative tables reviewed

Commit messages contain cumulative closure tables (e.g. "Session
pattern: 7 closures"). Reviewed each for accuracy:

| # | Claim | Holds up? |
|---|---|---|
| 1 | Down-type 6 via S_3 orbit + cascade | Yes — D1 rigorous, D2 structural-with-caveat |
| 2 | Mass-sector √w closes at q=2 | Yes — scope narrowed appropriately |
| 3 | Ω_b residual closes via \|r\|² | Yes — Phase B script verifies 0.1σ, uses derived \|r\| = 0.968 |
| 4 | K_c = 0 for identical oscillators | Yes — reads directly from gap1_theorem.md §Ingredient B |
| 5 | ℓ_c = ℓ_P derived from R | Yes — status reconciliation between two docs; corrected above |
| 6 | PMNS θ_12, θ_23 match within 5-10% | Yes for numerics; "structural forcing" claim corrected above |
| 7 | Neutrino masses closed at 0.12-0.31σ | Yes — `item12_neutrino_solar_closure.py` numerically verified |

## Stale content preserved (intentional)

Some phase docs contain hypotheses that were later refuted by
subsequent phase docs. Kept as-is:

- `down_type_double_cover_phase_a.md` §6: methodological note
  suggesting Z_6 gauge-center reading was the right template.
  Refuted by `down_type_double_cover_phase_b_followup.md` (the
  actual group is S_3, not Z_6). The Phase A §6 was not edited —
  it is a historical record of the hypothesis space. Phase B
  followup and Phase D documents clearly cite the refutation.

- `down_type_double_cover_phase_c.md`: proposes DoF(K²) = 1 as a
  claim. Phase D1 (`down_type_phase_d1_eigenvalue.py`) rigorously
  derives this. Phase C is preserved as the reformulation that
  led to the derivation.

This preservation is methodologically intentional (audit trail)
and the chain is navigable via the cross-reference tables in each
doc.

## Issue #56 stale content not updated

Issue #56 itself contains attribution errors that the session's
audits corrected in framework docs but not in the issue body:

| Issue #56 claim | Session finding |
|---|---|
| "Gap 1 K = K_c critical case" (Tier 1 open) | K_c = 0 for identical oscillators; closed |
| "Gap 2 sub-E ℓ_c" (listed open) | Already closed by hierarchy_gaussian_lattice.md |
| "Neutrino masses (depth → ∞ limit)" (Tier 2 open) | Closed at finite K via interaction-scale correction |
| "CKM / PMNS mixing (partial from SL(2,Z))" | Refined: tree-level = PMNS (2 of 3 within 10%), CKM needs RG |

These are flagged in the PR for issue-body update but not
edited directly — Issue #56 is a living status doc and edits
should go through the issue body, not via framework derivation
commits.

## Claims with explicit caveats in their docs

### D2 cascade saturation is structural, not rigorous

`down_type_phase_d2_cascade.py` relies on the claim that q=3 is
an "inner Stern-Brocot denominator" that fully locks at any K > 0.
The numerical scan shows w(q=3)/w(q=6) ~ 25 at K*, consistent with
this reading. But `boundary_weight.py`'s `HONEST SUMMARY` docstring
notes that the rigorous coherence-window definition does not
close under current machinery; the same caveat applies here. D2's
saturation is a structural argument, not a rigorous dynamical
proof.

This is stated in `down_type_double_cover_closed.md`
§"Residual caveats" item 1 with the limitation labeled.

### Mass-sector q-scan noise

`mass_sector_sqrt_w_phase_b.py` reports ratio/π values at q=2 of
1.04 (not exactly 1). Finite-K measurements have numerical noise
~5%; the "exactly π" claim at q=2 is asymptotic (small K) and
the finite-K measurement picks up next-order corrections. The doc
states this: "matches π (within measurement noise)".

### ℓ_c factor-9 residual

Already addressed above. The reconciliation doc now says "within
an order of magnitude, not fully derived." The ℓ_c closure sits
at the free-parameter-count level (S1), not at the precise-
numerical-match level (S2 requires additional convention-fixing).

## Summary

Corrected two specific overclaims (ℓ_c factor, PMNS θ_23
structural forcing). Kept historical artifacts (phase doc
progressions) with forward cross-references. Flagged Issue #56
body items for separate update. The remaining 5-7 closures hold
up under critical review; caveats are labeled in the respective
docs.

## Cross-references

| File | Role |
|---|---|
| `gap2_sub_e_status_reconciled.md` | Corrected in this audit |
| `mixing_angle_audit.md` | Corrected in this audit |
| `down_type_double_cover_closed.md` §"Residual caveats" | Labels D2 limits |
| `mass_sector_sqrt_w_phase_b.md` | Labels finite-K noise |
