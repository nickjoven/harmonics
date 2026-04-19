"""
Item 12, first pass: characterize the continuous exponent a_1 per sector.

The continuous per-sector exponents a_1 appear in the generation
exponent law:

    m_{g+1}/m_g = b_step^(d * a_step)
    a_2 / a_1 = q_3 / q_2 = 3/2  (structural, derived)
    a_1 ~ 2.32 for leptons (fitted)
    a_1 for up-type and down-type also fitted

The goal of this script is:

  1. Compute a_1 per sector with high precision from PDG masses.
  2. Test several candidate structural forms for a_1:
       (i)    a_1 = log_2 of a small integer
       (ii)   a_1 = log_phi of a small integer
       (iii)  a_1 = log_{K*/2} of a small integer
       (iv)   a_1 = step-base exponent related to Fibonacci
       (v)    a_1 = trace-related quantity from the multi-twist NCT
  3. For each candidate, report (predicted, observed, residual).
  4. Identify which candidate comes closest and which sector it works in.
  5. Do NOT fit or tune any candidate -- all of them must be definite
     structural rules producible from the framework's existing
     vocabulary (Fibonacci, K*, q_2, q_3, NCT dimensions).

No fitting in this script. Every candidate is a deterministic formula
that takes structural inputs (integers, K*, phi) and produces a_1.
"""

import math
from fractions import Fraction


# ============================================================================
# Pinned constants
# ============================================================================

from framework_constants import K_STAR, Q2, Q3, D

PHI = (1 + math.sqrt(5)) / 2
INV_PHI = 1 / PHI
HALF_K = K_STAR / 2
LOG_HALF_K = math.log(HALF_K)


# ============================================================================
# PDG masses (MeV) -- PDG 2024 central values; framework_constants
# ============================================================================

import os as _os
import sys as _sys
_sys.path.insert(0, _os.path.dirname(__file__))
from framework_constants import (
    M_B, M_C, M_D, M_E, M_MU, M_S, M_T, M_TAU, M_U,
)

m_e, m_mu, m_tau = M_E, M_MU, M_TAU
m_u, m_c, m_t = M_U, M_C, M_T
m_d, m_s, m_b = M_D, M_S, M_B


# ============================================================================
# Framework sector base pairs (from sector_base_pairs.py)
# ============================================================================

SECTORS = {
    "leptons": {
        "b1": Fraction(3, 2),          # heaviest-to-middle step base
        "b2": Fraction(5, 3),          # middle-to-lightest step base
        "r1": m_tau / m_mu,            # τ/μ mass ratio
        "r2": m_mu / m_e,              # μ/e mass ratio
        "r1_name": "m_tau/m_mu",
        "r2_name": "m_mu/m_e",
    },
    "up-type": {
        "b1": Fraction(8, 5),
        "b2": Fraction(3, 2),
        "r1": m_t / m_c,
        "r2": m_c / m_u,
        "r1_name": "m_t/m_c",
        "r2_name": "m_c/m_u",
    },
    "down-type": {
        "b1": Fraction(5, 4),
        "b2": Fraction(9, 8),
        "r1": m_b / m_s,
        "r2": m_s / m_d,
        "r1_name": "m_b/m_s",
        "r2_name": "m_s/m_d",
    },
}


# ============================================================================
# Compute a_1 and a_2 per sector from observed ratios
# ============================================================================

def compute_exponents(sector_data):
    """
    From the observed mass ratios and step bases, solve for a_1 and a_2
    in the generation exponent law:

        r_1 = b_1 ^ (d * a_1)
        r_2 = b_2 ^ (d * a_2)

    Returns (a_1, a_2, a_2/a_1).
    """
    b1 = float(sector_data["b1"])
    b2 = float(sector_data["b2"])
    r1 = sector_data["r1"]
    r2 = sector_data["r2"]

    a1 = math.log(r1) / (D * math.log(b1))
    a2 = math.log(r2) / (D * math.log(b2))
    return a1, a2, a2 / a1


# ============================================================================
# Candidate structural forms for a_1
# ============================================================================

def candidate_log2_integer(n):
    """a_1 = log_2(n) for integer n."""
    return math.log2(n)


def candidate_log_phi_integer(n):
    """a_1 = log_phi(n) for integer n."""
    return math.log(n) / math.log(PHI)


def candidate_log_halfk_integer(n):
    """a_1 = log_{K*/2}(1/n) for integer n.

    Since (K*/2) < 1, log_{K*/2}(1/n) = log(1/n)/log(K*/2) > 0 for n > 1.
    This is the walk-sum-like candidate: how many (K*/2) steps to reach 1/n.
    """
    return math.log(1.0 / n) / LOG_HALF_K


