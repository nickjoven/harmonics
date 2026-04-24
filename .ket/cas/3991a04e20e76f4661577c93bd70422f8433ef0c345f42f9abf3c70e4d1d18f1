"""
K-axis uniqueness probe: composed K-scan + Klein-antipodal Z_2-rep
+ coprime-to-(q_2 q_3) filter.

Setup. The bare K-scan (k_scaling_scan.md, PR #76) landed Class 2:
the bare circle map ranks rationals by tongue width but never
forbids any. The follow-up sketched in that writeup: compose with
the framework's existing forcing filters (Klein-antipodal Z_2 rep
and coprime-to-(q_2 q_3)) and see whether the composed
resolved-count maps onto framework integers structurally.

Both filters are forced by prior framework work:

- Klein-antipodal Z_2 rep: pattern_pattern.md, used in
  down-type quarks (factor 6), up-type quarks (factor 9), and the
  Omega partition (13:5:1/19).
- Coprime-to-(q_2 q_3) = coprime-to-6: used in the Omega partition
  to isolate the baryonic mode (omega_partition_combinatorial.md).

What we test. For each Farey level n in [2, 12], compute:

  N_orbits(n) = number of Klein-antipodal Z_2 orbits of (p, q)
                pairs in F_n with gcd(q, q_2 q_3) = 1

Then for each K, find which Farey level the K-scan resolves, and
report the corresponding N_orbits.

Plateau hypothesis. Because the coprime-to-6 filter rejects q in
{2, 3, 4, 6, 8, 9, 10, 12, ...} (multiples of 2 or 3), N_orbits(n)
has plateaus. Within a plateau, N_orbits is constant, so the
result is robust to the K-window width: any K that resolves
exactly Farey level n in the plateau range gives the same orbit
count.

Framework-integer prediction. The plateaus at primes p coprime to
6 give:

  p = 5:  N_orbits = 3    (= q_3 = D)
  p = 7:  N_orbits = 6    (= q_2 q_3 = INTERACT)
  p = 11: N_orbits = 11   (no framework match)
  p = 13: N_orbits = 17   (no framework match)

Only the first two primes coprime to 6 give framework integers.
After p = 7 the count escapes.

K-axis test. Compute the K-window where the resolved Farey level
falls in each plateau range. Test whether canonical K-values
(K_STAR, 1.0, 1/phi^2, etc.) fall into the framework-matching
plateaus.

Triage. Even if K_STAR falls into the q_3 = 3 or INTERACT = 6
plateau, the Farey-level cutoff is structurally given by the
coprime-to-6 filter (no free parameter), and the orbit count is
forced by the Klein-antipodal involution. The only remaining free
choice is K, which is constrained to a window, not a point.

If K_STAR (or another canonical K) lands in a framework-matching
plateau, that elevates the result to a candidate Class 4 (proposed
structural). If it lands in a non-framework plateau or between
plateaus, the result is Class 2.

Usage:
    python sync_cost/derivations/k_axis_uniqueness.py
"""

import math


# ---------------------------------------------------------------------------
# Framework constants (mirror sync_cost/derivations/framework_constants.py)
# ---------------------------------------------------------------------------

Q2 = 2
Q3 = 3
INTERACT = Q2 * Q3   # = 6
MEDIANT = Q2 + Q3    # = 5
K_STAR = 0.86196052
PHI = (1 + math.sqrt(5)) / 2


# ---------------------------------------------------------------------------
# Combinatorial part: Klein-antipodal orbits with coprime-to-INTERACT filter
# ---------------------------------------------------------------------------

def farey_set(n):
    """F_n = all coprime p/q in [0, 1] with q <= n."""
    fracs = {(0, 1), (1, 1)}
    for q in range(2, n + 1):
        for p in range(1, q):
            if math.gcd(p, q) == 1:
                fracs.add((p, q))
    return fracs


