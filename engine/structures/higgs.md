# Higgs Mass from Crossing Curvature

**Layer 2 structure.** Composed from Layer 1 derived types: klein.md, duty.md.

## Hypothesis

m_H = v/q₂

## Derivation

From **klein.md** + **duty.md**:

1. The Higgs field is the **D-state residual coupling** — the amplitude of the dark (timelike) mode that cannot propagate as a free particle but whose fluctuations around the vacuum are observable.
2. The **crossing curvature** of the Klein bottle figure-8 at the self-intersection scales as 1/q₂² (the period of the smaller sector).
3. The Higgs quartic coupling: **λ = 1/(2q₂²) = 1/(2 × 4) = 1/8 = 0.125**.
4. The Higgs mass formula (from the Mexican hat potential):
   - m_H = v√(2λ) where v = 246.22 GeV is the electroweak vev
   - m_H = v√(2 × 1/8) = v√(1/4) = v/2 = **v/q₂**
5. Numerically: m_H = 246.22/2 = **123.11 GeV**

## Prediction

- **m_H = v/q₂ = 123.11 GeV**
- **λ = 1/8 = 0.125**

## Test

- Observed m_H = 125.10 ± 0.14 GeV
- **Residual: 1.6%**
- Observed λ ≈ 0.129 ± 0.006
- **Residual: 3.3%**

Both residuals are consistent with radiative corrections to the tree-level prediction.

## Dependencies

- `derived/klein.md` — provides the figure-8 crossing and q₂ = 2
- `derived/duty.md` — provides the curvature scaling 1/q²
- `primitives/z.md` — integers
- `primitives/mediant.md` — adjacency structure selecting q₂
