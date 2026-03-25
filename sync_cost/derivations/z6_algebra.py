"""
D21-E: Does Z₆ = Z₂ × Z₃ grow into SU(2) × SU(3)?

The fiber bundle computation showed:
- The GCD reduction (equality operator) on Klein bottle fibers has
  structure Z₂ × Z₃ = Z₆ = center(SU(2) × SU(3))
- The mediant doesn't commute with scaling

The question: does the nonlinear self-consistency loop
  N → r → K_eff → w → N
grow the center Z₆ into the full group SU(2) × SU(3)?

Method: compute the Jacobian of the EXTENDED field equation that
includes the fiber representatives (not just the irreducible modes).
The extended system has modes at kp/kq for k = 1, 2, 3. The GCD
acts as a projection. The Jacobian of the projected system encodes
how perturbations in the fiber directions affect the base modes.

If the projected Jacobian has the Lie algebra structure of
su(2) ⊕ su(3), the full group emerges from the self-consistency loop.
"""

import sys
import math
import numpy as np
from fractions import Fraction
from math import gcd

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2]))
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from circle_map_utils import PHI, INV_PHI
from field_equation_klein import tongue_width


# ============================================================
# Extended mode space: base modes + fiber representatives
# ============================================================

# Base Klein bottle modes (irreducible)
BASE_MODES = [
    (Fraction(1, 3), Fraction(1, 2)),  # mode 0: (q₁=3, q₂=2)
    (Fraction(1, 2), Fraction(1, 3)),  # mode 1: (q₁=2, q₂=3)
    (Fraction(1, 2), Fraction(2, 3)),  # mode 2: (q₁=2, q₂=3)
    (Fraction(2, 3), Fraction(1, 2)),  # mode 3: (q₁=3, q₂=2)
]

# Fiber representatives: scale each base mode by k = 2, 3
# These are reducible fractions at deeper tree positions
def fiber_reps(p, q, max_k=3):
    """Return [(kp, kq, k)] for k = 1..max_k."""
    return [(k * p, k * q, k) for k in range(1, max_k + 1)]


# Build extended mode list: base + fiber reps for each slot
def build_extended_modes(max_k=3):
    """
    Extended mode space: for each base mode (f1, f2), include
    all (k1*f1_num/k1*f1_den, k2*f2_num/k2*f2_den) with k1, k2 in 1..max_k.
    Each extended mode maps to a base mode via GCD reduction.
    """
    extended = []
    for base_idx, (f1, f2) in enumerate(BASE_MODES):
        p1, q1 = f1.numerator, f1.denominator
        p2, q2 = f2.numerator, f2.denominator
        for k1 in range(1, max_k + 1):
            for k2 in range(1, max_k + 1):
                ext_p1, ext_q1 = k1 * p1, k1 * q1
                ext_p2, ext_q2 = k2 * p2, k2 * q2
                # XOR check on EXTENDED denominators
                xor_ok = (ext_q1 + ext_q2) % 2 == 1
                extended.append({
                    'base_idx': base_idx,
                    'f1': Fraction(ext_p1, ext_q1),  # auto-reduces
                    'f1_unreduced': (ext_p1, ext_q1),
                    'f2': Fraction(ext_p2, ext_q2),
                    'f2_unreduced': (ext_p2, ext_q2),
                    'k1': k1, 'k2': k2,
                    'xor_ok': xor_ok,
                    'gcd1': gcd(ext_p1, ext_q1),
                    'gcd2': gcd(ext_p2, ext_q2),
                })
    return extended


# ============================================================
# Part 1: Map out the extended mode space
# ============================================================

print("=" * 70)
print("  EXTENDED MODE SPACE (fiber representatives)")
print("=" * 70)

ext_modes = build_extended_modes(max_k=3)

print(f"\n  Total extended modes: {len(ext_modes)}")
print(f"  XOR-allowed: {sum(1 for m in ext_modes if m['xor_ok'])}")
print(f"  XOR-forbidden: {sum(1 for m in ext_modes if not m['xor_ok'])}")

print(f"\n  {'base':>5s}  {'k1':>3s} {'k2':>3s}  {'unreduced':>14s}  {'reduced':>14s}  "
      f"{'GCD':>6s}  {'XOR':>4s}")
print("  " + "-" * 60)

for m in ext_modes:
    p1u, q1u = m['f1_unreduced']
    p2u, q2u = m['f2_unreduced']
    label = f"({p1u}/{q1u}, {p2u}/{q2u})"
    reduced = f"({m['f1']}, {m['f2']})"
    gcds = f"({m['gcd1']},{m['gcd2']})"
    xor = "✓" if m['xor_ok'] else "✗"
    print(f"  {m['base_idx']:5d}  {m['k1']:3d} {m['k2']:3d}  {label:>14s}  "
          f"{reduced:>14s}  {gcds:>6s}  {xor:>4s}")


