"""
Suspended imbalanced rotor: spin-down through rational frequency locks.

A motivating bench observation. Suspend a die (or any rigid body) from a
single point and spin it about a near-vertical axis:

  * Perfectly balanced, spun on a principal axis of inertia, it spins down
    smoothly. Angular momentum L stays parallel to angular velocity omega,
    no internal torque is needed to sustain the rotation, and the only thing
    acting is dissipation. The energy decays monotonically -- no wave, no
    swing.

  * Imbalanced (centre of mass off the spin axis, or spun off a principal
    axis), the mass offset co-rotates with the body and becomes a *periodic
    forcing at the spin frequency* in the lab frame. The suspension adds a
    slow pendulum / torsion mode. As the rotor spins down, its spin rate
    sweeps downward through the pendulum band, and whenever the ratio
    spin : pendulum passes a low-order rational the two modes lock and energy
    pours into a visible swing.

This is the same mechanism as `driven_stribeck.py` (a periodic drive feeding
a dissipative oscillator across a bifurcation into subharmonic channels) and
`bifurcation_sweep.py` (parameter sweep revealing the locked bands), here
driven by rotational imbalance instead of an explicit forcing term. The locks
land specifically on the low-order rationals (small denominators) -- the
Arnold-tongue / mediant ordering that the rest of this framework is built on.

A caution on reading the amplitudes: smaller denominators have wider Arnold
tongues, but the *measured* peak swing here is not a clean read-out of tongue
width. Two confounds ride on top of it. (1) The imbalance forcing scales as
omega**2, so high-spin locks are driven harder than low-spin ones. (2) The
spin-down is exponential, so the rotor dwells far longer at low spin rates and
the swing has more time to accumulate there. In the default run these push the
largest *amplitude* toward the lower-frequency locks (e.g. 2:3) even though the
widest *tongue* is at 1:1. The robust, model-independent claim is the one you
can see on the bench: the swing wakes up at low-order rational locks and stays
quiet between them. Disentangling tongue width from the envelope would need a
constant-amplitude, constant-sweep-rate drive -- which is `bifurcation_sweep.py`'s
job, not this script's.

This script is illustrative: it demonstrates the locking mechanism the
framework relies on. It is not a derivation of any physical constant.

Dependencies: Python 3.9+, standard library only (math, dataclasses).
matplotlib is used only for the optional figure in __main__; numpy only for
the optional spectral helper. The simulation itself needs neither.
"""

import math
from dataclasses import dataclass


