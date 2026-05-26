#!/usr/bin/env python3
"""Critical (K=1) tongue-width exponent: it is NOT a single number.

Sharpens `farey_tongue_width_null.py`. That file recorded that the dynamical
tongue width decays faster than 1/q^2 (so the mass-function baseline is not
-2), fitting "beta ~ 2.3" from the 1/q tongues at q=2..7. This file measures
the SAME widths by the accurate tangent-bifurcation (saddle-node) condition
-- F^q(theta) = theta + p AND (F^q)'(theta) = 1 -- validates against those
recorded numbers to 4 digits, then extends, and finds:

  (1) beta is sequence-dependent (the width law is MULTIFRACTAL). The 1/q
      "harmonic" sequence has a local exponent that DRIFTS monotonically and
      never settles: 2.18 (q=3) -> 2.54 (q=7) -> 2.88 (q=22), still rising.
      So "beta ~ 2.3" is a low-q artifact of the 1/q sequence, not a constant.

  (2) The UNIVERSAL exponent comes from the golden-mean (Fibonacci) sequence
      p/q = F_n/F_{n+1}. Its tongue-width ratios converge to the
      Feigenbaum-Kadanoff-Shenker constant delta_FKS = 2.83361 (measured
      2.837), the parameter-scaling eigenvalue of the critical circle map's
      renormalization. Hence the universal width exponent is

          beta_gold = ln(delta_FKS) / ln(phi) = 2.1644   (measured 2.1640)

      and the universal dynamical mass-function slope is

          alpha = -1 - 2/beta_gold = -1.924

      governed by delta_FKS (RENORMALIZATION), not by the Jensen-Bak-Bohr
      mode-locked-complement dimension D = 0.870.

REFUTED here (recorded so the trail is in the evidence, not in canon): the
guess alpha = -(1+D) with D = D_JBB = 0.870 (i.e. beta = 2/D = 2.299). The
actual universal values are beta = 2.164, alpha = -1.924 -- beta != 2/D. The
near-coincidence 2/0.87 ~ 2.3 only matched where the 1/q local exponent
happens to pass through 2.3 at low q.

NET for the framework: the -q_2 = -2 baseline null stands and is sharpened.
There is no single dynamical baseline (it is a multifractal spectrum); the
clean universal representative is -1.924. Substituting it makes Salpeter
WORSE: -1.924 - 1/q_3 = -2.26 vs the combinatorial -7/3 = -2.333 (Salpeter
-2.35). So the -2 must remain the combinatorial Stern-Brocot tree weight
1/q^2; no single dynamical width law reproduces -7/3.

Run: python3 tongue_width_universality.py   (pure stdlib; ~seconds)
"""
from __future__ import annotations

import math

TWO_PI = 2.0 * math.pi
K = 1.0  # critical circle map


def fq_and_deriv(theta0: float, omega: float, q: int) -> tuple[float, float]:
    """q-fold lift of theta + Omega - (K/2pi) sin(2pi theta), and d/dtheta."""
    th, d = theta0, 1.0
    for _ in range(q):
        d *= 1.0 - K * math.cos(TWO_PI * th)        # f'(theta) = 1 - K cos(2pi theta)
        th = th + omega - (K / TWO_PI) * math.sin(TWO_PI * th)
    return th, d


def _bisect(g, a: float, b: float, tol: float = 1e-14, it: int = 200):
    ga, gb = g(a), g(b)
    if ga == 0:
        return a
    if gb == 0:
        return b
    if ga * gb > 0:
        return None
    for _ in range(it):
        m = 0.5 * (a + b)
        gm = g(m)
        if abs(gm) < 1e-16 or (b - a) < tol:
            return m
        if ga * gm < 0:
            b = m
        else:
            a, ga = m, gm
    return 0.5 * (a + b)


def superstable_omega(p: int, q: int):
    """Omega of the superstable p/q orbit (passes through the critical point)."""
    return _bisect(lambda om: fq_and_deriv(0.0, om, q)[0] - p, p / q - 0.9, p / q + 0.9)


def _orbit_seed(omega: float, q: int, p: int, n_settle: int = 8000):
    """Settle onto the period-q attractor; return (theta, multiplier) or None."""
    th = 0.1234567
    for _ in range(n_settle):
        th = (th + omega - (K / TWO_PI) * math.sin(TWO_PI * th)) % 1.0
    pts = [th]
    lift = th
    for _ in range(q):
        lift = lift + omega - (K / TWO_PI) * math.sin(TWO_PI * lift)
        pts.append(lift % 1.0)
    if abs(pts[-1] - pts[0]) > 1e-6 or round(lift - th) != p:
        return None
    m = 1.0
    for x in pts[:-1]:
        m *= 1.0 - K * math.cos(TWO_PI * x)
    return pts[0], m


