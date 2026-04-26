"""
Direction 4 Phase C — audit what's needed to force 13/14 within
cusp 1/2 of Γ_0(6).

Inventories the cusp-1/2 orbit representatives and the candidate
"natural representative selection rules" that could pick 13/14.
"""

from math import gcd

# Framework integers
Q2 = 2
Q3 = 3
MEDIANT = 5
INTERACT = 6
F4 = 7
K_QUARK = 8
K_LEPTON = 9
F5 = 11
F6 = 13
F7 = 19

print("=" * 60)
print("Cusp-1/2 of Γ_0(6) representatives near observation")
print("=" * 60)

# Cusp-1/2 orbit: {p/q : gcd(q, 6) = 2, gcd(p, q) = 1, p > 0, p < q}
# (taking representatives in (0, 1))

OBS_W_PLUS = 0.9298  # empirical fit value

print(f"\nObservation: w_+ ≈ {OBS_W_PLUS:.4f}")
print(f"Cusp 1/2 representatives p/q with gcd(q,6)=2 in (0,1) "
      f"close to observation:\n")
print(f"{'p/q':<12} {'value':<10} {'rel.err':<10} {'q factorization':<20}")
print("-" * 56)

orbit_close = []
for q in range(2, 30):
    if gcd(q, 6) != 2:
        continue
    for p in range(1, q):
        if gcd(p, q) != 1:
            continue
        v = p / q
        rel_err = abs(v - OBS_W_PLUS) / OBS_W_PLUS
        if rel_err < 0.05:
            orbit_close.append((p, q, v, rel_err))

orbit_close.sort(key=lambda x: x[3])
for p, q, v, rel_err in orbit_close[:10]:
    # factorize q
    factors = []
    qq = q
    for f in [2, 3, 5, 7, 11, 13]:
        while qq % f == 0:
            factors.append(f)
            qq //= f
    if qq > 1:
        factors.append(qq)
    fact_str = "·".join(str(f) for f in factors)
    print(f"{p}/{q:<10} {v:<10.5f} {rel_err*100:<9.3f}% q = {fact_str:<15}")

print(f"\n{'='*60}")
print(f"Candidate selection rules for cusp-1/2 representative")
print(f"{'='*60}\n")

# Rule A: smallest-q in cusp 1/2
print("Rule A — Smallest-q representative:")
print(f"  Smallest q with gcd(q,6)=2: q=2, giving 1/2 = 0.5")
print(f"  → predicts w_+ = 0.5, observation 0.93 → FAILS")

# Rule B: logit numerator = |F_6| = 13
print("\nRule B — Logit numerator = |F_6| = 13 (DE mode count):")
print(f"  logit(p/q) = p/(q-p); set numerator = 13 → p = 13(q-p) "
      f"→ q-p = p/13, i.e., q = 14p/13")
print(f"  Smallest integer solution with gcd(q,6)=2: p=13, q=14")
print(f"  → predicts w_+ = 13/14 = {13/14:.6f}")
print(f"  Observation: {OBS_W_PLUS:.4f}, rel.err: {abs(13/14 - OBS_W_PLUS)/OBS_W_PLUS*100:.3f}%")
print(f"  → MATCHES, but rule itself is not derived")

# Rule C: complement = 1/(q_2 · |F_4|) = 1/(matter-sector denominator)
print("\nRule C — Complement = 1/(q_2·|F_4|) = inverse Ω_DM denom:")
print(f"  1 - w_+ = 1/14 = 1/{Q2*F4}")
print(f"  → predicts w_+ = 13/14 ≡ Rule B")

# Rule D: q-coordinate = q_2 · |F_4|
print("\nRule D — Denominator = q_2·|F_4|:")
print(f"  q = q_2·|F_4| = {Q2*F4} = 14, then 13 chosen by cusp-orbit "
      f"representative-in-(0,1) closest-to-1")
print(f"  Multiple p/14 with gcd(p,14)=1, p<14: p ∈ "
      f"{{1, 3, 5, 9, 11, 13}}")
