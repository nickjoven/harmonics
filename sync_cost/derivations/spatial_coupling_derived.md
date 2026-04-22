# Spatial Coupling Derived from Gate Propagation

## Claim

The spatial coupling term D∇²θ in the extended Kuramoto equation
(Derivation 12, §2) is not an independent assumption. It is the
unique lowest-order coupling consistent with three already-derived
results:

1. **Finite gate propagation speed c** (D31)
2. **Spatial dimension d = 3** with isotropy (D14)
3. **Locality from causal structure** (D31 + D32)

The form of the coupling (diffusive, local, isotropic) is forced.
Only the overall scale D remains, and it is determined by D₀ = 1/2
from the Stern-Brocot tree geometry (D45).

---

## 1. Locality from finite c

**Theorem.** If information propagates at finite speed c (D31),
then the coupling kernel K(x,x') has compact support: K(x,x') = 0
for |x - x'| > cΔt, where Δt is the gate period.

**Proof.** In D31, c is the gate propagation speed — the rate at
which phase coincidence sweeps through the coherent medium. An
oscillator at position x can only influence oscillator x' if a
gate-opening at x reaches x' within one gate period. The gate
opens for duration Δt_gate and propagates at speed c. Therefore
the influence of x reaches at most to x + cΔt_gate.

For the q = 1 fundamental mode at K = 1: Δt_gate ~ 1/(2π) of the
period T, so the causal range is cT/(2π) = λ/(2π), where λ = cT
is the coherence wavelength. For higher modes (q > 1), the gate
is narrower and the causal range shorter.

The coupling kernel is therefore local: K(x,x') is negligible
beyond the coherence length. This is not assumed — it follows from
the finite speed of gate propagation, which is itself derived from
the nilpotent generator N₊ of sl(2,R) (D31).

**Status**: Derived. Uses only D31 (c finite) and the gate
mechanism.

---

## 2. Isotropy from the group manifold

**Theorem.** If the spatial manifold is SL(2,R) acting on itself
by left multiplication (D14, Step 3c), then the coupling kernel
K(x,x') depends only on |x - x'| (the geodesic distance), not
on direction.

**Proof.** In D14, the spatial manifold M = SL(2,R) with the
self-consistent adjacency condition. The isometry group of SL(2,R)
with its Killing metric acts transitively on tangent directions at
each point (the adjoint action of SL(2,R) on sl(2,R) is the
isometry group of the metric at the identity, and left translation
carries this to every point).

More precisely: the Killing form B(X,Y) = 4 tr(XY) on sl(2,R) is
Ad-invariant. The induced left-invariant metric on SL(2,R) has
isometry group SL(2,R)_L × SL(2,R)_R (left and right multiplication).
At any point g, the isotropy of the right action on the tangent
space TgG ≅ sl(2,R) is the full adjoint action Ad(G), which acts
transitively on unit vectors.

Therefore any physical quantity that depends only on the group
structure — including the coupling kernel, which is the Green's
function of the coherence tensor (D12, D46) — must be isotropic.

The coupling K(x,x') = K(d(x,x')) where d is the bi-invariant
distance on SL(2,R).

**Status**: Derived. Uses only D14 (M = SL(2,R)) and the Killing
metric.

---

## 3. Diffusive form from Taylor expansion

**Theorem.** A local, isotropic coupling kernel acting on a phase
field θ(x) produces, to lowest nontrivial order, the Laplacian:

    ∫ K(|x - x'|) [θ(x') - θ(x)] d³x' = D∇²θ + O(∇⁴θ)

where D = (1/6) ∫ K(r) r² d³r (in d = 3 dimensions, with the
factor 1/(2d) = 1/6 from the angular average).

