#!/usr/bin/env python3
"""
Fermion mass running: tree-level predictions + correction analysis.

The tree-level mass formula (D34) gives mass ratios as
(W_heavy/W_light)^a with rational sector exponents.
This script:
  1. Computes tree-level predictions and residuals
  2. Shows that gauge RG running is flavor-universal (doesn't fix μ/e)
  3. Computes the SL(2,Z) trace correction (chain topology)
  4. Tests the Koide constraint
  5. Computes QCD running for quark sectors

Key finding: The 37% μ/e gap is a tree-level problem, not a
running problem. The correction must come from generation-dependent
chain topology in the SL(2,Z) structure.

Usage:
    python3 sync_cost/derivations/fermion_mass_running.py
"""

import math

# ── Constants ────────────────────────────────────────────────────────────────

PHI = (1 + math.sqrt(5)) / 2
PHI_SQ = PHI ** 2

# Phase-state weights (D34)
W_B = 26   # heaviest (duty(2) × gap(3))
W_C = 7    # middle (gap(2) × duty(3))
W_A = 1    # lightest (duty(2) × duty(3))

# Sector exponents: a = d - 1/2 + charge/2, d = 3
A_LEPTON = 5 / 2    # charged leptons
A_DOWN = 2           # down-type quarks
A_UP = 3             # up-type quarks

# Observed masses (GeV)
M_TAU = 1.77686;  M_MU = 0.10566;  M_E = 0.000511
M_TOP = 172.5;    M_CHARM = 1.27;   M_UP = 0.00216
M_BOTTOM = 4.18;  M_STRANGE = 0.0934; M_DOWN = 0.00467


def tree_ratio(w_heavy, w_light, a):
    return (w_heavy / w_light) ** a


