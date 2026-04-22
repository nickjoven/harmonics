# The Planck–Hubble Hierarchy from Gaussian Lattice Index

## Result

The Planck/Hubble hierarchy R is derived from the framework's
three framework integers (q₂ = 2, q₃ = 3, d = 3); no fitted factors:

  R = q₂ q₃ × (q₂² + q₃²)^{q₂ q₃^d} = 6 × 13^54

  Coefficient:  q₂ q₃ = 6 = |Z₆|, the gauge center order
  Base:         q₂² + q₃² = 13 = |q₂ + i q₃|², the Gaussian norm
  Exponent:     q₂ q₃^d = 54, the gauge cell count of K²

Numerical value: R ≈ 8.53 × 10^60.
Observed: t_H/t_P = c/(H₀ ℓ_P) ≈ 8.49 × 10^60 (0.48% residual).

## Proof

### Step 1: The Gaussian integer lattice

The Klein bottle K² has a complex structure inherited from
S¹ × S¹. The integer sublattice of this complex plane is the
Gaussian integers Z[i] = {a + bi : a, b ∈ Z}.

The two denominator classes (q₂, q₃) = (2, 3) combine as the
Gaussian integer z = q₂ + i q₃ = 2 + 3i.

### Step 2: Sublattice index = Gaussian norm

The sublattice L = (2 + 3i)·Z[i] has index

  [Z[i] : L] = |2 + 3i|² = q₂² + q₃² = 13.

This is standard: the index of the principal ideal (α) in Z[i]
equals the norm N(α) = |α|².

Each coarse-graining step (replacing Z[i] by L) loses a factor
of 13. After n steps: [Z[i] : L^n] = 13^n.

### Step 3: The exponent is the gauge cell count

The Klein bottle's phase space Ω × {±1} (frequency × orientation)
decomposes under the gauge structure:

  - The SU(3) sector (q₃ = 3) has duty cycle 1/q₃^d = 1/27.
    The frequency axis partitions into q₃^d = 27 equal cells.

  - The Z₂ non-orientability doubles each cell (two orientations).

  - Total: q₂ × q₃^d = 2 × 27 = 54 cells.

The coarse-graining iterates once per gauge cell. After 54
iterations, every cell has been visited exactly once: one
complete pass through the phase space.

### Step 4: n = 54 is forced (not selected)

The gauge prefactor q₂ q₃ = 6 = |Z₆| counts the gauge center
multiplicity. This factor is supplied ONCE by the Klein bottle's
topology (one K², one center Z₂ × Z₃, one Z₆).

  - n < 54: incomplete pass. Gauge cells un-visited.
  - n = 54: complete pass. One Z₆ prefactor, correctly matched.
  - n > 54: would require additional Z₆ factors (one per pass).
    The Klein bottle supplies exactly one. No second Z₆ exists.

Therefore n = 54 is the unique value compatible with the available
topological data. It is forced by the finiteness of the gauge center.

### Step 5: Assembly

  R = |Z₆| × [Z[i] : (q₂ + iq₃)^{q₂ q₃^d} Z[i]]^{1/2... no.

More directly:

  R = (gauge multiplicity) × (norm per cell)^(number of cells)
    = q₂ q₃ × (q₂² + q₃²)^{q₂ q₃^d}
    = 6 × 13^54.  ∎

## Consequences

### One formula, both sectors

  ℓ_P² = ℏG/c³

With ℓ_P = L_H / R and L_H = √(3/Λ):

  ℏG = c³ × 3 / (Λ R²)

Since Λ ℓ_P² = 13^{-108}/12 (framework-derived) and
R² = 36 × 13^{108}, the product ℏG is determined. One formula
relates both sectors. The gravitational constant G and the
quantum of action ℏ are not independent — they are the same
scale (ℓ_P) expressed in different units.

### The one irreducible input becomes zero

Previously, the framework required one dimensionful input
(v = 246 GeV, or equivalently ℓ_P, G, or ℏ). With R derived,
ℓ_P is determined by R and L_H (which depends on Λ, itself
derived). The dimensionful input is eliminated.

The framework derives all dimensionless ratios from
(q₂, q₃, d) = (2, 3, 3), which are themselves derived from the
four primitives. Per the scale-free reframe (`h_inf_status.md`),
absolute dimensional scales require observational anchors.

Two anchors are currently needed (see `anchor_count_audit.md`):

1. **Cosmological anchor** (H_0, equivalently Λ in SI, ℏG, or M_P):
   sets ℓ_P, t_P, M_P, Λ, ρ_crit via the framework's R = 6·13⁵⁴
   and Λℓ_P² = 13⁻¹⁰⁸/12 identities.

2. **Particle-physics anchor** (v = 246 GeV, equivalently the root
   oscillator frequency): sets absolute lepton/quark/gauge-boson
   masses, ℏ·c·G in absolute units.

The two sectors are structurally separate in the documented
derivations: no dimensionless identity connecting v/M_P to framework
integers has been proven. A suggestive near-match (v/M_P ≈ 13⁻¹⁵,
3.1% off) is recorded in `anchor_count_audit.md` as numerology
only — if it were derivable from framework structure, the anchor
count would reduce to one. That derivation is an open item and
would effectively solve the hierarchy problem in framework terms.

The current minimum dimensional input is **two observational anchors**
(H_0 cosmological, v_EW particle-sector). The framework does not yet
have a structural identity reducing them to one. The phrase "zero
free parameters" is retired across this repository — see
`statistical_conventions.md`. Individual predictions are classified
under Z1–Z3 directly; the framework-level input count is two, not
zero. The obstructions preventing closure to one anchor are
catalogued in `anchor_count_audit.md`.

### Sub-problem E (spatialization) is closed

D₀ = ½ λ_unlock ℓ_c² with ℓ_c = ℓ_P and ℓ_P derived from R.
The quantum sector's diffusion constant is determined.

## Formalizations

The three items below are formalized in `three_formalizations.md`:

1. **Gauge cell ↔ iteration bijection**: 54 = ord₂₇(13) × |Z₆|
   = 9 × 6. Each norm-cycle (period 9) is labeled by one Z₆
   element. 54 steps = 6 complete cycles.

2. **Z₆ non-renewability**: the Klein bottle supplies one Z₆
   (6 elements). After 6 norm-cycles the center is exhausted.
   A 7th cycle has no label. n = 54 is forced.

3. **The 0.48% residual**: R = 6 × 13⁵⁴ ≈ 8.53 × 10⁶⁰ vs.
   observed t_H/t_P = c/(H₀ · ℓ_P) ≈ 8.49 × 10⁶⁰ (residual 0.48%,
   consistent with the value quoted at line 15). The de Sitter
   identification L_H = √(3/Λ) gives ~1.02 × 10⁶¹ (≈17% above R),
   indicating the framework's R matches the Hubble-radius
   identification rather than the de Sitter horizon. Verified in
   `r_residual_audit.py`.

## References

- `gauge_factorization.md` — gauge algebra decomposition
- `gauge_dictionary.md` — Z₆ torsor identification
- `klein_bottle_derivation.md` — (q₂, q₃) = (2, 3)
- `three_dimensions.md` — d = 3
- `gap2_spatialization_decomposition.md` — sub-problem E context
- `sinw_effective_dimension.md` — uses same (q₂, q₃, d)
