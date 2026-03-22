"""
Stribeck lattice: N oscillators in a chain, each coupled to its
neighbors through Stribeck friction contacts.

The hypothesis: a spatially extended frictional medium can convert
energy from a high-frequency drive into subharmonic channels that
propagate coherently. Each Stribeck contact is one stage of a
frequency converter. The bifurcation cascade develops spatially
across the chain, not just temporally in a single oscillator.

Drive element 0 at ω_d, measure the spectrum at element N-1.
"""

import math
from dataclasses import dataclass, field
from typing import List


def stribeck_friction(
    v_rel: float,
    mu_s: float = 1.2,
    mu_k: float = 0.25,
    v_thr: float = 0.15,
    f_n: float = 0.4,
) -> float:
    """Stribeck friction force given relative velocity."""
    v_ratio = abs(v_rel) / v_thr
    mu = mu_k + (mu_s - mu_k) * math.exp(-v_ratio ** 2)
    sign = 1.0 if v_rel >= 0 else -1.0
    return mu * f_n * sign


@dataclass
class StribeckLattice:
    """
    Linear chain of N oscillators coupled by Stribeck friction.

    Each oscillator has mass, stiffness (anchoring spring), and damping.
    Adjacent oscillators interact through Stribeck friction contacts —
    no linear springs between them, only the nonlinear velocity-dependent
    friction coupling.

    Element 0 is driven externally at (drive_amp, drive_freq).
    All other elements are undriven.

    Parameters
    ----------
    n_elements    : number of oscillators in the chain
    mass          : mass of each oscillator
    stiffness     : anchoring spring constant (each element to ground)
    damping       : linear viscous damping per element
    mu_static     : static friction coefficient (all contacts)
    mu_kinetic    : kinetic friction coefficient (all contacts)
    v_threshold   : Stribeck transition velocity
    normal_force  : contact normal force (all contacts)
    drive_amp     : driving amplitude on element 0
    drive_freq    : driving frequency on element 0 (rad/s)
    """
    n_elements: int = 8
    mass: float = 1.0
    stiffness: float = 1.0
    damping: float = 0.02
    mu_static: float = 1.2
    mu_kinetic: float = 0.25
    v_threshold: float = 0.15
    normal_force: float = 0.4
    drive_amp: float = 0.0
    drive_freq: float = 1.0

    def simulate(
        self,
        dt: float = 0.0005,
        n_steps: int = 600_000,
        downsample: int = 4,
    ) -> dict:
        """
        Simulate the lattice. Returns time series for all elements.

        Output keys:
            t           : time array
            x_0 .. x_{N-1} : position of each element
            v_0 .. v_{N-1} : velocity of each element
        """
        N = self.n_elements
        x = [0.0] * N
        v = [0.0] * N

        out_t = []
        out_x = [[] for _ in range(N)]
        out_v = [[] for _ in range(N)]

        for step in range(n_steps):
            t = step * dt

            # Compute all friction forces between neighbors
            # f_fric[i] = friction force on element i from element i+1
            # By Newton's third law, element i+1 feels -f_fric[i]
            f_fric = [0.0] * (N - 1)
            for i in range(N - 1):
                v_rel = v[i + 1] - v[i]  # relative velocity of i+1 w.r.t. i
                f_fric[i] = stribeck_friction(
                    v_rel,
                    self.mu_static, self.mu_kinetic,
                    self.v_threshold, self.normal_force,
                )

            # Update each element
            for i in range(N):
                f_total = 0.0

                # Driving force (element 0 only)
                if i == 0:
                    f_total += self.drive_amp * math.sin(self.drive_freq * t)

                # Friction from left neighbor (i-1 → i)
                if i > 0:
                    # Element i feels -f_fric[i-1] (reaction)
                    f_total -= f_fric[i - 1]

                # Friction from right neighbor (i+1 → i)
                if i < N - 1:
                    f_total += f_fric[i]

                # Anchoring spring and damping
                f_total -= self.stiffness * x[i]
                f_total -= self.damping * v[i]

                # Symplectic Euler
                a = f_total / self.mass
                v[i] += a * dt
                x[i] += v[i] * dt

            if step % downsample == 0:
                out_t.append(t)
                for i in range(N):
                    out_x[i].append(x[i])
                    out_v[i].append(v[i])

        result = {"t": out_t}
        for i in range(N):
            result[f"x_{i}"] = out_x[i]
            result[f"v_{i}"] = out_v[i]
        return result
