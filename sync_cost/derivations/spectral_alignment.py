"""
Spectral alignment: do the dominant eigenmodes of H carry g*?

Not spatial (|ψ₀(p/q)|² vs g*(p/q) node by node — that gives
slope 0.14, not 1.0; see quantum_walk.py). Spectral: expand g*
in the eigenbasis of H and ask where the weight concentrates.

  g* = Σ_k c_k |E_k⟩     where c_k = ⟨E_k | g*⟩
  √g* = Σ_k a_k |E_k⟩    where a_k = ⟨E_k | √g*⟩

Key results:
  √g* concentrates 75.5% in the top eigenmode of H.
  g* does not (13.4%) — the square diffuses spectral weight.
  The Born rule IS this asymmetry: amplitude is spectrally
  concentrated, probability is not.

  Odd eigenmodes carry exactly zero weight (left-right symmetry).
  Jacobian dU/dg|_{g*} is exactly rank 1 (σ₁=24.5, σ₂=5.5e-7).

Usage:
    python sync_cost/derivations/spectral_alignment.py
"""

import math
import sys
from fractions import Fraction

import numpy as np

sys.path.insert(0, "sync_cost/derivations")
from universe_loop import (
    ConstraintTree, Operator, tongue_width,
    fibonacci_backbone, PHI,
)


def build_hamiltonian(tree, K):
    """H[i,j] = A[i,j] × √(w_i × w_j)."""
    nodes = tree.all_nodes
    N = len(nodes)
    index = {n.value: i for i, n in enumerate(nodes)}
    w = np.array([tongue_width(n.p, n.q, K) for n in nodes])
    sqrt_w = np.sqrt(w)

    H = np.zeros((N, N))
    for node in nodes:
        i = index[node.value]
        for parent in (node.left_parent, node.right_parent):
            if parent is not None and parent.value in index:
                j = index[parent.value]
                H[i, j] = sqrt_w[i] * sqrt_w[j]
                H[j, i] = H[i, j]
    return H, nodes, index, w


def linearized_U(tree, g_star, r_star, K0, eps=1e-6):
    """Jacobian of U at g* via finite differences.

    dU_i/dg_j ≈ (U(g* + eps*e_j) - U(g* - eps*e_j))_i / (2*eps)

    U factors through 1D bottleneck so this should be ~rank 1.
    """
    nodes = tree.all_nodes
    N = len(nodes)
    op = Operator(tree, K0=K0)

    J = np.zeros((N, N))
    keys = [n.value for n in nodes]

    for j in range(N):
        g_plus = dict(g_star)
        g_minus = dict(g_star)
        g_plus[keys[j]] += eps
        g_minus[keys[j]] -= eps

        U_plus = op(g_plus)
        U_minus = op(g_minus)

        for i in range(N):
            J[i, j] = (U_plus[keys[i]] - U_minus[keys[i]]) / (2 * eps)

    return J


