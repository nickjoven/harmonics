#!/usr/bin/env python3
"""
Kuramoto oscillators on the Klein bottle (3×3 minimum).

Derivation 19: two antiperiodic constraints simultaneously.
Compare with torus (periodic × periodic) and Möbius cylinder
(antiperiodic × periodic without y-reflection).

Klein bottle identification:
    x-direction: θ_{N_x+1, j} = θ_{1, N_y+1-j} + π   (twist + reflect)
    y-direction: θ_{i, N_y+1}  = θ_{i, 1}              (periodic)
"""

import numpy as np


# ── Neighbor maps ─────────────────────────────────────────────────────────────

def neighbors_torus(i, j, Nx, Ny):
    """Periodic in both directions."""
    return [
        ((i - 1) % Nx, j, 0),         # left
        ((i + 1) % Nx, j, 0),         # right
        (i, (j - 1) % Ny, 0),         # down
        (i, (j + 1) % Ny, 0),         # up
    ]


def neighbors_klein(i, j, Nx, Ny):
    """Klein bottle: antiperiodic+reflect in x, periodic in y."""
    nbrs = []

    # left
    if i > 0:
        nbrs.append((i - 1, j, 0))
    else:
        # wrap: (0, j) -> (Nx-1, Ny-1-j) with -π
        nbrs.append((Nx - 1, Ny - 1 - j, -np.pi))

    # right
    if i < Nx - 1:
        nbrs.append((i + 1, j, 0))
    else:
        # wrap: (Nx-1, j) -> (0, Ny-1-j) with +π
        nbrs.append((0, Ny - 1 - j, np.pi))

    # down (periodic in y)
    nbrs.append((i, (j - 1) % Ny, 0))

    # up (periodic in y)
    nbrs.append((i, (j + 1) % Ny, 0))

    return nbrs


# ── Dynamics ──────────────────────────────────────────────────────────────────

def kuramoto_2d(theta, omega, K, Nx, Ny, neighbor_func):
    """General 2D Kuramoto with arbitrary neighbor map."""
    dtheta = omega.copy()
    for i in range(Nx):
        for j in range(Ny):
            for ni, nj, shift in neighbor_func(i, j, Nx, Ny):
                dtheta[i, j] += (K / 4) * np.sin(
                    theta[ni, nj] + shift - theta[i, j]
                )
    return dtheta


def rk4_step_2d(theta, omega, K, Nx, Ny, neighbor_func, dt):
    f = lambda th: kuramoto_2d(th, omega, K, Nx, Ny, neighbor_func)
    k1 = f(theta)
    k2 = f(theta + 0.5 * dt * k1)
    k3 = f(theta + 0.5 * dt * k2)
    k4 = f(theta + dt * k3)
    return theta + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)


# ── Observables ───────────────────────────────────────────────────────────────

def order_parameter_2d(theta):
    """Global order parameter."""
    z = np.exp(1j * theta)
    return np.abs(z.mean())


def phase_gradients(theta, Nx, Ny):
    """Average phase gradient in x and y directions."""
    dx = np.zeros((Nx, Ny))
    dy = np.zeros((Nx, Ny))
    for i in range(Nx):
        for j in range(Ny):
            # x-gradient (ignore boundary effects for interior)
            i_next = (i + 1) % Nx
            dx[i, j] = theta[i_next, j] - theta[i, j]
            # y-gradient
            j_next = (j + 1) % Ny
            dy[i, j] = theta[i, j_next] - theta[i, j]

    # Wrap to [-π, π]
    dx = (dx + np.pi) % (2 * np.pi) - np.pi
    dy = (dy + np.pi) % (2 * np.pi) - np.pi

    return dx.mean(), dy.mean()


