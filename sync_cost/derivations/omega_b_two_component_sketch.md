# Ω_b two-component sketch: the C2 mechanism mechanically traced

## What this file is

A direct sketch of the two-component reading of the Ω_b residual,
prompted by the user's reframing question ("are we insisting on
anything structural that can be trivialized?"). The sketch maps
Klein-antipodal Z₂-rep eigenmode decomposition onto the partition
formula and tests whether the resulting (w_+, w_-) reading dissolves
the C5 continuity-in-K requirement.

**Result**: the sketch reveals a **structural sum-constraint
obstruction** — naive two-component generalizations trivialize to
single-w via the partition's sum-to-1 condition. A non-trivial
two-component reading exists with two free coefficients (α, β),
which fits observation to 0.15% (45× improvement on Ω_b residual)
but **inherits the same parameter-forcing problem** as the C5
β audit. The two-component reading is structurally promising but
not a free win.

## The sketch

### Step 1 — Two-component eigenmode decomposition

Klein-antipodal Z₂ involution τ: k → 6−k on Z_6. Eigenmodes per
antipodal pair (p, 6−p):

```
ψ_+(p) = (ψ_p + ψ_{6−p}) / √2    (Klein-singlet, sym)
ψ_-(p) = (ψ_p − ψ_{6−p}) / √2    (Klein-sign-rep, antisym)
```

For pair (1, 5):
- ψ_+(1, 5): EM-coupled (Klein-singlet ∩ coprime-to-6) →
  **baryonic mode**
- ψ_-(1, 5): no EM coupling (sign-rep, monodromy −1) →
  **DM-like (gravitates only)**

Singletons {0}, {3} are Klein-self-paired (sym only). Pair (2, 4)
contributes to DM (not coprime-to-6).

Define two boundary weights:
- `w_+`: sym (Klein-singlet) eigenmode partial-locking weight
- `w_-`: antisym (sign-rep) eigenmode partial-locking weight

At idealized K = 1: degeneracy gives `w_+ = w_- = 1` (full lock).
At finite K: Klein-twist lifts degeneracy — sym/antisym tongue
widths split.

### Step 2 — Partition formula generalization

Single-w formulas (from `omega_b_residual_phase_a.md` §2):

```
Ω_Λ(w)   = (11 + 2w) / (16 + 3w)
Ω_DM(w)  = 5 / (16 + 3w)
Ω_b(w)   = w / (16 + 3w)
```

**Naive two-component generalizations trivialize.** I tried two:

(A) Replace "2w" with "(w_+ + w_-)" everywhere:
- |F_eff| = 11 + (w_+ + w_-)
- matter = 5 + (w_+ − w_- correction)
- n_eff = 16 + (combinations)

Sum check: forces w_+ = w_- by the requirement that
Ω_Λ + Ω_DM + Ω_b = 1. The two-component reading collapses to
single-w.

(B) Asymmetric numerators with shared symmetric denominator:
- Ω_Λ = (11 + w_+ + w_-) / N
- Ω_b = w_+ / N
- Ω_DM = (5 + w_- − w_+) / N
- N = 16 + 3(w_+ + w_-)/2

Sum to 1 forces w_+ = w_- again. Same trivialization.

**Conclusion of Step 2**: any two-component reading that simply
"splits the w" without restructuring the partition denominator
trivially collapses. The sum-to-1 constraint is rigid.

### Step 3 — Non-trivial two-component reading

For a real two-component reading, the partition denominator must
itself depend on the (w_+ − w_-) asymmetry, with structurally-
determined coefficients (α, β):

```
Ω_b   = w_+ / N
Ω_DM  = (5 − α·δ) / N           where δ = w_+ − w_-
Ω_Λ   = (11 + 2w_+ − β·δ) / N
N     = 16 + 3w_+ − (α + β)·δ
```

Sum constraint satisfied identically (numerators sum to N).
Single-w limit (w_+ = w_-): δ = 0, recovers original formulas.

This is a real two-component reading. It carries **two unknown
parameters (α, β)** that capture how the asymmetry δ flows
between the three sectors:

