"""
Circle map sampled on the Stern-Brocot tree.

The devil's staircase is organized by rationals, not decimals.
The natural grid is the Farey/Stern-Brocot tree, where the path
to 1/φ goes through the Fibonacci convergents:

    1/2 → 2/3 → 3/5 → 5/8 → 8/13 → 13/21 → 21/34 → ...

Each mediant (a+c)/(b+d) sits exactly between parent rationals
a/b and c/d. The spacing shrinks as 1/(q_n × q_{n+1}) — the
natural resolution of the staircase.

Usage:
    python sync_cost/derivations/stern_brocot_map.py
"""

import math
from circle_map_utils import winding_number, PHI, INV_PHI


# ---------------------------------------------------------------------------
# Stern-Brocot tree and Farey mediants
# ---------------------------------------------------------------------------

def fibonacci_convergents(n_terms=15):
    """
    The Fibonacci convergents to 1/φ, alternating above and below:
    1/1, 1/2, 2/3, 3/5, 5/8, 8/13, 13/21, 21/34, 34/55, 55/89, ...
    """
    fibs = [1, 1]
    for _ in range(n_terms):
        fibs.append(fibs[-1] + fibs[-2])

    convergents = []
    for i in range(len(fibs) - 1):
        p, q = fibs[i], fibs[i + 1]
        convergents.append((p, q, p / q))
    return convergents


def farey_mediants_between(a, b, c, d, depth=5):
    """
    Generate Farey mediants between a/b and c/d, recursively.
    The mediant is (a+c)/(b+d).
    Returns list of (p, q, value) sorted by value.
    """
    if depth == 0 or b + d > 200:
        return []

    p, q = a + c, b + d
    mid = p / q

    left = farey_mediants_between(a, b, p, q, depth - 1)
    right = farey_mediants_between(p, q, c, d, depth - 1)

    return left + [(p, q, mid)] + right


def stern_brocot_path_to_phi(depth=12):
    """
    The path down the Stern-Brocot tree toward 1/φ.

    Starting from 0/1 and 1/1, take mediants.
    At each step, go LEFT if 1/φ < mediant, RIGHT if 1/φ > mediant.

    This produces exactly the Fibonacci convergents.
    """
    path = []
    a, b = 0, 1  # left parent
    c, d = 1, 1  # right parent

    for _ in range(depth):
        p, q = a + c, b + d
        val = p / q
        path.append((p, q, val, val - INV_PHI))

        if val < INV_PHI:
            a, b = p, q  # go right
        else:
            c, d = p, q  # go left

    return path


