"""
Self-similar structure of the devil's staircase near 1/φ.

The Fibonacci convergents bracket 1/φ at resolutions that shrink
by φ² ≈ 2.618 per level:

    Level  Bracket           Width
    0      [1/2, 1/1]        0.5
    1      [1/2, 2/3]        0.1667
    2      [3/5, 2/3]        0.0667
    3      [3/5, 5/8]        0.025
    4      [8/13, 5/8]       0.00962
    5      [8/13, 13/21]     0.00366
    ...    ...                ...
    n      [F_n/F_{n+1}, F_{n-1}/F_n]   ~ 1/φ^(2n)

Each zoom level reveals the same structure, scaled by φ².
This is the natural "octave" of the staircase.

Usage:
    python sync_cost/derivations/phi_squared_zoom.py
"""

import math
from circle_map_utils import winding_number, PHI, INV_PHI, PHI_SQ


# ---------------------------------------------------------------------------
# Fibonacci convergents and brackets
# ---------------------------------------------------------------------------

def fib_convergent_brackets(n_levels=14):
    """
    Returns the nested brackets around 1/φ from Fibonacci convergents.

    Each level n gives a bracket [lo, hi] where:
      - lo = F_{n}/F_{n+1}  (convergent from below)
      - hi = F_{n-1}/F_n    (convergent from above)
      - width ≈ 1/(F_n × F_{n+1}) ≈ 1/φ^{2n}

    Alternating: odd n has lo from below, even n from above.
    """
    fibs = [1, 1]
    for _ in range(n_levels + 5):
        fibs.append(fibs[-1] + fibs[-2])

    brackets = []

    # Walk the convergents: 1/2, 2/3, 3/5, 5/8, 8/13, 13/21, ...
    # These alternate above and below 1/φ
    # Convergent k: F_k / F_{k+1}

    lo_p, lo_q = 0, 1   # start: 0
    hi_p, hi_q = 1, 1   # start: 1

    for i in range(n_levels):
        # Mediant
        p, q = lo_p + hi_p, lo_q + hi_q
        val = p / q

        width = hi_p / hi_q - lo_p / lo_q
        ratio_to_prev = None
        if len(brackets) > 0:
            ratio_to_prev = brackets[-1][5] / width

        brackets.append((i, p, q, val, val - INV_PHI, width, ratio_to_prev))

        if val < INV_PHI:
            lo_p, lo_q = p, q
        else:
            hi_p, hi_q = p, q

    return brackets


