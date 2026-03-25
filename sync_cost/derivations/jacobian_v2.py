"""
Jacobian of the Klein bottle field equation at the Mobius operating point.

v2: Instead of solving for the self-consistent r (which gives r = 0, making
K_eff = 0 and the Jacobian degenerate rank-1), we FIX r at the dynamically
observed operating point (r ~ 0.48-0.61 from klein_bottle_kuramoto.py).

At r > 0, tongue widths differ by q:
  w(1/2, K) ~ K/(2pi) >> w(1/3, K) ~ (K/2)^3/3

This breaks the degeneracy and reveals the true stability structure.

Usage:
    python sync_cost/derivations/jacobian_v2.py
"""

import math
import sys
import numpy as np
from fractions import Fraction

sys.path.insert(0, "sync_cost/derivations")
from circle_map_utils import PHI, INV_PHI
from field_equation_klein import stern_brocot_tree, tongue_width


# -- The 4 surviving Klein bottle modes ------------------------------------

MODES = [
    (Fraction(1, 3), Fraction(1, 2)),
    (Fraction(1, 2), Fraction(1, 3)),
    (Fraction(1, 2), Fraction(2, 3)),
    (Fraction(2, 3), Fraction(1, 2)),
]

MODE_LABELS = [f"({f1},{f2})" for f1, f2 in MODES]
N_MODES = len(MODES)

# Class A (q1 odd, q2 even): modes 0, 3 -> (1/3,1/2), (2/3,1/2)
# Class B (q1 even, q2 odd): modes 1, 2 -> (1/2,1/3), (1/2,2/3)
CLASS_A = [0, 3]
CLASS_B = [1, 2]
BLOCK_ORDER = [0, 3, 1, 2]  # A then B


# -- Field equation at FIXED r (not self-consistent) -----------------------

def field_map_fixed_r(pops, g_func, K0, r_fixed):
    """
    One iteration of the field equation with r held fixed externally.

    F_i = N_total * g(f1_i, f2_i) * w(f1_i, K_eff) * w(f2_i, K_eff) / Z

    where K_eff = K0 * r_fixed (NOT computed from pops).
    """
    N_total = sum(pops)
    K_eff = K0 * r_fixed

    raw = np.zeros(N_MODES)
    for k, (f1, f2) in enumerate(MODES):
        g = g_func(float(f1), float(f2))
        w1 = tongue_width(f1.numerator, f1.denominator, K_eff)
        w2 = tongue_width(f2.numerator, f2.denominator, K_eff)
        raw[k] = N_total * g * w1 * w2

    # Normalize so sum = N_total
    Z = raw.sum()
    if Z > 0:
        raw *= N_total / Z

    return raw


def find_fixed_point_fixed_r(g_func, K0, r_fixed, n_iter=800, damping=0.3):
    """Iterate the field map at fixed r to convergence."""
    pops = np.ones(N_MODES)
    for _ in range(n_iter):
        new = field_map_fixed_r(pops, g_func, K0, r_fixed)
        pops = (1 - damping) * pops + damping * new
    return pops


# -- Jacobian via central differences --------------------------------------

def compute_jacobian(pops_star, g_func, K0, r_fixed, eps=1e-6):
    """J_ij = dF_i / dN_j by central differences at fixed r."""
    J = np.zeros((N_MODES, N_MODES))
    for j in range(N_MODES):
        pops_plus = pops_star.copy()
        pops_minus = pops_star.copy()
        pops_plus[j] += eps
        pops_minus[j] -= eps

        F_plus = field_map_fixed_r(pops_plus, g_func, K0, r_fixed)
        F_minus = field_map_fixed_r(pops_minus, g_func, K0, r_fixed)

        J[:, j] = (F_plus - F_minus) / (2 * eps)

    return J


# -- Display helpers --------------------------------------------------------

def print_matrix(M, name, labels=None, fmt="{:10.6f}"):
    if labels is None:
        labels = MODE_LABELS
    print(f"\n  {name}:")
    n = M.shape[0]
    print(f"  {'':>12s}", end="")
    for j in range(n):
        print(f"  {labels[j]:>12s}", end="")
    print()
    for i in range(n):
        print(f"  {labels[i]:>12s}", end="")
        for j in range(n):
            print(f"  {fmt.format(M[i, j]):>12s}", end="")
        print()