def klein_orbits(fracs, m=INTERACT):
    """
    Klein-antipodal Z_2 orbits of fracs filtered by gcd(q, m) = 1.

    Returns (n_orbits, n_singletons, n_pairs, surviving_set).
    """
    surviving = {(p, q) for (p, q) in fracs if math.gcd(q, m) == 1}
    seen = set()
    singletons = 0
    pairs = 0
    for (p, q) in surviving:
        if (p, q) in seen:
            continue
        sigma = (q - p, q)
        if sigma == (p, q):
            singletons += 1
            seen.add((p, q))
        else:
            pairs += 1
            seen.add((p, q))
            seen.add(sigma)
    return singletons + pairs, singletons, pairs, surviving


# ---------------------------------------------------------------------------
# Numerical part: K-windows from circle-map staircase
# ---------------------------------------------------------------------------

def winding_number(omega, K, n_transient=2000, n_measure=8000):
    factor = K / (2 * math.pi)
    theta = 0.0
    for _ in range(n_transient):
        theta = theta + omega - factor * math.sin(2 * math.pi * theta)
    theta_start = theta
    for _ in range(n_measure):
        theta = theta + omega - factor * math.sin(2 * math.pi * theta)
    return (theta - theta_start) / n_measure


def resolved_max_q(K, n_omega=2001, plateau_tol=5e-4, q_max=20,
                   min_plateau_pts=3):
    """
    Return the largest q for which every coprime p/q (in (0, 1))
    appears as a resolved plateau on the staircase at coupling K.
    """
    omegas = [i / (n_omega - 1) for i in range(n_omega)]
    Ws = [winding_number(om, K) for om in omegas]

    plateaus = []
    i = 0
    while i < n_omega:
        j = i + 1
        while j < n_omega and abs(Ws[j] - Ws[j - 1]) < plateau_tol:
            j += 1
        if j - i >= min_plateau_pts:
            W_mean = sum(Ws[i:j]) / (j - i)
            best = None
            best_dist = 1.0
            for q in range(1, q_max + 1):
                p_round = round(W_mean * q)
                if 0 <= p_round <= q and math.gcd(p_round, q) <= 1:
                    dist = abs(W_mean - p_round / q)
                    if dist < best_dist:
                        best_dist = dist
                        best = (p_round, q)
            if best is not None and best_dist < plateau_tol * 5:
                plateaus.append(best)
        i = j

    resolved = set(plateaus)
    top = 1
    for q in range(2, q_max + 1):
        coprime_p = [p for p in range(1, q) if math.gcd(p, q) == 1]
        if all((p, q) in resolved for p in coprime_p):
            top = q
        else:
            # Allow gaps (e.g., q=4 missing but q=5 present): take
            # max q with all reps present.
            pass
    return top


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 80)
    print("  K-AXIS UNIQUENESS PROBE")
    print("  Composed: K-scan + Klein-antipodal Z_2-rep + coprime-to-6 filter")
    print("=" * 80)

    # -------------------------------------------------------------------
    # Part 1: combinatorial table
    # -------------------------------------------------------------------
    print(f"\n  -- Part 1: orbit count vs Farey level (combinatorial only) --\n")
    print(f"  {'n':>3s}  {'|F_n|':>5s}  {'coprime6':>10s}  {'orbits':>7s}  "
          f"{'singletons':>11s}  {'pairs':>6s}  framework")
    print("  " + "-" * 80)

    plateaus = []
    last_count = -1
    plateau_start = None
    for n in range(1, 14):
        fracs = farey_set(n)
        N_orbits, n_sing, n_pair, surv = klein_orbits(fracs)
        framework = ""
        if N_orbits == 1:
            framework = "trivial"
        elif N_orbits == Q3:
            framework = "q_3 = D"
        elif N_orbits == INTERACT:
            framework = "INTERACT = q_2 * q_3"
        elif N_orbits == Q3 ** 2:
            framework = "K_LEPTON = q_3^2"
        elif N_orbits == Q2 ** 3:
            framework = "K_QUARK = q_2^3"
        print(f"  {n:>3d}  {len(fracs):>5d}  {len(surv):>10d}  {N_orbits:>7d}  "
              f"{n_sing:>11d}  {n_pair:>6d}  {framework}")
        if N_orbits != last_count:
            if plateau_start is not None:
                plateaus.append((plateau_start, n - 1, last_count))
            plateau_start = n
            last_count = N_orbits

    if plateau_start is not None:
        plateaus.append((plateau_start, 13, last_count))

    print(f"\n  -- Plateau structure --")
    for n_lo, n_hi, count in plateaus:
        framework = ""
        if count == 1:
            framework = "trivial"
        elif count == Q3:
            framework = " <- q_3 = D"
        elif count == INTERACT:
            framework = " <- INTERACT = q_2 * q_3"
        print(f"    n in [{n_lo}, {n_hi}]: orbits = {count}{framework}")

    # -------------------------------------------------------------------
    # Part 2: K-windows from numerical staircase
    # -------------------------------------------------------------------
    print(f"\n  -- Part 2: K-axis -- which Farey level is resolved at canonical K --\n")

    K_canonical = [
        ("0.5",                0.5),
        ("1/phi^2 = 0.382",    1.0 / (PHI * PHI)),
        ("1/phi   = 0.618",    1.0 / PHI),
        ("0.7",                0.7),
        ("0.8",                0.8),
        ("K_STAR = 0.86196",   K_STAR),
        ("0.9",                0.9),
        ("0.95",               0.95),
        ("1.0  (critical)",    1.0),
        ("1.05",               1.05),
    ]

    print(f"  {'K':>22s}  {'top-q resolved':>15s}  "
          f"{'plateau range':>15s}  {'orbits':>7s}  framework match?")
    print("  " + "-" * 95)

    for label, K in K_canonical:
        top = resolved_max_q(K)
        # Find which combinatorial plateau top falls into
        match = None
        for n_lo, n_hi, count in plateaus:
            if n_lo <= top <= n_hi:
                match = (n_lo, n_hi, count)
                break
        if match is None:
            print(f"  {label:>22s}  {top:>15d}  {'(beyond)':>15s}  {'-':>7s}  -")
        else:
            n_lo, n_hi, count = match
            framework = ""
            if count == Q3:
                framework = "q_3 = D"
            elif count == INTERACT:
                framework = "INTERACT = q_2 * q_3"
            elif count == 1:
                framework = "trivial"
            print(f"  {label:>22s}  {top:>15d}  "
                  f"[{n_lo},{n_hi}]:{count:<5d}  {count:>7d}  {framework}")

    # -------------------------------------------------------------------
    # Part 3: K-window for each plateau
    # -------------------------------------------------------------------
    print(f"\n  -- Part 3: K-windows where resolved set lands in each plateau --\n")
    K_grid = [0.05 + 0.01 * i for i in range(101)]  # 0.05 to 1.05 step 0.01
    plateau_K_windows = {}
    for K in K_grid:
        top = resolved_max_q(K)
        for n_lo, n_hi, count in plateaus:
            if n_lo <= top <= n_hi:
                plateau_K_windows.setdefault((n_lo, n_hi, count), []).append(K)
                break

    print(f"  {'plateau':>15s}  {'orbits':>7s}  {'K-window':>22s}  framework match?")
    print("  " + "-" * 75)
    for (n_lo, n_hi, count), Ks in sorted(plateau_K_windows.items(),
                                          key=lambda x: x[0][0]):
        if Ks:
            K_min, K_max = min(Ks), max(Ks)
            framework = ""
            if count == Q3:
                framework = "q_3 = D"
            elif count == INTERACT:
                framework = "INTERACT = q_2 * q_3"
            elif count == 1:
                framework = "trivial"
            print(f"  [{n_lo},{n_hi}]      {count:>7d}  "
                  f"[{K_min:.3f}, {K_max:.3f}]  {framework}")

    # -------------------------------------------------------------------
    # Part 4: triage and verdict
    # -------------------------------------------------------------------
    print(f"\n  -- Part 4: forcing-argument check --\n")
    print(f"  Klein-antipodal Z_2 rep filter: forced by ")
    print(f"    klein_antipodal_z2_rep_pattern.md (down-type 6, up-type 9, ")
    print(f"    Omega 13:5:1/19).")
    print(f"  Coprime-to-6 filter:           forced by ")
    print(f"    omega_partition_combinatorial.md (baryonic mode isolation).")
    print(f"  Stopping at Farey level n:     NOT forced as a single n. ")
    print(f"    But the plateau structure makes any n in a plateau give the ")
    print(f"    same orbit count -- so 'pick a plateau' is equivalent to ")
    print(f"    'pick a K-window'.")
    print(f"  K-window selection:            forced if K_STAR (or another ")
    print(f"    structurally-derived K) lands in a framework-matching plateau.")

    K_STAR_top = resolved_max_q(K_STAR)
    K_STAR_plateau = None
    for n_lo, n_hi, count in plateaus:
        if n_lo <= K_STAR_top <= n_hi:
            K_STAR_plateau = (n_lo, n_hi, count)
            break
    print(f"\n  K_STAR test: K_STAR = {K_STAR:.6f} resolves up to q = {K_STAR_top}.")
    if K_STAR_plateau is not None:
        n_lo, n_hi, count = K_STAR_plateau
        if count in (Q3, INTERACT):
            print(f"    -> falls in plateau [n={n_lo}..{n_hi}] with orbits = {count}.")
            print(f"    -> matches framework integer.")
        else:
            print(f"    -> falls in plateau [n={n_lo}..{n_hi}] with orbits = {count}.")
            print(f"    -> NOT a framework integer.")

    # -------------------------------------------------------------------
    # Part 5: ε-robustness check
    # -------------------------------------------------------------------
    print(f"\n  -- Part 5: epsilon-robustness of K_STAR plateau membership --\n")
    print(f"  K_STAR plateau membership across plateau-detection thresholds:")
    print(f"  {'plateau_tol':>14s}  {'top-q':>6s}  {'plateau':>10s}  "
          f"{'orbits':>7s}  framework match?")
    print("  " + "-" * 70)
    for tol in [1e-2, 5e-3, 2e-3, 1e-3, 5e-4, 2e-4, 1e-4]:
        top = resolved_max_q(K_STAR, plateau_tol=tol)
        match = None
        for n_lo, n_hi, count in plateaus:
            if n_lo <= top <= n_hi:
                match = (n_lo, n_hi, count)
                break
        framework = ""
        if match:
            n_lo, n_hi, count = match
            if count == Q3:
                framework = "q_3 = D"
            elif count == INTERACT:
                framework = "INTERACT = q_2 * q_3"
            elif count == 1:
                framework = "trivial"
        print(f"  {tol:>14.4f}  {top:>6d}  "
              f"[{match[0] if match else '?'},{match[1] if match else '?'}]"
              f"      {match[2] if match else '?':>5}  {framework}")

    print(f"\n  -- Part 6: alternative K-values in INTERACT plateau --\n")
    print(f"  Width of K-window for the INTERACT (orbits=6) plateau:")
    interact_window = plateau_K_windows.get((7, 10, 6), [])
    if interact_window:
        K_min, K_max = min(interact_window), max(interact_window)
        print(f"    K in [{K_min:.3f}, {K_max:.3f}], width = {K_max - K_min:.3f}")
        print(f"    K_STAR = {K_STAR:.4f} sits at fractional position "
              f"{(K_STAR - K_min)/(K_max - K_min):.2f} within the window.")
        print(f"    The framework provides K_STAR via mass-sector closure")
        print(f"    (independent of staircase reasoning). The window's "
              f"existence")
        print(f"    is a structural fact; K_STAR's location within is a "
              f"second")
        print(f"    structural fact (joint matter-sector closure).")


if __name__ == "__main__":
    main()
