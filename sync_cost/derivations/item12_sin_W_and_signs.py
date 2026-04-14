"""
Item 12/10 cross-check: does the sin^2(theta_W) 1.1% residual have
the same structural form as the lepton C residual?

The lepton C residual was matched to within 2ppm by a multiplicative
(1 + 1/F_10^2) correction. This script checks:

  1. Is the sin^2(theta_W) residual also a 1/F_k^2 multiplicative form?
  2. If so, at what k?
  3. Are the two residuals related by a simple structural factor
     (e.g., the 8/35 denominator itself)?

Also checks the sign-alternation hypothesis for the up/down sector
residuals against Fibonacci convergent over/under behavior.
"""

import math

PHI = (1 + math.sqrt(5)) / 2
INV_PHI_SQ = 1 / (PHI * PHI)

# Tree-scale sin^2(theta_W) from duty-cycle dictionary
Q2, Q3 = 2, 3
D = 3
SIN2_TREE = (Q2 ** D) / (Q2 ** D + Q3 ** D)     # 8/35 = 0.22857
SIN2_OBS  = 0.23121                              # PDG at M_Z
EPS_W = (SIN2_OBS - SIN2_TREE) / SIN2_TREE       # 0.01154

# Lepton C residual from earlier
EPS_C = 0.00033240


def fib(k):
    a, b = 1, 1
    for _ in range(k - 1):
        a, b = b, a + b
    return a


# ============================================================================
# Main
# ============================================================================

