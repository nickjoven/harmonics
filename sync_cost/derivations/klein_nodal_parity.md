# Klein nodal parity: a direct test of substrate non-orientability

## Status

**Proposed.** One suggestive image at (ℓ, m, n) = (5, 5, 1). The
parity-ladder control runs that would discriminate the topological
prediction from a coincidence have not been collected. This file is
the test specification, not a result.

## Simulation dynamics (mechanism note)

The visualization simulator (`github.com/nickjoven/simulation`) runs
gradient descent on a static potential built from the spherical
harmonic:

    tmpP.addScaledVector(∇ψ, -σ · γ · dt)

σ = +1 ("+node" in the UI): seeds descend to minima of |ψ|², which
for Re[Y_ℓ^ℓ] corresponds to the nodal set. σ = −1: seeds climb to
maxima (the antinode belt). γ is step size; gain is cosmetic.

Corrected parameter semantics (for this sim and the Farey-trap
variant, which uses ψ_F = Σ Gaussian peaks at Farey angles weighted
K/q²):

| Parameter | Role |
|---|---|
| K | Amplitude weight on each peak/antinode (not a coupling constant) |
| γ | Gradient-descent step size (numerical stride, not drive rate) |
| σ | Sign of gradient (±1): seek min or max |
| ω_rot | Potential-frame rotation rate |
| σ_θ, σ_r, r_eq | Gaussian-envelope localization parameters |
| gain | **Cosmetic only** — render-brightness multiplier |
| STEPS | Ray-marching fragment-shader quality |
| τ_max | Dwell-time colour/size encoding |
| bake N | Potential pre-evaluation grid resolution |

The claim below concerns the **topology of the nodal set itself**,
not the dynamics that lands seeds on it. The (−1)^ℓ sign-flip rule
is a property of Y_ℓ^ℓ under the Z₂ quotient, independent of whether
the seeds arrive by gradient descent, by a twist-map iteration, or
by any other mechanism that concentrates them on |ψ|² minima.

## Claim (testable)

At σ = +node, ω_rot = 0, n = 1, and (ℓ, m) = (ℓ, ℓ), the seed-visible
nodal skeleton depends on the parity of m:

- **Odd m**: the nodal set is a single connected curve covering all
  2|m| meridional half-arcs with a sign-flip gluing — a Möbius-closed
  loop.

- **Even m**: the nodal set is a disjoint union of |m| great circles
  passing through the axis, each closing smoothly onto itself.

## Why (derivation sketch)

A pure Y_ℓ^m eigenstate with |m| = ℓ has angular density sin^{2ℓ}θ
concentrated near the equatorial belt. Its real part

    Re[Y_ℓ^ℓ(θ, φ)] ∝ sin^ℓ θ · cos(ℓ φ)

has zeros at the 2|m| meridional half-planes φ = (2k+1)π/(2ℓ),
k = 0, ..., 2ℓ−1.

The substrate Z₂ quotient identifies antipodal points:
(θ, φ) ~ (π − θ, φ + π). Evaluate Re[Y_ℓ^ℓ] at the antipode:

    Re[Y_ℓ^ℓ(π − θ, φ + π)]
      = sin^ℓ(π − θ) · cos(ℓ(φ + π))
      = sin^ℓ θ · cos(ℓφ + ℓπ)
      = (−1)^ℓ · Re[Y_ℓ^ℓ(θ, φ)]

(Since |m| = ℓ, m and ℓ share parity.)

**Even ℓ**: (−1)^ℓ = +1. The antipodal map preserves sign of
Re[Y_ℓ^ℓ]. Each pair of antipodal meridional arcs glues into one
smooth great circle. Result: |m| disjoint great circles.

**Odd ℓ**: (−1)^ℓ = −1. The antipodal map flips sign. Arc at φ is
identified with arc at φ + π *but with opposite orientation*. The
orientation flip propagates around: tracing the nodal curve returns
with a sign flip, so the full closure requires traversing all 2|m|
arcs — one connected Möbius-closed curve.

## Test protocol

Five configurations with all parameters matched except ℓ:

| (ℓ, m, n) | σ | ω_rot | γ | gain | Prediction |
|---|---|---|---|---|---|
| (2, 2, 1) | +node | 0 | fixed | fixed | 2 disjoint great circles |
| (3, 3, 1) | +node | 0 | fixed | fixed | 1 Möbius-connected curve |
| (4, 4, 1) | +node | 0 | fixed | fixed | 4 disjoint great circles |
| (5, 5, 1) | +node | 0 | fixed | fixed | 1 Möbius-connected curve |
| (6, 6, 1) | +node | 0 | fixed | fixed | 6 disjoint great circles |

