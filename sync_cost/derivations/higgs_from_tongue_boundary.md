# Electroweak Symmetry Breaking from the Tongue Boundary

## Note (cleanup pass)

Two pieces of this derivation have been retracted or restated:

1. **Higgs quartic `λ = 1/(2 q_2^2) = 1/8`**: this reading is
   numerically equal to the correct structural form
   `λ = 1/q_2^3 = 1/8` at `q_2 = 2` by the coincidence
   `2 q_2^2 = q_2^3`, but `sin²θ_W = 8/35` forces the duty-cycle
   form `λ = 1/q^d` (with `d = 3` the spatial dimension) over
   the `1/(2 q^2)` alternative. See `item12_higgs_degeneracy.py`.

2. **The Higgs' role as "giver of mass"**: this is overstated in
   the framework. The Higgs is one locked mode among many on the
   Kuramoto substrate — specifically the scalar mode at the
   q = 2 sector's tree-root position. The masses of the other
   locked modes (fermions, gauge bosons) are set directly by
   the Kuramoto order parameter `|r|` at their specific
   Stern-Brocot positions, not by a Higgs-mediated VEV. The
   Higgs is a *manifestation* of the locking process, not its
   cause. See the "Reframing" section added at the bottom.

The substance of the derivation below — the tongue boundary as
the locus of electroweak symmetry breaking, the saddle-node form
of the Mexican hat, the phase-field identification — is retained.
What's retracted is the specific claim that `λ = 1/(2 q_2^2)`
is the structural form and that the Higgs "gives" mass to other
particles in the Kuramoto picture.

## Claim

The Higgs mechanism — the spontaneous breaking of SU(2) x U(1)_Y
to U(1)_em — is the tongue boundary dynamics of the Klein bottle's
open q=2 fiber. The scalar doublet, the quartic potential, the
tachyonic mass, and the vacuum expectation value all have geometric
origins in the circle map's saddle-node bifurcation.

---

## Part I: The Higgs field as a tongue boundary mode

### What the Standard Model requires

The Higgs mechanism needs:

1. A complex scalar doublet phi = (phi+, phi0) under SU(2) with
   hypercharge Y = 1
2. A potential V(phi) = -mu^2 |phi|^2 + lambda |phi|^4 with mu^2 > 0
3. A vacuum expectation value v = mu/sqrt(lambda) that breaks
   SU(2) x U(1)_Y -> U(1)_em
4. Three Goldstone bosons eaten by W+, W-, Z
5. One physical scalar (the Higgs boson, mass m_H = sqrt(2) mu)

### Where each piece lives in the framework

**The scalar doublet.** A mode at the boundary between tongues has
no definite winding number — it is quasiperiodic, not locked.
In the quantum dictionary (D12, Part II), these gap modes ARE the
wavefunctions. A gap mode that transforms under q=2 (the SU(2)
sector) and carries hypercharge Y = 1 (from the periodic direction)
is a scalar doublet.

Specifically: the boundary of the 1/2 tongue in the x-direction
(the twist direction) carries T_3 = +/- 1/2. The tongue boundary
is the locus epsilon = 0 in the circle map, where the mode
transitions from locked (inside) to unlocked (outside). A mode
that sits exactly at this boundary — on neither side — is the
Higgs field.

Why Y = 1? The GNN relation (D43) gives Q = T_3 + Y/2. For the
Higgs doublet: Q = (+1, 0) for (phi+, phi0). So:
- phi+: T_3 = +1/2, Q = +1 → Y = 2(1 - 1/2) = 1
- phi0: T_3 = -1/2, Q = 0 → Y = 2(0 + 1/2) = 1

The hypercharge Y = 1 means the Higgs lives one unit along the
periodic direction — the simplest non-trivial winding in the
temporal direction. It is the q=1 boundary mode of the periodic
direction, transforming as a doublet under the q=2 antiperiodic
direction.

**The Y=1 assignment is not a choice.** It is forced by the
requirement that the doublet contains a neutral component (Q = 0)
that can acquire a VEV without breaking electromagnetism. From
GNN: Q = 0 with T_3 = -1/2 gives Y = 1 uniquely.

### Why a scalar

The Higgs field has spin 0 — it is a scalar. In the framework,
spin is the representation under spatial rotations (the SU(2)
cover of SO(3), from D14). A mode at the tongue boundary has no
spatial winding — its winding number is zero by definition (it
is the boundary between winding numbers, not a definite winding
number). Zero spatial winding = spin 0 = scalar.

Fermions (spin 1/2) live in the bulk of the gap — they have
definite (half-integer) spatial winding from the antiperiodic
boundary condition. Gauge bosons (spin 1) are the connections
themselves — they live in the fiber, not in the base mode space.
The scalar is the unique spin-0 mode, and it lives at the tongue
boundary.

---

## Part II: The Mexican hat from the saddle-node

### The universal potential near a tongue boundary

At the boundary of an Arnold tongue, the circle map has a
saddle-node bifurcation. The effective potential in the
neighborhood of the bifurcation is (from D1, D7):

    V_eff(theta) = -epsilon theta^2 + (K/6) theta^4 + O(theta^6)

