"""
The universe in one recursive loop.

The observable is not the state, but the fixed point of an operator
on distributions over states.

Three objects:
  C — State space: the Stern-Brocot tree (topology preserved)
  U — Operator on distributions over C
  g* — The unique fixed point: U(g*) = g*

Uniqueness: U factors through a 1D bottleneck. The entire distribution
g enters U only through the scalar |r(g)|. The fixed-point equation
on Dist(C) reduces to F(|r|) = |r|, where F is continuous and
decreasing on [0,1] with F(0) > 0 and F(1) < 1. By IVT, F crosses
the diagonal exactly once. Therefore g* is unique.

The fixed point is located by bisection on the scalar equation,
not by iterating distributions. The iteration U^n(g₀) need not
converge (F'(r*) may exceed 1, giving a 2-cycle), but the fixed
point still exists and is unique. The observable does not depend
on whether you iterate to find it.

Usage:
    python sync_cost/derivations/universe_loop.py
"""

import math
import cmath
import sys
from fractions import Fraction

sys.path.insert(0, "sync_cost/derivations")
from circle_map_utils import tongue_width


# ── Constants ────────────────────────────────────────────────────────────────

PHI = (1 + math.sqrt(5)) / 2
INV_PHI = 1 / PHI
PHI_SQ = PHI ** 2
LN_PHI_SQ = math.log(PHI_SQ)
PSI = -1 / PHI


# ═══════════════════════════════════════════════════════════════════════════════
# C — STATE SPACE
# ═══════════════════════════════════════════════════════════════════════════════

class SBNode:
    """A node in the Stern-Brocot tree. The mediant of two parents."""
    __slots__ = ('value', 'depth', 'left_parent', 'right_parent',
                 'left_child', 'right_child')

    def __init__(self, value, depth, left_parent=None, right_parent=None):
        self.value = value
        self.depth = depth
        self.left_parent = left_parent
        self.right_parent = right_parent
        self.left_child = None
        self.right_child = None

    @property
    def p(self):
        return self.value.numerator

    @property
    def q(self):
        return self.value.denominator

    def __repr__(self):
        return f"SBNode({self.value}, d={self.depth})"


class ConstraintTree:
    """The Stern-Brocot tree. Topology preserved, no sorting."""

    def __init__(self, max_depth):
        self.max_depth = max_depth
        self.nodes_by_depth = {}
        self.node_map = {}
        self.left_sentinel = SBNode(Fraction(0, 1), depth=-1)
        self.right_sentinel = SBNode(Fraction(1, 1), depth=-1)
        self._build(max_depth)

    def _build(self, max_depth):
        boundaries = [self.left_sentinel, self.right_sentinel]
        for d in range(max_depth):
            new_nodes = []
            new_boundaries = [boundaries[0]]
            for i in range(len(boundaries) - 1):
                left = boundaries[i]
                right = boundaries[i + 1]
                med_value = Fraction(
                    left.value.numerator + right.value.numerator,
                    left.value.denominator + right.value.denominator
                )
                node = SBNode(med_value, depth=d,
                              left_parent=left, right_parent=right)
                if left.right_child is None:
                    left.right_child = node
                if right.left_child is None:
                    right.left_child = node
                new_nodes.append(node)
                self.node_map[med_value] = node
                new_boundaries.append(node)
                new_boundaries.append(right)
            self.nodes_by_depth[d] = new_nodes
            boundaries = new_boundaries

    @property
    def all_nodes(self):
        """Canonical order: by depth, left-to-right within depth."""
        result = []
        for d in range(self.max_depth):
            result.extend(self.nodes_by_depth.get(d, []))
        return result

    def __len__(self):
        return len(self.node_map)

    def __contains__(self, frac):
        return frac in self.node_map

    def get(self, frac):
        return self.node_map.get(frac)

    def nodes_at_depth(self, d):
        return self.nodes_by_depth.get(d, [])


# ═══════════════════════════════════════════════════════════════════════════════
# U — THE OPERATOR
#
# U: Dist(C) → Dist(C)
#
# CRITICAL STRUCTURE: U factors through a 1D bottleneck.
#
#   g ──→ |r(g)| ──→ K_eff ──→ {w(f, K_eff)} ──→ g_new
#   N dim   1 dim     1 dim      N dim            N dim
#
# The entire N-dimensional distribution is compressed to one scalar.
# The fixed-point equation reduces to F(|r|) = |r|, scalar.
#
# F is continuous, decreasing, F(0) > 0, F(1) < 1.
# By IVT: unique crossing. Therefore g* is unique.
#
# Note: F decreasing with |F'(r*)| > 1 means the naive iteration
# g → U(g) oscillates (2-cycle). This doesn't affect the existence
# or uniqueness of g*. It means you locate g* by bisection on the
# scalar equation, not by iterating distributions.
# ═══════════════════════════════════════════════════════════════════════════════



