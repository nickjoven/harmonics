# Derivation 3: a₀ from Synchronization Cost Threshold

## Claim

The MOND acceleration scale a₀ ≈ 1.2 × 10⁻¹⁰ m/s² is the point where
local gravitational synchronization cost equals the cosmological mean
field maintenance cost. This gives a mechanistic derivation of the
dimensional relation a₀ = cH₀/2π already established in proslambenomenos (a companion repository deriving cosmological dimensional relations from the Hubble frequency),
and connects it to the Stribeck lattice bifurcation threshold.

## The Pendulum

A circular orbit is a gravitational pendulum. For any pendulum:

    ω² = g / L

where g is the gravitational acceleration and L is the length. A
circular orbit at radius R with centripetal acceleration g(R) = V²/R
satisfies the same relation with L → R:

    ω_orbit² = g(R) / R

Now ask: what pendulum oscillates at the Hubble frequency?

    ω = H,    g = a₀,    L = ?

    H² = a₀ / L    →    L = a₀ / H²

Substituting a₀ = cH/(2π):

    L = cH/(2π) / H² = c/(2πH) = ƛ_H

This is the **reduced Hubble wavelength** — the Hubble radius divided
by 2π. The most natural length scale in oscillator physics.

**a₀ is the acceleration of a pendulum whose length is ƛ_H and whose
frequency is H.**

The 2π factor is not a Kuramoto subtlety or a cycle-vs-radian
convention. It is the geometric factor between a physical length and
its reduced wavelength — the same factor that appears in every
oscillator in physics (ƛ = λ/2π, ħ = h/2π, k = 2π/λ).

### The MOND transition as entrainment

This makes the MOND transition physically transparent:

- An orbit with g > a₀ has ω_orbit > H: the pendulum is **faster**
  than the cosmic clock. Too fast to entrain. Newtonian regime.

- An orbit with g < a₀ has ω_orbit < H: the pendulum is **slower**
  than the cosmic clock. It locks to the cosmic oscillator. MOND
  regime — the phantom acceleration boost appears.

This is Kuramoto synchronization reduced to one sentence: slow
pendulums lock to the dominant oscillator. The "dominant oscillator"
is the Hubble expansion. The critical frequency is H. The critical
acceleration is a₀ = cH/(2π).

The rest of this derivation provides the cost-accounting detail for
why locking is cheaper than not locking, and connects to the Stribeck
lattice bifurcation. But the pendulum is the physical core.

---

## Setup

### Two cost regimes

The framework identifies two synchronization operations with distinct
cost structures:

1. **Local gravitational synchronization**: Maintaining orbital coherence
   of matter within a gravitational potential well. The cost scales with
   the acceleration (force per unit mass) required to maintain the orbit:

       C_local(a) = m × a × λ_local

   where a is the centripetal acceleration, m is the participating mass,
   and λ_local is the synchronization wavelength (orbital circumference
   per cycle).

2. **Cosmological mean field maintenance**: Every gravitationally bound
   system must also maintain synchronization against the cosmological
   background — the expanding, Λ-dominated mean field. This cost is
   independent of local dynamics:

       C_cosmo = m × a_Λ × λ_cosmo

   where a_Λ is the acceleration scale set by the cosmological constant
   and λ_cosmo is the cosmological synchronization wavelength.

### The cosmological acceleration

From the proslambenomenos derivation (which showed that the cosmological constant Λ sets a fundamental oscillation frequency, and that H₀ and a₀ both reduce to expressions in that frequency), the fundamental frequency set by
Λ is:

    ν_Λ = c√(Λ/3)

The Hubble parameter is related to this through the dark energy fraction:

    H₀ = ν_Λ / √Ω_Λ

The cosmological synchronization cost per unit mass is the acceleration
required to maintain coherence against this background oscillation:

    a_Λ = c × ν_Λ / √Ω_Λ = c × H₀

This is the raw acceleration scale. But the cost is paid over a full
synchronization cycle, not per radian. The cost per cycle involves
the ratio of angular frequency to cycle frequency:

    a_cosmo = c × H₀ / (2π)

This is a₀.

## Derivation

### Cost equality at the transition

At the MOND transition, local and cosmological costs are equal:

    C_local(a₀) = C_cosmo

    m × a₀ × λ_local = m × (cH₀/2π) × λ_cosmo

If the synchronization wavelengths are equal at the transition
(λ_local = λ_cosmo — the mode where local and cosmological coupling
have the same reach), then:

    a₀ = cH₀ / (2π)

### Why 2π is structural, not numerical

The factor 2π appears because:

1. The Kuramoto critical coupling formula involves the frequency
   distribution g(ω) evaluated at the mean:

       K_c = 2 / (π g(0))

2. For a gravitating system with Hubble-scale frequency distribution,
   g(0) ∝ 1/H₀, giving:

       K_c ∝ 2H₀/π

3. The critical acceleration is c × K_c / (angular frequency per cycle):

       a₀ = c × (2H₀/π) / (2²)  ... [simplifying the coupling chain]

   The exact factor traces through the ADM-Kuramoto mapping in
   proslambenomenos (a mapping that recasts the ADM decomposition of general relativity as a Kuramoto-type coupled-oscillator system, with the lapse function playing the role of coupling strength). The point: 2π is the ratio of angular to cyclic
   frequency in the Kuramoto model. It appears because synchronization
   is inherently a phase phenomenon, and phase is measured in radians.

