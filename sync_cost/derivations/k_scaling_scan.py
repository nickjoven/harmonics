"""
K-scaling scan: how the Arnold-tongue spectrum evolves from K = 0
(pure rotation) through K = 1 (critical) toward chaos.

Motivation. `observer_register_closure.md` Section 7 logs an open
candidate: "K-variation as unifying axis -- whether H-reg (6 * 13^54)
and P-reg (19 states at Farey depth 7) are K-slices of a single
register structure." The previous K-variation probe (commit f034e69)
tested parametric interpolation, shared-13, Klein-antipodal
decomposition, and moire periods, all null. This probe takes the
orthogonal angle: treat K itself as the controlling axis and report
what scaling laws the tongue spectrum exhibits across K in [0, ~1.1].

Method. We sample the devil's staircase W(omega) on a fine omega
grid at each K, then identify plateaus (contiguous runs where W is
constant) and assign each plateau the p/q with smallest q whose
value matches W within tolerance. The plateau approach was originally
chosen to bypass a cold-start bug in circle_map.winding_number (the
measure loop discarded the post-transient theta and restarted from
0, so for orbits that hadn't reached the locked attractor within
n_measure iterations W deviated from p/q enough to fail the binary-
search tolerance test in tongue_width, collapsing widths to 0). The
upstream bug is now fixed in circle_map.py, but we keep the inline
plateau version for self-containment and reproducibility.

What we measure at each K:
  m(K)        -- total Lebesgue measure of locked tongues, summed
                 over all plateaus assignable to p/q with q <= Q_MAX
  N(K, eps)   -- number of resolved tongues with width > eps
  W_top(K)    -- the largest tongue width and its (p, q)
  framework_hit(K, eps) -- whether N(K, eps) hits a framework integer
                          from {3, 5, 6, 13, 19}

Output: a table per K. Any framework-integer hit is FLAGGED, not
claimed. ansatz_audit_policy.md says small-integer near-misses
between independently-defined counts are Class 2 numerology unless
a forcing argument exists.

Usage:
    python sync_cost/derivations/k_scaling_scan.py
"""

import math


# ---------------------------------------------------------------------------
# Circle map (inlined for self-containment; matches circle_map.py)
# ---------------------------------------------------------------------------

def winding_number(omega, K, n_transient=2000, n_measure=8000):
    """
    Average rotation per step of the standard circle map.

    theta_{n+1} = theta_n + omega - (K / 2*pi) * sin(2*pi*theta_n)
    """
    factor = K / (2 * math.pi)
    theta = 0.0
    for _ in range(n_transient):
        theta = theta + omega - factor * math.sin(2 * math.pi * theta)
    theta_start = theta
    for _ in range(n_measure):
        theta = theta + omega - factor * math.sin(2 * math.pi * theta)
    return (theta - theta_start) / n_measure


# ---------------------------------------------------------------------------
# Plateau detection from a fine staircase scan
# ---------------------------------------------------------------------------

def staircase_plateaus(K, n_omega=2001, plateau_tol=5e-4, Q_MAX=21):
    """
    Sample W(omega) on a fine grid in [0, 1], group consecutive
    near-equal values into plateaus, and return list of plateaus:

        [(p, q, omega_left, omega_right, W_mean), ...]

    where (p, q) is the rational with smallest q in [1, Q_MAX]
    closest to W_mean. Plateaus that don't match any low-q rational
    are dropped (they correspond to quasiperiodic orbits or to
    sub-resolution tongues with q > Q_MAX).
    """
    omegas = [i / (n_omega - 1) for i in range(n_omega)]
    Ws = [winding_number(om, K) for om in omegas]

    # Group consecutive omegas where successive W values agree
    # within plateau_tol -- these form candidate plateaus.
    plateaus = []
    i = 0
    while i < n_omega:
        j = i + 1
        while j < n_omega and abs(Ws[j] - Ws[j - 1]) < plateau_tol:
            j += 1
        if j - i >= 3:  # require at least 3 grid points for stability
            W_mean = sum(Ws[i:j]) / (j - i)
            # Match to nearest low-q rational
            best = None
            best_dist = 1.0
            for q in range(1, Q_MAX + 1):
                p = round(W_mean * q)
                if 0 <= p <= q and math.gcd(p, q) <= 1:
                    dist = abs(W_mean - p / q)
                    if dist < best_dist:
                        best_dist = dist
                        best = (p, q)
            if best is not None and best_dist < plateau_tol * 5:
                p, q = best
                plateaus.append((p, q, omegas[i], omegas[j - 1], W_mean))
        i = j

    # Dedupe: if multiple plateaus map to same (p, q), merge widths
    by_pq = {}
    for p, q, ol, or_, Wm in plateaus:
        key = (p, q)
        w = or_ - ol
        if key in by_pq:
            ol_old, or_old, Wm_old, w_old = by_pq[key]
            by_pq[key] = (min(ol_old, ol), max(or_old, or_), Wm, w_old + w)
        else:
            by_pq[key] = (ol, or_, Wm, w)

    out = []
    for (p, q), (ol, or_, Wm, w) in by_pq.items():
        out.append((p, q, ol, or_, Wm, w))
    out.sort(key=lambda r: -r[5])  # sort by total width desc
    return out


# ---------------------------------------------------------------------------
# Aggregate measures
# ---------------------------------------------------------------------------

FRAMEWORK_INTEGERS = {3, 5, 6, 13, 19}


def total_measure(plateaus):
    return sum(w for _, _, _, _, _, w in plateaus)


def resolved_count(plateaus, eps):
    return sum(1 for _, _, _, _, _, w in plateaus if w > eps)


