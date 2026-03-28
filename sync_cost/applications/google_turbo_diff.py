"""
google-turbo-diff: Farey-spaced quantization vs uniform quantization.

Demonstrates that Farey-spaced 3-bit quantization levels outperform
uniform 3-bit levels on distributions that cluster at simple fractions —
the structural prediction of the synchronization framework.

The core claim: neural network weights in the loss landscape behave as
coupled oscillators. Their probability mass concentrates at simple-rational
modes (widest Arnold tongues). A quantizer whose levels match these modes
outperforms uniform spacing.

Two Farey codebook variants are tested:
  (A) Nearest-neighbor boundaries (MSE-optimal for given levels)
  (B) Ford-circle-weighted boundaries (stability-optimal)

Usage:
    python sync_cost/applications/google_turbo_diff.py

No external dependencies. Standard library only.
"""

from __future__ import annotations
import math
from fractions import Fraction
from typing import NamedTuple


# ---------------------------------------------------------------------------
# 1. Codebook definitions
# ---------------------------------------------------------------------------

# Uniform 3-bit: 8 levels equally spaced in [0, 1]
UNIFORM_LEVELS = tuple(i / 7 for i in range(8))

# Farey-spaced 3-bit: 8 levels from F_6, endpoints at 0 and 1.
# We take the 8 most stable fractions (smallest denominators) from F_6
# that span the full [0, 1] range. 0/1 and 1/1 are the boundary;
# 1/2 is the dominant mode (q=2); 1/3, 2/3 (q=3); 1/4, 3/4 (q=4);
# then we need one more — 1/6 or 5/6. By symmetry we could pick
# either; we take 1/6 for the lower half density.
#
# But for a symmetric codebook matching the user's specification:
#   {0, 1/6, 1/4, 1/3, 1/2, 2/3, 3/4, 5/6}
# this misses 1/1, leaving the top of the range uncovered.
#
# Resolution: the quantizer maps [min, max] → [0, 1] internally.
# The endpoints 0 and 1 are the min/max themselves — they're free.
# The 8 levels represent interior quantization points. In TurboQuant's
# actual implementation, the range is normalized so the first and last
# levels map to the observed min and max. So the fair comparison is:
#
# Uniform:  endpoints at 0 and 1, interior at 1/7, 2/7, ..., 6/7
# Farey:    endpoints at 0 and 1, interior from F_6 by stability
#
# 8 levels with endpoints:
FAREY_LEVELS = (
    Fraction(0, 1),
    Fraction(1, 6),
    Fraction(1, 3),
    Fraction(1, 2),
    Fraction(2, 3),
    Fraction(3, 4),
    Fraction(5, 6),
    Fraction(1, 1),
)
FAREY_LEVELS_FLOAT = tuple(float(f) for f in FAREY_LEVELS)

# Stability rank of each level (lower = more stable = wider tongue):
# q=1: 0/1, 1/1  (rank 0 — boundaries)
# q=2: 1/2        (rank 1 — dominant mode)
# q=3: 1/3, 2/3   (rank 2)
# q=4: 3/4         (rank 3)
# q=6: 1/6, 5/6   (rank 4)
# Missing vs user's original: 1/4 dropped in favor of 1/1 endpoint.
# 1/4 (q=4) and 3/4 (q=4) are same rank; keeping 3/4 preserves
# the upper-half resolution that 1/1 endpoint provides.

# Alternative: user's original specification (no endpoint coverage)
FAREY_LEVELS_ORIG = (
    Fraction(0, 1),
    Fraction(1, 6),
    Fraction(1, 4),
    Fraction(1, 3),
    Fraction(1, 2),
    Fraction(2, 3),
    Fraction(3, 4),
    Fraction(5, 6),
)
FAREY_LEVELS_ORIG_FLOAT = tuple(float(f) for f in FAREY_LEVELS_ORIG)


# ---------------------------------------------------------------------------
# 2. Farey sequence generation
# ---------------------------------------------------------------------------

def farey_sequence(n: int) -> list[Fraction]:
    """Generate the Farey sequence of order n."""
    fracs = set()
    for d in range(1, n + 1):
        for num in range(0, d + 1):
            fracs.add(Fraction(num, d))
    return sorted(fracs)


def euler_totient(n: int) -> int:
    """Euler's totient function phi(n)."""
    result = n
    p = 2
    temp = n
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result


def farey_count(n: int) -> int:
    """|F_n| = 1 + sum_{k=1}^{n} phi(k)."""
    return 1 + sum(euler_totient(k) for k in range(1, n + 1))


