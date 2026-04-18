# Gap 2 Break 1: Spatialization Decomposition and Status

## Sub-problems

| | Sub-problem | Status | Result |
|---|---|---|---|
| A | RFE forces Q → R completion | **Closed** | Phase sum in the self-consistency equation produces irrational |r| from rational inputs. The field exists because the equation demands it. (`rfe_irrational_fixed_points.py`) |
| B | Mori–Zwanzig coarse-graining | **Closed** (Markovian level) | Standard projection with inputs from C (decorrelation rate) and D (continuum manifold). Markovian limit valid for τ_coarse ≫ 1/λ_unlock. |
| C | Lyapunov exponent from Klein bottle | **Closed** | λ_unlock(K) = 2∫_{cos<0} ln(1+K|cosθ|)dθ. Positive for all K>0, monotone increasing, limit ~0.473 as K→1. Expanding sector is exactly 50% of the circle. Non-orientability ensures unpaired (h_KS > 0). |
| D | Irrational completion → continuum H² | **Closed** (classical) | Ford circle packing tessellates H² (Ford 1938). The Stern-Brocot tree completes to H² as depth → ∞. Standard diffusion on H² via Laplace–Beltrami. |
| E | Bare diffusion D₀ | **Open** | D₀ = ½λ_unlock·ℓ_c². λ is computed (C). ℓ_c is not: ℓ_P fails by ~10⁶⁶; tree-depth route viable but introduces depth↔scale correspondence. Likely irreducible input. |

## The chain

```
Primitives (integers + mediant + fixed point + parabola)
    ↓ [A: fixed point on tree with phases]
RFE has irrational solutions → Q completes to R
    ↓ [D: Ford 1938]
R fills H² = SL(2,R)/SO(2) → continuum spatial manifold
    ↓ [C: circle map derivative, cos<0 sector]
Unlocked oscillators have λ_unlock > 0 → exponential decorrelation
    ↓ [B: Mori–Zwanzig, Markovian limit]
Coarse-grained ⟨θ⟩ satisfies Langevin with D₀·∇²⟨θ⟩
    ↓ [gap2_theorem_attempt.md Step 6: Ad-invariance]
D_{ij} = D₀·κ_{ij} → scalar Laplacian on H²
    ↓ [E: ℓ_c — OPEN]
D₀ = ½·λ_unlock·ℓ_c² → one irreducible dimensionful input
```

## Key results

### λ_unlock from the circle map (sub-problem C)

For the standard circle map θ → θ + Ω − (K/2π)sin(2πθ), the
derivative is dθ'/dθ = 1 − K cos(2πθ). The expanding sector
(|derivative| > 1) is {θ : cos(2πθ) < 0} = exactly half the circle.

| K | λ_unlock | λ_locked | sum (= 0 by Jensen) |
|---|---|---|---|
| 0.5 | +0.269 | −0.408 | −0.069 |
| 0.8 | +0.397 | −0.843 | −0.223 |
| 0.9 | +0.436 | −1.099 | −0.331 |
| 0.99 | +0.469 | −1.772 | −0.649 |

The average over the FULL circle is 0 (Jensen's formula for
analytic functions). The average over the EXPANDING sector alone
is positive. Non-orientability (K²) ensures this positive exponent
is not cancelled by a paired negative exponent — time-reversal
would pair them, but the Klein bottle forbids global time-reversal.

### RFE irrationality (sub-problem A)

At depth 3 (9 nodes), the order parameter |r| at K = 1 is
0.20731..., with best rational approximation 1747/8427 (error
~10⁻⁸). The self-consistency equation |r| = f(|r|) at every
tested depth and coupling produces irrational fixed points. The
mechanism: e^{2πi·p/q} at rational p/q is algebraic but not
rational; the weighted sum is irrational.

### D₀ obstruction (sub-problem E)

D₀ = ½·λ_unlock·ℓ_c² with λ computed and ℓ_c unknown. Identifying
ℓ_c = ℓ_P gives D₀ ~ 10⁻⁷⁰ m²/s, which is 10⁶⁶× too small
(ℏ/2m_e ~ 10⁻⁵ m²/s). Therefore ℓ_c ≠ ℓ_P. The tree-depth route
(ℓ_c = 1/(2F_d²) in hyperbolic units) is viable but introduces the
tree-depth ↔ energy-scale identification as an input. This is the
remaining irreducible input for the quantum sector.

## References

- `gap_2_spatial_diffusion.md` — problem statement
- `gap2_theorem_attempt.md` — topological route (Steps 1–7)
- `gap2_step4_farey_laplacian.md` — graph-theoretic route
- `rfe_irrational_fixed_points.py` — sub-problem A verification
- `rational_field_equation.md` — the RFE definition
- `second_law_topological.md` — non-orientability → h_KS > 0