def print_eigenvalues(eigvals, label):
    print(f"\n  Eigenvalues [{label}]:")
    print(f"  {'#':>4s}  {'real':>14s}  {'imag':>14s}  {'|lambda|':>14s}  {'arg/pi':>10s}")
    print("  " + "-" * 62)
    for k, lam in enumerate(sorted(eigvals, key=lambda x: -abs(x))):
        arg = math.atan2(lam.imag, lam.real) / math.pi if abs(lam) > 1e-15 else 0
        print(f"  {k:4d}  {lam.real:14.10f}  {lam.imag:14.10f}  "
              f"{abs(lam):14.10f}  {arg:10.6f}")

    # Check for conjugate pairs
    print(f"\n  Conjugate pair check:")
    used = [False] * len(eigvals)
    pairs = []
    for i in range(len(eigvals)):
        if used[i]:
            continue
        for j in range(i + 1, len(eigvals)):
            if used[j]:
                continue
            if abs(eigvals[i] - eigvals[j].conjugate()) < 1e-8:
                pairs.append((i, j))
                used[i] = used[j] = True
                print(f"    lambda_{i} and lambda_{j} are conjugate")
                break
        if not used[i]:
            print(f"    lambda_{i} = {eigvals[i].real:.10f} is real (unpaired)")
            used[i] = True

    # Check eigenvalue ratios
    print(f"\n  Eigenvalue ratios:")
    sorted_ev = sorted(eigvals, key=lambda x: -abs(x))
    if abs(sorted_ev[0]) > 1e-12:
        for i in range(1, len(sorted_ev)):
            ratio = abs(sorted_ev[i]) / abs(sorted_ev[0])
            print(f"    |lambda_{i}|/|lambda_0| = {ratio:.10f}")


# -- Block structure analysis -----------------------------------------------

def analyze_blocks(J, label):
    """Reorder to Class A / Class B and analyze 2x2 blocks."""
    J_r = J[np.ix_(BLOCK_ORDER, BLOCK_ORDER)]
    reordered_labels = [MODE_LABELS[i] for i in BLOCK_ORDER]

    print(f"\n  Block structure [{label}]:")
    print(f"  Reorder: Class A={{(1/3,1/2),(2/3,1/2)}}, Class B={{(1/2,1/3),(1/2,2/3)}}")
    print_matrix(J_r, f"J reordered (A|B)", labels=reordered_labels, fmt="{:12.8f}")

    AA = J_r[:2, :2]
    AB = J_r[:2, 2:]
    BA = J_r[2:, :2]
    BB = J_r[2:, 2:]

    for name, blk in [("AA (A->A)", AA), ("AB (A->B)", AB),
                       ("BA (B->A)", BA), ("BB (B->B)", BB)]:
        print(f"\n  Block {name}:")
        print(f"    [{blk[0,0]:12.8f}  {blk[0,1]:12.8f}]")
        print(f"    [{blk[1,0]:12.8f}  {blk[1,1]:12.8f}]")

    ab_norm = np.linalg.norm(AB, 'fro')
    ba_norm = np.linalg.norm(BA, 'fro')
    print(f"\n  ||AB||_F = {ab_norm:.6e}")
    print(f"  ||BA||_F = {ba_norm:.6e}")

    if ab_norm < 1e-8 and ba_norm < 1e-8:
        print("  => DECOUPLED (block diagonal)")
    else:
        print("  => COUPLED sectors")
        # Symmetry of off-diagonal coupling
        diff_sym = np.linalg.norm(AB - BA.T, 'fro')
        diff_antisym = np.linalg.norm(AB + BA.T, 'fro')
        print(f"  ||AB - BA^T||_F = {diff_sym:.6e}  (0 => symmetric coupling)")
        print(f"  ||AB + BA^T||_F = {diff_antisym:.6e}  (0 => antisymmetric coupling)")

    return AA, AB, BA, BB


# -- Traceless part and Lie algebra -----------------------------------------

