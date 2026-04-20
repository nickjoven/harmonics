# A_s Phase 0 + 1: 19/21 derivation attempt (SUPERSEDED)

> **SUPERSEDED.** This document attempted a numerological fit
> (1 − q₂/F₈ = 19/21) against the 11% Phase 0 residual. The fit
> was decomposed into three sub-claims (H.a, H.b, H.c); H.a was
> weakened by direct enumeration. The doc is preserved as a
> historical record.
>
> The canonical statement of A_s in the framework is now
> `a_s_geometric_proof.md`, which works only from established
> structural axioms (A1–A9) and reports the 11% discrepancy as a
> single open quantity, without partitioning it into ad-hoc
> corrections.
>
> Read this doc only if interested in why the 19/21 numerological
> match did **not** survive structural scrutiny.

---

Continuation of `a_s_phase0.md` §7 suggestive match. Attempt a
structural derivation of the factor **1 − q₂/F₈ = 19/21 ≈ 0.9048**
that would close A_s to within 0.3% of observation.

**Result.** Decomposition, not closure. The algebraic identity is
clean; the structural argument plausible; the derivation rests on
one unproven claim about sector-mode counting at the pivot bracket.

## 1. The identity

    19/21 = (F₈ − q₂)/F₈ = 1 − q₂/F₈                             (1.1)

with q₂ = 2 (Klein binary integer), F₈ = 21 (Fibonacci, the local
pivot denominator per `k_omega_mapping.py` n=5 reading of the
13/21 convergent).

Numerical match to the Phase 0 residual:

    A_s_obs / A_s_pred(Phase 0) = 0.9020                        (1.2)
    1 − q₂/F₈                   = 0.9048                        (1.3)

Relative deviation: 0.3%. Under Planck 2018 1σ uncertainty on A_s
(± 1.4%), this is well within observational error.

## 2. The candidate structural claim

**Hypothesis H.** The scalar curvature perturbation R couples to
modes in the **scalar-gravitational sector only**, not to modes
carrying q₂-winding (spinor / weak sector). At the pivot bracket
(containing 13/21), the fraction of modes in the q₂ sector is
q₂/F₈ = 2/21. The available variance reduction for R is then
1 − 2/21 = 19/21.

Under H, the corrected A_s prediction is:

    A_s_corrected = (19/21) × A_s_phase0
                  = (19/21) × (1 − φ⁻⁴)/(4 λ_unlock × φ × F₂₁²)
                  ≈ 2.10 × 10⁻⁹                                  (2.1)

matching A_s_obs = 2.10 × 10⁻⁹ to **0.3% relative / ~0.2σ under
Planck**.

## 3. What the derivation needs

H is **not proven** — it rests on three sub-claims:

### 3.1 (H.a) Pivot bracket mode count

**Claim**: the pivot bracket carries F₈ = 21 effective modes.

**Status**: the bracket near 1/φ at Fibonacci level 7 contains
infinitely many rationals (all sub-level continued-fraction
approximants). F₈ is specifically the **denominator of the
convergent** 13/21, not a mode count.

**Direct enumeration of the SB bracket [8/13, 5/8] (containing
13/21) by denominator bound**:

| max denom | # irreducibles in bracket |
|---|---|
| q ≤ 21 | 1 (just 13/21) |
| q ≤ 34 | 3 |
| q ≤ 55 | 9 |
| q ≤ 89 | 23 |
| q ≤ 144 | 61 |
| q ≤ 233 | 159 |

**None of these is F₈ = 21.** The count grows roughly linearly
with q_max, not matching any Fibonacci or Farey integer. The "21
modes" interpretation of F₈ as a mode count in the bracket is not
supported by naive enumeration.

**What's needed**: either (a) a different definition of "mode"
under which exactly F₈ = 21 modes sit in the bracket, or (b) an
argument that the 19/21 factor does NOT arise from a literal mode
count but from some other structural fraction.

**H.a remains open, and enumeration weakens the claim.**

### 3.2 (H.b) Sector decomposition at the pivot

**Claim**: exactly q₂ = 2 modes of the F₈ total are in the q₂-
sector.

**Status**: the framework partitions observables by q₂/q₃
(`duty_cycle_dictionary.md`, `discrete_gauge_resolution.md`), but
the mode-by-mode sector assignment at a specific SB bracket is not
explicit in any doc.

**What's needed**: a derivation that at the pivot bracket, exactly
q₂ = 2 of the F₈ = 21 modes carry the spinor-sector index. Plausible
candidate: the bracket contains one mediant pair at the q₂-denominator
boundary, and that pair has multiplicity 2 (the two signs of a Z₂
winding). But this is heuristic.

**H.b remains open.**

### 3.3 (H.c) Scalar-R decoupling from q₂-modes