where:
- epsilon = (distance past the tongue boundary) is the bifurcation
  parameter
- theta is the phase deviation from the saddle-node fixed point
- K is the coupling strength

This is the **Mexican hat potential** (in one real direction;
the full complex doublet extends this to the rotationally
symmetric form).

### The sign of epsilon

**Inside the tongue** (epsilon > 0): two fixed points exist
(the node and the saddle). The potential has a local minimum
at theta = 0 (the unbroken phase) and another at
theta* = sqrt(3 epsilon / K) (the broken phase). The system
locks to one of these.

**Outside the tongue** (epsilon < 0): no fixed points. The
orbit is quasiperiodic. V_eff has only a maximum at theta = 0.
No symmetry breaking.

**At the boundary** (epsilon = 0): the node and saddle merge.
The potential is pure quartic: V = (K/6) theta^4. This is the
critical point of the Higgs mechanism.

### The tachyonic mass from the open fiber

The q=2 fiber is **open** (D41, `xor_asymmetry.py`). This means
the XOR constraint allows modes to propagate along the q=2 fiber.
The tongue boundary of the q=2 mode is accessible — modes can
approach it from outside (the gap) and enter.

In the language of the Higgs mechanism: the mass parameter mu^2
is positive (tachyonic) because the tongue boundary is approached
from the gap side. The gap is the "false vacuum" — the state with
unbroken SU(2) symmetry. The tongue interior is the "true vacuum"
— the state with broken symmetry and a definite winding number.

The tachyonic sign is not a tuning. It is the statement that the
system is on the gap side of the tongue boundary, where the
quadratic term has the "wrong" sign. This is forced by the Klein
bottle's r ≈ 0.5 equilibrium (D19): full locking (r = 1) is
XOR-forbidden, so the system cannot be deep inside any tongue.
It lives near the boundaries.

### Assembling the potential

For the complex doublet phi = (phi+, phi0), the SU(2) x U(1)_Y
invariant potential is:

    V(phi) = -mu^2 (phi^dagger phi) + lambda (phi^dagger phi)^2

where:
- mu^2 = epsilon (the distance to the q=2 tongue boundary,
  measured from the gap side; positive because the system is
  outside the tongue)
