# Framework topology

*Dependency map of the canonical state. Each line is "what depends
on what," not "what was discovered when." Read top-down to see
how observables are built; read bottom-up to see what changes if
a foundation moves.*

## Notation

```
A
├── depends on
│   └── B
└── depends on
    └── C
```

means A is derived from B and C. No claim about order of discovery.

---

## L0 — Foundations (no dependencies)

```
four primitives
├── integers (countability)
├── mediant (a/b ⊕ c/d = (a+c)/(b+d))
├── fixed point (x = f(x))
└── parabola (saddle-node normal form: dx/dt = μ − x²)
```

Plus:
- **Klein bottle topology** (compact, non-orientable, no boundary —
  the unique closed surface compatible with antiperiodic + periodic
  identifications)

These are the L0 inputs to everything. Removing any of them removes
the framework.

---

## L1 — Forced selections from L0

### `(q_2, q_3) = (2, 3)`

```
(q_2, q_3) = (2, 3)
└── cross-link uniqueness theorem
    ├── q_2² − 1 = q_3        (from dim adj SU(q_2) reading)
    └── q_3² − 1 = q_2³       (from dim adj SU(q_3) reading)
        └── algebraic proof: a²(a − 2)(a + 1) = 0
```

Source: `mass_sector_closure.md`.

### `d = 3`

```
d = 3 = q_3
└── SL(2, R) characterization
    ├── mediant operates on integer pairs (rank-2)
    └── continuum completion has dim = 2² − 1 = 3
```

Source: `lie_group_characterization.md`, `three_dimensions.md`.

### Klein parity `Z_2 × Z_3`

```
Klein parity
└── Z_2 × Z_3 = Z_6 center
    ├── from XOR filter on Stern-Brocot at (q_2, q_3)
    └── from GCD fiber as principal Z_6-bundle
```

Source: `klein_bottle.md`, `gap3_principal_bundle.py`.

### Signature `(3, 1)`

```
signature (3, 1)
└── {locked, unlocked}² phase states
    ├── 4 states total
    ├── 3 observable (at least one channel locked)
    └── 1 dark (both unlocked, coupling time-averages to zero)
```

Source: `minkowski_signature.md`.

---

## L2 — Derived integers from L1

```
framework alphabet
├── q_2 = 2                     (from L1)
├── q_3 = 3                     (from L1)
├── d = 3                       (from L1, = q_3)
├── MEDIANT = q_2 + q_3 = 5
├── INTERACT = q_2 · q_3 = 6
├── q_2² = 4
├── q_3² = 9 = k_lepton          (squared adjoint reading)
├── q_2³ = 8 = k_quark           (direct adjoint reading)
├── q_2² · q_3 = 12              (Pythagorean N, circle-of-fifths)
├── q_2³ + q_3³ = 35             (sum of cubes, neutrino depth)
├── q_2 · q_3³ = 54              (cosmological hierarchy exponent)
├── q_2³ · q_3 = 24              (down-type sector integer)
├── |F_6| = q_2² + q_3² = 13     (Farey count at INTERACT)
└── |F_7| = |F_6| + INTERACT = 19  (Ω_Λ denominator)
```

Source: `framework_constants.py` (canonical numerical values).

The set `{1, 2, 3, 4, 5, 6, 8, 9, 12, 13, 19, 24, 27, 35, 54}` is
closed under bounded operations on `(2, 3)`. See
`lowest_integer_closure.py` for the generator-side reading.

---

## L3 — Derived structural laws from L2

### Integer conservation law

```
depth × |3Q| = k_sector
├── k_lepton = q_3² = 9          (chiral-doubled SU(2) adjoint)
├── k_quark = q_2³ = 8           (direct SU(3) adjoint)
└── consequences:
    ├── lepton depth = 3 (from |Q| = 1)
    ├── up-type depth = 4 (from |Q| = 2/3)
    └── down-type depth = 8 (from |Q| = 1/3)
```

Source: `integer_conservation_law.py`, `mass_sector_closure.md`.

### Per-sector base pairs

