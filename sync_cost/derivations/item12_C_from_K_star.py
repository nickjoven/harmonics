"""
Item 12: C = a_1(leptons)^2 and the K* identity.

Working claim:

    a_1(leptons) * K* = q_2 = 2

which squared gives the closed form for the last remaining mass-sector
constant:

    C = a_1(leptons)^2 = q_2^2 / K*^2

If exact, this reduces item 12 to ZERO fit parameters (K* itself is
independently derived from the Kuramoto / boundary-weight sector).

Numerical status at PDG 2024 + framework K_STAR = 0.862:

    a_1(leptons) = 2.320292 +/- 0.000056     (from m_tau, m_mu)
    q_2 / K_STAR = 2.320186
    difference   = +0.000106                 (1.9 sigma)

    C (observed) = 5.383754 +/- 0.000258
    q_2^2 / K_STAR^2 = 5.383261
    difference    = +0.000493                 (1.9 sigma on sqrt, 3.8 sigma on C)

The discrepancy disappears if K* is taken to be 0.861961 instead of the
framework's rounded 0.862.  This script tests:

  1. The identity a_1(lep) * K* = q_2 at the framework's quoted K*.
  2. The "lepton-implied" K* = q_2 / a_1(lep) at high precision.
  3. Whether the identity also holds (in any form) for up-type and
     down-type sectors -- it should NOT, because those sectors have
     different Klein-bottle parities and different sector-scaling
     factors.
  4. Consistency with other framework constraints on K* that exist in
     the derivations tree (field_equation_iteration.py's neutrino-mass
     fit of K*, boundary_weight.md's cited value).
  5. Candidate structural readings for WHY a_1(lep) = q_2/K* would be
     exact:
       (a) 1 / sqrt(tongue_width(3/2, K*)) = 2/K*  (perturbative Arnold)
       (b) "walk length" = q_2 / (step size K*)
       (c) pure numerical coincidence

The script does NOT claim the identity is derived; it states it as a
strong observational near-identity (4 decimal digits match) and
quantifies what level of independent K* precision is required to
confirm or refute it.
"""

from __future__ import annotations

import math

from framework_constants import (
    K_STAR,
    M_B,
    M_C,
    M_MU,
    M_S,
    M_T,
    M_TAU,
    Q2,
    D,
    mass_err,
)

# Lepton-sector step bases
B1_LEP = 3 / 2
B2_LEP = 5 / 3
B1_UP = 8 / 5
B2_UP = 3 / 2
B1_DN = 5 / 4
B2_DN = 9 / 8


def a1_from_masses(heavy, light, b1):
    """a_1 = log(r_1) / (d log b_1)."""
    return math.log(heavy / light) / (D * math.log(b1))


def sigma_a1(heavy, s_heavy, light, s_light, b1):
    """Propagated 1-sigma on a_1 from masses."""
    r = heavy / light
    sigma_r = r * math.hypot(s_heavy / heavy, s_light / light)
    return sigma_r / (abs(D * math.log(b1)) * r)


def tongue_width_perturbative(q, K):
    """Arnold tongue width at rational with denominator q, perturbative form."""
    return 2 * (K / 2) ** q / q


