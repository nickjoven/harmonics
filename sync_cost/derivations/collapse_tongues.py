"""
Measurement collapse from tongue traversal.

In the circle map picture:
- A quantum state is a point (Ω, K) in the parameter plane
- "Superposition" = sitting in the gap between tongues (unlocked,
  quasiperiodic orbit, no definite winding number)
- "Measurement" = a coupling event that changes K (coupling strength)
  or Ω (frequency), pushing the system into a tongue
- "Collapse" = the transient from quasiperiodic to mode-locked
- "Born rule" = which tongue you land in (basin measure ∝ |ψ|²)

Key insight: collapse has DURATION, not a timestamp. The time to
lock into a tongue after crossing its boundary depends on:
  1. How deep inside the tongue you end up (depth ε)
  2. The coupling strength K
  3. The period q of the target tongue

Near a tongue boundary, the locking time diverges as:
    τ_lock ∝ 1/√ε

This is the INVERSE of the Born rule scaling (Δθ ∝ √ε):
- Deep inside a tongue: fast locking, large basin (high probability)
- Near the boundary: slow locking, small basin (low probability)
- AT the boundary: infinite locking time, zero basin (zero probability)

The locking time × basin size product is CONSTANT:
    τ_lock × Δθ = const

This is an uncertainty relation: measurement precision × collapse
duration = constant. You can't have both fast collapse and sharp
discrimination between nearby outcomes.

Usage:
    python sync_cost/derivations/collapse_tongues.py
"""

import math
from circle_map_utils import circle_map_step, winding_number, PHI, INV_PHI


def locking_time(omega, K, target_W, tol=1e-6, max_steps=200000):
    """
    How many iterations until the orbit converges to the mode-locked
    fixed point?

    For a period-1 orbit (target_W near integer), we track when the
    per-step advance stabilizes. For the 0/1 tongue, the fixed point
    satisfies Ω = (K/2π)sin(2πθ*), and convergence is exponential
    with rate λ = ln|f'(θ*)|.

    We measure convergence by tracking the per-step advance and
    detecting when it stabilizes to target_W.

    Returns (n_lock, final_W).
    """
    theta = 0.5  # start away from the fixed point
    window = 20  # small window for quick detection
    recent = []

    for n in range(1, max_steps + 1):
        new_theta = theta + omega - K / (2 * math.pi) * math.sin(2 * math.pi * theta)
        advance = new_theta - theta
        theta = new_theta

        recent.append(advance)
        if len(recent) > window:
            recent.pop(0)

        if n >= window and n % 5 == 0:
            running_W = sum(recent) / len(recent)
            spread = max(recent) - min(recent)
            if abs(running_W - target_W) < tol and spread < tol * 10:
                return n, running_W

    final_W = sum(recent) / len(recent) if recent else 0
    return max_steps, final_W


