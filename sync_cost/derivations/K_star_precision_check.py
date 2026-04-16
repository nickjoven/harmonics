"""
K_star_precision_check.py

Tightening move (A) on the K_STAR ~ 2^(-3/14) chain.  Recompute
K_STAR_lep at full PDG precision and test the closed-form relation
K_STAR^14 = q_2^(-q_3) = 1/8.

Formula: K_STAR_lep = sqrt(N_lep) / a_1(lep) where
    a_1(lep) = log(m_tau/m_mu) / (d * log(b_1))
    N_lep = 4, d = 3, b_1 = 3/2

From item12_K_star_closure.py, the framework canonical value is
K_STAR_lep = 0.86196057 +/- 2.06e-05, tau-mass-limited.

KEY RESULT:

    K_STAR_lep      = 0.8619605739 +/- 2.06e-05
    K_STAR_lep^14   = 0.12497514 +/- 4.19e-05
    1/8             = 0.12500000
    gap             = -2.49e-05
    in K^14 sigma   = 0.594

The relation K_STAR^14 = 1/8 holds at 0.594 sigma.  Sub-1 sigma
but not decisively confirmed.  Equivalent to saying: K_STAR_lep is
1.22e-5 below the exact value K_exact = 8^(-1/14) = 0.86197282.

PRECISION BUDGET:

  The uncertainty on K_STAR_lep is DOMINATED by sigma(m_tau) =
  0.12 MeV.  Relative: sigma(m_tau)/m_tau = 6.75e-5 = 68 ppm.
  This propagates as

      sigma(K_STAR_lep) / K_STAR_lep = sigma(m_tau) / (m_tau * d * log(b_1))
                                     = 6.75e-5 / 1.2164
                                     = 5.55e-5 relative
                                     = 48 ppm relative to K

  To resolve the 1/8 relation at < 0.1 sigma, we need
  sigma(K)/K < 5 ppm, which requires sigma(m_tau)/m_tau < 6 ppm,
  i.e., sigma(m_tau) < 0.012 MeV.  That's 10x tighter than
  current PDG.

INDIVIDUAL EXPERIMENTS:

  The PDG average m_tau = 1776.86 is built from several
  measurements with different central values.  Testing the 1/8
  relation against each:

    BESIII 2014: 1776.91 +/- 0.12 +/- 0.10
    BaBar 2009:  1776.68 +/- 0.12 +/- 0.41
    Belle 2007:  1776.61 +/- 0.13 +/- 0.35
    KEDR 2007:   1776.80 +/- 0.23

  Different experiments give slightly different K_STAR values, and
  the sigma on the 1/8 gap varies accordingly.  None definitively
  confirms or rules out K_STAR^14 = 1/8 at current precision.

VERDICT:

  The K_STAR^14 = 1/8 closed form is CONSISTENT with PDG 2024 at
  0.594 sigma.  It is NEITHER confirmed nor ruled out at current
  precision.  Resolution requires ~10x tighter tau mass measurement,
  which is plausible at Belle II and BESIII upgrades over the
  coming years.

  For now, the relation stands as a candidate closed form that is
  within 1 sigma of the canonical K_STAR but cannot be established
  as exact without better data.

  Either:
    (i) The relation is EXACT and K_STAR is exactly 2^(-3/14).
        PDG tau mass is ~0.02 MeV too low on average.
    (ii) The relation is NOT exact, and the 0.594 sigma gap is
         a numerical coincidence at the precision floor.

  We cannot distinguish (i) from (ii) with current data.
"""

from __future__ import annotations

import math

from framework_constants import K_STAR, Q2, Q3, M_MU, M_TAU


# PDG 2024 (matches framework_constants.py)
M_MU_VALUE = 105.6583755
M_MU_SIGMA = 0.0000023
M_TAU_VALUE = 1776.86
M_TAU_SIGMA = 0.12

B1_LEP = 3.0 / 2.0
D_DIM = 3
N_LEP = Q2 ** 2


def header(text: str) -> None:
    print()
    print("-" * 78)
    print(f"  {text}")
    print("-" * 78)
    print()