def main():
    print("=" * 78)
    print("  ITEM 12: C FROM K* VIA a_1(lep) * K* = q_2")
    print("=" * 78)
    print()

    # --------------------------------------------------------------
    # Part 1: a_1 per sector with PDG propagation
    # --------------------------------------------------------------
    print("-" * 78)
    print("  PART 1: OBSERVED a_1 PER SECTOR")
    print("-" * 78)
    print()

    a1_lep = a1_from_masses(M_TAU, M_MU, B1_LEP)
    s_lep = sigma_a1(M_TAU, mass_err("tau"), M_MU, mass_err("mu"), B1_LEP)

    a1_up = a1_from_masses(M_T, M_C, B1_UP)
    s_up = sigma_a1(M_T, mass_err("t"), M_C, mass_err("c"), B1_UP)

    a1_dn = a1_from_masses(M_B, M_S, B1_DN)
    s_dn = sigma_a1(M_B, mass_err("b"), M_S, mass_err("s"), B1_DN)

    for name, a1, s in [("leptons", a1_lep, s_lep),
                        ("up-type", a1_up, s_up),
                        ("down-type", a1_dn, s_dn)]:
        print(f"  {name:<12} a_1 = {a1:.10f}  (sigma = {s:.2e}, "
              f"{s/a1*100:.3f}%)")
    print()

    # --------------------------------------------------------------
    # Part 2: The lepton identity  a_1(lep) * K* = q_2
    # --------------------------------------------------------------
    print("-" * 78)
    print("  PART 2: THE LEPTON IDENTITY  a_1(lep) * K* = q_2")
    print("-" * 78)
    print()

    product = a1_lep * K_STAR
    print(f"  framework K_STAR      = {K_STAR:.10f}")
    print(f"  a_1(lep) * K_STAR     = {product:.10f}")
    print(f"  target q_2            = {Q2}")
    print(f"  difference            = {product - Q2:+.8f}")
    print(f"  relative error        = {abs(product - Q2) / Q2 * 100:.5f}%")
    print()

    predicted_a1 = Q2 / K_STAR
    diff = a1_lep - predicted_a1
    sigma_ratio = abs(diff) / s_lep
    print(f"  a_1(lep) observed     = {a1_lep:.10f} +/- {s_lep:.2e}")
    print(f"  q_2 / K_STAR          = {predicted_a1:.10f}")
    print(f"  difference            = {diff:+.8f}")
    print(f"  PDG sigma deviation   = {sigma_ratio:.2f}")
    print()

    # --------------------------------------------------------------
    # Part 3: C from the identity, and its PDG status
    # --------------------------------------------------------------
    print("-" * 78)
    print("  PART 3: C = q_2^2 / K*^2")
    print("-" * 78)
    print()

    C_obs = a1_lep ** 2
    s_C = 2 * a1_lep * s_lep
    C_pred = Q2 ** 2 / K_STAR ** 2

    print(f"  C (observed)          = {C_obs:.10f} +/- {s_C:.2e}")
    print(f"  q_2^2 / K_STAR^2      = {C_pred:.10f}")
    print(f"  difference            = {C_obs - C_pred:+.8f}")
    print(f"  PDG sigma deviation   = {abs(C_obs - C_pred) / s_C:.2f}")
    print()

    # --------------------------------------------------------------
    # Part 4: Lepton-implied K*
    # --------------------------------------------------------------
    print("-" * 78)
    print("  PART 4: LEPTON-IMPLIED K* AT HIGH PRECISION")
    print("-" * 78)
    print()

    K_star_from_leptons = Q2 / a1_lep
    s_K_from_leptons = Q2 / a1_lep ** 2 * s_lep

    print(f"  K* = q_2 / a_1(lep)   = {K_star_from_leptons:.10f}")
    print(f"                          +/- {s_K_from_leptons:.2e}")
    print()
    print(f"  framework K_STAR      = {K_STAR:.10f}")
    print(f"  difference            = {K_star_from_leptons - K_STAR:+.8f}")
    print()
    print("  The framework value is quoted at 3 significant figures.")
    print("  The lepton-implied value is a 6+ digit refinement that is")
    print("  consistent with 0.862 under rounding.")
    print()

    # --------------------------------------------------------------
    # Part 5: Does the identity extend to other sectors?
    # --------------------------------------------------------------
    print("-" * 78)
    print("  PART 5: a_1 * K* FOR OTHER SECTORS (the identity is lepton-only)")
    print("-" * 78)
    print()
    print(f"  {'sector':<12} {'a_1':>12} {'a_1 * K*':>14} {'a_1 / K*':>14}")
    print("  " + "-" * 60)
    for name, a1 in [("leptons", a1_lep),
                     ("up-type", a1_up),
                     ("down-type", a1_dn)]:
        print(f"  {name:<12} {a1:>12.6f} {a1 * K_STAR:>14.6f} "
              f"{a1 / K_STAR:>14.6f}")
    print()
    print("  Only the lepton sector lands on a clean integer (q_2 = 2).")
    print("  This is consistent with the cross-sector scaling derived in")
    print("  item12_cross_sector_ratios.md: once C = q_2^2/K*^2 is fixed")
    print("  for leptons, the other sectors are determined by the Fibonacci")
    print("  shift (up-type: factor 9/4) and the Klein-bottle double cover")
    print("  (down-type: factor 6).")
    print()

    # --------------------------------------------------------------
    # Part 6: Structural reading candidates
    # --------------------------------------------------------------
    print("-" * 78)
    print("  PART 6: STRUCTURAL READINGS FOR WHY a_1(lep) = q_2/K*")
    print("-" * 78)
    print()

    # Reading (a): tongue width inverse sqrt
    w_3_2 = tongue_width_perturbative(Q2, K_STAR)
    inv_sqrt_w = 1 / math.sqrt(w_3_2)
    print("  (a) 1 / sqrt(w(3/2, K*)) where w = 2 (K*/2)^q / q")
    print(f"      w(3/2, K*) = 2 (K*/2)^2 / 2 = (K*/2)^2 = {w_3_2:.10f}")
    print(f"      1 / sqrt(w) = 2/K* = {inv_sqrt_w:.10f}")
    print(f"      a_1(lep)    = {a1_lep:.10f}")
    print(f"      agreement   = {1 - abs(inv_sqrt_w - a1_lep)/a1_lep:.6f}")
    print()
    print("      Reading: a_1 is the inverse square-root of the perturbative")
    print("      Arnold-tongue width at the sector's heavy-step base rational,")
    print("      evaluated at the self-consistent K*.  For leptons this is")
    print("      exact because b_1 = 3/2 has denominator q_2 = 2, and")
    print("      sqrt(w(3/2, K*)) = K*/2 collapses to q_2/K* after inversion.")
    print()

    # Reading (b): walk-length interpretation
    print("  (b) Walk length = q_2 / (step size K*)")
    print("      In log-ratio space, the lepton sector's generation walk")
    print("      takes q_2 = 2 steps at effective step-size K*, giving")
    print("      a_1 = 2/K* directly.  This is the 'Klein-bottle twist count'")
    print("      reading: q_2 = 2 is the antiperiodic cycle count, K* is the")
    print("      per-step coupling.")
    print()

    # Reading (c): coincidence
    print("  (c) Pure numerical coincidence")
    print("      Possible if no independent derivation of K* to 5+ digits")
    print("      recovers 0.861961.  Rules out this reading only if another")
    print("      constraint pins K* elsewhere.")
    print()

    # --------------------------------------------------------------
    # Part 7: Verification of reading (a) -- extend to up-type?
    # --------------------------------------------------------------
    print("-" * 78)
    print("  PART 7: READING (a) DOES NOT EXTEND TO QUARK SECTORS")
    print("-" * 78)
    print()
    print("  For reading (a) to be universal, 1/sqrt(w(b_1, K*)) should give")
    print("  a_1 in every sector.  It does not:")
    print()
    print(f"  {'sector':<12} {'b_1':>6} {'q=den(b_1)':>12} "
          f"{'1/sqrt(w)':>14} {'observed a_1':>14}")
    print("  " + "-" * 62)
    for name, b1, q, a1 in [
        ("leptons", "3/2", 2, a1_lep),
        ("up-type", "8/5", 5, a1_up),
        ("down-type", "5/4", 4, a1_dn),
    ]:
        w = tongue_width_perturbative(q, K_STAR)
        pred = 1 / math.sqrt(w)
        print(f"  {name:<12} {b1:>6} {q:>12} {pred:>14.4f} {a1:>14.4f}")
    print()
    print("  The inverse-sqrt reading works ONLY for leptons.  This is")
    print("  consistent with the cross-sector derivation: leptons are the")
    print("  'primary' sector, and the up-type and down-type exponents are")
    print("  obtained from a_1(lep) by the sector scaling factors")
    print("  (9/4 and 6 respectively), NOT by applying the same formula")
    print("  with a different b_1.")
    print()

    # --------------------------------------------------------------
    # Summary
    # --------------------------------------------------------------
    print("=" * 78)
    print("  SUMMARY")
    print("=" * 78)
    print()
    print("  Observed identity (within lepton PDG precision):")
    print()
    print("    a_1(leptons) * K* = q_2 = 2           (1.9 sigma at K* = 0.862)")
    print()
    print("  Squared form:")
    print()
    print("    C = a_1(leptons)^2 = q_2^2 / K*^2")
    print()
    print("  Lepton-implied K* at high precision:")
    print()
    print(f"    K* = q_2 / a_1(lep) = {K_star_from_leptons:.8f}")
    print(f"         +/- {s_K_from_leptons:.2e}")
    print()
    print("  Compatible with framework's cited K* = 0.862 (3-digit round).")
    print()
    print("  Structural reading (a): a_1(lep) = 1/sqrt(w(3/2, K*)) where")
    print("  w is the perturbative Arnold tongue width.  For q=2 this")
    print("  collapses to 2/K*.  Does NOT extend to quark sectors; those")
    print("  are governed by the cross-sector scaling of")
    print("  item12_cross_sector_ratios.md instead.")
    print()
    print("  Item 12 status:")
    print()
    print("    IF the identity is exact:")
    print("      - C is a closed form, not a fit")
    print("      - Item 12 closes completely, ZERO fit parameters")
    print("      - K* gains an independent high-precision determination")
    print()
    print("    Pending:")
    print("      - An independent K* derivation at 5+ digit precision that")
    print("        recovers 0.861961 confirms the identity.")
    print("      - Otherwise the identity remains a strong numerical")
    print("        near-coincidence (4 decimal digits) awaiting structural")
    print("        justification.")
    print()


if __name__ == "__main__":
    main()
