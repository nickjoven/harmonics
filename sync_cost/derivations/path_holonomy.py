"""
Path holonomy on the XOR-filtered Stern-Brocot tree.

The mediant is commutative: med(a,b) = med(b,a).
But PATHS through the tree are not: left-left-right ≠ left-right-left.

The question: does parallel transport around the 4-mode Klein bottle
loop have non-trivial holonomy? If the holonomy group is non-abelian,
the gauge structure exists in the paths, not the vertices.

In the Stern-Brocot tree, each node is reached by a unique binary
path from the root (L = take left child, R = take right child).
The SL(2,Z) matrix associated with each path is:
  L → [[1, 0], [1, 1]]
  R → [[1, 1], [0, 1]]

These generate SL(2,Z), which is non-abelian.
The path from node A to node B through the tree has a well-defined
SL(2,Z) matrix = (path to B) × (path to A)^{-1}.
"""

import numpy as np
from fractions import Fraction

# ============================================================
# Stern-Brocot path matrices
# ============================================================

L = np.array([[1, 0], [1, 1]])  # Left child
R = np.array([[1, 1], [0, 1]])  # Right child

def sb_path(p, q):
    """
    Find the Stern-Brocot path (sequence of L, R moves) to p/q.
    Returns the product matrix and the path string.
    """
    if q == 0:
        return np.eye(2, dtype=int), ""

    # Mediant search
    a_n, a_d = 0, 1  # left boundary
    b_n, b_d = 1, 0  # right boundary (infinity)

    M = np.eye(2, dtype=int)
    path = ""

    for _ in range(100):  # safety limit
        m_n = a_n + b_n
        m_d = a_d + b_d
        if m_n == p and m_d == q:
            break
        elif p * m_d < m_n * q:  # p/q < mediant: go left
            b_n, b_d = m_n, m_d
            M = M @ L
            path += "L"
        else:  # p/q > mediant: go right
            a_n, a_d = m_n, m_d
            M = M @ R
            path += "R"

    return M, path


# ============================================================
# The 4 Klein bottle modes and their SL(2,Z) matrices
# ============================================================

modes_1d = [(1, 2), (1, 3), (2, 3)]

print("=" * 70)
print("  STERN-BROCOT PATH MATRICES")
print("=" * 70)

matrices = {}
for p, q in modes_1d:
    M, path = sb_path(p, q)
    matrices[(p, q)] = M
    f = Fraction(p, q)
    # Verify: M applied to (0/1, 1/0) gives the fraction
    # The matrix maps the initial interval to the node
    print(f"\n  {p}/{q}:  path = {path}")
    print(f"  M = [{M[0,0]:2d} {M[0,1]:2d}]")
    print(f"      [{M[1,0]:2d} {M[1,1]:2d}]")
    print(f"  det(M) = {np.linalg.det(M):.0f}")


# ============================================================
# Transport matrices between modes
# ============================================================

print("\n" + "=" * 70)
print("  TRANSPORT MATRICES (path from A to B)")
print("=" * 70)

def transport(A, B):
    """SL(2,Z) matrix for parallel transport from mode A to mode B."""
    M_A = matrices[A]
    M_B = matrices[B]
    # Transport = M_B @ M_A^{-1}
    # For SL(2,Z): [[a,b],[c,d]]^{-1} = [[d,-b],[-c,a]] (det=1)
    M_A_inv = np.array([[M_A[1,1], -M_A[0,1]],
                         [-M_A[1,0], M_A[0,0]]])
    T = M_B @ M_A_inv
    return T

for A in modes_1d:
    for B in modes_1d:
        if A == B:
            continue
        T = transport(A, B)
        print(f"\n  T({A[0]}/{A[1]} → {B[0]}/{B[1]}) = [{T[0,0]:3d} {T[0,1]:3d}]")
        print(f"                        [{T[1,0]:3d} {T[1,1]:3d}]")
        print(f"  det = {int(round(np.linalg.det(T)))}")


# ============================================================
# Holonomy around loops
# ============================================================

print("\n" + "=" * 70)
print("  HOLONOMY AROUND LOOPS")
print("=" * 70)