def detect_rational(val, tol=0.08):
    """Check if val/(2π) is near a simple rational."""
    x = (val % (2 * np.pi)) / (2 * np.pi)
    if x > 0.5:
        x = 1 - x
    for p, q in [(0, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
                  (2, 5), (2, 3), (3, 4), (3, 5), (3, 8), (5, 8)]:
        if abs(x - p / q) < tol:
            return f"{p}/{q}"
    return None


# ── Simulation ────────────────────────────────────────────────────────────────

def run_sim(Nx, Ny, K, neighbor_func, label, gamma=1.0, epsilon=0.1,
            dt=0.01, T=200.0, seed=42):
    """Run one simulation on the 2D lattice."""
    rng = np.random.default_rng(seed)

    omega = gamma * np.clip(rng.standard_cauchy((Nx, Ny)), -10, 10)
    theta = np.zeros((Nx, Ny))
    theta[0, 0] = epsilon  # single perturbation

    n_steps = int(T / dt)
    r_hist = np.zeros(n_steps)

    for step in range(n_steps):
        r_hist[step] = order_parameter_2d(theta)
        theta = rk4_step_2d(theta, omega, K, Nx, Ny, neighbor_func, dt)

    r_final = order_parameter_2d(theta)
    grad_x, grad_y = phase_gradients(theta, Nx, Ny)

    print(f"\n  [{label}] Nx={Nx}, Ny={Ny}, K={K:.2f}")
    print(f"    r(final) = {r_final:.4f}")
    print(f"    <∂θ/∂x> = {grad_x:.4f}  ({grad_x/(2*np.pi):.4f} × 2π)"
          f"  {detect_rational(grad_x) or ''}")
    print(f"    <∂θ/∂y> = {grad_y:.4f}  ({grad_y/(2*np.pi):.4f} × 2π)"
          f"  {detect_rational(grad_y) or ''}")

    if abs(grad_y) > 0.01:
        ratio = grad_x / grad_y
        print(f"    gradient ratio ∂x/∂y = {ratio:.4f}"
              f"  {detect_rational(ratio * 2 * np.pi) or ''}")

    # Phase pattern
    print(f"    Phase lattice (mod 2π):")
    for j in range(Ny - 1, -1, -1):
        row = "      "
        for i in range(Nx):
            val = theta[i, j] % (2 * np.pi)
            row += f"{val:6.3f} "
        print(row)

    # Phase differences across x at each y
    print(f"    x-differences at each y:")
    for j in range(Ny):
        diffs = []
        for i in range(Nx):
            i_next = (i + 1) % Nx
            d = ((theta[i_next, j] - theta[i, j] + np.pi) % (2 * np.pi)) - np.pi
            diffs.append(d)
        row = f"      y={j}: "
        for d in diffs:
            rat = detect_rational(d) or "·"
            row += f"{d:+.3f}({rat}) "
        print(row)

    return {
        "label": label,
        "r_final": r_final,
        "grad_x": grad_x,
        "grad_y": grad_y,
        "theta": theta.copy(),
        "r_hist": r_hist,
    }


# ── Field equation: Klein bottle XOR filter ───────────────────────────────────

def xor_filter_analysis():
    """Analyze which mode pairs survive the Klein bottle XOR constraint."""
    from fractions import Fraction

    print(f"\n{'=' * 70}")
    print(f"  KLEIN BOTTLE XOR FILTER ON STERN-BROCOT PAIRS")
    print(f"{'=' * 70}")

    # Build small tree
    fracs = [Fraction(0, 1), Fraction(1, 1)]
    for _ in range(5):
        new = [fracs[0]]
        for i in range(len(fracs) - 1):
            a, b = fracs[i], fracs[i + 1]
            med = Fraction(a.numerator + b.numerator,
                           a.denominator + b.denominator)
            new.append(med)
            new.append(b)
        fracs = new
    tree = sorted(f for f in set(fracs) if Fraction(0) < f < Fraction(1))

    # Parity classification
    def parity(f):
        """0 = even-q (Möbius-compatible), 1 = odd-q."""
        return f.denominator % 2

    # Count allowed vs forbidden pairs
    allowed = []
    forbidden = []
    for f1 in tree:
        for f2 in tree:
            p1, p2 = parity(f1), parity(f2)
            if (p1 + p2) % 2 == 1:  # XOR = 1
                allowed.append((f1, f2))
            else:
                forbidden.append((f1, f2))

    total = len(tree) ** 2
    print(f"\n  Tree nodes: {len(tree)}")
    print(f"  Total pairs: {total}")
    print(f"  Allowed (XOR=1): {len(allowed)} ({100*len(allowed)/total:.1f}%)")
    print(f"  Forbidden (XOR=0): {len(forbidden)} ({100*len(forbidden)/total:.1f}%)")

    # Population by (q1, q2) for allowed pairs
    print(f"\n  Allowed pairs by (q_x, q_y) — first 10 × 10:")
    print(f"  {'':>6s}", end="")
    for q2 in range(1, 11):
        print(f"  q_y={q2:<3d}", end="")
    print()

    for q1 in range(1, 11):
        print(f"  q_x={q1:<3d}", end="")
        for q2 in range(1, 11):
            count = sum(1 for f1, f2 in allowed
                        if f1.denominator == q1 and f2.denominator == q2)
            if count > 0:
                print(f"  {count:>5d}  ", end="")
            else:
                print(f"    ·    ", end="")
        print()

    # Most populated allowed modes
    print(f"\n  Top 20 allowed mode pairs (by 1/q₁q₂ weight):")
    print(f"  {'(p₁/q₁, p₂/q₂)':>25s}  {'q₁':>4s}  {'q₂':>4s}  "
          f"{'1/q₁q₂':>10s}  {'parity':>10s}")
    print("  " + "-" * 60)

    weighted = [(f1, f2, 1.0 / (f1.denominator * f2.denominator))
                for f1, f2 in allowed]
    weighted.sort(key=lambda x: -x[2])

    for f1, f2, w in weighted[:20]:
        p1, p2 = parity(f1), parity(f2)
        print(f"  ({str(f1):>5s}, {str(f2):>5s})  "
              f"{f1.denominator:4d}  {f2.denominator:4d}  "
              f"{w:10.6f}  ({p1},{p2})")

    # Fibonacci backbone on Klein bottle
    fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34]
    print(f"\n  Fibonacci convergent pairs on Klein bottle:")
    print(f"  {'(F_m/F_{m+1}, F_n/F_{n+1})':>35s}  {'allowed':>8s}  {'reason':>20s}")
    print("  " + "-" * 70)

    for m in range(1, 7):
        for n in range(1, 7):
            f1 = Fraction(fibs[m], fibs[m + 1])
            f2 = Fraction(fibs[n], fibs[n + 1])
            p1, p2 = parity(f1), parity(f2)
            ok = (p1 + p2) % 2 == 1
            reason = f"q₁={f1.denominator}({'even' if p1==0 else 'odd'}), q₂={f2.denominator}({'even' if p2==0 else 'odd'})"
            mark = "✓" if ok else "✗"
            print(f"  ({fibs[m]}/{fibs[m+1]}, {fibs[n]}/{fibs[n+1]})"
                  f"{'':>{20-len(f'{fibs[m]}/{fibs[m+1]}, {fibs[n]}/{fibs[n+1]}')}}"
                  f"  {mark:>8s}  {reason:>20s}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("  DERIVATION 19: KURAMOTO ON THE KLEIN BOTTLE")
    print("=" * 70)

    results = {}

    # ── Experiment 1: 3×3 comparison at multiple K ────────────────────────
    for K in [4.0, 6.0, 8.0, 12.0]:
        print(f"\n{'─' * 70}")
        print(f"  K = {K}")
        print(f"{'─' * 70}")

        results[f"torus_{K}"] = run_sim(
            3, 3, K, neighbors_torus, "TORUS", seed=42)
        results[f"klein_{K}"] = run_sim(
            3, 3, K, neighbors_klein, "KLEIN", seed=42)

    # ── Experiment 2: 5×5 at K=8 ─────────────────────────────────────────
    print(f"\n{'─' * 70}")
    print(f"  5×5 lattice, K = 8")
    print(f"{'─' * 70}")

    results["torus_5x5"] = run_sim(
        5, 5, 8.0, neighbors_torus, "TORUS 5×5", seed=42)
    results["klein_5x5"] = run_sim(
        5, 5, 8.0, neighbors_klein, "KLEIN 5×5", seed=42)

    # ── Experiment 3: Aspect ratio 3×5 ────────────────────────────────────
    print(f"\n{'─' * 70}")
    print(f"  3×5 lattice (asymmetric), K = 8")
    print(f"{'─' * 70}")

    results["torus_3x5"] = run_sim(
        3, 5, 8.0, neighbors_torus, "TORUS 3×5", seed=42)
    results["klein_3x5"] = run_sim(
        3, 5, 8.0, neighbors_klein, "KLEIN 3×5", seed=42)

    # ── Summary table ─────────────────────────────────────────────────────
    print(f"\n{'=' * 70}")
    print(f"  SUMMARY")
    print(f"{'=' * 70}")

    print(f"\n  {'Label':>20s}  {'r':>8s}  {'<∂x>':>8s}  {'<∂y>':>8s}  "
          f"{'∂x/∂y':>8s}")
    print("  " + "-" * 58)

    for key in sorted(results.keys()):
        res = results[key]
        ratio = (res["grad_x"] / res["grad_y"]
                 if abs(res["grad_y"]) > 0.01 else float('nan'))
        print(f"  {res['label']:>20s}  {res['r_final']:8.4f}  "
              f"{res['grad_x']:8.4f}  {res['grad_y']:8.4f}  "
              f"{ratio:8.4f}")

    # ── XOR filter analysis ───────────────────────────────────────────────
    xor_filter_analysis()

    print(f"\n{'=' * 70}")
    print(f"  DONE")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
