# Gap 1: The Christoffel Connection from Kuramoto Ensemble Averages

## Status

**Open.** The weak-gradient ADM evolution equation is derived. The exact
Levi-Civita connection from Kuramoto ensemble averages is not.

## What is derived

At K=1 (critical coupling, full locking), the spatially extended
Kuramoto equation with coherence tensor

    C_ij(x,t) = delta_ij - <partial_i theta  partial_j theta>

produces, after time-differentiation and the ADM dictionary
(r = N, partial_i psi = N_i/N, K_ij = <partial_i theta cos(psi-theta) partial_j theta>):

    partial_t gamma_ij = -2N K_ij + D_i N_j + D_j N_i

This is the first ADM evolution equation. The derivation is valid in the
**weak-gradient regime** where partial_i theta is small and nonlinear
terms in the ensemble averages are negligible.

The Hamiltonian constraint (R + K^2 - K_ij K^ij = 16piG rho) and
momentum constraint (D_j(K^j_i - delta^j_i K) = 8piG J_i) are derived
structurally. The single normalization sigma^2 = 1/4 produces both
prefactors simultaneously, because the 16piG/8piG ratio is forced by
the Gauss-Codazzi structure of the 3+1 decomposition.

## What is not derived

The covariant derivative D_i in the evolution equation is defined by the
Levi-Civita connection:

    Gamma^k_ij = (1/2) g^{kl} (partial_i gamma_{jl} + partial_j gamma_{il} - partial_l gamma_{ij})

This connection is the unique torsion-free, metric-compatible connection
on (Sigma, gamma_ij). The gap: **no proof exists that the Kuramoto
ensemble averages produce exactly this connection at finite gradient.**

## The precise mathematical problem

### What needs to be proved

**Theorem (unproven).** Let theta(x,t) satisfy the spatially extended
Kuramoto equation at K=1 with coupling kernel K(x,x') and local order
parameter r(x,t) e^{i psi(x,t)}. Define the coherence tensor

    gamma_ij(x,t) = C_ij / C_0  where  C_ij = delta_ij - <partial_i theta partial_j theta>

Then the ensemble averages of second-order terms in the evolution equation
satisfy:

1. **Metric compatibility**: nabla_k gamma_ij = 0, where nabla is the
   connection defined by the natural transport structure of the Kuramoto
   ensemble.

2. **Torsion-free**: Gamma^k_ij = Gamma^k_ji (the connection is symmetric).

These two conditions determine the Levi-Civita connection uniquely
(Fundamental Theorem of Riemannian geometry).

### Why it is hard

At weak gradients, all metric connections agree to leading order. The
Levi-Civita connection differs from other connections only at O(h^2)
where h ~ |partial gamma|. The derivation must therefore control the
second-order ensemble averages:

    <(partial_i theta)^2 partial_j theta>,  <partial_i theta partial_j theta partial_k theta>,  etc.

and show that these higher moments arrange into exactly the Christoffel
symbols of gamma, not some other connection coefficients.

The difficulty is that Kuramoto oscillators are not geodesics — they are
phase-coupled nonlinear oscillators. There is no a priori reason why
their collective spatial correlations should produce the geometric
connection. The self-consistency condition (the oscillators determine the
field that determines the oscillators) constrains the ensemble, but
whether it constrains it enough to force Levi-Civita is unknown.

### Why it might be true

**Self-consistency as metric compatibility.** The Kuramoto self-consistency
equation r = integral g w e^{2pi i Omega} dOmega is a fixed-point
condition: the order parameter is consistent with the locking it produces.
Metric compatibility nabla g = 0 is also a self-consistency condition:
the metric is consistent with its own parallel transport. These are
structurally analogous — the metric "determines" the connection which
"preserves" the metric, just as the order parameter "determines" the
locking which "produces" the order parameter.

**Torsion-free from S^1 compactness.** The circle map operates on S^1,
which has no preferred direction. The ensemble averages inherit this
symmetry: <partial_i theta partial_j theta> = <partial_j theta partial_i theta>.
If the connection inherits this symmetry at all orders, torsion vanishes.

**Lovelock as consistency check.** If the connection is Levi-Civita and
d=3+1, then by Lovelock's theorem the only divergence-free rank-2
tensor is G_mu_nu + Lambda g_mu_nu. The framework already derives d=3+1
and the constraints match Einstein's equations with the correct prefactors.
The Lovelock result is independent of the connection derivation — it
provides a cross-check, not a substitute.

## Possible approaches

### A. Direct expansion

Expand the Kuramoto evolution to O(h^2) explicitly. The ensemble averages
at second order involve the coupling kernel K(x,x') and the locked-state
phase distribution. In the fully locked state (K=1), the phase theta(x)
is determined by the frequency distribution omega(x) through the
self-consistency equation. The second-order terms depend on how this
solution varies spatially. Check whether the O(h^2) terms match
Gamma^k_ij term by term.

This is a brute-force calculation. It would settle the question but
provides no structural insight into why the result holds (if it does).

### B. Variational approach

The Kuramoto system at K=1 minimizes a free energy functional
F[theta] = -(K/2N) sum_{ij} cos(theta_i - theta_j). In the continuum,
this becomes F = -(1/2) integral K(x,x') cos(theta(x) - theta(x')) dx dx'.
The fully locked state is a critical point of F.

If F can be identified with the Einstein-Hilbert action (or a functional
whose Euler-Lagrange equations are the ADM equations), then the
connection question reduces to: does the variational principle produce
Levi-Civita? For the Einstein-Hilbert action S = integral R sqrt(g) d^4x,
the answer is yes (Palatini variation).

This approach would close the gap by construction, but requires
identifying the Kuramoto free energy with the gravitational action —
which is itself an unproven step.

### C. Rigidity from self-consistency

Prove that the self-consistency condition at K=1 is rigid enough that
the connection is determined by gamma_ij alone (no additional degrees
of freedom). If the connection has no freedom beyond the metric, it
must be Levi-Civita (by the fundamental theorem).

The argument would be: at K=1, the oscillator distribution is completely
determined by gamma_ij (via the self-consistency equation). Therefore
the ensemble averages are functionals of gamma_ij alone. Therefore the
connection defined by these averages depends only on gamma_ij. By the
fundamental theorem, the unique metric-compatible torsion-free connection
depending only on the metric is Levi-Civita.

The weak point: "ensemble averages are functionals of gamma_ij alone"
needs proof. If the ensemble retains memory of higher-order structure
(e.g., the specific frequency distribution omega(x) beyond what gamma_ij
encodes), the connection could depend on non-metric data.

## Connection to other gaps

This gap is shared with Gap 2 (Schrödinger): both require the
**spatialization step** — promoting the oscillator ensemble to a field
on a 3-manifold. The spatialization itself (why a field theory rather
than a discrete system?) is a separate assumption, not derived from the
four primitives.

## References

- continuum_limits.md §4 (lines 87–107): weak-gradient derivation
- continuum_limits.md §7 (lines 200–210): stated gaps
- adm_prefactor_verification.py: sigma^2 = 1/4 verification
- rational_field_equation.md Part VI item 2: continuum limit as open question
