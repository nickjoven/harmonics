"""
Jacobian of the Klein bottle field equation at its 4-mode fixed point.

D21 item D: Stability analysis, Lie algebra structure, and block decomposition
of the 4-dimensional dynamical system that emerges from the Klein bottle
XOR filter + twist selection rule (Derivation 19).

The 4 surviving modes are:
    (1/3, 1/2), (1/2, 1/3), (1/2, 2/3), (2/3, 1/2)

Usage:
    python sync_cost/derivations/jacobian_fixed_point.py
"""

import math
import sys
import numpy as np
from fractions import Fraction

sys.path.insert(0, "sync_cost/derivations")
from circle_map_utils import PHI, INV_PHI
from field_equation_klein import stern_brocot_tree, tongue_width


# ── The 4 surviving modes ────────────────────────────────────────────────────

MODES = [
    (Fraction(1, 3), Fraction(1, 2)),
    (Fraction(1, 2), Fraction(1, 3)),
    (Fraction(1, 2), Fraction(2, 3)),
    (Fraction(2, 3), Fraction(1, 2)),
]

MODE_LABELS = [f"({f1},{f2})" for f1, f2 in MODES]

N_MODES = len(MODES)


# ── Field equation map (restricted to 4 modes) ──────────────────────────────

def order_parameter(pops):
    """
    Compute r = sum N_i * exp(2*pi*i*(f1+f2)) * (-1)^{q1} / sum N
    with twist in x-direction.
    """
    total = sum(pops)
    if total == 0:
        return 0j
    r = 0j
    for k, (f1, f2) in enumerate(MODES):
        phase = 2 * math.pi * (float(f1) + float(f2))
        sign = (-1) ** f1.denominator  # twist
        r += pops[k] * sign * (math.cos(phase) + 1j * math.sin(phase))
    return r / total


def field_map(pops, g_func, K0=1.0):
    """
    One iteration of F: R^4 -> R^4.

    F_i = N_total * g(f1_i, f2_i) * w(f1_i, K_eff) * w(f2_i, K_eff) / Z

    where Z normalizes to N_total and K_eff = K0 * |r(pops)|.
    """
    N_total = sum(pops)
    r = order_parameter(pops)
    r_abs = abs(r)
    K_eff = K0 * max(r_abs, 1e-15)

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


def find_fixed_point(g_func, K0=1.0, n_iter=800, damping=0.3):
    """Iterate the field map to convergence."""
    pops = np.ones(N_MODES)  # uniform initial
    for it in range(n_iter):
        new = field_map(pops, g_func, K0)
        pops = (1 - damping) * pops + damping * new
    return pops


# ── Jacobian via numerical differentiation ───────────────────────────────────

def compute_jacobian(pops_star, g_func, K0=1.0, eps=1e-6):
    """
    J_ij = dF_i / dN_j computed by central differences.
    """
    J = np.zeros((N_MODES, N_MODES))
    for j in range(N_MODES):
        pops_plus = pops_star.copy()
        pops_minus = pops_star.copy()
        pops_plus[j] += eps
        pops_minus[j] -= eps

        F_plus = field_map(pops_plus, g_func, K0)
        F_minus = field_map(pops_minus, g_func, K0)

        J[:, j] = (F_plus - F_minus) / (2 * eps)

    return J


# ── Analysis functions ───────────────────────────────────────────────────────

def print_matrix(M, name, fmt="{:10.6f}"):
    """Pretty-print a matrix."""
    print(f"\n  {name}:")
    n = M.shape[0]
    # Header
    print(f"  {'':>12s}", end="")
    for j in range(n):
        print(f"  {MODE_LABELS[j]:>12s}", end="")
    print()
    for i in range(n):
        print(f"  {MODE_LABELS[i]:>12s}", end="")
        for j in range(n):
            print(f"  {fmt.format(M[i, j]):>12s}", end="")
        print()


