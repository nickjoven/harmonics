# Continuity-in-K derivation: prior null results

## What this file is

A registry of prior null findings that constrain the
"continuity-in-K" derivation identified as the missing structural
ingredient by `omega_b_c5_beta_audit.md` and the user's reframing
question. These nulls were already in the repo but were not
collected together as a constraint on the C5 closure's required
mechanism.

The C5 closure assumes:
- `w(z)` is a smooth, continuous function interpolating
  `w ∈ [0, 1]` between Farey levels F_5 and F_6
- `w(z)` runs with H(z) via framework-derived a_0(z)
- The functional form `w(z) = 1 − α·(H_0/H)^β` is structurally
  motivated

The nulls below say: **multiple natural attempts to derive
continuity-in-K from framework primitives have failed**. The
continuity is asserted, not derived. This is the framework's
substantive open structural work.

## Null inventory

### N9 — K(t) Friedmann dynamics: setup only, S3-S5 pending

**Source**: commits `aba6a83`, `505c6aa`;
`k_of_t_friedmann.md`.

**Attempted**: Derive a cosmological-scale ODE for K(t) using
the ADM-Kuramoto dictionary, recovering the Friedmann equation
at K = 1.

**Result (partial)**: S1-S2 closed at K = 1 (flat FLRW gives
r(t) = 1 throughout, since K_eff = 3/2 > K_c = 1). S3 (lock
fraction F_locked(K) as Ω_m(K)), S4 (horizon-crossing
amplification τ_unlock(n)), S5 (inflation → matter → Λ era
timeline) **pending**.

**Constraint on C5**: the framework explicitly attempted to
derive K(t) running across cosmological eras and only got the
trivial K = 1 fixed point. The intermediate-era K(z) running
that C5 requires is not yet derived. *The framework knows it
needs this and has not produced it.*

### N10 — K_STAR is a coordinate scale, NOT a synchronization order parameter

**Source**: commit `fd48905`, `cross_parabola_audit.py`,
`a1_from_saddle_node.md` §"It is not".

**Attempted**: Derive K_STAR via Kuramoto r-iteration as the
synchronization order parameter; alternatively, find joint
(K*, d) such that matter and duty cells populate one parabola.

**Result (null)**: r-iteration converges to r = 0 (superstable
fixed point with contraction rate exactly q_2 = 2). K_STAR sits
in the *disordered phase* of the iteration, NOT at the synchronized
fixed point. Cross-parabola K* ↔ d does not constrain K_STAR.

**Constraint on C5**: K_STAR is *the parabola primitive's
coordinate scale*, not a Kuramoto K_c that runs continuously.
**This rules out the natural reading "K_STAR is the today-value
of a continuously running K".** If K(z) runs, it is not K_STAR
that runs — K_STAR is a fixed coordinate. The C5 closure's
implicit assumption that "the framework's effective K varies
between K_STAR (matter) and K=1 (cosmological)" needs a
different mechanism than continuous K-running through K_STAR.

### N11 — Tongue coverage as w(K): caps at 0.138 then discontinuously jumps to 1

**Source**: commit `b85d043`,
`boundary_weight.py` HONEST SUMMARY (lines 13-50).

**Attempted**: Derive `w(K) = tongue_coverage_q6(K) / max_coverage`
as a smooth function of K, hoping w sweeps [0, 1] continuously.

**Result (null)**: tongue coverage caps at 0.138 for K < 1,
then jumps discontinuously to 1.0 at K = 1 because of the
`min(w6/max_w6, 1.0)` clamp. **The function is non-monotone
and discontinuous; it never reaches w* = 0.828 (the empirical
target) at any K < 1.**

The HONEST SUMMARY in boundary_weight.py explicitly states:
> "Section 2 (tongue_coverage_q6 scan) and Section 3
> (fixed-point search) are NOT genuine self-consistencies."

**Constraint on C5**: The most direct framework derivation of
w(K) from substrate primitives (tongue widths) **fails
structurally**. The C5 closure's `w(z) ∈ [0.828, 0.957]` must
come from a different mechanism than tongue coverage.

This is the **most damaging prior null** for the C5 closure:
it says the natural framework attempt was tested and didn't
work. The continuity-in-K derivation requires either a
different mechanism for w(K) or a fix to the tongue-coverage
discontinuity.

### N12 — A_s α_2 Phase B: three-sub-gap decomposition

**Source**: commit `e06684a`, `a_s_alpha2_phase_b.md`
(if file exists; otherwise commit body).

**Attempted**: Derive A_s prefactor by decomposing into
α_1·α_2·α_3 from existing axioms A1-A6.

**Result (null)**: All three coefficients open. Three sub-gaps:

