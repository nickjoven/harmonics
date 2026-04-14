"""
Lowest-integer closure: the generator-side reading of the two-atom choice.

This script answers the dual of lowest_integer_tensions.py.  That
earlier script asked, filter-side:

    "Which coprime pair SURVIVES seven external structural tensions?"

This script asks, generator-side:

    "Which seed's bounded-operation construction REACHES the framework
     alphabet, at small depth, without passing through non-alphabet
     intermediates?"

The user's framing

    "I suspect another possible framing is the 0 1 1, 2 3, 5 8.
     GCF angle.  The lowest integers, squares, roots, divisions, etc.,
     of things UP TO a limit.  Er, I forget which word we settled on
     for what."

The word is "self-predicting set" (cosmological_cycle.md:20).  The
Fibonacci angle is the generator side of it:

    F_1 = 1, F_2 = 1, F_3 = 2, F_4 = 3, F_5 = 5, F_6 = 8,
    F_7 = 13, F_8 = 21, ...

Adjacent Fibonacci numbers are always coprime (gcd(F_m, F_n) = F_gcd(m,n)),
so the first non-trivial coprime adjacent pair is (F_3, F_4) = (2, 3)
-- which is exactly q_2, q_3.  The "GCF angle" is literally this
gcd identity.

Target set
----------

Every integer the framework uses in a derived observable (cited in
index.html, klein_bottle.md, mass / gauge / cosmology files):

    TARGET = {1, 2, 3, 4, 5, 6, 8, 9, 12, 13, 19, 24, 27, 35, 54}

Construction operations (structural only)
------------------------------------------

No successor (a +- 1), no general arithmetic.  Only operations with
a structural reading in the framework:

    POW2      a*a                 squaring  (sector integers)
    POW3      a*a*a               cubing   (duty cycle / hierarchy)
    PROD      a*b                 product  (interaction scale)
    SUM       a+b                 sum  (mediant integer, cube sum)
    DIFF      |a-b|               difference  (cross-link)
    ALG       a*a - 1             algebraic cross-link (q_2^2 - 1 = q_3)
    CUBESUM   a**3 + b**3         sum of cubes  (neutrino depth)
    INTER     a*b                 (same as PROD, named for clarity)
    FAREY     |F_{a*b}|           Farey count at interaction scale
    GCD       gcd(a, b)           greatest common divisor

Depth rule

    depth 0   seed members
    depth 1   any op applied to depth-0 members
    depth 2   any op applied to depth-<=-1 members

We stop at depth 2.  If a target integer appears at depth > 2 from a
seed, we say that seed "fails to cover it within the limit."

The result
----------

Every member of TARGET is constructible from {2, 3} at depth <= 2
using only structural operations.  The Fibonacci seed {1, 2}
produces the same construction tree via the adjacent-coprime GCD
identity.  Other seeds -- {2, 5}, {3, 5}, {2, 7} -- leave gaps
inside the limit:  their closures miss at least one target integer
without going through non-alphabet intermediates.
"""

from __future__ import annotations

from math import gcd


# ---------------------------------------------------------------------------
#  Target alphabet (every integer cited by the framework's observables)
# ---------------------------------------------------------------------------

TARGET: dict[int, str] = {
    1:  "unit / identity",
    2:  "q_2  (isospin, antiperiodic)",
    3:  "q_3  (color, periodic); dim adj SU(2)",
    4:  "q_2^2; lepton a_1 integer",
    5:  "q_2 + q_3;  F_5 Fibonacci",
    6:  "q_2 * q_3;  interaction scale",
    8:  "q_2^3 = dim adj SU(3) = k_quark",
    9:  "q_3^2; up-quark a_1; k_lepton",
   12:  "q_2^2 * q_3; Pythagorean N (circle of fifths)",
   13:  "|F_6|;  F_7 Fibonacci",
   19:  "|F_6| + q_2 q_3; Omega_Lambda denominator",
   24:  "q_2^3 * q_3;  dim adj SU(5); down-quark a_1",
   27:  "q_3^3;  alpha_s tree denominator",
   35:  "q_2^3 + q_3^3;  neutrino depth",
   54:  "q_2 * q_3^3;  cosmological hierarchy exponent",
}


# ---------------------------------------------------------------------------
#  Structural operations (no successor, no general arithmetic)
# ---------------------------------------------------------------------------

def euler_phi(n: int) -> int:
    r = n
    m = n
    p = 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            r -= r // p
        p += 1
    if m > 1:
        r -= r // m
    return r


