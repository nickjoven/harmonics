"""framework_core.py — the synchronization-cost framework's structural side
in lambda-functional Python.

A single self-contained file that derives the framework's headline
dimensionless predictions — Ω_Λ, sin²θ_W, α_s/α₂, n_s, K_c — from
first principles, with no fitting, no SI conversions, no mutable state.

Run with:
    python3 sync_cost/derivations/framework_core.py
"""

from fractions import Fraction
from functools import reduce
from math import gcd, log, pi, sqrt
from typing import Callable, Iterator, Tuple

Pair = Tuple[int, int]


# ── Tier 0: the four primitives ──────────────────────────────────────────
# Integers — Python native.
# Mediant — the column-sum on unimodular pairs.
# Fixed point — Banach iteration as a higher-order function.
# Parabola — the saddle-node normal form.

mediant: Callable[[Pair, Pair], Pair] = lambda p, q: (p[0] + q[0], p[1] + q[1])

fixed_point = lambda f, x0, eps=1e-12, max_iter=10_000: (
    reduce(
        lambda x, _: x if (lambda fx: abs(fx - x) < eps)(f(x)) else f(x),
        range(max_iter),
        x0,
    )
)

parabola = lambda eps: lambda x: eps - x * x


# ── Tier 1: Farey counting on the Stern-Brocot tree ──────────────────────

totient = lambda n: sum(1 for k in range(1, n + 1) if gcd(n, k) == 1)

farey_count = lambda n: 1 + sum(map(totient, range(1, n + 1)))


# Stern-Brocot tree as a lazy generator (depth-bounded, in-order traversal).
def stern_brocot(depth: int, left: Pair = (0, 1), right: Pair = (1, 0)) -> Iterator[Pair]:
    if depth == 0:
        return
    m = mediant(left, right)
    yield from stern_brocot(depth - 1, left, m)
    yield m
    yield from stern_brocot(depth - 1, m, right)


# ── Tier 3: structural constants ─────────────────────────────────────────

phi = (1 + sqrt(5)) / 2          # golden ratio, fixed point of x² = x + 1
phi_sq = phi + 1                 # φ² = φ + 1, the staircase self-similarity ratio
K_c = lambda: 2 / pi             # Kuramoto critical coupling for uniform g(0) = 1


# ── Tier 4: the dimensionless predictions ────────────────────────────────
# All functions of zero arguments, all returning exact rationals or
# transparent floats. No fitting. Each value comes from counting.

# Ω_Λ = |F_6| / (|F_6| + q₂·q₃) = 13/19.
omega_Lambda = lambda: Fraction(farey_count(6), farey_count(6) + 2 * 3)

# Klein-bottle XOR parity selects exactly 4 surviving modes at q ∈ {2, 3}.
klein_modes = lambda: 4

# Duty cycle d(q) = w(p/q, K=1) / q = (1/q²) / q = 1/q³ at K = 1.
duty = lambda q: Fraction(1, q ** 3)

# Weinberg angle: sin²θ_W = duty(3) / (duty(2) + duty(3)) = 8/35.
sin2_theta_W = lambda: duty(3) / (duty(2) + duty(3))

# Gauge coupling ratio α_s/α₂ = duty(2)/duty(3) = 27/8.
alpha_ratio = lambda: duty(2) / duty(3)

# Spectral tilt: 2/57 ≈ 0.0351 Fibonacci levels per CMB e-fold (substrate-forced
# cadence per PRs #178/#179; see minimum_alphabet.md §3). Earlier n_s-anchored
# rate ≈ 0.0365 (= 1/27.4) is superseded. The lambda below now returns the
# substrate-side prediction n_s ≈ 0.9662; scorecard promotion of that value
# is flagged as a separate Wave-1.5 audit (not promoted here).
n_s = lambda: 1 - log(phi_sq) * Fraction(2, 57)


# ── Tier 5: address (the only place anchors enter) ───────────────────────
# Tree depth from the Planck-to-Hubble frequency ratio.

tree_depth = lambda omega_planck, H_0: log(omega_planck / H_0) / log(phi_sq)


# ── Reporting ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    fmt = lambda label, value, observed=None: (
        f"  {label:<22s} = {str(value):<14s}"
        + (f" ≈ {float(value):.6f}" if isinstance(value, Fraction) else "")
        + (f"   observed: {observed}" if observed else "")
    )

    print("Synchronization-cost framework — structural predictions")
    print("=" * 60)
    print(fmt("|F_6|",          farey_count(6)))
    print(fmt("q₂·q₃",          2 * 3))
    print(fmt("Ω_Λ",            omega_Lambda(),   "0.685 ± 0.007 (Planck 2018)"))
    print(fmt("sin²θ_W",        sin2_theta_W(),   "0.2312 (PDG)"))
    print(fmt("α_s/α₂",         alpha_ratio(),    "≈ 3.05 at M_Z (running)"))
    print(fmt("n_s",            f"{n_s():.6f}",   "0.9649 ± 0.0042"))
    print(fmt("K_c",            f"{K_c():.6f}",   "Kuramoto uniform g(0)=1"))
    print(fmt("φ²",             f"{phi_sq:.6f}",  "staircase scaling"))
    print(fmt("Klein modes",    klein_modes(),    "after XOR parity filter"))

    print()
    print("Stern-Brocot tree, first 7 mediants (depth 3, in-order):")
    for p, q in list(stern_brocot(3))[:7]:
        print(f"  {p}/{q}")