- α: how much (w_+ − w_-) shifts modes from baryonic to DM
- β: how much (w_+ − w_-) shifts modes from baryonic to DE

The minimal-structural choice is α = β = 1 (each unit of δ shifts
one mode each way). Other choices (α = 2, β = 0; α = 0, β = 2;
etc.) correspond to different mode-flow patterns.

### Step 4 — Numerical test at α = β = 1

Fitting (w_+, w_-) to match Ω_b and Ω_DM exactly:

```
w_+ = 0.918,  w_- = 0.855,  asymmetry δ = +0.063
```

Predictions vs Planck 2018:

| Observable | Predicted | Observed | Residual |
|---|---|---|---|
| Ω_b | 0.0493 | 0.0493 | 0% (fit) |
| Ω_DM | 0.2650 | 0.2650 | 0% (fit) |
| Ω_Λ | 0.6857 | 0.6847 | **0.15%** |

Compared to original Ω_b 6.7% Floor: **45× reduction**.
Compared to C5 closure (β-audit-ansatz, ~0.2-0.3%): comparable
quality, different structural mechanism.

### Step 5 — The asymmetry sign and magnitude

Required asymmetry δ = w_+ − w_- = +0.063. Interpretation:

- **Sign positive**: sym (baryonic) eigenmode is MORE LOCKED than
  antisym (DM-like). Equivalent: at finite K, the Klein-twist
  shifts the sym tongue width above the antisym.
- **Magnitude ~6%**: comparable to the original Ω_b residual
  (6.7%). Specific numerical prediction for the Klein-twist
  splitting at the relevant K.

This is a **specific testable claim**: at the K where the framework
operates (between K_STAR ≈ 0.86 and K = 1), the Klein-antipodal
Z₂-rep eigenmode tongue widths should show a sym/antisym split of
~6%, with sym wider than antisym.

If actual finite-K Klein eigenmode calculations produce this split
sign and magnitude, the C2 mechanism closes structurally. If they
don't, the two-component reading is numerology-equivalent to the
single-w + ansatz approach.

## Verdict on the sketch

The sketch produced three findings:

### Finding 1 — The two-component reading is real but constrained

Naive "split w into w_+ and w_-" trivializes by sum constraint
(Step 2). A real two-component partition requires asymmetric
mode flow with parameters (α, β) capturing which sectors absorb
the asymmetry (Step 3).

### Finding 2 — Quality of fit matches C5 single-w

With (α, β) = (1, 1) (minimal-structural), the two-component fit
gives 0.15% residual on Ω_Λ and exact fit on (Ω_b, Ω_DM). This is
**comparable** to the C5 single-w closure (0.002-0.28% residuals).
Both readings achieve ~30-50× reduction of the original 6.7% gap.

The two readings are nearly equivalent in NUMBER (since both have
two effective fit parameters: (w_+, w_-) here, (α, β) in C5 single-w).

### Finding 3 — Same parameter-forcing obstacle

The two-component reading requires (α, β) to be framework-derived
to count as Class 5. Without forcing arguments for (α, β):

- α = β = 1 is the "minimal structural" choice but not uniquely
  forced
- Alternative (α, β) values would predict different (w_+, w_-) and
  different asymmetry magnitudes
- Per `ansatz_audit_policy.md`, this is **the same multi-candidate
  ansatz pattern** as the C5 β = 1/12 vs 1/(4π) audit

The user's reframing question therefore lands as:

> **Two-component reading does NOT trivially dissolve the
> structural requirement. It REPLACES the C5 continuity-in-K
> derivation with the C2 sym/antisym tongue-width-asymmetry
> derivation. Both require structural ingredients the framework
> does not currently supply.**

## What the sketch confirms

The user's intuition was correct in *direction*:

- The Klein-antipodal Z₂-rep two-foldness IS a real structural
  feature
- The single-w formalism IS an aggregation that loses
  information
- The two-component reading IS more natural framework-vocabulary

But not in *trivializing*:

- The sum-to-1 constraint forces non-trivial structural choices
  (α, β) to make the two-component reading work
- These choices are themselves not framework-forced at the
  audit-of-one-sitting level
- The C2 mechanism (sym/antisym tongue width asymmetry at finite
  K) is well-defined but requires explicit calculation that
  hasn't been done