def top_resolved_q(plateaus, eps, Q_MAX=21):
    """
    Largest q for which every coprime p/q in (0, 1) appears as a
    resolved plateau with width > eps.
    """
    by_q = {}
    for p, q, _, _, _, w in plateaus:
        by_q.setdefault(q, []).append(w)
    top = 1
    for q in range(2, Q_MAX + 1):
        widths = by_q.get(q, [])
        n_coprime = sum(1 for p in range(1, q) if math.gcd(p, q) == 1)
        if len(widths) >= n_coprime and all(w > eps for w in widths):
            top = q
    return top


def framework_hits(plateaus, eps_grid):
    hits = []
    for eps in eps_grid:
        N = resolved_count(plateaus, eps)
        if N in FRAMEWORK_INTEGERS:
            hits.append((eps, N))
    return hits


# ---------------------------------------------------------------------------
# Main scan
# ---------------------------------------------------------------------------

def main():
    print("=" * 80)
    print("  K-SCALING SCAN: tongue spectrum from K = 0 to chaos")
    print("=" * 80)

    Q_MAX = 21  # covers Farey level 7 (|F_7| = 19) cleanly
    K_grid = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.86196052,
              0.9, 0.95, 1.0, 1.05]
    eps_grid = [0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001]

    print(f"\n  Q_MAX = {Q_MAX}, n_omega per scan = 2001")
    print(f"  Reference: |F_6| = 13, |F_7| = 19 (framework integers)\n")

    print(f"  {'K':>8s}  {'m(K)':>8s}  {'top-q(eps=1e-2)':>16s}  "
          f"{'N(0.1)':>7s} {'N(0.05)':>7s} {'N(0.02)':>7s} {'N(0.01)':>7s} "
          f"{'N(0.005)':>8s} {'N(0.002)':>8s} {'N(0.001)':>8s}  "
          f"framework hits (eps,N)")
    print("  " + "-" * 145)

    rows = []
    for K in K_grid:
        plats = staircase_plateaus(K, n_omega=2001, Q_MAX=Q_MAX)
        m = total_measure(plats)
        top = top_resolved_q(plats, 1e-2, Q_MAX=Q_MAX)
        Ns = [resolved_count(plats, eps) for eps in eps_grid]
        hits = framework_hits(plats, eps_grid)
        hit_str = " ".join(f"({eps:g},{N})" for eps, N in hits) if hits else "-"
        annot = ""
        if abs(K - 0.86196052) < 1e-6:
            annot = "  <- K_STAR"
        if abs(K - 1.0) < 1e-9:
            annot = "  <- critical"
        print(f"  {K:8.4f}  {m:8.5f}  {top:16d}  "
              f"{Ns[0]:7d} {Ns[1]:7d} {Ns[2]:7d} {Ns[3]:7d} "
              f"{Ns[4]:8d} {Ns[5]:8d} {Ns[6]:8d}  {hit_str}{annot}")
        rows.append((K, m, top, Ns, plats))

    # ---- Top-5 tongues per K (structural ranking) ------------------------
    print(f"\n{'-'*80}")
    print("  TOP-5 TONGUES (sorted by width) at each K")
    print(f"{'-'*80}")
    for K, m, top, Ns, plats in rows:
        ranked = "  ".join(f"({p}/{q}, {w:.4f})" for p, q, _, _, _, w in plats[:5])
        print(f"  K={K:7.4f}  {ranked}")

    # ---- Scaling: m(K) vs K ---------------------------------------------
    print(f"\n{'-'*80}")
    print("  SCALING: m(K) vs K")
    print(f"{'-'*80}")
    Ks = [r[0] for r in rows]
    ms = [r[1] for r in rows]
    print(f"\n  {'K':>8s}  {'m(K)':>10s}  {'m/K':>10s}  {'m/K^2':>10s}  {'1-(1-K)^2':>12s}")
    for K, m in zip(Ks, ms):
        ratio1 = m / K if K > 0 else 0
        ratio2 = m / (K * K) if K > 0 else 0
        soft = 1 - (1 - K) ** 2 if K <= 1 else float("nan")
        print(f"  {K:8.4f}  {m:10.6f}  {ratio1:10.4f}  {ratio2:10.4f}  {soft:12.4f}")

    print(f"\n  At K -> 0, the dominant 1/2 tongue has w(1/2, K) = K/pi (Adler).")
    print(f"  Compare m(K)/K at small K to 1/pi = {1/math.pi:.4f}.")
    print(f"\n  At K = 1, the truncated sum approaches 1 in the Q_MAX -> infty limit")
    print(f"  (Jensen-Bak-Bohr: complement is fat fractal, dim ~ 0.87).")

    # ---- Framework-register check ---------------------------------------
    print(f"\n{'-'*80}")
    print("  FRAMEWORK-REGISTER CHECK")
    print(f"{'-'*80}")
    print(f"\n  P-reg has 19 states (|F_7|). Look for K such that the tongue")
    print(f"  count N(K, eps) = 19 for some 'natural' eps.")
    print(f"\n  K-values where some N(K, eps) hits 19:")
    found = False
    for K, m, top, Ns, plats in rows:
        for eps, N in zip(eps_grid, Ns):
            if N == 19:
                print(f"    K = {K:.4f}, eps = {eps:g}: N = 19  (hit)")
                found = True
    if not found:
        print(f"    None at the sampled K and eps grids.")
    print(f"\n  Triage per ansatz_audit_policy.md: even if a hit is found, the")
    print(f"  forcing argument for the specific eps is the load-bearing piece.")
    print(f"  An (eps, K) pair selected to make N = 19 is Class 2 ansatz unless")
    print(f"  eps follows from a structural condition (e.g., eps = 1/Q_MAX, or")
    print(f"  eps = (1 - K)^beta with beta from the framework).")


if __name__ == "__main__":
    main()
