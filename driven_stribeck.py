"""
Driven stick-slip oscillator with Stribeck friction.

Extends the free-decay StickSlipOscillator from nickjoven/intersections
into a periodically forced configuration. The driving force pumps energy
at frequency ω_d; the Stribeck nonlinearity redistributes that energy
across subharmonic channels (ω_d/2, ω_d/3, …) when the driving amplitude
crosses the bifurcation threshold.

Two configurations:
  1. Single driven oscillator — establishes subharmonic emergence.
  2. Coupled pair (TX → medium → RX) — models energy transfer through
     the frictional medium via subharmonic channels.

Dependencies: Python 3.10+, standard library only (math, dataclasses).
Power spectrum analysis requires numpy; the simulation itself does not.
"""

import math
from dataclasses import dataclass
from typing import Optional


@dataclass
class DrivenStribeckOscillator:
    """
    Mass-spring-damper with Stribeck friction and periodic forcing.

    The Stribeck friction curve models a medium that couples strongly
    at low relative velocity (stick) and weakly at high relative velocity
    (slip). Periodic forcing at amplitude A and frequency ω_d drives
    the system across the stick-slip bifurcation boundary.

    Parameters
    ----------
    mass        : effective mass
    stiffness   : linear restoring force (spring constant)
    damping     : linear viscous damping coefficient
    mu_static   : static friction coefficient (peak coupling)
    mu_kinetic  : kinetic friction coefficient (residual coupling)
    v_threshold : characteristic velocity for the Stribeck transition
    normal_force: normal force applied to the friction contact
    drive_amp   : amplitude of the periodic driving force
    drive_freq  : angular frequency of the periodic driving force (rad/s)
    """
    mass: float = 1.0
    stiffness: float = 1.0
    damping: float = 0.02
    mu_static: float = 1.2
    mu_kinetic: float = 0.25
    v_threshold: float = 0.15
    normal_force: float = 0.4
    drive_amp: float = 0.0
    drive_freq: float = 1.0  # ω_d in rad/s

    def stribeck_friction(self, v_rel: float) -> float:
        """Stribeck friction: smooth interpolation from μ_s to μ_k."""
        v_ratio = abs(v_rel) / self.v_threshold
        mu = self.mu_kinetic + (self.mu_static - self.mu_kinetic) * math.exp(-v_ratio ** 2)
        sign = 1.0 if v_rel >= 0 else -1.0
        return mu * self.normal_force * sign

    def driving_force(self, t: float) -> float:
        """External periodic forcing."""
        return self.drive_amp * math.sin(self.drive_freq * t)

    def simulate(
        self,
        dt: float = 0.0005,
        n_steps: int = 200_000,
        downsample: int = 10,
    ) -> dict:
        """
        Symplectic Euler integration.

        Returns dict with keys: t, x, v, f_friction, f_drive
        Arrays are downsampled by factor `downsample` for storage.
        """
        x, v = 0.0, 0.0
        t_arr, x_arr, v_arr, ff_arr, fd_arr = [], [], [], [], []

        for i in range(n_steps):
            t = i * dt

            # Forces
            f_drive = self.driving_force(t)
            v_rel = -v  # medium is stationary; relative velocity is -v
            f_friction = self.stribeck_friction(v_rel)
            f_spring = -self.stiffness * x
            f_damp = -self.damping * v

            # Integration (symplectic Euler)
            a = (f_drive + f_friction + f_spring + f_damp) / self.mass
            v += a * dt
            x += v * dt

            if i % downsample == 0:
                t_arr.append(t)
                x_arr.append(x)
                v_arr.append(v)
                ff_arr.append(f_friction)
                fd_arr.append(f_drive)

        return {
            "t": t_arr,
            "x": x_arr,
            "v": v_arr,
            "f_friction": ff_arr,
            "f_drive": fd_arr,
        }