print(f"  Closest-to-1: p = 13, giving 13/14")
print(f"  → predicts w_+ = 13/14")

# Multi-candidate alternatives for the unlocking magnitude
print(f"\n{'='*60}")
print(f"Multi-candidate readings for 1 - w_+ = 1/14")
print(f"{'='*60}")

candidates_for_14 = [
    ("q_2 · |F_4|", Q2 * F4),
    ("|F_7| - MEDIANT", F7 - MEDIANT),
    ("2 · |F_4|", 2 * F4),
    ("q_3 + |F_5|", Q3 + F5),
    ("K_QUARK + INTERACT", K_QUARK + INTERACT),
    ("K_LEPTON + MEDIANT", K_LEPTON + MEDIANT),
    ("|F_6| + 1", F6 + 1),
    ("INTERACT + K_QUARK", INTERACT + K_QUARK),
]
print(f"\nThe integer 14 has many framework-internal expressions:")
for name, val in candidates_for_14:
    marker = "✓" if val == 14 else "✗"
    print(f"  {name:<28} = {val:>3}  {marker}")

print(f"\nMulti-candidate ansatz pattern at the unlocking-magnitude")
print(f"level. Per Region C Phase B: this is pigeonhole at α=0.05.")
print(f"Forcing 14 specifically requires substrate-side dynamics,")
print(f"not framework-integer ansatz selection.")

# Alternatives for w_+ NUMERATOR = 13
print(f"\n{'='*60}")
print(f"Multi-candidate readings for the numerator p = 13")
print(f"{'='*60}")
print(f"\nWithin cusp 1/2 with q = 14, valid numerators "
      f"(coprime to 14, in (0,14)):")
valid_p = [p for p in range(1, 14) if gcd(p, 14) == 1]
for p in valid_p:
    fraction = p / 14
    rel_err = abs(fraction - OBS_W_PLUS) / OBS_W_PLUS
    print(f"  p = {p:>2}: {p}/14 = {fraction:.5f}, "
          f"rel.err vs obs = {rel_err*100:>6.3f}%")

print(f"\nObservation 0.9298 fits 13/14 = 0.9286 (0.13% off) and")
print(f"11/14 = 0.7857 (15.5% off). 13 is the unique numerator")
print(f"in this set giving < 1% match.")
print(f"\nBut 'closest-to-observation' is a fit criterion, not a")
print(f"forcing argument. Need substrate-side rule for p=13.")

# Independent structural reading: p = q - 1?
print(f"\n{'='*60}")
print(f"Structural readings of p = 13 = q - 1 = 14 - 1")
print(f"{'='*60}")
print(f"\np = q - 1 reading: 'cusp-1/2 ground state is the orbit")
print(f"representative closest to 1' (largest p with gcd(p,q)=1).")
print(f"For q=14: largest p coprime to 14 in (0,14) is p=13. ✓")
print(f"\nThis IS a candidate selection rule: 'the cusp ground state")
print(f"in the q_2-cusp is the representative closest to total locking")
print(f"(p=q-1)'. The interpretation: at the q_2-cusp, the substrate's")
print(f"sym boundary mode is maximally locked subject to q_2-sector")
print(f"unlocking quantization (1/q steps).")
print(f"\nUnder this rule, 1 - w_+ = 1/q is the smallest possible")
print(f"unlocking magnitude given cusp 1/2 quantization.")
print(f"This is a STRONGER rule than 'just 13/14' — it's a function")
print(f"of q (denominator) that picks the (q-1)/q representative.")
print(f"\nDoes the rule force q = 14?")
print(f"  → No — q can be any 2k with gcd(k,3)=1.")
print(f"  → Smallest q in cusp 1/2 is 2; this gives w_+ = 1/2 (FAILS)")
print(f"  → q = 14 is the framework-integer option (q_2·|F_4|).")
print(f"  → Without forcing q = 14, the rule 'w_+ = (q-1)/q' is")
print(f"    incomplete.")
print(f"\nSo Phase C reduces to: force q = 14 = q_2·|F_4|, "
      f"i.e., force the specific Farey depth.")