def analyze_algebra(J, label):
    tr = np.trace(J)
    J0 = J - (tr / N_MODES) * np.eye(N_MODES)

    print(f"\n  Traceless part J_0 [{label}]:")
    print(f"  tr(J) = {tr:.10f}")
    print(f"  tr(J_0) = {np.trace(J0):.2e}")
    print_matrix(J0, f"J_0", fmt="{:12.8f}")

    # Eigenvalues of J0
    ev0 = np.linalg.eigvals(J0)
    print_eigenvalues(ev0, f"J_0 [{label}]")

    # Rank
    rank = np.linalg.matrix_rank(J0, tol=1e-8)
    svd = np.linalg.svd(J0, compute_uv=False)
    print(f"\n  Rank of J_0: {rank}")
    print(f"  Singular values: [{', '.join(f'{s:.10f}' for s in svd)}]")

    # Symmetric / antisymmetric decomposition
    anti = (J0 - J0.T) / 2
    sym = (J0 + J0.T) / 2
    a_norm = np.linalg.norm(anti, 'fro')
    s_norm = np.linalg.norm(sym, 'fro')
    total_norm = np.linalg.norm(J0, 'fro')

    print(f"\n  Symmetric/antisymmetric decomposition:")
    print(f"  ||antisymm||  = {a_norm:.10f}")
    print(f"  ||symm||      = {s_norm:.10f}")
    print(f"  ||J_0||       = {total_norm:.10f}")
    if total_norm > 1e-12:
        print(f"  antisymm/total = {a_norm/total_norm:.6f}")
        print(f"  symm/total     = {s_norm/total_norm:.6f}")

    if s_norm < 1e-8 * total_norm:
        print("  => J_0 is ANTISYMMETRIC -> so(4) ~ su(2) x su(2)")
    elif a_norm < 1e-8 * total_norm:
        print("  => J_0 is SYMMETRIC")
    else:
        print("  => J_0 has both symmetric and antisymmetric parts")

    # Commutator [J0, J0^T]
    comm = J0 @ J0.T - J0.T @ J0
    comm_norm = np.linalg.norm(comm, 'fro')
    print(f"\n  [J_0, J_0^T]:")
    print_matrix(comm, "Commutator [J_0, J_0^T]", fmt="{:12.8f}")
    print(f"  ||[J_0, J_0^T]||_F = {comm_norm:.6e}")
    if comm_norm < 1e-10:
        print("  => J_0 is NORMAL")
    else:
        # Check antisymmetry of commutator
        ca = np.linalg.norm(comm + comm.T, 'fro')
        print(f"  ||comm + comm^T|| = {ca:.6e}  (0 => antisymmetric commutator)")

    # J0^2 proportional to identity?
    J0sq = J0 @ J0
    tr_sq = np.trace(J0sq)
    dev = np.linalg.norm(J0sq - (tr_sq / N_MODES) * np.eye(N_MODES), 'fro')
    print(f"\n  J_0^2 vs (tr(J_0^2)/4)*I:")
    print(f"  tr(J_0^2) = {tr_sq:.10f}")
    print(f"  ||J_0^2 - (tr/4)*I|| = {dev:.6e}")
    if dev < 1e-6:
        print("  => J_0^2 ~ I => 1-parameter subgroup")

    # Algebra dimension from powers
    mats = [J0.flatten()]
    for k in range(2, 5):
        Jk = np.linalg.matrix_power(J0, k)
        mats.append(Jk.flatten())
    M = np.vstack(mats)
    alg_rank = np.linalg.matrix_rank(M, tol=1e-8)
    print(f"\n  Algebra dimension (powers J_0, J_0^2, J_0^3, J_0^4):")
    print(f"  rank = {alg_rank}")

    # Lie bracket closure: [J0, [J0, J0^T]] proportional to J0?
    bracket1 = J0 @ J0.T - J0.T @ J0
    bracket2 = J0 @ bracket1 - bracket1 @ J0
    if total_norm > 1e-10:
        proj = np.sum(bracket2 * J0) / np.sum(J0 * J0)
        residual = bracket2 - proj * J0
        res_norm = np.linalg.norm(residual, 'fro')
        print(f"\n  Lie bracket closure [J_0, [J_0, J_0^T]]:")
        print(f"  projection onto J_0: coeff = {proj:.10f}")
        print(f"  residual norm = {res_norm:.6e}")
        if res_norm < 1e-4 * total_norm:
            print("  => CLOSES: J_0, J_0^T generate a finite subalgebra")

    # Nested brackets: dimension of Lie algebra generated by {J0, J0^T}
    basis = [J0, J0.T]
    bracket_1_2 = J0 @ J0.T - J0.T @ J0
    basis.append(bracket_1_2)
    # [J0, bracket_1_2]
    b3 = J0 @ bracket_1_2 - bracket_1_2 @ J0
    basis.append(b3)
    # [J0^T, bracket_1_2]
    b4 = J0.T @ bracket_1_2 - bracket_1_2 @ J0.T
    basis.append(b4)

    flat = np.vstack([b.flatten() for b in basis])
    lie_dim = np.linalg.matrix_rank(flat, tol=1e-8)
    print(f"\n  Lie algebra generated by {{J_0, J_0^T}}:")
    print(f"  dim(span(J_0, J_0^T, [J_0,J_0^T], [J_0,[..]], [J_0^T,[..]])) = {lie_dim}")
    if lie_dim <= 3:
        print(f"  => {lie_dim}-dimensional subalgebra (sl(2,R) is 3-dim)")
    elif lie_dim <= 6:
        print(f"  => {lie_dim}-dimensional subalgebra (so(4) ~ su(2)+su(2) is 6-dim)")

    # Schmidt rank (tensor product structure) in class A/B basis
    idx = BLOCK_ORDER
    J0r = J0[np.ix_(idx, idx)]
    J0r_reshaped = J0r.reshape(2, 2, 2, 2).transpose(0, 2, 1, 3).reshape(4, 4)
    schmidt_svd = np.linalg.svd(J0r_reshaped, compute_uv=False)
    schmidt_rank = np.sum(schmidt_svd > 1e-8)
    print(f"\n  Tensor product structure (Schmidt decomposition in A/B basis):")
    print(f"  Schmidt singular values: [{', '.join(f'{s:.10f}' for s in schmidt_svd)}]")
    print(f"  Schmidt rank: {schmidt_rank}")
    if schmidt_rank == 1:
        print("  => J_0 = A x B (tensor product in su(2) x su(2))")

    return J0