@dataclass
class SuspendedRotor:
    """
    Two-degree-of-freedom model of a suspended, imbalanced rotor.

    Degree of freedom 1 -- spin: angle ``theta`` about the (near-vertical)
    suspension axis, with rate ``omega``. The spin loses energy to a linear
    drag ``spin_damping`` and, at resonance, back-reacts against the pendulum
    it is driving (the "wave" carries energy away from the spin).

    Degree of freedom 2 -- pendulum / torsion: angle ``phi`` of the slow
    swing the suspension permits, natural frequency ``omega_p``, viscous
    damping ratio ``zeta``. The pendulum is a true (nonlinear) pendulum:
    the ``sin(phi)`` restoring term is what opens superharmonic and
    subharmonic locks at low-order rationals rather than only the 1:1
    primary resonance.

    Coupling -- the rotating imbalance: a centre-of-mass offset of relative
    size ``imbalance`` produces a horizontal force that rotates with the
    body. Its centrifugal magnitude scales as omega**2, and its projection
    onto the swing plane is ``cos(theta)``. So the pendulum sees a forcing

        f_drive(t) = imbalance * omega(t)**2 * cos(theta(t))

    at the (slowly drifting) spin frequency. By Newton's third law the spin
    feels the reaction, scaled by ``reaction`` -- this is the only channel by
    which the spin-down curve "knows" it has passed through a resonance.

    A balanced rotor is simply ``imbalance = 0``: the coupling vanishes, the
    pendulum stays put, and the spin decays as a clean exponential.

    Parameters
    ----------
    spin_inertia : moment of inertia about the spin axis
    omega0       : initial spin rate (rad/s)
    spin_damping : linear drag on the spin (1/s); sets the spin-down rate
    omega_p      : pendulum / torsion natural frequency (rad/s)
    zeta         : pendulum damping ratio (dimensionless)
    imbalance    : relative centre-of-mass offset (0 = perfectly balanced)
    reaction     : strength of the pendulum -> spin back-reaction
    """

    spin_inertia: float = 1.0
    omega0: float = 6.0
    spin_damping: float = 0.05
    omega_p: float = 1.0
    zeta: float = 0.02
    imbalance: float = 0.0
    reaction: float = 0.3

    def drive(self, omega: float, theta: float) -> float:
        """Forcing the rotating imbalance applies to the pendulum."""
        return self.imbalance * omega * omega * math.cos(theta)

    def simulate(
        self,
        dt: float = 0.001,
        n_steps: int = 400_000,
        downsample: int = 20,
    ) -> dict:
        """
        Symplectic Euler integration of the coupled spin + pendulum system.

        Matches the integration style of `driven_stribeck.py`: velocities are
        advanced first, then positions, and the trajectory is downsampled for
        storage.

        Returns dict with keys: t, theta, omega, phi, phidot, f_drive.
        """
        theta, omega = 0.0, self.omega0
        phi, phidot = 0.0, 0.0

        out: dict[str, list[float]] = {
            k: [] for k in ("t", "theta", "omega", "phi", "phidot", "f_drive")
        }

        for i in range(n_steps):
            t = i * dt

            f_drive = self.drive(omega, theta)

            # Pendulum: nonlinear restoring + viscous damping + imbalance drive
            phi_acc = (
                -self.omega_p * self.omega_p * math.sin(phi)
                - 2.0 * self.zeta * self.omega_p * phidot
                + f_drive
            )
            phidot += phi_acc * dt
            phi += phidot * dt

            # Spin: linear drag + reaction torque from the pendulum it drives.
            # The reaction is largest when the pendulum is moving in phase with
            # the projected imbalance, i.e. exactly inside a resonance band.
            omega_acc = (
                -self.spin_damping * omega
                - self.reaction * self.imbalance * phidot * math.cos(theta)
            ) / self.spin_inertia
            omega += omega_acc * dt
            theta += omega * dt

            if i % downsample == 0:
                out["t"].append(t)
                out["theta"].append(theta)
                out["omega"].append(omega)
                out["phi"].append(phi)
                out["phidot"].append(phidot)
                out["f_drive"].append(f_drive)

        return out


@dataclass
class ResonanceBand:
    """A window of the spin-down where the swing amplitude peaks."""

    ratio_num: int
    ratio_den: int
    omega_ratio: float          # spin / pendulum at the peak
    peak_amplitude: float       # max |phi| in the band (rad)
    time_at_peak: float

    @property
    def label(self) -> str:
        return f"{self.ratio_num}:{self.ratio_den}"


def find_resonance_bands(
    result: dict,
    omega_p: float,
    max_denominator: int = 4,
    window: float = 0.06,
) -> list[ResonanceBand]:
    """
    Attribute swing-amplitude peaks to the low-order rational the spin rate
    was passing through.

    For each candidate ratio p/q (q <= ``max_denominator``) we look at the
    stretch of the run where ``omega / omega_p`` sat within ``window`` of p/q,
    and record the largest |phi| reached there. Every peak lands on a low-order
    rational; the amplitude ordering, however, is set by the omega**2 forcing
    envelope and the (longer) dwell time at low spin rates as much as by tongue
    width -- see the module docstring.
    """
    t = result["t"]
    omega = result["omega"]
    phi = result["phi"]

    # Candidate low-order ratios, smallest denominators first (mediant order).
    ratios: list[tuple[int, int]] = []
    for q in range(1, max_denominator + 1):
        for p in range(1, 4 * max_denominator + 1):
            if math.gcd(p, q) != 1:
                continue
            ratios.append((p, q))

    bands: list[ResonanceBand] = []
    for p, q in ratios:
        target = p / q
        best_amp = 0.0
        best_t = 0.0
        best_ratio = target
        for tt, w, ph in zip(t, omega, phi):
            r = w / omega_p
            if abs(r - target) <= window and abs(ph) > best_amp:
                best_amp = abs(ph)
                best_t = tt
                best_ratio = r
        if best_amp > 0.0:
            bands.append(ResonanceBand(p, q, best_ratio, best_amp, best_t))

    bands.sort(key=lambda b: b.peak_amplitude, reverse=True)
    return bands


