"""
Suspended symmetric top: the tilt as a real degree of freedom.

A follow-up to `suspended_rotor.py`. That earlier script *imposed* the spin
axis -- it carried a scalar spin rate plus a separate, hand-placed pendulum
mode. This one lets the axis and its tilt *emerge* from an actual inertia
tensor under gravity, which is the faithful answer to a bench remark: it is
hard to depict a tilt without first positing the axis of symmetry it departs
from. Here that axis (the figure axis ``n``) and its tilt are explicit state.

Model
-----
A symmetric rigid body (moments I1 = I2 about the pivot, I3 about the figure
axis) hangs from a single point a distance ``l`` below the pivot along the
figure axis, and is spun about a near-vertical axis. This is the classic
*Lagrange top* in its hanging (centre-of-mass-below-pivot) configuration --
equivalently a spinning spherical pendulum.

To keep the perfectly-axial baseline well-posed we integrate in the lab frame,
singularity-free, in terms of the figure-axis unit vector ``n`` and the angular
momentum about the pivot ``L`` (no Euler angles, so no gimbal lock at zero
tilt):

    dn/dt = (L x n) / I1
    dL/dt = -M g l (n x zhat) + (damping torques)

The spin about the figure axis is ``omega3 = (L . n) / I3``; gravity's torque is
perpendicular to ``n`` and so never changes ``L . n`` -- the spin decays only
through the explicit spin drag, exactly as a real top coasts down.

What the faithful model shows -- and an honest caveat
-----------------------------------------------------
Linearising about the hanging equilibrium (``n = -zhat``) gives two transverse
mode frequencies,

    Omega_pm = [ I3 omega3  +/-  sqrt( (I3 omega3)^2 + 4 I1 M g l ) ] / (2 I1),

a fast nutation branch and a slow (retrograde) precession branch. As the spin
coasts down (omega3 -> 0) BOTH converge to the bare pendulum +/- omega_p, with
omega_p = sqrt(M g l / I1). So the two tones the bench shows -- a fast wobble
and a slow swing -- are real, emergent, and meet at the gravitational pendulum
as the spin dies. The tilt is a genuine coordinate, and the "balanced" case is
simply ``tilt == 0`` held by symmetry.

But note what this model does NOT claim. A free (or linearly damped) symmetric
top is *integrable*: its motion is quasi-periodic nutation+precession, not the
Arnold-tongue mode-locking the rest of this framework is built on. Genuine
locking onto low-order rationals needs a non-integrable element -- the
stick-slip friction nonlinearity of `driven_stribeck.py`, or the contact drag
optionally enabled here via ``contact_friction``. Turning that on breaks
integrability and is the bridge back to the framework; left off (the default),
this script is the faithful, integrable top and should be read as such. It is
illustrative, not a derivation of any physical constant.

Dependencies: Python 3.9+, standard library only. matplotlib is used only for
the optional figure in __main__; the simulation needs nothing beyond ``math``.
"""

import math
from dataclasses import dataclass

Vec = tuple[float, float, float]

ZHAT: Vec = (0.0, 0.0, 1.0)


# --- minimal 3-vector helpers (stdlib only; no numpy dependency) -----------

def _add(a: Vec, b: Vec) -> Vec:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def _scale(a: Vec, s: float) -> Vec:
    return (a[0] * s, a[1] * s, a[2] * s)


def _dot(a: Vec, b: Vec) -> float:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def _cross(a: Vec, b: Vec) -> Vec:
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def _norm(a: Vec) -> float:
    return math.sqrt(_dot(a, a))


def _unit(a: Vec) -> Vec:
    n = _norm(a)
    return a if n == 0.0 else _scale(a, 1.0 / n)