# ============================================================
# Part 2: The GCD projection matrix
# ============================================================

print("\n" + "=" * 70)
print("  GCD PROJECTION: extended → base")
print("=" * 70)

# For XOR-allowed extended modes, build the projection matrix
# that maps them to base modes
allowed = [m for m in ext_modes if m['xor_ok']]
n_allowed = len(allowed)
n_base = len(BASE_MODES)

print(f"\n  XOR-allowed extended modes: {n_allowed}")
print(f"  Base modes: {n_base}")

# Projection matrix P: n_base × n_allowed
# P[i, j] = 1 if extended mode j reduces to base mode i
P = np.zeros((n_base, n_allowed))
for j, m in enumerate(allowed):
    P[m['base_idx'], j] = 1.0

print(f"\n  Projection matrix P ({n_base} × {n_allowed}):")
print(f"  Rank of P: {np.linalg.matrix_rank(P)}")

# The kernel of P: extended modes that map to the same base mode
# These are the "gauge degrees of freedom"
# dim(ker P) = n_allowed - rank(P)
gauge_dof = n_allowed - np.linalg.matrix_rank(P)
print(f"  Gauge degrees of freedom: {gauge_dof}")


# ============================================================
# Part 3: Field equation on extended space
# ============================================================

print("\n" + "=" * 70)
print("  FIELD EQUATION ON EXTENDED SPACE")
print("=" * 70)

def field_map_extended(pops, g_func, K0, r_fixed):
    """
    Field equation on extended (XOR-allowed) modes.
    Uses UNREDUCED denominators for tongue widths.
    """
    N_total = sum(pops)
    K_eff = K0 * r_fixed
    raw = np.zeros(len(pops))

    for i, m in enumerate(allowed):
        p1u, q1u = m['f1_unreduced']
        p2u, q2u = m['f2_unreduced']
        g = g_func(float(m['f1']), float(m['f2']))
        w1 = tongue_width(p1u, q1u, K_eff)
        w2 = tongue_width(p2u, q2u, K_eff)
        raw[i] = N_total * g * w1 * w2

    Z = raw.sum()
    if Z > 0:
        raw *= N_total / Z
    return raw


def find_extended_fp(g_func, K0, r_fixed, n_iter=1000, damping=0.2):
    """Find fixed point of extended field equation."""
    pops = np.ones(n_allowed)
    for _ in range(n_iter):
        new = field_map_extended(pops, g_func, K0, r_fixed)
        pops = (1 - damping) * pops + damping * new
    return pops


def jacobian_extended(pops_star, g_func, K0, r_fixed, eps=1e-7):
    """Jacobian of extended field equation."""
    n = len(pops_star)
    J = np.zeros((n, n))
    for j in range(n):
        pp = pops_star.copy()
        pm = pops_star.copy()
        pp[j] += eps
        pm[j] -= eps
        J[:, j] = (field_map_extended(pp, g_func, K0, r_fixed) -
                    field_map_extended(pm, g_func, K0, r_fixed)) / (2 * eps)
    return J


# Solve at r = 0.5
g_golden = lambda f1, f2: math.exp(-5 * ((f1 - INV_PHI)**2 + (f2 - INV_PHI)**2))
r_fixed = 0.5
K0 = 1.0

print(f"\n  Solving at r = {r_fixed}, K0 = {K0}...")
pops_star = find_extended_fp(g_golden, K0, r_fixed)
total = pops_star.sum()

print(f"\n  Fixed point ({n_allowed} modes):")
for i, m in enumerate(allowed):
    p1u, q1u = m['f1_unreduced']
    p2u, q2u = m['f2_unreduced']
    frac = pops_star[i] / total
    if frac > 0.01:
        print(f"    ({p1u}/{q1u}, {p2u}/{q2u}) k=({m['k1']},{m['k2']}): "
              f"{frac:.4f}  base={m['base_idx']}")

# ============================================================
# Part 4: Jacobian and its algebra
# ============================================================

print(f"\n  Computing Jacobian ({n_allowed}×{n_allowed})...")
J_ext = jacobian_extended(pops_star, g_golden, K0, r_fixed)

rank_J = np.linalg.matrix_rank(J_ext, tol=1e-8)
eigvals = np.linalg.eigvals(J_ext)
eigvals_sorted = sorted(eigvals, key=lambda x: -abs(x))

