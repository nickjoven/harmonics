# K(t): the table — problem statement for the cosmological coupling trajectory

Single entry point for the one remaining cosmological frontier. Consolidates
the scattered K(t) material (`k_of_t_friedmann.md`, `continuity_in_K_nulls.md`,
`era_timeline_disposition.md`, `master_cascade_identity.md`,
`inflation_seam_anchor_closure.md`) and integrates the FRW-transform
localization (`frw_staircase_transform.py`). This is scaffolding, not a
solution.

## 0. The correct object: a discrete cascade, not a continuous K(t)

"K(t)" is **not** a continuous RG-like running to be derived. Per
`continuity_in_K_nulls.md`: no Survives-class result requires a continuous
`w(z)`/`K(z)` (they are all combinatorial or fixed-K/ground-state), and the
matter-sector "running" is the **discrete cascade** `K_n^d = b^{-n}`
(`master_cascade_identity.md`). The K=1↔K<1 non-smoothness is a Class-5
*feature* (it forces two-anchor minimality), not a gap to smooth. So the
object is: the universe's passage through the **discrete cascade stations**,
and the open question is the **map from station to physical epoch/energy**.

## 1. What is settled (the fixed points the trajectory runs between)

- **Endpoint K → 1** — the de Sitter equilibrium / locked `r≡1` branch
  (`K_eff = d/2 = 3/2 > K_c`, stable; `k_of_t_friedmann.md` S1–S2 closed).
  The late-time attractor.
- **Stations K_n = b^{-n/d}** — the cascade fixed points (master identity):
  bowed `2^{-1/3}`, clarinet `3^{-1/2}`, Z₆ `2^{-1/6}`, K* `≈0.862`. Forced;
  the depths `d` are Klein-orbit-grounded (`imf_step2_klein_orbit.py`).
- **Floor K_c = 2/π** — the synchronization onset; below it, no global
  coherence (`farey_tongue_width_null.py`, the staircase argument).
- **Ordering — structural.** The inflation→matter→Λ sequence is a forced
  discrete cascade between forced endpoints, along the forced arrow
  (inviolable #9), via the Farey slip-order (`era_timeline_disposition.md`
  tier 1). Needs no continuous `w(K)`.
- **Schedule — anchor-declined.** Absolute durations/times/temperatures are
  out-of-class (need `H_0`; #INF, `inflation_seam_anchor_closure.md`). NOT
  to be derived.

## 2. The one open residual

The **K_eff ↔ epoch/energy map**: which physical epoch `a` (redshift `z`,
energy) each discrete station `K_n` sits at. This is the single genuine
Class-2 residual (`era_timeline_disposition.md` tier 3 = the "K↔energy
map"). The FRW transform (`frw_staircase_transform.py`) localized the entire
cosmological mass-function slope to exactly this map: the redshift kinematics
preserve `D ≈ 0.87` and `β ≈ 2.3`, so the slope is set **only** by the
station↔epoch map — and a *free* map gives any slope. **The map must be
forced to be predictive.**

## 3. Obstructions — what the map CANNOT be (catalogued nulls)

- **N10:** K is not a running synchronization order parameter. The
  r-iteration converges to the superstable `r = 0` fixed point; `K_STAR`
  sits in the disordered phase. So the map is **not** an order-parameter
  flow (no Kuramoto-`K_c` running); any `Ω_m(K)` must come from *fixed-K
  populations*, not K-running (`k_of_t_friedmann.md` S3).
- **N11:** the tongue-coverage proxy `w(K)` is discontinuous (caps at 0.138
  for `K<1`, jumps to 1 at `K=1`), non-monotone, never reaching target. The
  direct substrate `w(K)` proxy fails structurally. The map is not this.
- **N17:** the map is **not forced by preserving the invariant `D ≈ 0.87`**.
  An embedding relabels the scale axis `Ω → Ω^p`; box-counting dimension is
  bi-Lipschitz-invariant, so `D ≈ 0.87` survives for *every* exponent (spread
  0.017 across `p ∈ [0.6, 1.7]`; `geometric_forcing_null.py`). D-preservation
  is **vacuous** — it discriminates nothing, so it cannot force the map. This
  closes the "geometrically forced via the scale-relativistic invariant"
  route. (What *would* constrain the map is metric/curvature matching, not a
  topological invariant — but that carries one free rate, cascade-steps per
  FRW-expansion; whether that rate *is* the `n_s` e-fold rate is an open
  conjecture, not a result, and N12/S2 flags exactly this rate-conflation as
  a 27× ambiguity. The map stays Class-2.)

## 4. Acceptance criterion (what a solution must satisfy) — N9

A valid station↔epoch map must:
1. be produced **structurally** — forced by the framework, not a free
   function and not N10 iteration;
2. yield, via the FRW transform, a **dimensionless** cosmological prediction
   (mass-function slope, era partition);
3. **not smuggle in a scale** — the absolute schedule stays anchor-declined
   (Basepoint);
4. be consistent with the forced ordering (#9 arrow, Farey slip-order) and
   the forced endpoint (`K=1`).

## 5. The candidate, and the test

The discrete cascade `K_n^d = b^{-n}` itself is the structural candidate for
the map (`era_timeline_disposition.md` tier 3). The test datum is the
cascade↔Salpeter slope — **Class-2-gated, not promoted**. The win is a
*forced* assignment of stations to epochs that reproduces the observed
slope/partition; the failure mode is that the assignment is irreducibly free
(then the residual is genuinely Class-2 / anchor-side, and the framework
declines it).

## 6. Basepoint bright line

- **Allowed (structural):** the dimensionless station↔epoch map — which
  `K_n` ↔ which `a/z`, the relative ordering and spacing — forced by the
  cascade. A rate/dynamics, not a scale, so derivable in principle.
- **Declined (scale):** the absolute schedule (durations, times, `H(t)`),
  out-of-class by two-anchor minimality / #INF.
- **The warning (from the FRW transform):** a free map predicts nothing (any
  slope). Only a *forced* map predicts. So the bar is forcedness, not fit.

## 7. Win condition

A forced station→epoch map that, through the FRW transform, yields the
cosmological mass-function slope (and the era partition) as a dimensionless,
anchor-conditional prediction — promoting cascade↔Salpeter from Class-2-gated
to derivation. Or: an honest demonstration that the map cannot be forced from
the surviving primitives, leaving it permanently Class-2 (the framework
declines it, as it declines the schedule). Either outcome closes the frontier.

## Cross-links

- `master_cascade_identity.md` — the stations `K_n = b^{-n/d}`
- `k_of_t_friedmann.md` — S1–S2 closed; S3–S4 open (N10, N11)
- `continuity_in_K_nulls.md` — N9 acceptance criterion; continuous-K not a blocker
- `era_timeline_disposition.md` — three-tier disposition (ordering/schedule/map)
- `inflation_seam_anchor_closure.md` — #INF; schedule anchor-declined
- `frw_staircase_transform.py` — slope localized to the station↔epoch map
- `geometric_forcing_null.py` — N17: D-preservation is vacuous, does not force the map
- `imf_step2_klein_orbit.py` — the depths `d` are Klein-orbit-grounded