def _newton2d(p: int, q: int, th0: float, om0: float, it: int = 80):
    """Solve the saddle-node system F^q(th)=th+p, (F^q)'(th)=1 for the edge Omega."""
    x = [th0, om0]

    def big_f(v):
        th, om = v
        fq, d = fq_and_deriv(th, om, q)
        return [fq - th - p, d - 1.0]

    for _ in range(it):
        f = big_f(x)
        if max(abs(f[0]), abs(f[1])) < 1e-14:
            break
        h = 1e-7
        f1, f2 = big_f([x[0] + h, x[1]]), big_f([x[0], x[1] + h])
        j = [[(f1[0] - f[0]) / h, (f2[0] - f[0]) / h],
             [(f1[1] - f[1]) / h, (f2[1] - f[1]) / h]]
        det = j[0][0] * j[1][1] - j[0][1] * j[1][0]
        if abs(det) < 1e-18:
            return None
        dx = [(j[1][1] * f[0] - j[0][1] * f[1]) / det,
              (-j[1][0] * f[0] + j[0][0] * f[1]) / det]
        x = [x[0] - dx[0], x[1] - dx[1]]
    f = big_f(x)
    return x[1] if max(abs(f[0]), abs(f[1])) < 1e-9 else None


def _edge(p: int, q: int, om_star: float, side: int):
    step = 0.5 * (1.0 / q ** 2.3)
    seed = None
    for k in range(1, 600):
        om = om_star + side * step * k / 40.0
        res = _orbit_seed(om, q, p)
        if res is None:
            break
        seed = (res[0], om)
        if res[1] > 0.985:
            break
    if seed is None:
        return None
    return _newton2d(p, q, seed[0], seed[1])


def width(p: int, q: int):
    om = superstable_omega(p, q)
    lo, hi = _edge(p, q, om, -1), _edge(p, q, om, +1)
    return None if lo is None or hi is None else abs(hi - lo)


def main() -> int:
    phi = (1.0 + 5.0 ** 0.5) / 2.0
    delta_fks = 2.833611          # Feigenbaum-Kadanoff-Shenker (golden-mean critical circle map)
    d_jbb = 0.8700                # Jensen-Bak-Bohr mode-locked-complement dimension

    print("VALIDATE 1/q widths vs farey_tongue_width_null.py (w*q^2: 0.296..0.197, q=2..7)")
    for q in range(2, 8):
        w = width(1, q)
        print(f"  q={q}  w={w:.6e}  w*q^2={w * q * q:.4f}")

    print("\n1/q harmonic sequence -- local exponent DRIFTS (no limit):")
    qs = list(range(2, 23))
    ws = [width(1, q) for q in qs]
    for i in range(1, len(qs)):
        bl = -math.log(ws[i] / ws[i - 1]) / math.log(qs[i] / qs[i - 1])
        if qs[i] in (3, 7, 12, 22):
            print(f"  q={qs[i]:>2}  beta_local={bl:.4f}  alpha={-1 - 2 / bl:.4f}")

    print("\ngolden-mean approximants F_n/F_{n+1} -- ratio -> delta_FKS, beta CONVERGES:")
    fib = [(1, 2), (2, 3), (3, 5), (5, 8), (8, 13), (13, 21)]
    gw = [width(p, q) for p, q in fib]
    for i in range(1, len(fib)):
        ratio = gw[i - 1] / gw[i]
        bg = -math.log(gw[i] / gw[i - 1]) / math.log(fib[i][1] / fib[i - 1][1])
        print(f"  {fib[i-1][0]}/{fib[i-1][1]}->{fib[i][0]}/{fib[i][1]}  "
              f"width_ratio={ratio:.4f}  beta={bg:.4f}")

    beta_gold = math.log(delta_fks) / math.log(phi)
    print(f"\n  delta_FKS = {delta_fks}  (measured width ratio -> {gw[-2] / gw[-1]:.4f})")
    print(f"  beta_gold = ln(delta_FKS)/ln(phi) = {beta_gold:.4f}")
    print(f"  alpha_universal = -1 - 2/beta_gold = {-1 - 2 / beta_gold:.4f}")
    print(f"\n  REFUTED: alpha = -(1+D) = {-(1 + d_jbb):.4f} (beta=2/D={2 / d_jbb:.4f}) -- "
          f"D_JBB is NOT the governing constant; delta_FKS is.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