@dataclass
class SuspendedSymmetricTop:
    """
    Hanging Lagrange top integrated singularity-free in (n, L).

    Parameters
    ----------
    I1            : transverse moment of inertia about the pivot (I1 = I2)
    I3            : moment of inertia about the figure axis
    Mgl           : gravitational torque scale M*g*l (sets omega_p = sqrt(Mgl/I1))
    spin_damping  : drag on the figure-axis spin (1/s); sets the coast-down rate
    tilt_damping  : viscous drag on the transverse (nutation/precession) motion
    contact_friction : optional Stribeck-like drag opposing the transverse
                       slipping velocity. ZERO by default -- the faithful top is
                       integrable. A positive value breaks integrability and is
                       the bridge to the framework's locking picture.
    mu_static, mu_kinetic, v_thr : Stribeck curve for ``contact_friction``,
                       matching the convention in `driven_stribeck.py`.
    """

    I1: float = 1.0
    I3: float = 0.5
    Mgl: float = 1.0
    spin_damping: float = 0.02
    tilt_damping: float = 0.005
    contact_friction: float = 0.0
    mu_static: float = 1.2
    mu_kinetic: float = 0.25
    v_thr: float = 0.15

    @property
    def omega_p(self) -> float:
        """Bare gravitational pendulum frequency, sqrt(Mgl / I1)."""
        return math.sqrt(self.Mgl / self.I1)

    def mode_frequencies(self, omega3: float) -> tuple[float, float]:
        """
        The two linear transverse mode frequencies at spin rate ``omega3``:
        the fast nutation branch and the slow (retrograde) precession branch.
        Both tend to +/- omega_p as omega3 -> 0.
        """
        a = self.I3 * omega3
        disc = math.sqrt(a * a + 4.0 * self.I1 * self.Mgl)
        return ((a + disc) / (2.0 * self.I1), (a - disc) / (2.0 * self.I1))

    def _stribeck(self, v_rel: float) -> float:
        """Stribeck friction magnitude*sign (same curve as driven_stribeck.py)."""
        ratio = abs(v_rel) / self.v_thr
        mu = self.mu_kinetic + (self.mu_static - self.mu_kinetic) * math.exp(-ratio * ratio)
        return mu * (1.0 if v_rel >= 0.0 else -1.0)

    def _deriv(self, n: Vec, L: Vec) -> tuple[Vec, Vec]:
        """Right-hand side of the (n, L) system, including damping torques."""
        spin_mom = _dot(L, n)              # = I3 * omega3, conserved by gravity

        dn = _scale(_cross(L, n), 1.0 / self.I1)

        # Gravity: torque about the pivot, perpendicular to the figure axis.
        grav = _scale(_cross(n, ZHAT), -self.Mgl)

        # Spin drag: along the figure axis, drains omega3 only.
        tau_spin = _scale(n, -self.spin_damping * spin_mom)

        # Transverse (nutation/precession) viscous drag.
        L_perp = _add(L, _scale(n, -spin_mom))     # L - (L.n) n
        tau_perp = _scale(L_perp, -self.tilt_damping)

        dL = _add(_add(grav, tau_spin), tau_perp)

        # Optional Stribeck contact drag opposing the transverse slip. This is
        # the non-integrable element; zero by default.
        if self.contact_friction != 0.0:
            omega_perp = _scale(L_perp, 1.0 / self.I1)
            speed = _norm(omega_perp)
            if speed > 1e-12:
                f = self.contact_friction * self._stribeck(speed)
                dL = _add(dL, _scale(omega_perp, -f / speed))

        return dn, dL

    def simulate(
        self,
        tilt0: float = 0.15,
        omega3_0: float = 6.0,
        dt: float = 0.001,
        n_steps: int = 400_000,
        downsample: int = 20,
    ) -> dict:
        """
        RK4 integration from an initial tilt and spin.

        The body starts spinning about an axis tilted ``tilt0`` radians from the
        downward vertical. ``tilt0 = 0`` is the perfectly axial (balanced) case:
        the figure axis is the spin axis and stays put. Returns a dict of
        downsampled trajectories with keys:
        t, tilt, omega3, precession, nx, ny, nz.
        """
        # Figure axis starts in the x-z plane, tilted by tilt0 from straight down.
        n: Vec = (math.sin(tilt0), 0.0, -math.cos(tilt0))
        # Spin angular momentum initially along the figure axis.
        L: Vec = _scale(n, self.I3 * omega3_0)

        out: dict[str, list[float]] = {
            k: [] for k in ("t", "tilt", "omega3", "precession", "nx", "ny", "nz")
        }
        prev_azimuth = math.atan2(n[1], n[0])

        for i in range(n_steps):
            # Classic RK4 on the stacked (n, L) state.
            k1n, k1L = self._deriv(n, L)
            n2 = _add(n, _scale(k1n, dt / 2))
            L2 = _add(L, _scale(k1L, dt / 2))
            k2n, k2L = self._deriv(n2, L2)
            n3 = _add(n, _scale(k2n, dt / 2))
            L3 = _add(L, _scale(k2L, dt / 2))
            k3n, k3L = self._deriv(n3, L3)
            n4 = _add(n, _scale(k3n, dt))
            L4 = _add(L, _scale(k3L, dt))
            k4n, k4L = self._deriv(n4, L4)

            n = _add(n, _scale(_add(_add(k1n, _scale(k2n, 2)), _add(_scale(k3n, 2), k4n)), dt / 6))
            L = _add(L, _scale(_add(_add(k1L, _scale(k2L, 2)), _add(_scale(k3L, 2), k4L)), dt / 6))
            n = _unit(n)   # control numerical drift off the unit sphere

            if i % downsample == 0:
                t = i * dt
                tilt = math.acos(max(-1.0, min(1.0, -n[2])))   # angle from -zhat
                omega3 = _dot(L, n) / self.I3
                azimuth = math.atan2(n[1], n[0])
                # Unwrapped azimuthal rate ~ precession speed.
                dphi = azimuth - prev_azimuth
                while dphi > math.pi:
                    dphi -= 2 * math.pi
                while dphi < -math.pi:
                    dphi += 2 * math.pi
                precession = dphi / (downsample * dt) if i > 0 else 0.0
                prev_azimuth = azimuth

                out["t"].append(t)
                out["tilt"].append(tilt)
                out["omega3"].append(omega3)
                out["precession"].append(precession)
                out["nx"].append(n[0])
                out["ny"].append(n[1])
                out["nz"].append(n[2])

        return out


