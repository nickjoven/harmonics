"""
Zoom into the golden ratio region of the devil's staircase.

The Fibonacci convergents to 1/φ = 0.6180339887... are:
    1/2, 2/3, 3/5, 5/8, 8/13, 13/21, 21/34, ...

The pivot scale may sit at or near 1/φ — the most irrational
frequency, maximally resistant to mode-locking, in the widest
gap of the devil's staircase.

Usage:
    python sync_cost/derivations/golden_ratio_pivot.py
"""

import math


PHI = (1 + math.sqrt(5)) / 2  # 1.6180339887...
INV_PHI = 1 / PHI              # 0.6180339887...
INV_PHI_SQ = 1 / PHI**2        # 0.3819660113...


def arnold_tongue_width(p, q, coupling=1.0):
    """Width of Arnold tongue for ratio p/q."""
    return coupling ** q / q


def gaussian(x, mu, sigma):
    return math.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * math.sqrt(2 * math.pi))


def smooth_staircase_density(omega, n_max=12, coupling=0.8):
    """
    g(ω) from Arnold tongues, with deeper rational resolution.
    """
    density = 0.0
    for q in range(1, n_max + 1):
        for p in range(0, q + 1):
            if math.gcd(p, q) != 1:
                continue
            center = p / q
            w = arnold_tongue_width(p, q, coupling)
            sigma = max(w * 0.3, 0.001)
            density += w * gaussian(omega, center, sigma)
    return density


def ln_power(omega, n_max=12, coupling=0.8):
    """ln P(ω) = ln g(ω) (ignoring constant Kr² term)."""
    g = smooth_staircase_density(omega, n_max, coupling)
    if g <= 0:
        return -100.0
    return math.log(g)


def tilt_and_running(omega, n_max=12, coupling=0.8):
    """Numerical n_s - 1 and running at omega."""
    h = 1e-5 * omega
    ln_om = math.log(omega)

    def lnP_at(ln_o):
        return ln_power(math.exp(ln_o), n_max, coupling)

    f0 = lnP_at(ln_om)
    fp = lnP_at(ln_om + h / omega)
    fm = lnP_at(ln_om - h / omega)

    dlnk = h / omega
    tilt = (fp - fm) / (2 * dlnk)
    running = (fp - 2 * f0 + fm) / dlnk**2

    return tilt, running


