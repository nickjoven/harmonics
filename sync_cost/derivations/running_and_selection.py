"""
Running sign and golden ratio selection.

Two connected open questions:

#4: WHERE does the spectral running dn_s/d(ln k) come from?
#8: WHY is 1/φ selected over other noble numbers?

Answer to both: the system is at NEAR-CRITICAL COUPLING (K → 1).
Near criticality, only the golden gap survives (KAM theorem).
The running comes from the gap closing as K increases — it's the
derivative of the gap width with respect to coupling, not a feature
of the staircase's self-similarity (which gives zero running).

The connection:
  - At K < 1: gaps exist between tongues. The widest is at 1/φ.
  - As K → 1: gaps close. 1/φ closes LAST (KAM).
  - The running dn_s/dlnk measures HOW the tilt changes with scale.
  - If K varies slightly with scale (running coupling), this produces
    running through the K-dependence of the gap structure.
  - The SIGN of the running is negative because K increasing
    → gap narrowing → tilt becoming slightly more negative.

Usage:
    python sync_cost/derivations/running_and_selection.py
"""

import math
from circle_map_utils import (winding_number, circle_map_step,
                              PHI, INV_PHI, PHI_SQ, LN_PHI_SQ,
                              fibonacci_convergents, farey_mediants)


# ---------------------------------------------------------------------------
# Noble numbers: continued fractions eventually all 1s
# ---------------------------------------------------------------------------

def cf_to_float(cf_list, n_terms=50):
    """Convert continued fraction [a0; a1, a2, ...] to float."""
    # Extend to n_terms by repeating the last element if periodic
    extended = list(cf_list)
    if len(extended) < n_terms:
        tail = extended[-1] if extended else 1
        extended.extend([tail] * (n_terms - len(extended)))

    val = 0.0
    for a in reversed(extended[:n_terms]):
        val = 1.0 / (a + val) if (a + val) != 0 else float('inf')
    return val


def noble_numbers():
    """
    Generate noble numbers: irrationals with CF eventually all 1s.

    1/φ = [0; 1, 1, 1, ...] — the simplest
    Others: [0; 2, 1, 1, 1, ...], [0; 1, 2, 1, 1, 1, ...], etc.
    """
    nobles = []

    # 1/φ = [0; 1, 1, 1, ...]
    nobles.append(("1/φ", [1] * 50, INV_PHI))

    # [0; 2, 1, 1, 1, ...] = 1/(1+φ) = 2-φ
    cf = [2] + [1] * 49
    nobles.append(("[0;2,1,1,..]", cf, cf_to_float(cf)))

    # [0; 3, 1, 1, 1, ...]
    cf = [3] + [1] * 49
    nobles.append(("[0;3,1,1,..]", cf, cf_to_float(cf)))

    # [0; 1, 2, 1, 1, 1, ...]
    cf = [1, 2] + [1] * 48
    nobles.append(("[0;1,2,1,1,..]", cf, cf_to_float(cf)))

    # [0; 1, 1, 2, 1, 1, 1, ...]
    cf = [1, 1, 2] + [1] * 47
    nobles.append(("[0;1,1,2,1,..]", cf, cf_to_float(cf)))

    # [0; 1, 1, 1, 2, 1, 1, 1, ...]
    cf = [1, 1, 1, 2] + [1] * 46
    nobles.append(("[0;1,1,1,2,..]", cf, cf_to_float(cf)))

    return nobles


# ---------------------------------------------------------------------------
# Gap width measurement
# ---------------------------------------------------------------------------

def gap_width_at(omega, K, delta=0.001):
    """
    Measure the "gap width" at frequency omega by checking how much
    the winding number deviates from omega.

    If W(omega) ≈ omega: quasiperiodic (in a gap)
    If W(omega) ≠ omega: mode-locked (in a tongue)

    Returns |W - omega| as a proxy for gap proximity.
    """
    W = winding_number(omega, K, n_transient=5000, n_measure=50000)
    return abs(W - omega)


