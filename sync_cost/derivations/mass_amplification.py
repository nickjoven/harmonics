"""
Mass amplification from self-consistency loop iteration.

Key insight: the 4 XOR-surviving modes cancel with equal weights.
The physical order parameter r* comes from the FULL F₆ mode set.
The mass hierarchy operates as a PERTURBATION within the non-zero
background r*.

The amplification mechanism: the coupling between a fermion and
the Higgs condensate (= the mean field r*) involves traversing
the Stern-Brocot tree from the fermion's mode to the root.
Each link in the chain multiplies the coupling by the duty cycle
at that depth. The chain length IS the generation number.
The chain product IS the Yukawa coupling.
"""

import numpy as np
from fractions import Fraction
from math import gcd

phi = (1 + np.sqrt(5)) / 2


# ================================================================
# Part 1: Chain product as Yukawa coupling
# ================================================================

print("=" * 70)
print("Part 1: Yukawa Coupling = Chain Product through the Tree")
print("=" * 70)
print()

# A fermion at generation g has a chain of g links to the root.
# Each link has a duty cycle that depends on the depth.
# The Yukawa coupling = product of duty cycles along the chain.

# At the Fibonacci backbone, the denominator at depth d is q(d) ~ φ^d.
# The tongue width at depth d is w(d) ~ 1/φ^{2d}.
# The duty cycle at depth d is w(d)/q(d) = 1/φ^{3d}.

# Chain product for generation g (chain length g):
# y(g) = Π_{d=1}^{g} duty(d) = Π_{d=1}^{g} 1/φ^{3d}
#       = 1/φ^{3(1+2+...+g)} = 1/φ^{3g(g+1)/2}

print("Fibonacci backbone model:")
print("  Denominator at depth d: q(d) ~ φ^d")
print("  Tongue width at depth d: w(d) ~ 1/φ^{2d}")
print("  Duty cycle at depth d: duty(d) = w(d)/q(d) ~ 1/φ^{3d}")
print()
print("Chain product (Yukawa coupling) for generation g:")
print("  y(g) = Π_{d=1}^{g} 1/φ^{3d} = 1/φ^{3g(g+1)/2}")
print()

for g in range(1, 5):
    exponent = 3 * g * (g + 1) / 2
    y = 1 / phi**exponent
    print(f"  g={g}: exponent = 3×{g}×{g+1}/2 = {exponent:.0f}, "
          f"y = 1/φ^{exponent:.0f} = {y:.4e}")

print()

# Mass ratios: m(g)/m(g') = y(g)/y(g')
print("Mass ratios from chain products:")
print()

y = {}
for g in range(1, 5):
    exp_g = 3 * g * (g + 1) / 2
    y[g] = 1 / phi**exp_g

# Convention: gen 1 = heaviest (shortest chain), gen 3 = lightest (longest)
# Wait — in the SM, gen 3 is HEAVIEST (t, b, τ).
# In the tree, shorter chain = closer to root = STRONGER coupling = HEAVIER.
# So gen 1 in the tree (path length 1) = gen 3 in the SM (heaviest).

print("  Chain convention: shorter chain = stronger coupling = heavier")
print()
print(f"  y(1)/y(3) = φ^{{3×3×4/2 - 3×1×2/2}} = φ^{{18-3}} = φ^15")
print(f"            = {phi**15:.1f}")
print()
print(f"  y(1)/y(2) = φ^{{3×2×3/2 - 3×1×2/2}} = φ^{{9-3}} = φ^6")
print(f"            = {phi**6:.2f}")
print()

# Compare to observations
tau_e = 3477
mu_e = 207
print(f"  Observed τ/e = {tau_e}")
print(f"  φ^15 = {phi**15:.1f}")
print(f"  Ratio: {phi**15 / tau_e:.3f}")
print()
print(f"  Observed μ/e = {mu_e}")
print(f"  φ^6 = {phi**6:.2f}")
print(f"  Ratio: {phi**6 / mu_e:.3f}")
print()

# φ^15 ≈ 1597. Not 3477. Off by factor ~2.2.
# But φ^15 = F_15 (Fibonacci number) ≈ 610. No, φ^15/√5 ≈ F_15.
# φ^15 = 1596.7. m_τ/m_e = 3477. Ratio = 2.18.

# What if the chain product involves d-dimensional volume?
# Instead of 1/φ^{3d} per link, use 1/φ^{2d} (tongue width only)?
print("Alternative: tongue width only (no period factor):")
for g in range(1, 5):
    exp_g = 2 * g * (g + 1) / 2  # = g(g+1)
    y_alt = 1 / phi**exp_g
    print(f"  g={g}: y_alt = 1/φ^{g*(g+1)} = {y_alt:.4e}")

