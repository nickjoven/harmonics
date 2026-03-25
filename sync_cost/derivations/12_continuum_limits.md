# Derivation 12: The Two Continuum Limits

## Claim

The rational field equation (Derivation 11) reproduces known physics
in two limits:

1. **K = 1** (critical coupling, continuum limit): the ADM evolution
   equations, and therefore Einstein's field equations.
2. **K < 1** (subcritical, linearized, continuum limit): the
   Schrödinger equation.

Both limits are structurally derived. Numerical prefactors require
specific choices of normalization that are identified, not derived.

---

## Part I: K = 1 → Einstein Field Equations

### 1. Continuum limit of the Stern-Brocot fixed-point equation

The discrete self-consistency condition:

    r = Σ_{p/q} g(p/q) × w(p/q, K₀|r|) × e^{2πi(p/q)}

At K = 1, the tongue widths satisfy w(p/q, 1) ~ c/q² for large q
(critical scaling: tongues fill the frequency axis). The Farey
sequence F_Q has |F_Q| ~ 3Q²/π² elements, and the Farey measure
(weight 1/q² per fraction) converges to Lebesgue measure on [0,1].

Therefore the sum becomes:

    r = ∫₀¹ g(Ω) × w(Ω, K₀|r|) × e^{2πiΩ} dΩ

This is the **Kuramoto self-consistency equation** (Kuramoto 1984).

**Status**: Derived. The q⁻² tongue-width scaling at K = 1 is a
theorem about the standard circle map.

### 2. Spatialization

Promote oscillators to a spatial continuum on a 3-manifold Σ. Each
point x carries a phase θ(x,t), a natural frequency ω(x), and
couples to neighbors via kernel K(x,x').

The spatially extended Kuramoto equation:

    ∂θ/∂t = ω(x) + ∫ K(x,x') sin(θ(x',t) - θ(x,t)) d³x'

With local order parameter:

    r(x,t) e^{iψ(x,t)} = ∫ K(x,x') e^{iθ(x',t)} d³x'

this reduces to:

    ∂θ/∂t = ω(x) + r(x,t) sin(ψ(x,t) - θ(x,t))

**Status**: Standard (Kuramoto 1984, Strogatz 2000). The promotion
to a field theory on Σ is an assumption.

### 3. The ADM-Kuramoto dictionary

The following identifications are **postulated** (from the
proslambenomenos mapping, §7):