## What the sketch reveals about Klein-antipodal vs continuity-in-K

The C5 (continuity-in-K) and C2 (sym/antisym asymmetry) closures
are **DUAL formulations of the same physics** in a precise sense:

- C5: w(z) runs with H(z), single w, smooth interpolation
- C2: (w_+, w_-) split at fixed K, two boundary weights, asymmetry

In the static limit (no K-running), C2 is needed because the
single-w formalism overcounts boundary modes. In the dynamic
limit (K-running), C5 captures the same effect via the running
single-w.

Both readings would close the gap if the underlying mechanism
were derived. Currently neither is.

This is parallel to the discrete (1/12) vs continuum (1/(4π))
β reading — same structure, different scale-readings.

## What this means for the next step

Three sharper directions:

1. **Compute sym/antisym Klein eigenmode tongue widths at K ≈ 0.9
   directly**. Reuse the framework's existing tongue-width
   machinery (`circle_map_utils.py`, `boundary_weight.py`) but
   apply Z₂-rep boundary conditions. Test whether the numerical
   asymmetry δ ≈ 0.063 emerges naturally.

2. **Try to derive (α, β) = (1, 1) as the framework-forced
   choice**. Possible source: mode-counting arguments analogous
   to down-type Phase D (S_3 orbit dimensions). If (α, β) = (1, 1)
   is forced from Klein action on the partition, the two-component
   reading closes.

3. **Recognize C5 and C2 as dual readings**. Don't treat them as
   competing alternatives; treat them as the same physics
   needing one or the other derivation. The audit of "which one
   forces β" becomes irrelevant if either one closes.

Path 1 is the cheapest concrete probe. Path 2 is the most
structurally satisfying but requires real derivation work. Path 3
is a methodological reframe.

## Caveats (per `ansatz_audit_policy.md`)

The two-component sketch produces a numerical fit with parameters
that look framework-flavored but are not uniquely forced. Specific
risks:

- **(α, β) = (1, 1) is one of many "natural" choices.** Without
  forcing argument, this is post-hoc.
- **Asymmetry δ = +0.063 is a number that fits, not a number
  that's predicted from substrate.** Until I compute Klein
  eigenmode tongue widths at finite K and verify δ comes out
  naturally, this is fitting.
- **The 0.15% residual on Ω_Λ** is consistent with Floor noise
  but not exact. Could indicate a missing third correction or
  could just reflect the (α, β) = (1, 1) approximation.

Per the policy's Step 4: default Class 4 → Class 2 unless a
forcing argument is supplied within one sitting. The sketch
**does not supply** such an argument; it provides the framework
in which a forcing argument could be tested.

## Operational status

The sketch is **complete as a sketch** — the two-component
mechanism is now mechanically defined and numerically tested.
It is **not** a closure — it requires either:

- Numerical verification of δ ≈ 0.063 from finite-K Klein
  eigenmode tongue width calculation (path 1)
- Structural derivation of (α, β) = (1, 1) from framework
  primitives (path 2)

Without one of these, the two-component reading sits at the same
status as the C5 closure: Class 4-mechanism + Class 2-parameters.

The user's reframing was correct that two-foldness is structural;
incorrect (or at least not yet demonstrated) that it trivially
dissolves the parameter-forcing problem.

## Cross-references

- `omega_b_residual_phase_a.md` C2 — original C2 mechanism
  identification
- `omega_b_c5_closure.md` — single-w C5 closure
- `omega_b_c5_beta_audit.md` — parallel β-audit failure
- `continuity_in_K_nulls.md` — N9-N16 nulls; particularly N11
  (tongue coverage failure) limits direct Klein eigenmode
  calculation
- `klein_antipodal_z2_rep_pattern.md` — eigenmode framework
- `baryon_fraction.md` — baryonic = sym ∩ coprime-to-6
- `boundary_weight.py` — tongue-coverage formalism for w(K)
- `down_type_double_cover_closed.md` — Phase D (orbit-dimension
  closure as forcing pattern for analogous (α, β))
- `ansatz_audit_policy.md` — Step 4 default applies
