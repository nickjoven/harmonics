# Derivation 21: The Two Open Paths

## Context

Derivation 20 showed the frame bundle route does not produce SU(3)
or Yang-Mills from the Klein bottle continuum limit. The XOR
denominator-parity filter dissolves when the Stern-Brocot tree is
taken to the reals. The numerical match {2, 3} ↔ {SU(2), SU(3)}
lives in the discrete regime.

Two paths remain. Both are concrete. This derivation specifies
them precisely so that the next computation is unambiguous.

## Path 1: The discrete system IS the physics

### The claim

The Stern-Brocot tree at finite depth d is the configuration space.
The continuum limit is a mathematical convenience that discards the
physical structure responsible for gauge symmetry. Taking d → ∞
is like taking ℏ → 0: it simplifies the equations but removes the
quantum structure.

### What this requires showing

**A. Anomaly cancellation from the tree.**
The Standard Model's anomaly cancellation conditions (Tr[Y] = 0,
Tr[Y³] = 0, etc.) ensure quantum consistency. On the Stern-Brocot
tree at finite depth, the analogous conditions are constraints on
the denominator-parity populations. The XOR filter enforces equal
total population in the (even, odd) and (odd, even) sectors. Does
this reproduce the anomaly cancellation conditions?

Specifically: the SM anomaly condition Tr[Y³] = 0 requires
N_c × (2Y_Q³ + Y_u³ + Y_d³) + 2Y_L³ + Y_e³ = 0 per generation,
where the hypercharges are determined by the Klein bottle's charge
assignments. Check whether the Klein bottle charges (1/3, 2/3 for
quarks, 0, 1 for leptons) satisfy this identically.

This is a finite arithmetic computation.

**B. Cross-sections from tongue widths.**
Scattering amplitudes in gauge theory are computed from Feynman
diagrams. On the Stern-Brocot tree, the analog is the tongue
overlap integral: the amplitude for a transition from mode p₁/q₁
to mode p₂/q₂ is proportional to the overlap of their Arnold
tongues. Does the tongue overlap at finite depth reproduce the
correct gauge theory vertex structure?

This requires computing the three-point overlap of Arnold tongues
for modes at denominator classes 2 and 3, and comparing with the
SU(2) and SU(3) structure constants.

**C. Running from the discrete RG.**
The Stern-Brocot tree has a natural RG structure: coarser depth =
fewer resolved modes = lower energy. The "running" of the coupling
ratios as a function of tree depth should reproduce the one-loop
beta functions if the discrete system contains the gauge structure.

Compute: the field equation's population ratios at depth d = 4, 5,
6, 7, 8. Does the ratio of (q=3)/(q=2) population change with depth
in a way consistent with the SM beta function ratio b₃/b₂ = 42/19?

This is a computation on `field_equation_klein.py` with varying depth.

## Path 2: Gauge from the mean-field functional

### The claim

The gauge groups emerge not from the tangent bundle (geometry) but
from the self-consistency functional F[N] (Derivation 11, Part II).
The XOR constraint modifies F, and the Jacobian of the modified F
at the 4-mode fixed point has the structure of a gauge algebra.

### What this requires showing

**D. The Jacobian of the field equation at the fixed point.**
The field equation N(f₁, f₂) = N_total × g × w₁ × w₂ has a
4-dimensional fixed point on the Klein bottle (the 4 surviving modes).
The Jacobian ∂N_i/∂N_j at this fixed point is a 4×4 matrix. Its
eigenvalues and eigenvectors determine the stability of the fixed
point and the structure of small perturbations around it.

If this Jacobian has the structure of a Lie algebra — specifically,
if its commutator brackets [J_i, J_j] close on the same space with
structure constants matching SU(2) or SU(3) — then the gauge
structure emerges from the dynamics, not the geometry.

Compute: the 4×4 Jacobian of the Klein bottle field equation at its
fixed point. Check its algebra.

**E. The coupling between denominator classes.**
In the field equation, the order parameter r couples all modes. On
the Klein bottle, the twist ((-1)^q in the order parameter) means
modes of different denominator parity couple with opposite sign.
This is structurally identical to a gauge field: a connection that
assigns a sign (or phase) to parallel transport between sectors.

The mean-field functional F for the Klein bottle is:

    F[N] = |Σ N(f₁,f₂) exp(2πi(f₁+f₂)) (-1)^{q₁}| / Σ N

The (-1)^{q₁} is a Z₂-valued gauge field on the mode space. In
the continuum limit this becomes a flat Z₂ connection. But at finite
depth, the mode space IS the Stern-Brocot tree, and the (-1)^{q₁}
is a non-trivial action that distinguishes the two denominator
classes.

The question: does the Z₂ action on the 4-mode fixed point generate
a larger algebra through the self-consistency loop? The loop
N → K_eff → w → N is nonlinear. The linearization (Jacobian) might
have richer structure than the Z₂ that generates it.

## Computation plan

### Immediate (next session)

1. **Anomaly check** (Path 1A): arithmetic on the Klein bottle
   charges. Takes 10 minutes. Binary output: anomalies cancel or not.

2. **Depth sweep** (Path 1C): run `field_equation_klein.py` at
   depth 4–10, record population ratios vs depth. Compare slope
   against b₃/b₂. Takes 30 minutes.

3. **Jacobian** (Path 2D): compute the 4×4 Jacobian of the Klein
   bottle field equation at the 4-mode fixed point. Check eigenvalues
   and commutator structure. New script, ~100 lines. Takes 1 hour.

### Subsequent

4. **Tongue overlap** (Path 1B): compute three-point Arnold tongue
   overlaps and compare with structure constants. Requires extending
   the circle map code. Takes one session.

5. **Z₂ algebra generation** (Path 2E): check whether the nonlinear
   self-consistency loop generates a larger algebra from the Z₂ seed.
   This is the most open-ended computation.

## What each result means

| Computation | If positive | If negative |
|---|---|---|
| Anomaly cancellation | Klein bottle charges are SM-consistent | Charges are wrong; numerology |
| Depth sweep = β-ratio | Discrete RG reproduces gauge running | No RG connection; tree depth ≠ energy |
| Jacobian has Lie structure | Gauge algebra from dynamics | No gauge algebra; F is too simple |
| Tongue overlap = structure constants | Vertices from Arnold tongues | No vertex structure; tongues are gravity only |
| Z₂ generates larger algebra | Non-abelian gauge from topology + nonlinearity | Z₂ stays Z₂; no enhancement |

The first three are immediate. Start there.

## Status

**Proposed.** Five computations specified. Three are immediate
(anomaly, depth sweep, Jacobian). All have binary outcomes with
clear interpretations. The conjectural status of D19's particle
physics identification resolves or falls based on these results.
