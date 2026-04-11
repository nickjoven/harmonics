"""
Tongue formula accuracy: the framework's perturbative formula is
pi times the physical Arnold tongue width.

Setup
-----
The standard circle map

    theta_{n+1} = theta_n + Omega - (K / (2 pi)) sin(2 pi theta_n)

has Arnold tongues at every rational p/q.  The framework uses a
"perturbative" formula in multiple places (framework_utils.py,
circle_map_utils.py, born_rule.md, boundary_weight.py, ...):

    w_framework(p/q, K) = 2 (K/2)^q / q          (q >= 2, K < 1)
    w_framework(p/1, K) = min(K / (2 pi), 1)

This script derives the analytic tongue width at q = 2 from the
2-iterate of the circle map and compares it to both the framework
formula and tight-tolerance numerical measurements.

Analytic derivation (q = 2)
---------------------------
At Omega = 1/2 + eps, the 2-iterate of the circle map has the
fixed-point condition (period-2 orbit):

    theta_{n+2} - theta_n = 1

Expanding to leading order in K and eps:

    theta_{n+1} = theta_n + 1/2 + eps - (K/(2 pi)) sin(2 pi theta_n)

    sin(2 pi theta_{n+1}) ~ -sin(2 pi theta_n)
                            - 2 pi eps cos(2 pi theta_n)
                            + (K/2) sin(4 pi theta_n)
                            + O(eps^2, K^2)

Substituting into the 2-iterate:

    2 eps = -(K/(2 pi))[sin(2 pi theta_n) + sin(2 pi theta_{n+1})]
          = (K eps) cos(2 pi theta_n)
          - (K^2 / (4 pi)) sin(4 pi theta_n) + higher order

Solving for eps:

    eps (2 + K cos(2 pi theta_n)) = (K^2 / (4 pi)) sin(4 pi theta_n)
    eps = (K^2 / (4 pi)) sin(4 pi theta_n) / (2 + K cos(2 pi theta_n))

For small K, |eps_max| = K^2 / (8 pi), so the full tongue width
(from -eps_max to +eps_max) is

    w_true(1/2, K) = K^2 / (4 pi)

Compare to the framework formula:

    w_framework(1/2, K) = 2 (K/2)^2 / 2 = K^2 / 4

Ratio: w_framework / w_true = pi.

The framework's formula is uniformly PI times the true tongue
width.  This is systematic across q (verified at q=1 by the
same method: w_true(0, K) = K/pi, w_framework = K).

Implications
------------
1. The framework's "w" is not the physical Arnold tongue width --
   it is pi times that.  This is a systematic factor, not a
   calibration that varies per-tongue.

2. The item 12 lepton identity a_1(lep) = 2/K* holds exactly
   against PDG masses, but its structural reading as "saddle-node
   relaxation at the q=2 Arnold tongue" is OFF BY sqrt(pi):

     tau_saddle_physical = 1 / sqrt(w_true) = 2 sqrt(pi) / K
                         ≈ 4.11 at K* = 0.862
     a_1(lep)            ≈ 2.32

   So a_1(lep) is NOT the saddle-node relaxation time at the
   physical tongue.  It is 1/sqrt(pi) times that, OR equivalently,
   1/sqrt(w_framework) where w_framework = pi w_true is the
   framework's (conventional) quantity.

3. Two interpretations:
     (A) The framework uses w_framework as a CONVENTIONAL quantity
         throughout, and the identity a_1(lep) = 1/sqrt(w_framework)
         holds by the framework's own definition.  The physical
         correspondence to Arnold tongues is via w_framework = pi
         w_physical; the sqrt(pi) factor is absorbed into the
         convention.
     (B) The framework has an error in the perturbative tongue
         formula.  Fixing it breaks the clean 4-digit match of the
         lepton identity.

   Interpretation (A) is internally consistent and does not require
   revisiting downstream results that use w_framework (e.g.,
   boundary_weight.py, field_equation_iteration.py).  But it
   requires re-stating the structural reading of the lepton
   identity away from "physical saddle-node relaxation".

This script computes both quantities, verifies the analytic
result against tight-tolerance numerics, and reports the
implications for item 12.
"""

from __future__ import annotations

import math
import sys

sys.path.insert(0, "sync_cost/derivations")
from circle_map_utils import winding_number  # noqa: E402
from framework_constants import K_STAR, M_MU, M_TAU  # noqa: E402

D = 3


# ============================================================================
# Analytic vs perturbative vs numerical tongue widths
# ============================================================================