def k_star_from_tau(m_tau: float, s_tau: float) -> tuple[float, float]:
    """Compute K_STAR_lep and its uncertainty from m_tau and m_mu."""
    log_b1 = math.log(B1_LEP)
    log_ratio = math.log(m_tau / M_MU_VALUE)
    a1 = log_ratio / (D_DIM * log_b1)
    K = math.sqrt(N_LEP) / a1

    # Error propagation (m_mu uncertainty negligible)
    sigma_log = math.sqrt(
        (s_tau / m_tau) ** 2 + (M_MU_SIGMA / M_MU_VALUE) ** 2
    )
    sigma_a1 = sigma_log / (D_DIM * log_b1)
    sigma_K = math.sqrt(N_LEP) / a1 ** 2 * sigma_a1
    return K, sigma_K


def test_kstar_14_eq_1_over_8(K: float, sigma_K: float) -> None:
    """Compute K^14 and compare to 1/8."""
    K14 = K ** 14
    target = 1.0 / 8.0
    gap = K14 - target
    # sigma(K^14) = 14 * K^13 * sigma(K)
    sigma_K14 = 14 * K ** 13 * sigma_K
    n_sigma = abs(gap) / sigma_K14
    print(f"    K        = {K:.10f} +/- {sigma_K:.2e}")
    print(f"    K^14     = {K14:.10f}")
    print(f"    1/8      = {target:.10f}")
    print(f"    gap      = {gap:+.4e}")
    print(f"    sigma    = {sigma_K14:.4e}")
    print(f"    n_sigma  = {n_sigma:.3f}")
    return K, K14, gap, n_sigma


def section_pdg_average() -> None:
    header("(A) PDG 2024 average (tau mass = 1776.86 +/- 0.12 MeV)")
    print(f"  Inputs:")
    print(f"    m_tau = {M_TAU_VALUE} +/- {M_TAU_SIGMA} MeV")
    print(f"    m_mu  = {M_MU_VALUE} +/- {M_MU_SIGMA} MeV")
    print(f"    d     = {D_DIM}")
    print(f"    b_1   = 3/2")
    print()
    K, sigma_K = k_star_from_tau(M_TAU_VALUE, M_TAU_SIGMA)
    print(f"  Derived:")
    print(f"    ratio = m_tau/m_mu = {M_TAU_VALUE/M_MU_VALUE:.10f}")
    print(f"    a_1   = log(ratio)/(d*log(b_1)) = {math.log(M_TAU_VALUE/M_MU_VALUE)/(D_DIM*math.log(B1_LEP)):.10f}")
    print(f"    K_STAR_lep = sqrt({N_LEP})/a_1 = {K:.10f}")
    print()
    print(f"  Test K_STAR^14 = 1/8:")
    test_kstar_14_eq_1_over_8(K, sigma_K)
    print()


def section_exact_kstar() -> None:
    header("(B) What K_STAR value would make K^14 = 1/8 exactly?")
    K_exact = (1.0 / 8.0) ** (1.0 / 14.0)
    K_pdg, sigma_K = k_star_from_tau(M_TAU_VALUE, M_TAU_SIGMA)
    gap_K = K_exact - K_pdg
    print(f"  K_exact such that K^14 = 1/8:")
    print(f"    K_exact = 8^(-1/14) = (1/8)^(1/14) = {K_exact:.12f}")
    print(f"    K_PDG   = {K_pdg:.12f}")
    print(f"    K_exact - K_PDG = {gap_K:+.4e}")
    print(f"    in K-sigma       = {abs(gap_K)/sigma_K:.3f}")
    print()
    print("  What m_tau value would be consistent with K = K_exact?")
    # K_exact corresponds to a_1 = sqrt(N_lep)/K_exact
    a1_exact = math.sqrt(N_LEP) / K_exact
    # and log(m_tau/m_mu) = a_1 * d * log(b_1)
    log_ratio_exact = a1_exact * D_DIM * math.log(B1_LEP)
    ratio_exact = math.exp(log_ratio_exact)
    m_tau_exact = ratio_exact * M_MU_VALUE
    print(f"    a_1 (for K_exact)    = {a1_exact:.10f}")
    print(f"    log(m_tau/m_mu) req  = {log_ratio_exact:.10f}")
    print(f"    m_tau/m_mu required  = {ratio_exact:.10f}")
    print(f"    m_tau required       = {m_tau_exact:.6f} MeV")
    print(f"    m_tau PDG 2024       = {M_TAU_VALUE} MeV")
    print(f"    difference           = {m_tau_exact - M_TAU_VALUE:+.6f} MeV")
    print(f"    in PDG sigma (0.12)  = {(m_tau_exact - M_TAU_VALUE)/M_TAU_SIGMA:+.3f}")
    print()
    print("  Reading: if K_STAR^14 = 1/8 exactly, then the true m_tau is")
    print(f"  about 0.07 MeV BELOW the PDG 2024 central value (1776.79 vs")
    print(f"  1776.86).  Within the PDG uncertainty (0.6 sigma below), but")
    print(f"  systematic rather than statistical.  KEDR 2007 (1776.80 MeV)")
    print(f"  is the closest individual measurement to this required value.")
    print()


