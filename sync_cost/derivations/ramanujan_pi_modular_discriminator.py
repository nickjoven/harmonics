"""
ramanujan_pi_modular_discriminator.py

The structural discriminator for ramanujan_pi_minimum_alphabet.md:
does the framework's forced modular data ever land on the data that
makes a Ramanujan 1/pi series special?

The Ramanujan-Sato hierarchy has TWO coordinates:
  - LEVEL  l   : the congruence subgroup Gamma_0(l). Small, structural.
  - DISCRIMINANT d : the singular value tau = sqrt(-d). Picks the
                     specific series within a level.

Framework forced datum (psl2z_subgroup_phase_a_results.md):
  Gamma_0(6),  level 6 = q_2 * q_3 = INTERACT.

1914 series (verified, Borwein-Borwein-Bailey 1989):
  level 2 (Gamma_0(2)),  discriminant d = 58 = 2*29,
  proved via a degree-29 modular equation.

This script tabulates the two layers and tests whether 29 (the prime
that fixes the 1914 series) or 58 has any substrate footing.
"""

# --- Farey counts |F_n| = 1 + sum_{k=1}^n phi(k) (framework mode counts) ---
def phi(n):
    r, m, p = n, n, 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            r -= r // p
        p += 1
    if m > 1:
        r -= r // m
    return r

FORCED_DEPTH = 6   # |F_6| = 13 drives Omega_Lambda = 13/19; |F_7| = 19

F = 1
farey = {}
for n in range(1, 12):
    F += phi(n)
    farey[n] = F

print("Farey counts |F_n| (framework mode counts):")
for n, v in farey.items():
    tag = "  <- forced depth (Omega_Lambda)" if n == FORCED_DEPTH else ""
    tag = "  <- 29 first appears here (depth 9)" if v == 29 else tag
    print(f"  |F_{n:>2}| = {v}{tag}")

# --- the two-coordinate ledger ---
print("\n--- Ramanujan-Sato two-coordinate ledger ---")
rows = [
    ("coordinate", "1914 series", "framework forced", "match?"),
    ("LEVEL (Gamma_0)", "2", "6 = q_2*q_3 (INTERACT)", "no (but 2 | 6)"),
    ("  -> uses prime", "{2}", "{2,3}", "partial: shares 2"),
    ("DISCRIMINANT d", "58 = 2*29", "(none supplied)", "NO"),
    ("  -> selector prime", "29", "{2,3}", "NO (29 foreign)"),
]
for a, b, c, d in rows:
    print(f"  {a:<18} {b:<14} {c:<24} {d}")

# --- is 29 / 58 framework-reachable? ---
print("\n--- footing test for the discriminant primes ---")
print(f"  29 == |F_9|?  {29 == farey[9]}  (Farey count at DEPTH 9)")
print(f"  framework forced depth = {FORCED_DEPTH}; 29 sits 3 levels deeper")
print(f"  58 = q_2 * |F_9| = 2 * 29 = {2*29}  (depth-9 mediant; not forced)")
print("  verdict: 29 is a deep-mediant artifact outside the forced depth-6")
print("           cone -> the 'z-fighting / far-plane' regime that")
print("           minimum_alphabet.md's cluster note declines to promote.")

# --- the cusp / divisor lattice of level 6 (the positive side) ---
print("\n--- level-6 divisor lattice: framework cusps vs eta-quotient ---")
print("  divisors of 6: 1, 2, 3, 6")
print("  Gamma_0(6) cusps (framework):  inf(d=1), 1/2(d=2), 1/3(d=3), 0(d=6)")
print("  framework sectors:             generic, q_2,      q_3,      INTERACT")
print("  level-6 Hauptmodul j_6B:       (eta(2t)eta(3t)/(eta(t)eta(6t)))^12")
print("  -> same four divisors {1,2,3,6}; the q_2 x q_3 factorization IS")
print("     the divisor lattice of 6 IS the eta-quotient index set.")
