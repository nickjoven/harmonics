# Ω_b w_+ structural derivation: candidate found, ansatz audit applied

## What this file is

Direction 2 of the post-Ω_b-closure work: derive w_+ ≈ 0.929
(the last empirical fit parameter in the Ω_b two-component
closure) from framework structure.

**Result**: Best framework-integer candidate is **w_+ = 13/14**,
which fits all three Planck partition observables within **0.13%**
(comparable to or better than the empirical fit). However, two
other framework-integer candidates (14/15, 12/13) also fit
within ~1%. Per `ansatz_audit_policy.md` Step 4, this defaults
to **Class 2** absent a specific forcing argument selecting 13/14.

This is a **partial result**: candidate identified, predictions
verified at high precision, but full Class 5 closure of w_+
requires a forcing argument that distinguishes 13/14 from the
nearby alternatives.

## The candidate: w_+ = 13/14

### Structural reading

```
w_+ = 13/14 = |F_6| / (q_2 × |F_4|)
            = (Ω_Λ logit numerator) / (Ω_DM logit denominator)
```

- 13 = |F_6| (Farey count at depth 6, the DE-mode count)
- 14 = q_2 × |F_4| = q_2 × 7 (matches the Ω_DM logit denominator
  per `partition_logit_form.md`)

Equivalently:

```
1 - w_+ = 1/14 = 1/(q_2 × |F_4|)
```

The "fractional unlocking" is `1/(q_2 × |F_4|)` — the inverse of
Ω_DM's logit denominator.

### Predictions at w_+ = 13/14

Under the (α, β) = (0, 1), w_- = 1 closure formulas
(`omega_b_alpha_beta_closure.md`):

| Observable | Predicted (rational) | Predicted (decimal) | Observed | Residual |
|---|---|---|---|---|
| Ω_b | 13/264 | 0.04924 | 0.04930 | **0.12%** |
| Ω_DM | 35/132 | 0.26515 | 0.26500 | **0.06%** |
| Ω_Λ | 181/264 | 0.68561 | 0.68470 | **0.13%** |
| Sum | 1 (exact) | 1.000 | 1.000 | exact |

All three predictions within 0.13% of observation. **No fit
parameter** — fully framework-integer prediction.

### Cleanest framework-integer reading

The framework's Ω partition under w_+ = 13/14:

```
Ω_Λ : Ω_DM : Ω_b = 181 : 70 : 13 / 264
```

Where:
- 264 = N · 7 = (132/7) · 7 (using N = 132/7 at w_+ = 13/14)
- 264 = q_2³ · 33 = 8 · 33 (33 = q_3 · |F_5|)
- 264 = 2 · 132 = q_2 · 132 (132 = 11 · 12 = |F_5| · (q_2·INTERACT))

The "264" denominator is more complex than "19" but reflects the
fractional w_+ structure.

## Ansatz audit (per `ansatz_audit_policy.md`)

### Step 1 — Enumerate alternative framework-integer candidates

Within 1% of observed w_+ ≈ 0.9296:

| Candidate | Value | Off | Framework expression |
|---|---|---|---|
| **13/14** | 0.9286 | 0.11% | \|F_6\| / (q_2·\|F_4\|) |
| 14/15 | 0.9333 | 0.40% | (q_2·\|F_4\|) / (q_3·MEDIANT) |
| 12/13 | 0.9231 | 0.70% | (\|F_6\|−1) / \|F_6\| |
| 23/25 | 0.9200 | 1.03% | not clean framework |

Three framework-integer candidates within ~1%. Multiple
candidates → ansatz pattern.

### Step 2 — Forcing argument for 13/14 specifically

Possible structural sources:

(a) **Cross-sector logit ratio**: w_+ = (Λ logit num)/(DM logit
    denom) = 13/14. Connects two specific logit elements as a
    cross-ratio. **Suggestive but not derived** — the framework
    doesn't currently have a "cross-ratio invariant"
    machinery.

(b) **Inverse Ω_DM logit denom**: 1 - w_+ = 1/14 = inverse of
    Ω_DM's logit denominator. The "unlocking magnitude" matches
    the DM-sector's structural integer. Suggestive structural
    relation but again not derived.

(c) **Stern-Brocot mediant approach**: 13/14 sits between 12/13
    and 14/15 in mediant order. The "best Diophantine
    approximation" of w_+ might be 13/14 by continued-fraction
    convergence — but this requires specifying what the "true"
    w_+ irrational target is.

None of these is a forcing argument that **uniquely** selects
13/14. **Step 2 fails.**

### Step 3 — Klein-antipodal pattern check

The Klein-antipodal Z_2 rep machinery (`klein_antipodal_z2_rep_pattern.md`)
forces specific framework integers (factor 6 from S_3 orbit
dimensions, factor 9 from Klein parity). For w_+ = 13/14 to be
analogous, we'd need a Klein-antipodal orbit count giving 13 in
the numerator AND 14 in the denominator separately.

13 = |F_6| comes naturally from Farey at depth 6.
14 = q_2 · |F_4| comes from a different (q_2 × Farey-depth-4) count.

These are NOT a single Klein-antipodal orbit decomposition;
they're two separate framework integers from different operations.
The cross-sector pairing is not Klein-antipodal-rep-derived.

