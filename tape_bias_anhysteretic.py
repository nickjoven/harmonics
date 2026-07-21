"""
AC-bias anhysteretic linearization of a hysteretic recording medium.

A numerical witness for the dual-regime reading of magnetic-tape recording
(see `sync_cost/derivations/tape_stick_slip_dual_regime_correspondence.md`).

The substrate claim under test is *not* about magnetism per se: it is that a
hysteretic medium driven with a high-frequency carrier exhibits the framework's
two non-smoothly-decoupled regimes — a LOCKED regime (the bare medium settles
into discrete remanent fixed points; nonlinear, low fidelity) and an UNLOCKED
regime (the high-frequency carrier dithers the medium across its loop so the
average follows the signal continuously; linear, high fidelity). The carrier is
the operational *basepoint* that selects the regime; the framework supplies the
two-regime structure and the carrier:signal separation, not the absolute carrier
amplitude.

Model: a Preisach ensemble of relay hysterons with switch-up threshold a and
switch-down threshold b (a >= b). Each element records a signal level two ways:

  1. UNBIASED  — apply H = H_signal, release the field, read remanent M.
     This traces the medium's *normal magnetization curve*: single-valued but
     nonlinear, with a dead zone near the origin (the hysterons closest to
     zero never switch) and saturation at the rails. The dead zone is the
     lock-in: near zero, distinct signal levels map to the same remanent state.

  2. AC-BIASED — apply H = H_signal + bias(t), where bias(t) is a high-frequency
     oscillation whose envelope decays from large to zero (the tape element
     leaving the bias-field gap). This is the classic *anhysteretic* process:
     the decaying HF carrier walks every hysteron through shrinking loops until
     it settles onto the value set by H_signal alone. The transfer is the
     anhysteretic curve: single-valued AND linear through the origin.

Linearity is quantified two ways: R^2 of the small-signal transfer against a
best-fit straight line, and the fraction of the input range that lies in the
dead zone (distinct inputs producing indistinguishable remanence).

Dependencies: Python 3.10+, standard library only (math, random).
"""

import math
import random


# --------------------------------------------------------------------------
# Preisach ensemble
# --------------------------------------------------------------------------

def make_hysterons(n: int, h_sat: float, seed: int = 0):
    """
    Build n relay hysterons. Each has an up-threshold a and down-threshold b
    with a >= b, drawn so the pair (mean, half-width) tiles the Preisach
    triangle roughly uniformly out to +/- h_sat. State starts at -1 (demagged
    toward negative rail so the normal curve starts from saturation remanence).
    """
    rng = random.Random(seed)
    hysterons = []
    for _ in range(n):
        # mean threshold m in [-h_sat, h_sat], coercive half-width c >= 0
        m = rng.uniform(-h_sat, h_sat)
        c = rng.uniform(0.0, h_sat)
        a = m + c        # switches UP   when H rises above a
        b = m - c        # switches DOWN when H falls below b
        hysterons.append([a, b, -1])  # [up, down, state]
    return hysterons


def apply_field(hysterons, h: float) -> None:
    """Update every relay state for an applied field h (rate-independent)."""
    for hy in hysterons:
        if h >= hy[0]:
            hy[2] = +1
        elif h <= hy[1]:
            hy[2] = -1
        # else: hold previous state (the memory)


def magnetization(hysterons) -> float:
    """Net magnetization in [-1, 1]."""
    return sum(hy[2] for hy in hysterons) / len(hysterons)


def reset(hysterons) -> None:
    for hy in hysterons:
        hy[2] = -1


# --------------------------------------------------------------------------
# Two recording protocols
# --------------------------------------------------------------------------

def record_unbiased(hysterons, h_signal: float) -> float:
    """
    Normal magnetization curve: drive to H_signal from the demagged negative
    state, release, read remanence. Reset first so each sample is independent
    (models a fresh medium element seeing only its own signal level).
    """
    reset(hysterons)
    apply_field(hysterons, h_signal)
    apply_field(hysterons, 0.0)          # release the field
    return magnetization(hysterons)


