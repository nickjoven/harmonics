#!/usr/bin/env python3
"""
Exact tongue widths via Newton's method on the boundary conditions.

The winding-number approach fails at K~1 due to critical slowing.
Instead, we solve the boundary conditions directly:

  F1 = f^q(θ, Ω, K) - θ - p = 0     (period-q orbit exists)
  F2 = d/dθ [f^q(θ, Ω, K)] - 1 = 0  (marginal stability = tongue boundary)

Two unknowns (θ, Ω), two equations. Newton's method converges
quadratically even at K=1.

The circle map:  f(θ) = θ + Ω - (K/2π) sin(2πθ)

For each K, we find the left and right boundaries of the 1/q tongue
by starting Newton from different initial guesses.

Then compare the duty ratio duty(2)/duty(3) to the SM running of
α_s/α₂ at one loop.

Usage:
    python3 sync_cost/derivations/tongue_newton.py
"""

import math


# ── Circle map and derivatives ───────────────────────────────────────────────

def f(theta, omega, K):
    """One step of the standard circle map."""
    return theta + omega - K / (2 * math.pi) * math.sin(2 * math.pi * theta)


def df_dtheta(theta, K):
    """∂f/∂θ = 1 - K cos(2πθ)."""
    return 1.0 - K * math.cos(2 * math.pi * theta)


def df_domega(theta, K):
    """∂f/∂Ω = 1 (always)."""
    return 1.0


def d2f_dtheta2(theta, K):
    """∂²f/∂θ² = 2πK sin(2πθ)."""
    return 2 * math.pi * K * math.sin(2 * math.pi * theta)


# ── q-th iterate and its Jacobian ────────────────────────────────────────────

def iterate_q(theta0, omega, K, q):
    """
    Compute f^q(θ₀) and accumulate:
      - df^q/dθ₀  (chain rule product of df/dθ at each step)
      - df^q/dΩ   (sum of products)
      - d²f^q/dθ₀² (for the second-order Newton system)

    Returns (theta_q, dq_dtheta, dq_domega, d2q_dtheta2).
    """
    theta = theta0
    # dq_dtheta = product of df/dθ_i
    dq_dtheta = 1.0
    # dq_domega = sum_{k=0}^{q-1} product_{j=k+1}^{q-1} df/dθ_j
    dq_domega = 0.0
    # d2q_dtheta2 via chain rule accumulation
    d2q_dtheta2 = 0.0

    # Store intermediate thetas for the product accumulation
    thetas = [theta0]
    derivs = []  # df/dθ at each step

    for i in range(q):
        di = df_dtheta(theta, K)
        derivs.append(di)
        theta = f(theta, omega, K)
        thetas.append(theta)

    # dq_dtheta = product of all derivs
    dq_dtheta = 1.0
    for di in derivs:
        dq_dtheta *= di

    # dq_domega: partial of f^q w.r.t. Ω
    # = sum_{k=0}^{q-1} product_{j=k+1}^{q-1} df/dθ_j
    dq_domega = 0.0
    for k in range(q):
        prod = 1.0
        for j in range(k + 1, q):
            prod *= derivs[j]
        dq_domega += prod

    # d2q_dtheta2: second derivative of f^q w.r.t. θ₀
    # Use recursive formula: if g = f ∘ h, then g'' = f''(h) (h')² + f'(h) h''
    # Build up iteratively
    Dq = 1.0   # first derivative accumulated so far
    D2q = 0.0  # second derivative accumulated so far
    theta = theta0
    for i in range(q):
        d1 = df_dtheta(theta, K)
        d2 = d2f_dtheta2(theta, K)
        # New second deriv: d2 * Dq^2 + d1 * D2q
        D2q_new = d2 * Dq * Dq + d1 * D2q
        Dq_new = d1 * Dq
        D2q = D2q_new
        Dq = Dq_new
        theta = f(theta, omega, K)

    d2q_dtheta2 = D2q
    theta_q = thetas[q]

    return theta_q, dq_dtheta, dq_domega, d2q_dtheta2


# ── Newton solver for tongue boundary ────────────────────────────────────────

