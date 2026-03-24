"""
Discrete Hilbert space over Q.

Basis:          {|p/q⟩} for each node in the Stern-Brocot tree
Inner product:  ⟨p/q | p'/q'⟩ = δ_{p/q, p'/q'}
Normalization:  Σ |ψ(p/q)|² = 1  and  Σ g*(p/q) = 1

Hamiltonian:    H[i,j] = A[i,j] × √(w_i × w_j)

  A[i,j] = 1 if |p_i q_j - p_j q_i| = 1 (Farey neighbors), else 0
  w_i = tongue_width(p_i, q_i, K)

Two adjacency choices, tested separately:
  TREE:   parent-child edges only (exponential localization)
  FAREY:  all |ad-bc|=1 pairs (includes long-range hopping)

The claim: the ground state |ψ₀⟩ of H_Farey satisfies
  |ψ₀(p/q)|² = g*(p/q)
  corr(log|ψ₀|², log g*) → 1
  slope(log|ψ₀|² vs log g*) → 1

No reals. No continuous space. Only rationals and adjacency.

Usage:
    python sync_cost/derivations/quantum_walk.py
"""

import math
import cmath
import sys
from fractions import Fraction

import numpy as np

sys.path.insert(0, "sync_cost/derivations")
from universe_loop import (
    ConstraintTree, Operator, tongue_width,
    fibonacci_backbone, PHI, PSI,
)


# ═══════════════════════════════════════════════════════════════════════════════
# ADJACENCY MATRICES
# ═══════════════════════════════════════════════════════════════════════════════

def build_tree_adjacency(tree):
    """Tree adjacency: parent-child edges only."""
    nodes = tree.all_nodes
    N = len(nodes)
    index = {n.value: i for i, n in enumerate(nodes)}
    A = np.zeros((N, N), dtype=float)

    for node in nodes:
        i = index[node.value]
        for parent in (node.left_parent, node.right_parent):
            if parent is not None and parent.value in index:
                j = index[parent.value]
                A[i, j] = 1.0
                A[j, i] = 1.0

    return A, nodes, index


def build_farey_adjacency(tree):
    """Farey adjacency: |p_i q_j - p_j q_i| = 1.

    This is the natural adjacency on Q. It includes tree edges
    plus long-range connections. Node 1/3 connects directly to
    3/8 (depth 3), not just through the tree path.
    """
    nodes = tree.all_nodes
    N = len(nodes)
    index = {n.value: i for i, n in enumerate(nodes)}
    A = np.zeros((N, N), dtype=float)

    for i in range(N):
        pi, qi = nodes[i].p, nodes[i].q
        for j in range(i + 1, N):
            pj, qj = nodes[j].p, nodes[j].q
            if abs(pi * qj - pj * qi) == 1:
                A[i, j] = 1.0
                A[j, i] = 1.0

    return A


# ═══════════════════════════════════════════════════════════════════════════════
# HAMILTONIAN AND GROUND STATE
# ═══════════════════════════════════════════════════════════════════════════════

def build_hamiltonian(A, w):
    """H[i,j] = A[i,j] × √(w_i × w_j).

    The tongue widths enter as the inner product metric.
    H is real symmetric → real eigenvalues, orthonormal eigenvectors.
    """
    N = len(w)
    sqrt_w = np.sqrt(w)
    H = A * np.outer(sqrt_w, sqrt_w)
    return H


def ground_state(H):
    """Ground state = eigenvector of largest eigenvalue.

    Perron-Frobenius: on a connected non-negative graph,
    the dominant eigenvector has all-positive components.

    Returns (ψ₀, E₀, |ψ₀|²) with Σ|ψ₀|² = 1.
    """
    eigenvalues, eigenvectors = np.linalg.eigh(H)
    psi0 = eigenvectors[:, -1]
    if psi0[0] < 0:
        psi0 = -psi0
    prob = psi0 ** 2
    return psi0, eigenvalues[-1], prob


# ═══════════════════════════════════════════════════════════════════════════════
# DIAGNOSTICS
# ═══════════════════════════════════════════════════════════════════════════════

