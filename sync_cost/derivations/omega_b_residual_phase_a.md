# Ω_b = 1/19 residual — Phase A: the three-way boundary-weight inconsistency

## Scope

The cosmic partition `Ω_b : Ω_DM : Ω_Λ = 1/19 : 5/19 : 13/19` is
derived in `baryon_fraction.md` from the Farey partition and Z_6
irreducibility. Against Planck 2018:

    Ω_Λ   =  13/19  =  0.6842     vs.  0.6847 ± 0.0073   0.07 σ
    Ω_DM  =   5/19  =  0.2632     vs.  0.265  ± 0.007    0.7 %
    Ω_b   =   1/19  =  0.0526     vs.  0.0493 ± 0.0003   6.7 %

The 6.7% residual in Ω_b is the largest in the framework's
scorecard. `baryon_fraction.md` §"The 6.7% residual" lists three
candidate correction sources. This Phase A:

1. Tightens the vocabulary (boundary weight vs. partition modes
   vs. decoherence tax).
2. Extends the `boundary_weight.md` partial-locking interpolation
   from `Ω_Λ` to `Ω_b` and `Ω_DM`, producing three observable-
   specific weight values.
3. Shows the three weights are **mutually inconsistent**, which
   converts the residual from "an unexplained miss" to "a
   three-way boundary-weight inconsistency" — a sharper and
   more actionable statement.

## 1. Terminology

| Term | Meaning | Scope |
|---|---|---|
| Farey depth `n` | Integer depth in the Stern-Brocot tree; at n = 5 the tree has `\|F_5\| = 11` fractions, at n = 6 it has 13 | `boundary_weight.md` |
| Farey count `\|F_n\|` | Number of reduced fractions p/q with 1 ≤ q ≤ n | Classical |
| Boundary weight `w` | Partial-locking fraction of the q = 6 modes, `w ∈ [0, 1]`; interpolates between F_5 (w=0) and F_6 (w=1) | `boundary_weight.md` |
| Total budget `n_eff(w)` | Effective partition denominator: `\|F_eff\|(w) + (5 + w) = 16 + 3w` | `boundary_weight.md` |
| Matter mode count | Elements of Z_{q_2 · q_3}, totalling 6 at w=1 | `baryon_fraction.md` |
| Baryonic mode count | Coprime-to-6 matter modes, identified in pairs under the Klein antiperiodic identification: `φ(6)/2 = 1` at w=1 | `baryon_fraction.md` |
| Decoherence tax `1 − \|r\|` | Reduction factor from the Kuramoto order parameter at observation scale | `baryon_fraction.md` |
| Klein identification | Antiperiodic pairing `k ~ (q_2 q_3 − k) mod 6`; identifies {1, 5} as one mode | `klein_bottle_derivation.md` |

## 2. Partition formulas under boundary-weight interpolation

The `boundary_weight.md` construction extends to the matter
sub-partition. At fractional depth `w`:

- `|F_eff|(w) = 11 + 2w` (dark energy modes, locked Farey).
- `n_eff(w) = |F_eff| + matter = 16 + 3w`.
- Matter modes (non-locked): `5 + w`.
  - Inner modes {0, 2, 3, 4} (always locked, w-independent): **4 modes**.
  - Boundary coprime modes {1, 5} (partial-locked at weight w):
    **2w modes** (two at w=1, zero at w=0).
  - Inner reducible mode {3} that gets promoted out of pure inner
    status at w: this is the subtle point — the interpolation
    treats one inner mode as joining the boundary class, giving
    the total `4 + 2w - w = 5 + w` I compute below.

Accepting the `boundary_weight.md` total `5 + w` matter modes
and the baryonic identification of coprime-to-6 modes under Klein
pairing, the partition formulas become:

    Ω_Λ(w)   =  (11 + 2w) / (16 + 3w)        [baryon_weight.md]
    Ω_DM(w)  =   5        / (16 + 3w)         [inner 5 modes always locked]
    Ω_b(w)   =   w        / (16 + 3w)         [boundary coprime pair / 2 via Klein]
    sum      =  (16 + 3w) / (16 + 3w) = 1     ✓

**Verification at endpoints:**