def sample_within_bracket(lo_p, lo_q, hi_p, hi_q, n_points=30):
    """
    Sample n_points Farey mediants between lo_p/lo_q and hi_p/hi_q.
    Uses iterated mediant subdivision.
    """
    points = [(lo_p, lo_q, lo_p / lo_q), (hi_p, hi_q, hi_p / hi_q)]

    # BFS mediant subdivision
    queue = [(lo_p, lo_q, hi_p, hi_q)]
    while len(points) < n_points and queue:
        next_queue = []
        for a, b, c, d in queue:
            if len(points) >= n_points:
                break
            p, q = a + c, b + d
            if q > 5000:  # don't go too deep
                continue
            points.append((p, q, p / q))
            next_queue.append((a, b, p, q))
            next_queue.append((p, q, c, d))
        queue = next_queue

    points.sort(key=lambda x: x[2])
    return points


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 85)
    print("  SELF-SIMILAR STRUCTURE AT 1/φ: φ²-ZOOM LEVELS")
    print("=" * 85)

    # --- 0. The bracket structure ---
    print(f"\n{'─'*85}")
    print("  0. FIBONACCI BRACKET HIERARCHY")
    print(f"{'─'*85}")
    print(f"\n  1/φ = {INV_PHI:.12f}")
    print(f"  φ²  = {PHI_SQ:.6f}")
    print()
    print(f"  {'lvl':>3s}  {'p/q':>12s}  {'value':>14s}  {'error':>14s}  "
          f"{'width':>12s}  {'zoom':>8s}")
    print("  " + "-" * 75)

    brackets = fib_convergent_brackets(20)
    for lvl, p, q, val, err, width, ratio in brackets:
        ratio_str = f"{ratio:.4f}" if ratio is not None else "---"
        print(f"  {lvl:3d}  {p:>5d}/{q:<5d}  {val:14.12f}  {err:+14.12f}  "
              f"{width:12.10f}  {ratio_str:>8s}")

    # --- 1. dW/dΩ at each zoom level ---
    print(f"\n{'─'*85}")
    print("  1. LOCAL dW/dΩ AT EACH FIBONACCI CONVERGENT")
    print(f"{'─'*85}")

    K_values = [0.8, 0.9, 0.95]

    # Compute W at each convergent and finite-difference dW/dΩ
    for K in K_values:
        print(f"\n  K = {K}:")
        print(f"  {'p/q':>12s}  {'Ω':>14s}  {'W':>14s}  {'W-Ω':>12s}  "
              f"{'local dW/dΩ':>12s}  {'ln(dW/dΩ)':>10s}")
        print("  " + "-" * 80)

        # Compute W at each convergent
        conv_data = []
        for lvl, p, q, val, err, width, ratio in brackets[:15]:
            W = winding_number(val, K)
            conv_data.append((lvl, p, q, val, W))

        # Finite-difference dW/dΩ between consecutive convergents
        for i in range(1, len(conv_data) - 1):
            lvl, p, q, omega, W = conv_data[i]
            _, _, _, omega_prev, W_prev = conv_data[i - 1]
            _, _, _, omega_next, W_next = conv_data[i + 1]

            dW_dOmega = (W_next - W_prev) / (omega_next - omega_prev)

            ln_dW = math.log(abs(dW_dOmega)) if abs(dW_dOmega) > 1e-10 else float('-inf')

            print(f"  {p:>5d}/{q:<5d}  {omega:14.10f}  {W:14.10f}  "
                  f"{W - omega:+12.10f}  {dW_dOmega:12.6f}  {ln_dW:10.4f}")

    # --- 2. Scale-by-scale analysis ---
    print(f"\n{'─'*85}")
    print("  2. SCALE-BY-SCALE: dW/dΩ WITHIN EACH BRACKET")
    print(f"{'─'*85}")

    K = 0.9
    print(f"\n  K = {K}")

    # For each zoom level, sample within the bracket and compute dW/dΩ
    # Brackets: level n uses [convergent_n, convergent_{n+1}]

    conv_list = [(p, q, val) for _, p, q, val, _, _, _ in brackets[:12]]

    for i in range(2, min(10, len(conv_list) - 1)):
        p1, q1, v1 = conv_list[i]
        p2, q2, v2 = conv_list[i + 1]

        if v1 > v2:
            lo_p, lo_q, hi_p, hi_q = p2, q2, p1, q1
        else:
            lo_p, lo_q, hi_p, hi_q = p1, q1, p2, q2

        width = hi_p / hi_q - lo_p / lo_q

        print(f"\n  Level {i}: [{lo_p}/{lo_q}, {hi_p}/{hi_q}]  "
              f"width = {width:.10f}")

        # Sample within this bracket
        points = sample_within_bracket(lo_p, lo_q, hi_p, hi_q, n_points=12)

        # Compute W at each point
        pw = []
        for p, q, omega in points:
            W = winding_number(omega, K)
            pw.append((p, q, omega, W))

        print(f"  {'p/q':>15s}  {'Ω':>14s}  {'W':>14s}  {'dW/dΩ':>10s}")
        print("  " + "-" * 60)

        for j in range(len(pw)):
            p, q, omega, W = pw[j]
            if j > 0 and j < len(pw) - 1:
                _, _, o_prev, W_prev = pw[j - 1]
                _, _, o_next, W_next = pw[j + 1]
                dW = (W_next - W_prev) / (o_next - o_prev)
                dW_str = f"{dW:10.4f}"
            else:
                dW_str = "---"
            print(f"  {p:>7d}/{q:<6d}  {omega:14.10f}  {W:14.10f}  {dW_str:>10s}")

    # --- 3. The φ² scaling law ---
    print(f"\n{'─'*85}")
    print("  3. THE φ² SCALING LAW")
    print(f"{'─'*85}")

    print(f"\n  If the staircase is self-similar at 1/φ, then dW/dΩ should")
    print(f"  scale the same way at each zoom level (scaled by φ²).")
    print()

    K = 0.9
    print(f"  K = {K}")
    print()

    # At each zoom level, compute the average dW/dΩ within the bracket
    print(f"  {'level':>5s}  {'bracket':>20s}  {'width':>12s}  "
          f"{'<dW/dΩ>':>10s}  {'width×φ^(2n)':>14s}  {'<dW/dΩ>×width':>14s}")
    print("  " + "-" * 85)

    for i in range(2, min(10, len(conv_list) - 1)):
        p1, q1, v1 = conv_list[i]
        p2, q2, v2 = conv_list[i + 1]

        if v1 > v2:
            lo_p, lo_q, hi_p, hi_q = p2, q2, p1, q1
        else:
            lo_p, lo_q, hi_p, hi_q = p1, q1, p2, q2

        width = hi_p / hi_q - lo_p / lo_q

        W_lo = winding_number(lo_p / lo_q, K)
        W_hi = winding_number(hi_p / hi_q, K)

        avg_dW = (W_hi - W_lo) / width
        scaled_width = width * PHI_SQ ** i
        total_dW = avg_dW * width  # ΔW across the bracket

        bracket_str = f"[{lo_p}/{lo_q}, {hi_p}/{hi_q}]"
        print(f"  {i:5d}  {bracket_str:>20s}  {width:12.10f}  "
              f"{avg_dW:10.4f}  {scaled_width:14.6f}  {total_dW:14.10f}")

    # --- 4. The key ratios ---
    print(f"\n{'─'*85}")
    print("  4. ΔW ACROSS EACH BRACKET (K = 0.9)")
    print(f"{'─'*85}")

    print(f"\n  ΔW_n = W(convergent_{{n+1}}) - W(convergent_n)")
    print(f"  If self-similar: ΔW_n / ΔW_{{n+1}} → φ² = {PHI_SQ:.6f}")
    print()

    prev_dW = None
    print(f"  {'n':>3s}  {'from':>12s}  {'to':>12s}  {'ΔΩ':>14s}  "
          f"{'ΔW':>14s}  {'ΔW_n/ΔW_(n+1)':>14s}  {'ratio/φ²':>10s}")
    print("  " + "-" * 90)

    delta_Ws = []
    for i in range(len(conv_list) - 1):
        if i < 1:
            continue
        p1, q1, v1 = conv_list[i]
        p2, q2, v2 = conv_list[i + 1]

        W1 = winding_number(v1, K)
        W2 = winding_number(v2, K)

        dOmega = v2 - v1
        dW = W2 - W1

        ratio_str = "---"
        ratio2_str = "---"
        if prev_dW is not None and abs(dW) > 1e-12:
            ratio = prev_dW / dW
            ratio_str = f"{ratio:14.6f}"
            ratio2_str = f"{ratio / PHI_SQ:10.6f}"

        from_str = f"{p1}/{q1}"
        to_str = f"{p2}/{q2}"
        print(f"  {i:3d}  {from_str:>12s}  {to_str:>12s}  {dOmega:+14.10f}  "
              f"{dW:+14.10f}  {ratio_str:>14s}  {ratio2_str:>10s}")

        prev_dW = dW
        delta_Ws.append((i, dW))

    # --- 5. Comparison to CMB ---
    print(f"\n{'─'*85}")
    print("  5. CONNECTING TO THE CMB")
    print(f"{'─'*85}")

    print(f"""
  The CMB power spectrum spans ~7 decades of wavenumber:
    k_min ≈ 10⁻⁴ Mpc⁻¹  to  k_max ≈ 10³ Mpc⁻¹

  In φ² "octaves", 7 decades = log(10⁷)/log(φ²) ≈ {7 * math.log(10) / math.log(PHI_SQ):.1f} levels

  The Fibonacci convergent at level n has denominator F_n ≈ φⁿ/√5.
  At level 17: F₁₇ = 1597, precision ≈ 1/φ¹⁷ ≈ {1/PHI**17:.2e}

  Each "octave" (factor of φ² in resolution) reveals one more
  Fibonacci convergent. The bracket width shrinks as 1/φ^(2n),
  but the STRUCTURE within each bracket is self-similar.

  If k ↔ Ω maps e-folds to Fibonacci levels:
    one e-fold of inflation = one φ² zoom level
    N ≈ 60 e-folds → {60:.0f} levels → F_{{60}} ≈ φ^{{60}}/√5 ≈ {PHI**60/math.sqrt(5):.2e}

  The spectral tilt n_s - 1 measures how the power changes
  per e-fold. On the staircase, this is how ΔW changes per
  φ² zoom level.
""")

    # Compute the "tilt per φ² level"
    print(f"  Tilt per φ² level (K = 0.9):")
    print(f"  {'n':>3s}  {'|ΔW_n|':>14s}  {'ln|ΔW_n|':>12s}  {'Δ(ln|ΔW|)':>12s}")
    print("  " + "-" * 50)

    prev_ln = None
    for i, dW in delta_Ws:
        ln_dW = math.log(abs(dW)) if abs(dW) > 1e-15 else float('-inf')
        d_ln = ""
        if prev_ln is not None and not math.isinf(ln_dW) and not math.isinf(prev_ln):
            d = ln_dW - prev_ln
            d_ln = f"{d:+12.6f}"
        print(f"  {i:3d}  {abs(dW):14.10f}  {ln_dW:12.4f}  {d_ln:>12s}")
        prev_ln = ln_dW

    print(f"\n  If Δ(ln|ΔW|) converges to a constant c per level,")
    print(f"  and each level = one e-fold, then n_s - 1 = c.")
    print(f"  Target: n_s - 1 ≈ -0.035")
