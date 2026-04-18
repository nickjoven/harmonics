# Gap 2: Spatial Diffusion and the Bare Coupling D₀

## Status

**Break 1 addressed; Break 2 remains open.**

The diffusion term D·∇²θ is forced by two complementary routes:

- **Topological** (`gap2_theorem_attempt.md`): non-orientability →
  no time-reversal → h_KS > 0 → decorrelation → Langevin → D·∇².
  Tensor structure forced by Ad(SL(2,ℝ))-invariance. Coarse-graining
  step (Mori–Zwanzig) is the main open technical piece.

- **Graph-theoretic** (`gap2_step4_farey_laplacian.md`): the
  Stern-Brocot tree tessellates H² = SL(2,ℝ)/SO(2) via Ford circles
  (exact to machine precision). The spatial coupling IS the tree's
  nearest-neighbor structure. Diffusion emerges from the irrational
  (continuum) completion, not from the rational skeleton.

Break 2: the scalar D₀ = ½·λ·ℓ_c² requires one microscopic length
ℓ_c as input — the framework's irreducible Planck-scale dimensionful
input, analogous to ω = √(4πGρ) in gravity. Gravity-parallel closure
standard.

## What is derived

The chain from Kuramoto at K<1 to Schrödinger:

1. **Unlocked oscillators** (K<1): oscillators in gaps between Arnold
   tongues have no definite winding number. They diffuse between modes.
   **Status: derived from circle map dynamics.**

2. **Continuity equation**: conservation of unlocked oscillator density
   rho gives dρ/dt + nabla·(rho v) = 0. **Status: exact.**

3. **Effective potential**: secular averaging over tongue structure gives
   V_eff(x) = omega(x) - p/q - K(x)r/2 (detuning from nearest tongue
   minus coupling pull). **Status: derived from near-resonance averaging.**

4. **Constant effective diffusion**: the Stern-Brocot tree has per-level
   variance sigma^2(d) ~ D_0 / phi^{4d}. The geometric series converges:
   D_eff = D_0 / (1 - phi^{-4}). The CLT over independent RG levels
   produces Gaussian diffusion with constant D_eff. **Status: derived
   from tree self-similarity (phi^4 convergence factor).**

5. **Quantum potential**: with constant D, Nelson's 1966 result applies
   as a theorem. Ito calculus produces the unique correction term
   Q = -(hbar^2/2m) nabla^2 sqrt(rho) / sqrt(rho). **Status: derived
   (universal, Nelson 1966).**

6. **Madelung ↔ Schrödinger**: the continuity + momentum equations with
   quantum pressure are exactly equivalent to ihbar dPsi/dt =
   -(hbar^2/2m) nabla^2 Psi + V_eff Psi. **Status: exact mathematical
   identity (Madelung 1927).**

## What is not derived

### Break 1: Spatial diffusion is assumed

The circle map theta_{n+1} = theta_n + Omega - (K/2pi) sin(2pi theta_n)
is a 0+1 dimensional dynamical system. The step to the spatially extended
Kuramoto equation

    dtheta/dt = omega(x) + D nabla^2 theta + K(x) r sin(psi - theta)

introduces the **diffusive coupling term D nabla^2 theta** by hand. This
term represents nearest-neighbor spatial coupling between oscillators. It
is physically standard for coupled oscillator arrays, but it is not
derived from the circle map or the four primitives (integers, mediant,
fixed point, parabola).

The framework derives d=3 from SL(2,R) and shows what manifold the field
lives on, but does not show why there should be a field at all rather
than a discrete ensemble.

This gap is **shared with Gap 1** (Einstein). Both the gravity and quantum
sectors require the spatialization step: oscillator ensemble → field on
3-manifold. The framework's derivation of d=3 determines the manifold's
dimension and topology but not the promotion of discrete degrees of
freedom to continuous fields.

### Break 2: D₀ is an input parameter

The formula

    hbar = 2m D_0 / (1 - phi^{-4})

has derived structure:
- The phi^{-4} convergence factor comes from the Stern-Brocot tree's
  self-similarity (Fibonacci backbone scaling).
