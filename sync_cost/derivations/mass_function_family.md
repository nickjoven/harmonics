# Mass-function family across cascade depths

The master cascade-lock identity gives a one-parameter slope family:

    α = -q_2 - n/d

with `(d, n)` selecting the cascade instance. Different observed mass
functions correspond to different cascade depths:

| Cascade instance | d | n | α | Observable | Match |
|---|---|---|---|---|---|
| Gravitational K = 1 (string) | — | 0 | -2.000 | Press–Schechter halo MF | exact |
| Globular-cluster MF | — | 0 | -2.000 | universal GC MF | exact |
| Z_6 cascade (conjectured) | 6 | 1 | -13/6 ≈ -2.167 | subhalo MF (-1.9 to -2.0) | **2.67σ tension — out of band** |
| Matter equilibrium K* | 14 | 3 | -31/14 ≈ -2.214 | (no fragmentation observable) | — |
| Bowed cascade (Phase II) | 3 | 1 | -7/3 ≈ -2.333 | Salpeter IMF | 0.33σ |
| Clarinet cascade (q_3-base) | 2 | 1 | -5/2 | predicted, untested | — |

## Structural reading

Part of the observed mass-function spread aligns with the slope
formula evaluated at different cascade depths: as cascade depth `d`
increases, α → -q_2 = -2 (the K = 1 boundary), and shallower
cascades give steeper slopes.

**Range caveat (important).** The formula's image is
`α = -q_2 - n/d ∈ (-2.5, -2.0]` for n ≥ 1 — it asymptotes to -2.0
from below and **cannot produce any slope shallower than -2.0**. The
spread of observed slopes therefore is *not* fully covered by the
formula at the shallow end: the observed subhalo slope (-1.9 to -2.0)
lies outside or at the edge of the formula's range and is matched by
the **K = 1 boundary (-2.0)**, not by a deeper Z_6 rung (-2.167). See
`cascade_slope_check.py`: the Z_6 assignment is in 2.67σ tension and
triggers this doc's own subhalo falsifier (below). The genuinely
supported rung is the bowed/Salpeter one (-7/3 vs -2.35 ± 0.05 =
0.33σ); the K = 1 boundary (-2.0) is consistent but observationally
cheap; the clarinet (-5/2) and matter-K* (-31/14) rungs have no clean
fragmentation observable and remain untested.

## Falsifiers

- Subhalo MF measurement giving α < -2.05 or α > -2.30: the Z_6-cascade
  prediction (-13/6 = -2.167) is out of band. **This falsifier is
  currently triggered**: the observed subhalo slope (-1.9 to -2.0)
  has α > -2.05, so the Z_6/subhalo assignment is out of band. The
  subhalo MF is matched by the K = 1 boundary (-2.0), not the Z_6 rung.
- Salpeter IMF measured at α < -2.40 or α > -2.27: the Phase II bowed
  cascade prediction (-7/3 = -2.333) is out of band.
- Discovery of a mass function with α < -2.50: forbidden by the master
  identity unless n > 1.

## Predicted observable: clarinet cascade α = -5/2

The q_3-cascade slope -5/2 has no current observable assignment.
Candidates worth checking:

- Massive young-cluster IMF (some studies report α ≈ -2.5 at the
  high-mass end; contested).
- Pre-main-sequence brown-dwarf formation regime.
- Dark-matter mode-mass spectrum if the antisym/clarinet sector hosts
  mass-locked modes.

## Companion: soliton mass spectrum on the same K-zoo

The fragmentation-slope formula `α = -q_2 - n/d` is one mass relation
the K-zoo gives. The soliton sector gives a second. By
`sine_gordon_substrate.md`, the kink mass at each cascade is
`M_k = 8 σ √(K r)`, so cross-sector ratios are

    M_k(d, n, b) / M_k(K=1) = b^(-n/(2d))

The two relations are structurally distinct — fragmentation slopes
come from the cascade-depth-as-Klein-orbit-count argument, kink masses
from the locked-state expansion of the framework Lagrangian — but they
share the same K input from `master_cascade_identity.md`. Sectors with
no fragmentation observable (e.g., the matter-equilibrium K* with
α = -31/14) may still admit a soliton observable; conversely, a sector
that hosts a fragmentation cascade may not host stable kinks.

| Cascade instance | α (fragmentation) | M_k / M_k(K=1) (soliton) |
|---|---|---|
| K = 1 boundary | -2.000 | 1.000 |
| Z_6 cascade (d=6, n=1) | -13/6 ≈ -2.167 | 2^(-1/12) ≈ 0.944 |
| Matter K* (d=14, n=3) | -31/14 ≈ -2.214 | 2^(-3/28) ≈ 0.928 |
| Bowed (d=3, n=1) | -7/3 ≈ -2.333 | 2^(-1/6) ≈ 0.891 |
| Clarinet (d=2, n=1) | -5/2 | 3^(-1/4) ≈ 0.760 |

> **Validity scope (soliton column only).** The kink-mass formula
> `M_k = 8 σ √(K r)` is rigorous only at K ≈ 1 per
> `sine_gordon_substrate.md` "Validity scope" subsection. Propagation
> across the K-zoo assumes each cascade-locked sector hosts an
> analogous sine-Gordon reduction around its own locked sub-state.
> The fragmentation-slope column is independent and not affected by
> this caveat.

## Cross-links

- `master_cascade_identity.md`
- `imf_bowed_cascade.md`
- `sine_gordon_substrate.md` — soliton mass spectrum companion
- `baryon_fraction.md` — Z_6 structure for the conjectured Z_6 cascade