- w = 0: Ω_Λ = 11/16, Ω_DM = 5/16, Ω_b = 0/16 = 0. No baryons
  at F_5 depth (the boundary modes haven't locked yet).
- w = 1: Ω_Λ = 13/19, Ω_DM = 5/19, Ω_b = 1/19. The framework's
  integer-depth prediction.

The w-dependence of `Ω_b` is approximately **linear in w near w = 1**:
`dΩ_b/dw ≈ 1/19 = 0.0526`. So a 5% change in w produces a 5%
change in Ω_b — comparable to the residual.

## 3. The three-way inconsistency

Invert each observed fraction against its weight formula:

    Ω_Λ  =  0.6847     →   w_Λ  =  (11 − 16·0.6847) / (3·0.6847 − 2)  =  0.828
    Ω_DM =  0.265      →   w_DM =  (5 − 0.265·16) / (3·0.265)           =  0.957
    Ω_b  =  0.0493     →   w_b  =  0.0493·16 / (1 − 3·0.0493)            =  0.926

(Signs and arithmetic are straightforward algebraic inversions
of the formulas in §2.)

Result:

    w from Ω_Λ   =  0.828
    w from Ω_b   =  0.926
    w from Ω_DM  =  0.957

**Three different values** of the same "boundary weight" are
implied by the three observables. Under a common-mode partial
locking, they must be equal. They are not.

The spread:

    max(w_i) − min(w_i)  =  0.957 − 0.828  =  0.129

is large — about 13% of the weight's dynamic range. This is
the structural shape of the 6.7% Ω_b residual.

## 4. What the inconsistency tells us

### The residual is not isolated

Before this Phase A: the Ω_b 6.7% miss was an isolated miss.
After: it is part of a three-way inconsistency with Ω_Λ (at
0.07σ) and Ω_DM (at 0.7%). The three observables predict three
different boundary weights.

### The residual has structural information

The pattern `w_Λ < w_b < w_DM` is interpretable:
- Ω_Λ prefers LESS partial locking.
- Ω_DM prefers MORE partial locking.
- Ω_b sits between.

If the true mechanism is a single w, then two of the three
observables must carry corrections. The natural candidates
(from `baryon_fraction.md` §"The 6.7% residual"):

### Candidate corrections (Phase B to test)

**C1 — Decoherence tax.**

The Kuramoto order parameter `|r|` at the observation scale is
< 1, introducing a multiplicative reduction. Applied uniformly
to all three fractions, `|r|` cancels from ratios and doesn't
resolve the inconsistency. Applied **only to the baryonic modes**
(the cross-sector coupled ones), it reduces Ω_b by `(1 − |r|) ≈
3.2%` — gets part of the way but not the full 6.7%.

**C2 — Klein identification asymmetry.**

The identification {1} ~ {5} under Klein pairing assumes the two
modes have equal tongue widths. At finite K the antiperiodic
twist introduces an asymmetry: the two modes have slightly
different `w_F`, so the pairing is not exact. This would
modify Ω_b without touching Ω_Λ or Ω_DM — a selective correction.

**C3 — Secondary sub-partition at fractional depth.**

The baryonic mode count is `φ(6)/2 = 1` at w = 1 because there
are 2 coprime modes identified in pairs. At fractional w, the
coprime-mode count is `2w`, but the Klein identification may
itself be w-dependent: perhaps at fractional depth, the pair
{1, 5} is not fully identified, and the effective baryonic count
is `f(w) · 2w / 2` with some `f(w)` that accounts for incomplete
identification.

If `f(w) = w` (the two boundary modes are both partially locked
AND partially identified), then Ω_b(w) = 2w²/2 = w². At
w = 0.828 (the Ω_Λ-consistent value), Ω_b = 0.686² × factor —
doesn't work dimensionally.

More careful: Ω_b(w) = (2w · f(w)) / (2 · n_eff(w)) = w · f(w)/n_eff(w).
At f(w) = w: Ω_b = w² / (16 + 3w). At w = 0.828: 0.686/18.49 = 0.0371. Too low.

This candidate needs more care in Phase B.

**C4 — Partition-denominator correction.**

The `n_eff(w) = 16 + 3w` counts "depth + |F_eff|". Maybe the
correct denominator at partial depth also includes a w-dependent
term from the coprime-mode non-identification, changing `16 + 3w`
to `16 + 3w + δ(w)`. This rescales all three fractions and can
be tuned to fit.

**C5 — Kinematic z-dependence.**

`Ω_b`, `Ω_DM`, `Ω_Λ` are measured at different cosmological
scales (CMB, galaxy clusters, supernovae). The framework's
`a_0(z) = c H(z)/(2π)` (`baryon_fraction.md` §5) predicts a
z-dependent MOND scale. If the three observables sample
different z, the implied w could genuinely differ — not an
inconsistency but a consistent w(z).

## 5. Candidate ranking (Phase B priority order)

Using the session's prior-pivot methodology:

1. **C5 (z-dependent w) — most leverage, most promising.**
   Precedent: `a_0(z)` already predicted in the framework.
   The three observables at different z naturally give
   different `w`. Phase B should compute `z_eff` for each and
   test whether `w(z)` is monotone.

2. **C2 (Klein asymmetry) — structural, tractable.**
   Precedent: the down-type derivation just closed used the
   Klein flip's action on the 6-point lattice. The asymmetry
   in the {1, 5} pairing at finite K is the same object,
   measured at the matter sub-partition.

3. **C4 (partition-denominator correction) — second-tier.**
   If C5 and C2 don't fully close, a systematic correction to
   `n_eff` could soak up the residual. Less structural but
   perhaps needed.

4. **C1 (decoherence tax) — partial.**
   Gets ~half the residual. Not sufficient alone; could combine
   with C2 or C5.

5. **C3 (sub-partition) — weakest.**
   Structurally plausible but numerically doesn't work out
   at first pass.

## 6. Methodological notes from prior pivots

Patterns from the just-closed Type Cs that apply here:

- **Down-type Phase D (self-consistent weight at saturation).**
  The reading `w_3 → 1` used `boundary_weight.md`'s template at
  an endpoint. Here we are at an **interior** w — closer to the
  Ω_Λ case. The template's interior-fixed-point version
  (Section 6 of `boundary_weight.py`'s `HONEST SUMMARY`
  docstring) applies.

- **Mass-sector Phase B (q-specific closure).**
  A universal claim was found to hold only at the structurally-
  relevant q. Analogously, a "universal w" may hold only at one
  observable's scale; the residual at other observables needs
  scale-specific corrections (C5).

- **Vocabulary discipline.**
  The down-type program split "Klein parity" (denominator) from
  "topological parity" (numerator) and found they were being
  conflated. Here the analogous split: the "boundary weight" may
  actually refer to different sub-concepts (cosmological-scale w
  vs. tongue-amplitude w vs. partition-depth w) that were being
  identified.

## 7. What Phase A establishes, and does not

**Establishes:**

- Explicit partition formulas `Ω_Λ(w), Ω_DM(w), Ω_b(w)` with
  endpoints matching the framework's integer-depth predictions.
- Inversion of each observed fraction gives three different
  implied `w` values: 0.828, 0.926, 0.957.
- The 6.7% Ω_b residual is part of a three-way boundary-weight
  inconsistency, not an isolated miss.
- Five candidate correction mechanisms, ranked by prior-pivot
  plausibility.

**Does not establish:**

- Which candidate dominates.
- Whether the inconsistency resolves under C5 (z-dependence) or
  C2 (Klein asymmetry) or a combination.
- A concrete numerical value for the dominant correction.

Phase B will test C5 and C2 numerically against the three
observables.

## 8. Cross-references

| File | Role |
|---|---|
| `baryon_fraction.md` | Source derivation of 13:5:1 partition, lists candidate corrections |
| `boundary_weight.md` | Partial-locking weight `w`, interpolation formula |
| `boundary_weight.py` | Algebraic inversion precedent, `HONEST SUMMARY` docstring caveat |
| `one_five_thirteen_readings.py` | Multiple independent readings of 1:5:13 |
| `framework_constants.py` | K*, |r|, numerical constants |
| `a0_high_z.py`, `a0_observable.py` | Candidate source of `a_0(z)` evolution (C5) |
| `down_type_double_cover_closed.md` | Klein-flip machinery applicable to C2 |
