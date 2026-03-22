# Derivation 4: Spectral Tilt from Mode-Locking Structure

> Strip away "cost." What remains is phase, frequency, coupling,
> and the rational numbers.

## The problem with Derivation 02

Derivation 02 modeled the CMB spectral tilt (n_s ≈ 0.965) as a synchronization cost gradient across scales, deriving P(k) ∝ 1/C(τ) and attributing the 3.5% deviation from scale-invariance to the slope of that gradient. It used P(k) ∝ 1/C(τ), where C
is a synchronization "cost function." A systematic scan of 7 cost
function families (cost_function_scan.py) showed that **every
monotonically decreasing C(τ) produces positive running**. This is
a theorem, not a fitting problem: for any such C, the function
ln(1/C(τ₀/k)) is convex in ln k.

The Planck central value for running is weakly negative (-0.005 ± 0.007).
Standard slow-roll inflation also predicts small negative running.

The failure is ontological, not parametric. "Cost" carries optimization
structure that obscures the mechanics. We don't need it.

## What a synchronizing system actually has

A Kuramoto system has:

- **Phases** θ_i(t) — the state of each oscillator
- **Natural frequencies** ω_i — drawn from a distribution g(ω)
- **Coupling** K — interaction strength
- **Order parameter** r(t) — amplitude of the mean field
- **Collective frequency** Ω(t) — frequency of the mean field

No "cost." The dynamics are:

    dθ_i/dt = ω_i + (K r / N) Σ sin(θ_j - θ_i)

## The fluctuation spectrum

Above the critical coupling K_c, the system synchronizes: r > 0.
The oscillators split into a locked population (|ω_i - Ω| < Kr,
phase-locked to the mean field) and a drifting population.

The fluctuations of the order parameter around its steady state have
a spectrum. For the locked oscillators, the variance of phase
fluctuations at natural frequency ω is:

    ⟨δθ²⟩(ω) ∝ g(ω) / (K r)²

This is a direct mechanical result: the fluctuation power at frequency
ω is proportional to the density of oscillators at that frequency,
divided by the restoring force (coupling × coherence) squared.

## The mapping

Identify:

    wavenumber k  ↔  natural frequency ω
    P(k)          ↔  ⟨δθ²⟩(ω) ∝ g(ω) / (K r(ω))²

The power spectrum of primordial perturbations is the fluctuation
spectrum of the synchronized state. The spectral shape comes from
g(ω) — the distribution of natural frequencies — modulated by
r(ω), the scale-dependent order parameter.

This is simpler and more mechanical than Derivation 02. No cost
function, no "power as inverse cost." Just: how are the oscillators
distributed in frequency, and how coherent is each sub-ensemble?

## Why rational numbers

In coupled oscillator systems, synchronization occurs preferentially
at rational frequency ratios. This is mode-locking: two oscillators
with frequencies in ratio p/q (integers) return to the same phase
relationship after q cycles of one and p of the other. The phase
relationship is periodic, so constructive interference persists.
Irrational ratios never repeat — phase coherence drifts.

This produces Arnold tongues in the (K, ω₁/ω₂) plane: wedge-shaped
regions of parameter space where oscillators lock to each rational
ratio. As coupling increases, the tongues widen. The fraction of
frequency space that is locked follows a devil's staircase — a
monotone function that is flat (constant, locked) on every rational,
with measure-zero transitions between them.

The frequency distribution g(ω) is not smooth. It is structured by
mode-locking: concentrated at rational multiples of the fundamental,
depleted at irrationals. At sufficient coupling, g(ω) approaches
a devil's staircase.

## The spectral tilt from g(ω)

If g(ω) is a devil's staircase (or an approximation to one), then:

    n_s - 1 = d ln g / d ln ω + d ln(1/(Kr)²) / d ln ω

The tilt has two contributions:

1. **The slope of g**: how the density of locked oscillators varies
   with frequency. If more oscillators lock at lower frequencies
   (larger Arnold tongues for small-integer ratios), g decreases
   with ω, giving a red tilt.

2. **The scale-dependent coherence**: if r decreases at higher
   frequencies (smaller ensembles synchronize less completely),
   this adds to the red tilt.

Both contributions are red (n_s < 1), consistent with observation.

## The running from the staircase

The running dn_s/d ln k depends on the **local curvature** of
ln g(ω) at the pivot scale. A devil's staircase has:

- **Flat segments** (locked plateaus): d ln g / d ln ω = 0, and
  the running is determined entirely by the r(ω) term.

- **Transition regions** between plateaus: g changes rapidly, and
  the curvature can be positive or negative depending on which
  side of the transition you're on.