print(f"  Rank: {rank_J}")
print(f"  Top eigenvalues (by magnitude):")
for i, ev in enumerate(eigvals_sorted[:10]):
    print(f"    λ_{i}: {ev.real:12.8f} + {ev.imag:12.8f}i  "
          f"|λ| = {abs(ev):.8f}")


# ============================================================
# Part 5: Project Jacobian to base space and fiber space
# ============================================================

print("\n" + "=" * 70)
print("  PROJECTED JACOBIAN")
print("=" * 70)

# J_base = P @ J_ext @ P^T (pseudoinverse for non-square)
# Actually: P @ J_ext @ P^+ where P^+ is the pseudoinverse
P_pinv = np.linalg.pinv(P)
J_base = P @ J_ext @ P_pinv

print(f"\n  J_base (projected to {n_base}×{n_base} base space):")
for i in range(n_base):
    print(f"  [{' '.join(f'{J_base[i,j]:10.6f}' for j in range(n_base))}]")

eigvals_base = np.linalg.eigvals(J_base)
print(f"\n  Base eigenvalues:")
for i, ev in enumerate(sorted(eigvals_base, key=lambda x: -abs(x))):
    print(f"    λ_{i}: {ev.real:12.8f} + {ev.imag:12.8f}i")

# The FIBER part: the kernel of P contains the gauge directions
# Project J into the fiber (kernel) directions
U, s, Vt = np.linalg.svd(P)
# Kernel of P = last (n_allowed - rank) rows of Vt
kernel_rank = n_allowed - np.linalg.matrix_rank(P)
if kernel_rank > 0:
    K_basis = Vt[-kernel_rank:, :]  # kernel basis vectors

    # Project J into kernel
    J_fiber = K_basis @ J_ext @ K_basis.T

    print(f"\n  J_fiber (projected to {kernel_rank}×{kernel_rank} fiber/gauge space):")
    if kernel_rank <= 12:
        for i in range(kernel_rank):
            print(f"  [{' '.join(f'{J_fiber[i,j]:9.5f}' for j in range(kernel_rank))}]")

    eigvals_fiber = np.linalg.eigvals(J_fiber)
    print(f"\n  Fiber eigenvalues ({kernel_rank} total):")
    for i, ev in enumerate(sorted(eigvals_fiber, key=lambda x: -abs(x))[:12]):
        print(f"    λ_{i}: {ev.real:12.8f} + {ev.imag:12.8f}i  |λ|={abs(ev):.6f}")

    # Traceless part
    J_fiber_0 = J_fiber - (np.trace(J_fiber) / kernel_rank) * np.eye(kernel_rank)
    rank_0 = np.linalg.matrix_rank(J_fiber_0, tol=1e-8)

    print(f"\n  Traceless fiber Jacobian:")
    print(f"    Rank: {rank_0}")
    print(f"    Trace: {np.trace(J_fiber_0):.2e}")

    # Antisymmetric part (Lie algebra generators are antisymmetric)
    anti = (J_fiber_0 - J_fiber_0.T) / 2
    sym = (J_fiber_0 + J_fiber_0.T) / 2
    anti_norm = np.linalg.norm(anti, 'fro')
    sym_norm = np.linalg.norm(sym, 'fro')
    total_norm = np.linalg.norm(J_fiber_0, 'fro')

    print(f"    ||antisymmetric|| = {anti_norm:.6f}")
    print(f"    ||symmetric||     = {sym_norm:.6f}")
    print(f"    ||total||         = {total_norm:.6f}")
    if total_norm > 1e-10:
        print(f"    antisym fraction  = {anti_norm/total_norm:.4f}")

    # Dimension of the Lie algebra generated by J_fiber_0 and its transpose
    basis_mats = [J_fiber_0, J_fiber_0.T]
    comm = J_fiber_0 @ J_fiber_0.T - J_fiber_0.T @ J_fiber_0
    basis_mats.append(comm)
    comm2 = J_fiber_0 @ comm - comm @ J_fiber_0
    basis_mats.append(comm2)
    comm3 = J_fiber_0.T @ comm - comm @ J_fiber_0.T
    basis_mats.append(comm3)
    comm4 = comm @ comm2 - comm2 @ comm
    basis_mats.append(comm4)

    flat = np.vstack([m.flatten() for m in basis_mats])
    lie_dim = np.linalg.matrix_rank(flat, tol=1e-6)

    print(f"\n  Lie algebra dimension (from nested brackets):")
    print(f"    dim = {lie_dim}")
    print(f"    (su(2) = 3, su(3) = 8, su(2)⊕su(3) = 11)")

    # Cross-coupling: does the fiber Jacobian mix the Z₂ and Z₃ sectors?
    # Group the fiber modes by their GCD structure
    print(f"\n  Fiber mode GCD structure:")
    for i in range(kernel_rank):
        # Which extended modes contribute to this kernel vector?
        v = K_basis[i, :]
        contrib = [(j, v[j]) for j in range(n_allowed) if abs(v[j]) > 0.01]
        gcds = [(allowed[j]['gcd1'], allowed[j]['gcd2'], v_j)
                for j, v_j in contrib]
        print(f"    Kernel mode {i}: {len(contrib)} contributors, "
              f"GCDs: {[(g1,g2) for g1,g2,_ in gcds[:5]]}")

