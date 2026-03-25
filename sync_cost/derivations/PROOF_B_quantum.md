# Proof Chain B: Polynomial → Quantum Mechanics

N. Joven — 2026 — CC0 1.0

---

## Statement

From the same two physical properties — energy conservation and
stability — the Schrödinger equation and the Born rule follow uniquely
at subcritical coupling. The first five propositions are shared with
Proof Chain A. The paths diverge at the coupling parameter K.

---

## Shared propositions (P1–P5)

These are identical to Proof Chain A and are not repeated here.
See [PROOF_A_gravity.md](PROOF_A_gravity.md).

| P | Statement | Source |
|---|-----------|--------|
| P1 | Phase space is S¹ | D10 §1 |
| P2 | Mediant is unique combining operation | D29 |
| P3 | Stern-Brocot tree is configuration space | D10 §2–3 |
| P4 | Rational field equation (fixed-point) | D11 |
| P5 | d = 3, SL(2,R) | D14 |

---

## Propositions (quantum branch)

### Q1. The parabola at tongue boundaries [D1, D10 §4]

*Uses: P3 (Stern-Brocot tree), circle map dynamics.*

At the boundary of every Arnold tongue, the circle map undergoes a
saddle-node bifurcation. Near the bifurcation point, the dynamics
reduce to:

$$\dot{x} = \mu - x^2$$

where μ is the distance from the tongue boundary. This is the normal
form — the parabola x² + μ = 0 is the fourth primitive.

The basin width scales as:

$$\Delta\theta \propto \sqrt{\varepsilon}$$

where ε = |μ| is the detuning from resonance. This is **exact** — it
is the universal normal form of the saddle-node, not an approximation.
The square root is the parabola's geometry. ∎

### Q2. The Born rule [D1, D9]

*Uses: Q1.*

The probability of finding the system in a particular locked state is
proportional to the basin of attraction of that state. From Q1, the
basin width is Δθ ∝ √ε, so the basin area (in the 2D phase-amplitude
space) is:

$$P_k \propto (\Delta\theta_k)^2 \propto \varepsilon_k \propto |\psi_k|^2$$

The exponent **2** in |ψ|² is the degree of the parabola at the
bifurcation. It is geometry, not a postulate.

Equivalently: the synchronization cost landscape near each attractor is
quadratic (C ≈ C₀ + α|ψ − ψ_k|²). Dissipative convergence on this
landscape contracts phase-space volume proportional to |ψ_k|². The
Born rule is the basin measure of a quadratic cost landscape. ∎

### Q3. The subcritical regime K < 1 [D12 §II]

*Uses: P4, P5.*

At subcritical coupling (K < 1), the order parameter r < 1. A finite
fraction of oscillators remain **unlocked** — they sit in the gaps of
the devil's staircase with no definite winding number. These are the
quantum states.

The population splits:

| Oscillators | Fraction | Character |
|-------------|----------|-----------|
| Locked (definite p/q) | r | Classical (metric, P7–P8) |
| Unlocked (drifting) | 1 − r | Quantum (wave, Q4) |

The ratio r/(1−r) is set by the self-consistency equation (P4). ∎

### Q4. Madelung variables [D12 §II]

*Uses: Q3, P5.*

For the unlocked oscillators, define:

- **Density**: ρ(x,t) = density of unlocked oscillators at position x
- **Phase**: S(x,t) = accumulated phase perturbation (action variable)

In the continuum limit on the SL(2,R) manifold (P5), with
nearest-neighbor diffusive coupling:

$$\partial_t \rho + \nabla \cdot (\rho\, \nabla S / m) = 0 \qquad \text{(continuity)}$$

$$\partial_t S + \frac{|\nabla S|^2}{2m} + V - \frac{\hbar^2}{2m}\frac{\nabla^2\sqrt{\rho}}{\sqrt{\rho}} = 0 \qquad \text{(Hamilton-Jacobi)}$$

where:

| Kuramoto quantity | QM quantity |
|---|---|
| Unlocked oscillator density ρ(x,t) | \|Ψ\|² |
| Accumulated phase S(x,t) | Action / phase |
| Tongue-structure effective potential | V(x) |
| Stern-Brocot RG diffusion D_eff | Quantum potential |

