# Klein-antipodal Z₂ representation theory: a recurring derivation
pattern

## What this file does

Point at three independent framework derivations that use the
same underlying machinery — Klein-antipodal Z₂ representation
theory on finite lattices built from framework integers. The
machinery is not one-off; it's a pattern.

## The pattern

1. **Lattice** `L = Z_{q_2} × Z_{q_3}` (or a Farey / Stern-Brocot
   subset thereof), a finite set of framework-integer residues.
2. **Klein action** `τ`: an antipodal or flip involution
   (e.g., `τ(x, y) = (1 − x, −y)` on `Z_2 × Z_3`; or
   `k → q_2·q_3 − k` on Z_6).
3. **Irreducible Z₂ decomposition.** For each antipodal pair
   `{ψ_p, ψ_{τ(p)}}`, form two eigenmodes:

       ψ_+ = ψ_p + ψ_{τ(p)}   (trivial Z₂ rep, Klein-singlet)
       ψ_- = ψ_p - ψ_{τ(p)}   (sign Z₂ rep, monodromy −1)

   Klein-singlets have single-valued phase around the Klein loop
   (can carry definite charge). Sign-rep modes have two-valued
   phase (net charge integrates to zero; gravitates only).
4. **Observable**: a framework-integer ratio that follows from
   the count of Klein-singlets vs sign-rep modes, or from the
   intersection of Klein-singlet with a sector criterion (e.g.,
   "coprime-to-6").

## Three independent applications

### Down-type quarks: `a_1(down)² / a_1(lep)² = q_2 · q_3 = 6`

- File: `down_type_double_cover_closed.md`.
- Lattice: `L = Z_2 × Z_3`, 6-point orbit of `G = ⟨τ, σ⟩`.
- Theorem: `dim F^⟨τ⟩ = |L|/|⟨τ⟩| = 3 = q_3`, `dim F^G = 1`.
- Observable ratio: factor 6 = q_2 · q_3 between down-type and
  lepton base-pair exponents.
- Numerical status: **0.04σ vs PDG 2024** (five-digit match).

### Up-type quarks: `a_1(up) · K_STAR = √N_up = 3`

- File: `item12_K_star_closure.py`, `uptype_base_pair_sweep.py`.
- Klein parity `−1` on Fibonacci shift applied to matter modes.
- `N_up = q_3² = 9`.
- Observable: up-type a_1 normalized by K_STAR equals the
  structural integer 3.
- Numerical status: **0.34σ vs PDG** (m_c dominated uncertainty).

### Ω partition: `Ω_Λ : Ω_DM : Ω_b = 13 : 5 : 1 / 19`

- File: `omega_partition_combinatorial.md`, `baryon_fraction.md`.
- Z_6 residues under Klein-antipodal `k → 6 − k`.
- (sym, antisym) eigenmode decomposition on each swapped pair;
  self-paired modes are Klein-singlets.
- Baryonic ≡ Klein-singlet ∩ coprime-to-6 → exactly one mode:
  `ψ_+(1, 5)`.
- Numerical status: 0.07σ (Ω_Λ), 0.7% (Ω_DM), 6.7% (Ω_b).

## Why this is structural, not numerological

Per Z1-Z3 in `statistical_conventions.md`:

- All three applications use only framework integers
  `(q_2, q_3, d)` — no fitted factors. **Z2 met.**
- Observational inputs are anchoring (PDG masses, Planck
  densities), labeled. **Z3 met.**
- Numerical matches are ≤ 1σ for the partition and down-type,
  ≤ 1σ for up-type. **Z1 met.**

The common machinery passes all three Z-conditions in the
specific derivations where it's been applied. The pattern is
the framework's most-leveraged derivational tool.

## Limits of the pattern (what's NOT derivable this way)

- **Absolute mass scales**: the pattern produces dimensionless
  ratios (factor 6, factor 9, 13:5:1) but not absolute values.
  Absolute m_t, m_b, Ω_b require the v_EW and H_0 anchors.
- **Numerical coincidences at higher precision**: the
  K_STAR¹⁴ = 1/8 closed form (`CHAIN_KSTAR.md`) uses different
  reasoning (algebraic chain, not Klein-antipodal Z₂ rep); it
  is Class 4 pending audit and may not extend the pattern.
- **Continuous parameters of the SM** (CKM, PMNS, fermion mass
  ratios): not currently derived via this machinery. The
  open-problem items in `framework_status.md` Proposed are not
  obviously in scope.

## What this file changes

Nothing numerical. It consolidates a recurring derivation
pattern into a single cross-reference so future structural
claims invoking Klein-antipodal Z₂ rep theory can point at this
file rather than re-deriving from scratch.

## Cross-references

| File | Application |
|---|---|
| `down_type_double_cover_closed.md` | Factor 6 from L = Z_2 × Z_3 |
| `item12_K_star_closure.py` | Factor 9 from Klein parity −1 |
| `uptype_base_pair_sweep.py` | Up-type structural base pair |
| `omega_partition_combinatorial.md` | 1:5 subdivision from sym/antisym |
| `baryon_fraction.md` | 13:5:1/19 via the same machinery |
| `fermion_spinors_from_z2.py` | H₁(K²) = Z ⊕ Z₂ — the torsion source |
| `statistical_conventions.md` | Z1-Z3 criteria the three applications meet |
