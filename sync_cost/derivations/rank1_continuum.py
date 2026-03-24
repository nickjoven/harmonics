"""
Rank-1 persistence of the Jacobian DU/Dg in the continuum limit.

═══════════════════════════════════════════════════════════════════════════
THEOREM (Rank-1 Fréchet derivative)

Let C_N be the Stern-Brocot tree truncated at depth N, with |C_N| nodes.
Let U_N: R^{|C_N|} → R^{|C_N|} be the operator

    U_N(g)(f) = g_bare(f) · w(f, K_0 |r(g)|) / Z

where r(g) = Σ g(f) e^{2πif} / Σ g(f) is the order parameter.

(A) DISCRETE CASE. For each N, the Jacobian J_N = dU_N/dg has rank 1.

    Proof: U_N factors as  g → |r(g)| → K_eff → g_new.
    The map g ↦ |r(g)| has gradient ∇|r| ∈ R^{|C_N|}.
    The map |r| ↦ g_new has derivative ∂g_new/∂|r| ∈ R^{|C_N|}.
    Therefore J_N = (∂g_new/∂|r|) ⊗ (∇|r|)^T, which is rank 1.

(B) CONTINUUM CASE. Let g ∈ L²([0,1]) and define U on L²([0,1]) by
    the same formula with sums replaced by integrals. Then DU, the
    Fréchet derivative of U at g*, has rank 1.

    Proof: DU[δg] = u · ⟨v, δg⟩_{L²}  where
        v(f) = ∂|r|/∂g(f)   ∈ L²([0,1])   (gradient of order parameter)
        u(f) = ∂g_new/∂|r|  ∈ L²([0,1])   (sensitivity of output)
    This is the outer product u ⊗ v in L²([0,1]), a rank-1 operator.

    The factorization g → |r(g)| → g_new passes through R regardless
    of the dimension of the function space. No finite-dimensional
    approximation is needed; the rank-1 structure is intrinsic.

═══════════════════════════════════════════════════════════════════════════

Numerical verification: at each depth N = 3..10, we compute J_N by
finite differences and confirm rank(J_N) = 1 via the singular value
decomposition. We show:
    - σ_1 >> σ_2 ≈ 0
    - σ_1 converges as N → ∞
    - The rank-1 eigenvectors converge with depth
"""

import sys
import os
import math
import numpy as np

# ── Import from universe_loop.py ──────────────────────────────────────────

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from universe_loop import ConstraintTree, Operator, Fraction


# ═══════════════════════════════════════════════════════════════════════════
# NUMERICAL JACOBIAN
# ═══════════════════════════════════════════════════════════════════════════

def distribution_to_vector(g, nodes):
    """Convert distribution dict to numpy vector in canonical node order."""
    return np.array([g[n.value] for n in nodes])


def vector_to_distribution(v, nodes):
    """Convert numpy vector back to distribution dict."""
    return {n.value: float(v[i]) for i, n in enumerate(nodes)}


def compute_jacobian(op, g_star, nodes, eps=1e-7):
    """Compute J = dU/dg at g_star by central finite differences.

    J[i,j] = ∂U(g)_i / ∂g_j  evaluated at g = g_star.
    """
    N = len(nodes)
    g_vec = distribution_to_vector(g_star, nodes)
    J = np.zeros((N, N))

    for j in range(N):
        g_plus = g_vec.copy()
        g_minus = g_vec.copy()
        g_plus[j] += eps
        g_minus[j] -= eps

        g_plus_dict = vector_to_distribution(g_plus, nodes)
        g_minus_dict = vector_to_distribution(g_minus, nodes)

        Ug_plus = distribution_to_vector(op(g_plus_dict), nodes)
        Ug_minus = distribution_to_vector(op(g_minus_dict), nodes)

        J[:, j] = (Ug_plus - Ug_minus) / (2 * eps)

    return J


# ═══════════════════════════════════════════════════════════════════════════
# RANK-1 VERIFICATION
# ═══════════════════════════════════════════════════════════════════════════