def log_correlation(x, y):
    """Pearson r of log(x) vs log(y), plus slope."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    mask = (x > 0) & (y > 0)
    n = mask.sum()
    if n < 3:
        return 0.0, 0.0, n
    lx, ly = np.log(x[mask]), np.log(y[mask])
    mx, my = lx.mean(), ly.mean()
    dx, dy = lx - mx, ly - my
    vx, vy = np.dot(dx, dx), np.dot(dy, dy)
    if vx == 0 or vy == 0:
        return 0.0, 0.0, n
    cov = np.dot(dx, dy)
    return cov / math.sqrt(vx * vy), cov / vx, n


def residual_stats(psi_sq, g_prob):
    """Stats of log(|ψ|²/g*) — should → 0 if they agree."""
    ratio = psi_sq / g_prob
    lr = np.log(ratio[ratio > 0])
    if len(lr) == 0:
        return 0.0, 0.0, 0.0
    return lr.mean(), lr.std(), np.max(np.abs(lr))


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 72)
    print("  DISCRETE HILBERT SPACE OVER Q")
    print("  fixed-point convergence = spectral decomposition")
    print("=" * 72)

    DEPTH = 8
    K = 1.0
    tree = ConstraintTree(DEPTH)
    N = len(tree)
    nodes = tree.all_nodes
    print(f"\n  Stern-Brocot tree, depth {DEPTH}, N = {N}")
    print(f"  Basis: {{|p/q⟩}}. No reals. No continuum.")

    # ── Classical fixed point ──────────────────────────────────────────
    U = Operator(tree, K0=K)
    g_star, r_star = U.find_fixed_point()
    g_vec = np.array([g_star[n.value] for n in nodes])
    g_prob = g_vec / g_vec.sum()

    print(f"  Classical: |r*| = {r_star:.10f}, Σg* = {g_prob.sum():.15f}")

    # ── Tongue widths ──────────────────────────────────────────────────
    w_vec = np.array([tongue_width(n.p, n.q, K) for n in nodes])

    # ── Both adjacencies ───────────────────────────────────────────────
    A_tree, _, index = build_tree_adjacency(tree)
    A_farey = build_farey_adjacency(tree)

    n_tree_edges = int(A_tree.sum() / 2)
    n_farey_edges = int(A_farey.sum() / 2)
    print(f"\n  Tree edges:  {n_tree_edges}")
    print(f"  Farey edges: {n_farey_edges}  "
          f"({n_farey_edges - n_tree_edges} long-range)")

    # ══════════════════════════════════════════════════════════════════════
    # CORE TEST: TREE vs FAREY HAMILTONIAN
    # ══════════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  H[i,j] = A[i,j] × √(w_i × w_j)")
    print(f"{'═' * 72}")

    results = {}
    for label, A in [("TREE", A_tree), ("FAREY", A_farey)]:
        H = build_hamiltonian(A, w_vec)
        psi0, E0, psi0_sq = ground_state(H)

        r_log, slope, n_pts = log_correlation(psi0_sq, g_prob)
        mean_r, std_r, max_r = residual_stats(psi0_sq, g_prob)

        results[label] = (psi0, E0, psi0_sq, r_log, slope)

        print(f"\n  {label} adjacency:")
        print(f"    E₀ = {E0:.10f}")
        print(f"    Σ|ψ₀|² = {psi0_sq.sum():.15f}")
        print(f"    corr(log|ψ₀|², log g*) = {r_log:.8f}")
        print(f"    slope(log|ψ₀|² vs log g*) = {slope:.8f}")
        print(f"    residual: mean={mean_r:.4f}, std={std_r:.4f}, max={max_r:.4f}")

    # ══════════════════════════════════════════════════════════════════════
    # FIBONACCI BACKBONE — both adjacencies
    # ══════════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  FIBONACCI BACKBONE")
    print(f"{'═' * 72}")

    backbone = fibonacci_backbone(tree)
    fib_idxs = [index[node.value] for _, node in backbone]

    _, _, psi_tree = results["TREE"][0], results["TREE"][1], results["TREE"][2]
    _, _, psi_farey = results["FAREY"][0], results["FAREY"][1], results["FAREY"][2]

    fib_g = g_prob[fib_idxs]
    fib_tree = psi_tree[fib_idxs]
    fib_farey = psi_farey[fib_idxs]

    r_fib_t, sl_fib_t, _ = log_correlation(fib_tree, fib_g)
    r_fib_f, sl_fib_f, _ = log_correlation(fib_farey, fib_g)

    print(f"\n  Fibonacci subset ({len(backbone)} nodes):")
    print(f"    TREE:  corr = {r_fib_t:.6f}, slope = {sl_fib_t:.6f}")
    print(f"    FAREY: corr = {r_fib_f:.6f}, slope = {sl_fib_f:.6f}")

    print(f"\n  {'lev':>3s}  {'p/q':>8s}  {'q':>5s}  "
          f"{'log g*':>10s}  {'log|ψ|²_T':>11s}  {'log|ψ|²_F':>11s}  "
          f"{'|ψ|²_F/g*':>10s}")
    print("  " + "-" * 68)

    for (lev, node), idx in zip(backbone, fib_idxs):
        lg = math.log(g_prob[idx]) if g_prob[idx] > 0 else float('-inf')
        lt = math.log(psi_tree[idx]) if psi_tree[idx] > 0 else float('-inf')
        lf = math.log(psi_farey[idx]) if psi_farey[idx] > 0 else float('-inf')
        ratio = psi_farey[idx] / g_prob[idx] if g_prob[idx] > 0 else 0
        print(f"  {lev:3d}  {str(node.value):>8s}  {node.q:5d}  "
              f"{lg:10.4f}  {lt:11.4f}  {lf:11.4f}  {ratio:10.6f}")

    # ══════════════════════════════════════════════════════════════════════
    # FULL NODE SET — top 20
    # ══════════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  FULL NODE SET (top 20 by g*)")
    print(f"{'═' * 72}")

    order = np.argsort(g_prob)[::-1]
    print(f"\n  {'#':>3s}  {'p/q':>7s}  {'q':>4s}  {'d':>2s}  "
          f"{'g*':>11s}  {'|ψ|²_T':>11s}  {'|ψ|²_F':>11s}  "
          f"{'F/g*':>8s}")
    print("  " + "-" * 64)

    for rank in range(min(20, N)):
        i = order[rank]
        n = nodes[i]
        ratio = psi_farey[i] / g_prob[i] if g_prob[i] > 0 else 0
        print(f"  {rank+1:3d}  {str(n.value):>7s}  {n.q:4d}  {n.depth:2d}  "
              f"{g_prob[i]:11.4e}  {psi_tree[i]:11.4e}  "
              f"{psi_farey[i]:11.4e}  {ratio:8.4f}")

    # ══════════════════════════════════════════════════════════════════════
    # SPECTRAL DECOMPOSITION — which eigenstates correlate with g*?
    # ══════════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  SPECTRAL DECOMPOSITION OF H_FAREY")
    print(f"{'═' * 72}")

    H_farey = build_hamiltonian(A_farey, w_vec)
    eigenvalues, eigenvectors = np.linalg.eigh(H_farey)

    print(f"\n  Top 15 eigenstates:")
    print(f"  {'k':>3s}  {'E_k':>10s}  {'E_k/E₀':>8s}  "
          f"{'corr(log)':>12s}  {'slope':>8s}  {'role':>15s}")
    print("  " + "-" * 62)

    for k in range(N - 1, max(N - 16, -1), -1):
        ev = eigenvectors[:, k]
        ev_prob = ev ** 2
        r_ev, sl_ev, _ = log_correlation(ev_prob, g_prob)
        ratio = eigenvalues[k] / eigenvalues[-1] if eigenvalues[-1] != 0 else 0
        rank = N - 1 - k
        role = ""
        if rank == 0:
            role = "GROUND STATE"
        print(f"  {rank:3d}  {eigenvalues[k]:10.6f}  {ratio:8.4f}  "
              f"{r_ev:12.6f}  {sl_ev:8.4f}  {role:>15s}")

    # ══════════════════════════════════════════════════════════════════════
    # DEPTH CONVERGENCE — does corr → 1 and slope → 1?
    # ══════════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  DEPTH CONVERGENCE")
    print(f"{'═' * 72}")

    print(f"\n  {'d':>3s}  {'N':>5s}  {'edges_T':>7s}  {'edges_F':>7s}  "
          f"{'corr_T':>10s}  {'slope_T':>8s}  {'corr_F':>10s}  {'slope_F':>8s}")
    print("  " + "-" * 68)

    for d in range(3, 10):
        tree_d = ConstraintTree(d)
        nodes_d = tree_d.all_nodes
        N_d = len(tree_d)

        U_d = Operator(tree_d, K0=K)
        g_d, _ = U_d.find_fixed_point()
        g_d_vec = np.array([g_d[n.value] for n in nodes_d])
        g_d_prob = g_d_vec / g_d_vec.sum()

        w_d = np.array([tongue_width(n.p, n.q, K) for n in nodes_d])

        A_t, _, _ = build_tree_adjacency(tree_d)
        A_f = build_farey_adjacency(tree_d)
        e_t = int(A_t.sum() / 2)
        e_f = int(A_f.sum() / 2)

        H_t = build_hamiltonian(A_t, w_d)
        H_f = build_hamiltonian(A_f, w_d)

        _, _, psi_t_sq = ground_state(H_t)
        _, _, psi_f_sq = ground_state(H_f)

        r_t, s_t, _ = log_correlation(psi_t_sq, g_d_prob)
        r_f, s_f, _ = log_correlation(psi_f_sq, g_d_prob)

        print(f"  {d:3d}  {N_d:5d}  {e_t:7d}  {e_f:7d}  "
              f"{r_t:10.6f}  {s_t:8.4f}  {r_f:10.6f}  {s_f:8.4f}")

    # ══════════════════════════════════════════════════════════════════════
    # RESIDUAL CONVERGENCE
    # ══════════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  RESIDUAL: std(log|ψ₀|²/g*) vs DEPTH")
    print(f"{'═' * 72}")

    print(f"\n  {'d':>3s}  {'N':>5s}  "
          f"{'std_T':>10s}  {'std_F':>10s}  {'max_T':>10s}  {'max_F':>10s}")
    print("  " + "-" * 52)

    for d in range(3, 10):
        tree_d = ConstraintTree(d)
        nodes_d = tree_d.all_nodes
        N_d = len(tree_d)

        U_d = Operator(tree_d, K0=K)
        g_d, _ = U_d.find_fixed_point()
        g_d_vec = np.array([g_d[n.value] for n in nodes_d])
        g_d_prob = g_d_vec / g_d_vec.sum()

        w_d = np.array([tongue_width(n.p, n.q, K) for n in nodes_d])

        A_t, _, _ = build_tree_adjacency(tree_d)
        A_f = build_farey_adjacency(tree_d)

        H_t = build_hamiltonian(A_t, w_d)
        H_f = build_hamiltonian(A_f, w_d)

        _, _, psi_t_sq = ground_state(H_t)
        _, _, psi_f_sq = ground_state(H_f)

        _, std_t, max_t = residual_stats(psi_t_sq, g_d_prob)
        _, std_f, max_f = residual_stats(psi_f_sq, g_d_prob)

        print(f"  {d:3d}  {N_d:5d}  "
              f"{std_t:10.4f}  {std_f:10.4f}  {max_t:10.4f}  {max_f:10.4f}")

    # ══════════════════════════════════════════════════════════════════════
    # WHAT DOES THE FAREY GRAPH GIVE THAT THE TREE DOESN'T?
    # ══════════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  WHY FAREY, NOT TREE")
    print(f"{'═' * 72}")

    # Show long-range connections for key nodes
    print(f"\n  Long-range Farey connections (not in tree):")
    key_nodes = [Fraction(1, 2), Fraction(1, 3), Fraction(2, 5),
                 Fraction(3, 8), Fraction(5, 13)]

    for frac in key_nodes:
        if frac not in index:
            continue
        i = index[frac]
        tree_neighbors = set()
        farey_neighbors = set()

        for j in range(N):
            if A_tree[i, j] > 0:
                tree_neighbors.add(nodes[j].value)
            if A_farey[i, j] > 0:
                farey_neighbors.add(nodes[j].value)

        extra = farey_neighbors - tree_neighbors
        if extra:
            extra_str = ", ".join(str(f) for f in sorted(extra)[:8])
            if len(extra) > 8:
                extra_str += f" ... ({len(extra)} total)"
            print(f"    {str(frac):>5s}: tree={len(tree_neighbors)}, "
                  f"farey={len(farey_neighbors)}, "
                  f"long-range: {extra_str}")

    # ══════════════════════════════════════════════════════════════════════
    # SUMMARY
    # ══════════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  SUMMARY")
    print(f"{'═' * 72}")

    _, _, _, r_tree, s_tree = results["TREE"]
    _, _, _, r_farey, s_farey = results["FAREY"]

    print(f"""
  Discrete Hilbert space over Q (depth {DEPTH}, N = {N}).

  Hamiltonian:  H[i,j] = A[i,j] × √(w_i × w_j)
  Normalization: Σ|ψ₀|² = 1,  Σg* = 1

                            corr(log|ψ₀|², log g*)    slope
                            ──────────────────────    ──────
  TREE adjacency:           {r_tree:10.6f}            {s_tree:8.4f}
  FAREY adjacency:          {r_farey:10.6f}            {s_farey:8.4f}

  Tree edges: {n_tree_edges}.  Farey edges: {n_farey_edges}.
  The {n_farey_edges - n_tree_edges} extra edges are long-range
  Farey neighbor connections (|ad-bc|=1 but not parent-child).

  The tree adjacency creates exponential localization:
    amplitude tunnels through d edges, each weaker → e^{{-O(d²)}}
    but g* decays as e^{{-O(d)}}

  The Farey adjacency adds direct connections from shallow
  to deep nodes, bypassing intermediate edges.

  Fixed-point convergence (classical) and spectral
  decomposition (quantum) operate on the same structure:
    Classical:  F(|r|) = |r|  →  bisect  →  g*
    Quantum:    H|ψ₀⟩ = E₀|ψ₀⟩  →  diag  →  |ψ₀|²
""")
