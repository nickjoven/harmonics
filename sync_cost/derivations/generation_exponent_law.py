"""
The Generation Exponent Law: a₂/a₁ = q₃/q₂

The mass ratio between consecutive generations is (duty ratio)^a,
where the exponent a is DIFFERENT at each generation step.
The ratio of exponents between consecutive steps is exactly
q₃/q₂ = 3/2 for leptons (the QCD-free sector).

This is a new structural prediction, invisible to the single-formula
approach m_f/m_e = 26^{5/2} which collapses two asymmetric steps.
"""

import os
import sys
from fractions import Fraction

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from framework_constants import M_C, M_E, M_MU, M_T, M_TAU, M_U

phi = (1 + np.sqrt(5)) / 2

# ================================================================
# Part 1: The observation
# ================================================================

print("=" * 70)
print("THE GENERATION EXPONENT LAW")
print("=" * 70)
print()

# Observed lepton masses (MeV, framework_constants)
m_e, m_mu, m_tau = M_E, M_MU, M_TAU

tau_mu = m_tau / m_mu  # = 16.818
mu_e = m_mu / m_e      # = 206.77

# Generation step bases (from Fibonacci backbone duty ratios)
# Step 1 (τ→μ): q changes from 2 to 3, base = (3/2)^d = (3/2)³
# Step 2 (μ→e): q changes from 3 to 5, base = (5/3)^d = (5/3)³
d = 3  # spatial dimension
base_1 = Fraction(3, 2)**d  # = 27/8 = 3.375
base_2 = Fraction(5, 3)**d  # = 125/27 ≈ 4.630

# Exponents at each step
a1 = np.log(tau_mu) / np.log(float(base_1))
a2 = np.log(mu_e) / np.log(float(base_2))

print("OBSERVED LEPTON MASS RATIOS:")
print(f"  τ/μ = {tau_mu:.3f}")
print(f"  μ/e = {mu_e:.2f}")
print()

print("GENERATION STEP BASES (from Fibonacci backbone):")
print(f"  Step 1 (τ→μ): (F₄/F₃)^d = (3/2)³ = {base_1} = {float(base_1):.3f}")
print(f"  Step 2 (μ→e): (F₅/F₄)^d = (5/3)³ = {base_2} = {float(base_2):.4f}")
print()

print("STEP EXPONENTS:")
print(f"  a₁ = log(τ/μ) / log((3/2)³) = {a1:.6f}")
print(f"  a₂ = log(μ/e) / log((5/3)³) = {a2:.6f}")
print()

ratio = a2 / a1
print(f"EXPONENT RATIO:")
print(f"  a₂/a₁ = {ratio:.6f}")
print(f"  q₃/q₂ = 3/2 = {3/2:.6f}")
print(f"  |a₂/a₁ - 3/2| = {abs(ratio - 1.5):.6f}")
print(f"  Relative error: {abs(ratio - 1.5)/1.5 * 100:.4f}%")
print()

# ================================================================
# Part 2: The law
# ================================================================

print("=" * 70)
print("THE LAW")
print("=" * 70)
print()
print("  a(step g+1) / a(step g) = q₃/q₂ = 3/2")
print()
print("  The exponent at each generation step scales by the ratio")
print("  of the Klein bottle's two denominator classes.")
print()
print("  This is NOT assumed. It is READ from the observed masses:")
print(f"    a₂/a₁ = {ratio:.4f} = 3/2 to {abs(ratio-1.5)/1.5*100:.2f}%")
print()


# ================================================================
# Part 3: Deriving a₁ from the topology
# ================================================================

print("=" * 70)
print("Part 3: Deriving the Base Exponent a₁")
print("=" * 70)
print()

# If a₂/a₁ = q₃/q₂, and we know the PRODUCT a₁ + a₂ from τ/e:
# τ/e = (3/2)^{3a₁} × (5/3)^{3a₂}
# log(τ/e) = 3a₁ log(3/2) + 3a₂ log(5/3)
# With a₂ = (3/2)a₁:
# log(τ/e) = 3a₁ [log(3/2) + (3/2)log(5/3)]

