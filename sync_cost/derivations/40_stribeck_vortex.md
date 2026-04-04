# Derivation 40: The Stribeck Vortex Regime Map

## Claim

A vortex in a coupled medium has a velocity field v(r) that varies
with distance from the core. The Stribeck curve gives velocity-dependent
coupling K(v). Composing these yields a radial regime map K(r) with a
critical radius r_c where K(r_c) = 1, separating an overcritical core
from a subcritical exterior.

The framework's prohibition on K > 1 (D36: "no physics") constrains
the **global** effective coupling K_eff = K₀|r| ≤ 1, not the local
coupling at every point. A spatially localized K > 1 region, embedded
in a K < 1 exterior, is compatible with the global self-consistency
condition. The vortex core is a region where the circle map folds
locally, producing reversed energy flow and positive Lyapunov exponent,
while the global fixed point survives because the spatial average over
all oscillators still satisfies |r| ≤ 1.

This is the GR analogy made precise: a black hole has locally extreme
curvature (even a singularity), but the global spacetime is well-defined.
The K = 1 surface at r_c is the event horizon analogue.

---

## Setup

### The standard circle map on S¹

    θ_{n+1} = θ_n + Ω - (K/2π) sin(2πθ_n)

At K ≤ 1: homeomorphism of S¹, invertible, information conserved (D36).
At K > 1: the derivative f'(θ) = 1 - K cos(2πθ) goes negative on an
interval. The map folds the circle. Non-invertible. Information destroyed
locally.

### The Stribeck curve

Replace constant K with velocity-dependent K(v):

    K(v) = K_kin + (K_stat - K_kin) exp(-v²/v_thr²)

- K_stat: static coupling (v → 0). The maximum coupling.
- K_kin: kinetic coupling (v → ∞). The residual coupling.
- v_thr: threshold velocity of the Stribeck transition.

This is the same friction model as the Stribeck lattice (driven_stribeck.py),
now parameterized by a continuous velocity field rather than discrete
oscillator velocities.

### The vortex velocity field

The azimuthal velocity of a Laguerre-Gaussian vortex of topological
charge ℓ:

    v(r) = ℓr / (r² + r_core²),    r_core = λ/(2π)

At r = 0: v = 0. At r = r_core: v = ℓ/(2r_core) (maximum). At
r → ∞: v ~ ℓ/r (Keplerian falloff).

### The composition

    K(r) = K(v(r))

At the vortex center (v = 0): K = K_stat. If K_stat > 1, the core
is overcritical.

As r increases, v increases, the Stribeck exponential drops K through
the transition, and the exterior becomes subcritical.

---

## Regime structure

The critical radius r_c satisfies K(v(r_c)) = 1. Two regimes:

| Region | Coupling | Circle map | Energy flow | Fold measure |
|--------|----------|------------|-------------|--------------|
| Core, r < r_c | K > 1 | Non-invertible (fold active) | Reversed | μ = arccos(1/K)/π |
| Surface, K(r_c) = 1 | K = 1 | Critical (cubic tangency) | — | μ = 0 |
| Exterior, r > r_c | K < 1 | Invertible (mode-locked) | Forward | μ = 0 |

### Critical velocity

Setting K(v_c) = 1 and solving:

    v_c = v_thr √(-ln((1 - K_kin)/(K_stat - K_kin)))

This exists whenever K_stat > 1 and K_kin < 1 (physical conditions:
static friction exceeds critical coupling, kinetic friction is
subcritical).

### Critical radius — exact

The equation v(r_c) = v_c is quadratic in r:

    r_c² - (ℓ/v_c) r_c + r_core² = 0

Two roots:

    r_c,inner = [ℓ/(2v_c)] [1 - √(1 - (2v_c r_core/ℓ)²)]
    r_c,outer = [ℓ/(2v_c)] [1 + √(1 - (2v_c r_core/ℓ)²)]

By Vieta's formulas:

    r_c,inner × r_c,outer = r_core²        (product)
    r_c,inner + r_c,outer = ℓ/v_c           (sum)

