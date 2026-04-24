"""
saddle_node_regularized.py

Mechanical computation of a_1(sector) and K_STAR from saddle-node
slow-manifold coefficients with Klein-bottle regularization.

Physical picture:

  Each matter sector is a mode lock on the Stern-Brocot tree.  Near the
  locked state, the local dynamics are the parabola primitive's
  saddle-node normal form:

      dx/dt = mu_sector - x^2

  The slow-manifold coefficient is tau = 1 / sqrt(mu_sector), which in
  the framework's canonical reading (item12_C_from_K_star) equals

      1 / sqrt(mu_sector) = a_1(sector)

  with mu_sector = K^2 / N_sector and N_sector the Klein-derived sector
  integer.

  This identification is tautological: a_1 K = sqrt(N) is the canonical
  parabola rotation identity, so using 1/sqrt(mu) as "a_1" just restates
  it.  Section 1 of this script verifies the tautology at K = K_STAR.

  To break the tautology, we need a from-primitives fixing of a_1 or K
  that does NOT go through PDG mass ratios.  Section 2 surveys
  primitive-integer arithmetic candidates for a_1(lep) directly.  None
  borrow from Shenker or external universality classes.

  Section 3 tries the cleanest candidate -- a_1(lep) = q_2 + 1/q_3 = 7/3
  -- as a from-primitives closure and reports the 0.56% gap, then
  searches for a small Klein-parity correction that would close it.

  Section 4 asks whether any surveyed candidate extends consistently
  across all three matter sectors under the canonical parabola rotation
  a_1(sector)^2 K^2 = N_sector.

Honest report: the survey finds no from-primitives expression that
matches a_1(lep) at PDG precision.  The cleanest candidate 7/3 is
0.56% off; the cleanest "extended" candidate involving Klein parity
reaches ~0.1% but doesn't close.  K_STAR remains PDG-anchored after
this pass.  What the computation does give is a precise catalogue of
the near-misses, which is data about which primitive combinations are
structurally natural in the framework's vocabulary.
"""

from __future__ import annotations

import math

from framework_constants import (
    D,
    K_STAR,
    M_B,
    M_C,
    M_MU,
    M_S,
    M_T,
    M_TAU,
    Q2,
    Q3,
)


# ============================================================================
# Framework targets
# ============================================================================

def a1_from_pdg(heavy: float, light: float, b1: float) -> float:
    return math.log(heavy / light) / (D * math.log(b1))


A1_LEP = a1_from_pdg(M_TAU, M_MU, 3 / 2)
A1_UP = a1_from_pdg(M_T, M_C, 8 / 5)
A1_DN = a1_from_pdg(M_B, M_S, 5 / 4)

N_LEP = Q2 ** 2       # 4
N_UP = Q3 ** 2        # 9
N_DN = Q2 ** 3 * Q3   # 24

PHI = (1 + math.sqrt(5)) / 2


def header(text: str) -> None:
    print()
    print("-" * 78)
    print(f"  {text}")
    print("-" * 78)
    print()


# ============================================================================
# Section 1 -- verify the tautology
# ============================================================================

def section_tautology() -> None:
    header("Section 1: saddle-node slow-manifold at canonical mu_sector = K^2/N")
    print("  Under the canonical item12 reading, the parabola slow-manifold")
    print("  coefficient is 1/sqrt(mu_sector) with mu_sector = K^2/N_sector.")
    print("  This gives 1/sqrt(mu) = sqrt(N)/K, which is exactly the")
    print("  identity a_1 * K = sqrt(N).  Verify it at K = K_STAR:")
    print()
    print(f"  K_STAR = {K_STAR:.10f}")
    print()
    print(f"  {'sector':<10} {'N':>4} {'mu=K^2/N':>14} "
          f"{'1/sqrt(mu)':>14} {'a_1 obs':>14} {'gap':>14}")
    print("  " + "-" * 74)
    for name, N, a1_obs in [
        ("leptons", N_LEP, A1_LEP),
        ("up-type", N_UP,  A1_UP),
        ("down-type", N_DN, A1_DN),
    ]:
        mu = K_STAR ** 2 / N
        coeff = 1 / math.sqrt(mu)
        print(f"  {name:<10} {N:>4} {mu:>14.6f} {coeff:>14.10f} "
              f"{a1_obs:>14.10f} {coeff - a1_obs:>+14.4e}")
    print()
    print("  Tautological: 1/sqrt(K^2/N) = sqrt(N)/K = a_1 by the canonical")
    print("  identity.  This path does not derive K_STAR; it restates it.")
    print()
    print("  To break the tautology, we need a from-primitives fixing of")
    print("  sqrt(N)/K (or equivalently of a_1(sector)) that does NOT")
    print("  reference PDG.  Sections 2-3 survey such fixings.")
    print()


