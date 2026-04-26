# Cross-ratio search for w_+ forcing argument

## What this file is

Recognize-mode probe (path 1 from chat after w_+ candidate
identification): search the framework for cross-ratio /
projective-invariant content that might force w_+ = 13/14
structurally.

**Result**: Cross-ratio machinery EXISTS in the framework
(`lie_group_characterization.md`: PSL(2,ℤ)-equivariance forces
preservation of all Farey cross-ratios). The probe surfaces TWO
different structural cross-ratio readings, each pointing at a
slightly different w_+ value:

- **Static cross-ratio**: `CR(0, 1/q_2; Ω_Λ_static, 1−1/q_3) = 13/14`
  using Ω_Λ_static = 13/19 (the framework's static prediction
  at single-w = 1)
- **Self-consistency cross-ratio**: under the closure formula
  with Ω_Λ(w_+) variable, the equation `w_+ = CR(0, 1/q_2;
  Ω_Λ(w_+), 2/3)` has unique rational solution **w_+ = 12/13**

Both are framework-integer candidates within ~1% of empirical
best fit. Per `ansatz_audit_policy.md` Step 4, **multi-candidate
ansatz pattern still defaults to Class 2**.

The cross-ratio reading is **structural content** (PSL(2,ℤ)
invariants are real framework objects), but doesn't uniquely
force a specific w_+ value.

## Cross-ratio machinery in framework

`lie_group_characterization.md` Step 3 derives:

> Farey-preserving implies cross-ratio-preserving. ... any
> homeomorphism of P¹(ℝ) that maps the Farey triangulation to
> itself must preserve the cross-ratio of every quadruple of
> points in P¹(ℚ).

The framework's substrate has a PSL(2,ℤ) action on the Farey
graph; cross-ratios of Farey 4-tuples are projective invariants
under this action.

This means: any framework prediction expressed as a cross-ratio
of Farey points is a STRUCTURAL INVARIANT, not an ad hoc
combination.

## Search results

### Direct enumeration: 13/14 as cross-ratio of framework points

Searched 4-permutations of {0, 1, 1/2, 1/3, 2/3, 1/6, 5/6,
Ω_b, Ω_DM, Ω_Λ} for cross-ratios giving 13/14. Found **24
distinct 4-tuples** producing 13/14 or its reciprocal 14/13.

Examples:
- `CR(0, 1/2; Ω_Λ, 2/3) = 13/14`
- `CR(0, Ω_DM; 1, 5/6) = 13/14`
- `CR(0, 1/2; 13/19, 2/3) = 13/14` (using Ω_Λ = 13/19 static)

Multiple natural 4-tuples → not uniquely forced.

### Cross-ratio self-consistency under closure

Under the closure `Ω_Λ(w_+) = (12 + w_+)/(17 + 2w_+)`, the
self-consistency condition

```
w_+ = CR(0, 1/q_2; Ω_Λ(w_+), 1 − 1/q_3)
```

simplifies to:

```
CR = w_+/14 + 6/7
w_+ = w_+/14 + 6/7
w_+ (13/14) = 6/7
w_+ = 6/7 × 14/13 = 12/13 ≈ 0.9231
```

So the self-consistent rational solution is **w_+ = 12/13**.

### Predictions comparison

| Candidate | Source | Ω_b residual | Ω_DM residual | Ω_Λ residual |
|---|---|---|---|---|
| **13/14** | Static cross-ratio match | **0.12%** | 0.06% | 0.13% |
| **12/13** | Self-consistency cross-ratio | 0.65% | 0.12% | 0.15% |
| **14/15** | Empirical near-fit | 0.34% | **0.01%** | 0.12% |

All within Floor noise (≤1%). None is decisively best on all
three observables.

## Ansatz audit

### Step 1 — Enumerate alternatives

THREE framework-integer candidates with three different sources:

- 13/14 = `|F_6|/(q_2·|F_4|)` from static cross-ratio
- 12/13 = `q_2·INTERACT/|F_6|` from cross-ratio self-consistency
- 14/15 = `(q_2·|F_4|)/(q_3·MEDIANT)` from empirical fit

All within 1% of observed. Multi-candidate ansatz pattern.

### Step 2 — Forcing argument check

For 13/14: requires selecting the specific 4-tuple
(0, 1/q_2, Ω_Λ_static, 2/3) over 23 other 4-tuples that also
give 13/14. No unique forcing.

For 12/13: requires the self-consistency cross-ratio choice of
(0, 1/q_2, Ω_Λ(w_+), 2/3) to be UNIQUELY framework-natural.
Other 4-tuples involving Ω_Λ(w_+) give different
self-consistencies (e.g., (1/2, 1/3, Ω_DM, Ω_Λ) gives an
irrational solution). The (0, 1/q_2, Ω_Λ, 2/3) tuple has
suggestive content (Farey-endpoint + q_2-reciprocal + DE
prediction + q_3-complement) but isn't uniquely forced.

