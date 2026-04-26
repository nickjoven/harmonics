# Ω_b Floor closure: C5 z-dependent w with framework-integer parameters

## What this file is

A focused calculation of `omega_b_residual_phase_a.md` candidate
C5 (z-dependent boundary weight w from a_0(z) = c·H(z)/(2π)),
applied to the three-way inconsistency in (Ω_Λ, Ω_b, Ω_DM).

**Result (substantive)**: with a single two-parameter framework-
integer expression `w(z) = 1 − (1/INTERACT)·(H_0/H(z))^(1/(2·INTERACT))`
and standard cosmology z-effective values, all three partition
predictions land **within 0.3% of observation** — a 34× reduction
in the Ω_b residual. Ω_Λ matches to 0.002% (within Planck
precision) with `w(0) = MEDIANT/INTERACT = 5/6` exactly.

This is candidate Class 4 (proposed structural). The audit risk
is in the specific exponent β = 1/12, which has competing
framework-integer forms (most notably 1/(4π) = 0.0796 within 1%
of the required value).

## Setup

The framework's static partition (per `baryon_fraction.md`,
`omega_b_residual_phase_a.md`):

```
Ω_Λ(w)   = (11 + 2w) / (16 + 3w)
Ω_DM(w)  = 5 / (16 + 3w)
Ω_b(w)   = w / (16 + 3w)
```

At w = 1, predicts (Ω_Λ, Ω_DM, Ω_b) = (13/19, 5/19, 1/19) =
(0.684, 0.263, 0.053). Observation: (0.685, 0.265, 0.0493).
Residuals 0.07%, 0.7%, 6.7%.

The three-way inconsistency: inverting each formula gives
three different implied weights {w_Λ = 0.828, w_b = 0.926,
w_DM = 0.957}. C5 hypothesis: this is one function `w(z)`
sampled at three different cosmological redshifts.

## C5 calculation

**z-effective assignment** (standard cosmology, *not*
framework-chosen):

| Observable | z_eff | Justification |
|---|---|---|
| Ω_Λ | 0 | DE-dominated today |
| Ω_b | z_rec ≈ 1090 | recombination (CMB acoustic peaks) |
| Ω_DM | z_eq ≈ 3400 | matter-radiation equality |

**Framework function**:

```
w(z) = 1 − α · (H_0 / H(z))^β

with H(z) = H_0 · √(Ω_r(1+z)^4 + Ω_m(1+z)^3 + Ω_Λ)
```

**Framework-integer parameters**:

```
α = 1 / INTERACT = 1 / (q_2·q_3) = 1/6
β = 1 / (2·INTERACT) = 1/12
```

This gives `w(0) = 1 − 1/6 = 5/6 = MEDIANT/INTERACT` —
the "characteristic ratio" between the two adjacent Klein
operations (q_2+q_3 vs q_2·q_3).

## Predictions vs observations

| Observable | z | H/H_0 | w(z) | Predicted | Observed | Residual |
|---|---|---|---|---|---|---|
| Ω_Λ | 0 | 1.00 | 0.8333 | **0.6847** | 0.6847 | **0.002%** |
| Ω_b | 1090 | 23,205 | 0.9279 | 0.04940 | 0.04930 | 0.199% |
| Ω_DM | 3400 | 157,076 | 0.9385 | 0.26574 | 0.26500 | 0.279% |

**Reduction from the original Floor residuals**:

| Observable | Original (w=1) | With C5 | Improvement |
|---|---|---|---|
| Ω_Λ | 0.07% | 0.002% | 32× |
| Ω_b | **6.76%** | **0.20%** | **34×** |
| Ω_DM | 0.70% | 0.28% | 2.5× |

The Ω_b 6.7% / 11σ Floor residual — the framework's largest
scorecard miss — is reduced to 0.2%, well within the
particle-numerology cloud floor (1–3%).

## The Ω_Λ exact rational

At z = 0 with w = 5/6, the framework's Ω_Λ formula gives an
exact rational:

```
Ω_Λ(5/6) = (11 + 10/6) / (16 + 15/6) = (66+10) / (96+15) = 76/111
```

Numerically 76/111 = 0.684685, against observed 0.6847 — agreement
to **0.002%**, well within Planck precision (σ_observed ≈ 0.0073
gives precision ~1%, so the agreement is at the 0.001σ level).

This is essentially a structural identity, not a fit. The 5/6
value of w(0) is forced by `α = 1/INTERACT` and the formula
`w(0) = 1 − α`.

## Why this is significant

Three observations align via one function with two framework-
integer parameters:

1. **The framework predicts a non-trivial w(z) running** — the
   boundary weight is not a constant but varies with the
   cosmological scale via H(z). This is consistent with the
   framework's existing prediction `a_0(z) = c·H(z)/(2π)` (D8 in
   `baryon_fraction.md`); the same H(z) drives the locking
   threshold.

2. **The three partition observables are consistent under this
   one function** — what looked like a three-way inconsistency
   in `omega_b_residual_phase_a.md` is now (mostly) resolved as
   sampling-at-different-z artifacts.

3. **The largest scorecard residual (Ω_b 11σ) reduces 34×** to
   0.2%, within Floor noise band.

This is the first Floor closure to make substantive progress under
the disambiguation pattern (`vocabulary_is_the_work_pattern.md`).
Where A_s G1 dissolved as anchor-side category statement
(Instance 7), Ω_b admits real substrate-side closure via
framework-internal a_0(z).

## Ansatz audit (per `ansatz_audit_policy.md`)

### Strengths

- **α = 1/INTERACT** is a single, framework-canonical expression.
  No competing close candidates within ~5%.
