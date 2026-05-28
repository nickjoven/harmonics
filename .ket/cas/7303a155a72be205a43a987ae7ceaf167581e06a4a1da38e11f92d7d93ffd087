#!/usr/bin/env python3
"""Lepton μ/e closure via the Koide constraint Q = 2/3 — the reconciliation check.

Settles the 26:7:1 conflict (numerology_inventory.md §C1 "Class 1" vs
fermion_mass_running.md D50 "closed"). The two judged DIFFERENT closures:

  - Bare tree: m_μ/m_e = 7^(5/2) = 129.6  vs observed 206.8  -> 37% miss (Class 1).
    The "K->μ running correction" patch is undefined; that null stands.
  - Koide closure: impose Q = 2/3 (the Klein-bottle population ratio,
    klein_bottle.md) together with the framework tree τ/e = 26^(5/2), and
    SOLVE for μ/e. This is the closure the 2026-04 audit did not evaluate.

Result: the Koide closure gives m_μ/m_e ≈ 204.8 (0.96%). So the honest verdict
is FLOOR, not Class 1 and not "closed/9->1": a structural mechanism reaching
the ~1% particle-sector coincidence floor, but with the Koide FORM imported
(only Q=2/3's value is framework-derived) and the 26:7:1 base / 5/2 exponent
un-forced. See free_parameter_scorecard.md, numerology_inventory.md.

μ/e is an OUTPUT here (solved from m_e scale + tree τ/e + Q=2/3), not an input
— the closure is a genuine prediction, not circular.

Run: python3 koide_closure_check.py
"""
from __future__ import annotations


def koide_Q(me: float, mmu: float, mtau: float) -> float:
    """Koide ratio Q = (Σ m) / (Σ √m)^2 ; equals 2/3 for the observed leptons."""
    return (me + mmu + mtau) / ((me**0.5 + mmu**0.5 + mtau**0.5) ** 2)


def solve_mu_from_koide(tau: float, Q: float = 2.0 / 3.0) -> float:
    """With m_e = 1 and m_τ/m_e = tau, solve Koide(Q) for the physical m_μ/m_e."""
    st = tau**0.5
    # Q (1 + s + st)^2 = 1 + s^2 + tau, s = √μ  ->  (Q-1)s^2 + 2Q(1+st)s + [Q(1+st)^2 - (1+tau)] = 0
    a, b, c = Q - 1.0, 2.0 * Q * (1.0 + st), Q * (1.0 + st) ** 2 - (1.0 + tau)
    disc = b * b - 4 * a * c
    roots = [((-b + sgn * disc**0.5) / (2 * a)) ** 2 for sgn in (+1.0, -1.0)]
    physical = [m for m in roots if 0.0 < m < tau]  # lighter than τ
    return physical[0]


def main() -> int:
    mu_obs, tau_obs = 206.768, 3477.23
    tau_tree, mu_tree = 26**2.5, 7**2.5

    print(f"observed Koide Q          = {koide_Q(1, mu_obs, tau_obs):.5f}  (= 2/3)")
    print(f"bare tree μ/e = 7^(5/2)   = {mu_tree:.1f}  vs obs {mu_obs:.1f}  "
          f"({(mu_tree / mu_obs - 1) * 100:+.0f}%)  -> Class 1")
    print(f"tree Koide Q (μ=129.6)    = {koide_Q(1, mu_tree, tau_tree):.5f}  (violates 2/3)")
    print()
    mu_closed = solve_mu_from_koide(tau_tree)
    print(f"Koide(2/3) + tree τ/e={tau_tree:.0f} -> μ/e = {mu_closed:.1f}  "
          f"vs obs {mu_obs:.1f}  ({(mu_closed / mu_obs - 1) * 100:+.2f}%)")
    print(f"Koide(2/3) + obs  τ/e={tau_obs:.0f} -> μ/e = {solve_mu_from_koide(tau_obs):.1f}  "
          f"(sanity: ≈ observed)")
    print()
    print("VERDICT: Floor. Closure works (~1%) but at the coincidence floor;")
    print("Koide form imported, 26:7:1 base / 5/2 exponent un-forced. Not Class 1, not 'closed'.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