- **Self-similar structure**: the curvature at any scale depends on
  the local rational approximation structure.

Unlike a smooth cost function (which always gives positive running),
the staircase structure can produce negative running if the pivot
scale sits on the **upper side of a transition** — where g is
concave (curving downward) as you approach the next locked plateau
from below.

Physical interpretation: at the pivot scale, the system is
transitioning from one mode-locked ratio to the next. The density
of states is bending over (concave) as it approaches the new
plateau. This concavity produces negative running.

## The hierarchy of ratios

Small-integer ratios have wider Arnold tongues (more robust locking):

    1:1 > 2:1 > 3:2 > 4:3 > 5:4 > ...

The tongue width decreases roughly as 1/q for ratio p/q. This means:

- The fundamental (1:1) dominates — most oscillators lock here
- The octave (2:1) is next — the first harmonic
- The fifth (3:2), fourth (4:3), etc. follow

The frequency distribution g(ω) has its largest concentration at
the fundamental, with decreasing concentrations at each successive
rational ratio. The **envelope** of these concentrations determines
the large-scale shape of g, and therefore the spectral tilt.

The **fine structure** — the specific curvature between adjacent
rationals — determines the running.

## What this changes

| Quantity | Old (Derivation 02) | New |
|----------|--------------------|----|
| P(k) | 1/C(τ) | g(ω) / (Kr)² |
| Tilt source | Cost gradient | Frequency distribution slope |
| Running sign | Always positive | Depends on staircase position |
| Free parameter | x_* (pivot depth) | Position on staircase |
| Physical picture | Cost minimization | Mode-locking |

The "cost function" was a smooth approximation to the envelope of
a devil's staircase. The smoothing destroyed the curvature structure
that determines the running sign.

## Open questions

1. **What sets the pivot position on the staircase?** The pivot scale
   k_* = 0.05 Mpc⁻¹ corresponds to a specific location in the
   rational hierarchy. Which transition is it near?

2. **Can we compute g(ω) from first principles?** The frequency
   distribution of primordial oscillators — what determines it?
   In the Kuramoto model, g is an input. Here it must emerge from
   the dynamics.

3. **The r(ω) dependence**: how does the order parameter vary with
   scale? This is the "how coherent is each sub-ensemble" question,
   and it feeds into both tilt and running.

4. **Connection to lattice**: the Stribeck lattice shows mode-locking
   (subharmonic generation at rational ratios of ω_d/ω₀). The
   differential attenuation IS the frequency distribution being
   sculpted by mode-locking. Can we extract g(ω) from lattice data?

## Status: Resolved

The numerical follow-through (see below) resolved the open questions:

1. **The pivot sits at 1/φ** — the golden ratio, the hardest point to
   mode-lock. This is the unique fixed point of the Gauss map, the
   "most irrational" number.

2. **The staircase at 1/φ is exactly self-similar** with scaling factor
   φ² ≈ 2.618. Each Fibonacci bracket carries 1/φ² of the parent's
   winding: Δ(ln|ΔW|) = -ln(φ²) per level. This gives an exactly
   flat power spectrum in the natural (Stern-Brocot) coordinates.

3. **The tilt comes from the k ↔ Ω mapping**, not from the staircase
   itself. rate = (n_s - 1)/(-ln φ²) = 0.0365 Fibonacci levels per
   e-fold. The observable universe samples ~2.2 levels.

4. **The amplitude A_s ≈ 2.1 × 10⁻⁹** places the pivot at Fibonacci
   level ~21 (F₂₁ = 17711, within 5×10⁻¹⁰ of 1/φ).

The separation is clean: **the staircase provides scale-invariance;
the dynamics provide the tilt.**

## Computational chain

The following Python scripts implement and verify this derivation
(read in order — see `INDEX.md` for the full dependency graph):

| Script | Role |
|--------|------|
| `cost_function_scan.py` | Shows all monotonic cost functions give wrong running sign |
| `circle_map.py` | Circle map, Arnold tongues, devil's staircase |
| `golden_ratio_pivot.py` | Zoom into 1/φ, identify it as the pivot |
| `stern_brocot_map.py` | Sample staircase on Stern-Brocot tree, not decimal grid |
| `phi_squared_zoom.py` | **Central result**: exact φ² self-similarity at 1/φ |
| `k_omega_mapping.py` | The k↔Ω mapping: rate, amplitude, running |
| `superharmonic_regime.py` | Non-Fibonacci rationals as overtone structure |
| `staircase_geometry.py` | 3D representations: Arnold surface, Poincaré disk, curvature |
| `fibonacci_ones.py` | The ψ-eigenmode and the alternating convergence |

Shared utilities: `circle_map_utils.py`
