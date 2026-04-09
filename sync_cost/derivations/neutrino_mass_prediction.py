"""
Neutrino mass from tree depth (q₂q₃)² = 36.

The neutrino integer conservation law breaks trivially because |Q|=0.
But neutrinos DO have a depth — set by the weak-only coupling structure.

Framework prediction:
  m_ν ~ v × (K*/2)^{(q₂q₃)²} = 246 GeV × (0.431)^36 ≈ 17 meV

Three neutrinos at three adjacent depths around (q₂q₃)² = 36:
  ν₃ at depth 35: ~40 meV (near atmospheric 50 meV)
  ν₂ at depth 36: ~17 meV (intermediate)
  ν₁ at depth 37: ~7  meV (near solar 9 meV)

The m₃/m₁ ratio predicted is (K*/2)^(-2) ≈ 5.4, within 10% of
the observed atmospheric/solar ratio 5.77.

Structural interpretation:
  depth = (q₂q₃)² = q₂²q₃² = 4 × 9 = k_lepton × q₂²
  = lepton sector constant × squared weak denominator

  The neutrino traverses the full lepton walk (9 steps) and then
  cycles back through 4 weak interactions, since it can't anchor
  on electric charge.

Depth 36 = 4 × (2q₂q₃) = 4 antiperiodic traversals. After four
traversals, (-1)^4 = +1 — the mode self-identifies. This predicts
neutrinos are MAJORANA.
"""

import numpy as np

K_star = 0.862
v_ew = 246  # GeV in natural units
v_ev = v_ew * 1e9  # eV

q2, q3 = 2, 3
d_center = (q2 * q3)**2  # = 36

# ================================================================
# The prediction
# ================================================================

print("=" * 70)
print("NEUTRINO MASS PREDICTION: m_ν at depth (q₂q₃)² = 36")
print("=" * 70)
print()

# The mass at depth d is approximately v × (K*/2)^d
# (single-mode tongue width estimate)

m_at_36 = v_ev * (K_star/2)**36  # in eV
m_at_35 = v_ev * (K_star/2)**35
m_at_37 = v_ev * (K_star/2)**37

print(f"K* = {K_star}")
print(f"v = {v_ew} GeV")
print(f"(q₂q₃)² = {d_center}")
print()

print("Three neutrinos at depths 35, 36, 37:")
print(f"{'Depth':>8} {'Mass (meV)':>15}")
print("-" * 25)
print(f"{35:>8} {m_at_35*1000:>15.2f}")
print(f"{36:>8} {m_at_36*1000:>15.2f}")
print(f"{37:>8} {m_at_37*1000:>15.2f}")
print()

# Observed scales
atm_scale = np.sqrt(2.5e-3)  # eV, atmospheric
sol_scale = np.sqrt(7.5e-5)  # eV, solar

print("Observed neutrino mass scales:")
print(f"  Atmospheric: √(Δm²_atm) = {atm_scale*1000:.1f} meV")
print(f"  Solar:       √(Δm²_sol) = {sol_scale*1000:.1f} meV")
print()

print("Comparison:")
print(f"  Predicted ν₃ at depth 35: {m_at_35*1000:.1f} meV")
print(f"  Observed (atmospheric):    {atm_scale*1000:.1f} meV")
print(f"  Ratio: {m_at_35/atm_scale:.3f}")
print()
print(f"  Predicted ν₁ at depth 37: {m_at_37*1000:.1f} meV")
print(f"  Observed (solar):          {sol_scale*1000:.1f} meV")
print(f"  Ratio: {m_at_37/sol_scale:.3f}")
print()

# The critical test: m₃/m₁ ratio
pred_ratio = (K_star/2)**(-2)
obs_ratio = atm_scale / sol_scale

print(f"m₃/m₁ predicted: (K*/2)^(-2) = {pred_ratio:.3f}")
print(f"m₃/m₁ observed:  {obs_ratio:.3f}")
print(f"Agreement: {abs(pred_ratio - obs_ratio)/obs_ratio * 100:.1f}% error")
print()

