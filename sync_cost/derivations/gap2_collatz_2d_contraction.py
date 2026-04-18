"""
gap2_collatz_2d_contraction.py

Rational Collatz in H²: testing 2D contraction.

Instead of the 1D integer Collatz (hard), test the full rational
Collatz map C: Q+ → Q+ in the (p, q) plane, embedded in H² via
Ford circles.

Rules (from docs/collatz.html):
  C(p/q) = (p/2) / q          if p even  (q odd by coprimality)
  C(p/q) = p / (q/2)          if q even  (p odd by coprimality)
  C(p/q) = (3p+1) / (q+1)     if both odd, then reduce

All results in lowest terms.

Questions:
  1. Does every (p, q) trajectory reach (1, 1)?
  2. Is the contraction exponential in the H² metric?
  3. How does the q > 1 dimension (the "forced" dimension) affect
     contraction rate vs the q = 1 boundary (standard Collatz)?
  4. Does the "height" h(p/q) = p + q contract on average?
"""

import numpy as np
from math import gcd
from collections import defaultdict


def rational_collatz_step(p, q):
    if p % 2 == 0:
        p2, q2 = p // 2, q
    elif q % 2 == 0:
        p2, q2 = p, q // 2
    else:
        p2, q2 = 3 * p + 1, q + 1
    g = gcd(p2, q2)
    return p2 // g, q2 // g


def hyp_dist(p1, q1, p2, q2):
    x1, y1 = p1 / q1, 1.0 / (2 * q1 * q1)
    x2, y2 = p2 / q2, 1.0 / (2 * q2 * q2)
    num = (x1 - x2) ** 2 + (y1 - y2) ** 2
    den = 2 * y1 * y2
    arg = 1 + num / den
    return np.arccosh(max(1.0, arg))


def run_trajectory(p0, q0, max_steps=5000):
    p, q = p0, q0
    traj = [(p, q)]
    seen = set()
    for _ in range(max_steps):
        if p == 1 and q == 1:
            break
        if (p, q) in seen:
            break
        seen.add((p, q))
        p, q = rational_collatz_step(p, q)
        traj.append((p, q))
    return traj


def height(p, q):
    return p + q