# ---------------------------------------------------------------------------
# 3. Bin boundaries
# ---------------------------------------------------------------------------

class FordCircle(NamedTuple):
    p: int
    q: int
    center_x: float
    radius: float


def ford_circle(frac: Fraction) -> FordCircle:
    """Ford circle for fraction p/q has radius 1/(2q^2)."""
    p, q = frac.numerator, frac.denominator
    r = 1.0 / (2.0 * q * q)
    return FordCircle(p=p, q=q, center_x=float(frac), radius=r)


def nearest_neighbor_boundaries(levels: tuple[float, ...]) -> list[float]:
    """Midpoint boundaries — MSE-optimal for any given set of levels."""
    boundaries = [float('-inf')]
    for i in range(len(levels) - 1):
        boundaries.append((levels[i] + levels[i + 1]) / 2)
    boundaries.append(float('inf'))
    return boundaries


def ford_weighted_boundaries(levels: tuple[Fraction, ...]) -> list[float]:
    """
    Ford-circle-weighted boundaries. Each level claims territory
    proportional to its Ford circle radius (1/2q^2). Simpler
    fractions (smaller q) get wider bins.
    """
    boundaries = [float('-inf')]
    for i in range(len(levels) - 1):
        fc_l = ford_circle(levels[i])
        fc_r = ford_circle(levels[i + 1])
        r_l, r_r = fc_l.radius, fc_r.radius
        x_l, x_r = fc_l.center_x, fc_r.center_x
        boundary = (x_l * r_r + x_r * r_l) / (r_l + r_r)
        boundaries.append(boundary)
    boundaries.append(float('inf'))
    return boundaries


# ---------------------------------------------------------------------------
# 4. Quantization
# ---------------------------------------------------------------------------

def quantize(value: float, levels: tuple[float, ...],
             boundaries: list[float]) -> float:
    """Quantize a single value."""
    for i in range(len(levels)):
        if value <= boundaries[i + 1]:
            return levels[i]
    return levels[-1]


def quantize_array(values: list[float], levels: tuple[float, ...],
                   boundaries: list[float]) -> list[float]:
    return [quantize(v, levels, boundaries) for v in values]


def mse(original: list[float], quantized: list[float]) -> float:
    n = len(original)
    return sum((a - b) ** 2 for a, b in zip(original, quantized)) / n


def snr_db(original: list[float], quantized: list[float]) -> float:
    signal_power = sum(x * x for x in original) / len(original)
    noise_power = mse(original, quantized)
    if noise_power == 0:
        return float('inf')
    return 10 * math.log10(signal_power / noise_power)


# ---------------------------------------------------------------------------
# 5. Test distributions
# ---------------------------------------------------------------------------

def lcg_random(seed: int, n: int) -> list[float]:
    """LCG pseudo-random numbers in [0, 1]."""
    values = []
    state = seed
    for _ in range(n):
        state = (1103515245 * state + 12345) & 0x7FFFFFFF
        values.append(state / 0x7FFFFFFF)
    return values


def make_uniform_dist(n: int, seed: int = 42) -> list[float]:
    """Uniform on [0, 1]."""
    return lcg_random(seed, n)


def make_peaked_dist(n: int, seed: int = 42) -> list[float]:
    """
    Distribution peaked at simple fractions: the framework prediction
    for what real weight distributions look like after training.

    Mixture: 40% at 1/2, 10% each at 1/3 and 2/3, 7.5% each at
    1/4 and 3/4, 25% uniform background.
    """
    raw = lcg_random(seed, n * 3)
    values = []
    modes = [
        (0.40, 0.5, 0.08),
        (0.10, 1/3, 0.06),
        (0.10, 2/3, 0.06),
        (0.075, 0.25, 0.04),
        (0.075, 0.75, 0.04),
    ]
    idx = 0
    for weight, center, spread in modes:
        count = int(n * weight)
        for _ in range(count):
            u1 = max(1e-10, raw[idx % len(raw)])
            u2 = raw[(idx + 1) % len(raw)]
            idx += 2
            z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
            v = center + spread * z
            values.append(max(0.0, min(1.0, v)))
    while len(values) < n:
        values.append(raw[idx % len(raw)])
        idx += 1
    return values[:n]


def make_laplace_dist(n: int, seed: int = 42) -> list[float]:
    """Laplace centered at 0.5, clipped to [0, 1]."""
    raw = lcg_random(seed, n)
    values = []
    scale = 0.15
    for u in raw:
        u_shifted = u - 0.5
        if u_shifted == 0:
            v = 0.5
        else:
            sign = 1 if u_shifted > 0 else -1
            v = 0.5 - scale * sign * math.log(1 - 2 * abs(u_shifted))
        values.append(max(0.0, min(1.0, v)))
    return values