# Sum bound
total_nu = m_at_35 + m_at_36 + m_at_37
print(f"Σ m_ν prediction: {total_nu*1000:.1f} meV")
print(f"Planck bound:     Σ m_ν < 120 meV")
if total_nu * 1000 < 120:
    print(f"  ✓ CONSISTENT")
else:
    print(f"  ✗ VIOLATES BOUND")
print()


# ================================================================
# Structural interpretation
# ================================================================

print("=" * 70)
print("WHY DEPTH = (q₂q₃)²?")
print("=" * 70)
print()

k_lepton = q3**2  # = 9
k_quark = q2**3   # = 8

print(f"Charged lepton walk budget (integer conservation law):")
print(f"  k_lepton = q₃² = (dim adj SU(2))² = {k_lepton}")
print()
print(f"Neutrino walk depth:")
print(f"  depth_ν = (q₂q₃)² = q₂²q₃² = {q2**2 * q3**2}")
print(f"          = 4 × 9")
print(f"          = q₂² × k_lepton")
print()
print("Reading: the neutrino walks the full lepton budget (9 steps)")
print("BUT must also cycle back through q₂² = 4 weak interactions")
print("because it has no electric charge to anchor on.")
print()
print("This is consistent with chirality asymmetry:")
print("  Charged lepton has L ≠ R under SU(2), needs (adj SU(2))² = 9")
print("  Neutrino has no EM anchor, needs q₂² × (adj SU(2))² = 4 × 9 = 36")
print()

# Note: 36 is also (q₂q₃)² = interaction scale squared
print(f"Equivalent interpretations:")
print(f"  36 = (q₂q₃)² = (interaction scale)²")
print(f"  36 = q₂² × q₃² = weak² × strong²")
print(f"  36 = 4 × k_lepton = q₂² × (k_lepton)")
print(f"  36 = 4 × 9 = (adj SU(2))² × q₂²")
print()


# ================================================================
# Majorana prediction
# ================================================================

print("=" * 70)
print("MAJORANA PREDICTION")
print("=" * 70)
print()

print(f"Depth 36 = 4 × (2q₂q₃) = 4 × 6 = 4 × (double interaction)")
print()
print("Each antiperiodic traversal of the Klein bottle gives a (-1)")
print("phase factor. Four traversals: (-1)⁴ = +1.")
print()
print("This means after 4 antiperiodic cycles, the neutrino mode")
print("returns to itself — it is its own conjugate.")
print()
print("PREDICTION: NEUTRINOS ARE MAJORANA.")
print()
print("This is testable by neutrinoless double beta decay experiments")
print("(KamLAND-Zen, LEGEND, CUPID). The rate is proportional to the")
print("'effective Majorana mass' m_ββ, which mixes the three ν masses")
print("through the PMNS matrix.")
print()
print("Framework estimate for m_ββ:")
print("  m_ββ ~ average of the three depths ~ 20 meV")
print("  Current bound: m_ββ < 60-165 meV (KamLAND-Zen 2024)")
print("  Future sensitivity: LEGEND-1000, nEXO will reach 10-20 meV")
print()


# ================================================================
# Summary
# ================================================================

print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()
print("Framework predictions for neutrinos:")
print()
print("  1. m_ν at depth (q₂q₃)² = 36, giving mass scale ~17 meV")
print("  2. Three neutrinos at depths 35, 36, 37 give observed")
print("     mass splittings within ~20% (structural)")
print("  3. m₃/m₁ = (K*/2)^(-2) ≈ 5.4 (observed 5.77, 7% error)")
print("  4. Σ m_ν ~ 64 meV (observed bound < 120 meV) ✓")
print("  5. NEUTRINOS ARE MAJORANA (from 4-traversal self-identification)")
print()
print("All predictions from two inputs:")
print("  - The fixed point K* = 0.862 (already derived from Ω_Λ)")
print("  - The electroweak scale v = 246 GeV (single dimensionful input)")
print()
print("The depth (q₂q₃)² = 36 is structural: the square of the")
print("Klein bottle's interaction scale, equal to q₂² × k_lepton.")
print()
print("This extends the integer conservation law to the neutrino sector")
print("through a MODIFIED rule: for Q=0 fermions, the walk budget is")
print("k_lepton multiplied by q²_weak-anchor = 4, giving depth 36.")
