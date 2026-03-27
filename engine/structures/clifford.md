# Cl(3,1) from the Figure-8 Crossing

**Layer 2 structure.** Composed from Layer 1 derived types: signature.md, klein.md.

## Hypothesis

The Clifford algebra Cl(3,1) arises from the crossing geometry of the Klein bottle.

## Derivation

From **signature.md** + **klein.md**:

1. The Klein bottle figure-8 immersion has **4 modes** = 2 loops × 2 modes/loop.
2. Each mode defines a **generator** γ_μ based on its topological character:

   **Spacelike generators** (stay/cross without twist, γ² = +I):
   - γ_A = σ₁ ⊗ I (stay on loop 1)
   - γ_B = σ₃ ⊗ σ₁ (cross to loop 2, no twist)
   - γ_C = σ₃ ⊗ σ₃ (cross to loop 2, return)

   **Timelike generator** (cross WITH twist, γ² = -I):
   - γ_D = J ⊗ I where J = [[0, -1], [1, 0]]
   - J² = -I because a double half-twist = full twist = orientation reversal

3. The twist is what makes the Klein bottle non-orientable. Algebraically, J² = -I encodes this non-orientability as the **timelike signature**.

## Prediction

**{γ_μ, γ_ν} = 2η_μν** with η = diag(+1, +1, +1, -1)

All 10 independent anticommutation relations:
- 4 diagonal: γ_A² = γ_B² = γ_C² = +I, γ_D² = -I
- 6 off-diagonal: {γ_μ, γ_ν} = 0 for μ ≠ ν

## Test

All 10 anticommutation relations **verified algebraically** (clifford_figure8.py) ✓

The verification is purely algebraic — no numerical approximation, no fitting. The Clifford algebra is an exact consequence of the crossing geometry.

## Dependencies

- `derived/signature.md` — provides the (3,1) mode decomposition
- `derived/klein.md` — provides the figure-8 immersion and its crossing structure
- `derived/circle.md` — provides S¹ (the loops of the figure-8)
- `primitives/fixpoint.md` — self-consistency of the algebra
- `primitives/mediant.md` — adjacency of modes