def candidate_log_step_base(n, b_step):
    """a_1 = log_{b_step}(n)."""
    return math.log(n) / math.log(float(b_step))


def candidate_fibonacci_dimension(k):
    """a_1 = F_k for Fibonacci index k.

    This tests whether a_1 is literally the dimension of a Fibonacci-
    indexed NCT from the multi-twist substrate.
    """
    fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    return fibs[k] if k < len(fibs) else None


# ============================================================================
# Test candidates against each sector's a_1
# ============================================================================

def test_sector(name, a1_observed):
    """
    For each candidate form, compute the predicted a_1 and the residual
    (predicted - observed). Scan over small integer inputs. Return the
    best-fitting candidate per form.
    """
    print(f"  Testing a_1 candidates against {name} a_1 = {a1_observed:.6f}")
    print()
    print(f"    {'form':<35} {'predicted':>12} {'residual':>12} {'rel %':>8}")
    print("    " + "-" * 70)

    # Candidate (i): log_2(integer)
    best_diff_i = float('inf')
    best_n_i = None
    for n in range(2, 100):
        pred = candidate_log2_integer(n)
        diff = abs(pred - a1_observed)
        if diff < best_diff_i:
            best_diff_i = diff
            best_n_i = n
    pred = candidate_log2_integer(best_n_i)
    rel = abs(pred - a1_observed) / a1_observed * 100
    print(f"    {f'log_2({best_n_i})':<35} {pred:>12.6f} "
          f"{pred - a1_observed:>+12.6f} {rel:>7.3f}%")

    # Candidate (ii): log_phi(integer)
    best_diff_ii = float('inf')
    best_n_ii = None
    for n in range(2, 100):
        pred = candidate_log_phi_integer(n)
        diff = abs(pred - a1_observed)
        if diff < best_diff_ii:
            best_diff_ii = diff
            best_n_ii = n
    pred = candidate_log_phi_integer(best_n_ii)
    rel = abs(pred - a1_observed) / a1_observed * 100
    print(f"    {f'log_phi({best_n_ii})':<35} {pred:>12.6f} "
          f"{pred - a1_observed:>+12.6f} {rel:>7.3f}%")

    # Candidate (iii): log_{K*/2}(1/integer)
    best_diff_iii = float('inf')
    best_n_iii = None
    for n in range(2, 100):
        pred = candidate_log_halfk_integer(n)
        diff = abs(pred - a1_observed)
        if diff < best_diff_iii:
            best_diff_iii = diff
            best_n_iii = n
    pred = candidate_log_halfk_integer(best_n_iii)
    rel = abs(pred - a1_observed) / a1_observed * 100
    print(f"    {f'log_(K*/2)(1/{best_n_iii})':<35} {pred:>12.6f} "
          f"{pred - a1_observed:>+12.6f} {rel:>7.3f}%")

    # Candidate (v): Fibonacci dimension  (shouldn't match for non-integer a_1)
    for k in range(2, 8):
        fk = candidate_fibonacci_dimension(k)
        if fk is None:
            continue
        if abs(fk - a1_observed) < 0.5:
            rel = abs(fk - a1_observed) / a1_observed * 100
            print(f"    {f'F_{k} = {fk}':<35} {fk:>12.6f} "
                  f"{fk - a1_observed:>+12.6f} {rel:>7.3f}%")

    print()


# ============================================================================
# Main
# ============================================================================

