# Master cascade-lock identity

The framework's K-values across multiple sectors satisfy a single
parameterized identity:

    K^d = b^(-n)

with `(d, n, b)` drawn from framework primitives `{q_2, q_3, |F_n|}`.
Three exact instances are confirmed; one suggestive instance is pending
verification.

## Confirmed instances

| Instance | K | (d, n, b) | Source |
|---|---|---|---|
| Matter-equilibrium | 0.86196052 | (q_2·\|F_4\|, q_3, q_2) = (14, 3, 2) | `CHAIN_KSTAR.md` |
| Bowed cascade (IMF) | 0.79370 = 2^(-1/3) | (q_3, 1, q_2) = (3, 1, 2) | Phase II derivation |
| Clarinet (q_3) cascade | 0.57735 = 3^(-1/2) | (q_2, 1, q_3) = (2, 1, 3) | Phase II clarinet-correction |
| Gravity boundary | 1 | (—, 0, —) | trivially, n = 0 limit |

## Suggestive instance (verification pending)

| Instance | K | Conjectured (d, n, b) | Source |
|---|---|---|---|
| Quantum-gravity interpolation | 0.892 | (q_2·q_3, 1, q_2) = (6, 1, 2)? | `quantum_gravity_interpolation.md` |

The conjectured form predicts K = 2^(-1/6) = 0.89090, differing from the
cited 0.892 by 0.18%. If verified exactly, this is the |Z_6|-cascade
fixed point: one Klein flip across the full Z_6 depth.

## Slope formula

For each cascade instance, the implied mass-function slope is

    α = -q_2 - n/d

| Instance | α | Observable |
|---|---|---|
| K = 1 (string) | -2 | Press–Schechter halo MF, GC MF |
| K = 2^(-1/6) (Z_6 cascade, conjectured) | -13/6 ≈ -2.167 | subhalo MF? |
| K = 2^(-1/3) (bowed) | -7/3 ≈ -2.333 | Salpeter IMF (0.33σ) |
| K = 3^(-1/2) (clarinet) | -5/2 | predicted, untested |
| K* matter equilibrium | -31/14 ≈ -2.214 | matter-sector running, not fragmentation |

## Numerical validation (Continuation 1)

Coupled van der Pol chain experiments confirm the master identity on
independent dynamics:

| Drive ratio | Critical chain length | Predicted | Match |
|---|---|---|---|
| 2:1 (octave, q_2) | N = 3 | q_3 = 3 | ✓ |
| 3:1 (twelfth, q_3) | N = 2 | q_2 = 2 | ✓ |

The Stribeck cascade (octave-base) and the van der Pol cascade
(twelfth-base) share the master-identity structure with cascade-base =
drive ratio, cascade-depth = the other prime. Numerics in
`clarinet_lattice.py`, results in `RESULTS.md` (Experiment 3).

## Soliton-sector implication

The same K-zoo also fixes a **soliton-mass spectrum** through a
different mechanism. `sine_gordon_substrate.md` derives sine-Gordon
as the substrate's effective theory by expanding around the locked
mean phase, with kink mass `M_k = 8 σ √(K r)` in framework natural
units. The kink mass scales as `√K`, so cross-sector ratios

    M_k(d, n, b) / M_k(K=1) = b^(-n/(2d))

are fixed by the same `(d, n, b)` triples that define the master
identity. This is structurally distinct from the fragmentation-slope
family (`mass_function_family.md`) but uses the same K-zoo as the
substrate-side input — two different mass relations on one set of
cascade fixed points.

## Open

1. Pigeonhole audit on the 3-instance family — joint false-positive
   rate at the small-integer search space `{(d,n,b): d ∈ [1,20],
   n ∈ [0,q_3], b ∈ {q_2, q_3, q_2 q_3}}`.
2. Verification that 0.892 is exactly 2^(-1/6) structurally derived,
   not just an empirical fit.
3. Search for additional instances at hadronic-sector depths (potential
   route for Phase I unblock).

## See also

- `CHAIN_KSTAR.md` — matter-equilibrium derivation, the original instance
- `imf_bowed_cascade.md` — bowed instance, Phase II
- `mass_function_family.md` — fragmentation-slope family across observables
- `sine_gordon_substrate.md` — soliton-mass spectrum (`M_k ∝ √K`) on the
  same K-zoo
- `down_type_double_cover_phase_d.md` — companion structural piece