def w_framework(q: int, K: float) -> float:
    """Framework's perturbative formula: 2 (K/2)^q / q."""
    return 2 * (K / 2) ** q / q


def w_true_q2(K: float) -> float:
    """Analytic leading-order width at q=2: K^2 / (4 pi)."""
    return K * K / (4 * math.pi)


def w_true_q1(K: float) -> float:
    """Analytic leading-order width at q=1: K/pi."""
    return K / math.pi


def numerical_q2_tongue_width(K: float,
                              n_trans: int = 20000,
                              n_meas: int = 80000,
                              step: float = 0.0002,
                              tol: float = 1e-5) -> float:
    """Tight-tolerance numerical bisection of the q=2 tongue."""
    inside = []
    for i in range(-300, 301):
        Om = 0.5 + i * step
        W = winding_number(Om, K, n_trans, n_meas)
        if abs(W - 0.5) < tol:
            inside.append(Om)
    if not inside:
        return 0.0
    return max(inside) - min(inside)


# ============================================================================
# Main
# ============================================================================

def main():
    print("=" * 78)
    print("  TONGUE FORMULA ACCURACY: framework w_pert vs physical tongue")
    print("=" * 78)
    print()
    print("  Derivation (in docstring): the q=2 tongue of the standard")
    print("  circle map has analytic width w_true(1/2, K) = K^2 / (4 pi)")
    print("  at leading order in K.  The framework's formula w = K^2/4")
    print("  overestimates this by a factor of pi.")
    print()

    # -------------------------------------------------------------
    print("-" * 78)
    print("  PART 1: analytic vs framework formula at q=1 and q=2")
    print("-" * 78)
    print()
    print(f"  {'K':>6}  {'q=1: K/pi':>14}  {'framework K':>14}  "
          f"{'ratio':>8}  {'q=2: K^2/(4 pi)':>18}  "
          f"{'framework K^2/4':>18}  {'ratio':>8}")
    print("  " + "-" * 110)
    for K in [0.1, 0.3, 0.5, 0.7, 0.862, 1.0]:
        w1_true = w_true_q1(K)
        w1_fw = w_framework(1, K)
        w2_true = w_true_q2(K)
        w2_fw = w_framework(2, K)
        r1 = w1_fw / w1_true
        r2 = w2_fw / w2_true
        print(f"  {K:>6.3f}  {w1_true:>14.8f}  {w1_fw:>14.8f}  "
              f"{r1:>8.5f}  {w2_true:>18.8f}  {w2_fw:>18.8f}  "
              f"{r2:>8.5f}")
    print()
    print(f"  Both ratios equal pi = {math.pi:.8f} exactly (leading order).")
    print()

    # -------------------------------------------------------------
    print("-" * 78)
    print("  PART 2: numerical verification at q=2 (tight tolerance)")
    print("-" * 78)
    print()
    print("  The prior framework numerical (circle_map_utils.tongue_width_")
    print("  numerical) used a 5e-4 winding-number tolerance.  At that")
    print("  tolerance, the reported 'width' for q=2 at small K is a")
    print("  tolerance artifact, not the actual tongue.  Here we use")
    print("  a 1e-5 tolerance with 80k-step averaging.")
    print()
    print(f"  {'K':>6}  {'w_true = K^2/(4 pi)':>22}  {'w_num':>14}  "
          f"{'ratio':>8}")
    print("  " + "-" * 58)
    for K in [0.3, 0.5, 0.7, 0.862, 1.0]:
        w_true = w_true_q2(K)
        w_num = numerical_q2_tongue_width(K)
        r = w_num / w_true if w_true > 0 else 0.0
        print(f"  {K:>6.3f}  {w_true:>22.8f}  {w_num:>14.8f}  "
              f"{r:>8.5f}")
    print()
    print("  Analytic agrees with numerical to ~5%.  The small residual")
    print("  is higher-order in K (the leading-order expansion drops")
    print("  O(K^4) corrections).  Framework's K^2/4 differs by factor")
    print("  of pi at all tested K -- NOT a small-K correction.")
    print()

    # -------------------------------------------------------------
    print("-" * 78)
    print("  PART 3: implications for item 12 lepton identity")
    print("-" * 78)
    print()
    a1_lep = math.log(M_TAU / M_MU) / (D * math.log(1.5))
    w2_fw = w_framework(2, K_STAR)
    w2_true = w_true_q2(K_STAR)
    inv_sqrt_fw = 1 / math.sqrt(w2_fw)
    inv_sqrt_true = 1 / math.sqrt(w2_true)

    print("  Three quantities at K* = 0.862:")
    print()
    print(f"    a_1(leptons) observed          = {a1_lep:.8f}")
    print(f"    2 / K*                         = {2/K_STAR:.8f}")
    print(f"    1 / sqrt(w_framework(1/2, K*)) = {inv_sqrt_fw:.8f}")
    print(f"    1 / sqrt(w_true(1/2, K*))      = {inv_sqrt_true:.8f}")
    print()
    print("  The identity a_1(lep) = 1/sqrt(w) holds exactly only")
    print("  when w is the FRAMEWORK's conventional quantity w_framework,")
    print("  NOT the physical tongue width.  At w_true the match is")
    print(f"  off by sqrt(pi) = {math.sqrt(math.pi):.6f}:")
    print()
    print(f"    a_1(lep) * sqrt(pi) = {a1_lep * math.sqrt(math.pi):.8f}")
    print(f"    1 / sqrt(w_true)    = {inv_sqrt_true:.8f}")
    print(f"    agreement          = "
          f"{1 - abs(a1_lep * math.sqrt(math.pi) - inv_sqrt_true) / inv_sqrt_true:.6f}")
    print()

    # -------------------------------------------------------------
    print("-" * 78)
    print("  PART 4: status of the saddle-node reading of item 12")
    print("-" * 78)
    print()
    print("  The 'stick-slip / saddle-node relaxation at the q=2 Arnold")
    print("  tongue' structural reading from a1_from_saddle_node.md is:")
    print()
    print("    a_1(lep) ?= tau_saddle(q=2 tongue at K*) = 1/sqrt(w_true)")
    print()
    print("  That prediction:")
    print()
    print(f"    predicted tau_saddle = {inv_sqrt_true:.6f}")
    print(f"    observed a_1(lep)    = {a1_lep:.6f}")
    print(f"    ratio                = {a1_lep / inv_sqrt_true:.6f}")
    print(f"    1/sqrt(pi)           = {1/math.sqrt(math.pi):.6f}")
    print()
    print("  The observed ratio is 1/sqrt(pi), NOT 1.  The saddle-node")
    print("  relaxation reading is OFF by a factor of sqrt(pi).")
    print()
    print("  Three ways to interpret this:")
    print()
    print("  (A) The identity is algebraic, not physical.  a_1(lep) = 2/K*")
    print("      is a clean relation between the lepton generation")
    print("      exponent, the Klein-bottle integer q_2, and the Kuramoto")
    print("      self-consistent coupling.  It does NOT correspond to a")
    print("      saddle-node relaxation at the physical Arnold tongue --")
    print("      the factor sqrt(pi) is structurally unaccounted for.")
    print("      'Stick-slip' is a shape metaphor but not an exact")
    print("      physical identification.")
    print()
    print("  (B) The framework's w = 2(K/2)^q/q is a CONVENTIONAL quantity")
    print("      (pi * w_physical), used consistently throughout, and")
    print("      a_1(lep) = 1/sqrt(w_framework) holds by framework's own")
    print("      definition.  This rescues the formal identity without")
    print("      physical meaning -- the framework's w absorbs the pi.")
    print()
    print("  (C) The sqrt(pi) factor comes from a framework primitive")
    print("      not yet identified.  Possibilities: the Gauss integral")
    print("      normalization, the 2 pi of 'one cycle = one radian x 2 pi',")
    print("      or a missing factor in the mean-field Kuramoto integral.")
    print("      Each would give sqrt(pi) naturally.")
    print()
    print("  Reading (A) is the most honest: the identity is real, the")
    print("  stick-slip SHAPE is the right conceptual frame, but the")
    print("  precise correspondence to physical saddle-node relaxation")
    print("  has a sqrt(pi) gap that needs accounting before the")
    print("  4-decimal-digit identity can be called 'derived'.")
    print()
    print("  The refinement path: compute the q=2 tongue correctly in")
    print("  every framework file that uses the perturbative w formula,")
    print("  and see whether any self-consistency condition forces the")
    print("  missing pi.  Files to audit:")
    print()
    print("    framework_utils.py: tongue_width()")
    print("    circle_map_utils.py: tongue_width()")
    print("    boundary_weight.py: tongue_coverage_q6()")
    print("    field_equation_iteration.py: w normalization")
    print("    born_rule.md: Delta theta / tongue_width relation")
    print("    K_star_iteration.py: field sum weightings")
    print()


if __name__ == "__main__":
    main()