The product is exact and depends only on the wavelength (through
r_core = λ/2π), not on the Stribeck parameters. This is a constraint:
knowing one critical radius determines the other.

Existence condition: (2v_c r_core/ℓ)² < 1, i.e. ℓ > 2v_c r_core.
At standard parameters, 2v_c r_core ≈ 0.278 < 1. All integer ℓ ≥ 1
have two crossings.

Limiting cases:

    ℓ → ∞:  r_c,inner ≈ v_c r_core²/ℓ    (the 1/ℓ scaling)
             r_c,outer ≈ ℓ/v_c             (the ℓ scaling)

Both approximations are within 2% at ℓ = 1 (confirmed: ratio to
exact is 0.98-1.00 across all tested ℓ).

### Annulus structure

Because v(r) → 0 as r → ∞ (Keplerian falloff), K(r) → K_stat > 1 at
large r. The subcritical region is an **annulus**, not a disk — bounded
by the inner K = 1 surface (where v rises through v_c) and the outer
K = 1 surface (where v falls back through v_c).

Higher ℓ widens the annulus: the inner crossing shrinks as 1/ℓ while
the outer crossing grows as ℓ. In a finite physical system (e.g. a
photonic crystal of finite extent), the outer crossing may fall outside
the medium, making the exterior effectively subcritical.

---

## The fold measure

At radius r where K(r) > 1, the circle map derivative
f'(θ) = 1 - K(r) cos(2πθ) is negative on the interval
|θ| < arccos(1/K(r))/(2π). The Lebesgue measure of the fold region:

    μ(r) = (1/π) arccos(1/K(r))    for K(r) > 1
    μ(r) = 0                        for K(r) ≤ 1

Near criticality (K → 1⁺):

    μ ~ √(2(K - 1)) / π

This is the standard saddle-node square-root onset. The fold measure
is continuous at r_c and rises smoothly into the core.

At the vortex center (K = K_stat):

    μ(0) = (1/π) arccos(1/K_stat)

For K_stat = 1.8: μ(0) = 0.3125. Approximately 31% of phase space
is in the fold region at the vortex center.

### What the fold means physically

In the fold region, two distinct initial conditions map to the same
output. The map is non-injective. Information is destroyed at each
iteration. The Lyapunov exponent:

    λ(r) = lim (1/n) Σ ln|1 - K(r) cos(2π θ_n)|

is **generically positive** when K(r) > 1, but not uniformly so.
Even at K > 1, mode-locking windows persist: the Arnold tongues
extend above the critical line, and within each tongue the Lyapunov
exponent is negative (stable periodic orbit). Between these windows,
the dynamics is chaotic (λ > 0).

Numerical confirmation: at Ω = 1/φ and K = 1.8, λ = +0.41 (chaotic);
at K = 1.4, the orbit falls near a mode-locking window and λ = -0.11
(stable). The fold region is a mixture of chaotic seas and periodic
islands — the same structure as the Hénon map or the standard map
above the last invariant torus.

The sharp statement is: **the fold (non-invertibility) is present at
all K > 1, regardless of the Lyapunov sign.** The fold measure μ
counts the fraction of phase space where f'(θ) < 0 — this is a
geometric fact about the map, not a dynamical one. Chaos is a
consequence of the fold (orbits can merge), but periodic windows
survive within the fold region.

In a physical medium, the fold manifests as **reversed energy flow**:
the coupling is strong enough that the response overshoots the drive,
and energy flows backward (from the response to the source). The
fraction of phase space in the fold region μ(r) predicts the fraction
of energy flow that is reversed at radius r.

---

## Compatibility with D36

### The apparent contradiction

D36 proves: S¹ compact → |r| ≤ 1 → K_eff ≤ 1 → circle map invertible
→ information conserved → fixed point exists. K > 1 means "no physics."

The Stribeck vortex has K(r) > 1 at the core.

### The resolution

