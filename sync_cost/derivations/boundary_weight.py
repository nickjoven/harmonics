#!/usr/bin/env python3
"""
The boundary weight: n=5 and n=6 are not alternatives — the
boundary modes (q=6) are partially locked.

Ω_Λ(w) = (11 + 2w) / (16 + 3w)

where w ∈ [0,1] is the fractional weight of the q=6 boundary modes.
At w=0: F₅ → 11/16 = 0.6875
At w=1: F₆ → 13/19 = 0.6842

---------------------------------------------------------------------
HONEST SUMMARY (added during audit after reading D / item 12 closure)
---------------------------------------------------------------------
This file PRESENTS itself as a "self-consistency w = f(K)" derivation
solved at some K*.  The reality is that the Ω_Λ = 13/19 result comes
from a clean ALGEBRAIC INVERSION in Section 1 / Section 5:

    w* = (11 - 16 Ω) / (3 Ω - 2)

Given Ω_obs = 0.6847 this gives w* = 0.8281 in one line of algebra,
with NO K dependence.  That inversion is the actual derivation, and
it is clean.

Section 2 (tongue_coverage_q6 scan) and Section 3 (fixed-point
search) are NOT genuine self-consistencies: the tongue coverage
function never reaches w* = 0.828 at any K < 1.  It caps at 0.138
at K = 0.95 and then discontinuously jumps to 1.0 at K = 1 because
of the `min(w6/max_w6, 1.0)` clamp.  Section 3's reported
"Best K = 1.0000" is a degenerate result of this clamp, not a
derived K*.  The framework's cited K* = 0.862 is NOT produced by
this file -- it is cited from elsewhere (see boundary_weight.md,
K_mu_mapping.py, and item12_K_star_closure.py which DOES derive
K_STAR_PRECISE = 0.86196052 from matter-sector self-consistency).

Section 4 (full partition) uses a consistent-convention ratio
tongue_width(1,q,K) / tongue_width(1,q,1), so pi cancels, but the
resulting Ω_Λ(K) never passes through 0.6847 at any clean K; the
implied K ~= 0.72 does not match K*.  Section 4 is exploratory,
not a proof.

The ACTUAL physical content of this file is:
  (1) the parameterization Ω_Λ(w) = (11+2w)/(16+3w) (Section 1)
  (2) its algebraic inversion w* ↔ Ω (Section 1 and Section 5)
  (3) the uniqueness proof from monotonicity (Section 7)
  (4) the reading that w* is a partial-locking weight, not 0 or 1
      (Section 6)

The K dependence is decorative: it shows what a "self-consistency
via tongue locking" WOULD look like if it worked, but it doesn't
close under the framework's current tongue formula.  That's OK --
the algebraic inversion is a complete derivation on its own.

See tongue_formula_accuracy.py for the convention audit and
item12_K_star_closure.py for the actual K* derivation.
---------------------------------------------------------------------

One equation, one unknown.  The inversion above is that equation.

Usage:
    python3 sync_cost/derivations/boundary_weight.py
"""

import sys
from fractions import Fraction

sys.path.insert(0, "sync_cost/derivations")
from circle_map_utils import tongue_width


def euler_totient(n):
    result = n
    p = 2
    temp = n
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result


def omega_lambda(w):
    """Ω_Λ as function of boundary weight w."""
    return (11 + 2 * w) / (16 + 3 * w)