if __name__ == "__main__":
    print("=" * 80)
    print("  GOLDEN RATIO PIVOT: ZOOM INTO THE NOBLE GAP")
    print("=" * 80)
    print(f"\n  1/φ   = {INV_PHI:.10f}")
    print(f"  1/φ²  = {INV_PHI_SQ:.10f}")
    print(f"  3/5   = {3/5:.10f}")
    print(f"  5/8   = {5/8:.10f}")
    print(f"  8/13  = {8/13:.10f}")
    print(f"  2/3   = {2/3:.10f}")

    # --- 1. Fine scan: 0.580 to 0.680 ---
    print(f"\n{'─'*80}")
    print("  1. FINE SCAN: ω = 0.580 to 0.680 (the golden ratio neighborhood)")
    print(f"{'─'*80}")
    print(f"\n  {'ω':>10s}  {'g(ω)':>10s}  {'n_s-1':>10s}  {'running':>10s}  {'note':>20s}")
    print("  " + "-" * 70)

    for i in range(101):
        omega = 0.580 + i * 0.001
        g = smooth_staircase_density(omega, n_max=12, coupling=0.8)
        tilt, run = tilt_and_running(omega, n_max=12, coupling=0.8)

        note = ""
        if abs(omega - INV_PHI) < 0.001:
            note = "<<< 1/φ >>>"
        elif abs(omega - 3/5) < 0.001:
            note = "3/5"
        elif abs(omega - 5/8) < 0.001:
            note = "5/8"
        elif abs(omega - 8/13) < 0.002:
            note = "8/13"
        elif abs(omega - 13/21) < 0.002:
            note = "13/21"
        elif abs(omega - 2/3) < 0.001:
            note = "2/3"

        # Print every 5th point, plus all notable ones
        if i % 5 == 0 or note or (run < 0 and -0.06 < tilt < -0.02):
            marker = " *" if (run < 0 and -0.06 < tilt < -0.02) else ""
            print(f"  {omega:10.4f}  {g:10.4f}  {tilt:+10.4f}  {run:+10.4f}  {note:>20s}{marker}")

    # --- 2. Ultra-fine scan around 1/φ ---
    print(f"\n{'─'*80}")
    print(f"  2. ULTRA-FINE SCAN: ω = 1/φ ± 0.01")
    print(f"{'─'*80}")
    print(f"\n  {'ω':>12s}  {'g(ω)':>10s}  {'n_s-1':>10s}  {'running':>10s}  {'ω - 1/φ':>12s}")
    print("  " + "-" * 65)

    for i in range(41):
        omega = INV_PHI - 0.010 + i * 0.0005
        g = smooth_staircase_density(omega, n_max=12, coupling=0.8)
        tilt, run = tilt_and_running(omega, n_max=12, coupling=0.8)
        delta = omega - INV_PHI
        marker = " ***" if (run < 0 and -0.045 < tilt < -0.025) else ""
        if i % 4 == 0 or marker or abs(delta) < 0.001:
            print(f"  {omega:12.6f}  {g:10.4f}  {tilt:+10.4f}  {run:+10.4f}  {delta:+12.6f}{marker}")

    # --- 3. At exactly 1/φ ---
    print(f"\n{'─'*80}")
    print(f"  3. AT EXACTLY 1/φ = {INV_PHI:.10f}")
    print(f"{'─'*80}")

    g_phi = smooth_staircase_density(INV_PHI, n_max=12, coupling=0.8)
    tilt_phi, run_phi = tilt_and_running(INV_PHI, n_max=12, coupling=0.8)
    print(f"\n  g(1/φ)   = {g_phi:.6f}")
    print(f"  n_s - 1  = {tilt_phi:+.6f}")
    print(f"  running  = {run_phi:+.6f}")
    print(f"\n  Planck:  n_s - 1 = -0.0351, running = -0.0045 ± 0.0067")

    # --- 4. What if n_s - 1 = -0.035 isn't AT 1/φ but ENCODES 1/φ? ---
    print(f"\n{'─'*80}")
    print(f"  4. DOES n_s - 1 ENCODE THE GOLDEN RATIO?")
    print(f"{'─'*80}")

    ns_observed = 0.9649
    tilt_observed = ns_observed - 1  # -0.0351

    print(f"\n  n_s = {ns_observed}")
    print(f"  n_s - 1 = {tilt_observed}")
    print(f"  1 - n_s = {1 - ns_observed}")
    print(f"\n  Ratios involving φ:")
    print(f"  1/(φ^8)        = {1/PHI**8:.6f}")
    print(f"  1/(8φ²)        = {1/(8*PHI**2):.6f}")
    print(f"  (1-1/φ)/φ^3    = {(1 - INV_PHI)/PHI**3:.6f}")
    print(f"  1/(4π φ²)      = {1/(4*math.pi*PHI**2):.6f}")
    print(f"  2/(φ^7)        = {2/PHI**7:.6f}")
    print(f"  1 - n_s        = {1 - ns_observed:.6f}")

    # Fibonacci connection
    print(f"\n  Fibonacci numbers: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89")
    print(f"  F_n/F_{'{n+1}'} converges to 1/φ:")
    fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for i in range(len(fibs) - 1):
        ratio = fibs[i] / fibs[i + 1]
        print(f"    {fibs[i]:>3d}/{fibs[i+1]:<3d} = {ratio:.10f}  "
              f"(error from 1/φ: {abs(ratio - INV_PHI):.2e})")

    # --- 5. Coupling scan at 1/φ ---
    print(f"\n{'─'*80}")
    print(f"  5. COUPLING SCAN AT ω = 1/φ")
    print(f"{'─'*80}")
    print(f"\n  How do tilt and running at 1/φ depend on coupling strength?")
    print(f"\n  {'K':>6s}  {'g(1/φ)':>10s}  {'n_s-1':>10s}  {'running':>10s}  {'n_s':>8s}")
    print("  " + "-" * 55)

    for K_100 in range(30, 160, 5):
        K = K_100 / 100.0
        g = smooth_staircase_density(INV_PHI, n_max=12, coupling=K)
        tilt, run = tilt_and_running(INV_PHI, n_max=12, coupling=K)
        ns = 1 + tilt
        marker = ""
        if abs(ns - 0.9649) < 0.005:
            marker = " <<<"
        print(f"  {K:6.2f}  {g:10.4f}  {tilt:+10.4f}  {run:+10.4f}  {ns:8.4f}{marker}")

    # --- 6. Depth scan at 1/φ ---
    print(f"\n{'─'*80}")
    print(f"  6. RATIONAL DEPTH SCAN AT ω = 1/φ, K = 0.8")
    print(f"{'─'*80}")
    print(f"\n  How does including deeper rationals change the picture?")
    print(f"\n  {'n_max':>6s}  {'g(1/φ)':>10s}  {'n_s-1':>10s}  {'running':>10s}")
    print("  " + "-" * 45)

    for n_max in range(3, 22):
        g = smooth_staircase_density(INV_PHI, n_max=n_max, coupling=0.8)
        tilt, run = tilt_and_running(INV_PHI, n_max=n_max, coupling=0.8)
        # Mark Fibonacci depths
        fib_note = ""
        if n_max in [3, 5, 8, 13, 21]:
            fib_note = f" (Fibonacci)"
        print(f"  {n_max:6d}  {g:10.4f}  {tilt:+10.4f}  {run:+10.4f}{fib_note}")

    # --- 7. Summary ---
    print(f"\n{'='*80}")
    print("  SUMMARY")
    print(f"{'='*80}")
    print(f"""
  The golden ratio 1/φ = 0.618... sits in the widest gap of the
  devil's staircase — the frequency most resistant to mode-locking.

  The Fibonacci convergents bracket it:
    3/5 = 0.600 < 5/8 = 0.625 < 8/13 = 0.615 < 1/φ = 0.618...
    2/3 = 0.667 > 5/8 = 0.625 > 8/13 = 0.615 > 1/φ = 0.618...

  If the CMB pivot scale sits at 1/φ on the frequency axis:
    - It's maximally between locked states (noble number)
    - The tilt comes from the staircase slope at the noble gap
    - The running sign depends on the curvature of the gap
    - The KAM theorem says this is the last torus to break

  The spectral tilt would then encode the universe's proximity to
  the golden ratio — the most unlocked frequency, the edge of chaos.
""")