else:
    print("  No fiber directions (all modes independent)")


# ============================================================
# Part 6: The mediant as a map on the extended space
# ============================================================

print("\n" + "=" * 70)
print("  MEDIANT MAP ON EXTENDED SPACE")
print("=" * 70)

print("\n  For each pair of XOR-allowed extended modes, compute their")
print("  mediant and check which extended mode it maps to.\n")

# Build mediant connection matrix
n = n_allowed
M_med = np.zeros((n, n, n))  # M[i,j,k] = 1 if med(mode_i, mode_j) = mode_k

med_results = {}
for i in range(n):
    for j in range(i+1, n):
        mi, mj = allowed[i], allowed[j]
        p1i, q1i = mi['f1_unreduced']
        p2i, q2i = mi['f2_unreduced']
        p1j, q1j = mj['f1_unreduced']
        p2j, q2j = mj['f2_unreduced']

        # Mediant in both slots
        med_p1 = p1i + p1j
        med_q1 = q1i + q1j
        med_p2 = p2i + p2j
        med_q2 = q2i + q2j

        # Reduce
        g1 = gcd(med_p1, med_q1)
        g2 = gcd(med_p2, med_q2)
        red_f1 = Fraction(med_p1, med_q1)
        red_f2 = Fraction(med_p2, med_q2)

        # Check XOR on unreduced
        xor_ok = (med_q1 + med_q2) % 2 == 1

        # Find if it matches any existing extended mode
        target = None
        for k, mk in enumerate(allowed):
            if (mk['f1_unreduced'] == (med_p1, med_q1) and
                mk['f2_unreduced'] == (med_p2, med_q2)):
                target = k
                break

        key = (i, j)
        med_results[key] = {
            'unreduced': (med_p1, med_q1, med_p2, med_q2),
            'reduced': (red_f1, red_f2),
            'gcd': (g1, g2),
            'xor': xor_ok,
            'target': target,
        }

# Count statistics
n_xor_ok = sum(1 for v in med_results.values() if v['xor'])
n_hits = sum(1 for v in med_results.values() if v['target'] is not None)
n_new = sum(1 for v in med_results.values() if v['xor'] and v['target'] is None)

print(f"  Total mediant pairs: {len(med_results)}")
print(f"  XOR-allowed mediants: {n_xor_ok}")
print(f"  Hit existing extended mode: {n_hits}")
print(f"  New modes (XOR-ok but not in extended set): {n_new}")

# Show the most interesting: mediants that land on base modes
print(f"\n  Mediants landing on base modes (after GCD reduction):")
for (i, j), v in med_results.items():
    rf1, rf2 = v['reduced']
    for base_idx, (bf1, bf2) in enumerate(BASE_MODES):
        if rf1 == bf1 and rf2 == bf2:
            mi, mj = allowed[i], allowed[j]
            p1i, q1i = mi['f1_unreduced']
            p2i, q2i = mi['f2_unreduced']
            p1j, q1j = mj['f1_unreduced']
            p2j, q2j = mj['f2_unreduced']
            print(f"    med(({p1i}/{q1i},{p2i}/{q2i}), ({p1j}/{q1j},{p2j}/{q2j})) "
                  f"= {v['unreduced'][:2]} × {v['unreduced'][2:]} "
                  f"→ ({rf1},{rf2}) = base mode {base_idx}  "
                  f"GCD=({v['gcd'][0]},{v['gcd'][1]})")

# ============================================================
# Summary
# ============================================================

print("\n" + "=" * 70)
print("  SUMMARY")
print("=" * 70)
print(f"""
  Extended mode space: {n_allowed} XOR-allowed modes (from {len(ext_modes)} total)
  Base modes: {n_base}
  Gauge DOF (fiber): {gauge_dof}
  Extended Jacobian rank: {rank_J}
  Fiber Jacobian Lie dimension: {lie_dim if kernel_rank > 0 else 'N/A'}

  Key question: does the fiber Lie dimension match su(2) ⊕ su(3) = 11?
""")