- The (1 - phi^{-4})^{-1} comes from the geometric series over RG levels.
- The form of the quantum potential (nabla^2 sqrt(rho) / sqrt(rho))
  is universal by Nelson/Ito.

But D_0 — the bare diffusion constant at the finest tree level — is an
input. It sets the overall scale of quantum mechanics.

This is the framework's version of "why does hbar have the value it
does?" The ratio hbar/m is identified with the tree geometry through
the phi^4 factor, but the overall dimensionful scale requires one
external input.

## The precise mathematical problem

### For Break 1 (spatialization)

**What needs to be proved**: Starting from the four primitives and the
circle map on S^1, derive the existence of spatial coupling between
oscillators at different positions.

Possible routes:

1. **Coupling kernel as derived object.** If oscillators are indexed by
   their Stern-Brocot addresses (paths in the binary tree), then "nearby"
   oscillators are those sharing a common ancestor at depth d. The tree
   metric defines adjacency. Show that the tree adjacency, in the K→1
   continuum limit, produces a 3-dimensional lattice with nearest-neighbor
   diffusive coupling.

2. **SL(2,R) as configuration space.** The framework derives M = SL(2,R)
   (three_dimensions.md). If the oscillators live on the group manifold
   and interact via the group's invariant metric, then spatial coupling
   D nabla^2 theta is the Laplace-Beltrami operator on M. This would
   derive D from the group geometry, but requires showing that Kuramoto
   dynamics on SL(2,R) naturally produce the Laplacian as the leading
   spatial interaction.

3. **Self-consistency of the field equation.** The rational field equation
   (Derivation 11) is a fixed-point equation on the Stern-Brocot tree.
   In the continuum limit, it becomes the Kuramoto self-consistency
   equation. If this limit necessarily involves spatial correlations
   (because oscillators at nearby frequencies must be at nearby spatial
   positions for the mean field to be well-defined), then spatial
   diffusion emerges from the self-consistency condition.

### For Break 2 (D₀)

**What needs to be proved**: D_0 is determined by the tree geometry alone,
with no external input.

Possible routes:

1. **D_0 from mediant spacing.** At tree depth d, adjacent Farey
   fractions are separated by 1/(q_n q_{n+1}). If D_0 is the natural
   diffusion constant on the Farey graph at the finest resolved level,
   then D_0 = f(q_max) for some function f determined by the graph
   Laplacian. This would make D_0 (and therefore hbar) a function of
   the maximum resolved denominator.

2. **D_0 from the duty cycle.** The duty cycle scales as 1/q^3.
   If the diffusion rate between adjacent modes is proportional to
   the overlap of their Arnold tongues (which decreases as 1/q^3 for
   large q), then D_0 ~ 1/q_max^3. This would give hbar a specific
   dependence on the UV cutoff (Planck scale).

3. **D_0 is irreducible.** Every physical framework requires at least
   one dimensionful parameter to set the scale. In SI units, this is
   the kilogram (or equivalently hbar, c, G — any one suffices given
   the other two). If the framework derives all dimensionless ratios
   from topology and leaves one overall scale undetermined, this may be
   the best possible result. The question then becomes: is D_0 the
   unique irreducible scale, or can it be reduced further?

## Connection to other gaps

- **Gap 1 (Einstein)**: shares the spatialization problem. Both gaps
  would be partially resolved by deriving D nabla^2 from the tree/group
  geometry.
- **Gap 3 (Gauge)**: independent. The gauge gap is about discrete vs.
  continuum structure, not about spatial coupling or scale.
- **Planck scale**: the relationship l_P = sqrt(hbar G / c^3) connects
  D_0 to G. If one is derived, both are constrained.

## References

- continuum_limits.md Part II (K<1 section)
- minimum_alphabet.md §Status/Open
- Nelson, E. (1966). Derivation of the Schrödinger Equation from
  Newtonian Mechanics. Physical Review, 150(4), 1079–1085.
- Madelung, E. (1927). Quantentheorie in hydrodynamischer Form.
  Zeitschrift für Physik, 40(3-4), 322–326.