# ============================================================================
# Section 2 -- primitive-integer candidates for a_1(lep)
# ============================================================================

def section_candidates() -> None:
    header("Section 2: primitive-integer candidates for a_1(lep) = 2.3203")
    print("  Catalogue arithmetic combinations of q_2, q_3, d, and framework")
    print("  integers (4, 9, 24, 13, 19, 35, 54) that land near 2.3203.")
    print("  None use PDG input or literature constants.")
    print()
    q2, q3, d = Q2, Q3, D
    phi = PHI

    candidates = [
        ("q_2 + 1/q_3 = 7/3",                  q2 + 1/q3),
        ("q_3 - 1/q_2 + 1/q_3^2",              q3 - 1/q2 + 1/q3**2),
        ("q_2 + (q_3-1)/q_3^2 = 2 + 2/9",      q2 + (q3-1)/q3**2),
        ("sqrt(q_2^2 + q_3^2 - 4) = sqrt(9)",  math.sqrt(q2**2 + q3**2 - 4)),
        ("sqrt(q_3 + q_2) = sqrt(5)",          math.sqrt(q3 + q2)),
        ("q_2 * (1 + 1/q_3^2)",                q2 * (1 + 1/q3**2)),
        ("q_2 + 1/q_3 - 1/(q_3^4)",            q2 + 1/q3 - 1/q3**4),
        ("q_2 + 1/q_3 - 1/(q_2*q_3)^2",        q2 + 1/q3 - 1/(q2*q3)**2),
        ("q_2 + 1/q_3 - 1/(q_2^3 * q_3)",      q2 + 1/q3 - 1/(q2**3 * q3)),
        ("q_2 + 1/q_3 - 1/(q_2*q_3*F_6)",      q2 + 1/q3 - 1/(q2*q3*13)),
        ("phi + 1/phi^2 + 1/q_2^3",            phi + 1/phi**2 + 1/q2**3),
        ("log(q_2^3 + q_3^3) / log(3/2)",      math.log(q2**3 + q3**3) / math.log(3/2)),
        ("sqrt(q_2^3 + q_3^3 / 3) ~ sqrt(19/3+...)", math.sqrt((q2**3 + q3**3) / 6.5)),
        ("2 + 1/(pi - phi)",                   2 + 1/(math.pi - phi)),
        ("q_2 + q_3/F_10",                     q2 + q3/55),
    ]

    print(f"  target: a_1(lep) observed = {A1_LEP:.10f}")
    print()
    print(f"  {'candidate':<44} {'value':>14} {'rel gap':>14}")
    print("  " + "-" * 74)
    for label, val in candidates:
        rel = (val - A1_LEP) / A1_LEP
        marker = "  <-- within 0.1%" if abs(rel) < 0.001 else ""
        print(f"  {label:<44} {val:>14.10f} {rel*100:>+11.4f}%  {marker}")
    print()


# ============================================================================
# Section 3 -- the 7/3 hypothesis and its Klein-parity correction
# ============================================================================

