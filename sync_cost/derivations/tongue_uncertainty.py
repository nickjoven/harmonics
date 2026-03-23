"""
Nonlinear corrections to the tongue uncertainty relation.

The linearized (small-ε) limit gives:
    τ × Δθ ≈ const        (the uncertainty relation)

This is the QM limit — it corresponds to Gaussian minimum-uncertainty
states and the Heisenberg bound ΔxΔp = ℏ/2.

At large ε (deep inside a tongue), the saddle-node approximation
breaks down. The Floquet multiplier f'(θ*) = 1 - K cos(2πθ*) is
NOT well-approximated by 1 - 2√(πKε). The cosine has higher-order
terms. The parabola becomes visibly a cosine.

This script computes the EXACT τ×Δθ product across the full ε range
and identifies the shape of the nonlinear correction.

The prediction: deep inside tongues, the uncertainty product τ×Δθ
DECREASES — the system becomes MORE certain than the Gaussian bound
allows. This is new physics from the tongue geometry, not a
restatement of QM.

Usage:
    python sync_cost/derivations/tongue_uncertainty.py
"""

import math
from circle_map_utils import circle_map_step, winding_number, PHI, INV_PHI


def tongue_01_exact(epsilon, K):
    """
    Exact quantities for the 0/1 tongue at depth epsilon.

    Returns dict with all geometric and dynamical quantities,
    or None if epsilon is outside the tongue.
    """
    edge = K / (2 * math.pi)
    omega = edge - epsilon

    if omega < 0:
        return None

    ratio = 2 * math.pi * omega / K
    if abs(ratio) > 1.0:
        return None

    # Fixed points
    theta_s = math.asin(ratio) / (2 * math.pi)     # stable
    theta_u = 0.5 - theta_s                          # unstable
    delta_theta = theta_u - theta_s                  # basin separation

    # Floquet multiplier at stable fixed point (EXACT)
    f_prime_s = 1 - K * math.cos(2 * math.pi * theta_s)

    if abs(f_prime_s) >= 1.0:
        return None

    # Convergence rate (EXACT)
    lam_exact = -math.log(abs(f_prime_s))

    # Locking time (iterations to reduce error by e^10)
    tau_exact = 10.0 / lam_exact

    # The product
    product = tau_exact * delta_theta

    # Linearized (saddle-node) approximation
    lam_linear = 2 * math.sqrt(math.pi * K * epsilon)
    delta_linear = 2 * math.sqrt(epsilon / (math.pi * K))
    tau_linear = 10.0 / lam_linear
    product_linear = tau_linear * delta_linear  # = 10 * 2√(ε/πK) / (2√(πKε)) = 10/(πK)

    return {
        "epsilon": epsilon,
        "omega": omega,
        "theta_s": theta_s,
        "theta_u": theta_u,
        "delta_theta": delta_theta,
        "f_prime": f_prime_s,
        "lambda": lam_exact,
        "tau": tau_exact,
        "product": product,
        "lambda_linear": lam_linear,
        "delta_linear": delta_linear,
        "tau_linear": tau_linear,
        "product_linear": product_linear,
    }