# -- Tongue width diagnostics -----------------------------------------------

def print_tongue_widths(r_fixed, K0):
    K_eff = K0 * r_fixed
    print(f"\n  Tongue widths at K_eff = {K_eff:.6f} (r = {r_fixed}, K0 = {K0}):")
    for f1, f2 in MODES:
        w1 = tongue_width(f1.numerator, f1.denominator, K_eff)
        w2 = tongue_width(f2.numerator, f2.denominator, K_eff)
        print(f"    {MODE_LABELS[MODES.index((f1,f2))]:>12s}: "
              f"w({f1})={w1:.8f}  w({f2})={w2:.8f}  product={w1*w2:.10f}")
    # Individual tongue widths
    print(f"\n  Individual tongue widths:")
    for p, q in [(1, 2), (1, 3), (2, 3)]:
        w = tongue_width(p, q, K_eff)
        print(f"    w({p}/{q}, {K_eff:.4f}) = {w:.10f}")
    w12 = tongue_width(1, 2, K_eff)
    w13 = tongue_width(1, 3, K_eff)
    if w13 > 1e-15:
        print(f"\n  Ratio w(1/2)/w(1/3) = {w12/w13:.4f}")


# -- Main -------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 80)
    print("  JACOBIAN v2: KLEIN BOTTLE FIELD EQUATION AT MOBIUS OPERATING POINT")
    print("  Fixed r (not self-consistent) -- breaks the rank-1 degeneracy")
    print("=" * 80)

    K0 = 1.0
    R_VALUES = [0.1, 0.3, 0.5, 0.6, 0.8]

    g_uniform = lambda f1, f2: 1.0
    g_golden = lambda f1, f2: math.exp(
        -5 * ((f1 - INV_PHI) ** 2 + (f2 - INV_PHI) ** 2))

    for g_name, g_func in [("uniform", g_uniform),
                            ("golden-peaked", g_golden)]:

        print(f"\n{'#' * 80}")
        print(f"#  g(w1, w2) = {g_name}")
        print(f"{'#' * 80}")

        for r_fixed in R_VALUES:

            print(f"\n{'=' * 80}")
            print(f"  r_fixed = {r_fixed}   |   g = {g_name}   |   K_eff = {K0 * r_fixed:.4f}")
            print(f"{'=' * 80}")

            # 0. Tongue widths
            print_tongue_widths(r_fixed, K0)

            # 1. Fixed point at this r
            print(f"\n{'~' * 60}")
            print(f"  1. FIXED POINT at r = {r_fixed}")
            print(f"{'~' * 60}")

            pops_star = find_fixed_point_fixed_r(g_func, K0, r_fixed)
            total = pops_star.sum()

            print(f"\n  Fixed point populations (N_total = {total:.6f}):")
            for k in range(N_MODES):
                frac = pops_star[k] / total
                print(f"    {MODE_LABELS[k]:>12s}:  N = {pops_star[k]:.8f}  "
                      f"({100*frac:.4f}%)")

            # Verify fixed point
            F_star = field_map_fixed_r(pops_star, g_func, K0, r_fixed)
            residual = np.linalg.norm(F_star - pops_star)
            print(f"  ||F(N*) - N*|| = {residual:.2e}")

            # 2. Jacobian
            print(f"\n{'~' * 60}")
            print(f"  2. JACOBIAN at r = {r_fixed}")
            print(f"{'~' * 60}")

            J = compute_jacobian(pops_star, g_func, K0, r_fixed)
            print_matrix(J, f"J (r={r_fixed})")

            # 3. Eigenvalues
            print(f"\n{'~' * 60}")
            print(f"  3. EIGENVALUES at r = {r_fixed}")
            print(f"{'~' * 60}")

            eigvals = np.linalg.eigvals(J)
            rank_J = np.linalg.matrix_rank(J, tol=1e-8)
            print(f"\n  Rank of J: {rank_J}")
            print_eigenvalues(eigvals, f"r={r_fixed}")

            # Stability
            max_ev = max(abs(lam) for lam in eigvals)
            print(f"\n  Spectral radius: {max_ev:.10f}")
            if max_ev < 1.0:
                print("  => STABLE (all |lambda| < 1)")
            elif abs(max_ev - 1.0) < 1e-6:
                print("  => MARGINALLY STABLE (|lambda| ~ 1)")
            else:
                print("  => UNSTABLE")

            # 4. Block structure
            print(f"\n{'~' * 60}")
            print(f"  4. BLOCK STRUCTURE at r = {r_fixed}")
            print(f"{'~' * 60}")

            AA, AB, BA, BB = analyze_blocks(J, f"r={r_fixed}")

            # 5. Traceless part and Lie algebra
            print(f"\n{'~' * 60}")
            print(f"  5. TRACELESS PART AND LIE ALGEBRA at r = {r_fixed}")
            print(f"{'~' * 60}")

            J0 = analyze_algebra(J, f"r={r_fixed}")

    # -- Summary across r values --
    print(f"\n\n{'#' * 80}")
    print(f"#  SUMMARY: EIGENVALUE SPECTRUM vs r")
    print(f"{'#' * 80}")

    for g_name, g_func in [("uniform", g_uniform),
                            ("golden-peaked", g_golden)]:
        print(f"\n  g = {g_name}")
        print(f"  {'r':>6s}  {'rank':>4s}  {'|lam_1|':>12s}  {'|lam_2|':>12s}  "
              f"{'|lam_3|':>12s}  {'|lam_4|':>12s}  {'stable?':>8s}")
        print("  " + "-" * 72)

        for r_fixed in R_VALUES:
            pops = find_fixed_point_fixed_r(g_func, K0, r_fixed)
            J = compute_jacobian(pops, g_func, K0, r_fixed)
            ev = sorted(np.linalg.eigvals(J), key=lambda x: -abs(x))
            rank = np.linalg.matrix_rank(J, tol=1e-8)
            stable = "YES" if all(abs(lam) < 1.0 for lam in ev) else "NO"
            print(f"  {r_fixed:6.2f}  {rank:4d}  " +
                  "  ".join(f"{abs(lam):12.8f}" for lam in ev) +
                  f"  {stable:>8s}")

    print(f"\n{'=' * 80}")
    print("  DONE")
    print(f"{'=' * 80}")