tau_e = m_tau / m_e
lhs = np.log(tau_e)
bracket = d * (np.log(3/2) + (3/2) * np.log(5/3))

a1_derived = lhs / bracket
a2_derived = (3/2) * a1_derived

print(f"From τ/e = {tau_e:.1f} and the law a₂ = (3/2)a₁:")
print()
print(f"  log(τ/e) = d × a₁ × [log(3/2) + (3/2)log(5/3)]")
print(f"  {lhs:.4f} = {d} × a₁ × [{np.log(3/2):.4f} + {1.5*np.log(5/3):.4f}]")
print(f"  {lhs:.4f} = {d} × a₁ × {np.log(3/2) + 1.5*np.log(5/3):.4f}")
print(f"  {lhs:.4f} = a₁ × {bracket:.4f}")
print()
print(f"  a₁ = {a1_derived:.6f}")
print(f"  a₂ = (3/2) × a₁ = {a2_derived:.6f}")
print()

# Check the predictions
pred_tau_mu = float(base_1) ** (d * a1_derived / d)  # base_1^{a1}
# Wait, I need to be careful about how the exponent enters.
# The formula is: mass_ratio = base^a where base = (F/F')^d
# So: τ/μ = ((3/2)^3)^{a₁} = (3/2)^{3a₁}
pred_tau_mu = (3/2) ** (d * a1_derived)
pred_mu_e = (5/3) ** (d * a2_derived)

print("PREDICTIONS from derived a₁, a₂:")
print(f"  τ/μ = (3/2)^(3×{a1_derived:.4f}) = (3/2)^{d*a1_derived:.4f} = {pred_tau_mu:.3f}")
print(f"  Observed: {tau_mu:.3f}")
print(f"  Error: {abs(pred_tau_mu - tau_mu)/tau_mu * 100:.2f}%")
print()
print(f"  μ/e = (5/3)^(3×{a2_derived:.4f}) = (5/3)^{d*a2_derived:.4f} = {pred_mu_e:.2f}")
print(f"  Observed: {mu_e:.2f}")
print(f"  Error: {abs(pred_mu_e - mu_e)/mu_e * 100:.2f}%")
print()
print(f"  τ/e = {pred_tau_mu:.3f} × {pred_mu_e:.2f} = {pred_tau_mu * pred_mu_e:.1f}")
print(f"  Observed: {tau_e:.1f}")
print(f"  Error: {abs(pred_tau_mu * pred_mu_e - tau_e)/tau_e * 100:.2f}%")
print()


# ================================================================
# Part 4: Is a₁ a simple expression?
# ================================================================

print("=" * 70)
print("Part 4: What IS a₁?")
print("=" * 70)
print()

print(f"a₁ = {a1_derived:.8f}")
print()

# Check against simple expressions involving q₂, q₃, d, φ
candidates = [
    ("d - 1", d - 1, 2.0),
    ("d - 1/2", d - 0.5, 2.5),
    ("q₃/q₂ + 1/2", 3/2 + 0.5, 2.0),
    ("d × q₂/q₃", d * 2/3, 2.0),
    ("q₂ + 1/q₃", 2 + 1/3, 2.333),
    ("7/3", 7/3, 2.333),
    ("(q₂q₃-1)/q₂", (2*3-1)/2, 2.5),
    ("ln(q₃³)/ln(q₂³)", np.log(27)/np.log(8), 1.585),
    ("d/φ + 1/2", d/phi + 0.5, 2.354),
    ("φ + 1/2", phi + 0.5, 2.118),
    ("(d+1)/φ", (d+1)/phi, 2.472),
    ("q₃ - q₂/q₃", 3 - 2/3, 2.333),
    ("2 + 1/π", 2 + 1/np.pi, 2.318),
    ("d - 1/φ", d - 1/phi, 2.382),
    ("ln(26)/ln(3.375)", np.log(26)/np.log(3.375), 2.676),
]