def analyze_eigenvalues(J, label):
    """Compute and report eigenvalues."""
    eigvals = np.linalg.eigvals(J)

    print(f"\n  Eigenvalues of J [{label}]:")
    print(f"  {'index':>6s}  {'real':>12s}  {'imag':>12s}  {'|lambda|':>12s}")
    print("  " + "-" * 48)
    for k, lam in enumerate(eigvals):
        print(f"  {k:6d}  {lam.real:12.8f}  {lam.imag:12.8f}  {abs(lam):12.8f}")

    stable = all(abs(lam) < 1.0 for lam in eigvals)
    print(f"\n  Stability: {'STABLE (all |lambda| < 1)' if stable else 'UNSTABLE'}")

    return eigvals


def analyze_commutator(J, label):
    """Compute [J, J^T] and check normality."""
    JT = J.T
    comm = J @ JT - JT @ J

    print_matrix(comm, f"Commutator [J, J^T] [{label}]", fmt="{:12.8f}")

    norm = np.linalg.norm(comm, 'fro')
    print(f"\n  Frobenius norm of [J, J^T]: {norm:.2e}")

    if norm < 1e-10:
        print("  J is NORMAL (commutes with its transpose)")
    else:
        print("  J is NOT normal")
        # Check if commutator has structure of a Lie bracket
        # A Lie bracket [A,B] is antisymmetric: [A,B]^T = -[A,B]
        antisymm_check = np.linalg.norm(comm + comm.T, 'fro')
        print(f"  Antisymmetry check ||[J,J^T] + [J,J^T]^T||: {antisymm_check:.2e}")
        if antisymm_check < 1e-10:
            print("  Commutator IS antisymmetric (consistent with Lie bracket)")
        else:
            print("  Commutator is NOT antisymmetric")

    return comm


def analyze_block_structure(J, label):
    """
    Check if J decomposes into 2x2 blocks by denominator class.

    Ordering: modes 0,1 have q-pairs (3,2) and (2,3)
              modes 2,3 have q-pairs (2,3) and (3,2)

    Actually, let's identify explicitly:
      Mode 0: (1/3, 1/2) -> q1=3, q2=2 (odd, even)
      Mode 1: (1/2, 1/3) -> q1=2, q2=3 (even, odd)
      Mode 2: (1/2, 2/3) -> q1=2, q2=3 (even, odd)
      Mode 3: (2/3, 1/2) -> q1=3, q2=2 (odd, even)

    Two denominator classes:
      Class A (q1=odd, q2=even): modes 0, 3  -> (1/3,1/2), (2/3,1/2)
      Class B (q1=even, q2=odd): modes 1, 2  -> (1/2,1/3), (1/2,2/3)
    """
    # Reorder to group by class: [0, 3, 1, 2]
    idx = [0, 3, 1, 2]
    J_reordered = J[np.ix_(idx, idx)]

    reordered_labels = [MODE_LABELS[i] for i in idx]

    print(f"\n  Block structure analysis [{label}]:")
    print(f"  Reordering: Class A = {{(1/3,1/2), (2/3,1/2)}}, "
          f"Class B = {{(1/2,1/3), (1/2,2/3)}}")

    print(f"\n  J reordered (A,A | A,B // B,A | B,B):")
    print(f"  {'':>12s}", end="")
    for lab in reordered_labels:
        print(f"  {lab:>12s}", end="")
    print()
    for i in range(4):
        print(f"  {reordered_labels[i]:>12s}", end="")
        for j in range(4):
            val = J_reordered[i, j]
            print(f"  {val:12.8f}", end="")
        print()
        if i == 1:
            print("  " + "-" * 60)

    A = J_reordered[:2, :2]
    B = J_reordered[:2, 2:]
    C = J_reordered[2:, :2]
    D = J_reordered[2:, 2:]

    print(f"\n  Block A (Class A -> Class A):")
    print(f"    {A[0,0]:12.8f}  {A[0,1]:12.8f}")
    print(f"    {A[1,0]:12.8f}  {A[1,1]:12.8f}")

    print(f"\n  Block B (Class A -> Class B, off-diagonal):")
    print(f"    {B[0,0]:12.8f}  {B[0,1]:12.8f}")
    print(f"    {B[1,0]:12.8f}  {B[1,1]:12.8f}")

    print(f"\n  Block C (Class B -> Class A, off-diagonal):")
    print(f"    {C[0,0]:12.8f}  {C[0,1]:12.8f}")
    print(f"    {C[1,0]:12.8f}  {C[1,1]:12.8f}")

    print(f"\n  Block D (Class B -> Class B):")
    print(f"    {D[0,0]:12.8f}  {D[0,1]:12.8f}")
    print(f"    {D[1,0]:12.8f}  {D[1,1]:12.8f}")

    B_norm = np.linalg.norm(B, 'fro')
    C_norm = np.linalg.norm(C, 'fro')
    print(f"\n  ||B|| (off-diagonal A->B): {B_norm:.2e}")
    print(f"  ||C|| (off-diagonal B->A): {C_norm:.2e}")

    if B_norm < 1e-8 and C_norm < 1e-8:
        print("  Sectors are DECOUPLED (block diagonal)")
    else:
        print("  Sectors are COUPLED (non-zero off-diagonal blocks)")
        # Check if B ~ C^T (symmetric coupling)
        diff = np.linalg.norm(B - C.T, 'fro')
        print(f"  ||B - C^T||: {diff:.2e} ", end="")
        if diff < 1e-8:
            print("(symmetric coupling)")
        else:
            print("(asymmetric coupling)")

    return A, B, C, D