print()
print(f"  y(1)/y(3) with tongue widths = φ^{{3×4-1×2}} = φ^10 = {phi**10:.1f}")
print(f"  Observed τ/e = {tau_e}")
print(f"  φ^10 = {phi**10:.1f}")
print()


# ================================================================
# Part 2: What exponent matches observations?
# ================================================================

print("=" * 70)
print("Part 2: What Fibonacci Power Matches Each Observed Ratio?")
print("=" * 70)
print()

# Since the Stern-Brocot tree's self-similar structure is governed
# by φ, the mass ratios should be powers of φ.
# What powers?

ratios = {
    "τ/e": 3477,
    "μ/e": 207,
    "t/u": 80000,
    "c/u": 588,
    "b/d": 895,
    "s/d": 20.0,
    "t/c": 136,
    "b/s": 44.8,
    "τ/μ": 16.8,
}

print(f"{'Ratio':>8} {'Value':>10} {'log_φ':>10} {'Nearest n':>10} "
      f"{'φ^n':>10} {'Error':>8}")
print("-" * 62)

for name, val in ratios.items():
    log_phi = np.log(val) / np.log(phi)
    n_nearest = round(log_phi)
    phi_n = phi**n_nearest
    err = abs(phi_n - val) / val * 100
    print(f"{name:>8} {val:>10.1f} {log_phi:>10.2f} {n_nearest:>10d} "
          f"{phi_n:>10.1f} {err:>7.1f}%")

print()
print("Key observations:")
print("  τ/e ≈ φ^{17} = 1597 (54% off) or φ^{16.9} exactly")
print("  μ/e ≈ φ^{11} = 89 (57% off) or φ^{11.1} exactly")
print("  t/u ≈ φ^{23.5}")
print("  b/d ≈ φ^{14.1}")
print()


# ================================================================
# Part 3: Generation structure in φ-powers
# ================================================================

print("=" * 70)
print("Part 3: Generation Spacing in φ-Powers")
print("=" * 70)
print()

# If mass ratios are φ^n, what are the SPACINGS between generations?

print("Within each sector (heaviest/middle, middle/lightest):")
print()

sectors = {
    "Leptons": [("τ/μ", 16.8), ("μ/e", 207)],
    "Up-type": [("t/c", 136), ("c/u", 588)],
    "Down-type": [("b/s", 44.8), ("s/d", 20.0)],
}

for sector, pairs in sectors.items():
    spacings = []
    for name, val in pairs:
        n = np.log(val) / np.log(phi)
        spacings.append((name, n))

    print(f"  {sector}:")
    for name, n in spacings:
        print(f"    {name}: log_φ = {n:.2f}")

    if len(spacings) == 2:
        ratio = spacings[0][1] / spacings[1][1]
        print(f"    Spacing ratio: {spacings[0][1]:.2f} / {spacings[1][1]:.2f} = {ratio:.3f}")
    print()


# ================================================================
# Part 4: The self-referential structure
# ================================================================

print("=" * 70)
print("Part 4: What the Tree Structure Actually Gives")
print("=" * 70)
print()

# The Stern-Brocot tree at the Fibonacci backbone has:
# - F_n denominators at depth n (Fibonacci numbers)
# - Tongue widths scaling as 1/F_n² ≈ 1/φ^{2n}
# - Duty cycles scaling as 1/F_n³ ≈ 1/φ^{3n}

# The chain product for path length g involves specific depths,
# not consecutive depths. The physical generations connect at
# depths determined by q₂ = 2 and q₃ = 3:

# q = 2 appears at Fibonacci depth 1 (since F_1 = 1, F_2 = 1, F_3 = 2)
# q = 3 appears at Fibonacci depth 4 (F_4 = 3)

# Gen 1 (heaviest, path length 1):
#   Chain: root → q=2 mode. One A-link.
#   Coupling: duty(q=2) = 1/q₂³ = 1/8

# Gen 2 (middle, path length 2):
#   Chain: root → q=2 → q=5 (mediant of q=2 and q=3).
#   Coupling: duty(q=2) × duty(q=5) = (1/8)(1/125) = 1/1000

# Gen 3 (lightest, path length 3):
#   Chain: root → q=2 → q=5 → deeper mode.
#   Coupling: duty(q=2) × duty(q=5) × duty(q_deeper)

print("Physical chain products using actual denominators:")
print()

# Actual Farey fractions at each depth in the (2,3) region:
# Depth 1: 1/2 (q=2)
# Depth 2: 1/3, 2/3 (q=3) — but in the OTHER XOR sector
# Depth 3: 2/5, 3/5 (q=5) — mediants of 1/2 with 1/3, 2/3