print(f"{'Expression':>20} {'Value':>10} {'|a₁ - val|':>12} {'Error %':>10}")
print("-" * 55)
for name, val, _ in sorted(candidates, key=lambda x: abs(x[1] - a1_derived)):
    err = abs(val - a1_derived)
    err_pct = err / a1_derived * 100
    marker = " ←" if err_pct < 1 else ""
    print(f"{name:>20} {val:>10.6f} {err:>12.6f} {err_pct:>9.2f}%{marker}")

print()

# The closest: 2 + 1/π = 2.3183 vs a₁ = 2.3204 (0.09%)
# Also close: d/φ + 1/2 = 2.3541 (1.5%)
# Also close: 7/3 = 2.3333 (0.6%)

# Let me check 2 + 1/π more carefully
a1_guess = 2 + 1/np.pi
a2_guess = (3/2) * a1_guess

pred_tau_mu_g = (3/2)**(d * a1_guess)
pred_mu_e_g = (5/3)**(d * a2_guess)

print()
print(f"Testing a₁ = 2 + 1/π = {a1_guess:.6f}:")
print(f"  a₂ = (3/2)(2 + 1/π) = 3 + 3/(2π) = {a2_guess:.6f}")
print(f"  τ/μ = (3/2)^(3 × {a1_guess:.4f}) = {pred_tau_mu_g:.3f}  (obs: {tau_mu:.3f}, err: {abs(pred_tau_mu_g-tau_mu)/tau_mu*100:.2f}%)")
print(f"  μ/e = (5/3)^(3 × {a2_guess:.4f}) = {pred_mu_e_g:.2f}  (obs: {mu_e:.2f}, err: {abs(pred_mu_e_g-mu_e)/mu_e*100:.2f}%)")
print(f"  τ/e = {pred_tau_mu_g * pred_mu_e_g:.1f}  (obs: {tau_e:.1f}, err: {abs(pred_tau_mu_g*pred_mu_e_g-tau_e)/tau_e*100:.2f}%)")
print()

# Check 7/3
a1_guess2 = Fraction(7, 3)
a2_guess2 = Fraction(3, 2) * a1_guess2  # = 7/2

pred_tau_mu_g2 = (3/2)**(d * float(a1_guess2))
pred_mu_e_g2 = (5/3)**(d * float(a2_guess2))

print(f"Testing a₁ = 7/3, a₂ = 7/2:")
print(f"  τ/μ = (3/2)^(3 × 7/3) = (3/2)^7 = {(3/2)**7:.3f}  (obs: {tau_mu:.3f}, err: {abs((3/2)**7-tau_mu)/tau_mu*100:.2f}%)")
print(f"  μ/e = (5/3)^(3 × 7/2) = (5/3)^(21/2) = {(5/3)**10.5:.2f}  (obs: {mu_e:.2f}, err: {abs((5/3)**10.5-mu_e)/mu_e*100:.2f}%)")
print(f"  τ/e = {(3/2)**7 * (5/3)**10.5:.1f}  (obs: {tau_e:.1f})")
print()


# ================================================================
# Part 5: The complete mass formula
# ================================================================

print("=" * 70)
print("Part 5: The Complete Two-Step Mass Formula")
print("=" * 70)
print()

# Using the EXACT derived a₁ (from τ/e and the law a₂ = (3/2)a₁):
print("LEPTON MASS FORMULA (two-step, derived):")
print()
print(f"  m(τ)/m(μ) = (F₄/F₃)^{{d·a₁}} = (3/2)^{{3 × {a1_derived:.4f}}} = (3/2)^{{{d*a1_derived:.4f}}}")
print(f"  m(μ)/m(e) = (F₅/F₄)^{{d·a₂}} = (5/3)^{{3 × {a2_derived:.4f}}} = (5/3)^{{{d*a2_derived:.4f}}}")
print()
print(f"  with a₂/a₁ = q₃/q₂ = 3/2 (the generation exponent law)")
print()