D36's constraint is on the **global** effective coupling:

    K_eff = K₀|r|,    |r| = |(1/N) Σ_j e^{iθ_j}| ≤ 1

The order parameter r is a spatial average over all oscillators —
those at the K > 1 core and those at the K < 1 exterior. The global
|r| remains bounded by 1 because it is the mean of unit vectors on
S¹, regardless of local coupling strength.

**Proposition.** A spatially varying coupling K(r) with K(r) > 1 on a
bounded region Ω_core and K(r) < 1 on the complement is compatible
with the global self-consistency condition K_eff ≤ 1 provided:

    K_eff = K₀ × |∫ ρ(r) e^{iθ(r)} d³r / ∫ ρ(r) d³r| ≤ 1

This holds by the triangle inequality on S¹ for any density ρ(r) ≥ 0
and any phase field θ(r). The bound is topological (compactness of S¹)
and does not depend on the local coupling profile.

**Proof.** The quantity inside |·| is a convex combination of points on
S¹ (unit vectors e^{iθ}). A convex combination of points on S¹ lies in
the closed unit disk D². Therefore |r| ≤ 1. Therefore K_eff = K₀|r| ≤ 1
when K₀ = 1 (critical coupling). The bound holds regardless of the local
K(r) profile. □

### The physical interpretation

D36 says: "the universe prevents matter creation not by force but by the
requirement that it remain computable." The Stribeck vortex says: the
universe can have locally non-computable regions (the fold core) as long
as the global computation converges. The K = 1 surface at r_c is the
boundary of local computability — inside it, the circle map folds and
local information is destroyed. Outside it, mode-locking and forward
energy flow persist. The global fixed point survives because it depends
on the spatial integral, not the local value.

This is why the analogy to black holes is structural, not metaphorical:

| General relativity | Stribeck vortex |
|---|---|
| Schwarzschild radius r_s | Critical radius r_c |
| Curvature diverges at r = 0 | K(0) = K_stat > 1 (fold maximal) |
| Horizon at r = r_s | K = 1 surface at r = r_c |
| Exterior: geodesics well-defined | Exterior: mode-locked, forward flow |
| Interior: geodesic incompleteness | Interior: non-invertible, reversed flow |
| Global spacetime well-defined (Penrose) | Global K_eff ≤ 1 (triangle inequality) |
| Information paradox | Fold measure μ: where does the information go? |

---

## Computation

### Parameters

    K_stat = 1.8       (static coupling, overcritical)
    K_kin  = 0.3       (kinetic coupling, subcritical)
    v_thr  = 1.0       (Stribeck threshold velocity)
    λ      = 1.0       (wavelength)
    r_core = λ/(2π) = 0.1592

### Results: critical radius vs topological charge

| ℓ | r_c,inner / r_core | r_c,outer / r_core | product / r_core² |
|---|---|---|---|
| 1 | 0.1417 | 7.055 | 1.0000 |
| 2 | 0.0698 | 14.32 | 1.0000 |
| 5 | 0.0278 | 35.96 | 1.0000 |
| 8 | 0.0174 | 57.56 | 1.0000 |
| 13 | 0.0107 | 93.55 | 1.0000 |

The product r_c,inner × r_c,outer = r_core² (Vieta) is confirmed to
6+ digits across all ℓ. This is exact and parameter-independent. The
inner crossing scales as 1/ℓ and the outer as ℓ — both are limiting
cases of the same quadratic.

### Lyapunov exponent

At Ω = 1/φ (golden mean):

    K > 1: λ generically positive (chaotic), but mode-locking
           windows persist with λ < 0 (periodic islands)
    K = 1: λ = 0 (marginal, the map is a homeomorphism)
    K < 1: λ ≤ 0 (stable, mode-locked or quasiperiodic)

The K = 1 surface at r_c is where the fold disappears. Below K = 1,
the map is invertible (D36) and no positive Lyapunov is possible.
Above K = 1, the fold enables chaos generically but does not
guarantee it at every parameter value.

---

## Structural predictions

These hold for any Stribeck parameters with K_stat > 1:

1. **The overcritical region is centered on the vortex core** (v = 0,
   K maximal). This is where reversed energy flow lives.

2. **The extent of reversed flow shrinks monotonically with ℓ.** Higher
   topological charge → faster core velocity → narrower overcritical
   region. The scaling is r_c ~ 1/ℓ.

3. **The fold measure peaks at the center and decays to zero at r_c.**
   The decay follows μ ~ √(2(K-1))/π near the boundary (saddle-node
   scaling).

4. **The subcritical annulus widens with ℓ.** The inner crossing
   shrinks as 1/ℓ and the outer crossing grows as ℓ. In finite
   physical systems, the outer K > 1 return may fall outside the
   medium, making the exterior effectively subcritical.

5. **The fold disappears at r_c.** The critical radius is
   simultaneously the regime boundary (coupling), the invertibility
   boundary (fold measure goes to zero), and the energy-flow boundary
   (observables). Chaos is generically present but not uniform inside
   r_c — mode-locking windows persist above K = 1.

---

## The Bragg-circle map identification

### Transfer matrix = circle map iteration

The coupled-mode equations for a 1D Bragg grating with coupling κ
and detuning δ give a transfer matrix M per period Λ. Iterating M^N
(cascading N grating periods) is structurally identical to iterating
the circle map N times:

    Ω ↔ δΛ/π    (normalized detuning)
    K ↔ sec(κΛ) = 1/cos(κΛ)    (normalized coupling)
    θ_n ↔ arg(transmission after n periods)

### Stop band = fold = reversed energy flow

The stop band (where the transfer matrix eigenvalue is real > 1,
the backward wave B grows exponentially, and energy flow |A|² - |B|²
reverses) occupies fraction κΛ/π of the Brillouin zone.

With K = sec(κΛ):

    stop band fraction = κΛ/π = arccos(1/K)/π = μ (fold measure)

This equality is **exact** — verified numerically to 4 decimal places
across κΛ ∈ [0.1, 1.5] (bragg_circle_map.py, Part 3).

**The fold measure μ IS the reversed-energy-flow fraction.** The
identification is not conjectural — it follows from the equivalence
between the circle map fold (f'(θ) < 0) and the Bragg stop band
(eigenvalues real, |B| > |A|). Both count the same fraction of
phase space.

---

## Application: 2D photonic crystals

### The K-mapping

For a 2D hexagonal photonic crystal (arXiv:2601.21704), the 1D Bragg
result extends via the three equivalent Bragg directions {G₁, G₂, G₃}:

    K_stat = 1 + 2(Δn)²(1 + f π/√3)

The coefficient 2(Δn)² comes from the step-index Fourier coefficient
(stronger than the sinusoidal sec expansion by factor ~16/π² due to
the sharp index profile). The geometric factor (1 + f π/√3) comes
from the hexagonal unit cell: the area ratio A_hex/A_circle = π/√3
weights the coherent sum of three Bragg directions.

    K_kin = f(Δn)²

Forward-scattering limit: at high velocity, only single-scattering
contributes. Subcritical by construction.

    v_thr = 1/(n_eff Q)

Coherent response bandwidth of the crystal mode.

### Velocity field with Bessel modulation

The azimuthal Poynting-vector velocity in a photonic crystal includes a
Bessel lattice modulation:

    v(r) = v_LG(r) [1 - α J₀(G₁ r)]

where G₁ is the first reciprocal lattice vector and α is the modulation
depth (set by the filling fraction f).

### Numerical result

At Δn = 0.5, f = 0.15, Q = 50:

    K_stat = 1.636
    μ(0) = 0.291    (29.1% reversed energy flow at core)

### Remaining

Extract Δn, f, Q from Pryamikov's specific geometry (Figs. 3-5 of
arXiv:2601.21704) and compare the predicted r_c to the observed
spatial extent of reversed Poynting vector flow.

---

## The gravity sector: complementarity, not analogy