def record_biased(hysterons, h_signal: float, h_bias0: float,
                  cycles: int = 60, decay: float = 0.92,
                  steps_per_cycle: int = 24) -> float:
    """
    Anhysteretic process: superimpose a high-frequency carrier of initial
    amplitude h_bias0 on the DC signal level and let the carrier envelope decay
    geometrically toward zero. Read remanence at H = H_signal.
    """
    reset(hysterons)
    amp = h_bias0
    for _ in range(cycles):
        for s in range(steps_per_cycle):
            phase = 2.0 * math.pi * s / steps_per_cycle
            apply_field(hysterons, h_signal + amp * math.sin(phase))
        amp *= decay
    apply_field(hysterons, h_signal)     # settle at the signal level
    return magnetization(hysterons)


# --------------------------------------------------------------------------
# Linearity diagnostics
# --------------------------------------------------------------------------

def r_squared(xs, ys) -> float:
    """R^2 of ys against the best-fit line in xs (small-signal linearity)."""
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    if sxx == 0:
        return 0.0
    slope = sxy / sxx
    intercept = my - slope * mx
    ss_tot = sum((y - my) ** 2 for y in ys)
    ss_res = sum((y - (slope * x + intercept)) ** 2 for x, y in zip(xs, ys))
    if ss_tot == 0:
        return 0.0
    return 1.0 - ss_res / ss_tot


def deadzone_fraction(xs, ys, tol_frac: float = 0.02) -> float:
    """
    Fraction of adjacent input steps whose output changes by less than
    `tol_frac` of the full output swing — i.e. the lock-in dead zone where
    distinct signal levels collapse to the same remanent fixed point.
    """
    swing = max(ys) - min(ys)
    if swing == 0:
        return 1.0
    tol = tol_frac * swing
    flat = sum(1 for i in range(1, len(ys)) if abs(ys[i] - ys[i - 1]) < tol)
    return flat / (len(ys) - 1)


# --------------------------------------------------------------------------
# Experiment
# --------------------------------------------------------------------------

def main() -> None:
    H_SAT = 1.0
    N = 4000
    hysterons = make_hysterons(N, H_SAT, seed=1)

    # Small-signal sweep (well inside the rails) to probe the transfer curve.
    levels = [(-0.5 + i / 40.0) for i in range(41)]  # -0.5 .. +0.5

    unbiased = [record_unbiased(hysterons, h) for h in levels]
    biased = [record_biased(hysterons, h, h_bias0=2.0) for h in levels]

    r2_u = r_squared(levels, unbiased)
    r2_b = r_squared(levels, biased)
    dz_u = deadzone_fraction(levels, unbiased)
    dz_b = deadzone_fraction(levels, biased)

    print("=" * 66)
    print("AC-bias anhysteretic linearization — dual-regime witness")
    print("=" * 66)
    print(f"Preisach ensemble: N = {N} hysterons, H_sat = {H_SAT}")
    print(f"Small-signal sweep: {len(levels)} levels in [{levels[0]:+.2f},"
          f" {levels[-1]:+.2f}]")
    print()
    print(f"{'regime':<22}{'linearity R^2':>16}{'dead-zone frac':>18}")
    print("-" * 66)
    print(f"{'UNBIASED (locked)':<22}{r2_u:>16.4f}{dz_u:>18.3f}")
    print(f"{'AC-BIASED (unlocked)':<22}{r2_b:>16.4f}{dz_b:>18.3f}")
    print("-" * 66)
    print()
    print("Transfer curves (signal -> remanent M):")
    print(f"{'H_signal':>10}{'unbiased':>14}{'biased':>14}")
    for h, u, b in zip(levels[::4], unbiased[::4], biased[::4]):
        print(f"{h:>10.3f}{u:>14.4f}{b:>14.4f}")
    print()
    print("Reading:")
    print(f"  * Unbiased transfer is nonlinear (R^2={r2_u:.3f}) with a")
    print(f"    {dz_u*100:.0f}% dead zone: near the origin distinct signal")
    print("    levels collapse onto the same remanent fixed point (lock-in).")
    print(f"  * AC bias dithers the medium across its loop; the transfer")
    print(f"    linearizes (R^2={r2_b:.3f}) and the dead zone closes")
    print(f"    ({dz_b*100:.0f}%). Same medium, two regimes — the carrier is")
    print("    the basepoint that selects which one.")


if __name__ == "__main__":
    main()
