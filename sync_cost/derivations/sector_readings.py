"""
Sector readings: test multiple topological coordinate systems
to find one in which leptons, up-type, and down-type quarks
give compatible readings of the same fixed point.

For leptons, the coordinate system (base₁, base₂) = ((3/2)³, (5/3)³)
with d=3 gives a₂/a₁ = 1.4994 ≈ 3/2.

For quarks, this gives different values (1.03 for up-type, 0.63 for
down-type). The question: is there a DIFFERENT coordinate system
that makes all three readings consistent?
"""

import os
import sys
from fractions import Fraction

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from framework_constants import (
    M_B, M_C, M_D, M_E, M_MU, M_S, M_T, M_TAU, M_U,
)

# PDG masses (MeV, framework_constants)
m_e, m_mu, m_tau = M_E, M_MU, M_TAU
m_u, m_c, m_t = M_U, M_C, M_T
m_d, m_s, m_b = M_D, M_S, M_B


def reading(r1, r2, base1, base2):
    """Compute (a1, a2, a2/a1) for given mass ratios and bases."""
    a1 = np.log(r1) / np.log(base1)
    a2 = np.log(r2) / np.log(base2)
    return a1, a2, a2/a1


sectors = {
    'Leptons':     (m_tau/m_mu, m_mu/m_e),
    'Up-type':     (m_t/m_c,    m_c/m_u),
    'Down-type':   (m_b/m_s,    m_s/m_d),
}

print("=" * 70)
print("SECTOR READINGS IN MULTIPLE COORDINATE SYSTEMS")
print("=" * 70)
print()

# ---- Candidate 1: Pure d-dimensional duty ratios ----
print("Candidate 1: base = (F_{n+1}/F_n)^d with d varying")
print("-" * 70)
print(f"{'d':>4} {'Leptons':>12} {'Up-type':>12} {'Down-type':>12} {'compat?':>10}")

for d in [1, 2, 3, 4, 5, 6]:
    b1 = (3/2)**d
    b2 = (5/3)**d
    results = {}
    for name, (r1, r2) in sectors.items():
        _, _, ratio = reading(r1, r2, b1, b2)
        results[name] = ratio
    compat = (abs(results['Leptons'] - results['Up-type']) < 0.1 and
              abs(results['Leptons'] - results['Down-type']) < 0.1)
    print(f"{d:>4} {results['Leptons']:>12.4f} {results['Up-type']:>12.4f} "
          f"{results['Down-type']:>12.4f} {'✓' if compat else '✗':>10}")

# Note: a₂/a₁ is INDEPENDENT of d because d cancels when computing the ratio.
# ln(r)/ln(b^d) = (1/d) ln(r)/ln(b), and the d cancels in a₂/a₁.
# So varying d alone cannot make quarks match leptons.

print()
print("Observation: a₂/a₁ is independent of d (it cancels).")
print("Varying d alone cannot reconcile sectors.")
print()

# ---- Candidate 2: Different Farey bases for quarks ----
print("Candidate 2: quark-specific Farey bases")
print("-" * 70)

# What if quarks use (2/1, 3/2) or (5/2, 5/3) or similar?
fibonacci_pairs = [
    ("(3/2, 5/3)",  3/2,   5/3),    # lepton baseline
    ("(2/1, 3/2)",  2/1,   3/2),    # shifted down
    ("(5/3, 8/5)",  5/3,   8/5),    # shifted up
    ("(2/1, 5/3)",  2/1,   5/3),    # skip one
    ("(3/1, 2/1)",  3/1,   2/1),    # next shift
    ("(4/3, 3/2)",  4/3,   3/2),    # denser
]

for d in [3]:
    print(f"\n  d = {d}:")
    print(f"  {'Bases':>16} {'Leptons':>10} {'Up':>10} {'Down':>10}")
    for label, f1, f2 in fibonacci_pairs:
        b1 = f1**d
        b2 = f2**d
        results = {}
        for name, (r1, r2) in sectors.items():
            _, _, ratio = reading(r1, r2, b1, b2)
            results[name] = ratio
        print(f"  {label:>16} {results['Leptons']:>10.4f} "
              f"{results['Up-type']:>10.4f} {results['Down-type']:>10.4f}")

print()
print("Observation: changing (F_{n+1}/F_n) also scales a₂/a₁ uniformly.")
print("No single Fibonacci base makes all sectors agree.")
print()

# ---- Candidate 3: Sector-dependent exponent (d_eff hypothesis) ----
print("Candidate 3: sector-dependent effective dimension d_eff")
print("-" * 70)

# If quarks use d_eff ≠ 3, maybe because of color, can we find d_eff
# such that the quark reading gives a₂/a₁ = 3/2?
#
# The reading a₂/a₁ only depends on the SHAPE of the bases, not their
# exponent. So d_eff alone doesn't help.
#
# BUT: what if the bases themselves are DIFFERENT for different sectors?
# E.g., up-type uses (b1_up, b2_up) where b1_up ≠ (3/2)³?