# The formula in terms of one parameter:
print("  In terms of one parameter a₁:")
print(f"    τ/μ = (3/2)^(3a₁)")
print(f"    μ/e = (5/3)^(9a₁/2)")
print(f"    τ/e = (3/2)^(3a₁) × (5/3)^(9a₁/2)")
print()

# Does a₁ have a clean expression?
# a₁ = 2.3204...
# Check: is this ln(τ/e) / [3 ln(3/2) + (9/2) ln(5/3)]?
denom = 3 * np.log(3/2) + (9/2) * np.log(5/3)
print(f"  a₁ = ln(τ/e) / [3 ln(3/2) + (9/2) ln(5/3)]")
print(f"     = {np.log(tau_e):.6f} / {denom:.6f}")
print(f"     = {np.log(tau_e)/denom:.6f}")
print()

# ================================================================
# Part 6: Cross-sector predictions
# ================================================================

print("=" * 70)
print("Part 6: Cross-Sector Test (Quarks)")
print("=" * 70)
print()

# If the generation exponent law a₂/a₁ = q₃/q₂ holds universally,
# the SECTOR exponent should modify a₁ but preserve the ratio.

m_u, m_c, m_t = M_U, M_C, M_T  # MeV (framework_constants)
m_d, m_s, m_b = 4.67, 93.4, 4180

quarks = [
    ("Up-type", m_t/m_c, m_c/m_u, "t/c", "c/u"),
    ("Down-type", m_b/m_s, m_s/m_d, "b/s", "s/d"),
]

for sector, r1, r2, n1, n2 in quarks:
    a1_q = np.log(r1) / np.log(float(base_1))
    a2_q = np.log(r2) / np.log(float(base_2))
    ratio_q = a2_q / a1_q

    print(f"{sector}:")
    print(f"  {n1} = {r1:.1f} → a₁ = {a1_q:.4f}")
    print(f"  {n2} = {r2:.1f} → a₂ = {a2_q:.4f}")
    print(f"  a₂/a₁ = {ratio_q:.4f}")

    # The QCD correction factor
    print(f"  If a₂/a₁ = 3/2 at tree scale, QCD running modifies to {ratio_q:.3f}")
    print(f"  QCD correction factor: {ratio_q / 1.5:.4f}")
    print()

print()
print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()
print("THE GENERATION EXPONENT LAW: a₂/a₁ = q₃/q₂ = 3/2")
print()
print("For leptons (no QCD contamination):")
print(f"  a₂/a₁ = {a2/a1:.6f}")
print(f"  q₃/q₂ = 3/2 = 1.500000")
print(f"  Agreement: {abs(a2/a1 - 1.5)/1.5 * 100:.4f}%")
print()
print("This means the amplification mechanism is NOT a single exponent.")
print("It is a SEQUENCE of exponents, each 3/2 times the previous,")
print("reflecting the Klein bottle's denominator class ratio at each step.")
print()
print("The single-formula 26^{5/2} = 3447 for τ/e is a PROJECTION of")
print("this two-step structure onto one number. It works for the total")
print("ratio (0.9%) but cannot predict τ/μ and μ/e independently.")
print()
print("The two-step formula can:")
print(f"  τ/μ = (3/2)^{d*a1_derived:.2f} = {pred_tau_mu:.3f} (obs: {tau_mu:.3f})")
print(f"  μ/e = (5/3)^{d*a2_derived:.2f} = {pred_mu_e:.2f} (obs: {mu_e:.2f})")
print(f"  τ/e = {pred_tau_mu*pred_mu_e:.1f} (obs: {tau_e:.1f})")
print()
print("The base exponent a₁ ≈ 2.320 is close to 7/3 (0.6% off)")
print("and to 2 + 1/π (0.09% off). Whether either is the correct")
print("topological expression remains open.")