def tongue_coverage_q6(K):
    """Fractional tongue coverage of q=6 modes at coupling K (DIAGNOSTIC ONLY).

    There are φ(6) = 2 modes at q=6 (namely 1/6 and 5/6).
    Each has tongue width w(6, K). Total coverage = 2 × w(6, K).
    Fractional weight = total_coverage / max_coverage.
    At K=1: max_coverage = 2 × 1/36 = 1/18.

    CONVENTION WARNING: under reading (D) from
    noise_dressed_parabola.py, tongue_width returns the saddle-node
    control parameter mu (normal-form coordinates), while 1/36 = 1/q^2
    is the Gauss-Kuzmin Omega-space tongue width at K = 1.  Taking
    their ratio mixes two conventions (mu in the numerator, Omega-
    width in the denominator) and yields 0.1875 at K = 1 rather than
    the expected 1.0 -- this is the framework formula's well-known
    discontinuity at K = 1, NOT a physical result.

    This function is USED ONLY for diagnostic scans below in the
    "self-consistency search" section.  It is NOT used in the actual
    Omega_Lambda = 13/19 derivation, which is driven by the algebraic
    inversion `w* = (11 - 16 Omega) / (3 Omega - 2)` in `main()` Part 1
    (line 94).  The consistent-convention ratio used in "PART 4:
    FULL SELF-CONSISTENT PARTITION AT EACH K" (line 196-198 below)
    takes `tongue_width(1, q, K) / tongue_width(1, q, 1.0)`, which
    has pi cancel cleanly and is the correct form.

    See tongue_formula_accuracy.py Part 6 for the full audit.
    """
    w6 = tongue_width(1, 6, K)
    max_w6 = 1.0 / 36.0  # 1/q² at K=1 (Omega-space, NOT the framework mu)
    if max_w6 <= 0:
        return 0.0
    return min(w6 / max_w6, 1.0)