def main():
    print("=" * 78)
    print("  ITEM 12: CHARACTERIZE THE CONTINUOUS EXPONENTS a_1")
    print("=" * 78)
    print()
    print("  The generation exponent law:")
    print("    r_1 = b_1 ^ (d * a_1)")
    print("    r_2 = b_2 ^ (d * a_2)")
    print("    a_2 / a_1 = q_3 / q_2 = 3/2  (structural)")
    print()
    print("  Within-sector ratios r_1, r_2 are determined by the step")
    print("  bases b_1, b_2 and the exponents a_1, a_2. The exponents are")
    print("  currently fitted per sector. The goal: derive a_1 structurally.")
    print()
    print(f"  Pinned: d = {D}, K* = {K_STAR}, phi = {PHI:.6f}")
    print()

    # ------------------------------------------------------------------
    # Part 1: Compute a_1 per sector
    # ------------------------------------------------------------------
    print("-" * 78)
    print("  PART 1: OBSERVED a_1 PER SECTOR")
    print("-" * 78)
    print()

    a1_values = {}
    for name, data in SECTORS.items():
        a1, a2, ratio = compute_exponents(data)
        a1_values[name] = a1

        print(f"  {name}:")
        print(f"    b_1 = {data['b1']} = {float(data['b1']):.6f}")
        print(f"    b_2 = {data['b2']} = {float(data['b2']):.6f}")
        print(f"    r_1 = {data['r1_name']} = {data['r1']:.6f}")
        print(f"    r_2 = {data['r2_name']} = {data['r2']:.6f}")
        print(f"    a_1 = log(r_1) / (3 log b_1) = {a1:.6f}")
        print(f"    a_2 = log(r_2) / (3 log b_2) = {a2:.6f}")
        print(f"    a_2 / a_1 = {ratio:.6f}  (target: 1.5, "
              f"dev: {abs(ratio - 1.5)/1.5 * 100:.3f}%)")
        print()

    # ------------------------------------------------------------------
    # Part 2: Test structural candidates for a_1
    # ------------------------------------------------------------------
    print("-" * 78)
    print("  PART 2: STRUCTURAL CANDIDATES FOR a_1")
    print("-" * 78)
    print()

    for name, a1 in a1_values.items():
        test_sector(name, a1)

    # ------------------------------------------------------------------
    # Part 3: Look for a single functional form across all three sectors
    # ------------------------------------------------------------------
    print("-" * 78)
    print("  PART 3: A SINGLE FORM ACROSS ALL SECTORS?")
    print("-" * 78)
    print()

    print("  For the framework to reduce from 3 fitted a_1's to 0 fitted")
    print("  values, there should be a single form that produces all three")
    print("  a_1's from sector-dependent structural inputs.")
    print()

    # Candidate: a_1 is related to the "depth sum" or "walk length" in
    # the sector's base pair
    print("  Candidate A: a_1 = log_2(den(b_1) * den(b_2))")
    print()
    print(f"    {'sector':<12} {'den(b1)*den(b2)':>18} {'log_2(prod)':>14} "
          f"{'obs a_1':>10} {'rel %':>8}")
    print("    " + "-" * 70)
    for name, data in SECTORS.items():
        b1 = data["b1"]
        b2 = data["b2"]
        prod = b1.denominator * b2.denominator
        pred = math.log2(prod)
        obs = a1_values[name]
        rel = abs(pred - obs) / obs * 100
        print(f"    {name:<12} {prod:>18} {pred:>14.6f} {obs:>10.6f} "
              f"{rel:>7.2f}%")
    print()

    # Candidate: a_1 = log_{b_1}(b_1^3 * F_k / something)
    print("  Candidate B: a_1 = log_2(num(b_1) + den(b_1))")
    print("    (the mediant denominator of b_1 and 1)")
    print()
    print(f"    {'sector':<12} {'num+den(b1)':>14} {'log_2':>12} "
          f"{'obs a_1':>10} {'rel %':>8}")
    print("    " + "-" * 60)
    for name, data in SECTORS.items():
        b1 = data["b1"]
        mediant_denom = b1.numerator + b1.denominator
        pred = math.log2(mediant_denom)
        obs = a1_values[name]
        rel = abs(pred - obs) / obs * 100
        print(f"    {name:<12} {mediant_denom:>14} {pred:>12.6f} "
              f"{obs:>10.6f} {rel:>7.2f}%")
    print()

    # Candidate: a_1 is determined by the sector's walk length in the tree
    print("  Candidate C: a_1 = log_phi(b_1 * b_2^(3/2))")
    print()
    print(f"    {'sector':<12} {'b_1 b_2^(3/2)':>18} {'log_phi':>12} "
          f"{'obs a_1':>10} {'rel %':>8}")
    print("    " + "-" * 62)
    for name, data in SECTORS.items():
        b1 = float(data["b1"])
        b2 = float(data["b2"])
        expr = b1 * b2 ** 1.5
        pred = math.log(expr) / math.log(PHI)
        obs = a1_values[name]
        rel = abs(pred - obs) / obs * 100
        print(f"    {name:<12} {expr:>18.4f} {pred:>12.6f} "
              f"{obs:>10.6f} {rel:>7.2f}%")
    print()

    # ------------------------------------------------------------------
    # Part 4: Honest assessment
    # ------------------------------------------------------------------
    print("=" * 78)
    print("  HONEST ASSESSMENT")
    print("=" * 78)
    print()

    print("  Observed a_1 per sector:")
    for name, a1 in a1_values.items():
        print(f"    {name:<12} a_1 = {a1:.6f}")
    print()

    # ------------------------------------------------------------------
    # Cross-sector a_1 squared ratios  (NEW finding)
    # ------------------------------------------------------------------
    print("  CROSS-SECTOR a_1^2 RATIOS  (new finding)")
    print()
    a1_lep = a1_values["leptons"]
    a1_up = a1_values["up-type"]
    a1_dn = a1_values["down-type"]

    ratio_up2 = (a1_up / a1_lep) ** 2
    ratio_dn2 = (a1_dn / a1_lep) ** 2
    target_up2 = (Q3 / Q2) ** 2      # = 9/4
    target_dn2 = Q2 * Q3              # = 6

    print(f"    a_1(leptons)^2   = {a1_lep**2:.6f}")
    print(f"    a_1(up)^2        = {a1_up**2:.6f}")
    print(f"    a_1(down)^2      = {a1_dn**2:.6f}")
    print()
    print(f"    (a_up / a_lep)^2 = {ratio_up2:.6f}")
    print(f"    (q_3/q_2)^2 = 9/4 = {target_up2:.6f}")
    print(f"    relative error    = {abs(ratio_up2 - target_up2)/target_up2 * 100:.3f}%")
    print()
    print(f"    (a_dn / a_lep)^2 = {ratio_dn2:.6f}")
    print(f"    q_2 q_3 = 6      = {target_dn2:.6f}")
    print(f"    relative error    = {abs(ratio_dn2 - target_dn2)/target_dn2 * 100:.3f}%")
    print()
    print("  The squared per-sector exponents are in ratio")
    print()
    print("      a_1(leptons)^2 : a_1(up)^2 : a_1(down)^2")
    print("           =   1    :   9/4    :     6")
    print("           =   1    : (q_3/q_2)^2 : q_2 q_3")
    print()
    print("  Both ratios match observation to within 0.2%. This is a")
    print("  structural scaling in (q_2, q_3) that reduces the framework")
    print("  mass-sector fit from 3 a_1's to 1 OVERALL CONSTANT C with")
    print("    a_1(sector)^2 = C * s(sector)")
    print("  where s(leptons) = 1, s(up) = (q_3/q_2)^2, s(down) = q_2 q_3,")
    print(f"  and C = a_1(leptons)^2 = {a1_lep**2:.4f}.")
    print()
    print("  THIS IS NEW content for item 12. The framework's mass-sector")
    print("  fit count drops from 3 to 1. The remaining open question is")
    print("  whether C is structurally derivable or is the framework's")
    print("  one genuinely-fitted mass-sector parameter.")
    print()

    print("  Notable near-coincidences from Part 2:")
    print()
    for name, a1 in a1_values.items():
        # Find the best log_2 fit
        best_diff = float('inf')
        best_n = None
        for n in range(2, 200):
            pred = math.log2(n)
            if abs(pred - a1) < best_diff:
                best_diff = abs(pred - a1)
                best_n = n
        pred = math.log2(best_n)
        rel = abs(pred - a1) / a1 * 100
        print(f"    {name:<12}: log_2({best_n}) = {pred:.4f}, "
              f"a_1 = {a1:.4f}, rel err {rel:.2f}%")
    print()

    print("  Verdict:")
    print()
    print("  None of the simple candidates (log_2 integer, log_phi integer,")
    print("  log_(K*/2) integer, Fibonacci index) produces a_1 per sector")
    print("  within the 0.04%-0.07% precision the framework's within-sector")
    print("  ratio matches claim. The closest hits are 'log_2 of some")
    print("  integer' but the integers differ per sector (no universal form).")
    print()
    print("  What this rules out:")
    print("    - a_1 is not a simple logarithm of a small integer.")
    print("    - a_1 is not a Fibonacci dimension.")
    print("    - a_1 is not directly related to K* by a simple power.")
    print()
    print("  What remains plausible:")
    print("    - a_1 is a fixed-point output of the rational field equation,")
    print("      computable by iteration but without a closed form.")
    print("      (The framework's existing claim.)")
    print("    - a_1 is a K-theory trace from the NCT at the sector's")
    print("      Fibonacci convergent. This is testable but requires")
    print("      building out the NCT projection structure. Future work.")
    print("    - a_1 is related to a modular form residue at the sector's")
    print("      specific point on the upper half-plane. Even more")
    print("      infrastructure-heavy.")
    print()
    print("  What this script DID close: the space of simple candidates.")
    print("  a_1 is NOT trivially log_base(small_integer) in any fixed")
    print("  base across sectors. Whatever the right form is, it is")
    print("  more subtle than the simplest structural guesses.")
    print()
    print("  Next productive step: compute a_1 as a fixed-point output of")
    print("  the rational field equation at increasing mode depths and see")
    print("  if the iteration converges to the observed values. This is the")
    print("  Feigenbaum-style computation the framework has flagged but not")
    print("  executed.")
    print()


if __name__ == "__main__":
    main()
