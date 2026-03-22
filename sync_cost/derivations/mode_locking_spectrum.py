"""
Spectral tilt from mode-locking structure.

Instead of P(k) ∝ 1/C(τ), we use P(k) ∝ g(ω) / (Kr)² where g(ω)
is the frequency distribution shaped by Arnold tongues. For sufficient
coupling, g approaches a devil's staircase.

This script:
1. Constructs g(ω) from Farey-mediant / Arnold tongue structure
2. Computes n_s and running as a function of position on the staircase
3. Identifies where on the staircase negative running occurs

Usage:
    python sync_cost/derivations/mode_locking_spectrum.py
"""

import math


# ---------------------------------------------------------------------------
# Devil's staircase construction via Farey mediants
# ---------------------------------------------------------------------------

def farey_sequence(n_max):
    """
    Generate Farey sequence F_n: all rationals p/q with 0 <= p/q <= 1,
    q <= n_max, in ascending order.
    """
    fracs = set()
    for q in range(1, n_max + 1):
        for p in range(0, q + 1):
            if math.gcd(p, q) == 1:
                fracs.add((p, q))
    return sorted(fracs, key=lambda f: f[0] / f[1])


def arnold_tongue_width(p, q, coupling=1.0):
    """
    Width of Arnold tongue for ratio p/q at given coupling.
    Approximate: width ∝ K^q / q (narrower for higher-order rationals).
    """
    return coupling ** q / q


def build_staircase(n_max=8, coupling=0.8, resolution=2000):
    """
    Build a devil's staircase g(ω) on [0, 1].

    At each rational p/q, there's a plateau of width ~ arnold_tongue_width.
    Between plateaus, g interpolates linearly (crude but captures structure).

    Returns (omega_array, g_array) where g is the cumulative distribution
    (staircase), and also (omega_array, density_array) where density is dg/dω.
    """
    rationals = farey_sequence(n_max)

    # Build plateaus: each rational p/q gets a flat segment
    segments = []  # (center, half_width, value)
    for p, q in rationals:
        center = p / q
        hw = arnold_tongue_width(p, q, coupling) * 0.5
        segments.append((center, hw, p / q))

    # Sort by center
    segments.sort(key=lambda s: s[0])

    # Build the staircase by distributing probability mass
    # Each rational p/q gets mass proportional to tongue width
    total_width = sum(2 * s[1] for s in segments)

    omega = []
    g_cumulative = []
    cum = 0.0

    for i, (center, hw, val) in enumerate(segments):
        lo = max(0.0, center - hw)
        hi = min(1.0, center + hw)
        mass = 2 * hw / total_width

        # Transition from previous plateau
        if omega and lo > omega[-1]:
            omega.append(lo)
            g_cumulative.append(cum)

        # Plateau
        omega.append(lo)
        g_cumulative.append(cum)
        cum += mass
        omega.append(hi)
        g_cumulative.append(cum)

    # Normalize
    if g_cumulative:
        g_max = g_cumulative[-1]
        g_cumulative = [g / g_max for g in g_cumulative]

    return omega, g_cumulative


def staircase_density(omega_arr, g_arr, omega_eval):
    """
    Evaluate the density dg/dω at omega_eval by finite difference
    on the staircase. This is the frequency distribution.
    """
    # Find bracketing interval
    eps = 0.005
    lo = max(0.001, omega_eval - eps)
    hi = min(0.999, omega_eval + eps)

    g_lo = interpolate(omega_arr, g_arr, lo)
    g_hi = interpolate(omega_arr, g_arr, hi)

    if hi <= lo:
        return 0.0
    return (g_hi - g_lo) / (hi - lo)


def interpolate(xs, ys, x):
    """Linear interpolation."""
    if x <= xs[0]:
        return ys[0]
    if x >= xs[-1]:
        return ys[-1]
    for i in range(len(xs) - 1):
        if xs[i] <= x <= xs[i + 1]:
            if xs[i + 1] == xs[i]:
                return ys[i]
            t = (x - xs[i]) / (xs[i + 1] - xs[i])
            return ys[i] + t * (ys[i + 1] - ys[i])
    return ys[-1]


# ---------------------------------------------------------------------------
# Smooth approximation to devil's staircase density
# ---------------------------------------------------------------------------

