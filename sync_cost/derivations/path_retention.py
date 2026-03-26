#!/usr/bin/env python3
"""
Retain path information for every mode in the minimum universe.

Each fraction p/q has two encodings:
  VALUE: p/q → tongue width, duty cycle, coupling
  PATH:  L/R sequence → complexity, matrix, mixing

The value encoding discards the path. This script retains it.

For every mode in F₆:
  - The Stern-Brocot path (sequence of L/R steps)
  - The continued fraction [a₀; a₁, ...]
  - The SL(2,Z) matrix product
  - The path length and shape

Then: what does the path add?

Usage:
    python3 sync_cost/derivations/path_retention.py
"""

from fractions import Fraction
import math


# ── Stern-Brocot path ────────────────────────────────────────────────────────

def sb_path(p, q):
    """
    Compute the Stern-Brocot path from root to p/q.
    Returns list of 'L' and 'R' steps.
    """
    if q == 0:
        return []
    # Navigate the SB tree
    # Boundaries: left = 0/1, right = 1/0
    a, b = 0, 1  # left = a/b
    c, d = 1, 0  # right = c/d
    path = []

    target = Fraction(p, q)
    for _ in range(100):  # safety limit
        med_n = a + c
        med_d = b + d
        mediant = Fraction(med_n, med_d)

        if mediant == target:
            break
        elif target < mediant:
            path.append('L')
            c, d = med_n, med_d
        else:
            path.append('R')
            a, b = med_n, med_d

    return path


def continued_fraction(p, q):
    """Compute continued fraction expansion of p/q."""
    cf = []
    while q > 0:
        a = p // q
        cf.append(a)
        p, q = q, p - a * q
    return cf


def cf_to_path(cf):
    """Convert continued fraction to L/R path."""
    path = []
    for i, a in enumerate(cf):
        if i == 0:
            # a₀ = 0 for fractions in (0,1), skip
            continue
        direction = 'L' if i % 2 == 1 else 'R'
        path.extend([direction] * a)
    return path


def sl2z_matrix(path):
    """
    Compute SL(2,Z) matrix from path.
    L = [[1,0],[1,1]], R = [[1,1],[0,1]]
    """
    # Start with identity
    m = [[1, 0], [0, 1]]

    L = [[1, 0], [1, 1]]
    R = [[1, 1], [0, 1]]

    def mat_mul(a, b):
        return [[a[0][0]*b[0][0] + a[0][1]*b[1][0],
                 a[0][0]*b[0][1] + a[0][1]*b[1][1]],
                [a[1][0]*b[0][0] + a[1][1]*b[1][0],
                 a[1][0]*b[0][1] + a[1][1]*b[1][1]]]

    for step in path:
        if step == 'L':
            m = mat_mul(m, L)
        else:
            m = mat_mul(m, R)
    return m


def mat_trace(m):
    return m[0][0] + m[1][1]


def mat_det(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]


# ── Farey sequence ────────────────────────────────────────────────────────────

