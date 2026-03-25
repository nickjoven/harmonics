# Synchronization Cost Framework

A cost accounting framework for physical dynamics. Not a theory of
everything. Systems converge to lowest-cost attractors — not "preferred"
states (which implies an external selector), but endogenously cheapest
configurations.

## Core Primitives

### Time

Mean-field self-coupling rate with dissipative convergence. Not a
background parameter. Differential proper time is differential
synchronization rate, determined by local coupling configuration.

This reframes GR's dynamical spacetime: the metric doesn't describe
a pre-existing geometry that matter moves through — it describes the
synchronization rate field that matter constitutes and participates in.

### Synchronization Cost

The primary physical quantity. Denominated in energy or entropy depending
on regime. All dynamics are cost minimization on the synchronization
landscape.

### Mean Field

Constituted by participants. Has no existence below a minimum coupling
density. This sets a natural lower bound (Planck scale) that is derivable,
not imposed.

---

## Derivation Targets

Open problems where the framework points with enough specificity to
attempt derivation rather than analogy.

### 1. Born Rule

|ψ|² as basin measure of the cost landscape under dissipative convergence.
The amplitude squared is the fraction of initial condition space that
drains into that attractor.

Not axiomatic. The Stribeck lattice -- a chain of friction-coupled oscillators exhibiting stick-slip bifurcation between coherent (subharmonic) and dissipative (fundamental) regimes -- results provide a concrete model:
each oscillator has basins (stick vs. slip), and the basin measure
determines which attractor dominates. The Born rule is the statement
that probability = basin volume in the cost landscape.

### 2. Spectral Tilt (n_s ≈ 0.965)

The devil's staircase -- the fractal step function W(Omega) of the circle map, constant on plateaus at each rational winding number -- evaluated at the golden ratio
1/φ, is exactly self-similar with scaling factor φ² ≈ 2.618. The circle map is the simplest discrete-time model of a driven nonlinear oscillator: theta_{n+1} = theta_n + Omega - (K/2pi) sin(2pi theta_n). This gives
an exactly scale-invariant power spectrum in the natural Stern-Brocot
coordinates (the binary tree that enumerates all rationals by mediant insertion, providing the natural indexing of mode-locked plateaus). The 3.5% tilt comes from the mapping between the staircase's
Fibonacci levels and the CMB wavenumber k.

The mapping traverses 0.0365 Fibonacci levels per e-fold of k (one
level per 27.4 e-folds). In 60 e-folds of observable inflation, the
universe samples ~2.2 Fibonacci levels — a tiny slice of the self-similar
hierarchy. The amplitude A_s ≈ 2.1 × 10⁻⁹ places the pivot at level
~21 (F₂₁ = 17711).

The staircase provides exact scale-invariance; inflation provides the
tilt. See `derivations/INDEX.md` for the full derivation chain.

Earlier approach (superseded): Michaelis-Menten cost function. A
systematic scan (cost_function_scan.py) showed that ALL monotonically
decreasing cost functions produce wrong-sign running. The pivot to the
circle map / devil's staircase resolves this — see
`derivations/04_spectral_tilt_reframed.md`.

### 3. Planck Scale

Not an imposed cutoff. The scale at which synchronization density becomes
self-sustaining — the minimum domain where a mean field can constitute
itself. ℏ and G are the coupling constants that set this threshold.

Connection to lattice results: N = 3 is the minimum chain length for
frequency conversion. The Planck scale may be the "N = 3" of the
synchronization substrate — the minimum extent for self-sustaining
mean-field dynamics.

### 4. Emergent Spacetime

The large-N, high-coupling-density limit of synchronization structure.
The manifold is the constraint surface (KKT) that active synchronization
dynamics live on. Below Planck scale, the manifold fails to constitute
itself.

### 5. a₀ from Synchronization Cost

A circular orbit is a gravitational pendulum: ω² = g/R. The pendulum
that oscillates at the Hubble frequency H has acceleration a₀ = cH/(2π)
and length ƛ_H = c/(2πH), the reduced Hubble wavelength. The 2π is the
geometric factor between a length and its reduced wavelength — the same
factor in ħ = h/2π.

Orbits faster than H (g > a₀) are Newtonian — too fast to entrain.
Orbits slower than H (g < a₀) lock to the cosmic oscillator — MOND
regime. The "dark matter" boost is what entrainment looks like.

The proslambenomenos derivation (a companion repository deriving
cosmological dimensional relations from the Hubble frequency) gives the
dimensional relation a₀ = cH₀/2π. The Stribeck lattice provides the
bifurcation mechanism: below a₀, maintaining Newtonian dynamics costs
more than locking to the enhanced stick-regime coupling.

See `derivations/03_a0_threshold.md` for the full pendulum argument and
cost-accounting detail.

---

## Resolved Framings