def smooth_staircase_density(omega, n_max=8, coupling=0.8):
    """
    Smooth approximation: g(ω) = Σ_{p/q} w(p,q) × gaussian(ω - p/q, σ(q))

    Each rational p/q contributes a gaussian peak with:
    - Weight w ∝ tongue width ∝ K^q / q
    - Width σ ∝ tongue width

    This is differentiable, so we can compute curvature analytically.
    """
    density = 0.0
    for q in range(1, n_max + 1):
        for p in range(0, q + 1):
            if math.gcd(p, q) != 1:
                continue
            center = p / q
            w = arnold_tongue_width(p, q, coupling)
            sigma = max(w * 0.3, 0.002)
            density += w * gaussian(omega, center, sigma)
    return density


def gaussian(x, mu, sigma):
    """Normalized gaussian."""
    return math.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * math.sqrt(2 * math.pi))


# ---------------------------------------------------------------------------
# Power spectrum from mode-locking density
# ---------------------------------------------------------------------------

def power_from_density(omega, n_max=8, coupling=0.8, Kr_squared=1.0):
    """
    P(ω) ∝ g(ω) / (Kr)²

    For now treat Kr as constant (scale-independent coupling × coherence).
    The spectral structure comes from g alone.
    """
    g = smooth_staircase_density(omega, n_max, coupling)
    return g / Kr_squared


def numerical_tilt_and_running(omega_pivot, n_max=8, coupling=0.8):
    """
    Compute n_s - 1 and running at omega_pivot from the mode-locking
    density, treating ω as proportional to k.

    n_s - 1 = d ln P / d ln ω
    running = d²ln P / (d ln ω)²
    """
    eps = 1e-4 * omega_pivot

    def ln_P(omega):
        p = power_from_density(omega, n_max, coupling)
        if p <= 0:
            return -100.0
        return math.log(p)

    ln_om = math.log(omega_pivot)
    om_p = math.exp(ln_om + eps / omega_pivot)
    om_m = math.exp(ln_om - eps / omega_pivot)

    # Use ln ω steps directly
    h = eps / omega_pivot
    lnP_0 = ln_P(omega_pivot)
    lnP_p = ln_P(om_p)
    lnP_m = ln_P(om_m)

    ns_minus_1 = (lnP_p - lnP_m) / (2 * h)
    running = (lnP_p - 2 * lnP_0 + lnP_m) / h ** 2

    return ns_minus_1, running


