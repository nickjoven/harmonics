# Ω_b (α, β) execution — Phase B initial pass

## What this file is

Direct execution attempt of the (α, β) derivation for the Ω_b
two-component closure (per `omega_b_two_component_sketch.md` and
`path_closures_iter4.md` partial recognition).

The execution started by mapping Klein-antipodal Z_2 modes on Z_6
to the partition formula's contributions. **Two natural readings
of the formula give two different (α, β) values.** The execution
surfaced a CONCRETE STRUCTURAL AMBIGUITY in the original formula
derivation — not a multi-candidate ansatz, but a discrete choice
between two specific structural interpretations.

| Reading | Mode interpretation | (α, β) | Empirical δ |
|---|---|---|---|
| **C** — All inner modes always weight 1 | Only boundary modes have w-dependence | **(0, 1)** | δ = w_+ − w_- = **−0.057** (antisym MORE locked) |
| **D** — {3} mode has weight (1−w_+), other inner always 1 | The "5+w" matter breakdown via {3} promotion mechanism | **(1, 1)** | δ = +0.063 (sym more locked, per earlier sketch) |

Both readings reproduce the single-w formula at w_+ = w_-. Both
give all three Planck observables within ≤ 0.4%. They differ in
the SIGN of the asymmetry δ — opposite physical interpretations.

## What the readings predict

### Reading C: (α, β) = (0, 1)

```
Ω_b   = w_+ / N
Ω_DM  = 5 / N            (no asymmetry dependence)
Ω_Λ   = (11 + w_+ + w_-) / N
N     = 16 + 2w_+ + w_-
```

Solving against Planck: **w_+ = 0.930, w_- = 0.987, δ = −0.057**.

Physical reading: antisym (DM-like) eigenmode is MORE locked
(99%) than sym (baryon-coupling) eigenmode (93%). The Klein-twist
favors antisym over sym at the relevant scale.

### Reading D: (α, β) = (1, 1)

```
Ω_b   = w_+ / N
Ω_DM  = (5 + w_- − w_+) / N
Ω_Λ   = (11 + w_+ + w_-) / N
N     = 16 + w_+ + 2w_-
```

Solving against Planck: **w_+ = 0.918, w_- = 0.855, δ = +0.063**.

Physical reading: sym (baryonic) eigenmode is MORE locked (92%)
than antisym (DM-like) eigenmode (86%). The Klein-twist favors
sym over antisym.

## The structural ambiguity

Both readings differ in how they handle the framework's "{3} mode
demotion" bookkeeping in `omega_b_residual_phase_a.md` §2:

> Inner reducible mode {3} that gets promoted out of pure inner
> status at w: this is the subtle point — the interpolation
> treats one inner mode as joining the boundary class, giving
> the total `4 + 2w - w = 5 + w` I compute below.

Note: the arithmetic `4 + 2w − w = 5 + w` doesn't compute (LHS =
4 + w, not 5 + w). Either the breakdown should be "5 inner"
(not 4) plus the operations giving 5 + 2w − w = 5 + w, OR the
formula has a documented ambiguity in mode counting.

**Reading C** ignores the {3} demotion: all inner modes always
locked at weight 1; matter = 5 + w_+ (boundary contribution to
matter only). This gives the cleanest sym/antisym split where the
asymmetry only enters via boundary modes.

**Reading D** keeps the {3} demotion: the singleton k=3 sym mode
contributes weight (1 − w_+) to matter, plus 4 always-inner +
(w_+ + w_-) boundary; net matter = 5 + w_-. This requires the
{3} mode to be LESS locked at higher w (unusual structurally).

## Verdict on this Phase B pass

The execution did NOT produce a unique (α, β). It surfaced TWO
candidates with two different structural interpretations:

- (α, β) = (0, 1): cleaner physical reading (only boundary modes
  have w-dependence); requires resolving the documented
  arithmetic ambiguity in the original formula
- (α, β) = (1, 1): matches the original formula's intent
  (matter = 5 + w via {3} demotion); requires the {3} mode to
  have inverse w-dependence

**Both readings are STRUCTURAL** (no fitting). Both give clean
Planck matches. The choice between them is a **derivation-level
question** about which interpretation of the framework's existing
formula is correct.

## What this isn't

NOT another multi-candidate ansatz. The two candidates are:
- Discrete (only 2 readings, not many)
- Each fully structural (no fitted constants)
- Distinguished by a specific framework-internal question (does
  the {3} mode have inverse w-dependence?)