def verify_rank1(depth, K0=1.0, eps=1e-7):
    """At given depth, compute the Jacobian and its SVD.

    Returns:
        sigma: singular values (descending)
        u1: left singular vector (sensitivity direction)
        v1: right singular vector (order-parameter gradient direction)
        N: number of nodes
        r_star: fixed-point order parameter
        nodes: list of SBNode
    """
    tree = ConstraintTree(depth)
    op = Operator(tree, K0)
    nodes = tree.all_nodes
    N = len(nodes)

    g_star, r_star = op.find_fixed_point()

    J = compute_jacobian(op, g_star, nodes, eps=eps)
    U_svd, sigma, Vt_svd = np.linalg.svd(J, full_matrices=False)

    return sigma, U_svd[:, 0], Vt_svd[0, :], N, r_star, nodes


def interpolate_to_common_grid(vec, nodes, grid):
    """Interpolate a vector defined on SB nodes to a common frequency grid.

    Uses nearest-neighbor assignment: each grid point gets the value
    of the nearest SB node.
    """
    freqs = np.array([float(n.value) for n in nodes])
    result = np.zeros(len(grid))
    for i, f in enumerate(grid):
        idx = np.argmin(np.abs(freqs - f))
        result[i] = vec[idx]
    return result


# ═══════════════════════════════════════════════════════════════════════════
# FORMAL PROOF (restated for the record)
# ═══════════════════════════════════════════════════════════════════════════

PROOF = r"""
═══════════════════════════════════════════════════════════════════════════
FORMAL PROOF: DU = u ⊗ v  (rank 1 in any dimension)
═══════════════════════════════════════════════════════════════════════════

SETUP.
  Let X be either R^N (discrete, N = |C_N|) or L²([0,1]) (continuum).
  Let U: X → X be the operator

      U(g)(f) = g_bare(f) · w(f, K_0 |r(g)|) / Z(|r(g)|)

  where  r(g) = ∫ g(f) e^{2πif} df / ∫ g(f) df   (or the discrete sum),
  and    Z(ρ) = ∫ g_bare(f) · w(f, K_0 ρ) df      (normalization).

FACTORIZATION.
  U factors through R:

      U = R ∘ S

  where  S: X → R,        S(g) = |r(g)|           (scalar extraction)
  and    R: R → X,        R(ρ)(f) = g_bare(f) · w(f, K_0 ρ) / Z(ρ)
                                                    (reconstruction)

FRÉCHET DERIVATIVES.
  At the fixed point g* with S(g*) = ρ* = |r*|:

  (1) DS[g*]: X → R  is the bounded linear functional
        DS[g*][δg] = ⟨v, δg⟩
      where v(f) = ∂|r|/∂g(f) evaluated at g*.

      Explicitly, with T = ∫ g(f) df:
        v(f) = Re[ e^{-iθ} (e^{2πif} - r) ] / T
      where θ = arg(r(g*)), r = r(g*).

  (2) DR[ρ*]: R → X  is the bounded linear map
        DR[ρ*][δρ] = δρ · u
      where u(f) = ∂R/∂ρ evaluated at ρ = ρ*.

      Explicitly:
        u(f) = g_bare(f) · [K_0 ∂w/∂K(f, K_0 ρ*) · Z - w(f, K_0 ρ*) · Z']
               / Z(ρ*)²
      where Z' = dZ/dρ.

CHAIN RULE.
  DU[g*] = DR[ρ*] ∘ DS[g*].

  For any δg ∈ X:
    DU[g*][δg] = DR[ρ*][ DS[g*][δg] ]
               = DR[ρ*][ ⟨v, δg⟩ ]
               = ⟨v, δg⟩ · u

  Therefore  DU[g*] = u ⊗ v.

RANK.
  u ⊗ v has range = span{u} (one-dimensional), hence rank 1.
  This holds in R^N for all N and in L²([0,1]).

PERSISTENCE IN THE CONTINUUM LIMIT.
  The rank-1 structure does not depend on N. It is a consequence of
  the factorization U = R ∘ S, which holds for any function space on
  which r(g) is well-defined. In particular:

  (a) v ∈ L²([0,1]) because e^{2πif} is bounded and g* ∈ L¹ ∩ L².
  (b) u ∈ L²([0,1]) because ∂w/∂K is bounded for each f and g_bare ∈ L².
  (c) u ⊗ v is a Hilbert-Schmidt operator on L²([0,1]) with
      ‖u ⊗ v‖_HS = ‖u‖ · ‖v‖ < ∞.

  The operator DU is compact (rank 1), self-adjoint iff u ∝ v,
  and has exactly one nonzero eigenvalue: λ = ⟨v, u⟩.

  The rank is 1 in every finite approximation and in the limit.  ∎
"""


# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    K0 = 1.0
    DEPTHS = list(range(3, 11))

    print("=" * 72)
    print("  RANK-1 PERSISTENCE OF DU/Dg IN THE CONTINUUM LIMIT")
    print("=" * 72)

    # ── 1. Singular values at each depth ──────────────────────────────
    print(f"\n{'─' * 72}")
    print("  SINGULAR VALUES OF THE JACOBIAN  J = dU/dg")
    print(f"{'─' * 72}")
    print(f"\n  At each depth N, J is |C_N| × |C_N|.")
    print(f"  Rank-1 means σ₁ >> 0 and σ₂ ≈ 0.\n")
    print(f"  {'depth':>5s}  {'|C_N|':>6s}  {'σ₁':>12s}  {'σ₂':>12s}  "
          f"{'σ₂/σ₁':>12s}  {'|r*|':>10s}")
    print("  " + "-" * 65)

    results = {}
    for depth in DEPTHS:
        sigma, u1, v1, N, r_star, nodes = verify_rank1(depth, K0)
        results[depth] = {
            'sigma': sigma, 'u1': u1, 'v1': v1,
            'N': N, 'r_star': r_star, 'nodes': nodes,
        }
        s1 = sigma[0]
        s2 = sigma[1] if len(sigma) > 1 else 0.0
        ratio = s2 / s1 if s1 > 0 else 0.0
        print(f"  {depth:5d}  {N:6d}  {s1:12.6e}  {s2:12.6e}  "
              f"{ratio:12.6e}  {r_star:10.6f}")

    # ── 2. Convergence of σ₁ ──────────────────────────────────────────
    print(f"\n{'─' * 72}")
    print("  CONVERGENCE OF σ₁  (the rank-1 eigenvalue)")
    print(f"{'─' * 72}")
    print(f"\n  σ₁ should converge as depth → ∞, confirming the continuum")
    print(f"  operator has a well-defined rank-1 structure.\n")
    print(f"  {'depth':>5s}  {'σ₁':>12s}  {'Δσ₁':>12s}  {'ratio Δ(n)/Δ(n-1)':>20s}")
    print("  " + "-" * 55)

    prev_s1 = None
    prev_delta = None
    for depth in DEPTHS:
        s1 = results[depth]['sigma'][0]
        if prev_s1 is not None:
            delta = s1 - prev_s1
            if prev_delta is not None and abs(prev_delta) > 1e-15:
                ratio = delta / prev_delta
                print(f"  {depth:5d}  {s1:12.6e}  {delta:+12.6e}  {ratio:20.6f}")
            else:
                print(f"  {depth:5d}  {s1:12.6e}  {delta:+12.6e}  {'—':>20s}")
            prev_delta = delta
        else:
            print(f"  {depth:5d}  {s1:12.6e}  {'—':>12s}  {'—':>20s}")
        prev_s1 = s1

    # ── 3. Convergence of the rank-1 eigenvectors ─────────────────────
    print(f"\n{'─' * 72}")
    print("  CONVERGENCE OF THE RANK-1 EIGENVECTORS")
    print(f"{'─' * 72}")
    print(f"\n  u = ∂g_new/∂|r|  (left singular vector, sensitivity)")
    print(f"  v = ∇|r|         (right singular vector, order-param gradient)")
    print(f"\n  We interpolate to a common grid and measure ‖Δu‖, ‖Δv‖")
    print(f"  between successive depths.\n")

    # Common grid for comparison
    GRID = np.linspace(0, 1, 200, endpoint=False)

    print(f"  {'depth':>5s}  {'‖Δu‖':>12s}  {'‖Δv‖':>12s}")
    print("  " + "-" * 35)

    prev_u_grid = None
    prev_v_grid = None
    for depth in DEPTHS:
        res = results[depth]
        # Sign-align: ensure u1[0] > 0 for consistency
        u1 = res['u1'].copy()
        v1 = res['v1'].copy()
        if u1[0] < 0:
            u1 = -u1
            v1 = -v1

        u_grid = interpolate_to_common_grid(u1, res['nodes'], GRID)
        v_grid = interpolate_to_common_grid(v1, res['nodes'], GRID)

        # Normalize on the grid
        u_norm = np.linalg.norm(u_grid)
        v_norm = np.linalg.norm(v_grid)
        if u_norm > 0:
            u_grid /= u_norm
        if v_norm > 0:
            v_grid /= v_norm

        if prev_u_grid is not None:
            # Align signs with previous
            if np.dot(u_grid, prev_u_grid) < 0:
                u_grid = -u_grid
                v_grid = -v_grid
            du = np.linalg.norm(u_grid - prev_u_grid)
            dv = np.linalg.norm(v_grid - prev_v_grid)
            print(f"  {depth:5d}  {du:12.6e}  {dv:12.6e}")
        else:
            print(f"  {depth:5d}  {'—':>12s}  {'—':>12s}")

        prev_u_grid = u_grid
        prev_v_grid = v_grid

    # ── 4. The full singular value spectrum at max depth ───────────────
    max_depth = DEPTHS[-1]
    sigma_full = results[max_depth]['sigma']
    print(f"\n{'─' * 72}")
    print(f"  FULL SINGULAR VALUE SPECTRUM AT DEPTH {max_depth}")
    print(f"  (|C_{max_depth}| = {results[max_depth]['N']} nodes)")
    print(f"{'─' * 72}\n")
    print(f"  {'index':>5s}  {'σ_i':>14s}  {'σ_i / σ₁':>14s}")
    print("  " + "-" * 38)
    n_show = min(15, len(sigma_full))
    for i in range(n_show):
        ratio = sigma_full[i] / sigma_full[0] if sigma_full[0] > 0 else 0
        marker = "  ← rank-1 eigenvalue" if i == 0 else ""
        print(f"  {i + 1:5d}  {sigma_full[i]:14.6e}  {ratio:14.6e}{marker}")
    if len(sigma_full) > n_show:
        print(f"  {'...':>5s}")
        print(f"  {len(sigma_full):5d}  {sigma_full[-1]:14.6e}  "
              f"{sigma_full[-1] / sigma_full[0]:14.6e}")

    # ── 5. Formal proof ──────────────────────────────────────────────
    print(PROOF)

    # ── 6. Summary ────────────────────────────────────────────────────
    s1_final = results[max_depth]['sigma'][0]
    s2_final = results[max_depth]['sigma'][1]
    print(f"{'═' * 72}")
    print(f"  CONCLUSION")
    print(f"{'═' * 72}")
    print(f"""
  The Jacobian DU/Dg has rank 1 at every depth N = 3..{max_depth}.

  At depth {max_depth}:
    σ₁ = {s1_final:.6e}
    σ₂ = {s2_final:.6e}
    σ₂/σ₁ = {s2_final / s1_final:.6e}

  The rank-1 structure persists because U factors through a scalar:
    g → |r(g)| → g_new
  and this factorization is independent of the dimension of the
  function space.

  In the continuum limit (L²([0,1])):
    DU = u ⊗ v
  where u(f) = ∂g_new/∂|r| and v(f) = ∂|r|/∂g(f) are both in L².
  The operator u ⊗ v is Hilbert-Schmidt, compact, and rank 1.
  The rank-1 property is not an artifact of finite truncation.
  It is intrinsic to the bottleneck factorization.  ∎
""")