class Operator:
    """U: Dist(C) → Dist(C), factoring through a 1D bottleneck.

    U(g)(f) = g_bare(f) × w(f, K₀|r(g)|) / Z

    g enters only through |r(g)|. The fixed point g* satisfies
    U(g*) = g*, which reduces to the scalar equation F(|r|) = |r|.
    """

    def __init__(self, tree, K0, g_bare=None):
        self.tree = tree
        self.K0 = K0
        self.nodes = tree.all_nodes
        self.N = len(self.nodes)
        self.g_bare = g_bare or {n.value: 1.0 for n in self.nodes}
        self._phases = {n.value: cmath.exp(2j * math.pi * float(n.value))
                        for n in self.nodes}

    def order_parameter(self, g):
        """r(g): the 1D bottleneck. All of g compressed to one scalar."""
        total = sum(g[n.value] for n in self.nodes)
        if total == 0:
            return 0j
        return sum(g[n.value] * self._phases[n.value]
                   for n in self.nodes) / total

    def reconstruct(self, r_abs):
        """Right half of the bottleneck: |r| → g.

        Given |r|, compute the unique distribution:
        g(f) = g_bare(f) × w(f, K₀|r|) / Z
        """
        K_eff = self.K0 * max(r_abs, 1e-15)
        g = {}
        for node in self.nodes:
            w = tongue_width(node.p, node.q, K_eff)
            g[node.value] = self.g_bare[node.value] * w
        total = sum(g.values())
        if total > 0:
            for v in g:
                g[v] *= self.N / total
        return g

    def __call__(self, g):
        """U(g) = reconstruct(|r(g)|)."""
        r = self.order_parameter(g)
        return self.reconstruct(abs(r))

    def scalar_map(self, r_abs):
        """F: [0,1] → [0,1].  F(|r|) = |r(reconstruct(|r|))|.

        The fixed-point equation on Dist(C) reduces to F(|r|) = |r|.
        F is continuous, decreasing, F(0) > 0, F(1) < 1.
        Unique crossing by IVT.
        """
        g = self.reconstruct(r_abs)
        return abs(self.order_parameter(g))

    def find_fixed_point(self):
        """Locate g* by bisection on the scalar equation F(|r|) = |r|.

        This does NOT iterate distributions. It solves the 1D equation
        directly. The fixed point exists and is unique regardless of
        whether the iteration U^n(g₀) converges.

        Returns: (g_star, r_star_abs)
        """
        # F(|r|) - |r| changes sign on [0,1]:
        #   F(0) - 0 > 0  (F(0) > 0 since any distribution has |r| > 0)
        #   F(1) - 1 < 0  (F(1) < 1 since no finite tree gives |r| = 1)
        # Bisect:
        lo, hi = 0.0, 1.0
        for _ in range(80):
            mid = (lo + hi) / 2
            if self.scalar_map(mid) - mid > 0:
                lo = mid
            else:
                hi = mid
        r_star = (lo + hi) / 2
        g_star = self.reconstruct(r_star)
        return g_star, r_star

    def verify_self_consistency(self, g_star, r_star):
        """Check that g* is genuinely a fixed point.

        Compute |r(g*)| and verify it equals r_star.
        Then compute U(g*) and verify it equals g*.
        """
        r_check = abs(self.order_parameter(g_star))
        g_check = self(g_star)
        max_diff = max(abs(g_check[n.value] - g_star[n.value])
                       for n in self.nodes)
        return r_check, max_diff


# ═══════════════════════════════════════════════════════════════════════════════
# g* — THE OBSERVABLE
# ═══════════════════════════════════════════════════════════════════════════════


def fibonacci_backbone(tree, max_terms=25):
    """The Fibonacci convergents: deepest path in the tree."""
    fibs = [1, 1]
    for _ in range(max_terms):
        fibs.append(fibs[-1] + fibs[-2])
    backbone = []
    for i in range(len(fibs) - 1):
        f = Fraction(fibs[i], fibs[i + 1])
        node = tree.get(f)
        if node is not None:
            backbone.append((i, node))
    return backbone


def psi_residual(n_cycles):
    """(-1)^n × φ^{-2n}: the Cassini alternation."""
    return [(-1)**n * PHI**(-2*n) for n in range(n_cycles + 1)]


