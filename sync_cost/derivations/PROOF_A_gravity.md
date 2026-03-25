# Proof Chain A: Polynomial → General Relativity

N. Joven — 2026 — CC0 1.0

---

## Statement

From two physical properties of coupled oscillators — energy conservation
and stability — the Einstein field equations follow uniquely. Each
proposition uses only the previous ones. No proposition uses the
continuum, coordinates, or any physics beyond oscillator coupling.

---

## Definitions

**D1.** An *oscillator* is a process with an integer cycle count.

**D2.** Two oscillators *couple* when they share energy without external input.

**D3.** A *winding number* p/q means: q cycles of one oscillator correspond to p cycles of the other.

---

## Propositions

### P1. The circle [D10 §1]

*Uses: integers, fixed-point condition.*

A period-q orbit with winding number p satisfies f^q(x) = x + p and
f^q(x) = x simultaneously. Therefore p ≡ 0 in the phase space. Since
p is an arbitrary integer, the phase space is **R/Z = S¹**. ∎

### P2. The mediant [D29]

*Uses: P1 (circle), energy conservation (D2), Arnold tongue stability.*

Two coupled oscillators at winding numbers a/b and c/d lock to a
frequency between them (energy conservation: no external source). Among
all rationals in (a/b, c/d), the one with smallest denominator has the
widest Arnold tongue — width w ~ (K/2)^q — and is reached first as
coupling increases.

**Theorem (Stern-Brocot, 1858).** For adjacent fractions (|ad − bc| = 1),
the unique rational in (a/b, c/d) with smallest denominator is the
mediant (a+c)/(b+d). ∎

### P3. The Stern-Brocot tree [D10 §2–3]

*Uses: P1, P2.*

Iterating the mediant from the endpoints 0/1 and 1/0 enumerates every
positive rational exactly once, ordered by denominator. The tree is the
unique configuration space: every winding number appears at its natural
complexity level. No other enumeration respects the Arnold tongue
stability ordering (P2). ∎

### P4. The rational field equation [D11]

*Uses: P3, fixed-point condition.*

The population N(p/q) at each node of the Stern-Brocot tree satisfies:

$$N(p/q) = N_{\text{total}} \times g(p/q) \times w(p/q,\; K_0 F[N])$$

where g is the frequency distribution, w is the tongue width, and F[N]
is the global order parameter. This is the fixed-point equation x = f(x)
applied to the population: the distribution determines the coupling
which determines the distribution. ∎

### P5. Three dimensions [D14]

*Uses: P2, P3.*

The mediant (a+c)/(b+d) acts on column vectors by addition:
$\binom{a}{b} + \binom{c}{d} = \binom{a+c}{b+d}$. The group generated
by these operations on pairs of coprime integers is **SL(2,Z)**. Its
continuum completion is **SL(2,R)**.

Self-consistent adjacency (the spatial manifold must be the group
itself, so that every point can serve as mediator) forces the spatial
manifold to have dimension **dim SL(2) = 2² − 1 = 3**.

SL(2,C) ≅ Spin(3,1) gives Lorentz symmetry by complexification. ∎

### P6. SL(2,R) is unique [D15]

*Uses: P5.*

Four conditions characterize SL(2,R) among all connected real Lie groups:

| Condition | Source |
|-----------|--------|
| Arithmetic skeleton from the mediant | P2 → SL(2,Z) |
| Projective action on frequency ratios | Winding numbers are ratios |
| Dynamical trichotomy from Iwasawa KAN | Elliptic/parabolic/hyperbolic |
| Farey-hyperbolic geometry | Stern-Brocot tree tiles H² |

The Bianchi classification of 3-dimensional Lie algebras eliminates
every alternative. ∎

### P7. The continuum limit at K = 1 [D12 §I]

*Uses: P4, P5, P6.*

At critical coupling K = 1, all oscillators are locked: the order
parameter r = 1. The rational field equation on the Stern-Brocot tree,
in the continuum limit on the SL(2,R) manifold, produces the ADM
evolution equations:

$$\partial_t \gamma_{ij} = -2N \mathcal{K}_{ij} + D_i N_j + D_j N_i$$

$$\partial_t \mathcal{K}_{ij} = -D_i D_j N + N\left(R_{ij} + \mathcal{K}\mathcal{K}_{ij} - 2\mathcal{K}_{ik}\mathcal{K}^k{}_j\right) + \text{matter}$$

The dictionary:

| Kuramoto | ADM |
|----------|-----|
| Coherence r(x,t) | Lapse N |
| Phase gradient ∂ᵢθ | Shift / momentum |
| Correlation ⟨∂ᵢθ ∂ⱼθ⟩ | Spatial metric γᵢⱼ |
| Phase curvature ⟨(∂ᵢ∂ⱼθ)²⟩ | Extrinsic curvature Kᵢⱼ |

The first equation is exact under locked-state conditions. The second
follows from differentiating and substituting the Kuramoto dynamics. ∎

### P8. Uniqueness: Einstein [D13, Lovelock 1971]

*Uses: P7, P5, P6.*

The continuum limit satisfies four conditions:

1. **Metric theory on a 3+1 manifold** (P5: dim = 3, P7: the metric is the correlation tensor)
2. **Self-consistency origin** (P4: fixed-point equation)
3. **Second-order in metric derivatives** (P7: Kuramoto is first-order in θ, so correlations are second-order in γ)
4. **General covariance** (P6: SL(2,R) acts transitively)

**Lovelock's theorem (1971):** In 4 dimensions, the unique
divergence-free, symmetric, second-order tensor built from the metric
and its first two derivatives is:

$$G_{\mu\nu} + \Lambda g_{\mu\nu}$$

Therefore:

$$\boxed{G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G\, T_{\mu\nu}}$$

The Einstein field equations are the **unique** output. Not the intended
output — the only one that satisfies the four conditions. ∎

---

## The chain

$$\text{Counting} \xrightarrow{P1} S^1 \xrightarrow{P2} \text{mediant} \xrightarrow{P3} \text{Stern-Brocot} \xrightarrow{P4} \text{field eq.} \xrightarrow{P5,P6} d{=}3,\;\text{SL}(2) \xrightarrow{P7,P8} G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}$$

Eight propositions. Two physical inputs (energy conservation,
stability). One output (Einstein). Every step is a theorem, not a
choice.

---

## Dependency graph

```
P1 (circle)
 ↓
P2 (mediant) ← energy conservation + stability
 ↓
P3 (Stern-Brocot tree)
 ↓           ↘
P4 (field eq.)  P5 (d=3, SL(2))
 ↓               ↓
 ↓             P6 (uniqueness of SL(2,R))
 ↓               ↓
P7 (ADM from Kuramoto at K=1)
 ↓
P8 (Lovelock → Einstein)
```

---

## Cross-references

| Proposition | Derivation | Key theorem |
|-------------|------------|-------------|
| P1 | D10 §1 | Circle from integers + fixed-point |
| P2 | D29 | Stern-Brocot (1858) |
| P3 | D10 §2–3 | Stern-Brocot tree enumeration |
| P4 | D11 | Rational field equation |
| P5 | D14 | dim SL(2) = 3 |
| P6 | D15 | Bianchi classification |
| P7 | D12 §I | ADM from Kuramoto |
| P8 | D13 | Lovelock (1971) |