def loop_holonomy(cycle):
    """Holonomy = product of transport matrices around a cycle."""
    H = np.eye(2, dtype=int)
    for i in range(len(cycle)):
        A = cycle[i]
        B = cycle[(i + 1) % len(cycle)]
        T = transport(A, B)
        H = T @ H
    return H

# All 3-cycles
cycles_3 = [
    [(1,2), (1,3), (2,3)],
    [(1,2), (2,3), (1,3)],  # reversed
]

for cycle in cycles_3:
    labels = " → ".join(f"{p}/{q}" for p, q in cycle) + f" → {cycle[0][0]}/{cycle[0][1]}"
    H = loop_holonomy(cycle)
    print(f"\n  Loop: {labels}")
    print(f"  H = [{H[0,0]:3d} {H[0,1]:3d}]")
    print(f"      [{H[1,0]:3d} {H[1,1]:3d}]")
    print(f"  det = {int(round(np.linalg.det(H)))}")
    print(f"  tr  = {H[0,0] + H[1,1]}")
    if np.array_equal(H, np.eye(2, dtype=int)):
        print("  => TRIVIAL holonomy (identity)")
    elif np.array_equal(H, -np.eye(2, dtype=int)):
        print("  => Z₂ holonomy (-I)")
    else:
        # Classify: |tr| < 2 elliptic, |tr| = 2 parabolic, |tr| > 2 hyperbolic
        tr = abs(H[0,0] + H[1,1])
        if tr < 2:
            print(f"  => ELLIPTIC (|tr| = {tr} < 2)")
        elif tr == 2:
            print(f"  => PARABOLIC (|tr| = {tr})")
        else:
            print(f"  => HYPERBOLIC (|tr| = {tr} > 2)")

# ============================================================
# Non-commutativity test
# ============================================================

print("\n" + "=" * 70)
print("  NON-COMMUTATIVITY TEST")
print("=" * 70)

T_12_to_13 = transport((1,2), (1,3))
T_12_to_23 = transport((1,2), (2,3))

# Forward: 1/2 → 1/3 → 2/3
path_forward = transport((1,3), (2,3)) @ T_12_to_13
# Reversed: 1/2 → 2/3 → 1/3
path_reversed = transport((2,3), (1,3)) @ T_12_to_23

print(f"\n  Path 1/2 → 1/3 → 2/3:")
print(f"  [{path_forward[0,0]:3d} {path_forward[0,1]:3d}]")
print(f"  [{path_forward[1,0]:3d} {path_forward[1,1]:3d}]")

print(f"\n  Path 1/2 → 2/3 → 1/3:")
print(f"  [{path_reversed[0,0]:3d} {path_reversed[0,1]:3d}]")
print(f"  [{path_reversed[1,0]:3d} {path_reversed[1,1]:3d}]")

commutator = path_forward @ np.linalg.inv(path_reversed).astype(int)
print(f"\n  Commutator [forward, reversed⁻¹]:")
print(f"  [{commutator[0,0]:6.2f} {commutator[0,1]:6.2f}]")
print(f"  [{commutator[1,0]:6.2f} {commutator[1,1]:6.2f}]")

if np.allclose(commutator, np.eye(2)):
    print("  => COMMUTATIVE (paths give same result)")
else:
    print("  => NON-COMMUTATIVE (path order matters)")
    print("  => The holonomy group is NON-ABELIAN")


# ============================================================
# The 2D Klein bottle: holonomy on product paths
# ============================================================

print("\n" + "=" * 70)
print("  2D KLEIN BOTTLE: PRODUCT PATH HOLONOMY")
print("=" * 70)

# The 4 Klein bottle modes as pairs
kb_modes = [
    ((1,3), (1,2)),
    ((1,2), (1,3)),
    ((1,2), (2,3)),
    ((2,3), (1,2)),
]

print("\n  The 4 Klein bottle modes:")
for i, ((p1,q1), (p2,q2)) in enumerate(kb_modes):
    M1 = matrices[(p1,q1)]
    M2 = matrices[(p2,q2)]
    # Product matrix (Kronecker product for 2D)
    print(f"  Mode {i}: ({p1}/{q1}, {p2}/{q2})")

# Transport in the product space is tensor product of transports
def transport_2d(A, B):
    """Transport between 2D Klein bottle modes."""
    T1 = transport(A[0], B[0])
    T2 = transport(A[1], B[1])
    return np.kron(T1, T2)

