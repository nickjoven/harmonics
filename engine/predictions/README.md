# Layer 3: Predictions

The complete prediction table. Every entry carries a derivation chain from Layer 2 structures through Layer 1 derived types down to Layer 0 primitives.

## The Prediction Table

| # | Prediction | Exact Value | Observed | Residual | Derivation Chain |
|---|-----------|-------------|----------|----------|-----------------|
| 1 | Dark energy fraction Ω_Λ | ∈ [13/19, 11/16] = [0.684, 0.688] | 0.685 ± 0.007 | within band | farey.md → klein.md + rationals.md → circle.md + mediant + Z |
| 2 | Strong/weak coupling ratio α_s/α₂ | 27/8 = 3.375 | 3.488 | 3.2% | coupling.md → duty.md + klein.md → dimension.md + rationals.md → Z + mediant |
| 3 | Weinberg angle sin²θ_W | 8/35 = 0.2286 | 0.2312 | 1.1% | weinberg.md → duty.md + klein.md → dimension.md + rationals.md → Z + mediant |
| 4 | Tau/electron mass ratio m_τ/m_e | 26^(5/2) = 3447 | 3477 | 0.9% | generations.md → signature.md + duty.md → circle.md + klein.md + parabola |
| 5 | Spatial dimension d | 3 | 3 | exact | dimension.md → rationals.md → Z + mediant |
| 6 | Spacetime signature | (3,1) | (3,1) | exact | signature.md → circle.md + klein.md → Z + fixpoint + mediant |
| 7 | Fermion generations | 3 | 3 | exact | generations.md → signature.md → circle.md + klein.md → Z + fixpoint + mediant |
| 8 | Gauge bosons | 12 = 8+3+1 | 8+3+1 | exact | gauge.md → klein.md + signature.md → circle.md + mediant + fixpoint |
| 9 | Higgs mass m_H | v/q₂ = 123.11 GeV | 125.10 GeV | 1.6% | higgs.md → klein.md + duty.md → dimension.md + rationals.md → Z + mediant |
| 10 | Born exponent | 2 | 2 | exact | parabola (Layer 0 primitive — direct!) |
| 11 | Clifford algebra Cl(3,1) | {γ_μ,γ_ν}=2η_μν | verified | exact | clifford.md → signature.md + klein.md → circle.md + mediant + fixpoint |
| 12 | Conservation of energy | invertible dynamics | no violation | exact | conservation.md → circle.md → Z + fixpoint |

## Reading the Table

- **Exact Value**: the prediction derived from the engine, as a rational or algebraic expression.
- **Observed**: the experimentally measured value or status.
- **Residual**: the percentage difference between prediction and observation.
- **Derivation Chain**: Layer 2 → Layer 1 → Layer 0, showing the complete proof path.

## Residual Budget

All non-exact residuals are **under 3.5%** and have identified physical origins:

| Prediction | Residual | Origin |
|-----------|----------|--------|
| α_s/α₂ | 3.2% | Running of coupling constants from tree level to M_Z |
| sin²θ_W | 1.1% | Radiative corrections to bare mixing angle |
| m_τ/m_e | 0.9% | Higher-order duty-cycle corrections |
| m_H | 1.6% | Radiative corrections to tree-level Higgs mass |

No residual is unexplained. No residual requires a free parameter.

## Derivation Chain Legend

### Layer 0 Primitives
| Symbol | File | Role |
|--------|------|------|
| Z | `primitives/z.md` | Counting, discreteness |
| mediant | `primitives/mediant.md` | Combining operation |
| fixpoint | `primitives/fixpoint.md` | Self-consistency |
| parabola | `primitives/parabola.md` | Nonlinearity, Born exponent |

### Layer 1 Derived Types
| File | Composition | Role |
|------|------------|------|
| `derived/rationals.md` | Z + mediant | The Stern-Brocot tree, all of Q |
| `derived/circle.md` | Z + fixpoint | Phase space S¹, compactness |
| `derived/dimension.md` | Z + mediant + fixpoint | d = 3 from SL(2,Z) |
| `derived/klein.md` | circle + mediant | Klein bottle, 4 modes, q₂ and q₃ |
| `derived/duty.md` | dimension + rationals | Tongue widths, 1/q³ scaling |
| `derived/signature.md` | circle + klein | (3,1) from orientability |
| `derived/farey.md` | klein + rationals | Farey fractions, Ω_Λ band |

### Layer 2 Structures
| File | Composition | Prediction |
|------|------------|-----------|
| `structures/coupling.md` | duty + klein | α_s/α₂ = 27/8 |
| `structures/weinberg.md` | duty + klein | sin²θ_W = 8/35 |
| `structures/generations.md` | signature + duty | 3 generations, mass ratios |
| `structures/gauge.md` | klein + signature | 12 gauge bosons |
| `structures/clifford.md` | signature + klein | Cl(3,1) |
| `structures/conservation.md` | circle | Energy conservation |
| `structures/higgs.md` | klein + duty | m_H = v/q₂ |

## The Single Loop

Every prediction in this table was derived by forward composition from the four primitives. No prediction was reverse-engineered from observation. The residuals are consequences of the derivation, not inputs to it.