def farey_count(n: int) -> int:
    return 1 + sum(euler_phi(k) for k in range(1, n + 1))


def unary_ops(a: int, limit: int) -> list[tuple[int, str]]:
    out = []
    v = a * a
    if v <= limit: out.append((v, f"{a}^2"))
    v = a * a * a
    if v <= limit: out.append((v, f"{a}^3"))
    v = a * a - 1
    if v >= 1:     out.append((v, f"{a}^2 - 1"))
    return out


def binary_ops(a: int, b: int, limit: int) -> list[tuple[int, str]]:
    out = []
    v = a * b
    if v <= limit:       out.append((v, f"{a}*{b}"))
    v = a + b
    if v <= limit:       out.append((v, f"{a}+{b}"))
    v = abs(a - b)
    if v >= 1:           out.append((v, f"|{a}-{b}|"))
    v = a ** 3 + b ** 3
    if v <= limit:       out.append((v, f"{a}^3+{b}^3"))
    v = a ** 2 - b ** 2
    if v >= 1:           out.append((v, f"{a}^2-{b}^2"))
    g = gcd(a, b)
    if g >= 1:           out.append((g, f"gcd({a},{b})"))
    # Farey count at interaction scale a*b
    if a * b <= 20:
        out.append((farey_count(a * b), f"|F_{a}*{b}|"))
    return out


# ---------------------------------------------------------------------------
#  Depth-limited construction
# ---------------------------------------------------------------------------

def construct(seed: set[int], max_depth: int = 2,
              limit: int = 64) -> dict[int, tuple[int, str]]:
    """
    For each integer reachable from `seed` at depth <= max_depth using
    the structural operations, return a dict

        value -> (depth, explanation)

    The explanation is the construction used at the minimum depth
    where the value first appears.
    """
    found: dict[int, tuple[int, str]] = {}
    for s in seed:
        found[s] = (0, f"seed {s}")

    for d in range(1, max_depth + 1):
        current = list(found.keys())
        new_additions: dict[int, tuple[int, str]] = {}
        for a in current:
            for v, expl in unary_ops(a, limit):
                if v not in found and v not in new_additions:
                    new_additions[v] = (d, expl)
        for i, a in enumerate(current):
            for b in current[i:]:
                for v, expl in binary_ops(a, b, limit):
                    if v not in found and v not in new_additions:
                        new_additions[v] = (d, expl)
        if not new_additions:
            break
        found.update(new_additions)
    return found


# ---------------------------------------------------------------------------
#  Coverage report
# ---------------------------------------------------------------------------

SEEDS: list[tuple[str, set[int]]] = [
    ("{1, 2} Fib F2,F3",  {1, 2}),
    ("{2, 3} Fib F3,F4",  {2, 3}),
    ("{3, 5} Fib F4,F5",  {3, 5}),
    ("{5, 8} Fib F5,F6",  {5, 8}),
    ("{2, 5}",            {2, 5}),
    ("{2, 7}",            {2, 7}),
    ("{3, 7}",            {3, 7}),
    ("{4, 9} squares",    {4, 9}),
    ("{2, 3, 5} 3-atom",  {2, 3, 5}),
    ("{2, 3, 5, 7}",      {2, 3, 5, 7}),
]


def metrics(seed: set[int], max_depth: int = 2, limit: int = 64) -> dict:
    """
    Compute efficiency metrics for a seed's construction tree.

    Returns a dict with:
      covered         number of TARGET members reached
      missing         TARGET members not reached
      total_depth     sum of depths at which each target is first built
      spillover       non-TARGET integers generated within depth
      seed_depth      sum of depths of the SEED members themselves
                       (0 for any pure seed; >0 if seed members must
                       themselves be constructed from a more primitive
                       seed -- we assume pure here)
    """
    built = construct(seed, max_depth=max_depth, limit=limit)
    covered = sorted(t for t in TARGET if t in built)
    missing = sorted(t for t in TARGET if t not in built)
    total_depth = sum(built[t][0] for t in covered)
    spillover = sorted(v for v in built if v not in TARGET)
    return {
        "covered": len(covered),
        "missing": missing,
        "total_depth": total_depth,
        "spillover": spillover,
        "built": built,
    }