def main():
    print("=" * 72)
    print("Rational Collatz in H²: 2D contraction test")
    print("=" * 72)

    # --- Part 1: Integer starting points (q=1, standard Collatz) ---
    print("\n--- Part 1: Integer starts (q = 1) ---")
    print(f"{'n':>6} {'steps':>6} {'max_h':>8} {'d_hyp(start)':>12} {'rate':>8}")

    int_steps = []
    for n in [7, 27, 97, 127, 255, 447, 871, 6171]:
        traj = run_trajectory(n, 1)
        steps = len(traj) - 1
        max_h = max(height(p, q) for p, q in traj)
        d0 = hyp_dist(n, 1, 1, 1)
        rate = d0 / steps if steps > 0 else 0
        reached = traj[-1] == (1, 1)
        int_steps.append(steps)
        print(f"{n:>6} {steps:>6} {max_h:>8} {d0:>12.3f} {rate:>8.3f}"
              f"  {'✓' if reached else '✗'}")

    # --- Part 2: Non-integer starting points (q > 1) ---
    print("\n--- Part 2: Non-integer starts (q > 1) ---")
    print(f"{'p/q':>10} {'steps':>6} {'max_h':>8} {'d_hyp':>12} {'rate':>8} {'GCDs':>8}")

    for p0, q0 in [(3, 2), (5, 3), (7, 5), (11, 7), (13, 8),
                    (27, 5), (97, 3), (127, 11), (255, 13), (871, 7)]:
        if gcd(p0, q0) != 1:
            continue
        traj = run_trajectory(p0, q0)
        steps = len(traj) - 1
        max_h = max(height(p, q) for p, q in traj)
        d0 = hyp_dist(p0, q0, 1, 1)
        rate = d0 / steps if steps > 0 else 0
        reached = traj[-1] == (1, 1)

        # Count GCD > 2 reductions (extra cancellation)
        gcds = []
        for i in range(len(traj) - 1):
            p, q = traj[i]
            if p % 2 == 1 and q % 2 == 1:
                g = gcd(3 * p + 1, q + 1)
                gcds.append(g)
        avg_gcd = np.mean(gcds) if gcds else 0

        print(f"{p0}/{q0:>4} {steps:>6} {max_h:>8} {d0:>12.3f} {rate:>8.3f}"
              f"  {avg_gcd:>7.2f}  {'✓' if reached else '✗'}")

    # --- Part 3: Systematic scan of (p, q) with q > 1 ---
    print("\n--- Part 3: Systematic scan (p ≤ 50, q ≤ 20, gcd=1) ---")
    total = 0
    reached_count = 0
    steps_list = []
    rates_by_q = defaultdict(list)

    for q0 in range(1, 21):
        for p0 in range(1, 51):
            if gcd(p0, q0) != 1:
                continue
            traj = run_trajectory(p0, q0, max_steps=10000)
            total += 1
            reached = traj[-1] == (1, 1)
            if reached:
                reached_count += 1
            steps = len(traj) - 1
            steps_list.append(steps)
            d0 = hyp_dist(p0, q0, 1, 1)
            if steps > 0:
                rates_by_q[q0].append(d0 / steps)

    print(f"Total tested: {total}")
    print(f"Reached (1,1): {reached_count} ({100*reached_count/total:.1f}%)")
    print(f"Steps: mean={np.mean(steps_list):.1f}, max={max(steps_list)}")

    print(f"\nContraction rate by denominator q:")
    print(f"{'q':>4} {'count':>6} {'mean_rate':>10} {'std':>10}")
    for q0 in sorted(rates_by_q):
        r = rates_by_q[q0]
        print(f"{q0:>4} {len(r):>6} {np.mean(r):>10.4f} {np.std(r):>10.4f}")

    # --- Part 4: Hyperbolic distance trajectory for a specific case ---
    print("\n--- Part 4: Distance trajectory for 27/1 and 27/5 ---")
    for p0, q0 in [(27, 1), (27, 5)]:
        traj = run_trajectory(p0, q0)
        print(f"\n  {p0}/{q0} → (1,1) in {len(traj)-1} steps")
        print(f"  {'step':>5} {'p/q':>12} {'h':>6} {'d_hyp':>8}")
        sample = list(range(0, min(len(traj), 15))) + [len(traj) - 1]
        for i in sorted(set(sample)):
            if i < len(traj):
                p, q = traj[i]
                h = height(p, q)
                d = hyp_dist(p, q, 1, 1)
                print(f"  {i:>5} {p}/{q:<8} {h:>6} {d:>8.3f}")

    # --- Part 5: Height contraction ratio ---
    print("\n--- Part 5: Per-step height ratio h(t+1)/h(t) ---")
    for p0, q0 in [(27, 1), (27, 5), (871, 7)]:
        traj = run_trajectory(p0, q0)
        ratios = []
        for i in range(len(traj) - 1):
            h0 = height(*traj[i])
            h1 = height(*traj[i + 1])
            if h0 > 0:
                ratios.append(h1 / h0)
        if ratios:
            geo_mean = np.exp(np.mean(np.log(ratios)))
            print(f"  {p0}/{q0}: geometric mean h-ratio = {geo_mean:.4f}"
                  f"  (< 1 = contracting, {len(traj)-1} steps)")

    print()
    print("=" * 72)
    print("Interpretation")
    print("=" * 72)
    print()
    print("If q>1 trajectories converge FASTER (higher rate, lower h-ratio)")
    print("than q=1 trajectories, the denominator dimension accelerates")
    print("contraction. The integer case (q=1) is the slowest — the 'worst'")
    print("boundary of a 2D contracting flow on H².")


if __name__ == "__main__":
    main()