def section_seven_thirds() -> None:
    header("Section 3: the 7/3 hypothesis and Klein-parity corrections")
    print("  Cleanest primitive-integer candidate: a_1(lep) = q_2 + 1/q_3 = 7/3.")
    print("  Implies K_STAR = q_2 / a_1 = 2/(7/3) = 6/7.")
    print()
    a1_cand = 7/3
    K_cand = 6/7
    print(f"  a_1 candidate = 7/3 = {a1_cand:.10f}")
    print(f"  K candidate   = 6/7 = {K_cand:.10f}")
    print(f"  a_1 observed  = {A1_LEP:.10f}")
    print(f"  K_STAR canon  = {K_STAR:.10f}")
    print(f"  a_1 gap       = {a1_cand - A1_LEP:+.6e}  "
          f"({(a1_cand - A1_LEP)/A1_LEP*100:+.4f}%)")
    print(f"  K gap         = {K_cand - K_STAR:+.6e}  "
          f"({(K_cand - K_STAR)/K_STAR*100:+.4f}%)")
    print()
    print("  Both gaps are 0.56%.  Search for a structural correction that")
    print("  closes them:")
    print()

    # Required multiplicative correction
    correction_needed = A1_LEP / a1_cand
    print(f"  Required: a_1 obs / (7/3) = {correction_needed:.10f}")
    print(f"  Required: (7/3) - a_1 obs = {a1_cand - A1_LEP:.6e}")
    print()
    print("  Candidate structural corrections (Klein parity, Fibonacci squares,")
    print("  interaction-scale corrections) within 0.6% of 1:")
    print()

    corr_candidates = [
        ("1 - 1/q_3^5 = 1 - 1/243",                 1 - 1/Q3**5),
        ("1 - 1/(q_2^3 * q_3^2) = 1 - 1/72",        1 - 1/(Q2**3 * Q3**2)),
        ("1 - 1/(q_2^2 * q_3^3)",                   1 - 1/(Q2**2 * Q3**3)),
        ("1 - 1/(q_2^5 * q_3) = 1 - 1/96",          1 - 1/(Q2**5 * Q3)),
        ("1 - 1/(q_2*q_3*F_9) = 1 - 1/(6*34)",      1 - 1/(Q2*Q3*34)),
        ("1 - 1/F_11^2 = 1 - 1/7921",               1 - 1/89**2),
        ("1 - 1/|F_7|^2 = 1 - 1/361",               1 - 1/19**2),
        ("1 - 1/(q_2*|F_7|*q_3)",                   1 - 1/(Q2*19*Q3)),
    ]

    print(f"  {'correction candidate':<44} {'value':>14} "
          f"{'matches target?':>18}")
    print("  " + "-" * 78)
    for label, val in corr_candidates:
        gap = val - correction_needed
        print(f"  {label:<44} {val:>14.10f} {gap:>+18.2e}")
    print()
    print("  No correction in the framework alphabet matches the required")
    print("  0.56% shift.  The 7/3 hypothesis is close but not a structural")
    print("  closure; the missing correction does not sit at a single")
    print("  framework integer's inverse square.")
    print()


# ============================================================================
# Section 4 -- cross-sector test of the best candidates
# ============================================================================

def section_cross_sector() -> None:
    header("Section 4: cross-sector extension under a_1(sector) K = sqrt(N)")
    print("  Under the canonical parabola rotation a_1(sector) K = sqrt(N),")
    print("  a from-primitives K_STAR makes ALL three sectors satisfy")
    print()
    print("      a_1(lep)  K = 2   (= sqrt(q_2^2))")
    print("      a_1(up)   K = 3   (= sqrt(q_3^2))")
    print("      a_1(down) K = 2 sqrt(6)  (= sqrt(q_2^3 q_3))")
    print()
    print("  If we FIX K from primitives (e.g. K = 6/7), the implied")
    print("  a_1(sector) values for each sector are:")
    print()
    K_cands = [
        ("K_STAR canonical", K_STAR),
        ("6/7 (from 7/3)",   6/7),
        ("2/phi^2 + 0",       2/PHI**2),
        ("sqrt(3)/2 ~ cos(30)", math.sqrt(3)/2),
        ("1 - 1/(q_2^3 - 1)",  1 - 1/(Q2**3 - 1)),
        ("1 - 1/|F_7|/q_2 ~ 1-1/38", 1 - 1/(19 * Q2)),
    ]
    print(f"  {'K source':<28} {'K':>12} {'a_1(lep)':>12} "
          f"{'a_1(up)':>12} {'a_1(dn)':>12}")
    print("  " + "-" * 78)
    for label, K in K_cands:
        a1_lep = 2 / K
        a1_up = 3 / K
        a1_dn = math.sqrt(24) / K
        print(f"  {label:<28} {K:>12.8f} {a1_lep:>12.6f} "
              f"{a1_up:>12.6f} {a1_dn:>12.6f}")
    print()
    print(f"  a_1 observed (PDG):      {A1_LEP:12.6f} {A1_UP:12.6f} "
          f"{A1_DN:12.6f}")
    print()
    print("  Under ANY K that's not the canonical K_STAR, at least one sector")
    print("  misses by > 0.1%.  The canonical K_STAR is the unique value that")
    print("  makes all three sectors close simultaneously -- which is exactly")
    print("  the statement of the joint matter-sector fit.  From a primitives-")
    print("  first standpoint, this says K_STAR is the VALUE that makes the")
    print("  parabola rotation self-consistent across the Klein-derived sector")
    print("  integers; it is not independently computable from primitives")
    print("  unless we can derive at least ONE a_1(sector) from primitives,")
    print("  and then propagate to K via the rotation.")
    print()