**Claim**: scalar curvature perturbation R is insensitive to
modes in the spinor sector.

**Status**: this is a standard claim in QFT — spinor fluctuations
contribute to tensor modes (gravitational waves) and to fermion-
loop corrections, but not directly to scalar R at tree level.

**In the framework**: the ADM dictionary (`continuum_limits.md`
Part I) identifies R with the Kuramoto phase δθ. If the q₂-sector
phase δθ_{q₂} is a distinct field (carrying antiperiodic boundary
conditions on the Klein bottle per `fermion_spinors_from_z2.py`),
then it does not contribute to the scalar R.

**H.c is plausible and arguably closable** via the Klein bottle's
Z₂ torsion separating boson and fermion sectors. This is the
strongest of the three sub-claims.

## 4. Numerical probe: alternative H variants

If H is instead stated with different integers, the residual
match degrades:

| variant | integer interpretation | value | % off 0.902 |
|---|---|---|---|
| 1 − q₂/F₈ | q₂=2, F₈=21 | 0.9048 | 0.30% |
| 1 − q₂/\|F_7\| | q₂=2, \|F_7\|=19 | 0.8947 | 0.82% |
| 1 − 1/F₈ | single-mode loss | 0.9524 | 5.59% |
| 1 − q₃/F₈ | q₃=3 instead of q₂ | 0.8571 | 4.98% |
| 1 − q₂/F₉ | F₉=34 (wrong pivot) | 0.9412 | 4.35% |
| 1 − q₂/|F_6| | \|F_6\|=13 | 0.8462 | 6.20% |

**Only 1 − q₂/F₈ lands within Planck 1σ.** The specific
q₂-over-F₈ identification is uniquely picked out.

## 5. What this derivation gives and does not give

**Gives**:
- A structurally-flavored candidate form (1 − q₂/F₈) that matches
  A_s_obs at 0.3% / ~0.2σ.
- Three sub-claims (H.a, H.b, H.c), each separable and addressable
  in its own right.
- Numerical isolation of this form from nearby alternatives.
- H.c is close to derivable from existing Klein-bottle Z₂ torsion
  arguments.

**Does not give**:
- A derivation of H.a (why F₈ specifically, not |F_7| or 2^7).
- A derivation of H.b (why q₂ of the F₈ modes are in the spinor
  sector, not some other count).
- A σ-closed A_s. The 0.3% match is numerology until H.a, H.b
  are derived.

## 6. Honest status

**A_s closure with Hypothesis H**:
- If H is true → A_s closed at 0.3% / ~0.2σ (σ-closed under
  `statistical_conventions.md`'s C-numerical definition).
- If H is false → residual remains at 11% (%-only, as Phase 0
  stated).

**Current status of H**: not derived, and weakened by §3.1
enumeration. The 0.3% numerical match remains tantalizing but
currently reads as **coincidence**: the bracket [8/13, 5/8]
does not naturally support "F₈ = 21 modes" under direct
enumeration.

**H.c alone is close to derivable** from existing Klein-bottle
Z₂ machinery (spinor vs boson separation). But H.c on its own
only gives "some fraction of modes drop out", not the specific
1 − q₂/F₈ form. The sharpness of the numerical match points to
a structural argument the framework doesn't currently possess.

**Promotion status**: A_s **stays at 11% / %-only** pending a
derivation that survives §3.1's enumeration challenge. The
19/21 match is documented as a suggestive lead but cannot
currently be promoted to a derivation.

## 7. The next focused sub-question

**Sub-question Q_H.a**: At the Stern-Brocot bracket containing the
convergent F_n/F_{n+1}, what is the natural "effective mode count"?
Candidates: F_{n+1}, |F_n| (Farey), |F_{n+1}|, 2^{depth}, or
something else. Each has a different prediction for the A_s
correction.

A focused derivation attempting Q_H.a could:

1. Define "effective mode" precisely (e.g., "rationals p/q in the
   bracket satisfying some coupling constraint").
2. Enumerate them for n = 7 explicitly.
3. Check which count matches F_{n+1} = 21.

This is one session of work. If Q_H.a gives F_{n+1}, the full H
chain (H.a → H.b → H.c) is likely derivable.

## 8. Cross-references

| File | Role |
|---|---|
| `a_s_phase0.md` | Phase 0 derivation; 11% residual |
| `a_s_phase0_lambda_audit.py` | Confirms λ not the source; suggests 19/21 |
| `k_omega_mapping.py` | n=5 reading: pivot convergent 13/21 |
| `fermion_spinors_from_z2.py` | Basis for H.c (spinor sector separation) |
| `duty_cycle_dictionary.md` | q₂/q₃ sector partition framework |
| `boundary_weight.py` | SB bracket machinery |
