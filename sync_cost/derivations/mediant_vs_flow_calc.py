"""
mediant_vs_flow_calc.py — the decisive #FLOW measurement.

Poses-doc: mediant_vs_flow_problem.md. The single decidable difference
between (Flow = continuous critical circle map) and (Mediant = discrete
generator) is the K=1 complement:

  - Critical circle map (where the universal Jensen-Bak-Bohr dimension
    D ~= 0.8700 lives) is the KNIFE-EDGE: mode-locked tongues exactly
    fill the line, total tongue measure Sum -> 1^-, complement is a
    measure-zero Cantor set of dimension D ~= 0.8700.
  - Sub-critical: Sum < 1, complement has positive measure, dimension 1.
  - Past filling (Sum > 1): tongues over-cover, complement is EMPTY
    (complete tree). No measure-zero fractal -> D ~= 0.8700 cannot exist.

So the decisive test is the regime: compute the framework's OWN total
tongue-width sum at K=1 using its OWN perturbative width
w(p/q, K) = 2 (K/2)^q / q, summed over all reduced rationals in [0,1)
(phi(q) of them per denominator q).

D ~= 0.8700 is realizable ONLY at Sum == 1 (exactly critical). Any
robust departure decides the regime.
"""

from math import gcd


def euler_phi(n: int) -> int:
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


def tongue_width(q: int, K: float = 1.0) -> float:
    # framework perturbative Arnold-tongue width (born_rule.md, a1_from_saddle_node.md)
    return 2.0 * (K / 2.0) ** q / q


def total_measure(K: float = 1.0, q_max: int = 200) -> float:
    return sum(euler_phi(q) * tongue_width(q, K) for q in range(1, q_max + 1))


if __name__ == "__main__":
    S = total_measure(K=1.0, q_max=200)
    print(f"Sum_(p/q in [0,1)) w(p/q, K=1)  =  {S:.6f}")
    print("knife-edge (critical, D~=0.8700 exists): Sum == 1")
    print("sub-critical (D == 1):                   Sum  < 1")
    print("complete/over-covered (no complement):   Sum  > 1")
    verdict = (
        "PAST exact-filling -> complete-tree regime; "
        "measure-zero fractal complement does NOT exist; "
        "universal D~=0.8700 structurally unrealizable at K=1"
    )
    assert S > 1.0, "regime check"
    print("VERDICT:", verdict)
    # convergence (decisive margin, not a knife-edge artifact)
    for q_max in (1, 2, 5, 10, 30, 100):
        print(f"  q<= {q_max:4d}:  Sum = {total_measure(1.0, q_max):.6f}")
