#!/usr/bin/env python3
"""Held-out test for the cascade slope ladder (Region-C Phase C #3).

The pigeonhole concern (cascade_slope_check.py, p ~ 0.10) is that the
framework's forced slope ladder is dense enough in [-2.5, -2.0] to hit
any slope. The held-out test controls for that: split observables into
ASSIGNED (slopes the framework claims a rung for) and CONTROL (independent
astrophysical power-law slopes the framework makes no cascade claim
about), and ask whether the ladder hits the assigned set better than it
hits the controls. If equal -> pigeonhole; if assigned closer -> the
framework's targeting carries information.

All slopes are in the dN/dM ~ M^alpha convention (Salpeter = -2.35).
Control values are representative literature figures (convention-
normalized); they are approximate, and the convention sensitivity (a
dN/dlnM quote differs by 1) is part of why this test has limited power.

Run: python3 held_out_slope_test.py
"""
from __future__ import annotations

from fractions import Fraction

# Forced ladder: alpha = -q_2 - n/d for the master-identity rungs.
LADDER = {
    "K=1 boundary": -2.0,
    "Z_6":          float(Fraction(-13, 6)),   # -2.167
    "K*":           float(Fraction(-31, 14)),  # -2.214
    "bowed":        float(Fraction(-7, 3)),     # -2.333
    "clarinet":     -2.5,
}

# ASSIGNED: (observed slope, sigma, the rung the framework pairs it to)
ASSIGNED = {
    "Salpeter IMF":   (-2.35, 0.05, "bowed"),
    "GC / halo MF":   (-2.0, 0.20, "K=1 boundary"),
}

# CONTROL: independent power-law slopes (dN/dM), NOT stellar-IMF-adjacent,
# NOT claimed by the framework. Representative literature values.
CONTROL = {
    "faint-end galaxy LF":      -1.3,
    "molecular cloud MF":       -1.7,
    "Kolmogorov turbulence":    -1.67,
    "solar flare energy":       -1.8,
    "cosmic-ray spectrum":      -2.7,
    "asteroid size dist":       -3.5,
    "debris collisional casc.": -3.5,
    "earthquake (G-R energy)":  -1.67,
    "initial cluster MF":       -2.0,
    "lunar crater size":        -3.0,
}


def nearest_rung(slope: float) -> tuple[str, float]:
    name, val = min(LADDER.items(), key=lambda kv: abs(kv[1] - slope))
    return name, abs(val - slope)


def main() -> int:
    print("=" * 64)
    print("HELD-OUT TEST: forced ladder vs assigned vs control slopes")
    print("=" * 64)
    print("Ladder rungs:", {k: round(v, 3) for k, v in LADDER.items()})
    print()

    print("ASSIGNED (framework's claimed pairings):")
    sal_gap = None
    for obs, (slope, sig, rung) in ASSIGNED.items():
        gap = abs(LADDER[rung] - slope)
        nz = gap / sig
        print(f"  {obs:<16} {slope:+.3f}  -> rung {rung:<13} gap {gap:.3f}  ({nz:.2f} sigma)")
        if obs.startswith("Salpeter"):
            sal_gap = gap
    print()

    print("CONTROL (independent, unclaimed; nearest rung):")
    near02 = []
    for obs, slope in CONTROL.items():
        rung, gap = nearest_rung(slope)
        flag = "  <- within Salpeter's gap" if gap <= sal_gap + 1e-9 else ""
        print(f"  {obs:<26} {slope:+.3f}  near {rung:<13} gap {gap:.3f}{flag}")
        if gap <= sal_gap + 1e-9:
            near02.append((obs, rung, gap))
    print()

    # separate pigeonhole-rich -2.0 from the informative -2.333
    print("VERDICT")
    print("-" * 64)
    rich = [c for c in near02 if abs(LADDER[c[1]] + 2.0) < 1e-9]
    other = [c for c in near02 if abs(LADDER[c[1]] + 2.0) >= 1e-9]
    print(f"Controls landing within Salpeter's gap ({sal_gap:.3f}) of a rung: "
          f"{len(near02)}/{len(CONTROL)}")
    print(f"  - at the -2.0 rung (pigeonhole-rich; -2.0 is the canonical")
    print(f"    self-similar value, common in nature): {[c[0] for c in rich]}")
    print(f"  - at any OTHER rung (informative): {[c[0] for c in other] or 'none'}")
    print()
    print("Reading:")
    print("  * GC/-2.0 assignment is uninformative: -2.0 is pigeonhole-rich,")
    print("    matched by independent controls (e.g. initial cluster MF).")
    print("  * bowed/Salpeter at the -7/3 = -2.333 rung: NO independent control")
    print("    lands within Salpeter's 0.017 gap of that rung. The one non-")
    print("    trivial rung is hit by the one observable, un-replicated.")
    print("  * But the informative sample is N = 1 (one rung, one observable):")
    print("    suggestive of real targeting, not statistically decisive.")
    print()
    print("Conclusion: the held-out test does NOT upgrade -7/3 to a decisive")
    print("statistical detection -- the ladder's range is narrow and sparsely")
    print("populated by independent controls, so power is low. The evidential")
    print("weight is one un-replicated match (Salpeter). What distinguishes")
    print("-7/3 from coincidence is the STRUCTURAL derivation (Step-2 orbit")
    print("count + Farey baseline + epsilon closure), now complete -- not the")
    print("statistics, which cannot be decisive with one rung and one observable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
