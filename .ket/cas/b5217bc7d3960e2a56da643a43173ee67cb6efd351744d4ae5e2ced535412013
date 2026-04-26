# Cosmic partition prediction in logit form

## What this file is

Restatement of the framework's cosmic partition prediction
(`baryon_fraction.md`: Ω_Λ : Ω_DM : Ω_b = 13 : 5 : 1 / 19) in
**logit form** — using the transformation `x → x/(1−x)` (odds
ratio) instead of the partition fraction directly.

The logit form **exposes a structural pattern hidden in the
original**: all three logit denominators factor cleanly as
`q_2 × (q_3-sector integer)`. This is a new structural
observation about the partition's complement structure.

This restatement does NOT change the framework's prediction (the
partition is the same). It clarifies what's being predicted and
exposes structure for downstream derivations.

## The transformation

The logit (odds-ratio) transformation:

```
x → x / (1 − x)
```

For partition fractions Ω_i ∈ [0, 1], this maps to "odds of being
in sector i versus all other sectors."

Inverse: `x = odds / (1 + odds)`.

Sum-to-1 constraint on Ω_i becomes: `Σ Ω_i = 1` ⟺ for each i:
`(1 − Ω_i) = Σ_{j≠i} Ω_j` (complement = sum of other sectors).

## Logit form of the framework's partition

At the framework's static prediction (single-w, w = 1):

| Sector | Ω_i | Logit Ω_i / (1 − Ω_i) | Numerator | Denominator |
|---|---|---|---|---|
| Λ (DE) | 13/19 | **13/6** | 13 = \|F_6\| | 6 = q_2·q_3 |
| DM | 5/19 | **5/14** | 5 = MEDIANT | 14 = q_2·\|F_4\| |
| b (baryon) | 1/19 | **1/18** | 1 = baryon count | 18 = q_2·q_3² |

## Structural observation: q_2 factorization in denominators

**All three logit denominators have a factor of q_2:**

```
6  = q_2 × q_3       (= q_2 × 3)
14 = q_2 × |F_4|     (= q_2 × 7)
18 = q_2 × q_3²      (= q_2 × 9)
```

The "complement integers" (the denominators of the logit ratios)
factor uniformly as `q_2 × (q_3-sector quantity)`. The
q_3-sector quantities are:

```
3  = q_3              (spatial dimension; gauge-color triplet count)
7  = |F_4|            (Farey count at depth 4; or q_2² + q_3 = 7)
9  = q_3² = K_LEPTON  (lepton-sector constant)
```

This is a **q_2 × q_3-sector factorization** of the partition's
complement structure. **The q_2 factor is uniform across all
three sectors**; the q_3-sector quantity varies per sector.

## Why this is interesting structurally

Under the original Ω_i = (i-numerator) / |F_7| form, the
partition denominators are all the same (= 19 = |F_7|). The
sector-specific structure is buried in the numerators.

Under the logit form, the sector-specific structure is in the
denominators (6, 14, 18), and the **uniform q_2 factor** is
exposed. The remaining q_3-sector quantities (3, 7, 9) describe
how each sector specifically relates to the q_3 (color/lepton)
structure.

This factorization isn't visible in the original form — it
emerges only under the logit transformation.

## Numerator + denominator sums

For each sector, num + denom = |F_7| = 19 trivially (since
num/(num + denom) recovers Ω_i = num/|F_7|).

This isn't new structure; it's a tautology of the logit
transformation. But it confirms |F_7| as the **conserved quantity**
across all three sectors: each sector's logit-num + logit-denom
sums to the same |F_7|.

## Logit form under the (α, β) = (0, 1) closure

Per `omega_b_alpha_beta_closure.md`, the partition under the
two-component (sym/antisym) closure is:

```
Ω_b   = w_+ / (17 + 2w_+)
Ω_DM  = 5 / (17 + 2w_+)
Ω_Λ   = (12 + w_+) / (17 + 2w_+)
```

with single free parameter w_+ ≈ 0.929 (sym baryon partial-locking
weight) and w_- = 1 (antisym DM-like always locked, structural).

Logit ratios under this closure:

```
Ω_b / (1 − Ω_b)   = w_+ / (17 + w_+)
Ω_DM / (1 − Ω_DM) = 5 / (12 + 2w_+)
Ω_Λ / (1 − Ω_Λ)   = (12 + w_+) / (5 + w_+)
```