- **S1 (R gauge ambiguity)**: R = δθ vs δθ/(2π) vs other; `sigma_squared.py` uses one but doesn't derive the canonical normalization.
- **S2 (formula-meaning ambiguity)**: same expression treated as per-bracket variance AND per-d-ln-k power in different sections; differ by `rate ≈ 0.0365`, a 27× ambiguity.
- **S3 (q^-2 source ambiguity)**: gate fraction (W1) vs inverse mode density (W2); both produce 1/q² scaling but predict different prefactors.

**Constraint on C5**: closely parallels the C5 audit's β
ambiguity. The framework's static formalism allows multiple
mutually-compatible parameterizations; selecting one requires
additional structural input that doesn't currently exist.
The pattern of "framework gives the right scaling, doesn't
force the prefactor" repeats here.

### N13 — A_s prefactor numerology cluster

**Source**: commit `95f165b`, `a_s_amplitude_audit.md`.

**Attempted**: Match the required prefactor `C_{A_s} = 4.415`
from a single framework-integer / framework-constant expression.

**Result (null with red flag)**: Multiple expressions match
within 1%:

| Candidate | Value | Off |
|---|---|---|
| e·φ | 4.398 | 0.38% |
| π·√2 | 4.443 | 0.64% |
| 4π/3 | 4.189 | 5.1% |

The audit doc explicitly flags "**e·φ and π·√2 both match within
1% — flagged as a red flag for numerological coincidence**."

**Constraint on C5**: the same multi-candidate ansatz pattern
applies to A_s prefactor as to Ω_b C5's β. Both are cases where
"framework-integer expressions cluster near observation without
forcing argument." The pattern is recurring; this isn't a
property of either specific derivation but of how the framework's
small-integer combinations populate near-target ranges
densely.

### N14 — Tongue-width convention split (μ vs μ/π)

**Source**: commit `4b6aac9`,
`tongue_formula_accuracy.py`,
`noise_dressed_parabola.py` reading (D).

**Attempted**: Establish a single convention for what
`tongue_width(p, q, K)` returns.

**Result**: Two valid conventions exist:
- (D-1) μ — saddle-node control parameter in (x, μ) normal-form
  coordinates
- (D-2) μ/π — Ω-space Arnold tongue width

Related by Jacobian π. **Both are correct framework readings**;
load-bearing derivations are robust only via ratio-taking
(π cancels).

**Constraint on C5**: the C5 functional form (H_0/H)^β requires
a specific tongue-width convention to evaluate. If β and α are
to be uniquely framework-forced, the convention must be
canonicalized — or the closure must be expressed in a
ratio-form that's convention-independent. Currently neither.

### N15 — Phase C halts: DoF(K²) = 1 not derived

**Source**: commit `e134a7c`, down-type Phase C
(`down_type_double_cover_phase_c.md`).

**Attempted**: Derive down-type factor 6 from per-direction
DoF count on Klein bottle K². Reached factor 6 via Z_2 × Z_3
DoF coupling.

**Result (partial halt at the time)**: Three sub-claims
remained:
- **C1**: justify DoF(K²) = 1 (not 2 or 3) from the non-abelian
  relator `abab⁻¹ = 1`.
- **C2**: identify 1/w(Σ) with DoF(Σ) per surface.
- **C3**: commutativity of Fibonacci shift with surface-DoF.

(Eventually closed in Phase D via S_3 orbit dimensions —
commit `fa7515f`. The intermediate halt is informative for
understanding what kind of structural arguments were needed.)

**Constraint on C5**: the closure of Phase C required a
**different formulation** (orbit dimensions instead of DoF
count). Lesson: the framework often needs to *change vocabulary*
to close a continuity claim. For C5, the analogous question
is: what's the right vocabulary for w(K) interpolation? Tongue
coverage failed (N11); something else is needed.

### N16 — Phase C halt C1: monodromy factor-3 residual

**Source**: commit `bcee583`, `down_type_double_cover_phase_c1.md`.

**Attempted**: Extract DoF from connection 1-form monodromy.

**Result (null)**: monodromy gives factor 6 instead of 1; off
by factor 3. The connection-form approach to deriving
DoF didn't close.

**Constraint on C5**: even when the framework gets close to a
result via geometric-topological machinery, residual factors
of small integers persist. This suggests the C5 closure's
β = 1/12 vs 1/(4π) ambiguity (with bridge factor π/3) might
have the same kind of residual — close but not closing without
a missing argument.

## Pattern across the nulls

The seven nulls (N9-N15, plus N16 closely related) share three
recurring failure modes:

1. **Discontinuity at K = 1** (N11): framework primitives often
   give clean results AT K = 1 but discontinuous behavior
   approaching K = 1 from below. The continuum-limit-meets-
   discrete-substrate transition is structurally tricky.