For 14/15: empirical only, no structural source identified.

### Step 3 — Klein-antipodal pattern

None of the candidates emerges from Klein-antipodal Z_2 rep
orbit-counting (the pattern that closed D.3, D.1, Ω_b (α, β)
to Class 5).

The cross-ratio invariance is a DIFFERENT framework structure
(PSL(2,ℤ) Farey-graph automorphism) than Klein-antipodal Z_2
rep orbit-counting. Both are framework-internal, but they
operate on different objects (Farey points vs Z_6 lattice
modes).

### Step 4 — Default verdict

Multi-candidate ansatz; no specific cross-ratio 4-tuple is
uniquely forced; **Class 2 default holds**.

## What the search yielded

**Substantive recognize-mode progress**:
- Cross-ratio machinery IS in the framework
  (`lie_group_characterization.md`)
- 13/14 IS a Farey cross-ratio (24 different 4-tuples)
- 12/13 IS the unique rational solution to a natural
  cross-ratio self-consistency
- Both readings are structural, not ad hoc

**But not uniquely forcing**:
- Multiple 4-tuples give 13/14
- Multiple cross-ratio self-consistencies are constructible
- No SPECIFIC framework derivation forces (0, 1/q_2,
  Ω_Λ, 2/3) over alternatives

The cross-ratio reading is RICHER than I expected (the framework
has the machinery + multiple identities give framework-relevant
ratios), but the multi-candidate pattern persists.

## Updated Ω_b closure status

Closure stands at:
- Tier 1 (mechanism): Class 5 (sym/antisym two-component)
- Tier 2 (α, β): Class 5 (sign-rep no-EM)
- Tier 3 (w_+ value): **Class 2** (multiple cross-ratio
  candidates: 13/14, 12/13, 14/15 all framework-integer-clean
  within 1%)

The cross-ratio reading **enriches** the Class 2 status (now
the candidates have specific projective-geometric
interpretations rather than just being "small framework-integer
ratios near 0.929"), but doesn't promote it.

## What would close to Class 5

Either of:

1. **Forcing the specific 4-tuple** (0, 1/q_2, Ω_Λ, 1−1/q_3)
   as THE framework-natural cross-ratio for w_+ — derivation
   from Klein-antipodal Z_2 rep + Farey cross-ratio invariance
   composed. Requires connecting the two framework structures.

2. **Identifying which candidate (13/14, 12/13, 14/15)
   the framework's underlying dynamics actually selects**
   via a different mechanism (e.g., MOND-threshold derivation
   of w_+).

Both are non-trivial multi-session work. Neither is closeable
in a recognize-mode probe.

## Methodological note

This recognize-mode probe is NOT a failure — it surfaced
substantive structural content (cross-ratio machinery applies;
multiple framework cross-ratios exist for 13/14). The verdict
is "structurally rich but not uniquely forcing," which is more
informative than "no structural content found."

The framework's discipline correctly demotes this to Class 2:
having multiple structural readings is itself a multi-candidate
ansatz pattern at the meta-level.

## Region C connection (sharper now)

Region C numerology count would test: is the framework's 1-3%
Floor cloud the expected density of "rational best
approximations to projective invariants"? Under the cross-ratio
reading, the cloud might consist of approximations to specific
cross-ratio invariants of Farey points + framework predictions.

If true, the cloud is calibrable structurally (cross-ratio
density), and individual entries (like w_+ = 13/14 vs 12/13 vs
14/15) are the framework's "best rational approximation to a
specific cross-ratio invariant."

This sharpens Region C's interpretation: the count would be
testing whether the Floor cloud matches Diophantine
approximation density of cross-ratio invariants.

## Cross-references

- `lie_group_characterization.md` Step 3 — PSL(2,ℤ) preserves
  Farey cross-ratios
- `omega_b_w_plus_candidate.md` — earlier identification of
  w_+ = 13/14
- `omega_b_alpha_beta_closure.md` — Tier 1 + Tier 2 closure
- `partition_logit_form.md` — direction 1 (logit form)
- `ansatz_audit_policy.md` — Step 4 default applied
- `numerology_count_phase_a.md` — Region C, sharpened now

## Status

Path 1 recognize-mode probe complete. Cross-ratio machinery
surfaces multiple structural readings but no unique forcing.
Ω_b Tier 3 (w_+) stays Class 2. Closure status unchanged
overall, but the Class 2 entry now has explicit structural
interpretation (cross-ratio invariants of Farey 4-tuples
involving framework prediction points).

Region C interpretation sharpened: cloud might be calibrable
as Diophantine density of cross-ratio invariants.