def natural_sample_points(n_fib=12, mediant_depth=3):
    """
    Sample points for the circle map, organized by the Stern-Brocot tree.

    Includes:
    1. Fibonacci convergents to 1/φ
    2. Farey mediants between consecutive convergents
    3. Key simple rationals (1/2, 1/3, 2/3, 3/5, 5/8)
    """
    points = set()

    # Fibonacci convergents
    convs = fibonacci_convergents(n_fib)
    for p, q, val in convs:
        if 0.05 < val < 0.95:
            points.add((p, q, val))

    # Mediants between consecutive convergents
    for i in range(len(convs) - 1):
        p1, q1, v1 = convs[i]
        p2, q2, v2 = convs[i + 1]
        if v1 > v2:
            p1, q1, p2, q2 = p2, q2, p1, q1
        mediants = farey_mediants_between(p1, q1, p2, q2, mediant_depth)
        for p, q, val in mediants:
            if 0.05 < val < 0.95:
                points.add((p, q, val))

    # Simple rationals
    for p, q in [(1, 2), (1, 3), (2, 3), (1, 4), (3, 4),
                 (1, 5), (2, 5), (3, 5), (4, 5),
                 (3, 7), (4, 7), (5, 7),
                 (5, 12), (7, 12)]:
        points.add((p, q, p / q))

    # 1/φ itself (approximated by high Fibonacci)
    points.add((610, 987, 610 / 987))  # F_15/F_16

    return sorted(points, key=lambda x: x[2])


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 80)
    print("  STERN-BROCOT SAMPLING OF THE CIRCLE MAP")
    print("=" * 80)

    # --- 0. The path to 1/φ ---
    print(f"\n{'─'*80}")
    print("  0. STERN-BROCOT PATH TO 1/φ")
    print(f"{'─'*80}")
    print(f"\n  1/φ = {INV_PHI:.10f}")
    print(f"\n  {'step':>4s}  {'p/q':>10s}  {'value':>12s}  {'error':>14s}  {'q':>4s}")
    print("  " + "-" * 50)

    path = stern_brocot_path_to_phi(20)
    for i, (p, q, val, err) in enumerate(path):
        print(f"  {i:4d}  {p:>4d}/{q:<4d}   {val:12.10f}  {err:+14.10f}  {q:4d}")

    # --- 1. Staircase at Fibonacci-natural sample points ---
    print(f"\n{'─'*80}")
    print("  1. CIRCLE MAP AT STERN-BROCOT SAMPLE POINTS")
    print(f"{'─'*80}")

    samples = natural_sample_points(n_fib=10, mediant_depth=2)

    for K in [0.8, 0.9, 1.0]:
        print(f"\n  K = {K}:")
        print(f"  {'p/q':>10s}  {'Ω':>12s}  {'W':>12s}  {'W-Ω':>12s}  {'locked?':>8s}")
        print("  " + "-" * 65)

        results = []
        for p, q, omega in samples:
            W = winding_number(omega, K)
            locked = abs(W - round(W * q) / q) < 0.001 if q < 50 else "?"
            results.append((p, q, omega, W, locked))

        for p, q, omega, W, locked in results:
            lock_str = "YES" if locked is True else "no" if locked is False else "?"
            # Is this a Fibonacci convergent?
            fib_mark = ""
            fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
            if q in fibs and p in fibs:
                fib_mark = " ← Fib"
            if abs(omega - INV_PHI) < 0.001:
                fib_mark = " ← 1/φ"

            print(f"  {p:>4d}/{q:<4d}   {omega:12.8f}  {W:12.8f}  {W-omega:+12.8f}  {lock_str:>8s}{fib_mark}")

    # --- 2. Zoom: between 3/5 and 2/3 via mediants ---
    print(f"\n{'─'*80}")
    print("  2. BETWEEN 3/5 AND 2/3: THE PATH THROUGH 1/φ")
    print(f"{'─'*80}")

    # Generate dense mediants between 3/5 and 2/3
    mediants_35_23 = farey_mediants_between(3, 5, 2, 3, depth=6)
    # Add 3/5 and 2/3 themselves
    all_points = [(3, 5, 0.6)] + mediants_35_23 + [(2, 3, 2/3)]
    all_points.sort(key=lambda x: x[2])

    for K in [0.8, 0.9]:
        print(f"\n  K = {K}:")
        print(f"  {'p/q':>12s}  {'Ω':>12s}  {'W':>12s}  {'dW':>10s}  {'note':>15s}")
        print("  " + "-" * 70)

        prev_W = None
        prev_omega = None
        for p, q, omega in all_points:
            W = winding_number(omega, K)

            dW = ""
            if prev_W is not None and prev_omega is not None:
                d_omega = omega - prev_omega
                if d_omega > 1e-10:
                    slope = (W - prev_W) / d_omega
                    dW = f"{slope:10.4f}"

            note = ""
            if abs(omega - INV_PHI) < 0.002:
                note = "<<< 1/φ >>>"
            elif abs(omega - 3/5) < 0.001:
                note = "3/5"
            elif abs(omega - 5/8) < 0.001:
                note = "5/8"
            elif abs(omega - 8/13) < 0.001:
                note = "8/13"
            elif abs(omega - 13/21) < 0.001:
                note = "13/21"
            elif abs(omega - 2/3) < 0.001:
                note = "2/3"

            # Fibonacci rational?
            fibs = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
            if p in fibs and q in fibs:
                if not note:
                    note = f"Fib({p}/{q})"

            print(f"  {p:>5d}/{q:<5d}  {omega:12.8f}  {W:12.8f}  {dW:>10s}  {note:>15s}")

            prev_W = W
            prev_omega = omega

    # --- 3. The power spectrum on the natural grid ---
    print(f"\n{'─'*80}")
    print("  3. POWER SPECTRUM ON STERN-BROCOT GRID (K = 0.9)")
    print(f"{'─'*80}")

    K = 0.9
    # Compute W at all mediant points between 3/5 and 2/3
    points_with_W = []
    for p, q, omega in all_points:
        W = winding_number(omega, K)
        points_with_W.append((p, q, omega, W))

    # Compute local dW/dΩ as the power proxy
    print(f"\n  {'p/q':>12s}  {'Ω':>12s}  {'W':>12s}  {'dW/dΩ':>10s}  {'ln(dW/dΩ)':>10s}  {'note':>12s}")
    print("  " + "-" * 75)

    for i in range(1, len(points_with_W) - 1):
        p, q, omega, W = points_with_W[i]
        _, _, omega_prev, W_prev = points_with_W[i - 1]
        _, _, omega_next, W_next = points_with_W[i + 1]

        dW_dOmega = (W_next - W_prev) / (omega_next - omega_prev)

        if dW_dOmega > 0.01:
            ln_dW = math.log(dW_dOmega)
        else:
            ln_dW = float('-inf')

        note = ""
        if abs(omega - INV_PHI) < 0.002: note = "<<< 1/φ >>>"
        elif abs(omega - 3/5) < 0.001: note = "3/5"
        elif abs(omega - 5/8) < 0.001: note = "5/8"
        elif abs(omega - 8/13) < 0.001: note = "8/13"
        elif abs(omega - 2/3) < 0.001: note = "2/3"

        print(f"  {p:>5d}/{q:<5d}  {omega:12.8f}  {W:12.8f}  {dW_dOmega:10.4f}  {ln_dW:10.4f}  {note:>12s}")

    # --- 4. Tilt from the natural grid ---
    print(f"\n{'─'*80}")
    print("  4. SPECTRAL TILT d(ln dW/dΩ) / d(ln Ω)")
    print(f"{'─'*80}")

    # Compute tilt: d ln P / d ln Ω where P = dW/dΩ
    print(f"\n  {'p/q':>12s}  {'Ω':>12s}  {'dW/dΩ':>10s}  {'tilt':>10s}  {'note':>12s}")
    print("  " + "-" * 65)

    for i in range(2, len(points_with_W) - 2):
        p, q, omega, W = points_with_W[i]

        # 3-point dW/dΩ at i-1, i, i+1
        dW = []
        om = []
        for j in [i - 1, i, i + 1]:
            _, _, o_prev, W_prev = points_with_W[j - 1]
            _, _, o_next, W_next = points_with_W[j + 1]
            d = (W_next - W_prev) / (o_next - o_prev)
            dW.append(d)
            om.append(points_with_W[j][2])

        if all(d > 0.01 for d in dW) and om[2] > om[0]:
            ln_dW = [math.log(d) for d in dW]
            ln_om = [math.log(o) for o in om]
            tilt = (ln_dW[2] - ln_dW[0]) / (ln_om[2] - ln_om[0])
        else:
            tilt = float('nan')

        note = ""
        if abs(omega - INV_PHI) < 0.002: note = "<<< 1/φ >>>"
        elif abs(omega - 3/5) < 0.001: note = "3/5"
        elif abs(omega - 5/8) < 0.001: note = "5/8"
        elif abs(omega - 8/13) < 0.001: note = "8/13"
        elif abs(omega - 2/3) < 0.001: note = "2/3"

        dW_here = dW[1] if len(dW) > 1 else 0

        if not math.isnan(tilt):
            print(f"  {p:>5d}/{q:<5d}  {omega:12.8f}  {dW_here:10.4f}  {tilt:+10.4f}  {note:>12s}")

    # --- Summary ---
    print(f"\n{'='*80}")
    print("  SUMMARY")
    print(f"{'='*80}")
    print(f"""
  Sampling on the Stern-Brocot tree instead of a decimal grid:

  The Farey mediants between 3/5 and 2/3 are:
    3/5 → 5/8 → 8/13 → 13/21 → ... → 1/φ ← ... ← 7/11 ← 5/8 ← 2/3

  Each mediant is a natural "tick mark" of the devil's staircase.
  The staircase density dW/dΩ, computed between these natural points,
  gives the power spectrum in the coordinate system the staircase
  itself uses.

  The spectral tilt d ln(dW/dΩ) / d ln Ω at 1/φ, computed on this
  natural grid, should be the cleanest measurement of how the
  staircase curves at the golden ratio.
""")
