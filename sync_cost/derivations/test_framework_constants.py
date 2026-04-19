"""
test_framework_constants.py

Consistency tests for framework_constants.py. A CI guard: these
tests run on every PR and fail if any framework constant drifts
out of consistency with a downstream derivation chain.

Rationale: the repository grew from a small start; many files
inline numerical literals (PDG masses, H_0, Planck units, Omega
ratios) that can diverge from framework_constants as the project
matures. These tests pin the single-source-of-truth relations.

Add new tests when a derivation chain produces a framework
constant — the test should recompute the constant from primitives
and assert agreement.

Run:
    python3 -m pytest sync_cost/derivations/test_framework_constants.py
    python3 sync_cost/derivations/test_framework_constants.py   # pytest-less

Every assertion quotes its source derivation in the message.
"""

from __future__ import annotations

import math
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from framework_constants import (
    # Klein integers
    Q2, Q3, D, INTERACT, F_6_COUNT, F_7_COUNT, R_HIERARCHY,
    # Kuramoto
    K_STAR, LAMBDA_UNLOCK,
    # Cosmology
    OMEGA_B, OMEGA_DM, OMEGA_L, OMEGA_M,
    H_0_SI, T_H, LAMBDA_SI, L_H_HUBBLE,
    # Physical
    HBAR, G_NEWTON, C_LIGHT,
    # Planck
    ELL_P, T_P, M_P,
    # Electroweak
    SIN2_TW_MZ, ALPHA_S_MZ, ALPHA_EM_MZ, ALPHA_2_MZ, ALPHA_Y_MZ,
    # Masses
    M_E, M_MU, M_TAU,
    V_GEV,
)


# ============================================================
# Klein-integer algebra
# ============================================================

def test_klein_integers():
    assert Q2 == 2
    assert Q3 == 3
    assert D == 3
    assert INTERACT == Q2 * Q3 == 6
    assert F_6_COUNT == 13                 # sin^2 theta_W denom
    assert F_7_COUNT == 19                 # Omega partition denom
    assert R_HIERARCHY == 6 * 13 ** 54     # hierarchy_gaussian_lattice.md Step 5


def test_cosmological_partition_sums_to_one():
    # The 13:5:1 partition (baryon_fraction.md)
    assert OMEGA_B + OMEGA_DM + OMEGA_L == 1
    assert OMEGA_M == OMEGA_B + OMEGA_DM
    assert OMEGA_B == 1 / F_7_COUNT
    assert OMEGA_DM == 5 / F_7_COUNT
    assert OMEGA_L == F_6_COUNT / F_7_COUNT


# ============================================================
# Planck units
# ============================================================

def test_planck_length_from_hbar_G_c():
    ell_P_computed = math.sqrt(HBAR * G_NEWTON / C_LIGHT ** 3)
    assert abs(ELL_P - ell_P_computed) / ELL_P < 1e-10, (
        f"ELL_P={ELL_P} != sqrt(hbar G / c^3)={ell_P_computed}"
    )


def test_planck_time_consistency():
    assert abs(T_P - ELL_P / C_LIGHT) / T_P < 1e-10


def test_planck_mass_consistency():
    m_P_computed = math.sqrt(HBAR * C_LIGHT / G_NEWTON)
    assert abs(M_P - m_P_computed) / M_P < 1e-10


def test_planck_length_numerical():
    # CODATA 2022: ell_P = 1.616255(18) e-35 m
    assert abs(ELL_P - 1.616255e-35) / 1.616255e-35 < 1e-4


# ============================================================
# Hubble / cosmological
# ============================================================

def test_hubble_time_consistent():
    assert abs(T_H - 1 / H_0_SI) / T_H < 1e-10


def test_cosmological_constant_from_H0_OmegaL():
    # Lambda = 3 Omega_L H_0^2 / c^2 (FLRW dark-energy identification)
    Lambda_expected = 3 * 0.6847 * H_0_SI ** 2 / C_LIGHT ** 2
    assert abs(LAMBDA_SI - Lambda_expected) / LAMBDA_SI < 1e-6


# ============================================================
# R hierarchy — the key cross-check that caught the 7.14e60 stale
# ============================================================