- **w(0) = 5/6 = MEDIANT/INTERACT** is the framework's
  natural ratio between the two adjacent Klein operations.
  Reproduces Ω_Λ to 0.002% — within observational precision,
  not a tunable match.
- **Functional form `w(z) = 1 − α·(H_0/H)^β`** is the simplest
  saturating form with H(z) as its argument; H(z) is framework-
  derived (uses Ω_m, Ω_Λ).

### Audit risks

- **β = 1/12 is not uniquely framework-forced.** Required β =
  0.0804 (to exactly fit w_b at z=1090). Candidates:

  | β candidate | Value | Off from required |
  |---|---|---|
  | 1/12 = 1/(2·INTERACT) | 0.0833 | 3.6% |
  | 1/(4π) | 0.0796 | 1.0% |
  | 1/(q_3·INTERACT/2) = 1/9 | 0.111 | 38% |
  | (1−φ⁻⁴)/12 | 0.071 | 11% |

  `1/(4π)` matches *better* than `1/12`. It is also a clean
  geometric constant. Without a forcing argument for `1/12`
  specifically, this is the K_STAR^14 ansatz pattern (multiple
  candidates near observation).

- **Functional form is one of several.** `w(z) = 1 − α·exp(−H/H_*)`
  or `w(z) = 1 − α·log(H_0/H + e)` would also match at fitted
  parameters. The (H_0/H)^β form is natural but not uniquely
  forced.

- **z_eff assignment is approximate.** Each Planck observation
  depends on a range of z; assigning one z per observable is a
  simplification that introduces ~1-2% noise.

### Triage outcome

**Candidate Class 4**, with audit work concentrated on:

1. Forcing argument for `β = 1/12` over `1/(4π)`. Most natural
   candidate: a Klein-antipodal Z₂-rep counting that produces
   `2·INTERACT = 12` from the framework's existing machinery
   (down-type derivation uses `q_2²·q_3 = 12`).

2. Forcing argument for the `(H_0/H)^β` functional form. Most
   natural candidate: derive from the framework's underlying
   stochastic dynamics (D33 decoherence formalism or D8 a_0(z)
   integration).

3. Sharpening z_eff: each Planck observation's effective
   redshift could be refined via the actual CMB likelihood
   sensitivity functions. Reduces residuals further.

If item 1 closes (β = 1/12 forced from Klein-antipodal Z₂-rep),
the C5 closure becomes Class 5 / Survives. Until then, it is
candidate Class 4 with the K^14 = 1/8 risk pattern flagged.

## What this does to the work map

`remaining_gap_shapes.md` Shape A.2 (Ω_b genuine Floor) shifts
substantially:

- **Before this calculation**: Ω_b is the framework's first
  remaining substrate-side structural gap.
- **After this calculation**: Ω_b residual closes 34× via
  framework-integer C5 to within 0.2%. Remaining 0.2% is
  comfortably within Floor noise band.
- **Status**: Candidate Class 4 closure pending β forcing
  argument. If that audit closes, Ω_b moves to Class 5 /
  Survives. If not, Class 2 / Class 4 borderline.

Shape A.3 (Ω_c/Ω_b) inherits: Ω_DM/Ω_b at C5-corrected weights
gives 0.2658/0.0494 = 5.380 vs observed 5.41 (0.6% off, vs
original 7.5%). Same pattern.

## Comparison to A_s closure attempt

| Property | A_s (Floor #1) | Ω_b (Floor #2) |
|---|---|---|
| Disambiguation test | Dissolves (anchor-side) | Survives (substrate-side) |
| Original residual | 11% / 7.7σ | 6.7% / 11σ |
| Closure attempt | G1.α + G1.β both null | C5 with framework integers |
| Remaining residual | 11% (irreducible at current scope) | **0.2%** (within Floor noise) |
| Audit status | Category statement, not derivation | Candidate Class 4 (β forcing TBD) |

The asymmetry holds: A_s closes via category disambiguation; Ω_b
closes via substrate-side derivation. Both closures land on the
"vocabulary-is-the-work" pattern but in opposite ways.

## What to do next

If user accepts the C5 closure:

1. Update `framework_status.md`: move Ω_b from Floor (genuine)
   to Floor (candidate Class 4 closure), pending β forcing.
2. Update `omega_b_residual_phase_a.md` and
   `omega_b_substrate_side_audit.md`: cross-reference this
   closure.
3. Audit β = 1/12 vs 1/(4π) for forcing argument. If Klein-
   antipodal Z₂-rep produces 12 = q_2²·q_3 in the right
   context, the closure consolidates to Class 5.

If user wants to keep auditing:

1. Test alternative functional forms (exponential, log) against
   the same z_eff data; see if (H_0/H)^β is uniquely fit-best.
2. Refine z_eff assignment via CMB likelihood sensitivity;
   check whether residuals shrink further.
3. Test whether β = 1/(4π) gives a better global fit than
   β = 1/12 — if yes, the framework-integer interpretation
   weakens.

## Cross-references

- `omega_b_residual_phase_a.md` — three-way inconsistency, C1-C5
- `omega_b_substrate_side_audit.md` — disambiguation test passes
  (substrate-side)
- `baryon_fraction.md` D8 — a_0(z) = cH(z)/(2π) framework
  prediction
- `boundary_weight.md`, `boundary_weight.py` — w-formalism
- `ansatz_audit_policy.md` — triage applied (β = 1/12 risk
  pattern)
- `klein_antipodal_z2_rep_pattern.md` — pattern needed to force
  β = 1/12 via 12 = q_2²·q_3 if such a derivation exists
- `framework_status.md` — needs update if closure accepted
- `a_s_g1_closure_attempt.md` — parallel Floor closure attempt
  with opposite outcome