def main():
    print("=" * 75)
    print("  FERMION MASS ANALYSIS: TREE + CORRECTIONS")
    print("  From D34 phase-state weights + D50 running analysis")
    print("=" * 75)

    # ── 1. Tree-level predictions ────────────────────────────────────────
    print(f"\n{'─' * 75}")
    print("  1. TREE-LEVEL PREDICTIONS (K = 1)")
    print(f"{'─' * 75}\n")

    sectors = [
        ("LEPTONS (a=5/2)", A_LEPTON, [
            ("m_τ/m_e", W_B, W_A, M_TAU / M_E),
            ("m_μ/m_e", W_C, W_A, M_MU / M_E),
            ("m_τ/m_μ", W_B, W_C, M_TAU / M_MU),
        ]),
        ("DOWN QUARKS (a=2)", A_DOWN, [
            ("m_b/m_d", W_B, W_A, M_BOTTOM / M_DOWN),
            ("m_s/m_d", W_C, W_A, M_STRANGE / M_DOWN),
            ("m_b/m_s", W_B, W_C, M_BOTTOM / M_STRANGE),
        ]),
        ("UP QUARKS (a=3)", A_UP, [
            ("m_t/m_u", W_B, W_A, M_TOP / M_UP),
            ("m_c/m_u", W_C, W_A, M_CHARM / M_UP),
            ("m_t/m_c", W_B, W_C, M_TOP / M_CHARM),
        ]),
    ]

    print(f"  {'ratio':>12s}  {'a':>4s}  {'tree':>10s}  {'observed':>10s}  "
          f"{'residual':>10s}  {'formula'}")
    print("  " + "-" * 72)

    for sector_name, a, ratios in sectors:
        for name, wh, wl, obs in ratios:
            pred = tree_ratio(wh, wl, a)
            resid = (pred - obs) / obs
            formula = f"{wh}^{a}" if wl == 1 else f"({wh}/{wl})^{a}"
            print(f"  {name:>12s}  {a:4.1f}  {pred:10.1f}  {obs:10.1f}  "
                  f"{resid:+10.1%}  {formula}")
        print()

    # ── 2. Why gauge running doesn't help ────────────────────────────────
    print(f"{'─' * 75}")
    print("  2. GAUGE RG RUNNING IS FLAVOR-UNIVERSAL")
    print(f"{'─' * 75}\n")

    ALPHA_EM = 1 / 137.036
    ALPHA_2 = 0.03380

    gamma_qed = (3 / 2) * (ALPHA_EM / math.pi)
    gamma_weak = (9 / 4) * (ALPHA_2 / (4 * math.pi))
    gamma_total = gamma_qed + gamma_weak

    print(f"  One-loop lepton anomalous dimension (gauge part):")
    print(f"    γ_QED  = (3/2)(α_em/π)  = {gamma_qed:.6f}")
    print(f"    γ_weak = (9/4)(α₂/4π)   = {gamma_weak:.6f}")
    print(f"    γ_total                  = {gamma_total:.6f}")
    print()
    print(f"  This is FLAVOR-INDEPENDENT. It runs y_μ and y_e at the same rate.")
    print(f"  The ratio y_μ/y_e = m_μ/m_e is RG-invariant at one loop.")
    print()
    print(f"  The flavor-dependent part (Yukawa self-coupling y_f²/(16π²)) is:")
    y_mu = M_MU / (246.22 / math.sqrt(2))
    y_e = M_E / (246.22 / math.sqrt(2))
    print(f"    y_μ = {y_mu:.6e},  y_μ²/(16π²) = {y_mu**2/(16*math.pi**2):.2e}")
    print(f"    y_e = {y_e:.6e},  y_e²/(16π²) = {y_e**2/(16*math.pi**2):.2e}")
    print(f"  Both negligible. Gauge running CANNOT fix the μ/e ratio.")

    # ── 3. Chain topology / SL(2,Z) correction ───────────────────────────
    print(f"\n{'─' * 75}")
    print("  3. CHAIN TOPOLOGY CORRECTION (SL(2,Z) traces)")
    print(f"{'─' * 75}\n")

    print("  From D34 §6: SL(2,Z) matrices for q=3 pair:")
    print("    M(1/3) via path LL: [[1,0],[2,1]]")
    print("    M(2/3) via path LR: [[1,1],[1,1]]")
    print("    tr(M₁⁻¹M₂) = 1 → elliptic, mixing angle 30°")
    print()

    # The mixing matrix M₁⁻¹M₂
    # M(1/3) = [[1,0],[2,1]], M(2/3) = [[1,1],[1,1]]  (up to normalization)
    # Actually the SB matrices are cumulative products of L and R.
    # For 1/3: from 0/1--1/0, go L to get 1/2, then L to get 1/3.
    # M(1/3) = L² = [[1,0],[1,1]]² = [[1,0],[2,1]]
    # For 2/3: from 0/1--1/0, go L to 1/2, then R to 2/3.
    # M(2/3) = R·L = [[1,1],[0,1]]·[[1,0],[1,1]] = [[2,1],[1,1]]
    # M₁⁻¹ = [[1,0],[-2,1]]
    # M₁⁻¹M₂ = [[1,0],[-2,1]]·[[2,1],[1,1]] = [[2,1],[-3,-1]]
    # tr = 2 + (-1) = 1

    print("  Correct computation:")
    print("    M(1/3) = L² = [[1,0],[2,1]]")
    print("    M(2/3) = RL = [[2,1],[1,1]]")
    print("    M₁⁻¹M₂ = [[2,1],[-3,-1]]")
    print("    tr(M₁⁻¹M₂) = 2 + (-1) = 1")
    print()

    # Elliptic: |tr| < 2, so cos(θ) = tr/2 = 1/2, θ = 60° (or π/3)
    trace = 1
    cos_theta = trace / 2
    theta = math.acos(cos_theta)
    print(f"    |tr| = {abs(trace)} < 2 → elliptic rotation")
    print(f"    cos θ = tr/2 = {cos_theta}")
    print(f"    θ = {math.degrees(theta):.1f}° = π/3")
    print()

    # The mixing angle θ = 60° modifies the effective weight.
    # In the mass matrix, off-diagonal elements go as sin(θ):
    # M_mass = diag(m_1, m_2, m_3) × U(θ)
    # The eigenvalue shift for the middle generation is proportional to sin²θ.

    # Test: does sin²(60°) × (some weight factor) give the right correction?
    sin2_theta = math.sin(theta) ** 2  # = 3/4
    print(f"  sin²(60°) = {sin2_theta:.4f} = 3/4")
    print()

    # With mixing, the effective weight for the middle generation is modified.
    # The simplest model: W_C_eff = W_C + (W_B - W_C) × sin²θ × mixing_fraction
    # At θ = 60°: sin²θ = 3/4
    # If we assume the mixing "borrows" from the heavy generation:

    # Actually, let's find what W_C_eff gives the correct ratio.
    target = M_MU / M_E  # 206.8
    W_C_needed = target ** (1 / A_LEPTON)  # = 206.8^0.4
    print(f"  Required W_C_eff for μ/e = 206.8:")
    print(f"    (W_C_eff)^(5/2) = 206.8  →  W_C_eff = 206.8^(2/5) = {W_C_needed:.4f}")
    print(f"    Tree value: W_C = 7")
    print(f"    Correction factor: {W_C_needed / 7:.4f}")
    print()

    # The correction factor is ~1.27. Can the mixing explain this?
    # With θ = 60° and a transition matrix element proportional to sin θ:
    # Eigenvalue shift ~ sin²θ × coupling ~ (3/4) × (something)
    # We need (3/4) × x = 0.27, so x = 0.36

    # Test specific mixing models:
    corrections = [
        ("sin²θ × (W_B-W_C)/(W_B+W_C)", sin2_theta * (W_B - W_C) / (W_B + W_C)),
        ("sin²θ × W_A/W_C", sin2_theta * W_A / W_C),
        ("sin²θ × 1/3", sin2_theta * 1 / 3),
        ("2sin²θ/(q₃²)", 2 * sin2_theta / 9),
        ("(q₃-q₂)/q₃", (3 - 2) / 3),
    ]

    print(f"  Candidate mixing corrections to W_C:")
    print(f"    {'model':>35s}  {'δW/W':>8s}  {'W_eff':>8s}  {'(W_eff)^2.5':>12s}  {'residual':>10s}")
    print("    " + "-" * 80)

    for name, delta in corrections:
        w_eff = W_C * (1 + delta)
        pred = w_eff ** A_LEPTON
        resid = (pred - target) / target
        print(f"    {name:>35s}  {delta:8.4f}  {w_eff:8.4f}  {pred:12.2f}  {resid:+10.1%}")

    # ── 4. Koide formula test ────────────────────────────────────────────
    print(f"\n{'─' * 75}")
    print("  4. KOIDE FORMULA (phenomenological constraint)")
    print(f"{'─' * 75}\n")

    # Koide: (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² = 2/3
    sum_m = M_E + M_MU + M_TAU
    sum_sqrt_m = math.sqrt(M_E) + math.sqrt(M_MU) + math.sqrt(M_TAU)
    koide = sum_m / sum_sqrt_m ** 2
    print(f"  Koide parameter Q = (Σmᵢ)/(Σ√mᵢ)²")
    print(f"    Observed: Q = {koide:.8f}")
    print(f"    2/3      = {2/3:.8f}")
    print(f"    Residual: {abs(koide - 2/3) / (2/3):.4%}")
    print(f"    The factor 2/3 = Klein bottle population ratio (D19)")
    print()

    # Use Koide + τ/e to predict μ/e:
    # Let r = m_τ/m_e = 3477 (observed, ≈ tree prediction)
    # Koide says: (1 + x + r) / (1 + √x + √r)² = 2/3
    # where x = m_μ/m_e
    # Solve for x.

    r = M_TAU / M_E  # use observed τ/e
    # (1 + x + r) / (1 + √x + √r)² = 2/3
    # 3(1 + x + r) = 2(1 + √x + √r)²
    # Let s = √x.  Then x = s².
    # 3(1 + s² + r) = 2(1 + s + √r)²
    # 3 + 3s² + 3r = 2 + 4s + 4√r + 2s² + 4s√r + 2r
    # s² - 4s(1+√r) + (1 + r - 4√r) = 0  ... let me do this numerically.

    sqrt_r = math.sqrt(r)
    # Solve: 3(1 + s² + r) = 2(1 + s + sqrt_r)²
    best_s = 0
    best_err = float('inf')
    for i in range(1, 100000):
        s = i * 0.001
        lhs = 3 * (1 + s * s + r)
        rhs = 2 * (1 + s + sqrt_r) ** 2
        err = abs(lhs - rhs)
        if err < best_err:
            best_err = err
            best_s = s

    x_koide = best_s ** 2
    print(f"  Koide prediction for m_μ/m_e (given m_τ/m_e = {r:.1f}):")
    print(f"    m_μ/m_e = {x_koide:.2f}")
    print(f"    Observed: {M_MU/M_E:.2f}")
    print(f"    Residual: {abs(x_koide - M_MU/M_E)/(M_MU/M_E):.1%}")
    print()
    print(f"  If we use the TREE value m_τ/m_e = {tree_ratio(W_B, W_A, A_LEPTON):.1f}:")

    r_tree = tree_ratio(W_B, W_A, A_LEPTON)
    sqrt_r_tree = math.sqrt(r_tree)
    best_s2 = 0
    best_err2 = float('inf')
    for i in range(1, 100000):
        s = i * 0.001
        lhs = 3 * (1 + s * s + r_tree)
        rhs = 2 * (1 + s + sqrt_r_tree) ** 2
        err = abs(lhs - rhs)
        if err < best_err2:
            best_err2 = err
            best_s2 = s

    x_koide_tree = best_s2 ** 2
    print(f"    Koide → m_μ/m_e = {x_koide_tree:.2f}")
    print(f"    Observed: {M_MU/M_E:.2f}")
    print(f"    Residual: {abs(x_koide_tree - M_MU/M_E)/(M_MU/M_E):.1%}")

    # ── 5. QCD running for quarks ────────────────────────────────────────
    print(f"\n{'─' * 75}")
    print("  5. QCD RUNNING FOR QUARK SECTORS")
    print(f"{'─' * 75}\n")

    # SM quark mass running: m(μ₂)/m(μ₁) = [α_s(μ₂)/α_s(μ₁)]^(γ₀/(2b₀))
    gamma_0 = 8.0 / 3
    n_f = 5
    b_0 = (33 - 2 * n_f) / (12 * math.pi)
    rg_exponent = gamma_0 / (2 * b_0)

    ALPHA_S_MZ = 0.1179
    M_Z = 91.2

    print(f"  QCD mass running exponent: γ₀/(2b₀) = {rg_exponent:.4f}")
    print(f"  This means m_q(μ) ∝ α_s(μ)^{rg_exponent:.3f}")
    print()

    # Running α_s to various scales (1-loop)
    def alpha_s(mu):
        return ALPHA_S_MZ / (1 + b_0 * ALPHA_S_MZ * math.log(mu / M_Z))

    # Mass ratio running: the RATIO m_b/m_d runs because
    # the two masses are evaluated at different scales.
    # m_b is typically quoted at m_b (pole or MS-bar at m_b)
    # m_d is typically quoted at 2 GeV.
    # The running between 2 GeV and 4.18 GeV:
    a_s_2 = alpha_s(2.0)
    a_s_mb = alpha_s(M_BOTTOM)
    a_s_mt = alpha_s(M_TOP)
    a_s_mc = alpha_s(M_CHARM)

    print(f"  α_s at key scales:")
    print(f"    α_s(2 GeV) = {a_s_2:.4f}")
    print(f"    α_s(m_c)   = {alpha_s(M_CHARM):.4f}")
    print(f"    α_s(m_b)   = {alpha_s(M_BOTTOM):.4f}")
    print(f"    α_s(M_Z)   = {ALPHA_S_MZ:.4f}")
    print(f"    α_s(m_t)   = {alpha_s(M_TOP):.4f}")

    # The tree-level predictions assume all masses at the SAME scale (tree/Planck).
    # To compare with observed masses at DIFFERENT scales, we need to run
    # each mass from tree scale to its evaluation scale.

    # The common-scale mass ratio at μ = 2 GeV:
    # m_b(2 GeV) / m_d(2 GeV) vs tree prediction
    # m_b(2 GeV) = m_b(m_b) × [α_s(2)/α_s(m_b)]^(γ₀/(2b₀))
    m_b_at_2 = M_BOTTOM * (a_s_2 / a_s_mb) ** rg_exponent
    ratio_at_2 = m_b_at_2 / M_DOWN

    print(f"\n  Running to common scale (2 GeV):")
    print(f"    m_b(2 GeV) = m_b(m_b) × [α_s(2)/α_s(m_b)]^{rg_exponent:.3f}")
    print(f"               = {M_BOTTOM} × ({a_s_2:.4f}/{a_s_mb:.4f})^{rg_exponent:.3f}")
    print(f"               = {m_b_at_2:.2f} GeV")
    print(f"    m_b(2)/m_d(2) = {ratio_at_2:.1f}")
    print(f"    Tree: 26² = {26**2}")
    print(f"    Residual: {abs(ratio_at_2 - 676)/676:.1%}")

    m_t_at_2 = M_TOP * (a_s_2 / a_s_mt) ** rg_exponent
    m_c_at_2 = M_CHARM * (a_s_2 / a_s_mc) ** rg_exponent
    ratio_tu_at_2 = m_t_at_2 / (M_UP)
    ratio_cu_at_2 = m_c_at_2 / (M_UP)

    print(f"\n    m_t(2 GeV) = {m_t_at_2:.1f} GeV")
    print(f"    m_c(2 GeV) = {m_c_at_2:.3f} GeV")
    print(f"    m_t(2)/m_u(2) = {ratio_tu_at_2:.0f}   (tree: {26**3})")
    print(f"    m_c(2)/m_u(2) = {ratio_cu_at_2:.1f}   (tree: {7**3})")

    # ── 6. Summary ───────────────────────────────────────────────────────
    print(f"\n{'=' * 75}")
    print("  SUMMARY")
    print(f"{'=' * 75}")
    print(f"""
  TREE-LEVEL PREDICTIONS (zero free parameters):

    Phase-state weights: B=26, C=7, A=1
    Sector exponents: a_lepton=5/2, a_down=2, a_up=3

  BEST RESULTS:
    m_τ/m_e = 26^(5/2) = 3447    vs  3477   →  0.9%  (excellent)
    Koide Q = 2/3                 vs  0.6667 →  0.04% (if Koide is traced to Klein bottle)

  OPEN:
    m_μ/m_e = 7^(5/2) = 130      vs  207    →  37%   (needs SL(2,Z) mass matrix)
    Koide with tree τ/e → μ/e = {x_koide_tree:.0f}  vs  207    →  {abs(x_koide_tree - 207)/207:.0%}

  GAUGE RG RUNNING:
    Flavor-universal at one loop → cannot fix lepton ratios.
    QCD running significant for quarks (evaluated at different scales).

  THE REMAINING COMPUTATION:
    Diagonalize the 3×3 mass matrix from SL(2,Z) path matrices
    at q=2 and q=3 denominators. The off-diagonal elements are
    determined by the trace classification (D34 §6). This is a
    finite matrix computation, not an infinite-dimensional problem.
""")


if __name__ == "__main__":
    main()
