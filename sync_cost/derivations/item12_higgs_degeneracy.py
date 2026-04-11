"""
Item 12: break the q_2 = 2 degeneracy on the Higgs quartic.

The framework's Higgs quartic lambda = 1/8 has two possible readings:

  Form A: lambda = 1/(2 q^2)    -- half inverse square
  Form B: lambda = 1/q^d         -- duty cycle with d = 3

Both give 1/8 for q = 2 because 2 * 2^2 = 2^3 = 8. The degeneracy is
a coincidence at the framework's specific q_2 = 2.

For q = 3 the two forms differ:
  Form A: 1/(2*9) = 1/18 = 0.05555
  Form B: 1/27    = 0.03703

This script checks whether the framework's sin^2(theta_W) prediction
breaks the degeneracy. The duty-cycle dictionary gives
    1/alpha_Y(tree) = q_3^d
    1/alpha_2(tree) = q_2^d
    sin^2(theta_W)  = alpha_Y / (alpha_Y + alpha_2)
                    = (1/q_3^d) / (1/q_2^d + 1/q_3^d)
                    = q_2^d / (q_2^d + q_3^d)

Under form B (d = 3): sin^2(theta_W) = 8/35 = 0.2286 -- matches
observation.
Under form A (with "d" = 2 and factor 1/2):
    1/alpha_Y = 2 q_3^2 = 18
    1/alpha_2 = 2 q_2^2 = 8
    sin^2(theta_W) = 8 / (8 + 18) = 8/26 = 4/13 = 0.3077
This does NOT match observation.

So if form A were correct for the Higgs, the same form would give a
sin^2(theta_W) that's 33% too high. The framework's sin^2(theta_W)
prediction FORCES form B (the 1/q^3 duty cycle) at the coupling
dictionary level. Since lambda = 1/8 at q = 2 only by coincidence
under either form, the q = 3 analog distinguishes them decisively.

Conclusion: the Higgs quartic is 1/q_2^3, not 1/(2 q_2^2). The
"2 q^2" reading is retired. The framework's Higgs identification
is on the 1/q^d = 1/q^3 duty-cycle line, consistent with its
treatment of the gauge couplings.
"""

import math


Q2, Q3 = 2, 3
D = 3


# ============================================================================
# The two forms, evaluated at each denominator class
# ============================================================================

def form_A(q):
    """lambda = 1/(2 q^2)"""
    return 1 / (2 * q * q)


def form_B(q):
    """lambda = 1/q^d"""
    return 1 / (q ** D)


# ============================================================================
# sin^2(theta_W) prediction under each form
# ============================================================================

def sin2_theta_W(form):
    """
    Framework: sin^2(theta_W) = alpha_Y/(alpha_Y + alpha_2)
                              = (1/(1/alpha_Y)) / (1/(1/alpha_Y) + 1/(1/alpha_2))
    with 1/alpha_2 = 1/form(q_2), 1/alpha_Y = 1/form(q_3).
    Equivalently: sin^2 = form(q_3) / (form(q_2) + form(q_3)).

    Wait -- need to be careful. Tree value of 1/alpha_2 is inverse
    of form(q_2). If form(q) is the coupling alpha directly, then
    1/alpha_2 = 1/form(q_2) = q_2^d or 2 q_2^2.
    And sin^2 = alpha_Y / (alpha_Y + alpha_2) = form(q_3) / (form(q_2) + form(q_3)).

    For form B (alpha = 1/q^d): sin^2 = (1/q_3^d) / (1/q_2^d + 1/q_3^d)
                                      = q_2^d / (q_2^d + q_3^d) = 8/35.
    For form A (alpha = 1/(2q^2)): sin^2 = (1/(2q_3^2)) / (1/(2q_2^2) + 1/(2q_3^2))
                                         = q_2^2 / (q_2^2 + q_3^2) = 4/13.
    """
    aY = form(Q3)
    a2 = form(Q2)
    return aY / (aY + a2)


# ============================================================================
# Main
# ============================================================================