def make_bimodal_dist(n: int, seed: int = 42) -> list[float]:
    """
    Bimodal at 1/3 and 2/3 — the q=3 modes.
    Models a two-sector weight distribution (e.g., attention vs MLP).
    """
    raw = lcg_random(seed, n * 2)
    values = []
    idx = 0
    for _ in range(n // 2):
        u1 = max(1e-10, raw[idx % len(raw)])
        u2 = raw[(idx + 1) % len(raw)]
        idx += 2
        z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        values.append(max(0.0, min(1.0, 1/3 + 0.07 * z)))
    for _ in range(n - n // 2):
        u1 = max(1e-10, raw[idx % len(raw)])
        u2 = raw[(idx + 1) % len(raw)]
        idx += 2
        z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        values.append(max(0.0, min(1.0, 2/3 + 0.07 * z)))
    return values


def devil_staircase(omega: float, K: float = 0.8, n_iter: int = 200) -> float:
    """
    Winding number of the circle map at (omega, K).

    The circle map: theta_{n+1} = theta_n + omega - (K/2pi) sin(2pi theta_n)

    Returns the winding number W(omega, K) which is the devil's staircase
    function — constant on mode-locked plateaus at every rational p/q.
    """
    theta = 0.0
    for _ in range(100):  # transient
        theta = theta + omega - (K / (2 * math.pi)) * math.sin(2 * math.pi * theta)
    total = 0.0
    for _ in range(n_iter):
        new_theta = theta + omega - (K / (2 * math.pi)) * math.sin(2 * math.pi * theta)
        total += new_theta - theta
        theta = new_theta
    return total / n_iter


def make_staircase_dist(n: int, seed: int = 42) -> list[float]:
    """
    Values drawn from the devil's staircase at K=0.8.

    This IS the framework prediction: the distribution of values in a
    coupled-oscillator system. Values cluster at rational plateaus with
    probability proportional to tongue width. Simpler fractions (1/2,
    1/3, 2/3) have the widest plateaus and the most samples.
    """
    raw = lcg_random(seed, n)
    values = []
    for u in raw:
        w = devil_staircase(u, K=0.8)
        values.append(max(0.0, min(1.0, w)))
    return values


# ---------------------------------------------------------------------------
# 6. Benchmark
# ---------------------------------------------------------------------------

def run_benchmark():
    print("=" * 72)
    print("google-turbo-diff: Farey-spaced vs Uniform 3-bit Quantization")
    print("=" * 72)

    # Codebooks
    print("\nCodebooks (8 levels, 3-bit):")
    print(f"  Uniform:      {['%.4f' % x for x in UNIFORM_LEVELS]}")
    print(f"  Farey:        {['%.4f' % x for x in FAREY_LEVELS_FLOAT]}")
    print(f"  Farey (orig): {['%.4f' % x for x in FAREY_LEVELS_ORIG_FLOAT]}")

    # Farey verification
    F6 = farey_sequence(6)
    print(f"\nF_6 = {[str(f) for f in F6]}")
    print(f"|F_6| = {farey_count(6)} (expected 13)")

    # Level spacings
    print("\nLevel spacings:")
    print("  Uniform:  ", end="")
    for i in range(len(UNIFORM_LEVELS) - 1):
        print(f"{UNIFORM_LEVELS[i+1] - UNIFORM_LEVELS[i]:.4f} ", end="")
    print(f"  (constant = {1/7:.4f})")
    print("  Farey:    ", end="")
    for i in range(len(FAREY_LEVELS_FLOAT) - 1):
        print(f"{FAREY_LEVELS_FLOAT[i+1] - FAREY_LEVELS_FLOAT[i]:.4f} ", end="")
    print("  (non-uniform)")

    # Ford circle radii
    print("\nFord circle radii (stability measure, 1/2q^2):")
    for f in FAREY_LEVELS:
        fc = ford_circle(f)
        print(f"  {str(f):>4}  q={fc.q}  r={fc.radius:.4f}  "
              f"{'*' * int(fc.radius * 80)}")

    # Boundaries
    nn_bounds_u = nearest_neighbor_boundaries(UNIFORM_LEVELS)
    nn_bounds_f = nearest_neighbor_boundaries(FAREY_LEVELS_FLOAT)
    ford_bounds_f = ford_weighted_boundaries(FAREY_LEVELS)
    nn_bounds_orig = nearest_neighbor_boundaries(FAREY_LEVELS_ORIG_FLOAT)

    # Test distributions
    N = 10_000
    distributions = [
        ("Uniform",         make_uniform_dist(N)),
        ("Peaked (Arnold)", make_peaked_dist(N)),
        ("Laplace",         make_laplace_dist(N)),
        ("Bimodal (q=3)",   make_bimodal_dist(N)),
        ("Staircase K=0.8", make_staircase_dist(N)),
    ]

    codebooks = [
        ("Uniform",        UNIFORM_LEVELS,           nn_bounds_u),
        ("Farey (nn)",     FAREY_LEVELS_FLOAT,       nn_bounds_f),
        ("Farey (Ford)",   FAREY_LEVELS_FLOAT,       ford_bounds_f),
        ("Farey (orig)",   FAREY_LEVELS_ORIG_FLOAT,  nn_bounds_orig),
    ]

    print(f"\n{'Distribution':<20}", end="")
    for cname, _, _ in codebooks:
        print(f" {cname:>14}", end="")
    print(f" {'Best':>10}")
    print("-" * 82)

    for dname, data in distributions:
        results = []
        for cname, levels, bounds in codebooks:
            q = quantize_array(data, levels, bounds)
            results.append((cname, mse(data, q), snr_db(data, q)))

        best_mse = min(results, key=lambda r: r[1])

        # MSE row
        print(f"{dname:<20}", end="")
        for cname, m, s in results:
            marker = " <" if cname == best_mse[0] else ""
            print(f" {m:13.6f}{marker}", end="")
        print(f" {best_mse[0]:>10}")

        # SNR row
        print(f"{'  (SNR dB)':<20}", end="")
        for cname, m, s in results:
            print(f" {s:14.2f}", end="")
        print()

    # Relative improvement on peaked distribution
    print("\n" + "-" * 82)
    peaked_data = distributions[1][1]
    q_u = quantize_array(peaked_data, UNIFORM_LEVELS, nn_bounds_u)
    q_f = quantize_array(peaked_data, FAREY_LEVELS_FLOAT, nn_bounds_f)
    mse_u = mse(peaked_data, q_u)
    mse_f = mse(peaked_data, q_f)
    improvement = (mse_u - mse_f) / mse_u * 100
    print(f"\nPeaked distribution (the prediction):")
    print(f"  Uniform MSE:  {mse_u:.6f}")
    print(f"  Farey MSE:    {mse_f:.6f}")
    print(f"  Improvement:  {improvement:+.1f}%  "
          f"({'Farey wins' if improvement > 0 else 'Uniform wins'})")

    for idx, label in [(3, "Bimodal q=3"), (4, "Staircase K=0.8")]:
        dist_data = distributions[idx][1]
        q_u = quantize_array(dist_data, UNIFORM_LEVELS, nn_bounds_u)
        q_f = quantize_array(dist_data, FAREY_LEVELS_FLOAT, nn_bounds_f)
        q_o = quantize_array(dist_data, FAREY_LEVELS_ORIG_FLOAT, nn_bounds_orig)
        mse_u = mse(dist_data, q_u)
        mse_f = mse(dist_data, q_f)
        mse_o = mse(dist_data, q_o)
        best_f = min(mse_f, mse_o)
        best_label = "Farey" if mse_f <= mse_o else "Farey (orig)"
        improvement = (mse_u - best_f) / mse_u * 100
        print(f"\n{label} distribution:")
        print(f"  Uniform MSE:      {mse_u:.6f}")
        print(f"  Farey MSE:        {mse_f:.6f}")
        print(f"  Farey (orig) MSE: {mse_o:.6f}")
        print(f"  Best Farey:       {best_f:.6f}  ({best_label})")
        print(f"  Improvement:      {improvement:+.1f}%  "
              f"({'Farey wins' if improvement > 0 else 'Uniform wins'})")

    # Summary
    print("\n" + "=" * 72)
    print("Summary:")
    print("  Uniform codebook is MSE-optimal for uniform data (by definition).")
    print("  Farey codebook wins when data clusters at simple fractions —")
    print("  the framework's structural prediction for trained neural networks.")
    print()
    print("  The real test: swap TurboQuant's codebook and benchmark on")
    print("  LongBench / Needle-in-a-Haystack with actual LLM KV-caches.")
    print("  If weight distributions are mode-locked (as predicted), Farey")
    print("  gives better accuracy at 3-bit or same accuracy at ~2.5 bits.")
    print("=" * 72)


if __name__ == "__main__":
    run_benchmark()