**Step 3 doesn't validate** the specific 13/14 selection.

### Step 4 — Default verdict

Per `ansatz_audit_policy.md`:

> "Default Class 4 → Class 2 if the audit can't produce a
> forcing mechanism within one sitting."

Default applies. **w_+ = 13/14 is Class 2** at this audit's
resolution.

## What this changes

### What survives

- The Ω_b two-component closure stands (per
  `omega_b_alpha_beta_closure.md`) with (α, β) = (0, 1) and
  w_- = 1 STRUCTURAL.
- w_+ remains an empirical operating-point parameter.
- All three Planck observables fit to <0.13% at the candidate
  value.

### What this attempt yielded

- **Numerical match**: w_+ = 13/14 fits the data within 0.13%
  on all three observables (no fit, just framework-integer
  prediction).
- **Structural reading**: w_+ relates two specific logit-form
  integers (Λ numerator and DM denominator).
- **Ansatz status**: Class 2 per audit discipline; not Class 5.

### Comparison to other Floor entries

| Floor entry | Empirical | At candidate w_+ = 13/14 |
|---|---|---|
| Ω_b residual | 6.76% (single-w) | 0.12% |
| Ω_DM residual | 0.70% (single-w) | 0.06% |
| Ω_Λ residual | 0.07% (single-w) | 0.13% |

Substantial improvement on Ω_b. The 13/14 candidate, even at
Class 2 status, is a **strong empirical reading** of the
framework's prediction.

## Methodological note

This is the framework's recurring multi-candidate ansatz pattern
(per `continuity_in_K_nulls.md` N12-N13, `omega_b_c5_beta_audit.md`
β = 1/12 vs 1/(4π), and others). When the framework has a
specific empirical target and multiple framework-integer
expressions are within ~1%, ansatz_audit_policy correctly
demotes to Class 2 absent forcing.

The previous closures (D.3, D.1, Ω_b (α, β)) were Class 5 via
the **recognize mode** — the structural argument was already in
existing framework content; no choice between alternatives.

For w_+ = 13/14 to recognize-mode-close, the forcing argument
would need to be ALREADY IN existing framework content somewhere
(e.g., a derivation that establishes 13/14 as a specific
characteristic ratio). Not currently identified.

## Region C connection

Per `numerology_count_phase_a.md`, Region C tests whether the
framework's 1-3% Floor cloud is rational-approximation noise or
structural signal. The w_+ = 13/14 candidate is **exactly the
shape Region C should resolve**:

- If cloud is signal: 13/14 might be ANOTHER signal entry,
  promoting to Class 4 candidate
- If cloud is pigeonhole: 13/14 is a coincidence among many
  framework-integer candidates near the target

Region C empirical Phase B would inform whether 13/14 should
be promoted or stay Class 2.

## Recommendation

The honest landing: **w_+ closure to Class 5 is not achieved by
this attempt**. The framework supplies a strong candidate
(13/14) but multi-candidate ansatz pattern blocks Class 5 absent
forcing.

Path forward options:

1. **Accept w_+ as empirical operating-point parameter**.
   The Ω_b closure (per `omega_b_alpha_beta_closure.md`) is at
   one structural derivation + one empirical parameter. Same
   pattern as K_STAR (matter-sector operating coupling, also
   empirical).

2. **Pursue the cross-ratio forcing argument** for 13/14
   structurally. Would require deriving that "the cross-ratio
   between Ω_Λ logit numerator and Ω_DM logit denominator
   sets the baryon partial-locking weight" from framework
   primitives. Substantial multi-session work; not closeable
   in one sitting.

3. **Wait for Region C verdict** before pursuing further. If
   Region C says cloud is pigeonhole, this is just one more
   ansatz; if signal, the 13/14 candidate becomes worth
   pursuing harder.

Given the iteration discipline established earlier, **option 1
is the cleanest landing**. The framework's two-anchor minimum
plus per-sector operating-point parameters (K_STAR, w_+) is
the structural shape. Closing every operating-point parameter
to Class 5 requires deriving the framework's response to its
anchors — a deeper question.

## Status

Direction 2 produces partial result: framework-integer
candidate **w_+ = 13/14** identified with 0.13% match across
three observables. **Class 2 per audit discipline** (multi-
candidate ansatz pattern, no unique forcing argument).

Ω_b closure status (post this attempt):
- Tier 1 mechanism: Class 5 (sym/antisym two-component)
- Tier 2 (α, β): Class 5 (sign-rep no-EM)  
- Tier 3 (w_+ candidate): **Class 2** (this note)

The closure remains substantively progress over single-w
formula (6.7% → 0.12%); the empirical operating-point parameter
status is a feature, not a defect, parallel to K_STAR.

## Cross-references

- `omega_b_alpha_beta_closure.md` — Tier 1 + Tier 2 closure
- `partition_logit_form.md` — direction 1 result that exposed
  the q_2 × q_3-sector pattern
- `ansatz_audit_policy.md` — Step 4 default applied
- `continuity_in_K_nulls.md` N12-N13 — multi-candidate ansatz
  pattern precedent
- `numerology_count_phase_a.md` — Region C, which would inform
  whether 13/14 is signal or pigeonhole
- `framework_status.md` — needs no immediate update; Ω_b stays
  at substantial-but-not-fully-closed status