Cases where the framework provides mechanistic accounts for standard
postulates or formalisms.

### Measurement / Wavefunction Collapse

Collapse is dissipative convergence completing. The wavefunction is a
synchronization cost distribution across possible attractors. Measurement
is a coupling event that drives the cost of maintaining superposition
above what the system can sustain against the environmental mean field.

Collapse has duration, not a timestamp. The duration is τ ∝ 1/√ε, where
ε is the depth past the tongue boundary — the same saddle-node geometry
that produces the Born rule (Δθ ∝ √ε). This gives the uncertainty
relation τ × Δθ = const: fast collapse ↔ coarse discrimination.

The self-referential fidelity bound (Derivation 9) unifies this with
the MOND transition: both are instances of a system resolving its own
frequency against a reference it participates in. The resolution is
bounded because the measurement instrument and the measured quantity
are the same dynamics. The RAR interpolating function, collapse
duration, uncertainty relation, and Zeno effect all follow from one
constraint: the instrument IS the measured dynamics. See
`derivations/09_fidelity_bound.md`.

### Quantum-Classical Boundary

A cost threshold, not a size cutoff. A system is quantum when maintaining
phase superposition is affordable relative to available coupling energy
and timescale. It is classical when it cannot afford superposition against
the environmental mean field. Einselection (Zurek's pointer states) falls
out as synchronization-cheap attractors — no separate postulate required.

### Renormalization

UV divergences are self-consistency violations: summing synchronization
costs that exceed the mean field generating them. Renormalization enforces
the constraint that cost accounting must be consistent with the field it
accounts for. It works because the constraint is real.

The 120-order vacuum energy discrepancy: what you get when you sum
synchronization costs without imposing this self-consistency condition.

### Mass

The Higgs condensate is a globally phase-coherent state — mean-field
self-coupling that converged. Coupling cost to that field is mass. The
mass hierarchy problem (m_e/m_p ≈ 1/1836) may encode the cost difference
between a fundamental synchronization state and a composite three-body
state (three valence quarks + QCD sea). Derivation target, not closed
result.

### QPO and Rational Frequencies

Rational frequency ratios are synchronization-cheap (small beating
frequency, low maintenance cost). The QPO spectrum maps which modes a
system can afford given its energy budget. The stick-slip bowing geometry
at rational string subdivisions selects rational ratios by the same cost
mechanism. Regge trajectories (mass² linear in spin) are consistent with
synchronization cost increasing with internal phase coherence demand.

### CMB Low-ℓ Anomalies

The quadrupole is too large to have completed synchronization before last
scattering. Suppression is a mode that couldn't afford to lock —
mechanistic where inflation offers only cosmic variance. Silk damping is
the small-scale synchronization affordability horizon. The spectral tilt
is the cost gradient. Odd/even peak asymmetry is baryonic cost asymmetry
— one phase direction is cheaper than the other due to baryonic inertia.

---

## The Classical Forces as Cost Gradients

Forces aren't fundamental. They are derivatives of the cost functional
with respect to configuration — what we observe as force is the gradient
of synchronization cost. The apparent diversity of forces reflects
different coupling channels through which cost is denominated.

### Gravity

Cost structure of the global mean field itself. Gravitational attraction
is configurations moving toward cheaper global synchronization states.
Mass is synchronization cost already paid and stabilized. MOND is the
boundary where local cost gradient becomes comparable to the cosmological
mean field.

### Electromagnetism

Local U(1) phase synchronization cost. The photon is the cost-exchange
quantum. Charge is coupling constant — participation strength in U(1)
synchronization. The field is the cost gradient, not the primary object.

The Aharonov-Bohm effect is direct evidence that phase is primary and
field is derivative: the particle's synchronization history, encoded in
the potential, determines the outcome.

### Strong Force

SU(3) synchronization. Confinement is separation cost exceeding pair
production cost. Asymptotic freedom is cost approaching zero as
synchronization domains fully overlap. Gluons self-interact because they
participate in the synchronization they mediate.

### Weak Force

Attractor transition cost. The weak interaction changes particle identity:
a mode driven by cost gradient across a threshold into a different stable
attractor. W and Z bosons are massive because attractor transitions
require paying the cost of breaking local synchronization state.

Parity violation is a cost asymmetry in the attractor landscape —
right-handed transitions are unaffordable at accessible energies.

### Unification

Not a larger symmetry group. Recognizing all four as cost gradients
through different coupling channels at different scales. At high energy,
channel distinctions become too cheap to matter — electroweak unification
physically. Not symmetry restoration. A cost regime collapse.

---

## Two Stable Regimes and the Hierarchy Problem

The self-consistency condition is a nonlinear fixed-point equation.
Nonlinear fixed-point equations generically have multiple stable
solutions.

There are two structurally distinct synchronization operations:

- **Local phase coupling** (EM, strong, weak): mean field constituted by
  nearby participants, cost denominated in local coupling density, bounded
  participation set.

- **Global mean field coupling** (gravity, cosmological background): mean
  field constituted by all participants, cost denominated in total
  participation density, unbounded.

These solve different fixed-point equations — same functional form,
different domain. Each independently fixes a stable scale.

The hierarchy between regimes is the ratio of cosmological participation
density to local coupling density. This is large because the universe is
large and Λ is small — not fine-tuned, but fixed by two independently
derived quantities the KE derivation already handles.

**The hierarchy problem dissolves.** It was asking why a ratio is large
and apparently arbitrary. The synchronization answer: it's the ratio of
global to local synchronization density, both fixed by the cost
functional's self-consistency condition. Large because these are genuinely
distinct operational scales, not because something is unnaturally tuned.

---

## Structure as Lowest-Cost Mediation

**The central statement of the framework:**

> Structure is what lowest-cost mediation looks like when you step back
> from it.

The manifold, dimensionality, and topology are the configuration of
couplings that minimizes total synchronization cost across all
participants. The universe isn't shaped a certain way and then doing
physics inside that shape. The shape is the physics, settled.

The inherited stage problem dissolves completely — the manifold is what
you derive, not what you assume.

### Dimensionality

Three spatial dimensions is the lowest-cost mediation topology for this
universe's coupling density and cost functional structure. Higher
dimensions cost more to maintain coherence across. Lower dimensions can't
mediate enough distinct coupling channels to support the observed attractor
diversity. Three is the fixed point.

### Laws of Physics

Stable mediation protocols. The coupling rules that cost the least to
maintain globally while remaining locally self-consistent. Not imposed on
the structure. Co-emergent with it. Same fixed-point equation, same
solution.

### The Unreasonable Effectiveness of Mathematics

Mathematics is the study of structure. Structure is lowest-cost mediation.
Mathematics works because it independently discovers the same attractor
landscape the universe settled into.

### The Minimal System

Two things: **distinguishable states** and **a cost functional**.

Coupling, structure, dimensionality, laws — all are what the cost
functional produces at its fixed point over the full participation set.

Everything else is accounting.

---

## Structural Principles

1. Physical outcomes sit at constraint boundaries, not arbitrary preferred
   points (KKT complementary slackness -- the Karush-Kuhn-Tucker optimality condition requiring that at a solution, each constraint is either inactive or its associated cost multiplier is zero, so physical outcomes sit exactly at active constraint boundaries).

2. The cost function must be self-consistent with the field it accounts for
   (renormalization as constraint enforcement, not formal trick).

3. Synchronization cost can be denominated in energy or entropy depending
   on regime. The CMB low-ℓ anomalies may involve thermodynamic exclusion
   rather than energetic exclusion.

4. No external selector. Attractors, basins, cost gradients, and
   convergence dynamics. Probability is basin measure.

5. Spacetime is a participant, not a stage. Treating it as inherited
   geometry is an open derivation debt, not a solved problem.

---

## Open Questions

1. What is the entropy-vs-energy regime boundary for synchronization cost
   denomination?

2. Does spacetime emergence require a discrete substrate, or does the cost
   function produce a continuum limit naturally?

3. Is degenerate perturbation theory the right tool for near-threshold
   synchronization states at the quantum-classical boundary?

---

## Connection to Stribeck Lattice Results

The lattice experiments in this repo provide the first concrete numerical
confirmation of a key mechanism:

- **Dual regime**: The lattice operates in stick (coherent, subharmonic)
  or slip (dissipative, fundamental) depending on driving amplitude.
  The synchronization cost framework predicts exactly this: systems
  converge to the cheapest available attractor. The stick regime is cheap
  (strong coupling, low maintenance). The slip regime is expensive (weak
  coupling, dissipative).

- **Frequency conversion as cost minimization**: The lattice converts
  ω_d → ω₀ because ω₀ has lower synchronization cost in the stick regime.
  Energy finds the cheapest channel. This is not a designed filter — it
  emerges from the cost structure of the nonlinear coupling.

- **Critical chain length (N = 3)**: The minimum spatial extent for
  frequency conversion maps onto the minimum coupling density for a
  self-sustaining mean field. The Planck scale derivation target is the
  physical instantiation of this threshold.

- **Differential attenuation**: ω_d attenuates (high cost, slip regime);
  ω₀ propagates (low cost, stick regime). This is the spectral tilt in
  miniature — the cost gradient across frequencies, made visible in a
  chain of 8 oscillators.

- **Forces as cost gradients**: The friction force in the lattice is
  literally the derivative of synchronization cost with respect to
  velocity. The Stribeck curve is the cost function. What the lattice
  demonstrates at 8 elements, the framework claims at all scales: force
  is cost gradient, structure is settled cost minimization.
