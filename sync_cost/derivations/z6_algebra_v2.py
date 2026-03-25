"""
D21-E v2: Z₆ algebra with DEPTH-DEPENDENT tongue widths.

v1 failed because tongue_width(p,q,K) uses the irreducible fraction,
making all fiber representatives degenerate. But on the Stern-Brocot
tree, 3/9 is at depth 9 and 1/3 is at depth 3. Their tongue widths
differ exponentially: (K/2)^9 vs (K/2)^3.

Fix: use tongue_width(kp, kq, K) = (K/2)^(kq) — the unreduced
denominator determines the tongue width. The fiber is then
exponentially graded by tree depth, and different representatives
have genuinely different dynamics.
"""

import sys
import math
import numpy as np
from fractions import Fraction
from math import gcd

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2]))
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from circle_map_utils import INV_PHI


def tongue_width_unreduced(p, q, K):
    """Tongue width using the UNREDUCED denominator."""
    if q == 0:
        return 0.0
    if q == 1:
        return min(K / (2 * math.pi), 1.0)
    return 2 * (K / 2) ** q / q


# ============================================================
# Extended mode space
# ============================================================

BASE_MODES = [
    (Fraction(1, 3), Fraction(1, 2)),
    (Fraction(1, 2), Fraction(1, 3)),
    (Fraction(1, 2), Fraction(2, 3)),
    (Fraction(2, 3), Fraction(1, 2)),
]

def build_extended(max_k=4):
    """Build extended modes with XOR filter on unreduced denominators."""
    modes = []
    for base_idx, (f1, f2) in enumerate(BASE_MODES):
        p1, q1 = f1.numerator, f1.denominator
        p2, q2 = f2.numerator, f2.denominator
        for k1 in range(1, max_k + 1):
            for k2 in range(1, max_k + 1):
                kp1, kq1 = k1 * p1, k1 * q1
                kp2, kq2 = k2 * p2, k2 * q2
                xor_ok = (kq1 + kq2) % 2 == 1
                if xor_ok:
                    modes.append({
                        'base_idx': base_idx,
                        'p1': kp1, 'q1': kq1,
                        'p2': kp2, 'q2': kq2,
                        'k1': k1, 'k2': k2,
                        'f1_val': kp1 / kq1,
                        'f2_val': kp2 / kq2,
                    })
    return modes


# ============================================================
# Field equation with depth-dependent widths
# ============================================================

def field_map(pops, modes, g_func, K_eff):
    """Field equation: N_i = N_total * g_i * w1_i * w2_i, normalized."""
    N_total = np.sum(pops)
    raw = np.zeros(len(modes))
    for i, m in enumerate(modes):
        g = g_func(m['f1_val'], m['f2_val'])
        w1 = tongue_width_unreduced(m['p1'], m['q1'], K_eff)
        w2 = tongue_width_unreduced(m['p2'], m['q2'], K_eff)
        raw[i] = N_total * g * w1 * w2
    Z = np.sum(raw)
    if Z > 0:
        raw *= N_total / Z
    return raw


def find_fp(modes, g_func, K_eff, n_iter=2000, damping=0.15):
    """Find fixed point."""
    n = len(modes)
    pops = np.ones(n)
    for _ in range(n_iter):
        new = field_map(pops, modes, g_func, K_eff)
        pops = (1 - damping) * pops + damping * new
    return pops


def compute_jacobian(pops, modes, g_func, K_eff, eps=1e-7):
    """Jacobian by central differences."""
    n = len(pops)
    J = np.zeros((n, n))
    for j in range(n):
        pp, pm = pops.copy(), pops.copy()
        pp[j] += eps
        pm[j] -= eps
        J[:, j] = (field_map(pp, modes, g_func, K_eff) -
                    field_map(pm, modes, g_func, K_eff)) / (2 * eps)
    return J


# ============================================================
# Run
# ============================================================

g_golden = lambda f1, f2: math.exp(-5 * ((f1 - INV_PHI)**2 + (f2 - INV_PHI)**2))