# ---------------------------------------------------------------------------
# Main exploration
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 80)
    print("  SPECTRAL TILT FROM MODE-LOCKING STRUCTURE")
    print("=" * 80)

    # --- 1. Show the density structure ---
    print(f"\n{'─'*80}")
    print("  1. FREQUENCY DISTRIBUTION g(ω) from Arnold tongues")
    print(f"{'─'*80}")
    print(f"\n  Coupling K = 0.8, rational depth n_max = 8")
    print(f"\n  {'ω':>8s}  {'g(ω)':>12s}  {'nearest rational':>18s}")
    print("  " + "-" * 45)

    for i in range(21):
        omega = 0.05 + i * 0.045
        g = smooth_staircase_density(omega, n_max=8, coupling=0.8)
        # Find nearest simple rational
        best_p, best_q = 0, 1
        best_dist = abs(omega)
        for q in range(1, 9):
            for p in range(0, q + 1):
                if math.gcd(p, q) == 1:
                    d = abs(omega - p / q)
                    if d < best_dist:
                        best_dist = d
                        best_p, best_q = p, q
        print(f"  {omega:8.3f}  {g:12.4f}  {best_p}/{best_q} (d={best_dist:.3f})")

    # --- 2. Tilt and running across the staircase ---
    print(f"\n{'─'*80}")
    print("  2. TILT AND RUNNING vs position on staircase")
    print(f"{'─'*80}")

    print(f"\n  Scanning ω from 0.1 to 0.9:")
    print(f"\n  {'ω':>8s}  {'g(ω)':>10s}  {'n_s-1':>10s}  {'running':>10s}  {'near':>8s}")
    print("  " + "-" * 55)

    negative_running_regions = []

    for i in range(81):
        omega = 0.1 + i * 0.01
        g = smooth_staircase_density(omega, n_max=8, coupling=0.8)
        try:
            tilt, run = numerical_tilt_and_running(omega, n_max=8, coupling=0.8)
            # Nearest rational
            best_r = ""
            for q in range(1, 6):
                for p in range(0, q + 1):
                    if math.gcd(p, q) == 1 and abs(omega - p / q) < 0.02:
                        best_r = f"{p}/{q}"
            marker = " <--" if run < 0 else ""
            if i % 5 == 0 or run < 0:
                print(f"  {omega:8.3f}  {g:10.4f}  {tilt:+10.4f}  {run:+10.4f}  {best_r:>8s}{marker}")
            if run < 0:
                negative_running_regions.append((omega, tilt, run))
        except (ValueError, ZeroDivisionError):
            pass

    # --- 3. Summary ---
    print(f"\n{'─'*80}")
    print("  3. NEGATIVE RUNNING REGIONS")
    print(f"{'─'*80}")

    if negative_running_regions:
        print(f"\n  Found {len(negative_running_regions)} points with negative running:")
        print(f"\n  {'ω':>8s}  {'n_s-1':>10s}  {'running':>10s}")
        print("  " + "-" * 35)
        for omega, tilt, run in negative_running_regions:
            print(f"  {omega:8.3f}  {tilt:+10.4f}  {run:+10.4f}")

        # Check if any have tilt near -0.035
        matches = [(o, t, r) for o, t, r in negative_running_regions
                   if -0.06 < t < -0.02]
        if matches:
            print(f"\n  *** Points with BOTH n_s ≈ 0.965 AND negative running: ***")
            for omega, tilt, run in matches:
                print(f"      ω = {omega:.3f}, n_s - 1 = {tilt:+.4f}, running = {run:+.4f}")
        else:
            print(f"\n  No points simultaneously match n_s ≈ 0.965 and negative running.")
            print(f"  Tilt range in negative-running regions: "
                  f"{min(t for _,t,_ in negative_running_regions):+.4f} to "
                  f"{max(t for _,t,_ in negative_running_regions):+.4f}")
    else:
        print(f"\n  No negative running found at this coupling/depth.")
        print(f"  Try adjusting coupling or n_max.")

    # --- 4. Coupling scan ---
    print(f"\n{'─'*80}")
    print("  4. COUPLING SCAN — does stronger coupling change running sign?")
    print(f"{'─'*80}")

    print(f"\n  Scanning coupling K from 0.3 to 1.5, evaluating at ω = 0.4")
    print(f"  (near 2/5, between 1/3 and 1/2 — a transition region)")
    print(f"\n  {'K':>6s}  {'g(0.4)':>10s}  {'n_s-1':>10s}  {'running':>10s}")
    print("  " + "-" * 45)

    for K_10 in range(3, 16):
        K = K_10 / 10.0
        g = smooth_staircase_density(0.4, n_max=8, coupling=K)
        try:
            tilt, run = numerical_tilt_and_running(0.4, n_max=8, coupling=K)
            marker = " <-- NEG" if run < 0 else ""
            print(f"  {K:6.2f}  {g:10.4f}  {tilt:+10.4f}  {run:+10.4f}{marker}")
        except (ValueError, ZeroDivisionError):
            pass

    # --- 5. Physical interpretation ---
    print(f"\n{'='*80}")
    print("  INTERPRETATION")
    print(f"{'='*80}")
    print("""
  The frequency distribution g(ω) from Arnold tongues is a sum of
  peaks at rational frequencies. Between peaks, g drops — these are
  the transition regions.

  On the ASCENDING side of a peak (approaching a rational from below):
    d ln g / d ln ω > 0  (blue tilt locally)
    d² ln g / (d ln ω)² can be < 0 (concave — negative running)

  On the DESCENDING side of a peak (moving away from a rational):
    d ln g / d ln ω < 0  (red tilt locally)
    d² ln g / (d ln ω)² can be > 0 (convex — positive running)

  The OBSERVED spectral tilt (red, n_s < 1) with negative running
  places the pivot scale on the DESCENDING side of a peak BUT in
  a region where the descent is ACCELERATING (concave envelope).

  This happens naturally between two widely-spaced rationals where
  the envelope of g curves downward — the system is "falling off"
  one locked plateau and hasn't yet reached the next.

  Key insight: the running sign is not determined by the overall
  shape of g, but by the LOCAL curvature at the pivot. The devil's
  staircase has both convex and concave regions. The smooth "cost
  function" approximation washed out this structure.
""")