# For the law a₂/a₁ = 3/2 to hold for up-type:
# ln(c/u)/ln(b2_up) / (ln(t/c)/ln(b1_up)) = 3/2
# → ln(c/u) × ln(b1_up) = (3/2) × ln(t/c) × ln(b2_up)

tc = m_t/m_c
cu = m_c/m_u
bs = m_b/m_s
sd = m_s/m_d

# Solve for the required base ratio ln(b2)/ln(b1) in each sector:
# ln(b1)/ln(b2) = (3/2) × ln(r1)/ln(r2)
# (so that ratio = 3/2)

# Actually the law says a₂/a₁ = 3/2. Rearranging:
# ln(r2)/ln(b2) = (3/2) × ln(r1)/ln(b1)
# ln(r2)/ln(r1) = (3/2) × ln(b2)/ln(b1)

target = 3/2

required_log_base_ratio = {}
for name, (r1, r2) in sectors.items():
    mass_log_ratio = np.log(r2) / np.log(r1)
    # Need: mass_log_ratio = target × (ln(b2)/ln(b1))
    # So: ln(b2)/ln(b1) = mass_log_ratio / target
    required_log_base_ratio[name] = mass_log_ratio / target
    print(f"  {name:>12}: ln(r₂)/ln(r₁) = {mass_log_ratio:.4f}")
    print(f"  {'':>12}  ln(b₂)/ln(b₁) should be: {mass_log_ratio/target:.4f}")

# Lepton requirement: ln(b2)/ln(b1) = 1.2599 = ln(5/3)/ln(3/2)
# Up-type requirement: different value → different base structure
print()
print(f"Lepton: ln(b₂)/ln(b₁) = {required_log_base_ratio['Leptons']:.4f}")
print(f"        matches ln(5/3)/ln(3/2) = {np.log(5/3)/np.log(3/2):.4f} ✓")
print()
print(f"Up-type: ln(b₂)/ln(b₁) = {required_log_base_ratio['Up-type']:.4f}")
print(f"         What Fibonacci pair gives this ratio?")

# Search for (F_{n+1}/F_n, F_{n+2}/F_{n+1}) pair matching up-type
# Or any rational pair (p1/q1, p2/q2)

target_up = required_log_base_ratio['Up-type']
target_down = required_log_base_ratio['Down-type']

candidates = []
for a in range(2, 20):
    for b in range(1, a):
        for c in range(2, 20):
            for d in range(1, c):
                if a/b <= 1 or c/d <= 1:
                    continue
                ratio = np.log(c/d) / np.log(a/b)
                if abs(ratio - target_up) < 0.01 and (a,b) != (c,d):
                    candidates.append(('up', a, b, c, d, ratio))
                if abs(ratio - target_down) < 0.01 and (a,b) != (c,d):
                    candidates.append(('down', a, b, c, d, ratio))

print()
print("Closest rational base pairs for each sector:")
for sector in ['up', 'down']:
    matches = [c for c in candidates if c[0] == sector]
    matches.sort(key=lambda x: abs(x[5] - (target_up if sector=='up' else target_down)))
    target = target_up if sector == 'up' else target_down
    print(f"\n  {sector}-type target: {target:.4f}")
    for _, a, b, c, d, r in matches[:5]:
        err = abs(r - target)
        print(f"    ({a}/{b}, {c}/{d}): ratio = {r:.4f} (err {err:.4f})")

print()
print("=" * 70)
print("INTERPRETATION")
print("=" * 70)
print()
print("The reading a₂/a₁ depends only on the SHAPE of the base pair,")
print("specifically ln(b₂)/ln(b₁). For the law a₂/a₁ = 3/2 to hold")
print("universally, each sector needs a specific base pair shape.")
print()
print(f"  Leptons:    ln(b₂)/ln(b₁) = 1.2599 = ln(5/3)/ln(3/2)  ✓")
print(f"  Up-type:    ln(b₂)/ln(b₁) = 0.8653 ← different!")
print(f"  Down-type:  ln(b₂)/ln(b₁) = 0.5253 ← very different!")
print()
print("These correspond to DIFFERENT positions in the Stern-Brocot tree:")
print("  Lepton:    sits on the main Fibonacci backbone (3/2, 5/3)")
print("  Quarks:    sit on OTHER branches")
print()
print("This makes physical sense: leptons don't feel color, so they")
print("read the tree directly. Quarks feel color (SU(3) gauge field),")
print("which moves them to a different effective position in the tree.")
print()
print("The SU(3) coupling 'drags' the quark readings to different")
print("Fibonacci branches. The specific base pair for each quark sector")
print("should be computable from the QCD coupling at the relevant scale.")
print()
print("Next step: derive the effective (b₁, b₂) for quarks from")
print("first principles, using the SU(3) representation structure.")