def main():
    print("=" * 78)
    print("  sin^2(theta_W) residual: does it match 1/F_k^2?")
    print("=" * 78)
    print()
    print(f"  Tree (duty dict): 8/35         = {SIN2_TREE:.10f}")
    print(f"  Observed at M_Z:                = {SIN2_OBS:.10f}")
    print(f"  Multiplicative residual eps_W  = {EPS_W:.6e}")
    print(f"  (the 1.1% gap)")
    print()
    print(f"  Lepton C residual eps_C        = {EPS_C:.6e}")
    print(f"  Ratio eps_W / eps_C            = {EPS_W/EPS_C:.4f}")
    print()
    print("  Note: 8 + 27 = 35, the denominator of 8/35.")
    print(f"  eps_W / eps_C vs 35            = {EPS_W/EPS_C:.2f} vs 35")
    print()

    # Check 1/F_k^2 match for sin^2(theta_W)
    print("-" * 78)
    print("  1/F_k^2 candidates for eps_W:")
    print("-" * 78)
    print()
    print(f"    {'k':>3} {'F_k':>6} {'1/F_k^2':>14} {'rel err vs eps_W':>20}")
    print("    " + "-" * 48)
    best_k, best_err = None, float('inf')
    for k in range(3, 20):
        Fk = fib(k)
        corr = 1 / (Fk * Fk)
        err = abs(corr - EPS_W) / EPS_W * 100
        if err < best_err:
            best_err = err
            best_k = k
        flag = " <<" if err < 10 else ""
        print(f"    {k:>3} {Fk:>6} {corr:>14.8f} {err:>19.2f}%{flag}")
    print()
    print(f"  Best 1/F_k^2 for eps_W: k = {best_k}, F_{best_k} = {fib(best_k)}, "
          f"err {best_err:.2f}%")
    print()

    # Check 1/phi^k
    print("-" * 78)
    print("  1/phi^k candidates for eps_W:")
    print("-" * 78)
    print()
    print(f"    {'k':>3} {'1/phi^k':>14} {'rel err':>12}")
    print("    " + "-" * 34)
    best_k_phi, best_err_phi = None, float('inf')
    for k in range(4, 15):
        corr = 1 / (PHI ** k)
        err = abs(corr - EPS_W) / EPS_W * 100
        if err < best_err_phi:
            best_err_phi = err
            best_k_phi = k
        flag = " <<" if err < 10 else ""
        print(f"    {k:>3} {corr:>14.8f} {err:>11.2f}%{flag}")
    print()
    print(f"  Best 1/phi^k for eps_W: k = {best_k_phi}, err {best_err_phi:.2f}%")
    print()

    # Check 1/(F_k * F_{k+1}) forms
    print("-" * 78)
    print("  1/(F_k * F_{k+1}) product candidates:")
    print("-" * 78)
    print()
    print(f"    {'k':>3} {'F_k * F_{k+1}':>16} {'1/product':>14} {'rel err':>12}")
    print("    " + "-" * 50)
    for k in range(3, 15):
        prod = fib(k) * fib(k + 1)
        corr = 1 / prod
        err = abs(corr - EPS_W) / EPS_W * 100
        flag = " <<" if err < 10 else ""
        print(f"    {k:>3} {prod:>16} {corr:>14.8f} {err:>11.2f}%{flag}")
    print()

    # The specific 8+27=35 connection
    print("-" * 78)
    print("  THE 8+27=35 STRUCTURAL FORM")
    print("-" * 78)
    print()
    print(f"  sin^2(theta_W) = q_2^3 / (q_2^3 + q_3^3) = 8/35")
    print(f"  The denominator 35 = 8 + 27 is the total 'duty budget'.")
    print()
    print(f"  Observed eps_W  = {EPS_W:.6e}")
    print(f"  35 * eps_C      = {35 * EPS_C:.6e}")
    print(f"  Ratio           = {EPS_W / (35 * EPS_C):.4f}")
    print()
    print(f"  (q_2^3 + q_3^3) * eps_C = 35 * eps_C = {35 * EPS_C:.6e}")
    print(f"  Close to eps_W = {EPS_W:.6e}?")
    print(f"  Rel err         = {abs(EPS_W - 35*EPS_C)/EPS_W * 100:.3f}%")
    print()

    # Maybe (8+27) * (something) * eps_C
    print(f"  Try  eps_W = (q_2^3 + q_3^3) * eps_C * correction")
    print(f"  correction = {EPS_W / (35 * EPS_C):.6f}")
    print()

    # Sign alternation: Fibonacci convergents
    print("-" * 78)
    print("  SIGN ALTERNATION FROM FIBONACCI CONVERGENTS TO PHI")
    print("-" * 78)
    print()
    print("  Consecutive Fibonacci convergents F_{k+1}/F_k alternate above")
    print("  and below phi = 1.618034. This IS the framework's natural")
    print("  sign-alternation mechanism.")
    print()
    print(f"    {'k':>3} {'F_{k+1}/F_k':>14} {'- phi':>14} {'side':>8}")
    print("    " + "-" * 44)
    for k in range(1, 10):
        ratio = fib(k + 1) / fib(k)
        diff = ratio - PHI
        side = "above" if diff > 0 else "below"
        print(f"    {k:>3} {ratio:>14.6f} {diff:>+14.6f} {side:>8}")
    print()
    print("  Key point: consecutive convergents ALTERNATE above/below phi,")
    print("  with the difference shrinking as 1/(phi^2 F_k^2). Any quantity")
    print("  built from consecutive convergents inherits this alternation.")
    print()

    # Sector residual signs
    print("-" * 78)
    print("  SECTOR RESIDUAL SIGNS")
    print("-" * 78)
    print()
    print("  From item12_residual_sectors.py:")
    print("    leptons:   +0.000332  (small positive)")
    print("    up-type:   +0.002548  (larger positive)")
    print("    down-type: -0.001536  (negative)")
    print()
    print("  The sign alternation between up-type and down-type matches the")
    print("  Fibonacci convergent behavior. Up-type uses b_1 = 8/5 = F_6/F_5")
    print("  (below phi), down-type uses b_1 = 5/4 (not a convergent). If the")
    print("  correction were strictly from Fibonacci over/undershoot, we'd")
    print("  expect the sign to track 'above phi' vs 'below phi' for each")
    print("  sector's base pair.")
    print()
    print("  Up-type 8/5 = 1.600 is BELOW phi (-0.018)")
    print("  Up-type 3/2 = 1.500 is BELOW phi (-0.118)")
    print("  Both below -- the total step base product is 'below'.")
    print()
    print("  Leptons 3/2 = 1.500 is BELOW phi (-0.118)")
    print("  Leptons 5/3 = 1.667 is ABOVE phi (+0.049)")
    print("  Mixed -- one above, one below.")
    print()
    print("  Down-type 5/4 and 9/8 are NOT Fibonacci convergents. 5/4 = 1.250")
    print("  and 9/8 = 1.125 are far below phi.")
    print()
    print("  Pattern: does the residual sign correlate with (b_1 - phi) sign?")
    print("    leptons b_1 - phi = 1.500 - 1.618 = -0.118 (below) -> residual +")
    print("    up-type b_1 - phi = 1.600 - 1.618 = -0.018 (below) -> residual +")
    print("    down-type b_1 - phi = 1.250 - 1.618 = -0.368 (below) -> residual -")
    print()
    print("  All three b_1's are below phi, but the residual signs differ.")
    print("  So the sign alternation is NOT directly from the b_1 position.")
    print("  The pattern must involve something else -- perhaps the parity")
    print("  of the walk depth, or the sector's specific Fibonacci index.")
    print()


if __name__ == "__main__":
    main()