**Proof.** Expand θ(x') in a Taylor series around x:

    θ(x') = θ(x) + (x' - x)ⁱ ∂ᵢθ + ½(x' - x)ⁱ(x' - x)ʲ ∂ᵢ∂ⱼθ + ...

The difference θ(x') - θ(x) eliminates the zeroth-order term.
Substitute into the integral:

    ∫ K(|x-x'|)[θ(x')-θ(x)] d³x'
      = ∂ᵢθ ∫ K(r) rⁱ d³r'
      + ½ ∂ᵢ∂ⱼθ ∫ K(r) rⁱrʲ d³r'
      + ...

where r = x' - x, r = |r|.

**First-order term vanishes by isotropy.** Since K depends only on
|r|, the integral ∫ K(r) rⁱ d³r = 0 by the symmetry r → -r. This
is a direct consequence of the isotropic coupling (Section 2).

**Second-order term gives the Laplacian.** By isotropy:

    ∫ K(r) rⁱrʲ d³r = (δᵢⱼ/d) ∫ K(r) r² d³r

where d = 3 is the spatial dimension. Therefore:

    ½ ∂ᵢ∂ⱼθ × (δᵢⱼ/3) ∫ K(r) r² d³r = D∇²θ

with D = (1/6) ∫ K(r) r² d³r.

**Higher orders are suppressed.** The fourth-order term gives
∇⁴θ, which is O(a²/L²) smaller than ∇²θ, where a is the lattice
spacing (coherence length at the cutoff scale) and L is the
macroscopic length scale. At scales L >> a, only the Laplacian
survives.

This is the same argument that gives Fourier's law from microscopic
interactions, Fick's law from random walks, and the heat equation
from nearest-neighbor coupling. It is universal for local isotropic
kernels on Rⁿ (or, by the same expansion, on any Riemannian
manifold in normal coordinates).

**Status**: Derived. This is a standard result in continuum
mechanics / kinetic theory. The inputs are locality (Section 1)
and isotropy (Section 2), both derived.

---

## 4. The diffusion constant from tree geometry

From D45 (coupling_scales.md): the bare diffusion constant on the
Stern-Brocot tree is D₀ = 1/2, set by the symmetric binary random
walk with unit root spacing. The effective diffusion constant after
RG coarse-graining over tree levels is:

    D_eff = D₀ / (1 - φ⁻⁴) = (1/2) / (1 - 1/φ⁴)

where φ⁴ = (7 + 3√5)/2 ≈ 6.854, giving:

    D_eff = (1/2) × φ⁴/(φ⁴ - 1) = φ⁴/(2(φ⁴ - 1))
          = 6.854 / (2 × 5.854)
          ≈ 0.5854

This is the value identified with ℏ/(2m) in D12 Part II
(Schrödinger derivation). The tree geometry determines the
diffusion constant with no free parameter.

**Status**: Derived (D45). The value D₀ = 1/2 comes from the
binary structure of the Stern-Brocot tree (each node has exactly
two children: left mediant and right mediant).

---

## 5. Uniqueness of the Laplacian

**Theorem.** On a d-dimensional Riemannian manifold, the Laplacian
∇² is the unique second-order differential operator that is:
1. Linear
2. Scalar (invariant under isometries)
3. Elliptic (positive-definite principal symbol)

**Proof.** This is a classical result. A second-order scalar linear
operator on (M, g) has the form:

    L = aⁱʲ∇ᵢ∇ⱼ + bⁱ∇ᵢ + c

Isometry invariance forces aⁱʲ = αgⁱʲ (the metric is the only
isometry-invariant rank-2 tensor), bⁱ = 0 (no isometry-invariant
vector field on a homogeneous space), and c = 0 (the operator acts
on differences, not absolute values). Therefore L = α∇², and α is
absorbed into the diffusion constant D.

In d = 3 with the SL(2,R) Killing metric (D14), the Laplacian is
the Casimir operator of the left-regular representation. It is
unique up to the overall scale D.

**Status**: Theorem (Helgason, *Differential Geometry, Lie Groups,
and Symmetric Spaces*, 1978, Ch. II). Applied here with the
isometry group from D14.

---

## Summary

The derivation chain:

    D31 (finite c)  →  locality (Section 1)
    D14 (M = SL(2,R))  →  isotropy (Section 2)
    locality + isotropy  →  ∇² is the unique operator (Sections 3, 5)
    D45 (D₀ = 1/2)  →  D_eff = φ⁴/(2(φ⁴-1)) (Section 4)

Assembling: the spatial coupling term is

    D_eff ∇²θ

with D_eff determined by the tree geometry. No free parameter
consumed. No assumption beyond D31, D14, D45.

---

## What this closes

| Gap | Before D48 | After D48 |
|-----|-----------|-----------|
| Spatial coupling form | Assumed (diffusive, local, isotropic) | **Derived** from c + d=3 + SL(2,R) |
| Diffusion constant D | Free parameter | **Derived** from tree geometry (D₀ = 1/2, D45) |
| §8.4 of gap analysis | Open | **Closed** |

The extended Kuramoto equation

    ∂θ/∂t = ω(x) + D_eff ∇²θ + K(x) r sin(ψ₀ - θ)

now has every term derived:
- ω(x): natural frequency (input = frequency distribution g(ω))
- D_eff ∇²θ: spatial coupling (this derivation)
- K(x) r sin(ψ₀ - θ): mean-field coupling (Kuramoto, D12)

---

## Proof dependencies

- **D14** (`three_dimensions.md`): M = SL(2,R), d = 3, isotropy
- **D31** (`speed_of_light.md`): finite c from gate propagation
- **D32** (`minkowski_signature.md`): causal structure from (3,1)
- **D45** (`coupling_scales.md`): D₀ = 1/2 from tree geometry
- **D12** (`continuum_limits.md`): the equation being closed

---

## Proof chains

This derivation closes the spatial coupling assumption in:

- [**Proof A: Polynomial → General Relativity**](PROOF_A_gravity.md) — the K=1 limit now has no spatial coupling assumption
- [**Proof B: Polynomial → Quantum Mechanics**](PROOF_B_quantum.md) — the K<1 Schrödinger derivation's D∇²θ term is fully derived
