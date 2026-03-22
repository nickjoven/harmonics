"""
Superharmonic structure within the 2.2 Fibonacci levels.

The observable universe samples ~2.2 Fibonacci levels of the
staircase (levels ~20-22). Within each level, the Farey mediants
create a sub-hierarchy of higher-order resonances.

Between F_n/F_{n+1} and F_{n+1}/F_{n+2}, the mediants are:
  (F_n + F_{n+1}) / (F_{n+1} + F_{n+2}) = F_{n+1}/F_{n+2}  (... wait)

Actually: the mediant of consecutive Fibonacci convergents
F_n/F_{n+1} and F_{n+1}/F_{n+2} is (F_n + F_{n+1})/(F_{n+1} + F_{n+2})
= F_{n+1}/F_{n+2}... no, that's just the NEXT convergent.

The REAL sub-structure comes from the Stern-Brocot subtree:
between a/b and c/d, the mediant (a+c)/(b+d) has denominator
b+d. Between two Fibonacci convergents with denominators F_{n+1}
and F_{n+2}, the first mediant has denominator F_{n+1} + F_{n+2}
= F_{n+3}. That IS the next Fibonacci convergent.

So the Fibonacci path through the Stern-Brocot tree has NO room
for non-Fibonacci mediants — each mediant IS the next convergent.
This is unique to 1/φ.

But the superharmonics are the OTHER rationals in the bracket,
reached by going LEFT or RIGHT from the Fibonacci path. These
have denominators that are NOT Fibonacci numbers.

Usage:
    python sync_cost/derivations/superharmonic_regime.py
"""

import math
from circle_map_utils import winding_number, PHI, INV_PHI, PHI_SQ, LN_PHI_SQ


def stern_brocot_subtree(lo_p, lo_q, hi_p, hi_q, depth=0, max_depth=6):
    """
    Full Stern-Brocot subtree between lo_p/lo_q and hi_p/hi_q.
    Returns list of (p, q, value, depth, direction) tuples.
    direction: 'M' for mediant, 'L' for left-of-mediant, 'R' for right.
    """
    if depth >= max_depth or lo_q + hi_q > 3000:
        return []

    p, q = lo_p + hi_p, lo_q + hi_q
    val = p / q

    # Is this a Fibonacci number pair?
    fibs_set = set()
    a, b = 1, 1
    for _ in range(30):
        fibs_set.add(a)
        a, b = b, a + b
    is_fib = p in fibs_set and q in fibs_set

    left = stern_brocot_subtree(lo_p, lo_q, p, q, depth + 1, max_depth)
    right = stern_brocot_subtree(p, q, hi_p, hi_q, depth + 1, max_depth)

    return left + [(p, q, val, depth, is_fib)] + right


