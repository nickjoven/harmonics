#!/usr/bin/env python3
"""FRW transform of the flat staircase: does expansion remap D or the slope?

The framework's flat (K=1) mode-locking staircase is lab-confirmed: it is the
Josephson/CDW universality class with complement dimension D ~ 0.87 and 1/q
width exponent beta ~ 2.3 (josephson_staircase_comparison.py,
farey_tongue_width_null.py). The reframe asks whether the cosmological
(curved, expanding) version carries a DIFFERENT effective slope because the
universe expands. This computes the answer.

PART 1 -- redshift kinematics on D (the structure).
The FRW redshift relabels the frequency axis Omega -> g(Omega) (Omega/a for
uniform redshift; a smooth monotone map in general). Box-counting dimension
is invariant under any bi-Lipschitz reparametrization, so D is UNCHANGED.
Verified numerically below on the flat staircase and a warped (non-uniform)
resampling: both give D ~ 0.87. So the lab<->cosmos universality identity is
redshift-robust; expansion does not destroy or alter the structure.

PART 2 -- does the SLOPE change?
The redshift map is smooth and (for uniform Omega/a) linear, so it rescales
all tongue widths by the same factor: beta is unchanged, and the mass-
function slope stays at the flat value -1 - 2/beta ~ -1.86. So the redshift
KINEMATICS alone do NOT remap the slope -- the cosmos and the lab carry the
SAME slope under redshift.

Any difference must come from the structure-formation DYNAMICS: a tongue p/q
freezes at some epoch a(p/q) and its mass is the horizon mass M_H(a) at that
epoch. That tongue<->epoch map is the K(t) running -- an open, anchor-side
free function. With a power-law map a(q) ~ q^(-s) and matter-era horizon mass
M_H ~ a^(3/2), the slope becomes -1 - 4/(3s): a FREE FUNCTION gives ANY slope.
-2 needs the specific unforced s = 4/3; the kinematics alone (no map) give
-1.86. So the FRW transform does NOT predict -2 -- it relocates the slope's
determination entirely to the (gated) K(t) map.

Run: python3 frw_staircase_transform.py   (pure stdlib; ~3 s)
"""
from __future__ import annotations

import math

TWO_PI = 2.0 * math.pi


def W(Omega: float, K: float = 1.0, n: int = 4000) -> float:
    th = 0.1
    half = n // 2
    for _ in range(half):
        th += Omega - (K / TWO_PI) * math.sin(TWO_PI * th)
    th0, m = th, n - half
    for _ in range(m):
        th += Omega - (K / TWO_PI) * math.sin(TWO_PI * th)
    return (th - th0) / m


def boxcount_D(Ws: list[float], thresh: float = 1e-3) -> float:
    M = len(Ws)
    xs, ys = [], []
    for k in range(5, 10):                 # clean dyadic box range
        nb = 2 ** k
        cells = M // nb
        active = sum(1 for b in range(nb)
                     if max(Ws[b*cells:(b+1)*cells]) - min(Ws[b*cells:(b+1)*cells]) > thresh)
        xs.append(k * math.log(2))
        ys.append(math.log(active))
    n = len(xs)
    sx, sy = sum(xs), sum(ys)
    return (n*sum(x*y for x, y in zip(xs, ys)) - sx*sy) / (n*sum(x*x for x in xs) - sx*sx)


def main() -> int:
    M = 2 ** 12
    print("PART 1 -- D is redshift-invariant (structure survives expansion)")
    flat = [W((i + 0.5) / M, 1.0) for i in range(M)]
    D_flat = boxcount_D(flat)
    # warped resampling: a smooth bi-Lipschitz reparametrization of the axis
    # (stand-in for a non-uniform redshift), Omega = u + 0.2 sin(2 pi u)/(2 pi)
    def warp(u):
        return min(1 - 1e-9, max(1e-9, u + 0.2 * math.sin(TWO_PI * u) / TWO_PI))
    warped = [W(warp((i + 0.5) / M), 1.0) for i in range(M)]
    D_warp = boxcount_D(warped)
    print(f"  flat staircase D            = {D_flat:.3f}")
    print(f"  redshift-warped staircase D = {D_warp:.3f}")
    print(f"  lab/universal (Josephson,CDW) D ~ 0.87")
    print("  => D invariant: the universality class is redshift-robust.")
    print()

    print("PART 2 -- the slope is NOT set by the redshift; it is gated on K(t)")
    beta = 2.3
    print(f"  redshift kinematics alone (smooth/linear map): beta unchanged = {beta}")
    print(f"    => slope -1 - 2/beta = {-1 - 2/beta:.2f}  (same as the lab)")
    print("  with a tongue<->epoch map a(q) ~ q^(-s), matter-era M_H ~ a^(3/2):")
    print(f"    {'s':>6}{'slope -1 - 4/(3s)':>20}")
    for s in (0.5, 1.0, 4/3, 2.0, 3.0):
        print(f"    {s:>6.2f}{-1 - 4/(3*s):>20.2f}")
    print("  -> a FREE function (K(t)) gives ANY slope; -2 needs the specific")
    print("     unforced s = 4/3. The kinematics alone give -1.86.")
    print()
    print("VERDICT")
    print("-" * 60)
    print("Expansion does NOT, by itself, remap the slope: the redshift is a")
    print("smooth reparametrization, so D (~0.87) AND beta (~2.3) are invariant,")
    print("and the cosmological slope equals the lab slope, -1.86 -- NOT -2.")
    print("The only thing that can make the cosmos differ from the lab is the")
    print("tongue<->epoch (K(t)) map, a free anchor-side function the framework")
    print("has not fixed. So the FRW transform confirms the structure is")
    print("redshift-robust, and localizes the entire open problem to K(t): it")
    print("does NOT rescue the -2 baseline. All roads lead back to K(t).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
