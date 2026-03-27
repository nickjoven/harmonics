# 12 Gauge Bosons

**Layer 2 structure.** Composed from Layer 1 derived types: klein.md, signature.md.

## Hypothesis

Directed transitions between 4 Klein bottle modes = gauge bosons.

## Derivation

From **klein.md** + **signature.md**:

1. The Klein bottle immersion has **4 modes** (from signature.md: 3 spacelike + 1 timelike).
2. Each mode can transition to any of the other 3 modes. Transitions are **directed** (A→B ≠ B→A).
3. Total directed transitions: 4 × 3 = **12**.
4. **Sector decomposition**:
   - 8 transitions cross between the two loops of the figure-8 (cross-sector). These are the **gluons**.
   - 4 transitions stay within a single loop (within-sector): 2 + 2 in the two sectors. These are the **electroweak bosons** (unmixed).
5. **Mixing by sin²θ_W = 8/35** (from weinberg.md):
   - The 4 within-sector bosons mix into 3 massive (W⁺, W⁻, Z⁰) + 1 massless (γ).
   - The 8 cross-sector gluons remain unmixed (confinement).
6. Final count: **8 + 3 + 1 = 12**.

## Prediction

**12 gauge bosons** decomposing as **8 gluons + W⁺ + W⁻ + Z⁰ + γ**

## Test

Observed:
- 8 gluons (QCD) ✓
- W⁺, W⁻, Z⁰ (electroweak, massive) ✓
- γ (photon, massless) ✓
- Total: **12** ✓

## Dependencies

- `derived/klein.md` — provides the 4 modes of the Klein bottle
- `derived/signature.md` — provides the (3,1) decomposition into spacelike/timelike
- `structures/weinberg.md` — provides the mixing angle for electroweak decomposition
- `primitives/mediant.md` — adjacency structure
- `primitives/fixpoint.md` — self-consistency of the mode transitions