if __name__ == "__main__":
    print("=" * 85)
    print("  SUPERHARMONIC STRUCTURE WITHIN THE FIBONACCI BRACKET")
    print("=" * 85)

    # --- 0. The Stern-Brocot subtree between 3/5 and 5/8 ---
    print(f"\n{'─'*85}")
    print("  0. STERN-BROCOT SUBTREE BETWEEN 3/5 AND 5/8")
    print(f"{'─'*85}")

    tree = stern_brocot_subtree(3, 5, 5, 8, max_depth=5)
    tree_sorted = sorted(tree, key=lambda x: x[2])

    print(f"\n  {'p/q':>12s}  {'value':>14s}  {'Ω - 1/φ':>14s}  {'depth':>5s}  "
          f"{'q':>5s}  {'Fib?':>5s}")
    print("  " + "-" * 65)

    for p, q, val, depth, is_fib in tree_sorted:
        indent = "  " * depth
        fib_mark = "YES" if is_fib else ""
        print(f"  {p:>5d}/{q:<5d}  {val:14.10f}  {val - INV_PHI:+14.10f}  "
              f"{depth:5d}  {q:5d}  {fib_mark:>5s}")

    # --- 1. Mode-locking plateaus of the superharmonics ---
    print(f"\n{'─'*85}")
    print("  1. WINDING NUMBER AT SUPERHARMONIC RATIONALS (K = 0.9)")
    print(f"{'─'*85}")

    K = 0.9

    # Group by denominator to see the harmonic structure
    print(f"\n  Rationals between 3/5 and 5/8, grouped by denominator:")
    print()

    by_denom = {}
    for p, q, val, depth, is_fib in tree_sorted:
        if q not in by_denom:
            by_denom[q] = []
        by_denom[q].append((p, q, val, depth, is_fib))

    for q_val in sorted(by_denom.keys()):
        entries = by_denom[q_val]
        for p, q, val, depth, is_fib in entries:
            W = winding_number(val, K)
            locked = abs(W - round(W * q) / q) < 0.0005

            fib_mark = " ← Fibonacci" if is_fib else ""
            lock_mark = " LOCKED" if locked else ""

            nearest_rational = round(W * q) / q
            lock_width_proxy = abs(W - nearest_rational)

            print(f"  {p:>5d}/{q:<5d}  Ω={val:.8f}  W={W:.8f}  "
                  f"|W-{round(W*q)}/{q}|={lock_width_proxy:.6f}"
                  f"{lock_mark}{fib_mark}")

    # --- 2. The harmonic series within one bracket ---
    print(f"\n{'─'*85}")
    print("  2. HARMONIC STRUCTURE: DENOMINATORS AND THEIR PLATEAUS")
    print(f"{'─'*85}")

    # Between 8/13 and 13/21, enumerate ALL rationals with q ≤ 100
    lo, hi = 8/13, 13/21
    print(f"\n  All rationals p/q with {lo:.4f} < p/q < {hi:.4f} and q ≤ 100:")
    print()

    rationals = []
    for q in range(1, 101):
        for p in range(1, q):
            val = p / q
            if lo < val < hi and math.gcd(p, q) == 1:
                rationals.append((p, q, val))

    rationals.sort(key=lambda x: x[2])

    # Identify Fibonacci rationals
    fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    fib_set = set(fibs)

    print(f"  {'p/q':>12s}  {'Ω':>12s}  {'Ω - 1/φ':>14s}  {'q':>4s}  {'type':>15s}")
    print("  " + "-" * 65)

    for p, q, val in rationals:
        note = ""
        if p in fib_set and q in fib_set:
            note = "FIBONACCI"
        elif q == p + q - p:  # trivially true, check if q is Fibonacci
            if q in fib_set:
                note = f"Fib denom"

        # Is denominator a sum of two Fibonacci numbers?
        for f1 in fibs:
            if q - f1 in fib_set and q - f1 > 0:
                if not note:
                    note = f"q={f1}+{q-f1}"
                break

        print(f"  {p:>5d}/{q:<5d}  {val:12.8f}  {val - INV_PHI:+14.10f}  {q:4d}  {note:>15s}")

    # --- 3. Plateau widths as a function of q ---
    print(f"\n{'─'*85}")
    print("  3. PLATEAU WIDTHS vs DENOMINATOR (K = 0.9)")
    print(f"{'─'*85}")

    K = 0.9
    print(f"\n  For each rational p/q near 1/φ, measure the")
    print(f"  effective plateau width from dW/dΩ.")
    print()

    # Use a few representative rationals at each q level
    test_rationals = [
        (3, 5), (5, 8), (8, 13), (13, 21), (21, 34), (34, 55),
        (55, 89), (89, 144),
        # Non-Fibonacci
        (11, 18), (19, 31), (27, 44), (16, 26),
        (29, 47), (37, 60), (45, 73),
    ]

    print(f"  {'p/q':>12s}  {'q':>5s}  {'W(Ω)':>12s}  {'dW/dΩ':>10s}  "
          f"{'ln q':>8s}  {'ln(dW/dΩ)':>10s}  {'type':>10s}")
    print("  " + "-" * 75)

    for p, q in test_rationals:
        if math.gcd(p, q) != 1:
            continue
        omega = p / q
        W = winding_number(omega, K)

        # Numerical derivative
        eps = 1e-6
        W_plus = winding_number(omega + eps, K)
        W_minus = winding_number(omega - eps, K)
        dW = (W_plus - W_minus) / (2 * eps)

        is_fib = p in fib_set and q in fib_set
        typ = "Fibonacci" if is_fib else "other"

        ln_q = math.log(q)
        ln_dW = math.log(abs(dW)) if abs(dW) > 1e-10 else float('-inf')

        print(f"  {p:>5d}/{q:<5d}  {q:5d}  {W:12.8f}  {dW:10.4f}  "
              f"{ln_q:8.4f}  {ln_dW:10.4f}  {typ:>10s}")

    # --- 4. The superharmonic "forest" ---
    print(f"\n{'─'*85}")
    print("  4. THE SUPERHARMONIC FOREST")
    print(f"{'─'*85}")

    print(f"""
  Between any two Fibonacci convergents, the Stern-Brocot subtree
  contains ALL rationals. But their plateau widths scale as ~1/q².

  The Fibonacci rationals (q = F_n) have the NARROWEST plateaus
  for their neighborhood — that's why 1/φ is the hardest to lock.

  The non-Fibonacci rationals (q ≠ F_n) are the "superharmonics."
  They create a forest of small plateaus within each Fibonacci bracket.

  Question: does the power spectrum P(k) see these superharmonics?

  If the mapping k→Ω traverses 2.2 Fibonacci levels over 60 e-folds,
  it crosses MANY non-Fibonacci rationals along the way. Each one
  creates a small bump or dip in P(k).

  At level ~21, the Fibonacci denominators are ~17711. But within
  the bracket, there are rationals with denominators 2, 3, 4, ...
  relative to the bracket width. These create features at scales:

    δk/k ~ 1/q × (bracket width / e-fold range)
""")

    # How many rationals with q ≤ Q are there in a bracket of width w?
    # By Farey sequence density: ~3Q²/π² rationals with q ≤ Q in [0,1]
    # In a bracket of width w: ~3Q²w/π²

    bracket_width = 1 / (PHI**(2*21))  # width at level 21
    print(f"  Bracket width at level 21: {bracket_width:.4e}")
    print(f"  E-folds spanning this bracket: {bracket_width / 0.0365 * 60:.4f}")
    print()

    for Q in [10, 50, 100, 500, 1000]:
        n_rationals = 3 * Q**2 * bracket_width / (math.pi**2)
        print(f"  Rationals with q ≤ {Q:5d} in bracket: ~{n_rationals:.4f}")

    # --- 5. Do superharmonics create observable features? ---
    print(f"\n{'─'*85}")
    print("  5. SUPERHARMONIC FEATURES IN THE POWER SPECTRUM")
    print(f"{'─'*85}")

    # Within the bracket [8/13, 13/21] (a wider bracket we can resolve),
    # compute W at fine resolution and look for plateau features
    K = 0.9
    lo_omega = 8/13
    hi_omega = 13/21
    n_points = 200

    omegas = [lo_omega + i * (hi_omega - lo_omega) / n_points
              for i in range(n_points + 1)]

    W_values = [winding_number(omega, K) for omega in omegas]

    # Compute dW/dΩ
    dW_values = []
    for i in range(1, len(W_values) - 1):
        dW = (W_values[i+1] - W_values[i-1]) / (omegas[i+1] - omegas[i-1])
        dW_values.append((omegas[i], W_values[i], dW))

    # Find local minima and maxima of dW/dΩ (features)
    print(f"\n  Features in dW/dΩ between 8/13 and 13/21 (K = {K}):")
    print(f"  (Local extrema of the 'power spectrum')")
    print()
    print(f"  {'Ω':>12s}  {'W':>12s}  {'dW/dΩ':>10s}  {'type':>8s}  {'nearest p/q':>14s}")
    print("  " + "-" * 65)

    for i in range(1, len(dW_values) - 1):
        omega, W, dW = dW_values[i]
        _, _, dW_prev = dW_values[i-1]
        _, _, dW_next = dW_values[i+1]

        if (dW > dW_prev and dW > dW_next and dW > 1.5) or \
           (dW < dW_prev and dW < dW_next and dW < 1.0):
            # Find nearest rational
            best_p, best_q = 0, 1
            best_dist = 1.0
            for q in range(2, 60):
                p = round(omega * q)
                if 0 < p < q and math.gcd(p, q) == 1:
                    dist = abs(omega - p/q)
                    if dist < best_dist:
                        best_dist = dist
                        best_p, best_q = p, q

            typ = "MAX" if dW > 1.3 else "min"

            is_fib_r = best_p in fib_set and best_q in fib_set
            fib_note = " (Fib)" if is_fib_r else ""

            print(f"  {omega:12.8f}  {W:12.8f}  {dW:10.4f}  {typ:>8s}  "
                  f"{best_p}/{best_q}{fib_note}")

    # --- 6. Summary ---
    print(f"\n{'─'*85}")
    print("  6. SUPERHARMONIC REGIME: SUMMARY")
    print(f"{'─'*85}")

    print(f"""
  Within the 2.2 Fibonacci levels the observable universe samples:

  1. The Fibonacci convergents (q = F_n) define the PRIMARY structure:
     the self-similar backbone with scaling φ².

  2. Between convergents, non-Fibonacci rationals create a FOREST
     of small plateaus — the superharmonic structure.

  3. At level ~21, the bracket is incredibly narrow (~10⁻⁹),
     but RELATIVE to the bracket, the superharmonic forest is
     self-similar at every scale.

  4. The features in dW/dΩ (local maxima/minima) cluster near
     low-order rationals within the bracket. These would appear
     as oscillatory features in the power spectrum — potentially
     matching the observed "glitches" in the CMB at ℓ ≈ 20-40.

  5. The superharmonic structure is NOT a separate regime — it's
     the SAME staircase viewed at sub-Fibonacci resolution.
     The Fibonacci levels are the "fundamental mode"; the
     non-Fibonacci rationals are the overtones.
""")