def main():
    print("=" * 78)
    print("  BREAK THE q_2 = 2 DEGENERACY ON HIGGS LAMBDA")
    print("=" * 78)
    print()
    print("  Two candidate forms for the Higgs quartic coupling:")
    print("    Form A: lambda = 1/(2 q^2)")
    print("    Form B: lambda = 1/q^d  with d = 3 (duty cycle)")
    print()
    print("  Both give 1/8 at q = 2 (the framework's lepton/weak denominator)")
    print("  because 2 * 2^2 = 2^3 = 8. The degeneracy is a coincidence")
    print("  at q_2 = 2. Let's compute both at q = 3 to distinguish them.")
    print()

    # ------------------------------------------------------------------
    print("-" * 78)
    print("  Values at each q")
    print("-" * 78)
    print()
    print(f"  {'q':>4} {'form A (1/(2q^2))':>20} {'form B (1/q^3)':>18} {'difference':>14}")
    print("  " + "-" * 60)
    for q in [1, 2, 3, 4, 5]:
        A = form_A(q)
        B = form_B(q)
        print(f"  {q:>4} {A:>20.6f} {B:>18.6f} {A - B:>+14.6f}")
    print()
    print("  Note: at q = 2 both forms give 0.1250. Everywhere else they differ.")
    print()

    # ------------------------------------------------------------------
    print("-" * 78)
    print("  sin^2(theta_W) prediction under each form")
    print("-" * 78)
    print()
    print("  Framework: alpha_i(tree) = lambda-form(q_i), so")
    print("    1/alpha_2 = 1/form(q_2),  1/alpha_Y = 1/form(q_3)")
    print("    sin^2 theta_W = alpha_Y / (alpha_Y + alpha_2)")
    print()

    sin2_A = sin2_theta_W(form_A)
    sin2_B = sin2_theta_W(form_B)
    obs = 0.23122

    print(f"  Under form A: sin^2 theta_W = q_2^2 / (q_2^2 + q_3^2)")
    print(f"                              = 4 / 13 = {sin2_A:.6f}")
    print(f"  Under form B: sin^2 theta_W = q_2^3 / (q_2^3 + q_3^3)")
    print(f"                              = 8 / 35 = {sin2_B:.6f}")
    print(f"  Observed (PDG 2024):                   = {obs:.6f}")
    print()
    print(f"  Form A error: {abs(sin2_A - obs) / obs * 100:>6.2f}%")
    print(f"  Form B error: {abs(sin2_B - obs) / obs * 100:>6.2f}%")
    print()
    print("  Form A is 33% off. Form B matches observation to 1.1% (and")
    print("  with the 8/F_10^2 finite-K correction from item12_sin_W_and_signs.py,")
    print("  matches to PDG precision).")
    print()

    # ------------------------------------------------------------------
    print("-" * 78)
    print("  1/alpha values under each form")
    print("-" * 78)
    print()
    print(f"  {'':<20} {'form A':>12} {'form B':>12} {'observed(M_Z)':>16}")
    print("  " + "-" * 60)
    print(f"  {'1/alpha_2 (tree)':<20} {1/form_A(Q2):>12.4f} {1/form_B(Q2):>12.4f} "
          f"{29.57:>16.4f}")
    print(f"  {'1/alpha_Y (tree)':<20} {1/form_A(Q3):>12.4f} {1/form_B(Q3):>12.4f} "
          f"{98.40:>16.4f}")
    print(f"  {'1/alpha_em (tree)':<20} "
          f"{1/form_A(Q2) + 1/form_A(Q3):>12.4f} "
          f"{1/form_B(Q2) + 1/form_B(Q3):>12.4f} "
          f"{137.04:>16.4f}")
    print()
    print("  Form B gives 1/alpha_em(tree) = 35. The framework's hierarchy")
    print("  (R = 6 * 13^54) takes this tree value and runs it to 137 at M_Z.")
    print("  Form A gives 1/alpha_em(tree) = 26, which is wrong at both")
    print("  the ratio level (sin^2) and the individual-coupling level.")
    print()

    # ------------------------------------------------------------------
    print("=" * 78)
    print("  CONCLUSION")
    print("=" * 78)
    print()
    print("  The q_2 = 2 degeneracy on the Higgs quartic lambda = 1/8 is")
    print("  BROKEN by the framework's sin^2(theta_W) prediction.")
    print()
    print("  Under form B (duty cycle 1/q^d with d = 3):")
    print("    - Higgs lambda = 1/q_2^3 = 1/8 (observed 0.129, 3.4% off)")
    print("    - sin^2 theta_W = 8/35 (observed 0.23122, with 8/F_10^2")
    print("      correction matches to PDG precision)")
    print("    - 1/alpha_em(tree) = 35")
    print()
    print("  Under form A (half inverse square 1/(2q^2)):")
    print("    - Higgs lambda = 1/(2*4) = 1/8 (by coincidence at q=2)")
    print("    - sin^2 theta_W = 4/13 = 0.308 (33% OFF observed)")
    print("    - 1/alpha_em(tree) = 26 (wrong)")
    print()
    print("  Form B is forced by sin^2 theta_W matching observation.")
    print("  The Higgs quartic is lambda = 1/q_2^3, not 1/(2 q_2^2).")
    print("  The framework's Higgs identification is on the duty-cycle line.")
    print()
    print("  What this DOESN'T resolve: the 3.4% residual between framework")
    print("  lambda = 1/8 and observed lambda = 0.129. Form B correctly")
    print("  identifies the structural form but the residual is still")
    print("  unexplained by any (prefactor)/F_k^2 under 0.5%.")
    print()
    print("  However, the form is now TIGHT. The Higgs quartic is structurally")
    print("  lambda = 1/q_2^3 = duty(q_2) = alpha_2(tree), which is consistent")
    print("  with the framework's gauge-coupling dictionary. The residual is")
    print("  a finite-K correction to the tree-level duty cycle, analogous to")
    print("  the corrections on sin^2(theta_W) and alpha_s/alpha_2 -- but the")
    print("  specific Fibonacci depth (if any) for the Higgs correction is")
    print("  not yet identified.")
    print()


if __name__ == "__main__":
    main()