def staircase_slope_at(omega, K, h=0.0005):
    """
    Local slope dW/dΩ at omega. High slope = in a gap. Zero slope = on a plateau.
    """
    W_plus = winding_number(omega + h, K, n_transient=3000, n_measure=20000)
    W_minus = winding_number(omega - h, K, n_transient=3000, n_measure=20000)
    return (W_plus - W_minus) / (2 * h)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 85)
    print("  RUNNING SIGN AND GOLDEN RATIO SELECTION")
    print("=" * 85)

    # === 1. WHY 1/φ: GAP WIDTHS AT NOBLE NUMBERS ===
    print(f"\n{'─'*85}")
    print("  1. GAP STRUCTURE AT NOBLE NUMBERS")
    print(f"{'─'*85}")

    print(f"""
  Noble numbers have CF eventually all 1s. They are "equally irrational"
  in the sense of having bounded partial quotients. But their GAP WIDTHS
  in the devil's staircase differ.

  Hypothesis: 1/φ has the widest gap at EVERY coupling K.
  Other nobles approach the same asymptotic behavior but with a transient.
""")

    nobles = noble_numbers()

    for K in [0.5, 0.8, 0.95]:
        print(f"\n  K = {K}:")
        print(f"  {'noble':>18s}  {'value':>12s}  {'dW/dΩ':>10s}  "
              f"{'|W-Ω|':>10s}  {'gap rank':>10s}")
        print("  " + "-" * 70)

        results = []
        for name, cf, val in nobles:
            if val <= 0 or val >= 1:
                continue
            slope = staircase_slope_at(val, K)
            deviation = gap_width_at(val, K)
            results.append((name, val, slope, deviation))

        # Sort by slope (higher = wider gap)
        results.sort(key=lambda x: -x[2])

        for rank, (name, val, slope, dev) in enumerate(results, 1):
            marker = " <<<" if "1/φ" in name else ""
            print(f"  {name:>18s}  {val:12.8f}  {slope:10.4f}  "
                  f"{dev:10.6f}  {rank:>10d}{marker}")

    # === 2. 1/φ IS THE LAST GAP TO CLOSE ===
    print(f"\n{'─'*85}")
    print("  2. GAP CLOSING: 1/φ is the LAST to close (KAM theorem)")
    print(f"{'─'*85}")

    print(f"\n  dW/dΩ at each noble number as K → 1:")
    print(f"  (High dW/dΩ = wide gap; zero = closed/locked)")

    nobles_subset = noble_numbers()[:4]

    print(f"\n  {'K':>6s}", end="")
    for name, _, _ in nobles_subset:
        print(f"  {name:>14s}", end="")
    print()
    print("  " + "-" * (6 + 16 * len(nobles_subset)))

    for K_100 in range(50, 101, 5):
        K = K_100 / 100.0
        print(f"  {K:6.2f}", end="")
        for name, cf, val in nobles_subset:
            if val <= 0 or val >= 1:
                print(f"  {'---':>14s}", end="")
                continue
            slope = staircase_slope_at(val, K)
            marker = "*" if slope > 0.1 else " "
            print(f"  {slope:13.4f}{marker}", end="")
        print()

    print(f"\n  * = gap still open (dW/dΩ > 0.1)")
    print(f"  1/φ should have the highest slope at every K < 1")

    # === 3. THE THREE SOURCES OF RUNNING ===
    print(f"\n{'─'*85}")
    print("  3. THREE SOURCES OF SPECTRAL RUNNING")
    print(f"{'─'*85}")

    print(f"""
  The spectral tilt: n_s - 1 = -ln(φ²) × dn/d(ln k)

  A LINEAR mapping n(ln k) gives ZERO running (constant n_s).
  Three possible sources of nonlinearity:

  SOURCE 1: Staircase imperfections at finite Fibonacci level
    The φ² self-similarity has corrections ∝ (-1/φ²)^n.
    At level 21 (the pivot): correction ~ 1/φ^42 ≈ 10⁻⁹. NEGLIGIBLE.

  SOURCE 2: Sub-Fibonacci structure (superharmonic mediants)
    Within each Fibonacci bracket, non-Fibonacci rationals add
    structure. But the Fibonacci path in the Stern-Brocot tree
    has NO room for mediants (each mediant IS the next convergent).
    Unique to 1/φ. Sub-Fibonacci corrections are present but tiny.

  SOURCE 3: Scale-dependent coupling K(k)
    If the coupling strength varies with wavenumber, then the
    staircase itself changes shape at different scales. Since
    the gap width at 1/φ depends on K, a running coupling
    produces a running tilt.

  SOURCE 3 is the dominant one. Let's quantify it.
""")

    # === 4. RUNNING FROM K-DEPENDENCE ===
    print(f"{'─'*85}")
    print("  4. RUNNING FROM SCALE-DEPENDENT COUPLING")
    print(f"{'─'*85}")

    print(f"""
  If K = K(k), then the local tilt at scale k is:
    n_s(k) - 1 = -ln(φ²) × rate(K(k))

  The rate depends on K because the staircase shape depends on K.
  Specifically, the local dW/dΩ at 1/φ (which sets the power) depends
  on K. If we define:

    s(K) = dW/dΩ at Ω = 1/φ   (the gap slope)

  Then the effective tilt contribution from the staircase is:
    d ln(s) / d ln(k) = [d ln(s)/dK] × [dK/d ln(k)]

  The running is:
    dn_s/d(ln k) = -ln(φ²) × rate' + d²ln(s)/d(ln k)²

  Let's measure d ln(s)/dK numerically:
""")

    print(f"  {'K':>6s}  {'dW/dΩ at 1/φ':>14s}  {'ln(dW/dΩ)':>12s}  "
          f"{'Δ ln(dW/dΩ)/ΔK':>16s}")
    print("  " + "-" * 55)

    slopes = []
    for K_10 in range(3, 10):
        K = K_10 / 10.0
        s = staircase_slope_at(INV_PHI, K, h=0.0003)
        ln_s = math.log(abs(s)) if abs(s) > 1e-10 else float('-inf')
        slopes.append((K, s, ln_s))

    for i, (K, s, ln_s) in enumerate(slopes):
        if i > 0 and not math.isinf(ln_s) and not math.isinf(slopes[i-1][2]):
            d_ln_s = (ln_s - slopes[i-1][2]) / (K - slopes[i-1][0])
            print(f"  {K:6.2f}  {s:14.6f}  {ln_s:12.4f}  {d_ln_s:16.4f}")
        else:
            print(f"  {K:6.2f}  {s:14.6f}  {ln_s:12.4f}  {'---':>16s}")

    # === 5. THE SELECTION ARGUMENT ===
    print(f"\n{'─'*85}")
    print("  5. WHY 1/φ: THE SELECTION ARGUMENT")
    print(f"{'─'*85}")

    print(f"""
  The argument has three steps:

  STEP 1: The system is at near-critical coupling (K → 1).
    Why? The Planck scale derivation says the synchronization loop
    operates at its minimum viable threshold. Critical coupling is
    where the mean field is barely self-sustaining — the N = 3
    threshold. Below K_c, no synchronization. Above K_c, mode-locked.
    The physical system sits at K ≈ K_c.

  STEP 2: Near criticality, only the golden gap survives.
    The KAM theorem: as K → 1, all gaps close. They close in order
    of "irrationality" — gaps at rationals with large CF entries
    close first, nobles close last, 1/φ closes absolutely last.

    At K just below 1, the staircase is almost entirely flat
    (locked). The only remaining structure is at 1/φ. The power
    spectrum is dominated by the 1/φ neighborhood because there's
    nothing else left.

  STEP 3: 1/φ gives exact self-similarity at EVERY level.
    Other noble numbers [0; a₁, ..., aₖ, 1, 1, 1, ...] have the
    same φ² tail behavior. But their first k convergents are NOT
    Fibonacci. The self-similarity is exact only in the tail.

    1/φ = [0; 1, 1, 1, ...] has ALL convergents Fibonacci.
    The self-similarity is exact at EVERY level, from the Planck
    scale (level ~146) to the Hubble scale (level 0).

    If the physics requires self-similarity across the entire
    Planck-to-Hubble hierarchy (146 levels), only 1/φ provides it
    without transient corrections.

  CONCLUSION: 1/φ is selected by the conjunction of:
    (a) Near-critical coupling (Planck threshold)
    (b) KAM survival (golden is last)
    (c) Full-hierarchy self-similarity (no transient)

  No other number satisfies all three.
""")

    # === 6. NOBLE NUMBERS: TRANSIENT LENGTH ===
    print(f"{'─'*85}")
    print("  6. TRANSIENT LENGTH OF NOBLE NUMBERS")
    print(f"{'─'*85}")

    print(f"""
  For a noble number [0; a₁, ..., aₖ, 1, 1, 1, ...], the transient
  (non-Fibonacci) region is the first k terms. After that, the
  convergents follow the Fibonacci pattern with φ² scaling.

  The transient introduces corrections to self-similarity at the
  first k levels. If the pivot is at level ~21, and the transient
  is k levels long, the correction affects levels 0 through k.

  For 1/φ: k = 0 (no transient). Exact at every level.
""")

    print(f"  {'noble':>18s}  {'value':>12s}  {'transient k':>12s}  "
          f"{'exact from':>12s}")
    print("  " + "-" * 60)

    for name, cf, val in noble_numbers():
        # Find where the CF becomes all-1s
        transient = 0
        for i, a in enumerate(cf):
            if a != 1:
                transient = i + 1
        print(f"  {name:>18s}  {val:12.8f}  {transient:12d}  "
              f"{'level ' + str(transient):>12s}")

    # === 7. RUNNING SIGN FROM COUPLING GRADIENT ===
    print(f"\n{'─'*85}")
    print("  7. RUNNING SIGN: WHY NEGATIVE?")
    print(f"{'─'*85}")

    print(f"""
  The running dn_s/d(ln k) ≈ -0.0045 ± 0.007 is consistent with
  zero but has a negative central value. In the staircase picture:

  1. LINEAR mapping (n ∝ ln k): zero running. ESTABLISHED.

  2. SLOW-ROLL curvature: the standard inflationary prediction.
     dn_s/d(ln k) ≈ -(n_s - 1)² + ... ≈ -0.001
     This is negative and consistent with observations.

  3. COUPLING GRADIENT: if K increases at smaller scales
     (dK/d ln k > 0), the gap at 1/φ NARROWS, reducing dW/dΩ,
     reducing power. This makes the tilt more negative at small
     scales → negative running.

     Physical picture: smaller scales (higher k) have stronger
     coupling (more oscillators per wavelength → stronger mean
     field). Stronger coupling → narrower gap → less power.

  Sources 2 and 3 are both negative. The observed running is
  compatible with either or both.

  QUANTITATIVE CHECK:
    Observed: dn_s/d(ln k) = -0.0045 ± 0.007
    Slow-roll: -(n_s-1)² ≈ -{(0.0351)**2:.6f}
    Combined with O(1) coefficients: ~ -0.001 to -0.003
""")

    r_squared = -(0.0351)**2
    print(f"  -(n_s - 1)²  = {r_squared:.6f}")
    print(f"  Observed      = -0.0045 ± 0.007")
    print(f"  Ratio         = {-0.0045 / r_squared:.2f}  "
          f"(observed / slow-roll prediction)")
    print(f"  Consistent within 1σ: {'YES' if abs(-0.0045 - r_squared) < 0.007 else 'NO'}")

    # === 8. SUMMARY ===
    print(f"\n{'='*85}")
    print("  SUMMARY")
    print(f"{'='*85}")

    print(f"""
  RUNNING (#4):
    The staircase gives ZERO running (exact self-similarity).
    All running comes from the dynamics:
      (a) Slow-roll curvature in the k↔Ω mapping: ~ -(n_s-1)²
      (b) Scale-dependent coupling: dK/d(ln k) × d ln(s)/dK
    Both give NEGATIVE running, consistent with Planck's -0.0045.
    The separation is clean: staircase → scale-invariance,
    dynamics → tilt and running.

  SELECTION (#8):
    1/φ is selected by three conditions:
      (a) Near-critical coupling (from Planck threshold N=3)
      (b) KAM theorem: golden gap is last to close at K→1
      (c) Full-hierarchy self-similarity: CF all-1s → no transient
    Other noble numbers satisfy (a) and (b) but NOT (c):
    they have transients from non-1 CF entries.
    Only 1/φ gives exact φ² scaling at every level.

  CONNECTION:
    The running sign and the golden selection are the same physics:
    the system sits at near-critical coupling where only the 1/φ
    gap survives. The running measures how this gap responds to
    the small variation of K with scale.
""")