The Schwarzschild K(r) profile (schwarzschild_K_profile.py) reveals
that the gravity sector has the **inverse** structure of the Stribeck
vortex:

| | Stribeck vortex | Schwarzschild |
|---|---|---|
| Core/horizon | K > 1, fold, reversed flow | K → 0, fully unlocked, quantum |
| K = 1 surface | Critical radius r_c | Asymptotic infinity |
| Exterior | K < 1, mode-locked | K < 1 everywhere (D36 absolute) |

The D12 dictionary gives K_eff = K₀N = K₀√(1-2M/r), which goes to
zero at the horizon and 1 at infinity. The horizon is a **decoherence**
boundary (zero synchronization), not an overcritical boundary. D36's
prohibition K_eff ≤ 1 is absolute in the gravity sector.

The K > 1 regime exists only in **material** systems where coupling is
set by velocity-dependent friction (Stribeck), not by the lapse. The
photonic crystal and the black hole occupy opposite ends of the same
coupling landscape: one is overcoupled at rest, the other is
uncoupled at the horizon.

---

## Connection to existing derivations

| Derivation | Connection |
|---|---|
| D12 (continuum limits) | K(x,x') = G_γ(x,x') is spatially varying. The Stribeck vortex is the first explicit K(r) profile with K > 1 core. In the gravity sector, K_eff = √(1-2M/r) — complementary structure (K → 0 at horizon, not K → ∞). |
| D30 (denomination boundary) | The K*(q) values (all > 1) are denomination switches that live inside the vortex core. The core is the denomination-boundary laboratory. |
| D31 (speed of light) | D31 argued K > 1 "if it existed" would degrade coherence. The vortex shows where it exists: at the core of any vortex with K_stat > 1. The c = maximum speed result holds in the K < 1 exterior. |
| D36 (conservation = computability) | Reconciled: K > 1 locally is compatible with K_eff ≤ 1 globally. The fold is local information destruction; global information is conserved by the triangle inequality on S¹. |

---

## What remains

| Component | Status | Gap |
|-----------|--------|-----|
| Regime map K(r) | **Derived** (composition of known profiles) | — |
| Critical radius r_c | **Derived** (exact quadratic, Vieta) | — |
| 1/ℓ and ℓ scaling | **Derived** (limiting cases of quadratic) | — |
| r_c,inner × r_c,outer = r_core² | **Proved** (Vieta, parameter-independent) | — |
| Fold measure μ(r) | **Derived** (exact) | — |
| Fold structure at K > 1 | **Confirmed** (fold present; chaos generic but not uniform — mode-locking windows persist) | — |
| Local vs global K compatibility | **Proved** (triangle inequality) | — |
| Photonic crystal K-mapping | **Computed** | Validate against Pryamikov data |
| Reversed energy flow = fold measure | **Derived** (Bragg stop band = fold, bragg_circle_map.py) | — |
| K = sec(κΛ) identification | **Derived and verified** (exact to 4 digits, bragg_circle_map.py) | — |
| Gravity sector K(r) profile | **Computed** (schwarzschild_K_profile.py) | Stribeck and Schwarzschild have COMPLEMENTARY structures (see below) |
| Information fate in fold core | Open | Black hole information analogue: does the global fixed point encode local fold data? |

---

## Proof chains

This derivation extends all three proof chains:

- [**Proof A: Polynomial → General Relativity**](PROOF_A_gravity.md) — the gravity sector has K_eff = √(1-2M/r) ≤ 1 everywhere: D36 is absolute. The horizon is a decoherence boundary (K → 0), not an overcritical one. Stribeck vortex structure is complementary, not analogous.
- [**Proof B: Polynomial → Quantum Mechanics**](PROOF_B_quantum.md) — the K < 1 exterior is the quantum regime; the vortex provides the spatial boundary condition.
- [**Proof C: The Bridge**](https://github.com/nickjoven/proslambenomenos/blob/main/PROOF_C_bridge.md) — the local/global K distinction reconciles D36's "K > 1 = no physics" with physically realizable vortex systems.