def power_spectrum(signal: list[float], dt: float) -> tuple:
    """
    Optional spectral helper (requires numpy), mirroring driven_stribeck.py.

    Returns (freqs_hz, magnitude) for the positive-frequency half.
    """
    import numpy as np  # local import: simulation does not need numpy

    arr = np.asarray(signal, dtype=float)
    arr = arr - arr.mean()
    spectrum = np.abs(np.fft.rfft(arr))
    freqs = np.fft.rfftfreq(arr.size, d=dt)
    return freqs, spectrum


def _summarise(name: str, rotor: SuspendedRotor, result: dict, dt_eff: float) -> None:
    omega = result["omega"]
    phi = result["phi"]
    peak_swing = max(abs(x) for x in phi)
    spun_down = omega[-1] / rotor.omega0
    print(f"\n=== {name} ===")
    print(f"  imbalance           : {rotor.imbalance:.3f}")
    print(f"  initial spin rate   : {rotor.omega0:.3f} rad/s")
    print(f"  final spin fraction : {spun_down:6.1%} of omega0")
    print(f"  peak swing amplitude: {peak_swing:.4f} rad "
          f"({math.degrees(peak_swing):.2f} deg)")

    if rotor.imbalance == 0.0:
        print("  -> balanced: smooth spin-down, the swing never wakes up.")
        return

    bands = find_resonance_bands(result, rotor.omega_p)
    print("  resonance locks crossed during spin-down "
          "(largest swing first):")
    print("     ratio   omega/omega_p   peak swing (rad)   t (s)")
    for b in bands[:6]:
        print(f"     {b.label:>5}   {b.omega_ratio:11.3f}   "
              f"{b.peak_amplitude:14.4f}   {b.time_at_peak:7.1f}")


def main() -> None:
    """Compare a balanced rotor with an imbalanced one and (optionally) plot."""
    dt, n_steps, downsample = 0.001, 400_000, 20
    dt_eff = dt * downsample

    balanced = SuspendedRotor(imbalance=0.0)
    imbalanced = SuspendedRotor(imbalance=0.04)

    res_balanced = balanced.simulate(dt=dt, n_steps=n_steps, downsample=downsample)
    res_imbalanced = imbalanced.simulate(dt=dt, n_steps=n_steps, downsample=downsample)

    _summarise("balanced", balanced, res_balanced, dt_eff)
    _summarise("imbalanced", imbalanced, res_imbalanced, dt_eff)

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("\n(matplotlib not available -- skipping figure)")
        return

    fig, axes = plt.subplots(3, 1, figsize=(9, 9), sharex=True)

    axes[0].plot(res_balanced["t"], res_balanced["omega"], label="balanced")
    axes[0].plot(res_imbalanced["t"], res_imbalanced["omega"], label="imbalanced")
    axes[0].axhline(imbalanced.omega_p, ls=":", color="grey", lw=1)
    axes[0].set_ylabel("spin rate  omega (rad/s)")
    axes[0].legend(loc="upper right")
    axes[0].set_title("Suspended rotor: spin-down through rational locks")

    axes[1].plot(res_balanced["t"], res_balanced["phi"], label="balanced")
    axes[1].plot(res_imbalanced["t"], res_imbalanced["phi"], label="imbalanced")
    axes[1].set_ylabel("swing  phi (rad)")
    axes[1].legend(loc="upper right")

    # Swing amplitude versus the instantaneous spin:pendulum ratio, with the
    # low-order rationals marked -- the locks should sit on these lines.
    ratio = [w / imbalanced.omega_p for w in res_imbalanced["omega"]]
    axes[2].plot(ratio, [abs(p) for p in res_imbalanced["phi"]], color="C1")
    for p, q in [(1, 1), (2, 1), (3, 1), (3, 2), (1, 2)]:
        axes[2].axvline(p / q, ls=":", color="grey", lw=1)
        axes[2].text(p / q, 0, f"{p}:{q}", rotation=90,
                     va="bottom", ha="right", fontsize=8, color="grey")
    axes[2].set_xlabel("omega / omega_p   (spin : pendulum)")
    axes[2].set_ylabel("|swing| (rad)")
    axes[2].set_xlim(0, imbalanced.omega0 / imbalanced.omega_p)

    fig.tight_layout()
    out_path = "suspended_rotor.png"
    fig.savefig(out_path, dpi=110)
    print(f"\nFigure written to {out_path}")


if __name__ == "__main__":
    main()