# The generation chain goes through DIFFERENT denominators at each step.
# Using the actual tree structure near the {2,3} modes:

print("Path through the Stern-Brocot tree near q₂=2, q₃=3:")
print()

# The relevant fractions and their denominators:
fractions = [
    (Fraction(1,1), 1, "root"),
    (Fraction(1,2), 2, "gen 3 (heaviest)"),
    (Fraction(1,3), 3, "gen 2 (middle)"),
    (Fraction(2,5), 5, "gen 1 (lightest)"),
    (Fraction(1,4), 4, "4th gen (would be)"),
]

for f, q, label in fractions:
    duty = 1/q**3
    print(f"  {str(f):>5}  q={q}  duty=1/{q}³={duty:.6f}  [{label}]")

print()

# Mass ratios from duty cycle products:
# Gen 3 (τ): duty(2) = 1/8
# Gen 2 (μ): duty(3) = 1/27
# Gen 1 (e): duty(5) = 1/125

# Mass = Higgs VEV × Yukawa coupling
# Yukawa ~ duty^a where a is the sector exponent
# Ratio: m(gen3)/m(gen1) = (duty(2)/duty(5))^a = (125/8)^a

print("Duty cycle ratios (= Yukawa ratios at tree scale):")
d2 = 1/8
d3 = 1/27
d5 = 1/125

print(f"  duty(q=2)/duty(q=5) = {d2/d5:.2f}  (gen3/gen1)")
print(f"  duty(q=3)/duty(q=5) = {d3/d5:.2f}  (gen2/gen1)")
print(f"  duty(q=2)/duty(q=3) = {d2/d3:.2f}  (gen3/gen2)")
print()

# These raw duty ratios are 15.6, 4.6, 3.4 — still O(1-10), not O(1000).
# The exponent a amplifies: (15.6)^a = 3477 → a = log(3477)/log(15.6) = 2.96

a_from_tau = np.log(3477) / np.log(d2/d5)
a_from_mu = np.log(207) / np.log(d3/d5)
print(f"Required exponent a:")
print(f"  From τ/e: a = log(3477)/log({d2/d5:.1f}) = {a_from_tau:.3f}")
print(f"  From μ/e: a = log(207)/log({d3/d5:.2f}) = {a_from_mu:.3f}")
print()

# Check: is 15.625 = (5/2)^3 = q₅³/q₂³?
# 15.625 = 125/8 = 5³/2³ = (q₃+q₂)³/q₂³
print(f"  125/8 = 5³/2³ = (q₂+q₃)³/q₂³")
print(f"  27/125 = 3³/5³ = q₃³/(q₂+q₃)³")
print()

# With a = 3 (= d): (125/8)^3 = 15.625^3 = 3815
# Close to 3477! Only 10% off
print(f"  (125/8)^3 = {(125/8)**3:.1f}  (10% from τ/e = 3477)")
print(f"  (27/125)^3 = {(27/125)**3:.6f} × 3815 = {(27/125)**3 * 3815:.1f}")
print()

# With a = 5/2: (125/8)^{5/2} = 15.625^{2.5} = 964
print(f"  (125/8)^(5/2) = {(125/8)**2.5:.1f}")
print(f"  (27/125)^(5/2) = {(27/125)**2.5:.6f}")
print()

# The exponent a ≈ 3 works for the DUTY RATIO model
# (using duty(q=2)/duty(q=5) as the base instead of 26)
print("=" * 70)
print("RESULT: Duty ratio model with a=d=3")
print("=" * 70)
print()
print(f"  m(τ)/m(e) = (q₅/q₂)^(3d) = (5/2)^9 = {(5/2)**9:.1f}")
print(f"  Observed: 3477")
print(f"  Error: {abs((5/2)**9 - 3477)/3477*100:.1f}%")
print()
print(f"  m(μ)/m(e) = (q₅/q₃)^(3d) = (5/3)^9 = {(5/3)**9:.1f}")
print(f"  Observed: 207")
print(f"  Error: {abs((5/3)**9 - 207)/207*100:.1f}%")
print()

# Also try a = d = 3 with the simple duty ratio
print(f"  Alternative: duty^d")
print(f"  (duty₂/duty₅)^d = (125/8)^3 = {(125/8)**3:.1f}  (τ/e, 10% off)")
print(f"  (duty₃/duty₅)^d = (125/27)^3 = {(125/27)**3:.1f}  (μ/e, ???)")
print(f"  Observed μ/e = 207")
print(f"  Error: {abs((125/27)**3 - 207)/207*100:.1f}%")