@dataclass
class CoupledStribeckPair:
    """
    Two oscillators coupled through a shared frictional medium.

    Oscillator 1 (TX) is periodically driven. Oscillator 2 (RX) is
    undriven. They interact only through the medium: each experiences
    Stribeck friction proportional to its velocity relative to a shared
    medium element, which itself responds to the net force from both
    oscillators.

    The medium element has its own mass and damping, representing the
    inertia and loss of the coupling substrate.

    Parameters
    ----------
    tx, rx         : oscillator parameters (mass, stiffness, damping)
    medium_mass    : effective mass of the coupling medium element
    medium_damping : viscous damping of the medium element
    mu_static      : static friction (both contacts)
    mu_kinetic     : kinetic friction (both contacts)
    v_threshold    : Stribeck transition velocity
    normal_force   : contact normal force (both contacts)
    drive_amp      : TX driving amplitude
    drive_freq     : TX driving frequency (rad/s)
    """
    tx_mass: float = 1.0
    tx_stiffness: float = 1.0
    tx_damping: float = 0.02
    rx_mass: float = 1.0
    rx_stiffness: float = 1.0
    rx_damping: float = 0.02
    medium_mass: float = 0.5
    medium_damping: float = 0.05
    mu_static: float = 1.2
    mu_kinetic: float = 0.25
    v_threshold: float = 0.15
    normal_force: float = 0.4
    drive_amp: float = 0.0
    drive_freq: float = 1.0

    def _stribeck(self, v_rel: float) -> float:
        v_ratio = abs(v_rel) / self.v_threshold
        mu = self.mu_kinetic + (self.mu_static - self.mu_kinetic) * math.exp(-v_ratio ** 2)
        sign = 1.0 if v_rel >= 0 else -1.0
        return mu * self.normal_force * sign

    def simulate(
        self,
        dt: float = 0.0005,
        n_steps: int = 400_000,
        downsample: int = 10,
    ) -> dict:
        """
        Simulate the TX → medium → RX system.

        Returns dict with keys:
            t, tx_x, tx_v, rx_x, rx_v, med_v,
            f_tx_friction, f_rx_friction, f_drive
        """
        # State: (x, v) for TX, RX, and medium velocity v_m (no restoring force)
        tx_x, tx_v = 0.0, 0.0
        rx_x, rx_v = 0.0, 0.0
        med_v = 0.0

        out = {k: [] for k in [
            "t", "tx_x", "tx_v", "rx_x", "rx_v", "med_v",
            "f_tx_friction", "f_rx_friction", "f_drive",
        ]}

        for i in range(n_steps):
            t = i * dt

            # Driving force on TX
            f_drive = self.drive_amp * math.sin(self.drive_freq * t)

            # Friction: TX ↔ medium
            v_rel_tx = med_v - tx_v
            f_fric_tx = self._stribeck(v_rel_tx)  # force on TX from medium

            # Friction: RX ↔ medium
            v_rel_rx = med_v - rx_v
            f_fric_rx = self._stribeck(v_rel_rx)  # force on RX from medium

            # TX: driven + friction from medium + spring + damping
            a_tx = (f_drive + f_fric_tx - self.tx_stiffness * tx_x - self.tx_damping * tx_v) / self.tx_mass
            tx_v += a_tx * dt
            tx_x += tx_v * dt

            # RX: friction from medium + spring + damping (no external drive)
            a_rx = (f_fric_rx - self.rx_stiffness * rx_x - self.rx_damping * rx_v) / self.rx_mass
            rx_v += a_rx * dt
            rx_x += rx_v * dt

            # Medium: reaction forces from both contacts + its own damping
            # Newton's third law: medium feels -f_fric_tx and -f_fric_rx
            a_med = (-f_fric_tx - f_fric_rx - self.medium_damping * med_v) / self.medium_mass
            med_v += a_med * dt

            if i % downsample == 0:
                out["t"].append(t)
                out["tx_x"].append(tx_x)
                out["tx_v"].append(tx_v)
                out["rx_x"].append(rx_x)
                out["rx_v"].append(rx_v)
                out["med_v"].append(med_v)
                out["f_tx_friction"].append(f_fric_tx)
                out["f_rx_friction"].append(f_fric_rx)
                out["f_drive"].append(f_drive)

        return out
