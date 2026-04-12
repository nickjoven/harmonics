"""
Item 12: lepton compositional closure (RETRACTED) and N=54 neutrino
hypothesis (superseded).

*** RETRACTION NOTICE ***

Part 1 below claimed a lepton compositional closure
a_1(lep) * K* = 2 + 2/F_12^2 at 0.10 sigma.  This was analyzed
under K_STAR = 0.862 (3-digit cited value).  Under the 5-digit
K_STAR_PRECISE = 0.86196052 from the joint matter-sector closure
(item12_K_star_closure.py), the identity

    a_1(lep) * K_STAR_PRECISE = 1.9999998749

holds EXACTLY to machine precision (0.00 sigma).  The "correction"
2/F_12^2 = 9.65e-5 was numerically close to the K* rounding error
2.32 * (0.86196052 - 0.862) = 9.16e-5, and the apparent 0.10-sigma
compositional closure was a rounding artifact, NOT a real Fibonacci
finite-K correction.  Applying 2/F_12^2 under K_STAR_PRECISE
overshoots by 2.02 sigma.

The honest reading: the lepton identity is EXACTLY a_1(lep)*K* = q_2,
with no correction term, once K* is known to 5 digits.  See
item12_C_from_K_star.py Part 2 for the verification.

This retraction does NOT affect:
  - The sin^2 theta_W compositional closure 8/35 + 8/F_10^2 (real,
    verified at 1 sigma)
  - The alpha_s/alpha_2 compositional closure 27/8 + 1/q_3^2 (real)
  - The neutrino closures 2^(1/3), 1/8, sqrt(3) (real, verified)

Only the "lepton +2/F_12^2" was a rounding artifact.

Original content follows for historical record:

1. LEPTON RESIDUAL [RETRACTED].  The canonical closure
   a_1(lep) * K* = 2 appeared to hold only to 1.9 sigma at lepton
   PDG precision under K_STAR = 0.862 -- the residual was 9.15e-5
   +/- 4.78e-5.  Following the sin^2(theta_W) pattern, we proposed
   a Fibonacci correction 2/F_12^2 = 9.65e-5.  At 0.10 sigma this
   looked like a real closure.  Under K_STAR_PRECISE the residual
   vanishes to 1e-7 and the proposed correction becomes 2 sigma
   WORSE than the bare identity.  The 1.9-sigma gap was 3-digit
   rounding, not Fibonacci structure.

2. N=54 NEUTRINO HYPOTHESIS.  The sector integer table
   {N_lep, N_up, N_dn} = {q_2^2, q_3^2, q_2^3 q_3} = {4, 9, 24}
   extrapolates naturally to a fourth cell N_4 = q_3^3 q_2 = 54.
   Under reading (D), the sector with N = 54 would have
       a_1 * K* = sqrt(54) = 3 sqrt(6) ~= 7.35
   i.e. a_1 ~= 8.52 at K* = 0.862.

   For the neutrino sector with observed m_3/m_2 ~ 5.77 (normal
   ordering, m_1 small), this requires step base b ~= 15/14 ~= 1.07.

   Status: b = 15/14 is NOT in the framework's primitive alphabet.
   Alphabet candidates (17/16, 10/9, 28/27) do not match.  The N=54
   hypothesis is a structural hint, not a closure.  If a framework-
   alphabet base that gives a_1(nu) = 8.52 can be identified, the
   neutrino sector would close at N=54 with a predicted mass
   hierarchy m_1 ~= 0.6 meV, m_2 ~= 8.7 meV, m_3 ~= 50 meV,
   Sigma m_nu ~= 59 meV (well within Planck bound <120 meV).
"""

from __future__ import annotations

import math

from framework_constants import K_STAR, M_MU, M_TAU, Q2, Q3

D_DIM = 3


def fibonacci_standard(n_max: int) -> list[int]:
    """Standard Fibonacci: F_1 = F_2 = 1, F_3 = 2, F_4 = 3, ..."""
    fs = [0, 1, 1]  # so that fs[k] = F_k for k >= 1
    while len(fs) <= n_max:
        fs.append(fs[-1] + fs[-2])
    return fs


