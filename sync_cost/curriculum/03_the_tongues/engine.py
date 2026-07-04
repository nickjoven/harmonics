#!/usr/bin/env python3
"""
Module 3 — The tongues.

Module 2 drove two oscillators into a single 1:1 lock and saw its locked
band widen into a wedge. This module drives ONE oscillator with a periodic
rhythm and watches it once per beat of the driver. Now it can lock at any
whole-number ratio p:q — p of its cycles for every q of the driver's — and
the map of where it locks, across all driving rates and all coupling
strengths, is a whole family of wedges, one over every ratio.

The once-per-beat rule (the "sine circle map"):

    θ_{n+1} = θ_n + Ω − (K / 2π) sin(2π θ_n)

  θ  — the oscillator's phase, read once per beat of the driver
  Ω  — the bare rate: cycles the oscillator would advance per beat if the
       coupling K were switched off (this is the tunable frequency ratio)
  K  — coupling strength (0 = free, 1 = critical)

The locking ratio is the average phase advance per beat:

    ρ = lim (θ_N − θ_0) / N

At K = 0, ρ = Ω exactly (free running). At K > 0, ρ sticks to whole-number
ratios p/q over whole intervals of Ω — the wedges.

Three demonstrations:
  - "staircase" — fix K, sweep Ω: ρ climbs in flat steps (a staircase of
                  locked ratios); the widest step is the simplest ratio.
  - "widths"    — measure step widths and confirm they order by denominator:
                  1/2 widest, then 1/3 & 2/3, then quarters, then fifths.
  - "wedge"     — map one ratio's locked region in the (Ω, K) plane and watch
                  it open into a wedge rising from the K = 0 axis.

Pure standard library.
"""
import argparse
import math

TWO_PI = 2.0 * math.pi


def circle_step(theta, Omega, K):
    return theta + Omega - (K / TWO_PI) * math.sin(TWO_PI * theta)


def rotation_number(Omega, K, n_iter=3000, transient=800):
    """Average phase advance per beat. θ kept as a lift (no mod); sin is periodic."""
    theta = 0.0
    for _ in range(transient):
        theta = circle_step(theta, Omega, K)
    theta_start = theta
    for _ in range(n_iter):
        theta = circle_step(theta, Omega, K)
    return (theta - theta_start) / n_iter


# --------------------------------------------------------------------------- #
# Demo A — the staircase of locked ratios
# --------------------------------------------------------------------------- #

def demo_staircase():
    print("=" * 70)
    print("A — the staircase of locked ratios (fix coupling, sweep the rate)")
    print("=" * 70)
    print()
    K = 1.0
    print(f"Coupling K = {K:.2f} (critical). Sweep the bare rate Ω from 0 to 1")
    print("and measure the locking ratio ρ. An ASCII plot of ρ (vertical, 0 at")
    print("bottom to 1 at top) against Ω (horizontal, 0 to 1):")
    print()

    cols = 68
    rows = 22
    samples = []
    for c in range(cols):
        Omega = c / (cols - 1)
        rho = rotation_number(Omega, K)
        samples.append((Omega, rho))

    # build grid
    grid = [[" "] * cols for _ in range(rows)]
    for c, (Omega, rho) in enumerate(samples):
        r = int(round((1.0 - min(max(rho, 0.0), 1.0)) * (rows - 1)))
        grid[r][c] = "•"
    for r in range(rows):
        print("   " + "".join(grid[r]))
    print("   " + "-" * cols)
    print(f"   Ω=0{' ' * (cols - 8)}Ω=1")
    print()
    print("The flat runs are locks: over a whole interval of Ω the ratio ρ holds")
    print("fixed at a whole-number value. The longest flat run sits at ρ = 1/2 —")
    print("the simplest interior ratio has the widest lock. Shorter flats appear")
    print("at 1/3 and 2/3, shorter still at the quarters, and so on: the simpler")
    print("the ratio, the wider its step. Between the steps ρ rises smoothly —")
    print("those are the un-locked (quasiperiodic) rates.")
    print()


# --------------------------------------------------------------------------- #
# Demo B — step widths order by denominator
# --------------------------------------------------------------------------- #

def plateau_width(p, q, K, grid=2500, tol=1.5e-3):
    """Fraction of the Ω-axis (0..1) where ρ locks to p/q at this K."""
    target = p / q
    count = 0
    for i in range(grid + 1):
        Omega = i / grid
        rho = rotation_number(Omega, K, n_iter=1500, transient=500)
        if abs(rho - target) < tol:
            count += 1
    return count / (grid + 1)