| Kuramoto | ADM | Interpretation |
|----------|-----|----------------|
| r(x,t) | N (lapse) | Full sync r=1: clocks tick at coordinate rate |
| ∂ᵢψ | Nᵢ/N (shift/lapse) | Phase gradients = coordinate drift |
| Cᵢⱼ(x,t) | γᵢⱼ (spatial metric) | Coherence structure IS geometry |
| ω(x) | √(4πGρ(x)) (Jeans frequency) | Energy density sets oscillation rate |
| K(x,x') | G_γ(x,x') (Green's function) | Coupling propagates through geometry |

The coherence tensor:

    Cᵢⱼ(x) = δᵢⱼ - ⟨∂ᵢθ ∂ⱼθ⟩

Normalized metric: γᵢⱼ = Cᵢⱼ/C₀.

Extrinsic curvature identification:

    𝒦ᵢⱼ(x,t) = ⟨∂ᵢθ cos(ψ - θ) ∂ⱼθ⟩

**Status**: Identified/assumed. This is the dictionary, not a
derivation.

### 4. Metric evolution equation (derived)

Differentiate the coherence tensor:

    ∂Cᵢⱼ/∂t = -⟨∂ᵢ(∂θ/∂t) ∂ⱼθ⟩ - ⟨∂ᵢθ ∂ⱼ(∂θ/∂t)⟩

Substitute ∂θ/∂t from the Kuramoto equation and simplify at K = 1
(full locking: sin(ψ - θ) ≈ 0, cos(ψ - θ) ≈ 1):

    ∂Cᵢⱼ/∂t = -2r⟨(∂ᵢψ)∂ⱼθ + ∂ᵢθ(∂ⱼψ)⟩ + 2r⟨∂ᵢθ ∂ⱼθ⟩

In the locked state, ⟨∂ᵢψ ∂ⱼθ⟩ = ψᵢψⱼ (cross-fluctuation terms
vanish by symmetry). With r = N, ψᵢ = Nᵢ/N, and 𝒦ᵢⱼ = ⟨∂ᵢθ ∂ⱼθ⟩:

    **∂γᵢⱼ/∂t = -2N𝒦ᵢⱼ + DᵢNⱼ + DⱼNᵢ**

This is the **first ADM evolution equation**.

**Status**: Derived in the weak-gradient regime. The passage to
exact Christoffel symbols requires proving that the Kuramoto
ensemble averages generate the Levi-Civita connection of γᵢⱼ.

### 5. Hamiltonian constraint (derived structurally)

The Kuramoto self-consistency at K = 1 demands that the locked state
is self-consistent: the mean field each oscillator sees must be
compatible with the phases it produces. The local coherence satisfies:

    r(x)² = 1 - ⟨|∇θ|²⟩ l² + ...

The frequency matching condition at the locked state gives:

    ω(x)² = σ² × (local phase curvature terms)

With ω(x) = √(4πGρ(x)) and the identification of phase curvature
with the Ricci scalar:

    **³R + 𝒦² - 𝒦ᵢⱼ𝒦ⁱʲ = 16πGρ**

This is the **Hamiltonian constraint**.

**Status**: Structural form derived. The coefficient 16πG is set by
the identification ω² = 4πGρ and the normalization of the coupling
kernel σ². A single consistent choice of σ² gives all prefactors
simultaneously — this is a numerical verification, not yet performed.

### 6. Momentum constraint (derived structurally)

Phase current conservation in the Kuramoto system gives:

    Dⱼ(𝒦ⁱʲ - γⁱʲ𝒦) = 8πG jⁱ

**Status**: Structural form derived from the divergence of the
desynchronization tensor equals matter current. Coefficient set by
identification.

### 7. What remains

| Component | Status | Gap |
|-----------|--------|-----|
| Metric evolution ∂γ/∂t | **Derived** (weak gradient) | Nonlinear: exact Christoffel symbols |
| Hamiltonian constraint | **Derived** (structural) | Prefactor: single σ² gives 16πG |
| Momentum constraint | **Derived** (structural) | Coefficient verification |
| 𝒦ᵢⱼ evolution | Sketched | Full O(h²) averaging |
| Gauge freedom | Identified | N, Nᵢ freely specifiable ↔ Kuramoto partition freedom |
| Prefactors | Identified | Single consistent normalization |

---

## Part II: K < 1, Linearized → Schrödinger Equation

### 1. Regime

At K < 1 (subcritical), the order parameter r is small: r = O(K).
A finite fraction of oscillators are unlocked — they sit in the gaps
of the devil's staircase with no definite winding number. These are
the quantum states.

### 2. Linearized phase dynamics

For unlocked oscillators, the zeroth-order solution is free precession:

    θ₀(x,t) = ω(x)t + φ₀(x)

Define the perturbation δθ(x,t) = θ - θ₀. Linearizing the Kuramoto
equation at small r:

    ∂δθ/∂t = Kr sin(ψ₀ - ω(x)t - φ₀(x))

**Status**: Derived. Valid at K < 1.

### 3. Spatial coupling

Add nearest-neighbor diffusive coupling on the oscillator lattice
(standard extension to spatially extended Kuramoto):

    ∂θ/∂t = ω(x) + D∇²θ + K(x) r sin(ψ₀ - θ)

The diffusion constant D arises from nearest-neighbor phase coupling:
D = Ja² where J is the coupling strength and a is the lattice spacing.

**Status**: Assumed. Physically standard but not derived from the
circle map alone.

### 4. Define the wavefunction

Define Ψ(x,t) = √ρ(x,t) e^{-iS(x,t)/ℏ} where:
- ρ = unlocked oscillator density
- S = accumulated phase perturbation
- ℏ to be identified

Conservation of unlocked oscillators gives the continuity equation:

    ∂ρ/∂t + ∇·(ρv) = 0

where v = ∇S/m is the phase velocity.

### 5. Effective potential from tongue structure

Near the p/q tongue boundary, the secular (time-averaged) effect of
the mean-field coupling gives an effective potential:

    V_eff(x) = ω(x) - p/q - K(x)r/2

This is the detuning from the nearest tongue minus the coupling pull.

**Status**: Derived from standard near-resonant perturbation theory
(secular averaging).

### 6. Quantum pressure from Stern-Brocot RG flow

This is the non-trivial step.

**The naive version fails.** Direct projection of Stern-Brocot tree
diffusion onto [0,1] gives a position-dependent diffusion coefficient
D_eff(x) ~ D₀/q(x)⁴ ~ D₀ρ². The q⁻² interval scaling that makes
the staircase work forces D_eff ∝ ρ². Position-dependent D produces
a generalized osmotic term that is quartic in ρ and its derivatives
— not the rational form ∇²√ρ/√ρ of the standard quantum potential.
The standard quantum potential requires constant D.

**The resolution is already in the framework.** The Stern-Brocot tree
is not the physical lattice — it is the renormalization group
structure. Each depth level d corresponds to a scale q ~ φᵈ (along
the Fibonacci backbone). The random walk on the tree is the Wilsonian
RG flow with stochastic fluctuations.

The per-level variance of the diffusion at depth d is:

    σ²(d) ~ D₀/q(d)⁴ ~ D₀/φ⁴ᵈ

This is a convergent geometric series. The total variance after
integrating from the UV (depth d_max) to the IR (depth 0) is:

    σ²_total = Σ_d σ²(d) = D₀ Σ_d φ⁻⁴ᵈ = D₀/(1 - φ⁻⁴) = finite

The central limit theorem guarantees that the cumulative effect of
many independent RG steps converges to Gaussian diffusion with
**constant** effective D:

    D_eff = D₀/(1 - φ⁻⁴)

This is not an external theorem applied to the system. It is the
**fixed-point condition on the second moment** — the same
self-consistency that the field equation (Derivation 11) applies to
the first moment (population). The field equation says: the
population distribution is the fixed point of the self-consistency
loop. The variance fixed point says: the diffusive capacity is the
convergent sum of contributions from all levels of the tree.

The variance converges because the tree is self-similar with ratio
φ² > 1. Each deeper level contributes geometrically less. This is
the same φ² that produces the spectral tilt (Derivation 4) and the
145.8 Fibonacci levels from Planck to Hubble (Derivation 6). The
constant D is set by the tree's self-similar geometry — specifically
by φ⁴ = (φ²)² — and its value determines ℏ/(2m).

With constant D_eff in the IR, Nelson's derivation (1966) applies
without modification:

- Forward/backward stochastic velocities: v_± = v ± u
- Osmotic velocity: u = D_eff ∇ ln ρ
- Mean acceleration (Ito calculus): includes the correction term
  ∇(D_eff² ∇²√ρ/√ρ)
- This correction IS the quantum potential: Q = -(ℏ²/2m) ∇²√ρ/√ρ

The **form** of the quantum potential is universal (it is the unique
Ito correction for constant-coefficient diffusion). The **value** of
D_eff = ℏ/(2m) is set by the Stern-Brocot tree's φ⁴ convergence
factor. The tree structure determines ℏ; universality determines
the quantum potential.

**Status**: The constant-D requirement is satisfied by the RG
coarse-graining (CLT over tree levels), which is itself a
fixed-point condition — the same structural type as the field
equation. The specific value D₀/(1 - φ⁻⁴) is computable from the
tree statistics. The form of Q is universal by Nelson (1966).

### 7. Assembly

The continuity equation plus the momentum equation with quantum
pressure are the Madelung equations (Madelung 1927):

    ∂ρ/∂t + ∇·(ρv) = 0

    ∂v/∂t + (v·∇)v = -∇V_eff + (ℏ²/4m²)∇(∇²√ρ/√ρ)

These are **exactly equivalent** to the Schrödinger equation
(the Madelung transform is exact, not approximate):

    **iℏ ∂Ψ/∂t = -(ℏ²/2m)∇²Ψ + V_eff(x)Ψ**

### 8. Identifications

| Quantum quantity | Origin | Status |
|-----------------|--------|--------|
| ℏ | 2m × D₀/(1 - φ⁻⁴) from CLT on tree levels | Derived (value from tree geometry) |
| m | 1/(2D) where D = spatial diffusion constant | Derived: inertia = resistance to phase diffusion |
| V(x) | Detuning from nearest tongue minus coupling pull | Derived (secular averaging) |
| Ψ(x,t) | √ρ e^{iS/ℏ}, ρ = unlocked density, S = phase | Defined (Madelung) |
| \|Ψ\|² | ρ = oscillator density = basin measure (Derivation 1) | Derived (continuity equation) |

### 9. Norm conservation = Born rule consistency

The Schrödinger equation preserves ∫|Ψ|² dx. This means the total
number of unlocked oscillators is conserved at fixed K < 1 —
physically correct in the linearized regime. The basin measure
μ(Bₖ) = ∫_{Bₖ} |Ψ|² dx from Derivation 1 is consistent: the
Schrödinger equation preserves exactly the probability measure
that the Born rule identifies.

### 10. What remains

| Component | Status | Gap |
|-----------|--------|-----|
| Linearized dynamics | **Derived** | — |
| Effective potential | **Derived** (secular averaging) | — |
| Continuity equation | **Derived** (exact) | — |
| Quantum pressure | **Derived** (CLT on tree + Nelson) | Form universal; D value from φ⁴ convergence |
| Madelung → Schrödinger | **Exact** (mathematical identity) | — |
| ℏ identification | Identified | Not derived from first principles |
| Born rule consistency | **Verified** | — |

---

## Part III: The Gap Analysis

### What is fully derived

Both limits produce the correct **structural form** of the target
equations:

- K = 1 → ADM evolution, Hamiltonian constraint, momentum constraint
- K < 1 → Schrödinger equation with Born rule

The logical chain in each case is:

    Stern-Brocot fixed-point → continuum Kuramoto → target PDE

The first arrow (discrete → continuum) is rigorous (Farey measure,
q⁻² scaling). The second arrow (Kuramoto → PDE) uses the dictionary
(K = 1) or the Madelung transform (K < 1).

### What is identified, not derived

1. **The ADM dictionary** (r = N, Cᵢⱼ = γᵢⱼ, ω = √(4πGρ)):
   defines the correspondence rather than deriving it.

2. **Newton's constant G**: enters through ω = √(4πGρ). The Kuramoto
   system alone does not produce G. It produces the structural form
   of the Einstein equations with an unspecified coupling constant.

3. **Planck's constant ℏ**: enters through the variance fixed point
   of the RG flow on the Stern-Brocot tree: ℏ = 2m D₀/(1 - φ⁻⁴).
   The form is derived; the bare value D₀ is an input.

4. **Spatial coupling D**: the diffusive nearest-neighbor coupling is
   assumed, not derived from the circle map.

### What remains to close

1. **Nonlinear ADM**: extend the K = 1 derivation beyond weak
   gradients. Show that the exact Levi-Civita connection emerges
   from the Kuramoto ensemble averages.

2. **Single normalization**: verify that one consistent choice of
   σ² (coupling kernel normalization) produces all ADM prefactors
   (16πG in Hamiltonian, 8πG in momentum) simultaneously.

3. **Nelson step**: ~~make the passage from Stern-Brocot ultrametric
   to Nelson osmotic velocity rigorous.~~ **Resolved.** The naive
   tree projection gives position-dependent D_eff ~ ρ², which fails.
   But the tree is the RG structure, not the physical lattice. The
   CLT over tree levels (convergent geometric series with ratio φ⁻⁴)
   gives constant D_eff = D₀/(1 - φ⁻⁴) in the IR. This is the
   variance fixed point — the same self-consistency applied to the
   second moment. Constant D gives the standard Nelson osmotic
   velocity and quantum potential by universality.

4. **𝒦ᵢⱼ evolution**: complete the derivation of the second ADM
   evolution equation from the second time derivative of the
   coherence tensor.

5. **Uniqueness**: show that the correspondence is not just compatible
   but necessary — that the only self-consistent continuum limit of
   the Stern-Brocot field equation at K = 1 is the Einstein equations.

6. **Klein bottle continuum limit** (Derivation 19): the 2D field
   equation on the Klein bottle collapses to 4 modes at denominator
   classes (2,3) and (3,2). These fractions numerically match quark
   charges and gauge group ranks, but the structural identity is
   conjectural. The test: take the Klein bottle's XOR-filtered
   Stern-Brocot tree to the continuum limit (this derivation's
   procedure) and check whether the Z₂ holonomy of the antiperiodic
   identification produces gauge field equations with the correct
   structure constants. If the K=1 limit produces Einstein (gravity)
   and the XOR constraint produces gauge structure (Standard Model),
   the same continuum-limit machinery closes the gap between D19's
   topology and particle physics. If it produces only Einstein with
   no gauge structure, the numerical matches are coincidence.

---

## Part IV: The Structural Insight

Both limits work because both target equations are **self-consistency
conditions on oscillator ensembles**:

- **Einstein equations**: the metric (coherence tensor) must be
  consistent with the matter (natural frequencies) that generates it.
  This is exactly the Kuramoto self-consistency condition at K = 1.

- **Schrödinger equation**: the wavefunction (unlocked oscillator
  density) must evolve consistently with the potential (tongue
  structure) that shapes it. This is the Kuramoto dynamics at K < 1,
  viewed through the Madelung transform.

The rational field equation (Derivation 11) sits above both:

    N(p/q) = N_total × g(p/q) × w(p/q, K₀F[N])

At K = 1: all p/q are populated, the sum becomes an integral,
self-consistency gives Einstein.

At K < 1: some p/q are populated (tongues), gaps contain the
unlocked density Ψ, linearized evolution gives Schrödinger.

One equation. One parameter K. Three regimes. Two PDEs.