def test_R_matches_Hubble_to_Planck_ratio():
    """
    R = 6 * 13^54 should match the observed Hubble-to-Planck time
    ratio t_H/t_P to ~0.5% (hierarchy_gaussian_lattice.md, Issue
    #56 Tier 3 item 13). The value 7.14e60 that appeared in line
    125 of the same doc was stale; verified by r_residual_audit.py.
    """
    R_observed = T_H / T_P
    residual = abs(R_HIERARCHY - R_observed) / R_observed
    # 0.48% is the Planck-2018 value; allow up to 2% to survive
    # future Hubble parameter updates without churning the test
    assert residual < 0.02, (
        f"R = 6*13^54 = {R_HIERARCHY:.3e} vs t_H/t_P = {R_observed:.3e}, "
        f"residual {residual*100:.2f}%"
    )


# ============================================================
# Mass-sector identity a_1(lep) = q_2 / K*
# ============================================================

def test_a1_lepton_from_PDG_matches_q2_over_Kstar():
    """
    From a1_from_saddle_node.md: a_1(lep) = q_2 / K*.
    Equivalently: K* = q_2 / a_1(lep), where a_1(lep) is computed
    from PDG lepton masses via the generation exponent law.
    Cross-check: the constant K_STAR = 0.86196052 stored here must
    reproduce the lepton identity within 1%.
    """
    # generation ratio m_tau / m_mu = (3/2)^(d * a_1)
    r_32 = M_TAU / M_MU
    a_1 = math.log(r_32) / (D * math.log(3 / 2))
    K_star_derived = Q2 / a_1
    residual = abs(K_STAR - K_star_derived) / K_STAR
    assert residual < 0.001, (
        f"K_STAR={K_STAR:.8f} vs q_2/a_1(lep)={K_star_derived:.8f}, "
        f"residual {residual*100:.4f}%"
    )


# ============================================================
# sin^2 theta_W structural identity
# ============================================================

def test_sinsq_theta_W_matches_d_eff_80_over_27():
    """
    sinw_effective_dimension.md: sin^2 theta_W = 2^(80/27) /
    (2^(80/27) + 3^(80/27)). Should match PDG SIN2_TW_MZ to
    within 1 sigma (<1%).
    """
    d_eff = 80 / 27
    sinsq_predicted = (2 ** d_eff) / (2 ** d_eff + 3 ** d_eff)
    residual = abs(SIN2_TW_MZ - sinsq_predicted) / SIN2_TW_MZ
    assert residual < 0.01, (
        f"SIN2_TW_MZ={SIN2_TW_MZ} vs 2^(80/27)/(...)={sinsq_predicted:.5f}, "
        f"residual {residual*100:.3f}%"
    )


# ============================================================
# Omega_b with cross-sector |r|^2 tax
# ============================================================

def test_Omega_b_with_cross_sector_tax():
    """
    omega_b_residual_phase_b.py: Omega_b = (1/19) * |r|^2 where
    |r| = 0.968 (duty-cycle-derived). Predicts 0.04932 vs Planck
    2018 observed 0.0493 ± 0.0003.
    """
    r_coherence = 0.968                     # from duty_cycle_dictionary.md
    Omega_b_predicted = OMEGA_B * r_coherence ** 2
    Omega_b_observed = 0.0493
    sigma = abs(Omega_b_predicted - Omega_b_observed) / 0.0003
    assert sigma < 1.0, f"Omega_b Z-score {sigma:.2f} sigma (> 1)"


# ============================================================
# Framework D_0 = lambda_unlock * D_Schroedinger
# ============================================================

def test_framework_diffusion_matches_Madelung_within_lambda():
    """
    gap2_sub_e_residual_check.py: the framework's D_0 formula
    gives (lambda/2) * hbar/m at all scales, vs Schroedinger form
    hbar/(2m). Ratio should be exactly LAMBDA_UNLOCK.
    """
    # At Planck mass (any mass gives same ratio)
    D_framework = 0.5 * LAMBDA_UNLOCK * ELL_P ** 2 / T_P
    D_SM = HBAR / (2 * M_P)
    ratio = D_framework / D_SM
    residual = abs(ratio - LAMBDA_UNLOCK) / LAMBDA_UNLOCK
    assert residual < 1e-10, (
        f"D_framework / D_SM = {ratio:.6f}, expected LAMBDA_UNLOCK={LAMBDA_UNLOCK}"
    )