def analyze_algebra(J, label):
    """
    Form the traceless part of J and analyze its Lie algebra structure.

    J_0 = J - (tr J / 4) * I  lives in sl(4, R), which is 15-dimensional.
    Check if it lands in a smaller subalgebra.
    """
    tr = np.trace(J)
    J0 = J - (tr / 4) * np.eye(4)

    print(f"\n  Traceless part J_0 = J - (tr/4)*I [{label}]:")
    print(f"  tr(J) = {tr:.8f}")
    print(f"  tr(J_0) = {np.trace(J0):.2e} (should be ~0)")

    print_matrix(J0, f"J_0 [{label}]", fmt="{:12.8f}")

    # Eigenvalues of J0
    eigvals_J0 = np.linalg.eigvals(J0)
    print(f"\n  Eigenvalues of J_0:")
    for k, lam in enumerate(eigvals_J0):
        print(f"    lambda_{k} = {lam.real:12.8f} + {lam.imag:12.8f}i")

    # Check rank
    rank = np.linalg.matrix_rank(J0, tol=1e-8)
    print(f"\n  Rank of J_0: {rank}")

    # Singular values
    svd = np.linalg.svd(J0, compute_uv=False)
    print(f"  Singular values: {svd}")

    # Check if J0 is in su(2) x su(2) ~ so(4)
    # so(4) consists of antisymmetric matrices. Check:
    antisymm_part = (J0 - J0.T) / 2
    symm_part = (J0 + J0.T) / 2

    a_norm = np.linalg.norm(antisymm_part, 'fro')
    s_norm = np.linalg.norm(symm_part, 'fro')
    total_norm = np.linalg.norm(J0, 'fro')

    print(f"\n  Decomposition J_0 = symmetric + antisymmetric:")
    print(f"  ||antisymmetric part||: {a_norm:.8f}")
    print(f"  ||symmetric part||:     {s_norm:.8f}")
    print(f"  ||J_0||:                {total_norm:.8f}")
    print(f"  Ratio antisymm/total:   {a_norm/total_norm:.6f}")
    print(f"  Ratio symm/total:       {s_norm/total_norm:.6f}")

    if s_norm < 1e-8:
        print("  J_0 is ANTISYMMETRIC -> lives in so(4) ~ su(2) x su(2)")
    elif a_norm < 1e-8:
        print("  J_0 is SYMMETRIC -> lives in the symmetric traceless matrices")
    else:
        print("  J_0 has both symmetric and antisymmetric parts")

    # Check if J0^2 is proportional to identity (would mean J0 in a 1-dim subalgebra)
    J0_sq = J0 @ J0
    J0_sq_trace = np.trace(J0_sq)
    J0_sq_expected = (J0_sq_trace / 4) * np.eye(4)
    J0_sq_dev = np.linalg.norm(J0_sq - J0_sq_expected, 'fro')
    print(f"\n  ||J_0^2 - (tr(J_0^2)/4)*I||: {J0_sq_dev:.2e}")
    if J0_sq_dev < 1e-8:
        print("  J_0^2 ~ I  =>  J_0 generates a 1-parameter subgroup")

    # Check if J0 lives in sl(2,R) embedded in sl(4,R)
    # by checking if it's a rank-1 perturbation structure
    # More concretely: check the dimension of the algebra generated by J0
    # Compute J0, J0^2, J0^3 and check linear independence
    mats = [J0.flatten(), (J0 @ J0).flatten(), (J0 @ J0 @ J0).flatten()]
    M = np.vstack(mats)
    algebra_rank = np.linalg.matrix_rank(M, tol=1e-8)
    print(f"\n  Dimension of algebra generated by J_0 (via powers):")
    print(f"  rank({{J_0, J_0^2, J_0^3}}): {algebra_rank}")

    if algebra_rank == 1:
        print("  J_0 generates a 1-dimensional subalgebra (abelian)")
    elif algebra_rank == 2:
        print("  J_0 generates a 2-dimensional subalgebra")
    elif algebra_rank == 3:
        print("  J_0 generates a 3-dimensional subalgebra (possibly sl(2,R))")

    # Check the Killing form structure
    # For sl(2,R): the Killing form B(X,Y) = 4 tr(XY) is nondegenerate
    # Check if J0 and [J0, [J0, J0^T]] close under brackets
    bracket1 = J0 @ J0.T - J0.T @ J0
    bracket2 = J0 @ bracket1 - bracket1 @ J0

    # Check if bracket2 is proportional to J0
    if total_norm > 1e-10:
        # Project bracket2 onto J0
        proj = np.sum(bracket2 * J0) / np.sum(J0 * J0)
        residual = bracket2 - proj * J0
        res_norm = np.linalg.norm(residual, 'fro')
        print(f"\n  Lie bracket closure test:")
        print(f"  [J_0, [J_0, J_0^T]] projected onto J_0: coeff = {proj:.8f}")
        print(f"  Residual norm: {res_norm:.2e}")
        if res_norm < 1e-6:
            print("  -> Closes! J_0 and J_0^T generate a subalgebra")

    # Check symmetry group: does J0 have a tensor product structure?
    # If J0 = A (x) B for 2x2 matrices, then it lives in sl(2) (x) sl(2)
    # Compute SVD of J0 reshaped as 2x2 block matrix of 2x2 blocks
    # using the denominator-class reordering [0,3,1,2]
    idx = [0, 3, 1, 2]
    J0r = J0[np.ix_(idx, idx)]

    # Reshape as (2,2,2,2) and check if rank-1 in the tensor decomposition
    T = J0r.reshape(2, 2, 2, 2)
    # Flatten to (4,4) in the "operator on 2-qubit space" sense
    # This is already J0r. Check its Schmidt rank:
    J0r_reshaped = J0r.reshape(2, 2, 2, 2).transpose(0, 2, 1, 3).reshape(4, 4)
    schmidt_svd = np.linalg.svd(J0r_reshaped, compute_uv=False)
    print(f"\n  Tensor product structure (Schmidt decomposition):")
    print(f"  Schmidt singular values: {schmidt_svd}")
    schmidt_rank = np.sum(schmidt_svd > 1e-8)
    print(f"  Schmidt rank: {schmidt_rank}")
    if schmidt_rank == 1:
        print("  -> J_0 IS a tensor product A (x) B => lives in sl(2) (x) sl(2)")
    elif schmidt_rank == 2:
        print("  -> J_0 is a sum of 2 tensor products")
    else:
        print(f"  -> J_0 is a sum of {schmidt_rank} tensor products (generic)")

    return J0


# ── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 80)
    print("  JACOBIAN OF KLEIN BOTTLE FIELD EQUATION AT 4-MODE FIXED POINT")
    print("  D21 item D: Stability and Lie algebra structure")
    print("=" * 80)

    # g functions
    g_uniform = lambda f1, f2: 1.0
    g_golden = lambda f1, f2: math.exp(
        -5 * ((f1 - INV_PHI) ** 2 + (f2 - INV_PHI) ** 2))

    for g_name, g_func in [("uniform", g_uniform),
                            ("golden-peaked", g_golden)]:
        print(f"\n{'=' * 80}")
        print(f"  g(w1, w2) = {g_name}")
        print(f"{'=' * 80}")

        # 1. Find fixed point
        print(f"\n{'─' * 80}")
        print(f"  1. FIXED POINT")
        print(f"{'─' * 80}")

        pops_star = find_fixed_point(g_func)
        total = pops_star.sum()

        print(f"\n  Fixed point populations (N_total = {total:.4f}):")
        for k in range(N_MODES):
            f1, f2 = MODES[k]
            frac = pops_star[k] / total
            print(f"    {MODE_LABELS[k]:>12s}:  N = {pops_star[k]:.8f}  "
                  f"({100*frac:.2f}%)")

        r = order_parameter(pops_star)
        print(f"\n  Order parameter: r = {r.real:.8f} + {r.imag:.8f}i")
        print(f"  |r| = {abs(r):.8f}")

        # Verify it's a fixed point
        F_star = field_map(pops_star, g_func)
        residual = np.linalg.norm(F_star - pops_star)
        print(f"  ||F(N*) - N*|| = {residual:.2e} (should be ~0)")

        # 2. Jacobian
        print(f"\n{'─' * 80}")
        print(f"  2. JACOBIAN MATRIX")
        print(f"{'─' * 80}")

        J = compute_jacobian(pops_star, g_func)
        print_matrix(J, f"J [{g_name}]")

        # 3. Eigenvalues
        print(f"\n{'─' * 80}")
        print(f"  3. EIGENVALUES AND STABILITY")
        print(f"{'─' * 80}")

        eigvals = analyze_eigenvalues(J, g_name)

        # 4. Commutator
        print(f"\n{'─' * 80}")
        print(f"  4. COMMUTATOR STRUCTURE")
        print(f"{'─' * 80}")

        comm = analyze_commutator(J, g_name)

        # 5. Block decomposition
        print(f"\n{'─' * 80}")
        print(f"  5. BLOCK DECOMPOSITION BY DENOMINATOR CLASS")
        print(f"{'─' * 80}")

        A, B, C, D = analyze_block_structure(J, g_name)

        # 6. Lie algebra structure
        print(f"\n{'─' * 80}")
        print(f"  6. LIE ALGEBRA STRUCTURE")
        print(f"{'─' * 80}")

        J0 = analyze_algebra(J, g_name)

    print(f"\n{'=' * 80}")
    print("  SUMMARY")
    print(f"{'=' * 80}")
    print("""
  The 4-mode Klein bottle field equation admits a 4D fixed-point analysis.
  Key questions answered:
    - Are the fixed points stable? (eigenvalue moduli)
    - Is J normal? (commutator [J, J^T])
    - Do denominator classes decouple? (off-diagonal blocks B, C)
    - What subalgebra does the traceless part inhabit? (sl(4) decomposition)
    - Is there tensor product structure? (Schmidt rank)
""")
    print(f"{'=' * 80}")
    print("  DONE")
    print(f"{'=' * 80}")
