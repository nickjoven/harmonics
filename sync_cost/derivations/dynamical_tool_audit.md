# Dynamical-tool audit: circle maps vs Kuramoto, conceptual
periods vs discrete time

## What this file is

A research note auditing the framework's choice of dynamical
formalism. Triggered by recognizing that the hierarchy problem
(anchor-count obstructions #2, #4, #5) is the binding blocker
for the substrate-forced ε question (`epsilon_physical_reading.md`)
and likely for the framework's broader scale-bridging program.

Three claims tested:

(A) Circle maps and Kuramoto are alternative tools, choosing one
    over the other matters.
(B) Circle maps' discrete time is load-bearing physics; without
    it, derivations break.
(C) Neither tool naturally produces hierarchies; the hierarchy
    generator is something else in the framework.

**Verdicts:** (A) false — already audited as continuum-limit
equivalent. (B) false — circle-map iteration is structural/
algebraic time (Farey-mediant descent), not physical time, and
the framework primitives are continuous-time-agnostic. (C) true
— hierarchies come from z₀-stratification, not from the K-axis.
This recasts the K-axis uniqueness work: it was on the wrong
axis for hierarchy resolution.

## Status of the dynamical formalism in the framework

### Circle-map-based derivations

| File | Use of discrete time |
|---|---|
| `circle_map.py`, `circle_map_utils.py` | tongue widths, devil's staircase, winding number |
| `a_s_geometric_proof.md` | A_s residual via tongue width at K=1 |
| `born_rule.md`, `born_rule_tongues.py` | saddle-node parabola in 1D map |
| `higgs_from_tongue_boundary.md` | tongue boundary frequency at K=1 |
| `beta_from_tongues.py` | RG flow from tongue widths |
| `mode_locking_spectrum.py` | tongue dynamics |
| `K_star_iteration.py`, `CHAIN_KSTAR.md` | K-iteration to fixed point |
| `k_axis_uniqueness.py`, `k_scaling_scan.py` | K-sweep over staircase |

### Kuramoto-based derivations

| File | Use of continuous time |
|---|---|
| `einstein_from_kuramoto.md` | ADM/Einstein from Kuramoto field |
| `continuum_limits.md` | K=1 → Einstein, K<1 → Schrödinger |
| `a0_threshold.md` | MOND scale via critical Kuramoto |
| `kam_bridge_synthesis.md` | KAM/Lyapunov on Z₂ quotient |
| `proof_C_bridge` (in derivation/) | Λ → a₀ via Kuramoto K_c |

### The bridge that's already in the repo

`continuum_limits.md` Part I §1 establishes the equivalence:

> The discrete self-consistency condition
> `r = Σ_{p/q} g(p/q) · w(p/q, K₀|r|) · e^{2πi(p/q)}`
> at K = 1 with `w(p/q, 1) ~ c/q²` (theorem about standard
> circle map at criticality), summed against Farey measure
> `1/q²`, converges to Lebesgue on [0, 1] and the sum becomes
> the **Kuramoto self-consistency integral**.

So circle maps (discrete) and Kuramoto (continuous) are
**provably the same content** in the framework's already-
audited structure. Choosing one over the other for any
derivation that lives in the locking/Z₂-rep regime is a
formalism choice, not a physics choice.

This is reading (A) above: false. The audit was done in
`continuum_limits.md` and stands.

## Where the formalism choice does matter

Two derivations where the discrete-time formulation is *not* a
matter of taste:

### K_STAR via iteration

`a1_from_saddle_node.md:213-214, 241, 265` explicitly rules out
naive Kuramoto r-iteration for K_STAR:

> "naive Kuramoto iteration is ruled out; candidates not tried in
> code include cosmological K(t) running, non-perturbative tongue
> width near K ≈ 1, and Lyapunov spectrum at the golden rotation
> number."

Reason: in the Kuramoto formulation, r = 0 is a superstable
fixed point with contraction rate exactly q₂ = 2 — meaning naive
iteration on r converges to 0, not to K_STAR. The circle-map
iteration on K (`K_star_iteration.py`) does converge to K_STAR
because it iterates a different quantity (the K-fixed-point of
joint matter-sector closure), not the order parameter.

So K_STAR is a circle-map iteration result, but the iteration is
**on K-self-consistency**, not on phase dynamics. It does not
require physical discrete time — only an algebraic iteration on
K-values until the Farey-mediant condition closes.

### Tongue-width formulae

`circle_map.py`'s `tongue_width(p, q, K)` is a property of the
discrete iteration. The continuous-time analog (Adler equation
ode dθ/dt = ω - K sin θ) has the *same* tongue widths in the
limit of small K → 0 (Adler closed form), but the K = 1 critical
behavior differs in a noise-sensitive way.

The framework uses circle-map widths because:

- They are exact for any K (no continuous-time approximation).
- They are computationally cheap.
- The Z₂-rep / coprime-to-6 / Klein-antipodal machinery operates
  on rational denominators (combinatorial), not on phase
  trajectories.

These are convenience reasons, not physics reasons. A continuous-
time reformulation would give the same combinatorial output.

This is reading (B) above: false. The discrete time is a tool,
not load-bearing physics. Conceptual periods (next section)
substitute cleanly.

## What discrete time actually is in the framework

Reading `circle_map.py` carefully, "iteration" `θ_{n+1} = θ_n +
Ω - (K/2π) sin(2π θ_n)` is **not Planck-time stepping**. It is
an algebraic recursion on a 1D phase. The "time" index n counts
**applications of the map**, which physically corresponds to:

- **Stern-Brocot mediant levels**: each iteration descends one
  Farey level. n = 1 examines the 1/2 vs 1/3 vs 2/3 partition;
  n = 2 examines the F_5 partition; etc.
- **Klein-loop traversals**: each iteration is one full traversal
  of the Klein bottle's fundamental loop.
- **Z_6 / Z_{q₂q₃} cycles**: each iteration is one cycle through
  the gauge-fiber's residue group.
- **z₀-power depths**: each iteration is one application of
  multiplication by z₀ = q₂ + i q₃ on the Gaussian-integer
  lattice.

These are **all algebraic** — none of them is a physical-time
sample. The framework's primitives (`integers`, `mediant`,
`fixed_point`, `parabola`) are time-free.