def newton_boundary(p, q, K, theta_guess, omega_guess, max_iter=200, tol=1e-14):
    """
    Solve the 2×2 system:
      F1 = f^q(θ, Ω, K) - θ - p = 0
      F2 = df^q/dθ(θ, Ω, K) - 1 = 0

    Returns (theta, omega) or raises if no convergence.
    """
    theta = theta_guess
    omega = omega_guess

    for iteration in range(max_iter):
        theta_q, dq_dth, dq_dom, d2q_dth2 = iterate_q(theta, omega, K, q)

        F1 = theta_q - theta - p
        F2 = dq_dth - 1.0

        if abs(F1) < tol and abs(F2) < tol:
            return theta, omega

        # Jacobian of (F1, F2) w.r.t. (θ, Ω):
        # ∂F1/∂θ = dq_dth - 1
        # ∂F1/∂Ω = dq_dom
        # ∂F2/∂θ = d2q_dth2
        # ∂F2/∂Ω = d(dq_dth)/dΩ

        J11 = dq_dth - 1.0
        J12 = dq_dom
        J21 = d2q_dth2

        # For J22 = ∂(dq_dth)/∂Ω, use finite difference
        eps = 1e-8
        _, dq_dth_plus, _, _ = iterate_q(theta, omega + eps, K, q)
        J22 = (dq_dth_plus - dq_dth) / eps

        det = J11 * J22 - J12 * J21
        if abs(det) < 1e-30:
            # Degenerate Jacobian; perturb and retry
            theta += 1e-6
            continue

        dtheta = -(J22 * F1 - J12 * F2) / det
        domega = -(-J21 * F1 + J11 * F2) / det

        # Damped Newton step for safety
        step = 1.0
        for _ in range(10):
            th_new = theta + step * dtheta
            om_new = omega + step * domega
            tq, dq, _, _ = iterate_q(th_new, om_new, K, q)
            f1_new = abs(tq - th_new - p)
            f2_new = abs(dq - 1.0)
            if f1_new + f2_new < abs(F1) + abs(F2) or step < 0.01:
                break
            step *= 0.5

        theta = theta + step * dtheta
        omega = omega + step * domega

    raise RuntimeError(
        f"Newton did not converge for p/q={p}/{q}, K={K:.4f} "
        f"(|F1|={abs(F1):.2e}, |F2|={abs(F2):.2e})"
    )


def find_tongue_boundaries(p, q, K):
    """
    Find left and right boundaries of the p/q tongue at coupling K.

    Strategy: use a dense grid of (θ, Ω) initial guesses.
    The boundary solutions come in two branches (left and right),
    distinguished by their Ω values.  We collect all converged
    solutions and return the min and max Ω.

    At K=1, known exact widths: w(1/2) = 1/4, w(1/3) = 1/9.
    The 1/2 tongue spans [0.375, 0.625], so we need guesses out to ±0.15.
    """
    center = p / q
    # At K=1, w(1/2) = 0.25, so half-width = 0.125
    # Generous search range: half the Farey gap = 1/(2q)
    search_half = 0.5 / q

    all_omegas = []

    n_theta = 30
    n_omega = 20
    for i in range(n_theta):
        theta_g = i / n_theta

        for j in range(n_omega):
            # Spread omega guesses from center - search_half to center + search_half
            frac = (j + 0.5) / n_omega
            omega_g = center - search_half + 2 * search_half * frac

            try:
                th, om = newton_boundary(p, q, K, theta_g, omega_g)
                # Sanity: solution should be near the tongue
                if abs(om - center) < search_half * 1.5:
                    all_omegas.append(om)
            except (RuntimeError, OverflowError, ZeroDivisionError):
                pass

    if not all_omegas:
        return center, center, 0.0

    omega_left = min(all_omegas)
    omega_right = max(all_omegas)
    width = omega_right - omega_left
    return omega_left, omega_right, width


# ── SM running couplings ─────────────────────────────────────────────────────

M_Z = 91.2  # GeV

# α_s(M_Z) = 0.1179
ALPHA_S_MZ = 0.1179
# α₂(M_Z) = (1/127.95) / sin²θ_W, sin²θ_W = 0.23121
ALPHA_2_MZ = (1.0 / 127.95) / 0.23121

# One-loop beta coefficients (SM, 3 generations, 1 Higgs doublet)
# dα_s⁻¹/d(ln μ) = -b₃/(2π),  b₃ = -7
B3 = -7.0
# dα₂⁻¹/d(ln μ) = -b₂/(2π),  b₂ = -19/6
B2 = -19.0 / 6.0


def alpha_s(mu):
    """One-loop running of α_s from M_Z to μ."""
    return ALPHA_S_MZ / (1.0 + ALPHA_S_MZ * (-B3) / (2 * math.pi) * math.log(mu / M_Z))


def alpha_2(mu):
    """One-loop running of α₂ from M_Z to μ."""
    return ALPHA_2_MZ / (1.0 + ALPHA_2_MZ * (-B2) / (2 * math.pi) * math.log(mu / M_Z))


def ratio_alpha_s_alpha2(mu):
    """α_s(μ) / α₂(μ)."""
    return alpha_s(mu) / alpha_2(mu)


def find_mu_for_ratio(target_ratio, mu_lo=1.0, mu_hi=1e19):
    """Bisect to find μ where α_s/α₂ = target_ratio."""
    for _ in range(200):
        mu_mid = math.sqrt(mu_lo * mu_hi)  # geometric mean
        r = ratio_alpha_s_alpha2(mu_mid)
        if r > target_ratio:
            mu_lo = mu_mid
        else:
            mu_hi = mu_mid
        if mu_hi / mu_lo < 1.0 + 1e-12:
            break
    return math.sqrt(mu_lo * mu_hi)


# ── Main computation ─────────────────────────────────────────────────────────

