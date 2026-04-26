"""
PSL(2,Z)-subgroup orbit enumeration for w_+ candidates.

For each of {Γ(2), Γ_0(2), Γ_0(3), Γ_0(6)}, partition the three
w_+ candidates {13/14, 12/13, 14/15} into orbits under the
subgroup's action on P^1(Q) by Mobius transformations.

The cusps of X_0(N) (= Γ_0(N) orbits on P^1(Q)) are parametrized
by (d, a) with d | N and a in (Z/gcd(d, N/d))^* / {±1}.

For p/q in lowest terms with q > 0 and gcd(p, q) = 1, the cusp
class under Γ_0(N) is determined by d = gcd(q, N) and a residue
in (Z/gcd(d, N/d))^*. When gcd(d, N/d) = 1 (which holds for all
divisors of N=6, since 6 is squarefree), the residue is trivial
and the cusp class is determined by d alone.

For Γ(N), the cusps are (Z/N)^2 \ {(0,0)} / {±1}, parametrized
by (p mod N, q mod N).
"""

from math import gcd

CANDIDATES = [(13, 14), (12, 13), (14, 15)]


def normalize(p, q):
    """Reduce p/q to lowest terms with q > 0."""
    g = gcd(abs(p), abs(q))
    p, q = p // g, q // g
    if q < 0:
        p, q = -p, -q
    return p, q


def gamma0_N_cusp(p, q, N):
    """
    Cusp class of p/q under Γ_0(N).
    Returns (d, a) where d = gcd(q, N) and a is the residue class
    in (Z/gcd(d, N/d))^* / {±1}.
    For squarefree N (like 6), gcd(d, N/d) = 1 always, so a is
    trivial and (d,) characterizes the cusp.
    """
    p, q = normalize(p, q)
    d = gcd(q, N)
    h = gcd(d, N // d)
    if h == 1:
        return (d,)
    # Otherwise, compute a = p * (q/d)^{-1} mod h, up to sign
    qd = q // d
    qd_inv = pow(qd, -1, h)
    a = (p * qd_inv) % h
    a = min(a, h - a)  # ±-equivalence
    return (d, a)


def gamma_N_cusp(p, q, N):
    """
    Cusp class of p/q under Γ(N). Cusps are (Z/N)^2 \ {(0,0)} / {±1}.
    """
    p, q = normalize(p, q)
    pn, qn = p % N, q % N
    # ±-equivalence
    pn2, qn2 = (-p) % N, (-q) % N
    return min((pn, qn), (pn2, qn2))


print("=" * 60)
print("Cusp classes of w_+ candidates under PSL(2,Z) subgroups")
print("=" * 60)

for N in [2, 3, 6]:
    print(f"\n--- Γ_0({N}) ---")
    for p, q in CANDIDATES:
        cusp = gamma0_N_cusp(p, q, N)
        print(f"  {p}/{q}: gcd({q},{N}) = {gcd(q,N)}, cusp class {cusp}")
    classes = {gamma0_N_cusp(p, q, N) for p, q in CANDIDATES}
    print(f"  Distinct cusp classes: {len(classes)} of 3 candidates")
    if len(classes) == 3:
        print(f"  → SPLITS all three candidates")
    elif len(classes) == 2:
        print(f"  → 2-way split")
    else:
        print(f"  → all in same orbit (no split)")

print(f"\n--- Γ(2) ---")
for p, q in CANDIDATES:
    cusp = gamma_N_cusp(p, q, 2)
    print(f"  {p}/{q}: cusp class {cusp}")
classes = {gamma_N_cusp(p, q, 2) for p, q in CANDIDATES}
print(f"  Distinct cusp classes: {len(classes)} of 3 candidates")

print(f"\n--- Γ(3) ---")
for p, q in CANDIDATES:
    cusp = gamma_N_cusp(p, q, 3)
    print(f"  {p}/{q}: cusp class {cusp}")
classes = {gamma_N_cusp(p, q, 3) for p, q in CANDIDATES}
print(f"  Distinct cusp classes: {len(classes)} of 3 candidates")

print(f"\n--- Γ(6) ---")
for p, q in CANDIDATES:
    cusp = gamma_N_cusp(p, q, 6)
    print(f"  {p}/{q}: cusp class {cusp}")
classes = {gamma_N_cusp(p, q, 6) for p, q in CANDIDATES}
print(f"  Distinct cusp classes: {len(classes)} of 3 candidates")

print()
print("=" * 60)
print("Cusp counts for reference (number of orbits on P^1(Q)):")
print("  Γ_0(2): 2 cusps")
print("  Γ_0(3): 2 cusps")
print("  Γ_0(6): 4 cusps  ← squarefree, all divisors d | 6 give distinct cusps")
print("  Γ(2):   3 cusps")
print("  Γ(3):   4 cusps")
print("  Γ(6):  12 cusps")
print("=" * 60)