def _summarise(name: str, top: SuspendedSymmetricTop, res: dict) -> None:
    tilt = res["tilt"]
    omega3 = res["omega3"]
    peak = max(tilt)
    print(f"\n=== {name} ===")
    print(f"  I1, I3              : {top.I1:.3f}, {top.I3:.3f}")
    print(f"  omega_p (emergent)  : {top.omega_p:.4f} rad/s")
    print(f"  spin: {omega3[0]:.3f} -> {omega3[-1]:.3f} rad/s")
    print(f"  peak tilt           : {peak:.4f} rad ({math.degrees(peak):.2f} deg)")

    if peak < 1e-6:
        print("  -> axial: figure axis IS the spin axis; tilt stays zero, smooth coast-down.")
        return

    # Two emergent mode frequencies at the start and end of the coast-down.
    fast0, slow0 = top.mode_frequencies(omega3[0])
    fast1, slow1 = top.mode_frequencies(omega3[-1])
    print("  transverse mode frequencies (rad/s):")
    print(f"     at spin {omega3[0]:.2f}:  fast nutation {fast0:7.3f}   slow precession {slow0:7.3f}")
    print(f"     at spin {omega3[-1]:.2f}:  fast nutation {fast1:7.3f}   slow precession {slow1:7.3f}")
    print(f"     both -> +/- omega_p = +/-{top.omega_p:.3f} as the spin dies")
    if top.contact_friction != 0.0:
        print(f"  contact_friction = {top.contact_friction:.3f}: integrability broken "
              "(framework-locking bridge enabled)")
    else:
        print("  contact_friction = 0: integrable top -- quasi-periodic nutation, no locking")


def main() -> None:
    """Axial vs tilted suspended symmetric top, and (optionally) a figure."""
    dt, n_steps, downsample = 0.001, 400_000, 20

    axial = SuspendedSymmetricTop()
    tilted = SuspendedSymmetricTop()

    res_axial = axial.simulate(tilt0=0.0, dt=dt, n_steps=n_steps, downsample=downsample)
    res_tilted = tilted.simulate(tilt0=0.15, dt=dt, n_steps=n_steps, downsample=downsample)

    _summarise("axial (balanced)", axial, res_axial)
    _summarise("tilted", tilted, res_tilted)

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("\n(matplotlib not available -- skipping figure)")
        return

    fig, axes = plt.subplots(3, 1, figsize=(9, 9))

    axes[0].plot(res_axial["t"], res_axial["omega3"], label="axial")
    axes[0].plot(res_tilted["t"], res_tilted["omega3"], label="tilted")
    axes[0].set_ylabel("spin  omega3 (rad/s)")
    axes[0].legend(loc="upper right")
    axes[0].set_title("Suspended symmetric top: tilt as a real degree of freedom")

    axes[1].plot(res_axial["t"], res_axial["tilt"], label="axial")
    axes[1].plot(res_tilted["t"], res_tilted["tilt"], label="tilted")
    axes[1].set_ylabel("tilt of figure axis (rad)")
    axes[1].set_xlabel("time (s)")
    axes[1].legend(loc="upper right")

    # The figure-axis tip traces an epicycle (two emergent frequencies).
    axes[2].plot(res_tilted["nx"], res_tilted["ny"], lw=0.5, color="C1")
    axes[2].set_aspect("equal", adjustable="box")
    axes[2].set_xlabel("n_x")
    axes[2].set_ylabel("n_y")
    axes[2].set_title("figure-axis tip in the horizontal plane (nutation + precession)")

    fig.tight_layout()
    out_path = "suspended_top.png"
    fig.savefig(out_path, dpi=110)
    print(f"\nFigure written to {out_path}")


if __name__ == "__main__":
    main()