def main():
    print("=" * 90)
    print("Tongue widths via Newton's method on boundary conditions")
    print("=" * 90)
    print()
    print("Circle map: f(θ) = θ + Ω - (K/2π) sin(2πθ)")
    print("Boundary condition: f^q(θ) - θ - p = 0  AND  df^q/dθ - 1 = 0")
    print()

    K_values = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 1.0]

    # Header
    print(f"{'K':>6s}  {'w(1/2)':>10s}  {'w(1/3)':>10s}  "
          f"{'duty(2)':>10s}  {'duty(3)':>10s}  {'ratio':>10s}  "
          f"{'μ [GeV]':>12s}  {'α_s/α₂':>10s}")
    print("-" * 90)

    results = []

    for K in K_values:
        # q=2, p=1: the 1/2 tongue
        left2, right2, w2 = find_tongue_boundaries(1, 2, K)

        # q=3, p=1: the 1/3 tongue
        left3a, right3a, w3a = find_tongue_boundaries(1, 3, K)

        # q=3, p=2: the 2/3 tongue (same width by symmetry of Arnold tongues)
        left3b, right3b, w3b = find_tongue_boundaries(2, 3, K)

        # Use the 1/3 tongue width (p=1, q=3); verify against p=2 tongue
        w3 = w3a

        duty2 = w2 / 2.0
        duty3 = w3 / 3.0

        if duty3 > 1e-15:
            ratio = duty2 / duty3
        else:
            ratio = float('inf')

        # Find the SM energy scale where α_s/α₂ matches this ratio
        try:
            mu = find_mu_for_ratio(ratio)
            mu_str = f"{mu:.2e}"
            sm_ratio = ratio_alpha_s_alpha2(mu)
            sm_str = f"{sm_ratio:.6f}"
        except Exception:
            mu_str = "N/A"
            sm_str = "N/A"

        print(f"{K:6.2f}  {w2:10.6f}  {w3:10.6f}  "
              f"{duty2:10.6f}  {duty3:10.6f}  {ratio:10.6f}  "
              f"{mu_str:>12s}  {sm_str:>10s}")

        results.append({
            'K': K, 'w2': w2, 'w3': w3, 'w3b': w3b,
            'duty2': duty2, 'duty3': duty3, 'ratio': ratio
        })

    print("-" * 90)
    print()

    # ── Verification at K=1 ──────────────────────────────────────────────────
    print("Verification at K = 1.0 (exact values known):")
    r1 = [r for r in results if abs(r['K'] - 1.0) < 0.01][0]
    print(f"  w(1/2) = {r1['w2']:.6f}   (exact: 0.250000)")
    print(f"  w(1/3) = {r1['w3']:.6f}   (exact: 0.111111 = 1/9)")
    print(f"  w(2/3) = {r1['w3b']:.6f}   (should match w(1/3) by symmetry)")
    print()
    err2 = abs(r1['w2'] - 0.25)
    err3 = abs(r1['w3'] - 1.0 / 9.0)
    print(f"  |w(1/2) - 1/4| = {err2:.2e}")
    print(f"  |w(1/3) - 1/9| = {err3:.2e}")
    if err2 < 1e-4:
        print("  ✓ w(1/2) matches exact value")
    else:
        print(f"  ✗ w(1/2) off by {err2:.6f}")
    if err3 < 1e-4:
        print("  ✓ w(1/3) matches exact value")
    else:
        print(f"  ✗ w(1/3) off by {err3:.6f}")
    print()

    # ── SM running comparison ────────────────────────────────────────────────
    print("SM coupling running (one-loop):")
    print(f"  α_s(M_Z) = {ALPHA_S_MZ}")
    print(f"  α₂(M_Z) = {ALPHA_2_MZ:.6f}")
    print(f"  α_s/α₂(M_Z) = {ALPHA_S_MZ / ALPHA_2_MZ:.6f}")
    print()

    ref_scales = [91.2, 200, 1000, 1e4, 1e6, 1e10, 1e16]
    print(f"  {'μ [GeV]':>12s}  {'α_s':>10s}  {'α₂':>10s}  {'α_s/α₂':>10s}")
    print(f"  {'-' * 48}")
    for mu in ref_scales:
        a_s = alpha_s(mu)
        a_2 = alpha_2(mu)
        print(f"  {mu:12.1f}  {a_s:10.6f}  {a_2:10.6f}  {a_s / a_2:10.6f}")
    print()

    # ── Duty ratio at K=1 ────────────────────────────────────────────────────
    print("Key result at K = 1 (critical line):")
    print(f"  duty(2) = w(1/2)/2 = {r1['duty2']:.6f}")
    print(f"  duty(3) = w(1/3)/3 = {r1['duty3']:.6f}")
    print(f"  duty(2)/duty(3) = {r1['ratio']:.6f}")
    mu_k1 = find_mu_for_ratio(r1['ratio'])
    print(f"  SM scale where α_s/α₂ matches: μ = {mu_k1:.2e} GeV")
    print()


if __name__ == "__main__":
    main()