```
sector (b_1, b_2) pair
├── lepton: (3/2, 5/3)            (Fibonacci F_4/F_3, F_5/F_4)
├── up-type: (8/5, 3/2)           (Fibonacci shift F_6/F_5, F_4/F_3)
└── down-type: (5/4, 9/8)         (Klein parity double-cover)
```

Source: `sector_base_pairs.py`. Down-type's pair is the only sector
with Klein parity +1 (orientation-preserving), giving the q_2 q_3
double-cover scaling.

### Sector integers `N_sector`

```
N_sector = (a_1 K*)²
├── N_lep = q_2² = 4
├── N_up = q_3² = 9               (from Fibonacci shift, ×(q_3/q_2)²)
└── N_dn = q_2³ q_3 = 24          (from Klein-parity double-cover)
```

Source: `item12_cross_sector_derivation.py`.

### Tongue audit (reading D)

```
framework w(p/q, K)
├── = saddle-node μ in (x, μ) normal-form coordinates
└── ≠ Ω-space Arnold tongue width  (these differ by π factor)
```

Source: `tongue_formula_accuracy.py`. Resolves the perturbative ↔
critical ambiguity at q = 6 that otherwise blocks K\* derivation.

---

## L4 — Tree-scale coupling

```
K_STAR_PRECISE = 0.86196052
├── joint matter-sector self-consistency
│   ├── a_1(lep) · K* = √4 = 2     (single-step a_1 from m_τ/m_μ)
│   ├── a_1(up)  · K* = √9 = 3     (single-step a_1 from m_t/m_c)
│   └── a_1(dn)  · K* = √24         (single-step a_1 from m_b/m_s)
├── three-sector χ²/dof = 0.06
└── input: PDG 2024 mass ratios + sector integers from L3
```

Source: `item12_K_star_closure.py`, `item12_C_from_K_star.py`.

K\* drops out as the unique value making all three sectors sit on
the same parabola. Not fit to any single observable — joint over
three.

---

## L5 — Predicted observables

### Mass sector (charged)

```
m_τ, m_μ, m_e, m_t, m_c, m_u, m_b, m_s, m_d
└── two-step Fibonacci formula per sector
    ├── m(gen3)/m(gen1) = exp(a_1 · denom)
    │   └── a_1 = √N_sector / K_STAR_PRECISE  (from L4)
    └── matches PDG at sub-1σ across all three sectors
```

Source: `item12_cross_sector_derivation.py`.

### Neutrino sector

```
m_1, m_2, m_3
├── depth = q_2³ + q_3³ = 35     (from L2)
├── m_3 = v · (K*/2)^35 · ∛2
├── m_1 = m_3 / q_2³ = m_3 / 8   (exact)
└── m_2 = m_1 · (√3 − 1/(q_2 q_3)²) = m_1 · (√3 − 1/36)
    ├── atmospheric Δm² at 0.31σ of NuFIT
    └── solar Δm² at 0.12σ of NuFIT
```

Source: `item12_neutrino_solar_closure.py`.

### Gauge sector

```
sin² θ_W
├── tree: 8/35 = q_2³/(q_2³ + q_3³)
└── + Fibonacci-square correction: 8/F_10² = 8/3025
    └── total = 0.23122 (matches PDG to ~2×10⁻⁵)

α_s / α_2
├── tree: 27/8 = q_3³/q_2³
└── + gauge-integer correction: 1/q_3² = 1/9
    └── total = 251/72 = 3.4861 (matches PDG to 0.17%)
```

Source: `item12_sin_W_and_signs.py`, `item12_other_residuals.py`.

### Higgs

```
λ
├── tree: 1/(2 q_2²) = 1/8
└── + boundary correction: 1/228 = 1/(q_2² q_3 |F_7|)
    └── total = 0.129 (matches PDG)

m_H / v
└── 1/q_2 = 1/2 (matches PDG to 1.7%)
```

Source: `higgs_from_tongue_boundary.md`, commit `fc677bc`.

### Cosmology