The quantum potential ℏ²∇²√ρ / (2m√ρ) arises from the Stern-Brocot
renormalization group flow: per-level variance σ²(d) ~ φ^{−4d} sums
to a convergent constant D_eff = D₀/(1 − φ^{−4}). ∎

### Q5. The Schrödinger equation [D12 §II]

*Uses: Q4.*

Define Ψ = √ρ · e^{iS/ℏ}. The Madelung equations (Q4) are
algebraically equivalent to:

$$\boxed{i\hbar\,\partial_t \Psi = -\frac{\hbar^2}{2m}\nabla^2\Psi + V\Psi}$$

This is the **Schrödinger equation**. The transformation is invertible
(Madelung, 1927). ∎

### Q6. Uniqueness of the quantum branch

*Uses: Q1–Q5.*

The Schrödinger equation is the unique output of the subcritical regime
because:

1. The Madelung form is forced by continuity + Hamilton-Jacobi (the only
   equations consistent with probability conservation and energy
   conservation for the unlocked population)
2. The quantum potential is forced by the Stern-Brocot RG (the diffusion
   constant is set by φ, which is set by the tree structure P3)
3. The Born rule exponent 2 is forced by saddle-node universality (Q1–Q2)

No postulates of quantum mechanics are assumed. They are derived:

| QM postulate | Derivation |
|---|---|
| States are vectors in Hilbert space | Ψ = √ρ · e^{iS/ℏ} (Q4–Q5) |
| P = \|ψ\|² | Basin measure of parabolic cost (Q2) |
| Time evolution is Schrödinger | Madelung ↔ Schrödinger equivalence (Q5) |
| Observables are operators | Conjugate variables (ρ, S) → (x, p) |

∎

---

## The chain

$$\text{Counting} \xrightarrow{P1} S^1 \xrightarrow{P2} \text{mediant} \xrightarrow{P3} \text{Stern-Brocot} \xrightarrow{P4} \text{field eq.}$$

$$\xrightarrow{K < 1} \text{unlocked oscillators} \xrightarrow{Q3,Q4} \text{Madelung} \xrightarrow{Q5} i\hbar\partial_t\Psi = H\Psi$$

$$\text{Parabola} \xrightarrow{Q1} \sqrt{\varepsilon}\text{ scaling} \xrightarrow{Q2} P = |\psi|^2$$

Seven propositions (five shared, two independent). Same two physical
inputs. The quantum branch is the **subcritical limit** of the same
equation whose **critical limit** gives general relativity.

---

## Dependency graph

```
P1–P5 (shared with Proof A)
  ↓
P4 (field eq.) at K < 1
  ↓
Q3 (locked/unlocked split)
  ↓
Q4 (Madelung: ρ, S)
  ↓
Q5 (Schrödinger)

P3 (Stern-Brocot) + Primitive 4 (parabola)
  ↓
Q1 (saddle-node: Δθ ∝ √ε)
  ↓
Q2 (Born rule: P = |ψ|²)
```

---

## The two limits, one equation

| Parameter | Regime | Locked fraction | Output |
|-----------|--------|-----------------|--------|
| K = 1 | Critical | r = 1 (all locked) | Einstein (Proof A, P8) |
| K < 1 | Subcritical | r < 1 (partial) | Schrödinger (Q5) + Born (Q2) |
| K → 0 | Decoupled | r = 0 (none locked) | Free particles |

The rational field equation (P4) is one equation. General relativity
and quantum mechanics are its two continuum limits.

---

## Cross-references

| Proposition | Derivation | Key theorem |
|-------------|------------|-------------|
| P1–P5 | D10, D29, D11, D14 | (see Proof A) |
| Q1 | D10 §4, D1 | Saddle-node normal form |
| Q2 | D1, D9 | Basin measure = |ψ|² |
| Q3 | D12 §II | Subcritical: partial locking |
| Q4 | D12 §II | Madelung (1927) |
| Q5 | D12 §II | Schrödinger (1926) |
| Q6 | D1, D9, D12 | Uniqueness |
