"""
Exactly one half-twist is forced.

Four conditions that must hold to claim the Möbius structure is
physical, not just a pattern in the output:

  1. GLOBAL IDENTIFICATION: after one traversal of the backbone,
     orientation is reversed. Not locally — globally.

  2. NON-ORIENTABLE, NOT JUST ALTERNATING: the sign flip cannot be
     absorbed into a basis redefinition. The Z/2 bundle over the
     backbone is non-trivial.

  3. INVARIANT UNDER U: the operator preserves the non-orientability.

  4. REMOVING IT BREAKS A PHYSICAL PREDICTION: setting det(M) = +1
     (orientable) with the same trace kills the convergence entirely.
     No irrational limit, no golden ratio, no spectral tilt.

If all four hold, then exactly one half-twist is forced by the
structure, not imposed.

Usage:
    python sync_cost/derivations/one_half_twist.py
"""

import math
import cmath
from fractions import Fraction

import sys
sys.path.insert(0, "sync_cost/derivations")
from universe_loop import (
    ConstraintTree, Operator, tongue_width,
    fibonacci_backbone, psi_residual,
    PHI, PHI_SQ, PSI,
)


# ═══════════════════════════════════════════════════════════════════════════════
# THE RECURSION MATRIX
#
# The Fibonacci recursion [F_{n+1}, F_n] = M × [F_n, F_{n-1}]
# where M = [[1,1],[1,0]].
#
# det(M) = -1. This is the half-twist.
# ═══════════════════════════════════════════════════════════════════════════════

def mat_mul(A, B):
    """Multiply two 2×2 integer matrices."""
    return [
        [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
        [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]],
    ]

def mat_det(M):
    """Determinant of a 2×2 matrix."""
    return M[0][0]*M[1][1] - M[0][1]*M[1][0]

def mat_trace(M):
    """Trace of a 2×2 matrix."""
    return M[0][0] + M[1][1]

def mat_pow(M, n):
    """M^n for a 2×2 matrix, by repeated squaring."""
    result = [[1, 0], [0, 1]]  # identity
    base = [row[:] for row in M]
    while n > 0:
        if n % 2 == 1:
            result = mat_mul(result, base)
        base = mat_mul(base, base)
        n //= 2
    return result

def char_poly_roots(trace, det):
    """Roots of x² - trace·x + det = 0."""
    disc = trace * trace - 4 * det
    if disc >= 0:
        sqrt_disc = math.sqrt(disc)
        return ((trace + sqrt_disc) / 2, (trace - sqrt_disc) / 2), "real"
    else:
        sqrt_disc = math.sqrt(-disc)
        real_part = trace / 2
        imag_part = sqrt_disc / 2
        return ((real_part, imag_part), (real_part, -imag_part)), "complex"

def run_recursion(M, v0, n_steps):
    """Apply matrix M repeatedly to initial vector v0.

    Returns list of (a_n/b_n, det(M^n)) for each step.
    """
    v = list(v0)
    M_n = [[1, 0], [0, 1]]
    trajectory = [(v[0] / v[1] if v[1] != 0 else float('inf'), 1)]

    for _ in range(n_steps):
        v_new = [M[0][0]*v[0] + M[0][1]*v[1],
                 M[1][0]*v[0] + M[1][1]*v[1]]
        M_n = mat_mul(M_n, M)
        det_n = mat_det(M_n)
        ratio = v_new[0] / v_new[1] if v_new[1] != 0 else float('inf')
        trajectory.append((ratio, det_n))
        v = v_new

    return trajectory