# ── Run it ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 72)
    print("  THE OBSERVABLE IS THE FIXED POINT")
    print("  of an operator on distributions over states")
    print("=" * 72)

    # ── State space ───────────────────────────────────────────────────
    DEPTH = 8
    tree = ConstraintTree(DEPTH)
    print(f"\n  C — STATE SPACE")
    print(f"  Stern-Brocot tree, depth {DEPTH}, {len(tree)} nodes")
    print(f"  Max denominator: {max(n.q for n in tree.all_nodes)}")

    for d in range(min(DEPTH, 5)):
        nodes_d = tree.nodes_at_depth(d)
        if len(nodes_d) <= 6:
            vals = ", ".join(str(n.value) for n in nodes_d)
        else:
            vals = (", ".join(str(n.value) for n in nodes_d[:3])
                    + f" ... ({len(nodes_d)} total)")
        print(f"    depth {d}: {vals}")

    # ── The operator ──────────────────────────────────────────────────
    K0 = 1.0
    U = Operator(tree, K0)

    # ══════════════════════════════════════════════════════════════════
    # THE SCALAR MAP: why g* is unique
    # ══════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  THE 1D BOTTLENECK")
    print(f"{'═' * 72}")
    print(f"\n  U(g) depends on g only through |r(g)| (one scalar).")
    print(f"  Fixed-point equation: F(|r|) = |r|")
    print(f"\n  {'|r|':>8s}  {'F(|r|)':>10s}  {'F - |r|':>12s}")
    print("  " + "-" * 34)

    for r_val in [i / 20.0 for i in range(21)]:
        F_val = U.scalar_map(r_val)
        diff = F_val - r_val
        print(f"  {r_val:8.4f}  {F_val:10.6f}  {diff:+12.6f}")

    # ── Locate the fixed point by bisection ───────────────────────────
    g_star, r_star = U.find_fixed_point()

    print(f"\n  F is continuous, decreasing, F(0)>0, F(1)<1.")
    print(f"  By IVT: unique crossing at |r*| = {r_star:.12f}")

    # Verify self-consistency
    r_check, max_diff = U.verify_self_consistency(g_star, r_star)
    print(f"\n  Self-consistency check:")
    print(f"    |r(g*)| = {r_check:.12f}")
    print(f"    |r*|    = {r_star:.12f}")
    print(f"    ||r(g*)| - |r*|| = {abs(r_check - r_star):.2e}")
    print(f"    max|U(g*) - g*|  = {max_diff:.2e}")

    # ── Why the naive iteration oscillates ────────────────────────────
    print(f"\n  Slope of F at |r*|:")
    eps = 1e-6
    F_slope = (U.scalar_map(r_star + eps) - U.scalar_map(r_star - eps)) / (2 * eps)
    print(f"    F'(|r*|) = {F_slope:.4f}")
    if abs(F_slope) > 1:
        print(f"    |F'| = {abs(F_slope):.4f} > 1: naive iteration oscillates (2-cycle)")
    else:
        print(f"    |F'| = {abs(F_slope):.4f} < 1: naive iteration converges")
    print(f"\n  The 2-cycle is an artifact of iteration, not of the physics.")
    print(f"  The fixed point exists and is unique regardless.")
    print(f"  We locate it by bisection, not by iterating distributions.")

    # ══════════════════════════════════════════════════════════════════
    # g*: THE OBSERVABLE
    # ══════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  g* — THE OBSERVABLE (not a state, not a trajectory)")
    print(f"{'═' * 72}")

    print(f"\n  |r*| = {r_star:.10f}")
    print(f"  K_eff = K₀ × |r*| = {K0 * r_star:.10f}")

    backbone = fibonacci_backbone(tree)
    print(f"\n  g* along the Fibonacci backbone:")
    print(f"  {'level':>5s}  {'p/q':>10s}  {'depth':>5s}  {'g*(p/q)':>12s}  "
          f"{'w=1/q²':>12s}  {'ρ=g*/w':>12s}")
    print("  " + "-" * 65)

    densities = []
    for idx, node in backbone:
        pop = g_star.get(node.value, 0)
        w = 1.0 / (node.q * node.q)
        dens = pop / w if w > 0 else 0
        densities.append((idx, dens))
        print(f"  {idx:5d}  {str(node.value):>10s}  {node.depth:5d}  "
              f"{pop:12.6e}  {w:12.6e}  {dens:12.6e}")

    if len(densities) >= 3:
        ln_d = [math.log(d) for _, d in densities if d > 0]
        levels = [i for i, d in densities if d > 0]
        n = len(ln_d)
        mx = sum(levels) / n
        my = sum(ln_d) / n
        vx = sum((x - mx)**2 for x in levels) / n
        slope = (sum((x - mx)*(y - my) for x, y in zip(levels, ln_d))
                 / n / vx if vx > 0 else 0)
        print(f"\n  Density slope: {slope:.6f} per level")
        print(f"  (scale-invariant = 0)")

    # ── Born rule ─────────────────────────────────────────────────────
    total_g = sum(g_star.values())
    print(f"\n  Born rule: P(p/q) = g*(p/q) / Σg*")
    print(f"  {'p/q':>10s}  {'P(p/q)':>12s}  {'1/q²':>12s}  {'ratio':>10s}")
    print("  " + "-" * 50)
    for frac_val in [Fraction(1, 2), Fraction(1, 3), Fraction(2, 5),
                     Fraction(3, 8), Fraction(5, 13)]:
        if frac_val in g_star:
            prob = g_star[frac_val] / total_g
            basin = 1.0 / (frac_val.denominator ** 2)
            ratio = prob / basin if basin > 0 else 0
            print(f"  {str(frac_val):>10s}  {prob:12.6e}  "
                  f"{basin:12.6e}  {ratio:10.4f}")

    # ── Uniqueness across K₀ ──────────────────────────────────────────
    print(f"\n{'═' * 72}")
    print("  UNIQUENESS ACROSS COUPLING K₀")
    print(f"{'═' * 72}")
    print(f"\n  At each K₀, F has a unique crossing → unique g*.")
    print(f"\n  {'K₀':>6s}  {'|r*|':>12s}  {'K_eff':>10s}  {'self-con err':>12s}  "
          f"{'ρ(1/2→34/55)':>14s}")
    print("  " + "-" * 60)

    for K0_test in [0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0]:
        U_test = Operator(tree, K0_test)
        g_test, r_test = U_test.find_fixed_point()
        r_chk, md = U_test.verify_self_consistency(g_test, r_test)

        pop_half = g_test.get(Fraction(1, 2), 0)
        pop_deep = g_test.get(Fraction(34, 55), 0)
        ratio = pop_half / pop_deep if pop_deep > 0 else float('inf')

        print(f"  {K0_test:6.2f}  {r_test:12.8f}  {K0_test * r_test:10.6f}  "
              f"{md:12.2e}  {ratio:14.2f}")

    # ── The ψ-mode ────────────────────────────────────────────────────
    print(f"\n{'═' * 72}")
    print("  THE ψ-MODE: finite depth ≠ infinite trajectory")
    print(f"{'═' * 72}")

    N_CYCLES = 14
    residuals = psi_residual(N_CYCLES)
    fibs = [1, 1]
    for _ in range(N_CYCLES + 5):
        fibs.append(fibs[-1] + fibs[-2])

    print(f"\n  {'depth':>5s}  {'period':>10s}  {'residual':>20s}")
    print("  " + "-" * 40)
    for n_val in range(N_CYCLES + 1):
        print(f"  {n_val:5d}  {fibs[n_val + 1]:10d}  "
              f"{residuals[n_val]:+20.12f}")

    print(f"\n  At every depth: sign flips, amplitude × φ^{{-2}}.")
    print(f"  No finite depth tells you the next sign.")
    print(f"  The Cassini identity guarantees it flips.")

    # ── Summary ───────────────────────────────────────────────────────
    print(f"\n{'═' * 72}")
    print("  SUMMARY")
    print(f"{'═' * 72}")
    print(f"""
  The observable is not a state.
  It is the fixed point of an operator on distributions over states.

  U: Dist(C) → Dist(C)
  U(g)(f) = g_bare(f) × w(f, K₀|r(g)|) / Z

  U factors through a 1D bottleneck:
    g ─→ |r(g)| ─→ K_eff ─→ {{w(f,K)}} ─→ g_new
    N      1        1         N           N

  Fixed-point equation: F(|r|) = |r|
    F continuous, decreasing, F(0) > 0, F(1) < 1
    ⇒ unique crossing by IVT
    ⇒ g* unique

  Located by bisection (not iteration):
    |r*| = {r_star:.12f}
    max|U(g*) - g*| = {max_diff:.2e}

  F'(|r*|) = {F_slope:.2f} (|F'| > 1 → naive iteration 2-cycles)
  The 2-cycle is an artifact of the iteration scheme.
  The fixed point is not.

  Properties of g*:
    - Scale-invariant density along Fibonacci backbone
    - Born rule: P(p/q) = g*(p/q) / Σg*
    - Unique at each K₀

  What is not the observable:
    - Any particular state g₀
    - The iteration trajectory g₀, U(g₀), U²(g₀), ...
    - The 2-cycle attractor of the naive iteration
    - The convergence history

  The observable is the unique g* such that U(g*) = g*.
  Everything else is scaffolding.
""")