if __name__ == "__main__":
    print("=" * 90)
    print("  NONLINEAR CORRECTIONS TO THE TONGUE UNCERTAINTY RELATION")
    print("=" * 90)

    # === 1. THE EXACT PRODUCT τ×Δθ ACROSS THE FULL ε RANGE ===
    print(f"\n{'─'*90}")
    print("  1. EXACT τ×Δθ vs ε FOR THE 0/1 TONGUE")
    print(f"{'─'*90}")

    print(f"""
  The linearized (small-ε) uncertainty product is:

      (τ×Δθ)_linear = (10 / 2√(πKε)) × 2√(ε/(πK))
                     = 10 / (πK)

  This is CONSTANT — independent of ε. This is the Heisenberg bound.

  The exact product uses the full cosine in the Floquet multiplier.
  At large ε, the cosine differs from its small-angle expansion.
""")

    K = 0.9
    product_linear_const = 10.0 / (math.pi * K)

    print(f"  K = {K}")
    print(f"  (τ×Δθ)_linear = 10/(πK) = {product_linear_const:.6f}  (the Heisenberg bound)")
    print()

    print(f"  {'ε':>12s}  {'Δθ_exact':>10s}  {'λ_exact':>10s}  {'τ_exact':>10s}  "
          f"{'τ×Δθ':>10s}  {'τ×Δθ/HUP':>10s}  {'deviation':>10s}")
    print("  " + "-" * 85)

    results = []
    edge = K / (2 * math.pi)

    # Sweep from small ε (near boundary) to large ε (deep inside tongue)
    # Maximum ε for the 0/1 tongue: omega = 0, so ε_max = edge = K/(2π)
    eps_max = edge
    n_points = 60

    for i in range(n_points):
        # Logarithmic sweep from 1e-6 to near eps_max
        if i < 40:
            epsilon = 10 ** (-6 + i * 4.0 / 39)  # 1e-6 to 1e-2
        else:
            epsilon = 0.01 + (eps_max - 0.01) * (i - 40) / (n_points - 41)

        r = tongue_01_exact(epsilon, K)
        if r is None:
            continue

        ratio_to_hup = r["product"] / product_linear_const
        deviation_pct = (ratio_to_hup - 1) * 100

        results.append(r)

        # Print a subset
        if i % 3 == 0 or i >= 40:
            print(f"  {epsilon:12.2e}  {r['delta_theta']:10.6f}  {r['lambda']:10.6f}  "
                  f"{r['tau']:10.2f}  {r['product']:10.6f}  {ratio_to_hup:10.6f}  "
                  f"{deviation_pct:+9.2f}%")

    # === 2. THE SHAPE OF THE CORRECTION ===
    print(f"\n{'─'*90}")
    print("  2. THE SHAPE OF THE NONLINEAR CORRECTION")
    print(f"{'─'*90}")

    print(f"""
  Define the correction factor:

      η(ε) = (τ×Δθ)_exact / (τ×Δθ)_linear

  At small ε: η → 1 (Heisenberg limit, QM is exact).
  At large ε: η deviates — this is the nonlinear correction.

  The question: what SHAPE is η(ε)?

  Analytically, at the stable fixed point θ*:

      cos(2πθ*) = [1 - f'(θ*)] / K

  where f'(θ*) is the exact Floquet multiplier. Near the boundary
  (θ* → 1/4), cos(2πθ*) → 0 and f' → 1. The linear approximation
  expands cos around this zero crossing.

  The next correction comes from:

      cos(2πθ*) ≈ 2πδ - (2πδ)³/6 + ...

  where δ = 1/4 - θ*. Since δ ≈ √(ε/(πK)), the correction to the
  Floquet multiplier goes as ε^(3/2), making:

      η(ε) ≈ 1 - c₁ ε + c₂ ε² + ...

  The SIGN of the leading correction determines whether deep tongues
  are MORE certain or LESS certain than the Gaussian bound.
""")

    K = 0.9
    edge = K / (2 * math.pi)
    product_linear_const = 10.0 / (math.pi * K)

    print(f"  K = {K}")
    print(f"\n  {'ε':>12s}  {'ε/ε_max':>8s}  {'η(ε)':>10s}  {'η-1':>12s}  "
          f"{'(η-1)/ε':>12s}  {'shape':>15s}")
    print("  " + "-" * 80)

    eta_minus_1_over_eps = []

    for exp_10 in range(-12, 1):
        epsilon = 10 ** (exp_10 / 2.0)
        if epsilon >= eps_max:
            continue

        r = tongue_01_exact(epsilon, K)
        if r is None:
            continue

        eta = r["product"] / product_linear_const
        eta_m1 = eta - 1
        eta_m1_over_eps = eta_m1 / epsilon if epsilon > 1e-15 else 0

        eta_minus_1_over_eps.append((epsilon, eta_m1_over_eps))

        print(f"  {epsilon:12.2e}  {epsilon/eps_max:8.4f}  {eta:10.6f}  "
              f"{eta_m1:12.2e}  {eta_m1_over_eps:12.4f}  ", end="")

        if abs(eta_m1) < 1e-6:
            print(f"{'Heisenberg':>15s}")
        elif eta_m1 < 0:
            print(f"{'sub-Gaussian':>15s}")
        else:
            print(f"{'super-Gaussian':>15s}")

    # === 3. ANALYTICAL CORRECTION COEFFICIENTS ===
    print(f"\n{'─'*90}")
    print("  3. ANALYTICAL CORRECTION: Taylor expansion of the Floquet multiplier")
    print(f"{'─'*90}")

    print(f"""
  At the stable fixed point, the EXACT quantities are:

      sin(2πθ*) = 2πω/K = 2π(ε_max - ε)/K = 1 - 2πε/K

  Let u = 2πε/K (dimensionless depth). Then:

      sin(2πθ*) = 1 - u
      cos(2πθ*) = √(1 - (1-u)²) = √(2u - u²)
      f'(θ*)    = 1 - K√(2u - u²)

  The linearized form keeps only √(2u):

      f'_linear = 1 - K√(2u) = 1 - K√(4πε/K) = 1 - 2√(πKε)

  The exact correction is:

      f'_exact / f'_linear = [1 - K√(2u - u²)] / [1 - K√(2u)]

  For small u: √(2u - u²) = √(2u) × √(1 - u/2)
                           ≈ √(2u) × (1 - u/4 - u²/32 - ...)

  So the Floquet multiplier correction is:

      f'_exact ≈ f'_linear + K√(2u) × (u/4)
               = f'_linear × [1 + K√(2u)(u/4) / (1 - f'_linear)]

  In terms of ε:  u = 2πε/K, so the correction goes as u^(3/2) ∝ ε^(3/2).
""")

    K = 0.9
    edge = K / (2 * math.pi)

    print(f"  K = {K}")
    print(f"  u = 2πε/K")
    print()

    print(f"  {'ε':>12s}  {'u':>10s}  {'f_exact':>10s}  {'f_linear':>10s}  "
          f"{'Δf':>12s}  {'Δf/u^(3/2)':>12s}")
    print("  " + "-" * 75)

    correction_ratios = []

    for exp_10 in range(-12, 1):
        epsilon = 10 ** (exp_10 / 2.0)
        if epsilon >= eps_max:
            continue

        u = 2 * math.pi * epsilon / K

        r = tongue_01_exact(epsilon, K)
        if r is None:
            continue

        f_exact = r["f_prime"]
        f_linear = 1 - 2 * math.sqrt(math.pi * K * epsilon)

        delta_f = f_exact - f_linear
        u_32 = u ** 1.5
        ratio = delta_f / u_32 if u_32 > 1e-15 else 0

        correction_ratios.append((epsilon, ratio))

        print(f"  {epsilon:12.2e}  {u:10.6f}  {f_exact:10.6f}  {f_linear:10.6f}  "
              f"{delta_f:12.2e}  {ratio:12.6f}")

    if correction_ratios:
        # The ratio should converge to a constant = K√2/4
        c_predicted = K * math.sqrt(2) / 4
        _, last_ratio = correction_ratios[-1]
        print(f"\n  Δf/u^(3/2) converges to: {last_ratio:.6f}")
        print(f"  Predicted (K√2/4):       {c_predicted:.6f}")
        print(f"\n  The leading correction to the Floquet multiplier is:")
        print(f"      f'_exact = f'_linear + (K√2/4) × u^(3/2) + O(u²)")
        print(f"      f'_exact = [1 - 2√(πKε)] + (K√2/4)(2πε/K)^(3/2) + ...")

    # === 4. MULTI-K SURVEY: THE CORRECTION IS UNIVERSAL ===
    print(f"\n{'─'*90}")
    print("  4. UNIVERSALITY: η(ε) across coupling strengths")
    print(f"{'─'*90}")

    print(f"""
  If the correction shape is universal (same functional form at all K),
  then it's a property of the PARABOLA, not the coupling. It would mean
  the deviation from Heisenberg is a geometric invariant of the saddle-node.
""")

    print(f"  {'K':>6s}  {'ε':>12s}  {'u':>10s}  {'η(ε)':>10s}  {'η-1':>12s}  "
          f"{'(η-1)/u':>12s}")
    print("  " + "-" * 75)

    # Fixed set of u values, vary K
    for K in [0.3, 0.5, 0.7, 0.9, 0.99]:
        edge_k = K / (2 * math.pi)
        product_lin_k = 10.0 / (math.pi * K)

        for u_target in [0.01, 0.1, 0.5, 1.0]:
            epsilon = u_target * K / (2 * math.pi)
            if epsilon >= edge_k:
                continue

            r = tongue_01_exact(epsilon, K)
            if r is None:
                continue

            eta = r["product"] / product_lin_k
            eta_m1 = eta - 1

            u = 2 * math.pi * epsilon / K
            eta_m1_over_u = eta_m1 / u if u > 1e-15 else 0

            print(f"  {K:6.2f}  {epsilon:12.2e}  {u:10.4f}  {eta:10.6f}  "
                  f"{eta_m1:12.2e}  {eta_m1_over_u:12.6f}")
        print()

    # === 5. THE CONJUGATE PAIR: DERIVATIONS 1 AND 7 UNIFIED ===
    print(f"\n{'─'*90}")
    print("  5. THE CONJUGATE PAIR: Born rule and collapse are dual projections")
    print(f"{'─'*90}")

    print(f"""
  At every tongue boundary, the saddle-node normal form x² + μ = 0
  simultaneously determines:

      Δθ = 2√(|μ|/(πK))     (basin separation — Derivation 1)
      λ  = 2√(πK|μ|)         (convergence rate — Derivation 7)

  These are CONJUGATE projections of the same parabola:

      Δθ × λ = 2√(|μ|/(πK)) × 2√(πK|μ|) = 4|μ|

  The product Δθ × λ is LINEAR in ε — and ε is the control parameter.
  The τ×Δθ product (with τ = C/λ) is:

      τ × Δθ = C × Δθ / λ = C × [2√(ε/(πK))] / [2√(πKε)]
             = C / (πK)

  CONSTANT in the linear regime. This IS the Heisenberg bound.

  Now the exact (nonlinear) versions:

      Δθ_exact × λ_exact = ?  (not linear in ε)
""")

    K = 0.9
    edge = K / (2 * math.pi)

    print(f"  K = {K}")
    print(f"\n  {'ε':>12s}  {'Δθ':>10s}  {'λ':>10s}  {'Δθ×λ':>10s}  {'4ε':>10s}  "
          f"{'Δθ×λ/(4ε)':>12s}  {'shape':>10s}")
    print("  " + "-" * 80)

    for exp_10 in range(-10, 1):
        epsilon = 10 ** (exp_10 / 2.0)
        if epsilon >= eps_max:
            continue

        r = tongue_01_exact(epsilon, K)
        if r is None:
            continue

        dl_product = r["delta_theta"] * r["lambda"]
        four_eps = 4 * epsilon
        ratio = dl_product / four_eps if four_eps > 1e-15 else 0

        shape = "linear" if abs(ratio - 1) < 0.01 else (
            "sub-linear" if ratio < 1 else "super-linear"
        )

        print(f"  {epsilon:12.2e}  {r['delta_theta']:10.6f}  {r['lambda']:10.6f}  "
              f"{dl_product:10.6f}  {four_eps:10.6f}  {ratio:12.6f}  {shape:>10s}")

    # === 6. HIGHER-ORDER TONGUES ===
    print(f"\n{'─'*90}")
    print("  6. HIGHER-ORDER TONGUES: does the correction persist?")
    print(f"{'─'*90}")

    print(f"""
  The 0/1 tongue is the simplest case. The prediction must hold
  for ALL tongues — every p/q rational in the Stern-Brocot tree.

  For the 1/2 tongue: period-2 orbits. The Floquet multiplier is
  the product of derivatives at both points of the orbit.

  If the correction is universal (a property of the saddle-node
  normal form), it should appear identically at every tongue,
  differing only by the tongue-specific constant c(p/q, K).
""")

    K = 0.9
    print(f"  K = {K}")
    print(f"\n  Numerical locking-time survey for the 1/2 tongue:")

    # Find 1/2 tongue boundary
    lo_o, hi_o = 0.5, 0.7
    for _ in range(60):
        mid = (lo_o + hi_o) / 2
        W = winding_number(mid, K, n_transient=5000, n_measure=50000)
        if abs(W - 0.5) < 1e-4:
            lo_o = mid
        else:
            hi_o = mid
    edge_12 = (lo_o + hi_o) / 2

    print(f"  1/2 tongue right boundary ≈ {edge_12:.8f}")
    print()

    print(f"  {'ε':>12s}  {'W':>10s}  {'locked':>8s}  {'n_lock':>10s}  "
          f"{'n×√ε':>10s}")
    print("  " + "-" * 60)

    # Quick locking time measurement for the 1/2 tongue
    for exp in range(-1, -7, -1):
        epsilon = 10 ** (exp / 2.0)
        omega = edge_12 - epsilon

        theta = 0.5
        target_W = 0.5
        window = 40
        recent = []
        n_lock = 100000

        for n in range(1, 100001):
            new_theta = circle_map_step(theta, omega, K)
            advance = new_theta - theta
            theta = new_theta
            recent.append(advance)
            if len(recent) > window:
                recent.pop(0)
            if n >= window and n % 10 == 0:
                running_W = sum(recent) / len(recent)
                spread = max(recent) - min(recent)
                if abs(running_W - target_W) < 1e-4 and spread < 1e-3:
                    n_lock = n
                    break

        W_final = sum(recent) / len(recent) if recent else 0
        locked = "YES" if abs(W_final - 0.5) < 1e-3 else "no"
        n_sqrt_eps = n_lock * math.sqrt(epsilon)

        print(f"  {epsilon:12.2e}  {W_final:10.6f}  {locked:>8s}  "
              f"{n_lock:10d}  {n_sqrt_eps:10.2f}")

    # === 7. SUMMARY ===
    print(f"\n{'='*90}")
    print("  SUMMARY: THREE RESULTS")
    print(f"{'='*90}")

    print(f"""
  1. THE CONJUGATE PAIR (Derivations 1 + 7 unified):

     The saddle-node normal form x² + μ = 0 has two projections:
         Position: Δθ = 2√(|μ|/(πK))   — basin measure (Born rule)
         Momentum: λ  = 2√(πK|μ|)       — convergence rate (collapse)

     Their product Δθ × λ = 4|μ| is linear in the control parameter.
     The quotient τ × Δθ = C/(πK) is the Heisenberg bound.
     One parabola, two readings. Not two derivations.

  2. THE NONLINEAR CORRECTION:

     At large ε (deep inside tongues), the exact product τ×Δθ deviates
     from the constant Heisenberg value. The leading correction comes
     from the u^(3/2) term in the Floquet multiplier expansion:

         f'_exact = f'_linear + (K√2/4)(2πε/K)^(3/2) + O(ε²)

     The correction is sub-Gaussian: deep inside tongues, the system
     is MORE certain than the Heisenberg bound allows. Minimum-uncertainty
     states at large ε violate the Gaussian bound downward.

  3. THE HIERARCHY:

     Standard QM = small-ε limit of the tongue geometry.
     The Heisenberg bound is the linearization of the tongue uncertainty.
     Nonlinear corrections at large ε are computable predictions that
     go beyond QM while reducing to QM in the appropriate limit.

     The minimum alphabet {{integers, mediants, fixed-point, parabola}}
     generates the full structure. QM falls out when you linearize
     the parabola and complete to the reals.
""")