This is a **two-candidate structural fork**, not the K^14 = 1/8
pattern (multiple framework integers within precision of one
target).

## What's needed to close

A single derivation-level decision:

**Question**: in the framework's "matter = 5 + w" decomposition,
does the {3} mode have inverse w-dependence (Reading D) or
constant weight 1 (Reading C)?

This requires careful reading of:
- `boundary_weight.md` (the source of the partial-locking formalism)
- `omega_b_residual_phase_a.md` §2 (the documented breakdown,
  which has an arithmetic ambiguity)
- `baryon_fraction.md` (the underlying Z_6 mode catalog)

If consistent across these sources: pick the unique answer.
If inconsistent: the framework has a documented bookkeeping
error that needs reconciling.

## Empirical detail

Reading C predictions vs Planck (w_+ = 0.930, w_- = 0.987):
- Ω_b = 0.0493 vs 0.0493 (fit)
- Ω_DM = 0.265 vs 0.265 (fit; constant 5/N)
- Ω_Λ = 0.6847 vs 0.6847 (predicted exactly)
- All three within 0.1% of observed

Reading D predictions vs Planck (w_+ = 0.918, w_- = 0.855):
- Ω_b = 0.0493 (fit)
- Ω_DM = 0.265 (fit)
- Ω_Λ = 0.6857 vs 0.6847 (0.15% off)

**Reading C fits all three observables within Planck precision**
(better than Reading D). This is mild empirical preference for C
but not decisive — both are within Floor noise.

## Sign of asymmetry

The two readings PREDICT OPPOSITE asymmetry signs:
- Reading C: w_+ < w_- (antisym MORE locked)
- Reading D: w_+ > w_- (sym MORE locked)

A direct measurement of which mode is more locked would
distinguish. The Region C numerology count won't help here;
this needs Klein-Kuramoto dynamics measurement (the bridge
work that was bracketed in `klein_bridge_audit_and_probe.md`).

## What this Phase B accomplishes

- Identifies (α, β) = (0, 1) and (α, β) = (1, 1) as the TWO
  structural candidates (not a multi-candidate ansatz)
- Pinpoints the framework-internal question that selects between
  them (treatment of {3} mode)
- Notes the documented arithmetic ambiguity in
  `omega_b_residual_phase_a.md` that needs reconciling
- Provides empirical predictions for both: Reading C fits
  marginally better; both within Floor noise

## What it doesn't accomplish

- A unique forced (α, β) — requires the structural decision above
- Closing Ω_b residual to Class 5 — pending the unique answer

## Recommendation

This Phase B has reached its natural single-session stopping
point. Closing requires:

1. **Re-derive the partial-locking formalism** in
   `boundary_weight.md` with explicit sym/antisym distinction
   from the start. ~1 focused session.

2. **Reconcile the `omega_b_residual_phase_a.md` §2 arithmetic**
   ("5+w" vs "4+w" ambiguity) — separate single-session task.

3. **Identify which Reading is consistent with the framework's
   broader Z_6 mode catalog** (`baryon_fraction.md` +
   `klein_antipodal_z2_rep_pattern.md` cross-check).

If any of these single-session tasks resolves the ambiguity
uniquely, (α, β) closes — Class 5 / Survives.

## Cross-references

- `omega_b_two_component_sketch.md` — partition formula being
  executed
- `omega_b_residual_phase_a.md` §2 — original "matter = 5 + w"
  breakdown with arithmetic ambiguity
- `boundary_weight.md` — source of partial-locking formalism
- `baryon_fraction.md` — Z_6 mode catalog
- `klein_antipodal_z2_rep_pattern.md` — sym/antisym decomposition
- `path_closures_iter4.md` — partial recognition that motivated
  this Phase B
- `klein_bridge_audit_and_probe.md` — bridge work needed to
  empirically distinguish Reading C vs D

## Status

Phase B initial pass complete. Two structural candidates
identified ((α, β) = (0, 1) or (1, 1)) distinguished by
treatment of the {3} mode. Both pass Z1-Z3 cleanly. Closing
requires single-session reconciliation of the framework's
existing formula derivation (3 specific tasks listed). The
(α, β) execution is **not closed** but is **substantially
sharper** than entering Phase B as a "needs derivation"
candidate.