So "iteration count" in the framework should be read as
"structural depth," not "Planck time count." This is consistent
with how `K_star_iteration.py` actually uses iteration: to find
the joint matter-sector closure point K_STAR, which is a
fixed-point of a self-consistency equation, not a temporal
evolution.

## Conceptual periods as discrete-time substitutes

The framework already speaks an algebraic-period language:

| Period | Source | Cardinality | Meaning |
|---|---|---|---|
| Klein-loop | `klein_bottle.md` | 2 (Z_2 component) × 3 (Z_3 component) | One traversal of fundamental loop |
| Z_6 cycle | `klein_bottle.md` | 6 = q₂·q₃ | Residue cycle |
| Farey-mediant | `mediant_derivation.md` | depth-dependent | Stern-Brocot descent |
| z₀-power | `hierarchy_gaussian_lattice.md` | 13 per step | Gaussian-integer scaling |
| Fibonacci-depth | `hierarchy_gaussian_lattice.md` | φ-based | Mediant-recursion depth |

Each substitutes for "one iteration of the circle map" in
specific contexts:

- For tongue-locking and devil's-staircase content: Farey-mediant
  descent is the natural structural time.
- For the Z₂-rep / Klein-antipodal machinery: Klein-loop period
  is the natural cycle.
- For the gauge fiber: Z_6 cycle.
- For the cosmological hierarchy: z₀-power and Fibonacci-depth.

The framework's existing four primitives (integers, mediant,
fixed_point, parabola) all operate in algebraic time. None
requires Planck-time discrete sampling.

This is reading (B) confirmed: continuous time and discrete time
both reduce to the same algebraic structure — the difference is
representation, not physics.

## Why neither tool produces hierarchies

This is the load-bearing point.

The standard circle map has K ∈ [0, ~1] (and then chaos for
K > 1). It is **bounded**. There is no "K-iteration" that
produces a hierarchy of scales. The K-axis sweeps through tongues
of increasing q (and orbit counts 1, 3, 6, 11, …), but it does
not generate factor-of-13⁵⁴ separations.

The Kuramoto model has K ∈ [0, ∞). It has a critical coupling
K_c, above which synchronization sets in. But again, K is a
single coupling and does not generate scale hierarchies.

Neither formalism, on its own, produces the Planck-Hubble factor
R = 6·13⁵⁴.

What does produce it (per `hierarchy_gaussian_lattice.md`) is
**multiplication by z₀ = q₂ + i q₃ on the Gaussian-integer
lattice**. Each application multiplies the relevant scale by
|z₀|² = 13. Depth 54 gives 13⁵⁴ = R/6. The factor of 6 = |Z₆|
is the gauge multiplicity.

z₀-stratification is **algebraic, not dynamical**. It is not a
"time evolution" — it is a multiplicative depth count. The
framework's R = 6·13⁵⁴ derivation already uses this, and
`observer_register_closure.md` explicitly recasts R as "register
resolution at maximal depth."

So the hierarchy generator is in the framework, and it is
**neither circle map nor Kuramoto**. The dynamical tools handle
locking, tongues, and Z₂-rep partitioning; the algebraic tool
(z₀-stratification) handles the hierarchy.

## Implication for the K-axis uniqueness work

PR #77 (`k_axis_uniqueness.md`) and PR #76 (`k_scaling_scan.md`)
both swept the K-axis of the circle map. Both ran into the same
wall: the K-axis is bounded, doesn't produce hierarchies, and
the resolution ε needed to align K_STAR with framework integers
(INTERACT) sits between two canonical observer registers but at
no canonical intermediate scale.