def farey_interior(n):
    """Interior fractions of F_n (excluding 0/1 and 1/1)."""
    fracs = set()
    for q in range(2, n + 1):
        for p in range(1, q):
            if math.gcd(p, q) == 1:
                fracs.add(Fraction(p, q))
    return sorted(fracs)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 85)
    print("  PATH RETENTION: every mode's full address")
    print("=" * 85)

    modes = farey_interior(6)

    # ── 1. Full path catalog ──────────────────────────────────────────────
    print(f"\n{'─' * 85}")
    print("  1. COMPLETE PATH CATALOG FOR F₆")
    print(f"{'─' * 85}\n")

    print(f"  {'p/q':>6s}  {'q':>3s}  {'path':>12s}  {'len':>4s}  "
          f"{'CF':>14s}  {'CF len':>6s}  {'Σaᵢ':>4s}  "
          f"{'matrix':>20s}  {'tr':>4s}  {'det':>4s}")
    print("  " + "-" * 85)

    catalog = []
    for f in modes:
        p, q = f.numerator, f.denominator
        path = sb_path(p, q)
        cf = continued_fraction(p, q)
        mat = sl2z_matrix(path)
        tr = mat_trace(mat)
        det = mat_det(mat)
        path_str = ''.join(path)
        cf_str = '[' + '; '.join(str(a) for a in cf) + ']'
        cf_len = len(cf) - 1  # exclude a₀=0
        cf_sum = sum(cf)
        mat_str = f"[{mat[0][0]},{mat[0][1]};{mat[1][0]},{mat[1][1]}]"

        catalog.append({
            'frac': f, 'p': p, 'q': q, 'path': path_str,
            'path_len': len(path), 'cf': cf, 'cf_str': cf_str,
            'cf_len': cf_len, 'cf_sum': cf_sum,
            'matrix': mat, 'trace': tr, 'det': det
        })

        print(f"  {str(f):>6s}  {q:3d}  {path_str:>12s}  {len(path):4d}  "
              f"{cf_str:>14s}  {cf_len:6d}  {cf_sum:4d}  "
              f"{mat_str:>20s}  {tr:4d}  {det:4d}")

    # ── 2. Path vs value: what's different ────────────────────────────────
    print(f"\n{'─' * 85}")
    print("  2. WHAT THE PATH ADDS (beyond q)")
    print(f"{'─' * 85}\n")

    # Group by denominator
    by_q = {}
    for m in catalog:
        q = m['q']
        if q not in by_q:
            by_q[q] = []
        by_q[q].append(m)

    for q in sorted(by_q.keys()):
        modes_q = by_q[q]
        print(f"  q = {q}: {len(modes_q)} mode(s)")
        for m in modes_q:
            print(f"    {str(m['frac']):>6s}  path={m['path']:>12s}  "
                  f"len={m['path_len']}  CF={m['cf_str']}")

        if len(modes_q) > 1:
            # Path length difference
            lens = [m['path_len'] for m in modes_q]
            if len(set(lens)) > 1:
                print(f"    → PATH LENGTHS DIFFER: {lens}")
                print(f"    → The value (q) doesn't distinguish these.")
                print(f"    → Path length is ADDITIONAL information.")
            else:
                # Same length, different shape
                shapes = [m['path'] for m in modes_q]
                print(f"    → Same length ({lens[0]}), different shape: {shapes}")
                print(f"    → The path SHAPE is additional information.")

            # Matrix comparison
            for i, m1 in enumerate(modes_q):
                for m2 in modes_q[i+1:]:
                    # "Angle" between matrices: tr(M1^{-1} M2)
                    # For SL(2,Z): M^{-1} = [[d,-b],[-c,a]] for M=[[a,b],[c,d]]
                    M1 = m1['matrix']
                    M2 = m2['matrix']
                    M1_inv = [[M1[1][1], -M1[0][1]],
                              [-M1[1][0], M1[0][0]]]
                    prod = [[M1_inv[0][0]*M2[0][0] + M1_inv[0][1]*M2[1][0],
                             M1_inv[0][0]*M2[0][1] + M1_inv[0][1]*M2[1][1]],
                            [M1_inv[1][0]*M2[0][0] + M1_inv[1][1]*M2[1][0],
                             M1_inv[1][0]*M2[0][1] + M1_inv[1][1]*M2[1][1]]]
                    tr_prod = prod[0][0] + prod[1][1]
                    # For SL(2,Z): |tr| < 2 → elliptic, |tr| = 2 → parabolic, |tr| > 2 → hyperbolic
                    if abs(tr_prod) < 2:
                        mtype = "elliptic (rotation)"
                    elif abs(tr_prod) == 2:
                        mtype = "parabolic (shear)"
                    else:
                        mtype = "hyperbolic (boost)"

                    # Mixing angle: cos(2α) = tr/2 for elliptic
                    if abs(tr_prod) <= 2:
                        angle = math.acos(tr_prod / 2) / 2
                        angle_deg = math.degrees(angle)
                    else:
                        angle = math.acosh(abs(tr_prod) / 2)
                        angle_deg = math.degrees(angle)

                    print(f"    → {str(m1['frac'])} ↔ {str(m2['frac'])}: "
                          f"tr(M₁⁻¹M₂) = {tr_prod}, {mtype}, "
                          f"angle = {angle_deg:.2f}°")
        print()

    # ── 3. Path-weighted quantities ───────────────────────────────────────
    print(f"\n{'─' * 85}")
    print("  3. PATH-WEIGHTED DUTY CYCLES")
    print(f"{'─' * 85}\n")

    print("  The value encoding gives duty = 1/q³ for all modes at q.")
    print("  The path encoding gives a DIFFERENT weight to each mode:")
    print("    path_weight(p/q) = 1/q³ × (path_length_correction)")
    print()

    # Hypothesis: the path length correction is related to the CF sum
    # Modes with longer paths are "harder to reach" and should be rarer
    print(f"  {'p/q':>6s}  {'q':>3s}  {'duty=1/q³':>12s}  "
          f"{'path_len':>9s}  {'CF_sum':>7s}  "
          f"{'1/(q³×len)':>12s}  {'1/(q³×Σaᵢ)':>12s}")
    print("  " + "-" * 70)

    for m in catalog:
        q = m['q']
        duty = Fraction(1, q**3)
        plen = m['path_len']
        csum = m['cf_sum']
        duty_len = Fraction(1, q**3 * plen)
        duty_cf = Fraction(1, q**3 * csum) if csum > 0 else 0

        print(f"  {str(m['frac']):>6s}  {q:3d}  {float(duty):12.6f}  "
              f"{plen:9d}  {csum:7d}  "
              f"{float(duty_len):12.6f}  {float(duty_cf):12.6f}")

    # ── 4. The three generations with path correction ─────────────────────
    print(f"\n{'─' * 85}")
    print("  4. GENERATION MASS RATIOS WITH PATH CORRECTION")
    print(f"{'─' * 85}\n")

    # The three phase states involve the q=2 and q=3 sectors
    # q=2 sector: 1/2 (path L, len=1)
    # q=3 sector: 1/3 (path LL, len=2) and 2/3 (path LR, len=2)
    # The q=3 modes have the SAME path length but DIFFERENT shapes

    m_12 = [m for m in catalog if m['frac'] == Fraction(1, 2)][0]
    m_13 = [m for m in catalog if m['frac'] == Fraction(1, 3)][0]
    m_23 = [m for m in catalog if m['frac'] == Fraction(1, 3)][0]  # using 1/3 as representative

    print(f"  q=2 sector: {m_12['frac']}  path={m_12['path']}  len={m_12['path_len']}")
    print(f"  q=3 sector: 1/3  path={m_13['path']}  len={m_13['path_len']}")
    print(f"              2/3  path=LR  len=2")
    print()

    # Phase states with path-weighted duties
    # Value-only: duty(2) = 1/8, duty(3) = 1/27
    # Path-weighted: duty(2) × 1/len(2) = 1/8 × 1/1 = 1/8
    #                duty(3) × 1/len(3) = 1/27 × 1/2 = 1/54
    # The q=3 sector is HALVED by the path correction!

    duty_2_val = Fraction(1, 8)
    duty_3_val = Fraction(1, 27)
    duty_2_path = Fraction(1, 8 * m_12['path_len'])  # 1/(8×1) = 1/8
    duty_3_path = Fraction(1, 27 * 2)  # 1/(27×2) = 1/54

    print(f"  Value-only:  duty(2) = {duty_2_val} = {float(duty_2_val):.6f}")
    print(f"               duty(3) = {duty_3_val} = {float(duty_3_val):.6f}")
    print(f"               ratio   = {float(duty_2_val/duty_3_val):.4f}")
    print()
    print(f"  Path-weighted: duty(2) = 1/(8×{m_12['path_len']}) = {duty_2_path}"
          f" = {float(duty_2_path):.6f}")
    print(f"                 duty(3) = 1/(27×2) = {duty_3_path}"
          f" = {float(duty_3_path):.6f}")
    print(f"                 ratio   = {float(duty_2_path/duty_3_path):.4f}")
    print()

    # Generation weights with path correction
    gap_2_path = 1 - float(duty_2_path)
    gap_3_path = 1 - 2 * float(duty_3_path)

    B_path = float(duty_2_path) * gap_3_path
    C_path = gap_2_path * 2 * float(duty_3_path)
    A_path = float(duty_2_path) * 2 * float(duty_3_path)

    print(f"  Phase states with path correction:")
    print(f"    B = duty₂ × gap₃ = {B_path:.6f}")
    print(f"    C = gap₂ × duty₃ = {C_path:.6f}")
    print(f"    A = duty₂ × duty₃ = {A_path:.6f}")
    print(f"    Base ratios: {B_path/A_path:.1f} : {C_path/A_path:.1f} : 1")
    print()

    # Compare value-only and path-weighted
    duty_2_v = Fraction(1, 8)
    duty_3_v = Fraction(1, 27)
    gap_2_v = 1 - float(duty_2_v)
    gap_3_v = 1 - 2 * float(duty_3_v)
    B_v = float(duty_2_v) * gap_3_v
    C_v = gap_2_v * 2 * float(duty_3_v)
    A_v = float(duty_2_v) * 2 * float(duty_3_v)

    print(f"  Comparison:")
    print(f"  {'':>16s}  {'Value-only':>12s}  {'Path-weighted':>14s}  {'Observed':>10s}")
    print("  " + "-" * 56)
    print(f"  {'B/A (heavy/light)':>16s}  {B_v/A_v:12.1f}  {B_path/A_path:14.1f}  "
          f"{'3477 (τ/e)':>10s}")
    print(f"  {'C/A (mid/light)':>16s}  {C_v/A_v:12.1f}  {C_path/A_path:14.1f}  "
          f"{'207 (μ/e)':>10s}")
    print(f"  {'B/C (heavy/mid)':>16s}  {B_v/C_v:12.1f}  {B_path/C_path:14.1f}  "
          f"{'16.8 (τ/μ)':>10s}")

    # ── 5. Mass predictions with rational exponents ───────────────────────
    print(f"\n{'─' * 85}")
    print("  5. MASS PREDICTIONS: path-corrected base × rational exponent")
    print(f"{'─' * 85}\n")

    # Test with both bases
    for base_name, B_base, C_base in [
        ("Value-only", B_v/A_v, C_v/A_v),
        ("Path-weighted", B_path/A_path, C_path/A_path)
    ]:
        print(f"  {base_name} (B/A = {B_base:.2f}, C/A = {C_base:.2f}):")
        print()

        # Mass = base^exponent
        observed = {
            'leptons': (3477, 207, 'e/μ/τ'),
            'down': (895, 20, 'd/s/b'),
            'up': (80000, 588, 'u/c/t'),
        }

        for sector, (heavy_light, mid_light, names) in observed.items():
            # Find best exponent for heavy/light
            if B_base > 1:
                a_best = math.log(heavy_light) / math.log(B_base)
            else:
                a_best = 0
            # Predict mid/light at that exponent
            mid_pred = C_base ** a_best if C_base > 1 else 0

            print(f"    {sector} ({names}):")
            print(f"      a = ln({heavy_light})/ln({B_base:.2f}) = {a_best:.3f}")
            print(f"      m₃/m₁ = {B_base:.2f}^{a_best:.3f} = {heavy_light} (exact, input)")
            print(f"      m₂/m₁ = {C_base:.2f}^{a_best:.3f} = {mid_pred:.1f}"
                  f"  (observed: {mid_light}, "
                  f"Δ = {abs(mid_pred - mid_light)/mid_light:.0%})")
            print()

    # ── 6. The path as the missing generation quantum number ──────────────
    print(f"\n{'─' * 85}")
    print("  6. PATH LENGTH AS GENERATION QUANTUM NUMBER")
    print(f"{'─' * 85}\n")

    print("  The value (q) determines the SECTOR (which force).")
    print("  The path determines the GENERATION (which copy).")
    print()
    print("  At each depth d of the SB tree, new modes appear.")
    print("  The path length to each mode IS its generation index:")
    print()

    # Show how path length correlates with depth of first appearance
    print(f"  {'p/q':>6s}  {'q':>3s}  {'path_len':>9s}  "
          f"{'first appears at SB depth':>25s}  {'generation?':>12s}")
    print("  " + "-" * 60)

    for m in catalog:
        q = m['q']
        plen = m['path_len']
        # The SB depth where p/q first appears = path length
        # (each step in the path is one level deeper)
        gen = plen  # generation index = path length
        print(f"  {str(m['frac']):>6s}  {q:3d}  {plen:9d}  "
              f"{plen:25d}  {'gen ' + str(gen):>12s}")

    print()
    print("  The path length IS the SB depth of first appearance.")
    print("  It's the number of mediant steps from the root.")
    print("  It's a NATURAL generation quantum number.")
    print()
    print("  Generation 1 (len=1): 1/2")
    print("  Generation 2 (len=2): 1/3, 2/3")
    print("  Generation 3 (len=3): 1/4, 2/5, 3/5, 3/4")
    print("  Generation 4 (len=4): 1/5, 4/5")
    print("  Generation 5 (len=5): 1/6, 5/6")

    # ── Summary ───────────────────────────────────────────────────────────
    print(f"\n{'=' * 85}")
    print("  SUMMARY")
    print(f"{'=' * 85}")
    print(f"""
  The path encoding retains information that the value discards:

  1. PATH LENGTH = generation index = SB depth of first appearance
     This is a natural quantum number. Modes at the same q but
     different path lengths are different generations.

  2. PATH SHAPE = mixing angle. Modes at the same q and same length
     but different L/R sequences (like 1/3=LL vs 2/3=LR) are related
     by the SL(2,Z) transformation between their paths. The trace of
     M₁⁻¹M₂ determines whether the relationship is elliptic (rotation
     = mixing), parabolic (shear = mass splitting), or hyperbolic
     (boost = large hierarchy).

  3. PATH-WEIGHTED duty corrections: including 1/path_len in the
     duty cycle changes the generation base ratios. The q=3 sector
     gets halved (path length 2 vs 1 for q=2), steepening the hierarchy.

  The path is the generation quantum number we were missing.
  It's been in the tree all along — the Stern-Brocot tree IS
  a family tree, and the path length is the generation.
""")


if __name__ == "__main__":
    main()