```
Ω_Λ
├── topology: Ω_Λ ∈ [13/19, 11/16]  (Farey partition bounds)
├── boundary weight w*: dynamics gives the point
└── Ω_Λ = 0.6847                   (matches Planck)

R = Planck/Hubble
└── 6 × 13^54
    ├── 6 = INTERACT
    ├── 13 = |F_6|
    └── 54 = q_2 · q_3³
        └── matches observed at 0.48%

Λ · l_P²
└── 13^(−108) / 12               (108 = 2 × 54)
```

Source: `farey_partition.md`, `boundary_weight.md`, `hierarchy.md`.

### Spectral tilt

```
n_s
├── ∼ 0.965
└── eigenvalue separation of x² − x − 1 = 0  (golden ratio polynomial)
```

Source: `alphabet_check.py`, `tier2_extensions.py`.

### Generation count

```
3 generations
├── 4 phase states (locked,unlocked)²
└── 1 dark
    └── 4 − 1 = 3 observable
```

A 4th charged lepton is forbidden by the integer conservation law:
depth ≥ 4 violates `4 × 3 > k_lepton = 9`.

---

## Sensitivity (reverse direction)

What breaks if a foundation moves:

```
if (q_2, q_3) ≠ (2, 3):
    ├── L2: every alphabet integer changes
    ├── L3: integer conservation law fails
    ├── L4: K_STAR_PRECISE has no joint fit
    └── L5: every mass observable shifts
        └── (the framework no longer matches PDG)

if d ≠ 3:
    ├── SL(2, R) is no longer the spatial group
    ├── duty cycle 1/q^d gives wrong coupling tree values
    ├── Lorentz signature is no longer (3, 1)
    └── neutrino depth q_2³ + q_3³ no longer = 35

if Klein parity ≠ Z_2 × Z_3:
    ├── XOR filter no longer selects (2, 3)
    ├── down-type Klein-parity double-cover scaling fails
    └── N_dn ≠ q_2³ q_3 (down sector closures break)

if K_STAR_PRECISE has a small correction Δ:
    ├── all three a_1 values shift by Δ/K*
    ├── lepton, up, down mass ratios shift by ~ exp(Δ · denom)
    ├── neutrino spectrum shifts by ~ Δ · 35  (depth-amplified)
    └── boundary weight w* shifts via Ω_Λ(K*)

if PDG ratios drift:
    ├── K_STAR_PRECISE refits within 2.06×10⁻⁵
    └── joint χ²/dof increases above 0.06
        └── above ~1, sector identities break and N_sector
            assignments need re-derivation
```

The most fragile point is K\* itself: a derivation from first
principles (rather than joint fit to PDG) is the largest open
structural item. The most robust point is the cross-link uniqueness
— the integers are forced by integer arithmetic alone.

---

## What this map omits

- **Chronology.** Order of discovery is in the git history, not in
  the topology. None of that belongs here.
- **Retracted intermediate results.** Anything not in the current
  code/topology is not canonical. Derive item status from code + this
  topology directly.

## How to use this topology

1. **Before deriving:** find where in the topology your candidate
   would sit. If it's already at L2/L3/L4 you're re-deriving
   canonical work; if it's a refinement to L4 or a new closure at
   L5, proceed.
2. **When verifying:** trace the dependencies upward to make sure
   every input is canonical. If you find yourself relying on a
   retracted intermediate, you are off the canonical path.
3. **When discovering an inconsistency:** locate it on the graph
   and walk one level up. The inconsistency is usually at the
   level above what you noticed (a wrong projection of `a_1` is
   really a wrong reading at L3, not L4).
4. **When updating:** every new closure should add to L5; every
   refinement to K\* updates L4; every refinement to a sector
   integer updates L3. If you find yourself adding to L1 or L0,
   you are doing foundational work and should expect everything
   downstream to need re-verification.

---

*This document is intentionally short. Topology should fit in one
read. If it grows, split it by sector (mass, gauge, cosmology,
gravity, QM) rather than by depth, and let each sector point back
at its L0/L1 inputs.*