2. **K_STAR is fixed, not running** (N10): natural reading
   "K_STAR is the today-value of running K" is wrong by
   structural argument. K_STAR is a *coordinate*, not a
   *coupling* in the Kuramoto sense.

3. **Multi-candidate ansatz patterns** (N12, N13, plus current
   C5 β audit): when the framework produces near-matches via
   small-integer expressions, multiple candidates always
   appear. This is endemic, not specific to any one derivation.

These three patterns together explain why the C5 closure's
β = 1/12 vs 1/(4π) audit landed null: **the underlying
continuity-in-K derivation has known failure modes that the
ad hoc functional form `w(z) = 1 − α·(H_0/H)^β` does not
address**.

## What this means for the C5 Tier-2 closure

The β audit's "default Class 4 → Class 2" verdict can now be
re-read more sharply:

**Original reading**: β isn't uniquely forced because multiple
candidates match.

**Revised reading**: β isn't uniquely forced because the
**continuity-in-K derivation that would force β doesn't exist
yet, AND has known failure modes (N11 most directly) that any
new attempt would need to address**.

This is a stronger statement than "we haven't tried hard
enough." It says the framework has **structural reasons**
continuity-in-K is hard to derive at all.

## What's left untried

Of the C5 derivation's three required pieces (per
`omega_b_c5_continuity_requirement.md` framing):

1. **Continuity-in-K of Klein-antipodal Z₂-rep counts**:
   tongue-coverage attempt (N11) failed. **Untried**: a finite-K
   correction to Klein-antipodal eigenmode tongue widths
   (the "C2 mechanism" from `omega_b_residual_phase_a.md`).

2. **K(z) from substrate dynamics**: K(t) Friedmann attempt
   (N9) only got trivial K = 1. **Untried**: K(z) running via
   sector-coupling relaxation (path C5 from
   `omega_b_residual_phase_a.md` cited as most leverage).

3. **a_0(z) → w(z) bridge**: never directly attempted. Would
   require deriving how the MOND scale a_0(z) sets the locked-
   fraction at scale z. Saddle-node primitive (P4) is the
   natural source.

Each is non-trivial structural work. Together they constitute
the "Tier 2 closure" needed to upgrade C5 from Class 4-mechanism
to Class 5-derivation.

## Anti-patterns specific to this closure

Per `ansatz_audit_policy.md`, three anti-patterns to avoid:

- **Picking β to fit observation**: trivially Class 2.
- **Constructing framework-integer expressions evaluating to
  ~0.08**: too easy (1/12, 1/(4π), λ/INTERACT, 1/(4π+1), etc.
  all in range).
- **Asserting w(K) is "smooth" because we want it to be**:
  N11 says smooth w(K) from tongue coverage **doesn't exist
  in the framework**. Any continuity claim must address this.

## Acceptance criterion

A successful continuity-in-K derivation would:

1. Replace tongue-coverage w(K) (N11 failure) with a
   substrate-derived alternative that smoothly produces
   w ∈ [0, 1] across K ∈ [0, 1] without discontinuity at K = 1.
2. Produce K(z) as a structural function (not as iteration
   from K_STAR per N10).
3. Force a single β value (or a structurally bounded range,
   per the discrete-continuum bridge reading) without ansatz.
4. Pass Z1-Z3 of `statistical_conventions.md` cleanly.

None of N9-N15 produced this. The current closure (Tier 1
mechanism, Tier 2 ansatz) is the framework's best landing
*absent this derivation*.

## Cross-references

- `omega_b_c5_closure.md` — the Tier-1 mechanism this would
  upgrade
- `omega_b_c5_beta_audit.md` — the β audit defaulting to
  Class 2 absent the derivation
- `omega_b_residual_phase_a.md` — original Ω_b residual
  decomposition, C1-C5 candidates
- `boundary_weight.py` HONEST SUMMARY — N11 source
- `cross_parabola_audit.py` — N10 source
- `K_star_iteration.py` — N10 background; r=0 superstable
- `k_of_t_friedmann.md` — N9 source
- `a_s_alpha2_phase_b` — N12 source (commit `e06684a`)
- `a_s_amplitude_audit.md` — N13 source
- `tongue_formula_accuracy.py` — N14 source
- `down_type_double_cover_phase_c.md` — N15 source
- `dynamical_tool_audit.md` — context: K-zoo and K-iteration as
  algebraic, not temporal
- `vocabulary_is_the_work_pattern.md` Instance 4 — K-zoo
  precedent for distinguishing K's
- `ansatz_audit_policy.md` — pattern recurring across these
  nulls