# ============================================================================
# Section 5 -- what this tells us
# ============================================================================

def section_conclusion() -> None:
    header("Section 5: what the computation actually shows")
    print("""\
  1. The saddle-node slow-manifold coefficient at mu_sector = K^2/N is
     tautologically equal to a_1(sector) under the canonical item12
     reading.  It does not derive K_STAR; it restates it.

  2. A from-primitives fixing has to come from OUTSIDE the identity
     a_1 K = sqrt(N).  The natural external condition would be to
     pin at least ONE of {a_1(lep), K_STAR} from framework primitives
     directly, and then use the parabola rotation to propagate to the
     other sectors.

  3. The cleanest primitive-integer candidate is a_1(lep) = q_2 + 1/q_3
     = 7/3, giving K = 6/7.  Both are 0.56% off the canonical values.
     No small correction in the framework alphabet closes the 0.56%
     gap (Section 3 exhausted the natural candidates at this depth).

  4. At the canonical parabola rotation a_1(sector) K = sqrt(N), the
     K_STAR value is unique: only K = K_STAR makes all three sectors
     close simultaneously.  Any other K misses at least one sector by
     more than 0.1%.  This is already known from item12_K_star_closure
     but the mechanical re-derivation here confirms it: the rotation
     itself is a primitive-level structure (parabola + Klein-derived
     integers), but the CALIBRATION of that rotation is set by one
     observable per sector, and we have three observables (m_tau/m_mu,
     m_t/m_c, m_b/m_s) agreeing at chi^2/dof = 0.06.

  5. The physical picture developed in the discourse (saddle-node
     slow manifolds at tongue edges, Klein-bottle regularization of
     the logarithmic dwell-time divergence) is correct as a
     description of what a_1(sector) IS physically, but the
     regularization does not provide a new constraint on K -- it
     just confirms the tautology by a different route.

  The honest conclusion from this mechanical pass: K_STAR is not
  derivable from the saddle-node / parabola-rotation / Klein-parity
  structure alone at the current level of the framework's
  construction.  The computation is self-consistent at K_STAR but
  does not pick K_STAR out uniquely without one external input.

  What this suggests methodologically:

    - The from-primitives derivation of K_STAR, if it exists, must
      come from a piece of the framework's topology that we have
      not yet put into the computation.  The obvious candidates are
      (a) the Klein bottle's genus/Euler characteristic relation,
      (b) the SL(2,R) volume or Bergman kernel at the Fibonacci
      convergents, (c) a variational principle on the parabola
      primitive that we have not yet formulated.

    - Or K_STAR is fundamentally an observational anchor, like
      v = 246 GeV is the dimensionful scale, and the framework's
      "no fitted factors" claim should be sharpened to "zero
      dimensionless parameters plus one dimensionless anchor
      K_STAR plus one dimensionful scale v".  This would be a
      weaker claim than the framework currently advertises but
      would be consistent with everything actually demonstrated.

  The mechanical computation makes the gap precise.  Whether to
  pursue (a), (b), (c), or accept K_STAR as an anchor is the next
  research decision.
""")


def main() -> None:
    print("=" * 78)
    print("  SADDLE-NODE REGULARIZATION: K_STAR from primitives?")
    print("=" * 78)
    section_tautology()
    section_candidates()
    section_seven_thirds()
    section_cross_sector()
    section_conclusion()


if __name__ == "__main__":
    main()