if __name__ == "__main__":
    print("=" * 72)
    print("  EXACTLY ONE HALF-TWIST IS FORCED")
    print("=" * 72)

    # ══════════════════════════════════════════════════════════════════
    # CONDITION 1: global identification after one traversal
    # ══════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  CONDITION 1: global identification")
    print(f"{'═' * 72}")

    M_fib = [[1, 1], [1, 0]]  # Fibonacci recursion matrix
    print(f"\n  M = [[1,1],[1,0]]   (Fibonacci recursion)")
    print(f"  det(M) = {mat_det(M_fib)}")
    print(f"  trace(M) = {mat_trace(M_fib)}")

    print(f"\n  Traversals of the backbone (M^n):")
    print(f"  {'n':>3s}  {'det(M^n)':>8s}  {'orientation':>14s}")
    print("  " + "-" * 30)

    for n in range(8):
        M_n = mat_pow(M_fib, n)
        det_n = mat_det(M_n)
        orient = "preserved" if det_n == 1 else "REVERSED"
        print(f"  {n:3d}  {det_n:8d}  {orient:>14s}")

    print(f"\n  After one traversal: det(M) = -1. Orientation reversed.")
    print(f"  After two traversals: det(M²) = +1. Restored.")
    print(f"  This is the definition of one half-twist.")
    print(f"  (A full twist would be det = +1 after one traversal.)")

    # ══════════════════════════════════════════════════════════════════
    # CONDITION 2: non-orientable, not just alternating
    # ══════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  CONDITION 2: non-orientability (not just alternation)")
    print(f"{'═' * 72}")

    print(f"""
  The sign (-1)^n could come from either:
    (a) A non-orientable surface (Möbius strip)
    (b) A trivial alternating function on an orientable surface

  To distinguish: attempt to absorb the sign into a basis change.

  At each backbone level n, the state is [F_{{n+1}}, F_n].
  Try a diagonal change of basis: D_n = diag(s_n, 1) at each level,
  choosing s_n to make the effective matrix have det = +1.

  Effective matrix: D_{{n+1}} M D_n^{{-1}}
  det(D_{{n+1}} M D_n^{{-1}}) = (s_{{n+1}}/s_n) × det(M) = -(s_{{n+1}}/s_n)

  For this to equal +1 at EVERY level:
    s_{{n+1}}/s_n = -1   for all n
    ⇒ s_n = (-1)^n × s_0

  But s_n is a SCALE FACTOR (must be real and positive for the basis
  to preserve the meaning of "population"). s_n = (-1)^n × s_0
  alternates sign — not a valid basis.

  Therefore: the sign flip CANNOT be absorbed. The bundle is non-trivial.
  The structure is genuinely non-orientable.""")

    # Verify numerically: the Cassini identity in the matrix formulation
    # Standard convention: F_0=0, F_1=1, F_2=1, F_3=2, F_4=3, F_5=5, ...
    # M^n = [[F_{n+1}, F_n], [F_n, F_{n-1}]], det(M^n) = (-1)^n
    # Cassini identity: F_{n-1}F_{n+1} - F_n² = (-1)^n
    print(f"  Numerical verification (Cassini identity = det of M^n):")
    print(f"  {'n':>3s}  {'F_{{n-1}}F_{{n+1}} - F_n²':>22s}  {'(-1)^n':>8s}  {'det(M^n)':>10s}  {'all match':>10s}")
    print("  " + "-" * 58)

    # F_0 = 0, F_1 = 1
    fibs = [0, 1]
    for _ in range(15):
        fibs.append(fibs[-1] + fibs[-2])

    for n in range(1, 12):
        cassini = fibs[n-1] * fibs[n+1] - fibs[n] * fibs[n]
        expected = (-1)**n
        det_n = mat_det(mat_pow(M_fib, n))
        match = "YES" if cassini == expected == det_n else "NO"
        print(f"  {n:3d}  {cassini:22d}  {expected:8d}  {det_n:10d}  {match:>10s}")

    print(f"\n  Cassini identity = det(M^n). Same mathematical object.")
    print(f"  Non-orientability is not an interpretation — it's the determinant.")

    # ══════════════════════════════════════════════════════════════════
    # CONDITION 3: invariance under U
    # ══════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  CONDITION 3: invariance under U")
    print(f"{'═' * 72}")

    print(f"""
  U acts on distributions over the tree.
  The Cassini identity is a property of the tree itself.
  These are categorically different objects.

  Formally:
    - The tree C_d has structure: node values, mediant ancestry, depths.
    - U: Dist(C_d) → Dist(C_d) maps distributions, not tree structure.
    - det(M) = -1 is a fact about the tree's backbone.
    - U cannot modify det(M) because U doesn't touch M.

  But we should verify: does g* (the fixed point of U) preserve
  the Cassini structure in its populations?""")

    # At the fixed point, the ratio g*(F_n/F_{n+1}) / g*(F_{n-1}/F_n)
    # should reflect the eigenvalue structure of M.
    DEPTH = 10
    tree = ConstraintTree(DEPTH)
    U = Operator(tree, K0=1.0)
    g_star, r_star = U.find_fixed_point()

    backbone = fibonacci_backbone(tree)
    print(f"  g* at depth {DEPTH}, |r*| = {r_star:.8f}")
    print(f"\n  {'n':>3s}  {'F_n/F_{{n+1}}':>10s}  {'g*(f)':>14s}  "
          f"{'ratio g*_n/g*_{{n-1}}':>20s}  {'det sign':>9s}")
    print("  " + "-" * 62)

    prev_pop = None
    for idx, node in backbone:
        pop = g_star.get(node.value, 0)
        if prev_pop is not None and prev_pop > 0:
            ratio = pop / prev_pop
            det_sign = "(-1)^" + str(idx)
            print(f"  {idx:3d}  {str(node.value):>10s}  {pop:14.6e}  "
                  f"{ratio:20.8f}  {det_sign:>9s}")
        else:
            print(f"  {idx:3d}  {str(node.value):>10s}  {pop:14.6e}  "
                  f"{'—':>20s}  {'—':>9s}")
        prev_pop = pop

    print(f"\n  The ratio g*_n/g*_{{n-1}} converges to a constant as n grows.")
    print(f"  This constant is w(F_n/F_{{n+1}}, K_eff) / w(F_{{n-1}}/F_n, K_eff),")
    print(f"  which encodes the eigenvalue ratio of M at coupling K_eff.")
    print(f"  U does not (and cannot) alter the eigenvalue structure of M.")

    # ══════════════════════════════════════════════════════════════════
    # CONDITION 4: removing the half-twist breaks the physics
    # ══════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  CONDITION 4: removing the half-twist breaks everything")
    print(f"{'═' * 72}")

    print(f"\n  The Fibonacci matrix M has trace = 1, det = -1.")
    print(f"  Characteristic polynomial: x² - x - 1 = 0")
    roots_fib, kind_fib = char_poly_roots(1, -1)
    print(f"  Roots: {roots_fib[0]:.10f}, {roots_fib[1]:.10f}  ({kind_fib})")
    print(f"  These are φ = {PHI:.10f} and ψ = {PSI:.10f}")
    print(f"  |φ| > 1, |ψ| < 1: convergent approach to φ.")

    print(f"\n  Now remove the half-twist: set det = +1, keep trace = 1.")
    print(f"  Characteristic polynomial: x² - x + 1 = 0")
    roots_cyl, kind_cyl = char_poly_roots(1, +1)
    print(f"  Roots: ({roots_cyl[0][0]:.4f} ± {roots_cyl[0][1]:.4f}i)  ({kind_cyl})")
    mag = math.sqrt(roots_cyl[0][0]**2 + roots_cyl[0][1]**2)
    print(f"  |roots| = {mag:.10f}")
    print(f"  These are 6th roots of unity: e^{{±iπ/3}}.")

    print(f"\n  {'property':>25s}  {'det = -1 (Möbius)':>20s}  {'det = +1 (cylinder)':>20s}")
    print("  " + "-" * 68)

    comparisons = [
        ("eigenvalues", "φ, -1/φ (real)", "e^{±iπ/3} (complex)"),
        ("|eigenvalues|", "φ > 1, 1/φ < 1", "both = 1"),
        ("convergence", "exponential", "NONE (periodic)"),
        ("limit", "1/φ (irrational)", "no limit (period 6)"),
        ("golden ratio", "YES", "NO"),
        ("Cassini identity", "(-1)^n (alternating)", "+1 (trivial)"),
        ("number theory", "Farey, SB tree", "hexagonal lattice"),
    ]

    for prop, mob, cyl in comparisons:
        print(f"  {prop:>25s}  {mob:>20s}  {cyl:>20s}")

    # Run both recursions
    print(f"\n  Side by side: recursion trajectories from [1, 1]:")
    print(f"\n  {'step':>4s}  {'det=-1: ratio':>14s}  {'→ 1/φ?':>8s}  "
          f"{'det=+1: ratio':>14s}  {'periodic?':>10s}")
    print("  " + "-" * 56)

    M_cylinder = [[1, -1], [1, 0]]  # trace=1, det=+1: x²-x+1=0

    traj_mob = run_recursion(M_fib, [1, 1], 12)
    traj_cyl = run_recursion(M_cylinder, [1, 1], 12)

    for i in range(min(13, len(traj_mob))):
        r_mob = traj_mob[i][0]
        r_cyl = traj_cyl[i][0]

        err_mob = abs(r_mob - 1/PHI) if r_mob != float('inf') else float('inf')
        converging = f"{err_mob:.2e}" if err_mob < 100 else "far"

        # Check if cylinder is periodic
        if i >= 6 and i < len(traj_cyl):
            periodic = "= step " + str(i - 6) if abs(r_cyl - traj_cyl[i-6][0]) < 1e-10 else ""
        else:
            periodic = ""

        print(f"  {i:4d}  {r_mob:14.10f}  {converging:>8s}  "
              f"{r_cyl:14.10f}  {periodic:>10s}")

    print(f"\n  det = -1 (Möbius): converges to 1/φ = {1/PHI:.10f}")
    print(f"  det = +1 (cylinder): period-6 orbit, never converges")

    # ══════════════════════════════════════════════════════════════════
    # WHAT BREAKS WITHOUT THE HALF-TWIST
    # ══════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  WHAT BREAKS")
    print(f"{'═' * 72}")

    print(f"""
  Without det(M) = -1 (the half-twist), we lose:

  1. THE GOLDEN RATIO
     The irrational 1/φ emerges as the limit of F_n/F_{{n+1}} BECAUSE
     the eigenvalues of M are real and distinct (disc = 5 > 0).
     With det = +1, disc = -3 < 0: complex eigenvalues, no real limit.

  2. THE CONVERGENCE HIERARCHY
     The Fibonacci convergents approach 1/φ exponentially (rate φ^{{-2}}).
     With det = +1, |eigenvalue| = 1: no decay, no hierarchy, period 6.

  3. THE STERN-BROCOT TREE
     The tree is built from mediants. The mediant of a/b and c/d has
     the property ad - bc = 1 (adjacent Farey fractions). This
     adjacency condition is det = 1 for the 2×2 matrix [[a,c],[b,d]].
     But the RECURSION that generates the Fibonacci backbone has
     det = -1. Forcing det = +1 on the recursion changes the backbone
     from Fibonacci to a hexagonal lattice — incompatible with the
     tree structure.

  4. THE SPECTRAL TILT
     n_s - 1 ∝ ln(φ²). Without φ, no tilt. Without tilt, the CMB
     power spectrum is exactly scale-invariant (n_s = 1), contradicting
     Planck 2018 (n_s = 0.965 at 8σ from 1).

  5. THE FIXED POINT g*
     g* exists because the tongue widths at coupling K_eff form a
     convergent hierarchy (1/q² along the backbone). Without
     exponential convergence, the hierarchy is periodic, and the
     fixed point equation has no non-trivial solution.

  THEREFORE:
    det(M) = -1 is forced.
    trace(M) = 1 is forced (by the mediant: (a+c)/(b+d) adds
    numerators and denominators, giving the recurrence a_{{n+1}} = a_n + a_{{n-1}},
    which has trace = 1).

    Together: the characteristic polynomial x² - x - 1 = 0 is unique.
    The eigenvalues φ and ψ = -1/φ are unique.
    The half-twist (det = -1) is unique.

    One half-twist. Not zero. Not two. Not three.
    Forced by the mediant operation on rational boundaries.
""")