# ============================================================
# Generation exponent law:  a_2 / a_1 = q_3 / q_2 = 3/2
# (generation_exponent_law.py; appears in ~8 scripts)
# ============================================================

def test_generation_exponent_law_from_leptons():
    """
    Ratio of consecutive generation exponents equals q_3/q_2 = 3/2,
    to better than 1% via PDG lepton mass ratios.

        a_1 = log(m_tau / m_mu) / log((q_3/q_2)^D)
        a_2 = log(m_mu  / m_e)  / log((q_2+q_3)/q_3)^D)
        a_2 / a_1 ≈ q_3 / q_2 to 0.04% (Issue #56 recent results)
    """
    base_1 = (Q3 / Q2) ** D                      # = (3/2)^3 = 27/8
    base_2 = ((Q2 + Q3) / Q3) ** D               # = (5/3)^3
    a_1 = math.log(M_TAU / M_MU) / math.log(base_1)
    a_2 = math.log(M_MU  / M_E)  / math.log(base_2)
    ratio = a_2 / a_1
    expected = Q3 / Q2                            # = 3/2
    residual = abs(ratio - expected) / expected
    assert residual < 0.01, (
        f"a_2/a_1 = {ratio:.6f} vs q_3/q_2 = {expected}, "
        f"residual {residual*100:.4f}%"
    )


# ============================================================
# Electroweak derived identities: alpha_2 = alpha_em / sin^2 theta_W
# ============================================================

def test_alpha_2_alpha_Y_identities_at_MZ():
    """
    ALPHA_2_MZ and ALPHA_Y_MZ must follow from ALPHA_EM_MZ and
    SIN2_TW_MZ via the textbook identities:

        alpha_2 = alpha_em / sin^2 theta_W
        alpha_Y = alpha_em / cos^2 theta_W = alpha_em / (1 - sin^2 theta_W)
    """
    a_2_expected = ALPHA_EM_MZ / SIN2_TW_MZ
    a_Y_expected = ALPHA_EM_MZ / (1 - SIN2_TW_MZ)
    assert abs(ALPHA_2_MZ - a_2_expected) / ALPHA_2_MZ < 1e-12
    assert abs(ALPHA_Y_MZ - a_Y_expected) / ALPHA_Y_MZ < 1e-12


# ============================================================
# Tongue-to-bracket ratio at K=1: 4/phi
# (a_s_alpha2_phase_a.md Sec. 3; structural identity)
# ============================================================

def test_tongue_to_bracket_ratio_is_4_over_phi():
    """
    At K = 1 with sigma^2_kernel = 1/4, the Arnold tongue width at
    the Fibonacci convergent F_n/F_{n+1} captures exactly phi/4 of
    the Stern-Brocot bracket containing it.

    Equivalently: bracket_width / tongue_width = 4/phi at all
    sufficiently deep n. Verified via Binet.
    """
    phi = (1 + math.sqrt(5)) / 2

    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    sigma_sq_kernel = 1 / 4
    expected = 4 / phi

    # Test at depths n = 15, 20: limit is reached to ~6 digits.
    for n in (15, 20):
        q = fib(n + 1)
        qq = fib(n + 2)
        w_bracket = 1.0 / (q * qq)
        w_tongue = sigma_sq_kernel / (q * q)
        ratio = w_bracket / w_tongue
        assert abs(ratio - expected) / expected < 1e-4, (
            f"At n={n}: bracket/tongue = {ratio:.6f}, expected 4/phi = {expected:.6f}"
        )


# ============================================================
# Minimal runner for pytest-less environments
# ============================================================

def _collect_tests():
    return [
        (name, obj) for name, obj in globals().items()
        if name.startswith("test_") and callable(obj)
    ]


def _main() -> int:
    tests = _collect_tests()
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  PASS  {name}")
        except AssertionError as e:
            failed += 1
            print(f"  FAIL  {name}")
            print(f"        {e}")
        except Exception as e:
            failed += 1
            print(f"  ERROR {name}: {type(e).__name__}: {e}")
    print()
    print(f"  {len(tests) - failed}/{len(tests)} tests passed")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(_main())