At **w_+ = 1**:
- 1/18, 5/14, 13/6 (matching the framework's static prediction)

At **w_+ ≈ 0.929** (observed):
- 1/(17 + 0.929) = 0.0518 ≈ Ω_b_obs/(1 − Ω_b_obs) = 0.0519 ✓
- 5/(12 + 1.858) = 0.361 ≈ Ω_DM_obs/(1 − Ω_DM_obs) = 0.360 ✓
- (12.929)/(5.929) = 2.181 ≈ Ω_Λ_obs/(1 − Ω_Λ_obs) = 2.171 ✓

The closure formula is consistent with the logit form and the
static prediction is its w_+ = 1 limit.

## Implications

### 1. Cleaner exposition

The framework's partition prediction can be stated as:

> **Each cosmological sector i has odds-ratio
> Ω_i / (1 − Ω_i) = N_i / (q_2 × M_i)** where N_i ∈ {1, 5, 13}
> and M_i ∈ {q_3², |F_4|, q_3} are framework-derivable
> sector indices.

This is more transparent than "Ω_i = N_i / 19" because:
- The q_2 factor is exposed as universal
- The sector-specific q_3-sector variation is in M_i
- The conserved |F_7| = N_i + q_2·M_i is automatic

### 2. The q_2 factor in complements

The fact that all three sectors' COMPLEMENTS share a q_2 factor
suggests: the framework's partition has a **Z_2 doubling
structure** in the "everything except this sector" view. Each
sector's complement counts a Z_2-orbit-like structure (factor
q_2) of underlying q_3-sector elements.

This might connect to the Klein-antipodal Z_2 rep machinery (Z_2
is exactly the Klein-antipodal action's order). Worth checking
whether the q_3-sector quantities (3, 7, 9) correspond to specific
Klein orbit structures.

### 3. Predictive implication

If the framework predicts NEW cosmological observables (beyond
Ω_Λ, Ω_DM, Ω_b), they should also have logit denominators
factoring as q_2 × (q_3-sector integer). This is a TESTABLE
structural prediction.

For example: if the framework's `Ω_radiation` has a partition role,
its logit complement should follow the pattern `q_2 × M` for some
framework q_3-sector M. (Currently `Ω_r ~ 9·10⁻⁵` is too small
to test cleanly, but the predictive form is well-defined.)

## Comparison to original form

| Form | Statement | What's exposed |
|---|---|---|
| Original (partition fractions) | Ω_Λ : Ω_DM : Ω_b = 13 : 5 : 1 / 19 | 13, 5, 1 sector counts; 19 = \|F_7\| total |
| **Logit (odds ratios)** | (13/6, 5/14, 1/18) | sector counts + **q_2 × q_3-sector** factorization in complements |

Both are consistent. The logit form is **more structural-content-
dense per number**: each ratio's denominator carries factorization
information that's hidden in the original.

## What this is and isn't

**This is**: a vocabulary refinement (parallel to
`vocabulary_is_the_work_pattern.md` instances) that exposes
hidden structure in the framework's existing prediction.

**This is not**: a new derivation or closure. The partition
prediction itself is unchanged; the logit form is a different
coordinate that makes structure visible.

## Status

The logit form is now formally stated. Three follow-on
candidates:

1. **Connect q_2 factor to Klein-antipodal Z_2 rep machinery**
   structurally — verify that the universal q_2 in complements
   reflects the Z_2 rep order
2. **Identify the q_3-sector quantity pattern** (3, 7, 9 — is
   there a closed form across n? E.g., M_n = q_3·n − q_2 or
   similar)
3. **Apply to other framework predictions** (A_s amplitude, particle
   ratios, etc.) — see if the logit form exposes similar
   structure elsewhere

Not pursued in this note. This note's deliverable is just the
formal restatement; downstream work can build on the exposed
structure.

## Cross-references

- `baryon_fraction.md` — original partition derivation
- `omega_b_residual_phase_a.md` — single-w partition formulas
- `omega_b_alpha_beta_closure.md` — (α, β) = (0, 1) closure with
  w_- = 1 structural
- `omega_b_two_component_sketch.md` — two-component partition
  formula
- `framework_constants.py` — q_2, q_3, INTERACT, K_LEPTON, MEDIANT
  definitions
- `klein_antipodal_z2_rep_pattern.md` — Klein-antipodal Z_2 rep
  machinery (relates to the q_2 factor)
- `numerology_inventory.md` — for any near-matches that might
  benefit from logit-form re-reading

## Status

Direction 1 of three (per chat after Ω_b closure) complete.
Logit form formally stated. q_2 × q_3-sector factorization
identified as the exposed structure. Two unpursued follow-ons
flagged as candidates for further work.
