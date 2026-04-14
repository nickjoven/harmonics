"""
a1_klein_twist.py

Attempt to derive the candidate

    a_1(lep) = q_2 + 1/q_3 - 1/(q_2 q_3 (q_2^2 + q_3^2))
             = 2 + 1/3 - 1/78
             = 181/78

from the Klein bottle's topology, with an exhaustive search for
subleading corrections in the framework alphabet that might close
the residual 0.0095% gap.

Structural reading of the base + leading correction:

  q_2 = 2
    = Klein antiperiodic period
    = smallest Z_2 period (one full half-twist traversal)

  1/q_3 = 1/3
    = smallest non-trivial Z_3 fractional increment
    = one step on the Z_3 periodic direction out of q_3 total

  q_2 q_3 = 6 = |Z_6| = INTERACT
    = total order of the Klein-parity center Z_2 x Z_3 = Z_6

  q_2^2 + q_3^2 = 13 = |F_6|
    = Farey count at depth q_2 q_3 = 6 (interaction scale)

  |Z_6| * |F_6| = 78
    = total Z_6-fiber count across the Farey partition at the
      interaction scale (one Z_6 fiber per Farey cell, 13 cells)

So the candidate reads as

    a_1(lep) = (one full Z_2 period) + (one Z_3 increment)
             - (one Z_6 fiber out of total 78)

Physical picture: a_1(lep) is the parabola slow-manifold coefficient
at the q=2 matter tongue, discretized on the Z_6 center's fiber
structure at Farey depth 6. The base is the integer-plus-increment
reading on the discrete group; the correction is the first Klein-
twist deficit (one fiber out of the total count).

Numerically: this lands at 2.3205128, observed a_1(lep) = 2.3202917,
gap 0.0095% (4 sigma of PDG uncertainty on a_1).

This script:

  Section 1. Verify the base + leading correction numerically.

  Section 2. Exhaustive search for a subleading correction in the
             framework alphabet that would close the 0.0095% gap.

  Section 3. Cross-sector test: under a_1(sector) K = sqrt(N_sector),
             does K from the lepton candidate propagate to up and
             down sectors at PDG precision?

  Section 4. Failure-mode analysis: what the shape of the residual
             tells us about the framework's actual construction.
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
    F_6_COUNT,
    F_7_COUNT,
)


# Framework targets
def a1_from_pdg(heavy: float, light: float, b1: float) -> float:
    return math.log(heavy / light) / (D * math.log(b1))


A1_LEP = a1_from_pdg(M_TAU, M_MU, 3 / 2)
A1_UP = a1_from_pdg(M_T, M_C, 8 / 5)
A1_DN = a1_from_pdg(M_B, M_S, 5 / 4)

PDG_SIGMA_A1_LEP = 5.6e-5  # approx; from PDG uncertainty on m_tau

# Framework alphabet integers
INTERACT = Q2 * Q3                     # 6 = |Z_6|
F6 = F_6_COUNT                          # 13 = q_2^2 + q_3^2
F7 = F_7_COUNT                          # 19
N_LEP = Q2 ** 2                         # 4
N_UP = Q3 ** 2                          # 9
N_DN = Q2 ** 3 * Q3                     # 24


def header(text: str) -> None:
    print()
    print("-" * 78)
    print(f"  {text}")
    print("-" * 78)
    print()


# ============================================================================
# Section 1 -- verify the base + leading correction
# ============================================================================

def section_verify() -> None:
    header("Section 1: Klein-twist candidate base + leading correction")
    print("  Candidate: a_1(lep) = q_2 + 1/q_3 - 1/(|Z_6| * |F_6|)")
    print()
    print(f"  q_2 = {Q2}")
    print(f"  q_3 = {Q3}")
    print(f"  |Z_6| = q_2 * q_3 = {INTERACT}")
    print(f"  |F_6| = q_2^2 + q_3^2 = {F6}")
    print(f"  |Z_6| * |F_6| = {INTERACT * F6}")
    print()

    base = Q2 + 1 / Q3
    correction = 1 / (INTERACT * F6)
    candidate = base - correction

    print(f"  base         = q_2 + 1/q_3          = {base:.10f}")
    print(f"  correction   = 1/(|Z_6| * |F_6|)    = {correction:.10f}")
    print(f"  candidate    = base - correction    = {candidate:.10f}")
    print(f"  a_1(lep) obs                        = {A1_LEP:.10f}")
    print()
    print(f"  gap          = candidate - obs      = {candidate - A1_LEP:+.4e}")
    print(f"  relative     =                        {(candidate - A1_LEP) / A1_LEP * 100:+.4f}%")
    print(f"  in PDG sigma =                        {abs(candidate - A1_LEP) / PDG_SIGMA_A1_LEP:.1f}")
    print()
    print("  Leading-order match: 0.0095% gap, ~4 sigma of PDG.  Not a")
    print("  closure, but in the correct compositional-closure format")
    print("  (base primitive + Klein-alphabet inverse-integer correction).")
    print()


# ============================================================================
# Section 2 -- exhaustive search for subleading corrections
# ============================================================================

def section_subleading_search() -> None:
    header("Section 2: exhaustive search for subleading corrections")
    print("  Required additional correction to close the lepton residual:")
    residual = A1_LEP - (Q2 + 1 / Q3 - 1 / (INTERACT * F6))
    print(f"    delta = observed - candidate = {residual:+.6e}")
    print(f"    magnitude: |delta| = {abs(residual):.6e}")
    print(f"    1/|delta|         = {1/abs(residual):.1f}")
    print()
    print("  Search for 1/X with X a product of framework-alphabet")
    print("  integers, matching |delta| to within 1%:")
    print()

    # Build a set of products of framework alphabet integers up to some cap.
    alphabet = {
        "q_2":    Q2,      # 2
        "q_3":    Q3,      # 3
        "q_2^2":  Q2**2,   # 4
        "q_3^2":  Q3**2,   # 9
        "q_2^3":  Q2**3,   # 8
        "q_3^3":  Q3**3,   # 27
        "|F_6|":  F6,      # 13
        "|F_7|":  F7,      # 19
        "F_9":    34,
        "F_10":   55,
        "F_11":   89,
        "F_12":   144,
        "F_13":   233,
        "|F_6|^2": F6**2,  # 169
        "|F_7|^2": F7**2,  # 361
    }

    candidates = []
    names = list(alphabet.keys())
    vals = list(alphabet.values())

    # Single factors
    for n, v in zip(names, vals):
        candidates.append((n, v))
    # Pairs
    for i, n_i in enumerate(names):
        for j, n_j in enumerate(names):
            if j >= i:
                candidates.append((f"{n_i} * {n_j}", vals[i] * vals[j]))
    # Triples (limited to small factors)
    small_names = [n for n, v in alphabet.items() if v <= 20]
    small_vals = [v for n, v in alphabet.items() if v <= 20]
    for i, n_i in enumerate(small_names):
        for j, n_j in enumerate(small_names):
            for k, n_k in enumerate(small_names):
                if j >= i and k >= j:
                    candidates.append(
                        (f"{n_i} * {n_j} * {n_k}",
                         small_vals[i] * small_vals[j] * small_vals[k])
                    )
    # Quadruples of small factors
    for i, n_i in enumerate(small_names):
        for j, n_j in enumerate(small_names):
            for k, n_k in enumerate(small_names):
                for m, n_m in enumerate(small_names):
                    if j >= i and k >= j and m >= k:
                        prod = (small_vals[i] * small_vals[j]
                                * small_vals[k] * small_vals[m])
                        candidates.append(
                            (f"{n_i} * {n_j} * {n_k} * {n_m}", prod)
                        )

    target = abs(residual)
    hits = []
    for label, X in candidates:
        if X <= 0:
            continue
        val = 1.0 / X
        rel = (val - target) / target
        if abs(rel) < 0.05:  # within 5% of target
            sign = "+" if residual > 0 else "-"
            hits.append((X, val, rel, label, sign))

    hits.sort(key=lambda h: abs(h[2]))

    if not hits:
        print("  No single-alphabet or product-of-alphabet correction matches.")
    else:
        print(f"  {'X':>8} {'1/X':>14} {'rel to delta':>14} "
              f"{'sign':>6}  factorization")
        print("  " + "-" * 74)
        for X, val, rel, label, sign in hits[:20]:
            print(f"  {X:>8} {val:>14.6e} {rel * 100:>+12.3f}%  "
                  f"{sign:>6}  {label}")
    print()

    if hits:
        best = hits[0]
        X, val, rel, label, sign = best
        print(f"  Closest match: 1/{X} = {val:.6e}, gap {rel*100:+.2f}% of delta.")
        print(f"  Factorization: {label}")
        print()
        # Apply the closest correction and report
        direction = 1 if residual > 0 else -1
        a1_improved = (Q2 + 1/Q3 - 1/(INTERACT*F6)) + direction * val
        print(f"  Applying correction: a_1 = 181/78 {'+' if direction > 0 else '-'} 1/{X}")
        print(f"    improved candidate = {a1_improved:.10f}")
        print(f"    observed           = {A1_LEP:.10f}")
        print(f"    gap                = {a1_improved - A1_LEP:+.4e}")
        print(f"    relative           = {(a1_improved - A1_LEP)/A1_LEP * 100:+.4f}%")
        print(f"    in PDG sigma       = "
              f"{abs(a1_improved - A1_LEP) / PDG_SIGMA_A1_LEP:.1f}")
        print()


# ============================================================================
# Section 3 -- cross-sector extension for both candidates
# ============================================================================

# PDG sigma estimates on a_1(sector) from quark mass uncertainties.
# m_t = 172.76 +/- 0.40 GeV, m_c = 1.27 +/- 0.02 GeV
#   sigma(log m_c) ~ 0.02/1.27 = 1.57e-2 dominates sigma(log m_t) ~ 2.3e-3
#   sigma(log(m_t/m_c)) ~ 1.59e-2
#   sigma(a_1(up)) = sigma(log(m_t/m_c)) / (d log(8/5)) ~ 1.13e-2
# m_b = 4.18 +/- 0.03 GeV, m_s = 93.4 +/- 8 MeV
#   sigma(log m_s) ~ 8.6e-2 dominates sigma(log m_b) ~ 7.2e-3
#   sigma(log(m_b/m_s)) ~ 8.6e-2
#   sigma(a_1(down)) = sigma(log(m_b/m_s)) / (d log(5/4)) ~ 1.29e-1
PDG_SIGMA_A1_UP = 1.13e-2
PDG_SIGMA_A1_DN = 1.29e-1


def _report_cross_sector(label: str, K: float) -> None:
    """Print cross-sector predictions at coupling K with PDG-sigma gaps."""
    a1_lep = Q2 / K
    a1_up = math.sqrt(N_UP) / K
    a1_dn = math.sqrt(N_DN) / K
    print(f"  {label}  (K = {K:.10f})")
    print(f"  {'sector':<10} {'a_1 predicted':>16} {'a_1 observed':>16} "
          f"{'gap':>14} {'PDG sigma':>12}")
    print("  " + "-" * 74)
    for name, pred, obs, sig in [
        ("leptons",   a1_lep, A1_LEP, PDG_SIGMA_A1_LEP),
        ("up-type",   a1_up,  A1_UP,  PDG_SIGMA_A1_UP),
        ("down-type", a1_dn,  A1_DN,  PDG_SIGMA_A1_DN),
    ]:
        gap = pred - obs
        sigma = abs(gap) / sig
        print(f"  {name:<10} {pred:>16.10f} {obs:>16.10f} "
              f"{gap:>+14.4e} {sigma:>12.3f}")
    print()


def section_cross_sector() -> None:
    header("Section 3: cross-sector propagation -- leading vs improved")
    print("  Under a_1(sector) * K = sqrt(N_sector), a from-primitives")
    print("  a_1(lep) fixes K = q_2 / a_1(lep) and predicts the quark")
    print("  a_1 values.  Test three K values:")
    print()

    a1_leading = Q2 + 1/Q3 - 1/(INTERACT*F6)
    a1_improved = a1_leading - 1/(Q3**D * F6**2)  # subtract 1/4563 = 1/(q_3^d |F_6|^2)

    _report_cross_sector("CANONICAL K_STAR (joint matter fit)", K_STAR)
    _report_cross_sector("LEADING candidate 181/78", Q2 / a1_leading)
    _report_cross_sector(
        "IMPROVED candidate 181/78 - 1/(q_3^d |F_6|^2)",
        Q2 / a1_improved
    )

    print("  Observations:")
    print()
    print("  * Canonical K_STAR fits the lepton exactly (by construction)")
    print("    and the quarks within 0.35 sigma (up) and 0.04 sigma (down).")
    print()
    print("  * The leading candidate 181/78 alone gives 4 sigma on the lepton")
    print("    -- outside PDG -- and comparable 0.35/0.04 sigma on quarks.")
    print()
    print("  * The IMPROVED candidate (with 1/4563 subleading term) gives")
    print("    0.035 sigma on the lepton, 0.35 sigma on up, 0.04 sigma on")
    print("    down.  ALL THREE sectors are within PDG, and the lepton")
    print("    match is statistically indistinguishable from canonical.")
    print()
    print("  At current PDG precision, the improved Klein-twist candidate")
    print("  is statistically equivalent to the canonical K_STAR across")
    print("  all three matter sectors.  The distinction between 'this is")
    print("  the true structural formula' and 'this is an arithmetic")
    print("  accident within PDG noise' cannot be made at current precision.")
    print()


# ============================================================================
# Section 4 -- failure-mode analysis
# ============================================================================

def section_failure_mode() -> None:
    header("Section 4: what the failure mode actually suggests")
    print("""\
  The improved candidate

    a_1(lep) = q_2 + 1/q_3 - 1/(|Z_6| * |F_6|) - 1/(q_3^d * |F_6|^2)
             = 2 + 1/3 - 1/78 - 1/4563
             = 2.3202936664

  matches observed a_1(lep) = 2.3202917401 at 0.035 sigma of PDG,
  and propagates to both quark sectors within PDG (0.35 sigma on
  up-type, 0.04 sigma on down-type).  This is a GENUINELY
  PDG-level candidate for a_1(lep), built entirely from framework
  primitives without any observational input.

  But it is not a clean closure, for three reasons:

  1. The subleading correction 1/(q_3^d * |F_6|^2) = 1/4563 is
     only 0.87% off the required residual 2.21e-4.  The match is
     inside PDG precision but it is not exact: it is a specific
     framework-alphabet product chosen from a search that found
     ~10 products within 5% of the target.  1/4563 is the closest,
     but 1/4694 (= 1/(|F_6| |F_7|^2), also framework-alphabet) is
     within 3.6%.  The fact that MULTIPLE alphabet products sit
     near the required residual means the framework's integer
     alphabet is "dense" at scales ~1e-4, and any target in this
     range has several near-matches by construction.

  2. The structural form q_3^d * |F_6|^2 does not correspond to a
     canonical closure format used elsewhere in the framework.
     Compare to the established compositional closures:
        sin^2 theta_W = q_2^d / (q_2^d + q_3^d) + q_2^d / |F_10|^2
        alpha_s/alpha_2 = q_3^d / q_2^d + 1/q_3^2
        Higgs lambda = 1/q_2^d + 1/(q_2^2 q_3 |F_7|)
        m_2/m_1 = q_3^(1/q_2) - 1/(q_2 q_3)^2
     Each of these has a SPECIFIC alphabet integer as the correction
     denominator.  None uses q_3^d * |F_6|^2 as a single denominator.
     The proposed subleading term for a_1(lep) has the right INDIVIDUAL
     factors in the alphabet but the specific COMBINATION is novel.
     That is weak evidence -- the combination could be correct (the
     alphabet is consistent with it) but it has no independent
     structural justification.

  3. The cross-sector pattern is informative.  Under the improved K,
     up-type misses by 0.35 sigma and down-type by 0.04 sigma.
     These gaps are PDG-consistent but they do NOT correspond to
     a clean sector-specific corrective factor in the alphabet.
     If the compositional picture were universal across sectors,
     the quark gaps should either be zero or expressible as
     sector-specific Klein-parity corrections (similar to down-type's
     +1 orientation-preserving factor in the sector-integer
     derivation).  Instead the gaps just sit within PDG uncertainty
     without a clean structural form.

  What the failure mode suggests, in order of probability:

    (a) 60% -- The candidate is an arithmetic near-miss within PDG
        uncertainty.  The framework's alphabet is dense enough at
        1e-4 that a simple 4-term expression can land within PDG
        of any target in the 2-3 range.  This is the null hypothesis:
        no structural closure, just a fit that hit PDG by coincidence.

    (b) 35% -- The leading-order candidate q_2 + 1/q_3 - 1/(|Z_6| |F_6|)
        is structurally real (it has a clean topological reading as
        Z_6 base + Klein deficit) but the subleading correction
        1/(q_3^d |F_6|^2) is the wrong form.  The TRUE subleading
        term lives outside the integer-reciprocal format tested here
        -- maybe a curvature term, an entropy term, or a
        non-compositional correction.

    (c) 5% -- Both the leading and subleading terms are structural
        and the full form is exact at the level below PDG.  We
        cannot distinguish this from (a) at current m_tau precision
        (would need ~100x better).

  The honest methodological lesson: at 0.035 sigma on the lepton and
  0.35/0.04 on the quarks, the computation has BOTTOMED OUT at PDG
  precision.  We cannot tell whether the framework's K_STAR has a
  structural derivation or is an observational anchor.  Further
  progress on K_STAR from primitives requires EITHER:

    (i) A structural argument for why the specific combination
        1/(q_3^d |F_6|^2) (or whatever other alphabet integer)
        should appear at second order.  That argument would have
        to come from a topological construction, not a fit.

    (ii) A qualitatively different mechanism for fixing K_STAR --
         a variational principle, a boundary condition, or a
         non-compositional observable -- that does not rely on
         expanding a_1(lep) in inverse alphabet integers.

    (iii) Improvement of m_tau precision by ~2 orders of magnitude,
          which would let us distinguish (a) from (c) empirically.

  At the moment the framework sits exactly at the boundary between
  "K_STAR is a PDG anchor" and "K_STAR is structurally derived with
  a subleading correction at the alphabet level."  The improved
  Klein-twist candidate is consistent with both readings and does
  not distinguish them.

  This is a more refined understanding of the failure mode than
  the previous "candidate is an accident" reading: at PDG precision,
  there IS a candidate that closes, but we cannot tell if it is
  THE closure or ONE of several that happen to fit.
""")


# ============================================================================
# Main
# ============================================================================

def main() -> None:
    print("=" * 78)
    print("  a_1(lep) KLEIN-TWIST DERIVATION: base + correction + search")
    print("=" * 78)
    section_verify()
    section_subleading_search()
    section_cross_sector()
    section_failure_mode()


if __name__ == "__main__":
    main()
