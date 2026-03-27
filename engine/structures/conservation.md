# Conservation from Compactness

**Layer 2 structure.** Composed from Layer 1 derived type: circle.md.

## Hypothesis

Conservation of energy/information follows from S¹ being compact.

## Derivation

From **circle.md**:

1. S¹ is compact (from circle.md: the circle is bounded and closed).
2. Compactness implies **|r| ≤ 1** (the triangle inequality bound on the order parameter).
3. |r| ≤ 1 implies **K_eff ≤ 1** (the effective coupling cannot exceed the compact bound).
4. K_eff ≤ 1 implies the **circle map is invertible** (the map θ → θ + Ω - (K/2π)sin(2πθ) is a diffeomorphism when K ≤ 1).
5. Invertibility implies **information is preserved**: every state has exactly one predecessor and one successor. No states are created, no states are destroyed.
6. At K > 1: the map becomes **non-invertible**, information is destroyed (multiple states map to the same successor), and the fixed-point condition becomes undefined (the system leaves the domain of the engine).

## Prediction

**Matter/energy cannot be created or destroyed** within the domain where the engine applies (K_eff ≤ 1).

## Test

**No violation of energy conservation has ever been observed** ✓

This is the most-tested prediction in all of physics. Every calorimetric measurement, every particle physics conservation check, every thermodynamic cycle — all confirm that information/energy is preserved.

## Dependencies

- `derived/circle.md` — provides S¹ compactness and the |r| ≤ 1 bound
- `primitives/z.md` — the integers (iteration count)
- `primitives/fixpoint.md` — the self-consistency condition (closure)