def demo_widths():
    print("=" * 70)
    print("B — step widths order by denominator (simpler ratio = wider lock)")
    print("=" * 70)
    print()
    K = 1.0
    print(f"Coupling K = {K:.2f}. Measure the width of each lock — the fraction")
    print("of the Ω-axis over which ρ holds at a given ratio p/q — for the")
    print("simplest ratios strictly between 0 and 1:")
    print()
    ratios = [(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (2, 5), (3, 5)]
    print(f"{'ratio p/q':>10}  {'denominator q':>14}  {'lock width':>12}")
    print(f"{'-'*10}  {'-'*14}  {'-'*12}")
    measured = []
    for p, q in ratios:
        w = plateau_width(p, q, K)
        measured.append((p, q, w))
        print(f"{p:>4}/{q:<5}  {q:>14}  {w:>12.4f}")
    print()
    # confirm ordering: q=2 widest, then q=3, then q=4, then q=5
    widest = max(measured, key=lambda t: t[2])
    by_q = {}
    for p, q, w in measured:
        by_q.setdefault(q, []).append(w)
    avg_by_q = {q: sum(ws) / len(ws) for q, ws in by_q.items()}
    print(f"Widest lock: {widest[0]}/{widest[1]}  (width {widest[2]:.4f}).")
    print("Average width by denominator q:")
    for q in sorted(avg_by_q):
        print(f"   q = {q}:  {avg_by_q[q]:.4f}")
    ordered = all(
        avg_by_q[a] > avg_by_q[b]
        for a, b in zip(sorted(avg_by_q), sorted(avg_by_q)[1:])
    )
    print()
    print(f"Width strictly decreases as the denominator grows: "
          f"{'CONFIRMED' if ordered else 'NOT strictly monotone at this resolution'}.")
    print("The lock over the simplest ratio (smallest denominator) is the widest,")
    print("and therefore the most robust — the one that survives the most")
    print("mistuning and the most noise. That is the selection principle the")
    print("rest of the framework rests on: among competing locks, the simplest")
    print("ratio wins.")
    print()


# --------------------------------------------------------------------------- #
# Demo C — one ratio's wedge in the (Ω, K) plane
# --------------------------------------------------------------------------- #

def locked_interval(p, q, K, grid=1000, tol=1.5e-3):
    """Return (Omega_lo, Omega_hi) of the p/q lock at this K, or None."""
    target = p / q
    lo = hi = None
    for i in range(grid + 1):
        Omega = i / grid
        rho = rotation_number(Omega, K, n_iter=1500, transient=500)
        if abs(rho - target) < tol:
            if lo is None:
                lo = Omega
            hi = Omega
    if lo is None:
        return None
    return (lo, hi)


def demo_wedge():
    print("=" * 70)
    print("C — one lock is a wedge in the (rate, coupling) plane")
    print("=" * 70)
    print()
    p, q = 1, 2
    print(f"Track the {p}:{q} lock (ρ = {p}/{q}) as coupling K rises from 0 to 1.")
    print("Each row shows the interval of Ω over which the lock holds at that K.")
    print("Ω runs 0 (left) to 1 (right); '█' marks the locked interval:")
    print()
    width_axis = 60
    print(f"   {'K':>5}   {'0':<1}{' ' * (width_axis - 6)}{'Ω':>1}{' ':>2}{'1':>1}"
          f"   width")
    for k_i in range(1, 11):
        K = k_i / 10.0
        iv = locked_interval(p, q, K)
        line = [" "] * width_axis
        if iv:
            lo, hi = iv
            c_lo = int(round(lo * (width_axis - 1)))
            c_hi = int(round(hi * (width_axis - 1)))
            for c in range(c_lo, c_hi + 1):
                line[c] = "█"
            w = hi - lo
        else:
            w = 0.0
        print(f"   {K:>5.1f}   {''.join(line)}   {w:.4f}")
    print()
    print("The locked interval is a single point (zero width) at K = 0 and opens")
    print(f"steadily as K grows: a wedge rising from Ω = {p}/{q} on the K = 0")
    print("axis. Every whole-number ratio has one. The full plane is filled with")
    print("these wedges — widest over the simplest ratios, narrowing to threads")
    print("over the complicated ones. Module 4 asks which ratio's wedge appears")
    print("BETWEEN two known wedges as coupling weakens — and finds the rule that")
    print("builds them all.")
    print()


# --------------------------------------------------------------------------- #

def main():
    parser = argparse.ArgumentParser(description="Module 3 demonstrations.")
    parser.add_argument(
        "--demo",
        choices=["staircase", "widths", "wedge", "all"],
        default="all",
        help="Which demonstration to run.",
    )
    args = parser.parse_args()

    if args.demo in ("staircase", "all"):
        demo_staircase()
    if args.demo in ("widths", "all"):
        demo_widths()
    if args.demo in ("wedge", "all"):
        demo_wedge()


if __name__ == "__main__":
    main()