def section_experimental_measurements() -> None:
    header("(C) Individual tau mass measurements vs. K^14 = 1/8")
    print("  The PDG 2024 average is built from several independent")
    print("  experiments with different central values and uncertainties.")
    print("  Testing K^14 against each:")
    print()
    measurements = [
        ("BESIII 2014", 1776.91, math.hypot(0.12, 0.10)),
        ("BaBar 2009",  1776.68, math.hypot(0.12, 0.41)),
        ("Belle 2007",  1776.61, math.hypot(0.13, 0.35)),
        ("KEDR 2007",   1776.80, 0.23),
        ("PDG 2024 avg",1776.86, 0.12),
    ]
    print(f"  {'experiment':<14} {'m_tau +/- sigma':<22} {'K_STAR':<14} {'K^14 - 1/8':<16} {'n_sigma':<8}")
    print("  " + "-" * 78)
    for name, m_tau, s_tau in measurements:
        K, sigma_K = k_star_from_tau(m_tau, s_tau)
        K14 = K ** 14
        gap = K14 - 1.0/8.0
        sigma_K14 = 14 * K ** 13 * sigma_K
        n_sig = abs(gap) / sigma_K14
        mt_str = f"{m_tau} +/- {s_tau:.2f}"
        print(f"  {name:<14} {mt_str:<22} {K:<14.8f} {gap:+.4e}  {n_sig:.2f}")
    print()
    print("  Reading: KEDR 2007 (1776.80 MeV) gives K^14 closest to 1/8")
    print("  at only 0.05 sigma -- because 1776.80 is the closest to the")
    print("  K_exact-required value of 1776.79.  BESIII 2014 (high at")
    print("  1776.91) gives 0.78 sigma (gap negative, K too low).  BaBar")
    print("  and Belle (low, below 1776.79) give positive gaps.  The PDG")
    print("  average at 1776.86 sits 0.59 sigma above exact.  None rules")
    print("  out K^14 = 1/8, but KEDR is the tightest single match.")
    print()


def section_precision_requirement() -> None:
    header("(D) Precision requirement to resolve K^14 = 1/8")
    K_pdg, sigma_K_current = k_star_from_tau(M_TAU_VALUE, M_TAU_SIGMA)
    K14 = K_pdg ** 14
    target = 1.0 / 8.0
    gap = K14 - target

    print(f"  Current: sigma(K) = {sigma_K_current:.2e}, gap = {gap:.2e}")
    print(f"  Current: n_sigma = {abs(gap)/(14*K_pdg**13*sigma_K_current):.3f}")
    print()
    print(f"  To resolve at n_sigma = 1.0 (definitive):")
    print(f"    need sigma(K) < |gap|/(14*K^13) = {abs(gap)/(14*K_pdg**13):.2e}")
    sig_needed_K = abs(gap) / (14 * K_pdg ** 13)
    sig_needed_tau = sig_needed_K * M_TAU_VALUE * (K_pdg / sig_needed_K) * (D_DIM * math.log(B1_LEP)) * sig_needed_K / K_pdg
    # Easier: sigma(K)/K = sigma(m_tau)/(m_tau * d * log(b1))
    # So sigma(m_tau) = sigma(K)/K * m_tau * d * log(b1)
    rel_K_needed = sig_needed_K / K_pdg
    sigma_tau_needed = rel_K_needed * M_TAU_VALUE * D_DIM * math.log(B1_LEP)
    print(f"    requires sigma(m_tau) < {sigma_tau_needed:.4f} MeV")
    print()
    print(f"  To resolve at n_sigma = 5 (clear signal):")
    sig_5sig = 0.2 * abs(gap) / (14 * K_pdg ** 13)
    rel_5sig = sig_5sig / K_pdg
    sigma_tau_5sig = rel_5sig * M_TAU_VALUE * D_DIM * math.log(B1_LEP)
    print(f"    requires sigma(K) < {sig_5sig:.2e}")
    print(f"    requires sigma(m_tau) < {sigma_tau_5sig:.4f} MeV")
    print()
    print("  Context: current PDG 2024 is 0.12 MeV.  To reach 0.01 MeV")
    print("  would require ~10x improvement, which is plausible from")
    print("  Belle II (long-term running, ~10/ab) and BESIII upgrades")
    print("  over the coming years.  Not yet achievable.")
    print()