def tongue_01_boundary(K):
    """Right boundary of the 0/1 tongue."""
    return K / (2 * math.pi)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 85)
    print("  MEASUREMENT COLLAPSE FROM TONGUE TRAVERSAL")
    print("=" * 85)

    # === 1. LOCKING TIME vs DEPTH ===
    print(f"\n{'─'*85}")
    print("  1. LOCKING TIME vs TONGUE DEPTH (0/1 tongue)")
    print(f"{'─'*85}")

    K = 0.9
    edge = tongue_01_boundary(K)

    print(f"\n  K = {K},  tongue boundary Ω_edge = {edge:.8f}")
    print(f"\n  Collapse = time to lock after entering the tongue.")
    print(f"  Expect: τ_lock ∝ 1/√ε  (inverse of Born rule scaling)")
    print(f"\n  {'ε':>12s}  {'τ_lock':>10s}  {'Δθ':>10s}  {'τ×Δθ':>10s}  "
          f"{'τ×√ε':>10s}  {'1/√ε':>10s}")
    print("  " + "-" * 75)

    # ANALYTICAL locking rate for the 0/1 tongue:
    # The fixed point satisfies Ω = (K/2π)sin(2πθ*)
    # The Floquet multiplier is f'(θ*) = 1 - K cos(2πθ*)
    # Near the boundary (θ* ≈ 1/4): cos(2πθ*) ≈ 2πδ where δ = 1/4 - θ*
    # δ ≈ √(ε/(πK)), so f' ≈ 1 - 2√(πKε)
    # Convergence rate: λ = -ln|f'| ≈ 2√(πKε)  for small ε
    # Locking time:     τ = C/λ = C/(2√(πKε)) ∝ 1/√ε
    #
    # C depends on initial distance and tolerance.

    print(f"\n  ANALYTICAL (0/1 tongue, stable fixed point at θ_s):")
    hdr_fp = "|f'(θ*)|"
    hdr_lam = "λ=-ln|f'|"
    print(f"\n  {'ε':>12s}  {hdr_fp:>10s}  {hdr_lam:>12s}  "
          f"{'τ=10/λ':>10s}  {'Δθ':>10s}  {'τ×Δθ':>10s}  {'τ×√ε':>10s}")
    print("  " + "-" * 85)

    for exp in range(-1, -13, -1):
        epsilon = 10 ** (exp / 2.0)
        omega = edge - epsilon

        ratio = 2 * math.pi * omega / K
        if abs(ratio) > 1.0:
            continue

        theta_s = math.asin(ratio) / (2 * math.pi)
        delta_theta = 0.5 - 2 * theta_s

        # Floquet multiplier at the STABLE fixed point
        f_prime = 1 - K * math.cos(2 * math.pi * theta_s)

        if abs(f_prime) >= 1.0:
            continue

        lam = -math.log(abs(f_prime))  # convergence rate per iteration
        tau = 10.0 / lam  # time to reduce error by factor e^10 ≈ 22000

        tau_delta = tau * delta_theta
        tau_sqrt_eps = tau * math.sqrt(epsilon)

        print(f"  {epsilon:12.2e}  {abs(f_prime):10.6f}  {lam:12.6f}  "
              f"{tau:10.2f}  {delta_theta:10.6f}  {tau_delta:10.4f}  "
              f"{tau_sqrt_eps:10.4f}")

    # === 2. LOCKING TIME FOR DIFFERENT TONGUES ===
    print(f"\n{'─'*85}")
    print("  2. LOCKING TIME DEPENDS ON TONGUE ORDER q")
    print(f"{'─'*85}")

    print(f"""
  Higher-order tongues (larger q in p/q) take LONGER to lock.
  A period-q orbit needs q iterations to complete one cycle,
  so locking time scales with q.

  This means: collapsing to a "high-q" outcome (fine-grained
  measurement) takes longer than collapsing to a "low-q" outcome
  (coarse measurement). The measurement apparatus's coupling time
  determines which tongues are accessible.
""")

    K = 0.9
    epsilon = 0.005  # fixed depth inside tongue

    print(f"  K = {K},  ε = {epsilon}")
    print(f"\n  {'tongue':>8s}  {'Ω_center':>10s}  {'Ω_test':>10s}  "
          f"{'τ_lock':>10s}  {'W_final':>10s}  {'locked?':>8s}")
    print("  " + "-" * 70)

    test_tongues = [(0, 1), (1, 3), (1, 2), (2, 3), (2, 5), (3, 5)]

    for p, q in test_tongues:
        target = p / q
        # Test slightly inside the tongue (toward center)
        omega_test = target + epsilon * (0.5 - target) / abs(0.5 - target + 1e-10)
        # Simpler: just offset from center
        omega_test = target - epsilon if target > 0.5 else target + epsilon

        target_W = target  # exact rational
        n_lock, final_W = locking_time(omega_test, K, target_W, tol=1e-4,
                                        max_steps=100000)

        locked = "YES" if abs(final_W - target_W) < 1e-3 else "no"
        print(f"  {p}/{q:>2d}      {target:10.6f}  {omega_test:10.6f}  "
              f"{n_lock:10d}  {final_W:10.6f}  {locked:>8s}")

    # === 3. THE UNCERTAINTY RELATION ===
    print(f"\n{'─'*85}")
    print("  3. THE COLLAPSE UNCERTAINTY RELATION")
    print(f"{'─'*85}")

    print(f"""
  From the Born rule: Δθ ∝ √ε  (basin size grows with depth)
  From collapse:      τ  ∝ 1/√ε (locking time shrinks with depth)

  Therefore:          τ × Δθ = const

  This is a measurement uncertainty relation:
      (collapse duration) × (basin discrimination) = constant

  You cannot have BOTH:
      - fast collapse (quick measurement), AND
      - fine discrimination (distinguishing nearby tongues)

  Deep inside a tongue: fast, certain, coarse
  Near the boundary: slow, uncertain, fine

  At the boundary itself (ε → 0):
      Δθ → 0   (no basin — zero probability)
      τ → ∞    (never locks — eternal superposition)

  This is the quantum Zeno effect: continuously measuring
  prevents collapse by keeping the system at the tongue boundary.
""")

    K = 0.9
    edge = tongue_01_boundary(K)

    print(f"  Numerical check (0/1 tongue, K = {K}):")
    print(f"\n  {'ε':>12s}  {'τ':>10s}  {'Δθ':>10s}  {'τ×Δθ':>12s}  {'τ×Δθ²':>12s}")
    print("  " + "-" * 65)

    products = []
    for exp in range(-1, -8, -1):
        epsilon = 10 ** (exp / 2.0)
        omega = edge - epsilon

        n_lock, _ = locking_time(omega, K, target_W=0.0, tol=1e-5)

        ratio = 2 * math.pi * omega / K
        if abs(ratio) <= 1.0:
            a = math.asin(ratio) / (2 * math.pi)
            delta = 0.5 - 2 * a
        else:
            delta = 0

        product = n_lock * delta
        product2 = n_lock * delta**2
        products.append(product)

        print(f"  {epsilon:12.2e}  {n_lock:10d}  {delta:10.6f}  "
              f"{product:12.2f}  {product2:12.4f}")

    if len(products) >= 2:
        avg = sum(products) / len(products)
        spread = max(products) - min(products)
        print(f"\n  τ×Δθ range: {min(products):.1f} to {max(products):.1f}")
        print(f"  If τ×Δθ were exactly constant, spread would be 0.")
        print(f"  Actual spread: {spread:.1f} (from {min(products):.1f})")

    # === 4. SUPERPOSITION = GAP BETWEEN TONGUES ===
    print(f"\n{'─'*85}")
    print("  4. SUPERPOSITION = THE GAP BETWEEN TONGUES")
    print(f"{'─'*85}")

    print(f"""
  At subcritical coupling (K < 1), the devil's staircase has GAPS
  between tongues. In these gaps, the orbit is quasiperiodic — it
  never locks to any rational. No definite winding number.

  This IS superposition in the synchronization picture:
      - The system has no definite "outcome" (no locked winding number)
      - It participates in multiple tongues' basins simultaneously
      - The basin measure |ψ|² determines which tongue it WOULD lock
        to if coupling increased

  Measurement = increasing K (coupling to apparatus) until the gap
  closes and the system falls into a tongue.

  The gap width at 1/φ (the golden ratio) is the WIDEST gap in the
  staircase. It is the last to close as K → 1. This means:

      The "most quantum" state — the hardest to collapse — is the
      one at frequency 1/φ. It is maximally resistant to measurement.

  KAM theory says the same thing: the golden torus is the LAST to
  break under perturbation. The synchronization framework gives
  this a probability interpretation via the Born rule.
""")

    # Gap widths at 1/φ for different K
    print(f"  Gap width at 1/φ vs coupling K:")
    print(f"\n  {'K':>6s}  {'W(1/φ)':>12s}  {'W - 1/φ':>12s}  {'gap?':>12s}")
    print("  " + "-" * 50)

    for K_10 in range(0, 11):
        K = K_10 / 10.0
        if K < 0.01:
            K = 0.01
        W = winding_number(INV_PHI, K, n_transient=10000, n_measure=100000)
        gap = abs(W - INV_PHI)
        # 1/φ is irrational — it should NEVER mode-lock (at K < 1)
        # Small gaps are numerical noise; true locking would show gap >> 1e-3
        status = "quasiperiodic" if gap < 5e-3 else f"LOCKED ({W:.4f})"
        print(f"  {K:6.2f}  {W:12.8f}  {gap:12.2e}  {status:>12s}")

    # === 5. COLLAPSE DURATION IS PHYSICAL ===
    print(f"\n{'─'*85}")
    print("  5. COLLAPSE DURATION IS PHYSICAL AND TESTABLE")
    print(f"{'─'*85}")

    print(f"""
  The framework (FRAMEWORK.md) states:
      "Collapse has duration, not a timestamp."

  The tongue traversal picture makes this concrete:

  1. BEFORE measurement: system at (Ω, K₀) in a gap (superposition)
  2. MEASUREMENT begins: K increases (coupling to apparatus)
  3. AT K_critical: tongue boundary reaches the system's Ω
  4. DURING collapse: transient from quasiperiodic to mode-locked
     Duration τ ∝ 1/√ε where ε = depth past the boundary
  5. AFTER collapse: stably mode-locked (definite outcome)

  The collapse duration τ depends on:
      - How fast K increases (measurement strength)
      - Which tongue the system enters (outcome selected)
      - How deep past the boundary (measurement precision)

  Testable prediction: systems coupled at the MINIMUM strength
  to trigger collapse (ε → 0, near tongue boundary) should show
  anomalously long decoherence times. This is not the quantum Zeno
  effect (which prevents collapse entirely) but a SLOW collapse
  near threshold.

  The Stribeck lattice shows this: at A ≈ 0.8 (the bifurcation
  threshold), the transition between stick and slip regimes takes
  longer than deep in either regime. The transient duration peaks
  at the boundary — exactly as the tongue picture predicts.
""")

    # Measure transient duration at different depths
    print(f"  Collapse duration vs measurement strength (0/1 tongue):")
    print(f"\n  {'K_measure':>10s}  {'ε_eff':>10s}  {'τ_lock':>10s}  "
          f"{'regime':>15s}")
    print("  " + "-" * 55)

    omega_test = 0.10  # inside the 0/1 tongue for all K > 0.63

    for K_10 in range(6, 11):
        K = K_10 / 10.0
        edge = tongue_01_boundary(K)
        if omega_test < edge:
            epsilon = edge - omega_test
            n_lock, final_W = locking_time(omega_test, K, target_W=0.0,
                                            tol=1e-5, max_steps=50000)
            regime = "inside tongue"
        else:
            epsilon = omega_test - edge
            n_lock, final_W = locking_time(omega_test, K, target_W=0.0,
                                            tol=1e-5, max_steps=50000)
            regime = "outside tongue"

        print(f"  {K:10.2f}  {epsilon:10.6f}  {n_lock:10d}  {regime:>15s}")

    # === 6. SUMMARY ===
    print(f"\n{'='*85}")
    print("  SUMMARY: COLLAPSE = TONGUE TRAVERSAL")
    print(f"{'='*85}")

    print(f"""
  The tongue geometry gives a complete picture of quantum measurement:

  SUPERPOSITION:  System in a gap between tongues (quasiperiodic orbit)
                  No definite winding number. Multiple outcomes possible.

  MEASUREMENT:    Coupling event changes (Ω, K), pushing toward a tongue.
                  The apparatus provides the coupling increase.

  COLLAPSE:       Transient from quasiperiodic to mode-locked.
                  Has DURATION τ ∝ 1/√ε (not instantaneous).

  BORN RULE:      Which tongue? Basin measure ∝ tongue width ∝ |ψ|².
                  From saddle-node geometry (born_rule_tongues.py).

  UNCERTAINTY:    τ × Δθ ≈ constant.
                  Fast collapse ↔ coarse discrimination.
                  Slow collapse ↔ fine discrimination.

  ZENO EFFECT:    Continuous measurement holds the system at the tongue
                  boundary (ε → 0). Collapse time → ∞. Never locks.

  PLANCK LIMIT:   Tongue structure requires N ≥ 3 coupling stages.
                  Below the Planck scale, no tongues, no collapse,
                  no Born rule (planck_threshold.py).

  Collapse is not mysterious. It is the transient of a driven
  nonlinear oscillator crossing a mode-locking boundary. The
  duration is physical, measurable, and predicted by the same
  geometry that produces |ψ|².
""")