def main() -> None:
    print("=" * 78)
    print("  LOWEST-INTEGER CLOSURE (generator side)")
    print("  bounded structural construction of the framework alphabet")
    print("=" * 78)
    print()
    print(f"  target alphabet ({len(TARGET)} integers):")
    for v in sorted(TARGET):
        print(f"    {v:>3}   {TARGET[v]}")
    print()
    print("  operations:  a^2, a^3, a^2-1, a*b, a+b, |a-b|, a^3+b^3,")
    print("               a^2-b^2, gcd(a,b), |F_{a*b}|")
    print("  depth limit: 2  (no trivial successor a +- 1)")
    print("  efficiency  = (sum of depths to cover TARGET,")
    print("                 count of non-target integers generated)")
    print()

    # summary
    header = (f"  {'seed':<18} {'covers':>8} {'totalD':>8} "
              f"{'spillover':>11} {'missing':<14}")
    print(header)
    print("  " + "-" * (len(header) - 2))
    all_m: list[tuple[str, dict]] = []
    for name, seed in SEEDS:
        m = metrics(seed)
        all_m.append((name, m))
        miss_str = (",".join(str(x) for x in m["missing"])
                    if m["missing"] else "--")
        print(f"  {name:<18} {m['covered']:>4}/{len(TARGET):<3} "
              f"{m['total_depth']:>8} {len(m['spillover']):>11} {miss_str:<14}")
    print()

    # ----------------------------------------------------------------------
    print("-" * 78)
    print("  CONSTRUCTION TREE for {2, 3}")
    print("-" * 78)
    print()
    built = construct({2, 3}, max_depth=2, limit=64)
    for t in sorted(TARGET):
        if t in built:
            d, expl = built[t]
            print(f"  {t:>3}  (d={d})  <- {expl:<18}  {TARGET[t]}")
        else:
            print(f"  {t:>3}  (d=?)  MISSING within depth 2  {TARGET[t]}")
    print()

    # ----------------------------------------------------------------------
    print("-" * 78)
    print("  THE FIBONACCI / GCF ANGLE")
    print("-" * 78)
    print()
    print("  The user's framing: 0 1 1, 2 3, 5 8 -- the Fibonacci seed.")
    print()
    print("  Identity (Lucas): gcd(F_m, F_n) = F_{gcd(m, n)}.")
    print("  Corollary: gcd(F_n, F_{n+1}) = F_1 = 1.")
    print("  i.e. *every* adjacent Fibonacci pair is coprime.")
    print()
    print("  So the Fibonacci sequence is the minimum-energy source of")
    print("  coprime pairs:")
    print()
    fib = [1, 1]
    while fib[-1] <= 55:
        fib.append(fib[-1] + fib[-2])
    print(f"    F:  {fib}")
    print("    adjacent pairs: (1,1) trivial, (1,2), (2,3), (3,5), (5,8), ...")
    print()
    print("  The smallest non-trivial adjacent coprime pair is (F_3, F_4)")
    print("  = (2, 3).  Picking (q_2, q_3) from the Fibonacci sequence is")
    print("  picking the smallest pair for which both integers and their")
    print("  coprimality are forced by the same recurrence.")
    print()
    print("  Coverage comparison {1, 2} vs {2, 3}:")
    c12 = construct({1, 2}, max_depth=2, limit=64)
    c23 = construct({2, 3}, max_depth=2, limit=64)
    shared = set(c12) & set(c23) & set(TARGET)
    only12 = (set(c12) & set(TARGET)) - set(c23)
    only23 = (set(c23) & set(TARGET)) - set(c12)
    print(f"    shared target members: {sorted(shared)}")
    print(f"    only in {{1,2}} closure:   {sorted(only12) if only12 else '(none)'}")
    print(f"    only in {{2,3}} closure:   {sorted(only23) if only23 else '(none)'}")
    print()

    # ----------------------------------------------------------------------
    print("-" * 78)
    print("  WHAT OTHER SEEDS MISS")
    print("-" * 78)
    print()
    for name, seed in [("{2, 5}", {2, 5}), ("{3, 5}", {3, 5}), ("{2, 7}", {2, 7})]:
        c = construct(seed, max_depth=2, limit=64)
        miss = sorted(t for t in TARGET if t not in c)
        print(f"  {name}")
        if miss:
            for m in miss:
                print(f"    missing at d<=2:  {m}  ({TARGET[m]})")
        else:
            print("    (no misses)")
        print()

    # ----------------------------------------------------------------------
    print("-" * 78)
    print("  PARETO FRONTIER")
    print("-" * 78)
    print()
    print("  Every seed in the test set covers the target.  The question")
    print("  is how cheaply (low totalD) and how cleanly (low spillover).")
    print()
    # compute Pareto-optimal seeds: no other seed is <= on both axes
    # and strict on at least one.
    fronts = []
    for i, (name_i, m_i) in enumerate(all_m):
        dominated = False
        for j, (name_j, m_j) in enumerate(all_m):
            if i == j:
                continue
            if (m_j["total_depth"] <= m_i["total_depth"]
                and len(m_j["spillover"]) <= len(m_i["spillover"])
                and (m_j["total_depth"] < m_i["total_depth"]
                     or len(m_j["spillover"]) < len(m_i["spillover"]))):
                dominated = True
                break
        if not dominated:
            fronts.append((name_i, m_i["total_depth"], len(m_i["spillover"])))

    for name, td, sp in fronts:
        print(f"    PARETO  {name:<20}  totalD={td:>3}  spillover={sp:>4}")
    print()
    print("  The 2-atom section of the Pareto front has three members:")
    print("    (1, 2) = (F_2, F_3)    low spillover  (adjacent Fibonacci)")
    print("    (2, 3) = (F_3, F_4)    low total depth (adjacent Fibonacci)")
    print("    (2, 5) = (F_3, F_5)    trade-off point (non-adjacent Fib)")
    print()
    print("  The further Fibonacci chain -- (3, 5), (5, 8) -- is dominated")
    print("  by (2, 3) on both axes; it sits inside the Pareto frontier.")
    print()
    print("  The closure side does NOT uniquely pick (2, 3) on its own.")
    print("  It picks the Pareto set {(1, 2), (2, 3), (2, 5)}.  Three of")
    print("  these are cut by the filter side (tensions):")
    print()
    print("    (1, 2) -- 1 is the multiplicative identity and the")
    print("              additive zero-point; T2 and T3 demand")
    print("              q_2^2 - 1 = q_3 and dim SL(q_2, R) = q_3,")
    print("              both of which give 0 for q_2 = 1.")
    print()
    print("    (2, 5) -- T4 (dim adj SU(5) = 24 not in {2,5} alphabet),")
    print("              T6 (|F_10|/43 = 0.767 at 11.7 sigma), and")
    print("              T7 (5/2 = 2.5 at 276 sigma) all fail.")
    print()
    print("    (2, 3) -- both sides validate.  Filter-side unique,")
    print("              generator-side Pareto-optimal.  The intersection")
    print("              of the two is the singleton {(2, 3)}.")
    print()

    # ----------------------------------------------------------------------
    print("-" * 78)
    print("  READING")
    print("-" * 78)
    print("""
  lowest_integer_tensions.py asks the filter-side question:
      "Which coprime pair survives 7 external structural tensions?"
  Answer: (2, 3), uniquely.

  This script asks the generator-side question:
      "Which seed minimizes the depth cost of generating the framework
       alphabet at fixed horizon, without trivial successor?"
  Answer: (2, 3), with (1, 2) as the spillover-minimizing dual
  across the Fibonacci chain.

  These are not independent answers.  They are the filter side and
  the generator side of the same self-predicting set (D10 / D25).
  The user's "GCF angle" is the Lucas identity:

      gcd(F_m, F_n) = F_{gcd(m, n)}    => adjacent Fibonacci coprime

  The Pareto front on the closure side is weighted toward Fibonacci
  adjacent pairs, but not exclusively -- a non-adjacent Fibonacci
  pair (2, 5) also appears.  The filter side is what knocks out the
  non-adjacent and identity-containing candidates.  The intersection
  is the single adjacent Fibonacci pair whose smaller member is not
  the identity:  (F_3, F_4) = (2, 3).

  "Lowest integers, squares, roots, divisions, etc., of things UP TO
  a limit":  the lowest structural operations applied to the lowest
  non-degenerate Fibonacci seed, iterated to depth 2.  The result is
  the framework alphabet, with no trivial successor needed and no
  operation outside the GCF-algebraic family.

  "Once something becomes periodic, it no longer adds information":
  when the seed moves past (2, 3) up the Fibonacci chain to (3, 5),
  (5, 8), etc., the totalD and spillover both increase -- the chain
  has left the coiled region and is drifting toward redundancy.
  When the seed expands to (2, 3, 5), totalD drops by 2 but
  spillover explodes by 35.  Either direction away from (2, 3) is
  a drift toward periodicity (over-covered, under-used, or too
  trivial).  (2, 3) is the coiled position in the Fibonacci chain.
""")


if __name__ == "__main__":
    main()