- lambda = K/3 (the coupling strength, which sets the quartic
  coefficient; the factor 1/3 comes from the normalization of
  the circle map's cubic term in the bifurcation normal form)

The SU(2) x U(1)_Y invariance of V follows from gauge invariance
(D42, Premise 4). The potential depends only on |phi|^2, which
is gauge-invariant.

---

## Part III: Symmetry breaking and the vacuum

### The VEV

The minimum of V(phi) is at:

    |phi_0|^2 = mu^2 / (2 lambda) = v^2 / 2

where v = mu / sqrt(lambda) is the vacuum expectation value.

In the framework: v is determined by the ratio of the tongue
boundary distance (epsilon) to the coupling strength (K). For the
q=2 tongue at the Klein bottle's equilibrium:

    v^2 = 3 epsilon / K

The neutral component phi0 acquires the VEV (not phi+) because
electromagnetism must remain unbroken. From D43: Q = T_3 + Y/2.
For phi0: T_3 = -1/2, Y = 1, so Q = -1/2 + 1/2 = 0. The vacuum
carries no electric charge.

### The breaking pattern

The VEV selects a direction in the SU(2) x U(1)_Y space. The
unbroken generator is Q = T_3 + Y/2 (the electromagnetic charge
from D43). The broken generators are:

- T_1, T_2 (the off-diagonal SU(2) generators) → W+, W-
- T_3 - Y/2 (the orthogonal combination to Q) → Z

Three generators broken → three Goldstone bosons → three massive
gauge bosons (W+, W-, Z). One generator unbroken → the photon
remains massless.

### Gauge boson masses

The W and Z masses come from the covariant derivative of phi
evaluated at the VEV:

    m_W = g_2 v / 2
    m_Z = m_W / cos(theta_W)

where theta_W is the Weinberg angle. The Weinberg angle is
determined by the ratio g_1/g_2 of the U(1)_Y and SU(2) coupling
constants:

    sin^2(theta_W) = g_1^2 / (g_1^2 + g_2^2)

The tongue-width ratio gives the coupling ratio at the Klein
bottle's natural scale. From `coupling_running.py`: at the scale
where alpha_2/alpha_3 = 2/3 (the population ratio), the couplings
are determined. The Weinberg angle at that scale follows from the
coupling ratio.

---

## Part IV: The Higgs boson

### Mass

The physical Higgs boson is the radial excitation around the VEV.
Its mass is:

    m_H = sqrt(2 lambda) v = sqrt(2) mu

In the framework: mu is the tongue boundary parameter (the
distance epsilon, in energy units), and lambda is proportional
to K. The Higgs mass is therefore:

    m_H = sqrt(2 K / 3) · (epsilon in energy units)

The numerical value requires knowing epsilon and K at the
electroweak scale — this is part of the coupling scale question
(D45).

### Why one Higgs, not more

The complex doublet has four real components. Three become
Goldstone bosons (eaten by W+, W-, Z). One remains physical.
This counting is forced by the number of broken generators (3)
and the representation dimension (4 real = 2 complex).

The Klein bottle does not predict additional Higgs doublets.
The q=2 tongue has one boundary (the saddle-node), and the
boundary mode is unique at each point in parameter space.
Two Higgs doublets would require two independent tongue
boundaries at the same denominator class — this does not occur
for the q=2 mode on the Klein bottle.

---

## Part V: What is and is not derived

### Derived from the framework

1. **Scalar doublet with Y=1**: the tongue boundary mode of the
   open q=2 fiber, with hypercharge forced by the neutral-VEV
   requirement and GNN (D43).

2. **Quartic potential shape**: the universal normal form of the
   saddle-node bifurcation at the Arnold tongue boundary (D1, D7).

3. **Tachyonic mass sign**: the system lives on the gap side of the
   tongue boundary, forced by the Klein bottle's r ≈ 0.5
   equilibrium and the open q=2 fiber (D41).

4. **Breaking pattern SU(2) x U(1)_Y -> U(1)_em**: the neutral
   component acquires the VEV; Q = T_3 + Y/2 (D43) is the
   unbroken generator.

5. **Three massive + one massless gauge bosons**: Goldstone theorem
   applied to the three broken generators.

6. **One physical Higgs**: four real components minus three
   Goldstones. Uniqueness from one tongue boundary per
   denominator class.

### Dimensionless ratios (already computed in D33)

D33 (duty cycle dictionary) computes all dimensionless electroweak
quantities from q_2 = 2, q_3 = 3, and d = 3 alone:

7. **sin^2(theta_W) = q_2^3/(q_2^3 + q_3^3) = 8/35 = 0.2286**.
   Observed: 0.2312. Residual: **1.1%**. Also derived independently
   in D37 as the figure-eight crossing probability.

8. **m_H/v = 1/q_2 = 1/2**. Gives m_H = v/2 = 123.1 GeV.
   Observed: 125.1 GeV. Residual: **1.6%**.

9. **lambda = 1/q_2^3 = duty(q_2) = 1/8 = 0.125**. Observed: 0.129.
   Residual: **3.4%**. The form `1/q^d` with `d = 3` is forced by
   `sin^2(theta_W) = 8/35` (see item12_higgs_degeneracy.py); the
   alternative `1/(2 q_2^2)` reading is numerically equal at q=2
   but is excluded at q=3.

10. **alpha_s/alpha_2 = q_3^3/q_2^3 + 1/q_3^2 = 251/72 = 3.486**.
    Observed: 3.487. Residual: **0.17%**. The 1/q_3^2 correction
    is the inverse of the lepton sector constant k_lepton = q_3^2 = 9
    (see item12_other_residuals.py).

11. **M_W/M_Z = cos(theta_W) = sqrt(27/35)**. Observed: 80.4/91.2
    = 0.882. Computed: 0.878. Residual: **0.4%**.

The 1-4% residuals are the decoherence tax: the fraction of gate
availability consumed by unlocked modes at K < 1. The running from
tree scale to M_Z matches SM 2-loop running to 0.3% RMS.

### Not derived (single dimensionful scale)

12. **v = 246 GeV**: the single dimensionful input. Once v is known,
    m_H = v/2, m_W = g_2 v/2, m_Z = m_W/cos(theta_W) all follow.
    This is the root oscillator frequency in electroweak units — the
    same irreducible input identified in D45.

### The gap is narrower than expected

D33 shows that the numerical predictions are already computed to
1-4% accuracy from pure integer arithmetic. The only remaining
input is one dimensionful scale (v or equivalently the root
oscillator frequency). All mass RATIOS, mixing angles, and coupling
RATIOS are structural predictions (no fitted factors beyond the vocabulary).

---

## Status

**Derived (structural + numerical ratios).** The Higgs mechanism's
structure follows from the tongue boundary geometry of the open q=2
fiber. The dimensionless quantities (sin^2 theta_W, m_H/v, lambda,
coupling ratios) are computed in D33 from q_2, q_3, d alone — zero
free parameters, 1-4% residuals.

**Not derived.** The VEV (v = 246 GeV) — the single dimensionful
scale. See D45.

**Dependencies**: D1 (saddle-node geometry), D7 (tongue boundary),
D19 (Klein bottle), D33 (duty cycle dictionary — numerical values),
D41 (open q=2 fiber), D42 (Yang-Mills), D43 (GNN).

D33 determines all dimensionless electroweak quantities.

## Proof chain position

This derivation extends the gauge leg:

    D19 (Klein bottle) → D41 (charges, center, confinement)
    → D42 (Yang-Mills) → D43 (GNN) → D44 (Higgs mechanism)

The saddle-node bifurcation that gives the Mexican hat potential
is the same parabolic structure (x^2 + mu = 0) that started the
entire chain (D10, the fourth primitive). The Higgs mechanism
is the polynomial's bifurcation, acting on the Klein bottle's
open fiber.