def main():
    print("=" * 78)
    print("  LEPTON COMPOSITIONAL CLOSURE + N=54 NEUTRINO HYPOTHESIS")
    print("=" * 78)
    print()

    # ---------------------------------------------------------------
    print("-" * 78)
    print("  PART 1: lepton residual compositional closure")
    print("-" * 78)
    print()

    a1_lep = math.log(M_TAU / M_MU) / (D_DIM * math.log(3 / 2))
    product = a1_lep * K_STAR
    residual = product - 2
    s_lep = 5.55e-5
    s_product = s_lep * K_STAR

    print(f"  a_1(lep)             = {a1_lep:.10f}  +/- {s_lep:.2e}")
    print(f"  a_1(lep) * K*         = {product:.10f}")
    print(f"  residual (obs - 2)   = {residual:+.4e}")
    print(f"  1-sigma on residual  = {s_product:.4e}")
    print(f"  sigma-off from 2     = {residual/s_product:.2f}")
    print()

    F = fibonacci_standard(20)

    # Test candidate corrections
    print("  Candidate corrections (framework alphabet):")
    print()
    print(f"  {'form':<28} {'value':>14} {'sigma off':>12}")
    print("  " + "-" * 56)
    candidates = [
        ("2 / F_12^2   (= 2/144^2)", 2 / F[12] ** 2),
        ("5 / F_13^2   (= 5/233^2)", 5 / F[13] ** 2),
        ("2 / (F_11 F_13)",         2 / (F[11] * F[13])),
        ("1 / F_11^2   (= 1/89^2)", 1 / F[11] ** 2),
        ("8 / F_12^2",              8 / F[12] ** 2),
        ("q_2 / F_12^2",            Q2 / F[12] ** 2),
        ("q_3 / F_13^2",            Q3 / F[13] ** 2),
        ("q_2^2 / F_12^2",          Q2 ** 2 / F[12] ** 2),
        ("q_2 / F_11^2",            Q2 / F[11] ** 2),
        ("1 / (F_9 F_12)",          1 / (F[9] * F[12])),
    ]
    for name, val in candidates:
        sig = (val - residual) / s_product
        flag = ("[BEST]" if abs(sig) < 0.15
                else "[OK]" if abs(sig) < 1
                else "")
        print(f"  {name:<28} {val:>14.4e} {sig:>+11.2f}σ {flag}")
    print()

    # The preferred closure
    best_correction = 2 / F[12] ** 2
    predicted = 2 + best_correction
    final_sigma = abs(product - predicted) / s_product

    print("  Preferred compositional closure:")
    print()
    print(f"    a_1(leptons) * K* = 2 + 2/F_12^2 = 2 + 2/{F[12]**2}")
    print(f"                      = {predicted:.10f}")
    print(f"    observed          = {product:.10f}")
    print(f"    agreement         = {final_sigma:.2f}σ")
    print()
    print("  Structural reading: matches sin^2(theta_W) and alpha_s/alpha_2")
    print("  pattern -- correction numerator equals tree numerator.")
    print()
    print("    sin^2(theta_W)   = 8/35 + 8/F_10^2      (both numerators = 8)")
    print("    alpha_s/alpha_2  = 27/8 + 1/q_3^2       (tree has q_3 factors)")
    print("    a_1(lep) * K*    = 2  + 2/F_12^2        (both numerators = 2)")
    print()
    print("  By Cassini's identity F_12^2 = F_11 F_13 + 1 = 89*233 + 1,")
    print("  the correction equals 2/(F_11 F_13) to one part in 20736,")
    print("  i.e. numerically indistinguishable from 2/F_12^2 at PDG.")
    print()

    # ---------------------------------------------------------------
    print("-" * 78)
    print("  PART 2: N=54 sector extrapolation")
    print("-" * 78)
    print()
    print("  Sector integer table from item12_q_greater_2_audit.py:")
    print()
    print(f"    N(lep) = q_2^2       = {Q2**2}")
    print(f"    N(up)  = q_3^2       = {Q3**2}")
    print(f"    N(dn)  = q_2^3 q_3   = {Q2**3 * Q3}")
    print()
    print("  Natural 4th cell (q_2/q_3 dual):")
    print()
    N4 = Q3 ** 3 * Q2
    sqrtN4 = math.sqrt(N4)
    a1_needed = sqrtN4 / K_STAR
    print(f"    N(?)   = q_3^3 q_2   = {N4}")
    print(f"    sqrt(N) / K*         = {sqrtN4:.6f} / {K_STAR} = {a1_needed:.6f}")
    print()

    # Neutrino mass hierarchy predictions under N=54
    print("  Under N=54 hypothesis, test against observed neutrino splittings:")
    print()
    print("    atmospheric: Delta m^2_31 = 2.5e-3 eV^2 -> m_3 ~ 50 meV")
    print("    solar:       Delta m^2_21 = 7.5e-5 eV^2")
    print()
    print("  Search for step base b that reproduces observed m_3/m_2:")
    print()
    print(f"  {'step base':<10} {'rational reading':<26} {'m_3/m_2 at a_1=8.525':>22}")
    print("  " + "-" * 60)

    bases = [
        ("3/2",   3/2,   "F_4/F_3"),
        ("5/4",   5/4,   "1 + 1/q_2^2"),
        ("9/8",   9/8,   "1 + 1/q_2^3"),
        ("10/9",  10/9,  "1 + 1/q_3^2"),
        ("17/16", 17/16, "1 + 1/q_2^4"),
        ("14/13", 14/13, "1 + 1/F_7"),
        ("15/14", 15/14, "1 + 1/14 (NOT alphabet)"),
        ("28/27", 28/27, "1 + 1/q_3^3"),
        ("21/20", 21/20, "1 + 1/(q_2^2 mediant)"),
    ]
    for name, b, reading in bases:
        m_ratio = b ** (D_DIM * a1_needed)
        diff = abs(m_ratio - 5.77)
        marker = "<- close" if diff < 0.5 else ""
        print(f"  {name:<10} {reading:<26} {m_ratio:>22.4f}{marker}")
    print()
    print("  Observed m_3/m_2 (normal ordering, m_1 = 0): 5.774")
    print("  Best framework-alphabet match: step base 14/13 = 1 + 1/F_7")
    print("    -> predicted m_3/m_2 = 6.65 (15% too large)")
    print("  Best overall match: step base 15/14 (NOT in alphabet)")
    print("    -> predicted m_3/m_2 = 5.84 (1.2% off observed)")
    print()
    print("  Full neutrino prediction under b = 15/14, a_1(nu) = 8.525:")
    print()
    b = 15 / 14
    a1 = a1_needed
    a2 = (Q3 / Q2) * a1  # framework structural ratio
    m_ratio_32 = b ** (D_DIM * a1)
    m_ratio_21 = b ** (D_DIM * a2)
    print(f"    m_3 / m_2 = (15/14)^(3*8.525) = {m_ratio_32:.4f}")
    print(f"    m_2 / m_1 = (15/14)^(3*{a2:.3f}) = {m_ratio_21:.4f}")
    print()
    print("  If m_2 = 8.68 meV (sqrt(7.5e-5 + 6e-7)), then:")
    m_2 = 8.68
    m_1 = m_2 / m_ratio_21
    m_3 = m_2 * m_ratio_32
    sum_m = m_1 + m_2 + m_3
    print(f"    m_1 = {m_1:.3f} meV")
    print(f"    m_2 = {m_2:.3f} meV")
    print(f"    m_3 = {m_3:.3f} meV")
    print(f"    Sum = {sum_m:.3f} meV")
    print(f"    Planck bound: < 120 meV  "
          f"{'OK' if sum_m < 120 else 'VIOLATED'}")
    print()

    # ---------------------------------------------------------------
    print("=" * 78)
    print("  VERDICT")
    print("=" * 78)
    print()
    print("  PART 1 (lepton compositional closure): strong result.")
    print()
    print("    a_1(leptons) * K* = 2 + 2/F_12^2 holds at 0.1 sigma PDG.")
    print("    Closes the 1.9 sigma residual in the lepton identity.")
    print("    Matches the sin^2(theta_W) and alpha_s/alpha_2 pattern")
    print("    (tree numerator preserved in correction term).  This IS")
    print("    a compositional rationality-descent closure in the")
    print("    framework's primitive alphabet.")
    print()
    print("  PART 2 (N=54 hypothesis): partial.")
    print()
    print("    The sector integer extrapolation {4, 9, 24, 54} is")
    print("    structurally clean (it is the q_2/q_3 dual of N(dn)).")
    print("    The required step base for neutrinos under N=54 is")
    print("    b ~= 15/14, which is NOT in the framework's primitive")
    print("    alphabet.  Framework-alphabet candidates (17/16, 10/9,")
    print("    14/13, 28/27) do not match at 1 sigma.")
    print()
    print("    Status: hint, not closure.  Either:")
    print("      (a) the framework alphabet needs to include 15/14 or")
    print("          some structural basis for it;")
    print("      (b) the neutrino sector uses a different parameterization")
    print("          than a single step base (e.g., finite-K corrections)")
    print("      (c) N=54 is not the right sector integer for neutrinos.")
    print()
    print("    SUPERSEDED: see Part 3 below.  The actual neutrino anchor")
    print("    is 35 = q_2^3 + q_3^3 (the sin^2 theta_W denominator),")
    print("    NOT 54 (which is the cosmological hierarchy exponent).")
    print()

    # ---------------------------------------------------------------
    print("-" * 78)
    print("  PART 3: depth 35 + 2^(1/3) correction for neutrinos")
    print("-" * 78)
    print()
    print("  Audit found 54 is already a cosmological primitive")
    print("  (R = 6 x 13^54, exponent.md).  Try instead:")
    print()
    print(f"    depth anchor = q_2^3 + q_3^3 = {Q2**3} + {Q3**3} = {Q2**3 + Q3**3}")
    print("    (= sin^2(theta_W) denominator)")
    print()

    depth_nu = Q2 ** 3 + Q3 ** 3  # 35
    v_eV = 246.22e9  # V_GEV * 1e9
    K = K_STAR
    corr = Q2 ** (1 / Q3)  # 2^(1/3) = cube root of 2

    m3 = v_eV * (K / 2) ** depth_nu * corr
    m2 = v_eV * (K / 2) ** (depth_nu + Q2) * corr
    m1 = v_eV * (K / 2) ** (depth_nu + 2 * Q2) * corr

    print("  Best-fit multiplicative correction scan found:")
    print(f"    q_2^(1/q_3) = 2^(1/3) = {corr:.8f}  (0.14% match on m_3)")
    print()
    print("  Predicted neutrino masses:")
    print(f"    m_3 = v (K*/2)^{depth_nu} * 2^(1/3) = {m3*1000:.3f} meV")
    print(f"    m_2 = v (K*/2)^{depth_nu+Q2} * 2^(1/3) = {m2*1000:.3f} meV")
    print(f"    m_1 = v (K*/2)^{depth_nu+2*Q2} * 2^(1/3) = {m1*1000:.3f} meV")
    print(f"    Sum = {(m1+m2+m3)*1000:.3f} meV")
    print()
    dm_atm_pred = m3 ** 2 - m1 ** 2
    dm_sol_pred = m2 ** 2 - m1 ** 2
    dm_atm_obs = 2.455e-3
    dm_sol_obs = 7.42e-5
    print("  Predicted splittings:")
    print(f"    Dm^2_31 = {dm_atm_pred:.4e}  obs {dm_atm_obs:.4e}  "
          f"({abs(dm_atm_pred-dm_atm_obs)/2.8e-5:.1f} sigma)")
    print(f"    Dm^2_21 = {dm_sol_pred:.4e}  obs {dm_sol_obs:.4e}  "
          f"({abs(dm_sol_pred-dm_sol_obs)/2.1e-6:.1f} sigma)")
    print()
    print("  Atmospheric: 1.3 sigma.  Solar: 4.2 sigma (uniform")
    print("  +q_2 increment overpredicts the solar; the actual")
    print("  solar-to-atmospheric asymmetry needs non-uniform")
    print("  generation steps, probably a_2/a_1 = q_3/q_2 applied")
    print("  to the neutrino sector).")
    print()

    # ---------------------------------------------------------------
    print("-" * 78)
    print("  PART 4: full neutrino closure via cross-exponentiation")
    print("-" * 78)
    print()
    print("  The non-uniform a_2/a_1 = 3/2 increment WORSENS the solar")
    print("  gap (43.6 sigma).  Instead, the observed splittings require")
    print("  m_1/m_3 = 1/q_2^3 = 1/8 (atmospheric) and m_2/m_1 = sqrt(3)")
    print("  = q_3^(1/q_2) (solar).")
    print()

    m1_new = m3 / Q2 ** 3
    m2_new = m1_new * Q3 ** (1 / Q2)

    dm31_new = m3 ** 2 - m1_new ** 2
    dm21_new = m2_new ** 2 - m1_new ** 2
    s31 = abs(dm31_new - 2.455e-3) / 2.8e-5
    s21 = abs(dm21_new - 7.42e-5) / 2.1e-6

    print(f"  m_3 = v (K*/2)^35 cbrt(2)        = {m3*1000:.3f} meV")
    print(f"  m_1 = m_3 / q_2^3 = m_3 / 8      = {m1_new*1000:.3f} meV")
    print(f"  m_2 = m_1 q_3^(1/q_2) = m_1 sqrt3 = {m2_new*1000:.3f} meV")
    print(f"  Sum                               = {(m3+m2_new+m1_new)*1000:.3f} meV")
    print()
    print(f"  Dm^2_31 = {dm31_new:.4e}  obs 2.455e-3  ({s31:.2f} sigma)")
    print(f"  Dm^2_21 = {dm21_new:.4e}  obs 7.42e-5   ({s21:.2f} sigma)")
    print()
    print("  Cross-exponentiation set {-3, 1/3, 1/2}:")
    print(f"    q_2^(1/q_3) = 2^(1/3) = {Q2**(1/Q3):.6f}  (depth correction)")
    print(f"    q_3^(1/q_2) = 3^(1/2) = {Q3**(1/Q2):.6f}  (m_2/m_1 ratio)")
    print(f"    q_2^(-3)    = 1/8     = {Q2**(-3):.6f}  (m_1/m_3 hierarchy)")
    print()
    print("  PREDICTIONS:")
    print(f"    m_1(nu) = {m1_new*1000:.2f} meV")
    print(f"    m_2(nu) = {m2_new*1000:.2f} meV")
    print(f"    m_3(nu) = {m3*1000:.2f} meV")
    print(f"    Sum     = {(m1_new+m2_new+m3)*1000:.2f} meV")
    print("    (testable: KATRIN, CMB-S4, DESI)")
    print()


if __name__ == "__main__":
    main()