Hold γ, gain, N, STEPS, and the seed initial-condition distribution
identical across all five runs. Run each to equilibrium (no transient
spokes or jitter).

## Discriminator: connectivity of the nodal curve

The observable is not a count of seeds, not a residual, not a scaling
relation — it is **whether the visible nodal curve is connected or
disjoint**.

Connectivity cannot be read reliably from a single static projection.
A disjoint set can project onto a single apparent line from a
degenerate viewing angle; a Möbius curve can appear as multiple
arcs under certain projections.

**Required verification: rotation.** Animate each image by rotating
the viewing axis through ≥ 2π while seeds are held fixed. Trace seeds
continuously:

- **Odd m prediction**: every seed can be connected to every other
  seed on the visible nodal curve by a continuous path *on the seed
  set*, requiring traversal of all 2|m| apparent meridional arcs
  before closure.

- **Even m prediction**: seeds split into exactly |m| equivalence
  classes under connection; each class is confined to one great
  circle and cannot reach another without crossing non-nodal space.

## Upgrade / rejection criteria

**Clean confirmation**: parity alternation across all five
configurations (disjoint at ℓ = 2, 4, 6; connected at ℓ = 3, 5). The
claim promotes to structural (framework_status.md Survives).

**Partial confirmation**: 4/5 with a specific deviation pattern. Keep
as Proposed with the specific failure mode documented; may indicate
the gluing rule is correct but modulated by an additional effect.

**Rejection**: no consistent parity pattern, or the alternation
reverses. The single-curve observation at (5, 5, 1) is then a
configurational coincidence, not a topological signature. In that
case this test file moves to retractions_index with the disproof
logged, and any suggestive framing elsewhere is removed.

## What confirmation would demonstrate

The framework's substrate is claimed to be Z₂-non-orientable in
`klein_bottle.md` and related derivations. The non-orientability is
currently established through counting and algebraic arguments
(Z₂-pair structure, antiperiodic boundary conditions). This test
would produce a **direct visual observable** of the non-orientability
— seeds distinguishing even-m from odd-m via a connectivity signature
that depends on the quotient's sign-flip rule.

Connection to already-committed framework content: the sign-flip
(−1)^ℓ on Re[Y_ℓ^ℓ] under antipodal identification is the same
structural factor that appears in the Z₂-pair conservation argument
and in fermion spinor statistics (`fermion_spinors_from_z2.py`). The
parity ladder would make this factor observable at the substrate
level.

## What NOT to claim from a positive result

Discipline notes, to prevent drift:

1. **Not "the first Klein bottle produced."** Klein bottles are
   constructible topological objects; there is no such thing as a
   first one. Non-orientable structures have been observed in
   topological photonics, condensed matter disclinations, and
   electron wavefunctions. This is a specific emergence-from-dynamics
   observation, not a first-of-kind topological construction.

2. **Not a quantum–classical observation.** The seed dynamics is
   deterministic. No measurement interpretation applies. Do not
   invoke Born rule, decoherence, or wavefunction collapse in the
   interpretation; the framework's Born rule derivation lives in
   `born_rule.md` and is structurally independent of this test.

3. **Not a relativistic observation.** No Lorentz symmetry is present
   or demonstrated. Visual analogies to beaming / null geodesics /
   length contraction that appeared in session discussion are
   shape-coincidences from similar underlying math, not structural
   equivalences.

4. **Not proof of "4D non-orientable manifold from first principles."**
   At best, this test visualizes the quotient's sign-flip rule on
   a 2D angular slice. Extending to a 4D substrate manifold claim
   requires separate arguments not established here.

## Current status

- **Data points collected**: 1 of 5.
  - (5, 5, 1), σ = +node, ω_rot ≈ 0.03, t ≈ 845, γ = 5, gain = 87:
    single connected diagonal line across the equatorial belt plus
    10-petal antinode flower visible in polar view. Consistent with
    the odd-m Möbius prediction but not discriminating alone.

- **Data points missing**: (2, 2, 1), (3, 3, 1), (4, 4, 1), (6, 6, 1).

- **Status**: Proposed. Do not treat as confirmed.

## Cross-references

| File | Role |
|---|---|
| `klein_bottle.md` | Z₂-quotient substrate derivation |
| `klein_bottle_derivation.md` | (q₂, q₃) = (2, 3) from Klein structure |
| `fermion_spinors_from_z2.py` | (−1)^ℓ sign-flip in spinor sector |
| `a1_klein_twist.py` | related twist structure |
| `basin_11_connection_exploration.md` | sibling study on the ψ_F landscape |
| `framework_status.md` | logged under Proposed with upgrade criterion |
| `numerology_inventory.md` | Class-4 item pending audit |