def section_verdict() -> None:
    header("(E) Verdict")
    K, sigma_K = k_star_from_tau(M_TAU_VALUE, M_TAU_SIGMA)
    K14 = K ** 14
    gap = K14 - 1.0/8.0
    n_sigma = abs(gap) / (14 * K**13 * sigma_K)
    print(f"""\
  K_STAR_lep (from PDG 2024 m_tau, m_mu):
      K       = {K:.10f} +/- {sigma_K:.2e}
      K^14    = {K**14:.10f}
      1/8     = {1/8:.10f}
      gap     = {gap:+.4e}
      n_sigma = {n_sigma:.3f}

  The closed form K_STAR^14 = 1/8 = q_2^(-q_3) holds at {n_sigma:.3f} sigma
  of the PDG-derived K_STAR.  WITHIN 1 SIGMA but NOT DEFINITIVE.

  Precision is DOMINATED by the tau mass uncertainty (sigma_tau =
  0.12 MeV = 68 ppm of m_tau).  The K_STAR uncertainty (2.06e-5)
  is a direct consequence of this tau uncertainty.

  To distinguish 'K^14 = 1/8 exactly' from '0.59 sigma numerical
  coincidence', we need ~10x tighter m_tau (sigma ~ 0.01 MeV).
  That is plausible but not currently available.

  Individual experiment check:
    - KEDR 2007    (1776.80 MeV): gives K^14 - 1/8 at 0.05 sigma  **closest**
    - BaBar 2009   (1776.68 MeV): gives K^14 - 1/8 at 0.25 sigma
    - Belle 2007   (1776.61 MeV): gives K^14 - 1/8 at 0.48 sigma
    - PDG 2024 avg (1776.86 MeV): gives K^14 - 1/8 at 0.59 sigma
    - BESIII 2014  (1776.91 MeV): gives K^14 - 1/8 at 0.78 sigma

  The exact required value is m_tau = 1776.79 MeV.  KEDR 2007
  (1776.80 +/- 0.23) sits almost exactly at this value, and gives
  K^14 = 1/8 to within 0.05 sigma.  BESIII 2014 (the highest
  central value) is furthest from the exact required value and
  gives the largest gap.  If KEDR's central value is closer to
  the true tau mass than PDG's average (which is pulled higher by
  BESIII), the relation K^14 = 1/8 is plausibly exact.

  STATUS OF THE CHAIN:

    Step 1: q_2 = 2 (Klein parity)            [primitive]
    Step 2: N_lep = q_2^2 = 4                 [canonical]
    Step 3: Framework depth = 4               [3-way convergent]
    Step 4: |F_4| = 7                         [Farey theorem]
    Step 5: EDO basis = q_2 * |F_4| = 14      [Klein doubling]
    Step 6: K_STAR^14 = q_2^(-q_3) = 1/8      [0.59 sigma, this check]

  The closed form is within 1 sigma at current precision.  The chain
  is plausible end-to-end but contains three structural identifications
  (depth = 4, Klein parity on Farey rationals, K^14 = 1/8) that are
  each defensible but not yet theorems.

  The K_STAR ~ 2^(-3/14) candidate is the session's tightest closure
  candidate by a wide margin (~60x closer than the next-best form).
  Its definitive validation or refutation requires higher-precision
  tau mass data.
""")


def main() -> None:
    print("=" * 78)
    print("  K_STAR PRECISION CHECK: is K_STAR^14 = 1/8 exact, or a coincidence?")
    print("=" * 78)
    section_pdg_average()
    section_exact_kstar()
    section_experimental_measurements()
    section_precision_requirement()
    section_verdict()


if __name__ == "__main__":
    main()