if __name__ == "__main__":
    print("=" * 72)
    print("  SPECTRAL ALIGNMENT")
    print("  g* expanded in the eigenbasis of H")
    print("=" * 72)

    DEPTH = 8
    K = 1.0
    tree = ConstraintTree(DEPTH)
    nodes = tree.all_nodes
    N = len(tree)

    # Classical fixed point
    op = Operator(tree, K0=K)
    g_star, r_star = op.find_fixed_point()
    g_vec = np.array([g_star[n.value] for n in nodes])
    g_prob = g_vec / g_vec.sum()
    sqrt_g = np.sqrt(g_prob)
    sqrt_g /= np.linalg.norm(sqrt_g)  # unit vector

    # Hamiltonian
    H, _, index, w_vec = build_hamiltonian(tree, K)
    eigenvalues, eigenvectors = np.linalg.eigh(H)
    # eigh returns ascending; reverse for descending
    eigenvalues = eigenvalues[::-1]
    eigenvectors = eigenvectors[:, ::-1]

    print(f"\n  N = {N}, depth = {DEPTH}")
    print(f"  |r*| = {r_star:.8f}")

    # ══════════════════════════════════════════════════════════════════
    # SPECTRAL EXPANSION OF g*
    # ══════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  EXPAND g* AND √g* IN EIGENBASIS OF H")
    print(f"{'═' * 72}")

    # Project g* (as prob vector) onto eigenbasis
    c_g = eigenvectors.T @ g_prob        # coefficients for g*
    a_g = eigenvectors.T @ sqrt_g        # coefficients for √g*

    # Spectral weights
    weight_g = c_g ** 2
    weight_sqrt = a_g ** 2

    # Cumulative weight
    cum_g = np.cumsum(weight_g) / weight_g.sum()
    cum_sqrt = np.cumsum(weight_sqrt) / weight_sqrt.sum()

    print(f"\n  {'k':>4s}  {'E_k':>10s}  {'E_k/E₀':>8s}  "
          f"{'|c_k|²(g*)':>12s}  {'cum(g*)':>10s}  "
          f"{'|a_k|²(√g*)':>12s}  {'cum(√g*)':>10s}")
    print("  " + "-" * 80)

    for k in range(min(30, N)):
        print(f"  {k:4d}  {eigenvalues[k]:10.6f}  "
              f"{eigenvalues[k]/eigenvalues[0]:8.4f}  "
              f"{weight_g[k]:12.6e}  {cum_g[k]:10.6f}  "
              f"{weight_sqrt[k]:12.6e}  {cum_sqrt[k]:10.6f}")

    # How many modes to capture 90%, 95%, 99%?
    print(f"\n  Modes needed to capture g*:")
    for thresh in [0.50, 0.80, 0.90, 0.95, 0.99]:
        n_g = int(np.searchsorted(cum_g, thresh)) + 1
        n_s = int(np.searchsorted(cum_sqrt, thresh)) + 1
        print(f"    {thresh*100:5.1f}%:  g* needs {n_g:4d}/{N} modes, "
              f"√g* needs {n_s:4d}/{N} modes")

    # ══════════════════════════════════════════════════════════════════
    # SPECTRAL CONCENTRATION: weight vs eigenvalue rank
    # ══════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  SPECTRAL CONCENTRATION")
    print(f"{'═' * 72}")

    # Is the weight monotonically decreasing with eigenvalue rank?
    # Measure: correlation between eigenvalue rank and weight rank
    from scipy.stats import spearmanr
    rho_g, p_g = spearmanr(np.arange(N), -weight_g)
    rho_s, p_s = spearmanr(np.arange(N), -weight_sqrt)

    print(f"\n  Do top eigenvalues carry top weight?")
    print(f"    Spearman ρ(eigenvalue rank, weight rank):")
    print(f"      g*:  ρ = {rho_g:.6f}")
    print(f"      √g*: ρ = {rho_s:.6f}")
    print(f"    (ρ = 1 means perfect spectral alignment)")

    # ══════════════════════════════════════════════════════════════════
    # TOP-k RECONSTRUCTION
    # ══════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  TOP-k RECONSTRUCTION OF g*")
    print(f"{'═' * 72}")

    print(f"\n  Reconstruct g* using only the top k eigenmodes.")
    print(f"  {'k':>4s}  {'||g*_k - g*||':>14s}  {'rel error':>12s}  "
          f"{'corr(log)':>12s}")
    print("  " + "-" * 48)

    for k in [1, 2, 3, 5, 10, 20, 50, 100, N]:
        k = min(k, N)
        g_reconstructed = eigenvectors[:, :k] @ c_g[:k]
        err = np.linalg.norm(g_reconstructed - g_prob)
        rel_err = err / np.linalg.norm(g_prob)

        # log-space correlation of reconstruction vs original
        mask = (g_reconstructed > 0) & (g_prob > 0)
        if mask.sum() > 2:
            lx = np.log(g_reconstructed[mask])
            ly = np.log(g_prob[mask])
            mx, my = lx.mean(), ly.mean()
            dx, dy = lx - mx, ly - my
            vx, vy = np.dot(dx, dx), np.dot(dy, dy)
            corr = np.dot(dx, dy) / math.sqrt(vx * vy) if vx > 0 and vy > 0 else 0
        else:
            corr = 0

        print(f"  {k:4d}  {err:14.6e}  {rel_err:12.6e}  {corr:12.6f}")

    # ══════════════════════════════════════════════════════════════════
    # COMPARE SPECTRUM OF H TO SPECTRUM OF dU/dg|_{g*}
    # ══════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  SPECTRUM OF H vs SPECTRUM OF dU/dg|_{g*}")
    print(f"{'═' * 72}")

    print(f"\n  Computing Jacobian of U at g* (finite differences)...")
    J = linearized_U(tree, g_star, r_star, K)
    J_eigenvalues = np.sort(np.real(np.linalg.eigvals(J)))[::-1]

    print(f"\n  Top eigenvalues:")
    print(f"  {'k':>4s}  {'E_k(H)':>12s}  {'λ_k(dU)':>12s}  {'|λ_k|':>10s}")
    print("  " + "-" * 42)

    for k in range(min(15, N)):
        lam = J_eigenvalues[k]
        print(f"  {k:4d}  {eigenvalues[k]:12.6f}  "
              f"{lam:12.6f}  {abs(lam):10.6f}")

    # What's the effective rank of J?
    J_sv = np.linalg.svd(J, compute_uv=False)
    rank_90 = int(np.searchsorted(np.cumsum(J_sv**2) / np.sum(J_sv**2), 0.90)) + 1
    rank_99 = int(np.searchsorted(np.cumsum(J_sv**2) / np.sum(J_sv**2), 0.99)) + 1

    print(f"\n  Effective rank of Jacobian dU/dg|_{{g*}}:")
    print(f"    90% of variance: {rank_90} singular values")
    print(f"    99% of variance: {rank_99} singular values")
    print(f"    Top 5 singular values: {J_sv[:5]}")
    print(f"\n  (Rank ~1 confirms the 1D bottleneck.)")

    # ══════════════════════════════════════════════════════════════════
    # THE ψ-MODE IN THE EIGENBASIS
    # ══════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  THE ψ-MODE IN THE EIGENBASIS")
    print(f"{'═' * 72}")

    # The Cassini residual along the Fibonacci backbone
    backbone = fibonacci_backbone(tree)
    fib_idxs = [index[node.value] for _, node in backbone]
    n_fib = len(fib_idxs)

    # Build the ψ-mode vector: (-1)^depth × φ^{-2×depth} at Fibonacci nodes
    psi_mode = np.zeros(N)
    for lev, node in backbone:
        i = index[node.value]
        psi_mode[i] = ((-1) ** lev) * PHI ** (-2 * lev)

    psi_mode /= np.linalg.norm(psi_mode)

    # Project onto eigenbasis
    c_psi = eigenvectors.T @ psi_mode
    weight_psi = c_psi ** 2
    cum_psi = np.cumsum(weight_psi) / weight_psi.sum()

    print(f"\n  ψ-mode = (-1)^n φ^{{-2n}} on Fibonacci backbone")
    print(f"  Projected onto eigenbasis of H:")
    print(f"\n  {'k':>4s}  {'E_k':>10s}  {'|c_k|²(ψ)':>12s}  {'cum':>8s}")
    print("  " + "-" * 38)

    for k in range(min(20, N)):
        if weight_psi[k] > 1e-10:
            print(f"  {k:4d}  {eigenvalues[k]:10.6f}  "
                  f"{weight_psi[k]:12.6e}  {cum_psi[k]:8.4f}")

    # ══════════════════════════════════════════════════════════════════
    # DEPTH CONVERGENCE
    # ══════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  DEPTH CONVERGENCE OF SPECTRAL ALIGNMENT")
    print(f"{'═' * 72}")

    print(f"\n  {'d':>3s}  {'N':>5s}  "
          f"{'modes→90%':>10s}  {'modes→99%':>10s}  "
          f"{'top1 wt(g*)':>12s}  {'top1 wt(√g*)':>13s}  "
          f"{'J rank90':>9s}")
    print("  " + "-" * 68)

    for d in range(3, 10):
        td = ConstraintTree(d)
        nd = td.all_nodes
        Nd = len(td)

        ud = Operator(td, K0=K)
        gd, rd = ud.find_fixed_point()
        gd_vec = np.array([gd[n.value] for n in nd])
        gd_prob = gd_vec / gd_vec.sum()
        sqrtgd = np.sqrt(gd_prob)
        sqrtgd /= np.linalg.norm(sqrtgd)

        Hd, _, _, _ = build_hamiltonian(td, K)
        evd, evecd = np.linalg.eigh(Hd)
        evd = evd[::-1]
        evecd = evecd[:, ::-1]

        cd = evecd.T @ gd_prob
        ad = evecd.T @ sqrtgd
        wgd = cd ** 2
        wsd = ad ** 2
        cumgd = np.cumsum(wgd) / wgd.sum()
        cumsd = np.cumsum(wsd) / wsd.sum()

        n90g = int(np.searchsorted(cumgd, 0.90)) + 1
        n99g = int(np.searchsorted(cumgd, 0.99)) + 1

        # Jacobian rank
        Jd = linearized_U(td, gd, rd, K, eps=1e-6)
        svd = np.linalg.svd(Jd, compute_uv=False)
        jr90 = int(np.searchsorted(
            np.cumsum(svd**2) / np.sum(svd**2), 0.90)) + 1

        print(f"  {d:3d}  {Nd:5d}  "
              f"{n90g:10d}  {n99g:10d}  "
              f"{wgd[0]:12.6e}  {wsd[0]:13.6e}  "
              f"{jr90:9d}")

    # ══════════════════════════════════════════════════════════════════
    # SUMMARY
    # ══════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  SUMMARY")
    print(f"{'═' * 72}")

    n90 = int(np.searchsorted(cum_g, 0.90)) + 1
    n99 = int(np.searchsorted(cum_g, 0.99)) + 1

    print(f"""
  Spectral alignment of g* with H (depth {DEPTH}, N = {N}):

  g* expanded in eigenbasis of H:
    Top eigenmode carries {weight_g[0]*100:.2f}% of g*
    {n90} modes capture 90%, {n99} modes capture 99%

  √g* expanded in eigenbasis of H:
    Top eigenmode carries {weight_sqrt[0]*100:.2f}% of √g*

  Spectral concentration:
    ρ(eigenvalue rank, g* weight rank) = {rho_g:.4f}
    ρ(eigenvalue rank, √g* weight rank) = {rho_s:.4f}

  Jacobian dU/dg|_{{g*}}:
    Effective rank: {rank_90} (90%), {rank_99} (99%)
    Confirms: U factors through 1D bottleneck

  The question: do the DOMINANT eigenmodes of H
  carry the DOMINANT weight of g*?
""")