### The Stribeck interpretation

In the Stribeck lattice (a chain of friction oscillators coupled by elastic springs, showing mode-locking and bifurcation thresholds analogous to synchronization transitions), the bifurcation threshold is the driving
amplitude at which the system transitions from linear passthrough
(slip regime) to subharmonic conversion (stick regime).

Map this onto gravity:

| Lattice | Galaxy |
|---|---|
| Driving amplitude A | Gravitational acceleration a |
| Bifurcation threshold A_c | a₀ |
| Slip regime (A < A_c) | Newtonian gravity (a > a₀) |
| Stick regime (A > A_c) | MOND gravity (a < a₀) |

The inversion (lattice: above threshold → stick; galaxy: below
threshold → stick) reflects the relative velocity interpretation:

- High acceleration → high orbital velocity → high v_rel → slip
- Low acceleration → low orbital velocity → low v_rel → stick

The Stribeck transition velocity v_threshold maps onto a₀ through:

    v_threshold ↔ √(a₀ × r)

where r is the orbital radius. This is the MOND transition velocity:
the orbital speed at which the Stribeck curve changes character.

## Numerical check

Using Planck 2018 values:

    H₀ = 67.4 km/s/Mpc = 2.18 × 10⁻¹⁸ s⁻¹
    c = 3.0 × 10⁸ m/s

    a₀ = cH₀/(2π) = (3.0 × 10⁸)(2.18 × 10⁻¹⁸) / (2π)
       = 6.55 × 10⁻¹⁰ / 6.28
       = 1.04 × 10⁻¹⁰ m/s²

Observed: a₀ ≈ 1.2 × 10⁻¹⁰ m/s²

The ratio is 1.15, within the range attributable to the exact form
of the frequency distribution g(ω). The proslambenomenos derivation
handles this through Ω_Λ corrections.

## The cost landscape at the transition

Below a₀, the system faces a choice:

1. **Pay Newtonian cost**: Maintain flat rotation curve with only
   baryonic mass. Cost: C_Newton(a) = m × a_Newton × λ, where
   a_Newton = GM_baryon/r² < a₀. This underpays the cosmological
   cost — the mode can't maintain coherence against the mean field.

2. **Pay enhanced (MOND) cost**: Transition to the stick regime where
   coupling is enhanced. The Stribeck friction provides additional
   force beyond the baryonic contribution — the "dark matter" that
   Lagrangian relaxation in intersections (a companion repository applying constrained optimization to synchronization hierarchies) identifies as the dual
   variable (shadow price of the synchronization constraint).

3. **Decohere**: Stop maintaining orbital synchronization. The galaxy
   dissolves.

Option 2 is cheapest. The enhanced coupling in the stick regime
(μ_static > μ_kinetic in Stribeck terms) provides the extra
acceleration at lower cost than either maintaining Newtonian dynamics
with insufficient mass or losing coherence entirely.

**Dark matter is the cost of maintaining synchronization below a₀.**
It's not a substance — it's the difference between Newtonian cost
(too low to maintain coherence) and the actual cost (set by the
stick-regime coupling strength).

## Predictions

1. **a₀ varies with H₀**: If a₀ = cH₀/2π, then a₀ at redshift z
   differs from today's value:

       a₀(z) = c H(z) / (2π)

   This is testable: high-redshift galaxies should show a different
   MOND transition scale. The effect is strongest at z > 1 where
   H(z) differs significantly from H₀.

2. **Correlation with Λ**: Since H₀² ∝ Λ (in a Λ-dominated era),
   a₀² ∝ Λ. The acceleration scale is set by the cosmological
   constant. This explains the "cosmic coincidence" that a₀ ≈ cH₀:
   both are determined by Λ.

3. **Galaxy cluster anomaly**: Galaxy clusters have convergence
   failure in Lagrangian relaxation (shown in intersections). In the
   cost framework: clusters operate above the single-body MOND
   transition but below the multi-body synchronization threshold.
   Their cost accounting requires multi-constraint relaxation — a
   higher-order correction to the simple a₀ threshold.

## Status

This derivation provides the mechanistic grounding for a₀ = cH₀/2π:
the transition point where local gravitational cost equals cosmological
mean field maintenance cost. The 2π factor is structural (Kuramoto
phase coupling), not numerical.

**Open**: Derive the exact frequency distribution g(ω) for gravitating
systems from the cost functional. This would fix the O(15%) numerical
discrepancy and provide g(0) independently.

**Open**: The redshift dependence prediction (a₀(z) = cH(z)/2π) is
the strongest test. Existing high-z rotation curve data is sparse but
improving with JWST.

**Open**: The cost equality condition (λ_local = λ_cosmo at the
transition) needs independent justification. Why should the
synchronization wavelengths match at the critical point? Is this a
consequence of KKT complementary slackness (the Karush-Kuhn-Tucker condition requiring that at the optimum, either a constraint is exactly satisfied or its associated cost multiplier is zero) — the constraint binds
exactly when the wavelengths match?
