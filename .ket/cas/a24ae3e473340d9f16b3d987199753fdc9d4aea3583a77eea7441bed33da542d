#!/usr/bin/env python3
"""Cascade-slope check: mass-function slopes vs the master cascade ladder.

The master cascade-lock identity (master_cascade_identity.md) gives a
one-parameter family of mass-function slopes

    alpha = -q_2 - n/d        (q_2 = 2)

with (d, n, b) drawn from framework primitives. mass_function_family.md
assigns each cascade rung to a physical mass function. This script makes
the comparison explicit and, critically, runs a pigeonhole null so the
matches are not over-read: observed MF slopes cluster in a narrow band
(~ -1.9 to -2.5), so a "match" to *some* slope is statistically cheap.

Convention: all slopes are alpha in dN/dM proportional to M^alpha.

Run: python3 cascade_slope_check.py
"""
from __future__ import annotations

import math
import random
from dataclasses import dataclass

Q2 = 2  # smallest even denominator (substrate prime)


@dataclass
class Rung:
    label: str
    d: int | None   # cascade depth (None for the n=0 boundary)
    n: int          # Klein-flip count
    # observed assignment: (alpha_obs, sigma, source) or None if untestable
    obs: tuple[float, float, str] | None
    obs_note: str = ""

    @property
    def alpha_pred(self) -> float:
        # n = 0 boundary: alpha = -q_2 exactly
        if self.n == 0:
            return -float(Q2)
        assert self.d is not None
        return -Q2 - self.n / self.d


# Framework ladder + the sector->observable assignments from
# mass_function_family.md. Observed values (dN/dM ~ M^alpha):
#   GC/halo MF high-mass slope ~ -2.0, definition-dependent, wide band.
#   Subhalo MF: Springel+ 2008 (Aquarius) dN/dM ~ M^-1.90; Gao+ 2004 ~ -1.9.
#   Salpeter high-mass IMF: -2.35 +/- 0.05 (Salpeter 1955; Bastian+ 2010).
#   Clarinet / matter-K*: no clean fragmentation observable.
RUNGS = [
    Rung("K=1 boundary (string / GC / halo)", None, 0,
         (-2.00, 0.20, "GC/halo high-mass MF (definition-dependent)")),
    Rung("Z_6 cascade (conjectured)", 6, 1,
         (-1.90, 0.10, "subhalo MF, Springel+ 2008 / Gao+ 2004")),
    Rung("Matter equilibrium K*", 14, 3, None,
         "no fragmentation observable"),
    Rung("Bowed cascade (IMF)", 3, 1,
         (-2.35, 0.05, "Salpeter high-mass IMF, Bastian+ 2010")),
    Rung("Clarinet (q_3) cascade", 2, 1, None,
         "untested (massive-YC IMF ~ -2.5 contested)"),
]

# Range of slopes the framework permits (alpha in [-2.5, -2.0]; the
# identity forbids alpha < -2.5 unless n > 1, and alpha -> -2 as d -> inf).
ALPHA_LO, ALPHA_HI = -2.5, -2.0


def per_rung_report() -> list[tuple[str, float, float | None]]:
    """Return (label, alpha_pred, sigma_residual or None)."""
    rows = []
    for r in RUNGS:
        if r.obs is None:
            rows.append((r.label, r.alpha_pred, None))
        else:
            a_obs, sig, _ = r.obs
            sigma_resid = abs(r.alpha_pred - a_obs) / sig
            rows.append((r.label, r.alpha_pred, sigma_resid))
    return rows


def pigeonhole_null(trials: int = 200_000, seed: int = 1) -> dict:
    """How surprising is the observed match pattern?

    For each testable observable, draw a random slope uniform in the
    framework-permitted band [-2.5, -2.0] and ask how often it lands
    within 0.5 sigma / 1 sigma of the observed value. Also report the
    joint probability that a random 3-rung ladder matches >= 2 of the
    three testable observables at < 1 sigma.
    """
    rng = random.Random(seed)
    testable = [r for r in RUNGS if r.obs is not None]
    per = {r.label: {"<0.5sig": 0, "<1sig": 0} for r in testable}
    joint_ge2 = 0
    for _ in range(trials):
        n_match_1sig = 0
        for r in testable:
            a_obs, sig, _ = r.obs
            a_rand = rng.uniform(ALPHA_LO, ALPHA_HI)
            z = abs(a_rand - a_obs) / sig
            if z < 0.5:
                per[r.label]["<0.5sig"] += 1
            if z < 1.0:
                per[r.label]["<1sig"] += 1
                n_match_1sig += 1
        if n_match_1sig >= 2:
            joint_ge2 += 1
    for r in testable:
        per[r.label]["<0.5sig"] /= trials
        per[r.label]["<1sig"] /= trials
    return {"per_observable": per, "P(>=2 of 3 at <1sig)": joint_ge2 / trials}


def main() -> int:
    print("=" * 68)
    print("CASCADE-SLOPE CHECK   alpha = -q_2 - n/d   (q_2 = 2)")
    print("=" * 68)
    print(f"{'rung':<38}{'alpha_pred':>11}{'residual':>12}")
    print("-" * 68)
    testable_sigmas = []
    for label, a_pred, sig_resid in per_rung_report():
        if sig_resid is None:
            print(f"{label:<38}{a_pred:>11.4f}{'(no data)':>12}")
        else:
            verdict = "ok" if sig_resid < 1 else ("tension" if sig_resid < 3 else "FAIL")
            print(f"{label:<38}{a_pred:>11.4f}{sig_resid:>9.2f}σ  {verdict}")
            testable_sigmas.append(sig_resid)

    chi2 = sum(s * s for s in testable_sigmas)
    dof = len(testable_sigmas)
    print("-" * 68)
    print(f"testable rungs: {dof}   chi^2 = {chi2:.2f}  "
          f"(chi^2/dof = {chi2 / dof:.2f})")

    # chi^2 without the worst (most-tension) rung, to localize the signal
    if testable_sigmas:
        worst = max(testable_sigmas)
        chi2_drop = sum(s * s for s in testable_sigmas if s != worst)
        print(f"drop worst rung ({worst:.2f}σ): chi^2 = {chi2_drop:.2f} "
              f"on {dof - 1} rungs")

    print()
    print("PIGEONHOLE NULL (random slopes in the permitted band "
          f"[{ALPHA_LO}, {ALPHA_HI}]):")
    null = pigeonhole_null()
    for label, p in null["per_observable"].items():
        print(f"  {label:<40} P(<0.5σ)={p['<0.5sig']:.3f}  "
              f"P(<1σ)={p['<1sig']:.3f}")
    print(f"  P(random ladder matches >=2 of 3 at <1σ) = "
          f"{null['P(>=2 of 3 at <1sig)']:.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
