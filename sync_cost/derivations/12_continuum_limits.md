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

### 6. Quantum pressure from Stern-Brocot hierarchy

This is the non-trivial step. The hierarchical gap structure of the
devil's staircase introduces a correction to the naive diffusion.

The Stern-Brocot tree has a natural ultrametric: two fractions are
"close" if their mediant is at a low level. The density ρ of unlocked
oscillators, viewed as a diffusion process on this ultrametric space,
acquires an osmotic velocity:

    u = (D_eff/2) ∇ ln ρ

This is the Nelson stochastic mechanics result: diffusion on a
hierarchical (non-flat) space produces an osmotic correction that
acts as a quantum potential:

    Q(x) = -(ℏ²/2m) ∇²√ρ / √ρ

The coefficient D_eff = ℏ/(2m) is set by the scaling limit:

    K → 1⁻, q → ∞, with (K/2)^q × q⁻³ = ℏ/(2m) held fixed

**Status**: This is the most assumption-laden step. The claim that
the Stern-Brocot ultrametric produces exactly the Nelson osmotic
term requires the specific scaling limit above. Without the tree
structure (uniform gap distribution), the result would be a heat
equation, not Schrödinger.

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
| ℏ | D_eff × 2m from the Stern-Brocot scaling limit | Identified |
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
| Quantum pressure | **Derived** (Nelson + Stern-Brocot) | Scaling limit (15) is an identification |
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

3. **Planck's constant ℏ**: enters through the Stern-Brocot scaling
   limit. The value of ℏ is set by the choice of scaling, not
   computed from the framework.

4. **Spatial coupling D**: the diffusive nearest-neighbor coupling is
   assumed, not derived from the circle map.

### What remains to close

1. **Nonlinear ADM**: extend the K = 1 derivation beyond weak
   gradients. Show that the exact Levi-Civita connection emerges
   from the Kuramoto ensemble averages.

2. **Single normalization**: verify that one consistent choice of
   σ² (coupling kernel normalization) produces all ADM prefactors
   (16πG in Hamiltonian, 8πG in momentum) simultaneously.

3. **Nelson step formalization**: make the passage from Stern-Brocot
   ultrametric to Nelson osmotic velocity rigorous. This is the
   load-bearing step for the Schrödinger limit.

4. **𝒦ᵢⱼ evolution**: complete the derivation of the second ADM
   evolution equation from the second time derivative of the
   coherence tensor.

5. **Uniqueness**: show that the correspondence is not just compatible
   but necessary — that the only self-consistent continuum limit of
   the Stern-Brocot field equation at K = 1 is the Einstein equations.

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