Audit conclusion (now sharper): **the K-axis was the wrong axis
for a hierarchy-resolution probe**. It is the right axis for the
locking-content question (which produced the Class 5 plateau
theorem, intact). It is not the right axis for the resolution-
between-registers question (which is fundamentally a hierarchy
question).

The right axis for hierarchy: **z₀-stratification depth**
(equivalently, Fibonacci-depth in the φ² scaling regime). This is
exactly C1 / C2 of the decomposition note's candidate list.

## Reframing the substrate-forced ε question

Rather than: "what ε does the substrate force on the K-axis?"

The right question: "what depth does the substrate force at the
particle sector?"

In z₀-stratification language:
- Cosmological hierarchy is at depth 54 (forced by `R = 6·13⁵⁴`).
- Particle hierarchy at v_EW would be at some depth d_EW.
- v/M_P ≈ 13⁻¹⁵ suggests d_EW ≈ 15, but the depth is unforced
  (anchor-count obstruction #2, `numerology_inventory.md`
  Class 2).

If d_EW were structurally derived, the implied resolution at
that depth is `ε ≈ |z₀|^{-d_EW} = 13^{-d_EW/2}`. For
d_EW = 15: `ε ≈ 13^{-7.5} ≈ 6e-9` (very fine, escape regime).

This still doesn't land in the K_STAR-INTERACT window. So even
solving the depth-forcing problem at the EW scale doesn't
trivially close the ε question — but it would close the
hierarchy problem itself, after which ε becomes a derivative
property.

## Recommendation

Treat the hierarchy problem as the binding blocker. Three
specific actions:

1. **Stop K-axis probing for hierarchy resolution.** It is the
   wrong axis. The K-axis is correctly used for locking content
   (Z₂-rep partitions, A_s, Born rule, gauge structure); using
   it for scale separation is a category error.

2. **Pursue z₀-stratification depth-forcing for v_EW.** This is
   anchor-count obstruction #2, the C1 path of the decomposition.
   Concretely: construct an argument forcing d_EW from
   substrate-side considerations (Klein-fold structure,
   sub-action of |Z₆| × ⟨z₀⟩₅₄ × ⟨ι⟩, or Fibonacci-recursion
   on the gauge fiber). If d_EW = 15 emerges from such an
   argument, v/M_P closes structurally, anchor count drops to
   one, and ε is supplied as a derivative.

3. **Audit-tag K-axis results accordingly.** PR #77's
   `k_axis_uniqueness.md` plateau theorem stands. The K-axis
   tie-in (K_STAR → INTERACT) was already revised to Class 2 in
   `epsilon_physical_reading.md`. Both writeups should reference
   this dynamical-tool audit so the structural-time vs physical-
   time framing is explicit.

## What conceptual periods can do for the hierarchy problem

The framework's four primitives (`integers`, `mediant`,
`fixed_point`, `parabola`) plus the registered conceptual
periods (Klein-loop, Z_6, Farey-depth, z₀-power, Fibonacci-
depth) cover all of the framework's existing derivations
without requiring discrete physical time.

For the hierarchy problem specifically:
- **Klein-loop and Z_6** give the gauge multiplicity (factor 6 in R).
- **z₀-power** gives the depth-54 cosmological scaling.
- **Fibonacci-depth** in the φ² scaling regime gives the Planck-
  Hubble 145.8 levels (`anchor_count_audit.md`).

What's missing: **a Klein-fold operation that connects the
cosmological depth (54) to the EW depth (~15)** without anchor
import. This is anchor-count obstruction #2 stated in conceptual-
period language.

If such an operation exists — e.g., "the EW scale lives at the
sub-action depth that completes the Z_6-fold of the cosmological
register" — d_EW becomes derivable, and the entire ε / hierarchy
cluster closes.

This is the substantive open question. It is structural,
algebraic, and lives in the framework's already-existing
conceptual-period vocabulary. Discrete time (circle-map
iteration) is not needed; conceptual periods substitute fully.

## Cross-references

- `continuum_limits.md` — circle map ↔ Kuramoto continuum-limit
  equivalence (already audited)
- `a1_from_saddle_node.md` §"It is not" — naive Kuramoto
  r-iteration ruled out for K_STAR
- `K_star_iteration.py` — circle-map iteration as algebraic
  fixed-point search
- `hierarchy_gaussian_lattice.md` — z₀-stratification as the
  hierarchy generator
- `klein_antipodal_z2_rep_pattern.md` — algebraic period
  vocabulary
- `observer_register_closure.md` §2 — R = 6·13⁵⁴ as register
  resolution at depth 54
- `anchor_count_audit.md` §Obstructions — the five blockers,
  three of which intersect this audit
- `epsilon_substrate_decomposition.md` — the decomposition this
  refines
- `epsilon_physical_reading.md` — sub-problem 1 audit that this
  is the methodological follow-up to
- `k_axis_uniqueness.md` — the result whose axis-choice is
  audited here
- `framework_status.md` — needs no immediate update; this audit
  recommends pursuing C1 / C2 paths