# The fundamental loop: visit all 4 modes and return
loop_4 = [kb_modes[0], kb_modes[1], kb_modes[2], kb_modes[3]]

H4 = np.eye(4, dtype=float)
labels = []
for i in range(4):
    A = loop_4[i]
    B = loop_4[(i+1) % 4]
    T = transport_2d(A, B)
    H4 = T @ H4
    labels.append(f"({A[0][0]}/{A[0][1]},{A[1][0]}/{A[1][1]})")

labels_str = " → ".join(labels) + " → " + labels[0]
print(f"\n  Loop: {labels_str}")
print(f"\n  Holonomy (4×4):")
for i in range(4):
    print(f"  [{' '.join(f'{H4[i,j]:8.3f}' for j in range(4))}]")

eigvals = np.linalg.eigvals(H4)
print(f"\n  Eigenvalues: {[f'{ev:.4f}' for ev in sorted(eigvals, key=lambda x: -abs(x))]}")
print(f"  det = {np.linalg.det(H4):.4f}")
print(f"  tr  = {np.trace(H4):.4f}")

if np.allclose(H4, np.eye(4)):
    print("  => TRIVIAL holonomy")
else:
    print("  => NON-TRIVIAL holonomy")
    rank = np.linalg.matrix_rank(H4 - np.eye(4), tol=1e-6)
    print(f"  Rank of (H - I): {rank}")


# ============================================================
# The holonomy group
# ============================================================

print("\n" + "=" * 70)
print("  HOLONOMY GROUP STRUCTURE")
print("=" * 70)

# Generate holonomy group elements by composing all pairwise transports
generators_1d = []
for A in modes_1d:
    for B in modes_1d:
        if A != B:
            generators_1d.append(transport(A, B))

# Multiply generators and check closure
group_elements = [np.eye(2, dtype=int)]
to_process = list(generators_1d)
max_group = 48  # SL(2,Z) is infinite; cap at reasonable size

while to_process and len(group_elements) < max_group:
    g = to_process.pop(0)
    # Check if g is already in the group
    already = False
    for h in group_elements:
        if np.array_equal(g, h):
            already = True
            break
    if not already:
        group_elements.append(g)
        # Multiply with all existing elements
        for h in group_elements[:-1]:
            new = g @ h
            to_process.append(new)
            new2 = h @ g
            to_process.append(new2)

print(f"\n  Holonomy group generated by transports between {{1/2, 1/3, 2/3}}:")
print(f"  Found {len(group_elements)} elements (capped at {max_group})")

if len(group_elements) < max_group:
    print(f"  Group ORDER = {len(group_elements)}")
    # Check if it's abelian
    abelian = True
    for g in group_elements:
        for h in group_elements:
            if not np.array_equal(g @ h, h @ g):
                abelian = False
                break
        if not abelian:
            break
    print(f"  Abelian: {abelian}")

    # Known groups of this order
    if len(group_elements) == 1:
        print("  => Trivial group {e}")
    elif len(group_elements) == 2:
        print("  => Z₂")
    elif len(group_elements) == 6 and not abelian:
        print("  => S₃ (symmetric group on 3 elements)")
    elif len(group_elements) == 8 and not abelian:
        print("  => D₄ or Q₈")
    elif len(group_elements) == 24 and not abelian:
        print("  => S₄ (symmetric group on 4 elements)")
else:
    print(f"  Group is INFINITE (>{max_group} elements)")
    print("  This is a subgroup of SL(2,Z)")
    # Check if it's the full SL(2,Z) by looking for parabolic elements
    has_parabolic = False
    has_hyperbolic = False
    has_elliptic = False
    for g in group_elements:
        tr = abs(g[0,0] + g[1,1])
        if tr < 2:
            has_elliptic = True
        elif tr == 2 and not np.array_equal(g, np.eye(2, dtype=int)):
            has_parabolic = True
        elif tr > 2:
            has_hyperbolic = True
    print(f"  Has elliptic:   {has_elliptic}")
    print(f"  Has parabolic:  {has_parabolic}")
    print(f"  Has hyperbolic: {has_hyperbolic}")
    if has_elliptic and has_parabolic and has_hyperbolic:
        print("  => Contains all three types: likely generates all of SL(2,Z)")