for max_k in [3, 4]:
    modes = build_extended(max_k)
    n = len(modes)
    n_base = len(BASE_MODES)

    print("=" * 70)
    print(f"  DEPTH-DEPENDENT FIBER: max_k = {max_k}, {n} XOR-allowed modes")
    print("=" * 70)

    # Build projection matrix
    P = np.zeros((n_base, n))
    for j, m in enumerate(modes):
        P[m['base_idx'], j] = 1.0

    gauge_dof = n - np.linalg.matrix_rank(P)
    print(f"  Base modes: {n_base}, Gauge DOF: {gauge_dof}")

    for K_eff in [0.3, 0.5, 0.7]:
        print(f"\n  --- K_eff = {K_eff} ---")

        # Show tongue widths for representatives of 1/3
        print(f"  Tongue widths for fiber over 1/3:")
        for k in range(1, max_k + 1):
            w = tongue_width_unreduced(k, 3*k, K_eff)
            print(f"    k={k}: w({k}/{3*k}) = {w:.2e}  "
                  f"(ratio to k=1: {w / tongue_width_unreduced(1, 3, K_eff):.4e})")

        # Fixed point
        pops = find_fp(modes, g_golden, K_eff)
        total = np.sum(pops)

        # Group by base mode
        base_pops = np.zeros(n_base)
        for j, m in enumerate(modes):
            base_pops[m['base_idx']] += pops[j]

        print(f"\n  Base mode populations (summed over fiber):")
        for i in range(n_base):
            f1, f2 = BASE_MODES[i]
            print(f"    ({f1},{f2}): {base_pops[i]/total:.4f}")

        # Within-fiber distribution
        print(f"\n  Fiber distribution (population within each base mode):")
        for base_idx in range(n_base):
            f1, f2 = BASE_MODES[base_idx]
            fiber_modes = [(j, m, pops[j]) for j, m in enumerate(modes)
                          if m['base_idx'] == base_idx]
            fiber_total = sum(p for _, _, p in fiber_modes)
            if fiber_total > 0:
                print(f"    Base ({f1},{f2}):")
                for j, m, p in sorted(fiber_modes, key=lambda x: -x[2]):
                    frac = p / fiber_total
                    print(f"      k=({m['k1']},{m['k2']}): "
                          f"{m['p1']}/{m['q1']}×{m['p2']}/{m['q2']}  "
                          f"pop={p/total:.6f}  fiber_frac={frac:.4f}")

        # Jacobian
        J = compute_jacobian(pops, modes, g_func=g_golden, K_eff=K_eff)
        rank_J = np.linalg.matrix_rank(J, tol=1e-8)
        eigvals = np.linalg.eigvals(J)
        eigvals_sorted = sorted(eigvals, key=lambda x: -abs(x))

        print(f"\n  Jacobian: rank = {rank_J} (of {n})")
        n_show = min(12, n)
        print(f"  Top {n_show} eigenvalues:")
        for i in range(n_show):
            ev = eigvals_sorted[i]
            print(f"    λ_{i}: {ev.real:12.8f} + {ev.imag:12.8f}i  "
                  f"|λ|={abs(ev):.8f}")

        # Fiber Jacobian
        U, s, Vt = np.linalg.svd(P)
        kernel_rank = n - np.linalg.matrix_rank(P)
        if kernel_rank > 0:
            K_basis = Vt[-kernel_rank:, :]
            J_fiber = K_basis @ J @ K_basis.T

            eigvals_fiber = np.linalg.eigvals(J_fiber)
            eigvals_fiber_sorted = sorted(eigvals_fiber, key=lambda x: -abs(x))

            # Count significant eigenvalues
            sig = sum(1 for ev in eigvals_fiber if abs(ev) > 1e-6)
            print(f"\n  Fiber Jacobian: {kernel_rank}×{kernel_rank}, "
                  f"{sig} significant eigenvalues")

            for i in range(min(8, kernel_rank)):
                ev = eigvals_fiber_sorted[i]
                print(f"    λ_{i}: {ev.real:12.8f} + {ev.imag:12.8f}i  "
                      f"|λ|={abs(ev):.8f}")

            # Traceless part and Lie algebra
            J_f0 = J_fiber - (np.trace(J_fiber) / kernel_rank) * np.eye(kernel_rank)
            rank_f0 = np.linalg.matrix_rank(J_f0, tol=1e-6)

            anti = (J_f0 - J_f0.T) / 2
            anti_norm = np.linalg.norm(anti, 'fro')
            total_norm = np.linalg.norm(J_f0, 'fro')

            # Lie algebra dimension
            basis = [J_f0, J_f0.T]
            comm = J_f0 @ J_f0.T - J_f0.T @ J_f0
            basis.append(comm)
            for b in [J_f0, J_f0.T]:
                basis.append(b @ comm - comm @ b)
            comm2 = comm @ comm
            basis.append(comm2)

            flat = np.vstack([m.flatten() for m in basis])
            lie_dim = np.linalg.matrix_rank(flat, tol=1e-4)

            print(f"\n  Traceless fiber Jacobian:")
            print(f"    Rank: {rank_f0}")
            print(f"    ||J_f0|| = {total_norm:.6f}")
            if total_norm > 1e-10:
                print(f"    Antisym fraction: {anti_norm/total_norm:.4f}")
            print(f"    Lie algebra dim: {lie_dim}")
            print(f"    (target: su(2)⊕su(3) = 3+8 = 11)")

            # Check for specific dimensions
            if lie_dim == 3:
                print("    => su(2) or sl(2,R)")
            elif lie_dim == 8:
                print("    => su(3)")
            elif lie_dim == 11:
                print("    => su(2) ⊕ su(3)  *** MATCH ***")
            elif lie_dim == 6:
                print("    => so(4) ~ su(2) ⊕ su(2)")
            else:
                print(f"    => {lie_dim}-dimensional algebra")

print("\n" + "=" * 70)
print("  DONE")
print("=" * 70)