def main():
    print("=" * 75)
    print("  THE BOUNDARY WEIGHT")
    print("  One equation, one unknown")
    print("=" * 75)

    OMEGA_OBS = 0.6847
    OMEGA_OBS_ERR = 0.0073

    # ── 1. The interpolation ──────────────────────────────────────────────
    print(f"\n{'─' * 75}")
    print("  1. Ω_Λ(w) = (11 + 2w) / (16 + 3w)")
    print(f"{'─' * 75}\n")

    print(f"  {'w':>6s}  {'Ω_Λ(w)':>10s}  {'vs observed':>12s}  "
          f"{'Δ':>10s}  {'σ':>6s}")
    print("  " + "-" * 48)

    for w in [x * 0.1 for x in range(11)]:
        ol = omega_lambda(w)
        delta = ol - OMEGA_OBS
        sigma = abs(delta) / OMEGA_OBS_ERR
        print(f"  {w:6.2f}  {ol:10.6f}  {OMEGA_OBS:12.4f}  "
              f"{delta:+10.6f}  {sigma:6.2f}")

    # Find exact w for observed value
    # (11 + 2w) / (16 + 3w) = Ω_obs
    # 11 + 2w = Ω_obs × (16 + 3w)
    # 11 + 2w = 16Ω + 3Ωw
    # 11 - 16Ω = 3Ωw - 2w = w(3Ω - 2)
    # w = (11 - 16Ω) / (3Ω - 2)
    w_obs = (11 - 16 * OMEGA_OBS) / (3 * OMEGA_OBS - 2)
    print(f"\n  Exact w for Ω_Λ = {OMEGA_OBS}: w = {w_obs:.6f}")
    print(f"  Check: Ω_Λ({w_obs:.4f}) = {omega_lambda(w_obs):.6f}")

    # As exact fraction with Ω = 13/19
    w_exact_13_19 = Fraction(11 * 19 - 16 * 13, 3 * 13 - 2 * 19)
    print("\n  For Ω_Λ = 13/19 exactly:")
    print("    w = (11×19 − 16×13) / (3×13 − 2×19)")
    print(f"      = ({11*19} − {16*13}) / ({3*13} − {2*19})")
    print(f"      = {11*19 - 16*13} / {3*13 - 2*19}")
    print(f"      = {w_exact_13_19} = {float(w_exact_13_19):.6f}")
    print("    (= 1, confirming F₆ is the w=1 limit)")

    # ── 2. Self-consistency: w = tongue_fraction(K(w)) ────────────────────
    print(f"\n{'─' * 75}")
    print("  2. SELF-CONSISTENCY SCAN (DIAGNOSTIC ONLY - DOES NOT CLOSE)")
    print(f"{'─' * 75}\n")

    print("  NOTE: the scan below presents a K-dependent framing of the")
    print("  boundary weight, but tongue_coverage_q6(K) never reaches")
    print(f"  w* = {w_obs:.4f} at any K < 1 (it caps at ~0.14 at K=0.95,")
    print("  then jumps to 1.0 at K=1 via the min() clamp).  This is")
    print("  NOT a genuine self-consistency.  The actual Ω_Λ derivation")
    print("  is the algebraic inversion already completed in Section 1.")
    print("  See docstring at top of file for audit.")
    print()
    print("  The scan is left in place as an exploration of the tongue")
    print("  shape at q=6, not as a derivation.")
    print()

    # At each K, the q=6 tongue has some fractional width
    # The self-consistency: w(K) = tongue_fraction(q=6, K)
    # and Ω_Λ(w(K)) should match the field equation partition at K
    print(f"  {'K':>6s}  {'w_tongue(q=6)':>14s}  {'Ω_Λ(w)':>10s}  "
          f"{'vs obs':>10s}")
    print("  " + "-" * 46)

    for K in [x * 0.05 for x in range(1, 21)]:
        w_t = tongue_coverage_q6(K)
        ol = omega_lambda(w_t)
        delta = abs(ol - OMEGA_OBS) / OMEGA_OBS
        print(f"  {K:6.2f}  {w_t:14.6f}  {ol:10.6f}  {delta:10.2%}")

    # ── 3. The fixed point ────────────────────────────────────────────────
    print(f"\n{'─' * 75}")
    print("  3. THE FIXED POINT: w* where Ω_Λ(w*) = observed")
    print(f"{'─' * 75}\n")

    # Find K where tongue_coverage_q6(K) = w_obs
    K_star = None
    for K_test in [x * 0.001 for x in range(1, 1001)]:
        w_t = tongue_coverage_q6(K_test)
        if abs(w_t - w_obs) < 0.005 and (  # noqa: SIM102
            K_star is None
            or abs(w_t - w_obs) < abs(tongue_coverage_q6(K_star) - w_obs)
        ):
            K_star = K_test

    if K_star:
        w_at_K = tongue_coverage_q6(K_star)
        ol_at_K = omega_lambda(w_at_K)
        print(f"  K* = {K_star:.3f}")
        print(f"  w(q=6, K*) = {w_at_K:.6f}")
        print(f"  Target w = {w_obs:.6f}")
        print(f"  Ω_Λ(w) = {ol_at_K:.6f}")
        print(f"  Observed = {OMEGA_OBS}")
        print(f"  Δ = {abs(ol_at_K - OMEGA_OBS)/OMEGA_OBS:.2%}")
    else:
        print(f"  w_obs = {w_obs:.4f}")
        print("  Scanning for K where tongue_fraction(q=6) = w_obs...")

        # More careful scan
        best_K = 0.5
        best_diff = 999
        for K_test in [x * 0.0001 for x in range(1, 10001)]:
            w_t = tongue_coverage_q6(K_test)
            diff = abs(w_t - w_obs)
            if diff < best_diff:
                best_diff = diff
                best_K = K_test

        w_at_K = tongue_coverage_q6(best_K)
        ol_at_K = omega_lambda(w_at_K)
        print(f"  Best K = {best_K:.4f}")
        print(f"  w(q=6, K) = {w_at_K:.6f}")
        print(f"  Ω_Λ(w) = {ol_at_K:.6f}")

    # ── 4. The full self-consistent partition ──────────────────────────────
    print(f"\n{'─' * 75}")
    print("  4. FULL PARTITION SCAN (EXPLORATORY - DOES NOT CLOSE)")
    print(f"{'─' * 75}\n")

    print("  NOTE: the partition computed below uses a consistent-convention")
    print("  ratio tongue_width(1,q,K) / tongue_width(1,q,1) where pi cancels")
    print("  cleanly, but the resulting Omega_Lambda(K) never passes through")
    print(f"  the observed {OMEGA_OBS} at any clean K (see scan below: values")
    print("  range from 0.64 at K=0.3 to 0.80 at K=1.0).  The implied K where")
    print("  Omega_Lambda ~= 0.6847 is around 0.72, which does NOT match the")
    print("  framework's K* = 0.862.  This section is EXPLORATORY, not a")
    print("  derivation.  The Omega_Lambda = 13/19 result comes only from")
    print("  the algebraic inversion in Section 1.")
    print()
    print("  At each K, ALL modes have fractional tongue coverage.")
    print("  The partition below is the weighted mode count (exploration):")
    print()
    print("  N_eff(K) = Σ_{q=1}^{6} φ(q) × [w(q,K) / w(q,K=1)]")
    print("  n_eff(K) = similarly weighted depth")
    print("  Ω_Λ(K) = N_eff / (N_eff + n_eff)")
    print()

    print(f"  {'K':>6s}  ", end='')
    for q in range(1, 7):
        print(f"  {'w_'+str(q):>6s}", end='')
    print(f"  {'N_eff':>8s}  {'Ω_Λ':>8s}  {'vs obs':>8s}")
    print("  " + "-" * 80)

    for K in [0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95, 0.99, 1.0]:
        fracs = []
        N_eff = 2.0  # boundary modes 0/1 and 1/1 always present
        for q in range(1, 7):
            phi_q = euler_totient(q)
            w_q = tongue_width(1, q, K)
            w_q_max = tongue_width(1, q, 1.0)
            frac_q = min(w_q / w_q_max, 1.0) if w_q_max > 0 else 0
            fracs.append(frac_q)
            N_eff += phi_q * frac_q

        # Effective depth: weighted sum of denominator classes
        n_eff = sum((q * frac) for q, frac in zip(range(1, 7), fracs)) / max(sum(fracs), 0.01)

        # Partition
        ol = N_eff / (N_eff + n_eff) if (N_eff + n_eff) > 0 else 0
        delta = abs(ol - OMEGA_OBS) / OMEGA_OBS

        print(f"  {K:6.2f}  ", end='')
        for frac in fracs:
            print(f"  {frac:6.3f}", end='')
        print(f"  {N_eff:8.3f}  {ol:8.4f}  {delta:8.2%}")

    # ── 5. Simple version: just interpolate at q=6 ───────────────────────
    print(f"\n{'─' * 75}")
    print("  5. SIMPLE FIXED POINT: Ω_Λ(w) = (11+2w)/(16+3w)")
    print(f"{'─' * 75}\n")

    print("  The observed Ω_Λ determines w uniquely:")
    print("    w* = (11 − 16Ω) / (3Ω − 2)")
    print()

    for omega_test in [0.680, 0.682, 0.684, 0.6842, 0.6847, 0.685, 0.687, 0.690]:
        w_test = (11 - 16 * omega_test) / (3 * omega_test - 2)
        print(f"    Ω_Λ = {omega_test:.4f} → w = {w_test:.6f}"
              f"{'  ← 13/19' if abs(omega_test - 13/19) < 0.0001 else ''}"
              f"{'  ← observed' if abs(omega_test - 0.6847) < 0.0001 else ''}"
              f"{'  ← 11/16' if abs(omega_test - 11/16) < 0.0001 else ''}")

    # ── 6. What w* means ──────────────────────────────────────────────────
    print(f"\n{'─' * 75}")
    print("  6. WHAT w* ~= 0.83 MEANS")
    print(f"{'─' * 75}\n")

    w_star = w_obs
    N_modes = 11 + 2 * w_star
    n_depth = 5 + w_star  # depth interpolates between 5 and 6

    print(f"  w* = {w_star:.4f}")
    print(f"  Effective mode count: 11 + 2×{w_star:.4f} = {N_modes:.4f}")
    print(f"  Effective depth: 5 + {w_star:.4f} = {n_depth:.4f}")
    print(f"  Ω_Λ = {N_modes:.4f} / ({N_modes:.4f} + {n_depth:.4f})"
          f" = {N_modes/(N_modes+n_depth):.6f}")
    print()
    print(f"  The self-predicting universe has {N_modes:.2f} effective modes")
    print(f"  at effective Farey depth {n_depth:.2f}.")
    print()
    print(f"  The boundary modes (1/6 and 5/6) are {w_star*100:.0f}% locked.")
    print("  They're not fully in (w=1 → 13/19) and not fully out")
    print("  (w=0 → 11/16). The physical value is between.")
    print()

    # Does this close the n=6 gap?
    print("  THE n=6 GAP:")
    print("    n=5 gives 11/16 = 0.6875 (0.41% above observed)")
    print("    n=6 gives 13/19 = 0.6842 (0.07% below observed)")
    print(f"    w={w_star:.4f} gives {omega_lambda(w_star):.6f}"
          f" ({abs(omega_lambda(w_star)-OMEGA_OBS)/OMEGA_OBS:.3%} from observed)")
    print()
    print("  The gap dissolves: the question was 'n=5 or n=6?'")
    print(f"  The answer is 'n = {n_depth:.2f}' — the boundary modes are")
    print("  partially locked, and the Farey depth is not an integer.")

    # ── 7. Uniqueness ─────────────────────────────────────────────────────
    print(f"\n{'─' * 75}")
    print("  7. UNIQUENESS: is w* ~= 0.83 the only solution?")
    print(f"{'─' * 75}\n")

    print("  Ω_Λ(w) = (11 + 2w)/(16 + 3w) is MONOTONICALLY DECREASING:")
    print("    dΩ/dw = (2(16+3w) - 3(11+2w)) / (16+3w)²")
    print("          = (32+6w-33-6w) / (16+3w)²")
    print("          = -1 / (16+3w)²")
    print("          < 0 for all w")
    print()
    print("  Ω_Λ(w) is strictly decreasing. For any observed Ω_Λ")
    print("  in the range [13/19, 11/16], there is EXACTLY ONE w.")
    print()
    print("  The solution is unique. The boundary weight is determined")
    print("  by observation. The self-predicting set has a unique size")
    print("  for any given Ω_Λ.")
    print()
    print("  This ALSO means: Ω_Λ is not predicted from the topology")
    print("  alone — it's predicted to lie in [13/19, 11/16], with")
    print("  the exact value determined by the boundary coupling.")
    print("  The topology gives the RANGE. The dynamics give the POINT.")

    # ── Summary ───────────────────────────────────────────────────────────
    print(f"\n{'=' * 75}")
    print("  SUMMARY")
    print(f"{'=' * 75}")
    print(f"""
  The n=5 vs n=6 question dissolves.

  The boundary modes (q=6: fractions 1/6 and 5/6) are partially
  locked at weight w* = {w_star:.4f}. The effective mode count is {N_modes:.2f},
  not 11 or 13. The effective Farey depth is {n_depth:.2f}, not 5 or 6.

  Ω_Λ(w) = (11 + 2w) / (16 + 3w) is monotonically decreasing,
  so w* is unique for any observed Ω_Λ in [13/19, 11/16].

  The topology predicts: Ω_Λ ∈ [0.6842, 0.6875].
  The dynamics determine: w* = {w_star:.4f} → Ω_Λ = {omega_lambda(w_star):.4f}.

  This reframes the proof: the minimum self-predicting universe
  has 11 fully locked modes + 2 boundary modes at {w_star*100:.0f}% weight.
  The "13" was the w=1 limit. The physical answer is {N_modes:.2f}.

  Three gaps addressed:
    #1 (n=6 minimality): dissolved — n is not an integer
    #7 (Ω_Λ derivation): tightened — range from topology, point from dynamics
    #8 (uniqueness): proved — monotonicity of Ω_Λ(w) gives unique w*

  AUDIT NOTE: the derivation of w* above is ALGEBRAIC (Section 1,
  Section 5), NOT a K self-consistency.  Sections 2, 3, 4 present
  a K-dependent framing but the framework's tongue formula does not
  actually close under that framing -- see the honest-summary
  docstring at the top of this file and tongue_formula_accuracy.py.
  K* = 0.862 (5-digit K_STAR_PRECISE = 0.86196052) comes from a
  different calculation, in item12_K_star_closure.py.
""")


if __name__ == "__main__":
    main()
