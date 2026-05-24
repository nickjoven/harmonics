# IMF Salpeter slope from the bowed cascade

The framework predicts the Salpeter high-mass IMF slope as

    α_Salpeter = -|F_4| / q_3 = -7/3 = -2.333…

vs. observed Salpeter α = -2.35 ± 0.05 (Bastian, Covey & Meyer 2010).
Residual: **0.33σ** — well within the observational band.

## Derivation

The bowed cascade is the gravitational fragmentation cascade in the
matter-sector K < 1 regime. It satisfies the master cascade-lock
identity at parameters `(d, n, b) = (q_3, 1, q_2)`:

    K_IMF^q_3 = q_2^(-1)
    K_IMF     = q_2^(-1/q_3) = 2^(-1/3) = 0.79370

The slope formula:

    α = -1 - log_2(2/K)
      = -1 - log_2(2 · 2^(1/q_3))
      = -q_2 - 1/q_3

Substituting q_2 = 2, q_3 = 3:

    α = -2 - 1/3 = -7/3

The two pieces have distinct, framework-native provenance:

- **Baseline -q_2 = -2** (the `-1 - log_2(2)`). Derived from the Farey
  mode-counting measure (`farey_mass_baseline.py`): the mode count
  |F_n| ~ (3/pi^2) n^2 gives density dN/dq ~ q, and a locked mode's mass
  is its entrained tongue-width measure M ~ w(p/q) ~ 1/q^2 at K=1 (the
  "energy = synchronization cost" primitive), giving dN/dM ~ M^(-2).
  The "-1" is the dq/dM Jacobian, not an imported constant; the one
  load-bearing identification is mass = entrained measure (this is a
  third mass concept, distinct from the soliton kink mass ~ sqrt(Kr) and
  the ADM gravitational mass ~ sqrt(rho), and the only one with the
  measure-theoretic shape the slope needs).
- **Correction -n/d = -1/q_3** (the K-dependent part). d = q_3 = Klein-
  orbit count of F_3, n = 1 non-redundant antiperiodic flip
  (`imf_step2_klein_orbit.py`).

## Cascade-depth interpretation

The cascade depth `d = q_3` corresponds to the Klein-orbit count at
Stern–Brocot depth ≤ q_3. At depth ≤ 3:

- Boundary pair-orbit `{0/1, 1/1}`
- Depth-3 pair-orbit `{1/3, 2/3}`
- Fixed point `{1/2}`

Total: 3 distinct Klein orbits = q_3.

The Klein-flip count `n = 1` because exactly one pair-orbit
(`{1/3, 2/3}`) contributes a non-redundant Klein flip; the boundary's
flip is redundant with periodicity, and the fixed point contributes
zero.

## Stribeck experimental anchor

`RESULTS.md` documents that N = 3 is the critical chain length for
frequency conversion in the Stribeck lattice. This is exactly the
predicted cascade depth `d = q_3`.

The empirical N = 3 = q_3 correspondence is the structural lemma
that grounds the cascade-depth-as-Klein-orbit-count argument.

## Status

Class 2, gated on the pigeonhole audit. The two promotion gates:

1. **Pigeonhole audit on the slope identity — does not pass at α = 0.05.**
   `cascade_slope_check.py` gives p ≈ 0.10 for the Salpeter rung: a random
   slope in the permitted band [-2.5, -2.0] lands within 0.5σ of -2.35
   about 10% of the time. Suggestive, not decisive.
2. **Step-2 lemma (cascade depth = Klein-orbit count) — satisfied.**
   `imf_step2_klein_orbit.py`: under the canonical Klein involution
   r → 1-r, the Farey set F_{q_3} = F_3 has orbit count 3 = q_3 (the
   cascade depth d) and one non-redundant antiperiodic flip (the {1/3,2/3}
   pair; the boundary {0/1,1/1} is redundant with the y-periodic
   identification, the fixed point {1/2} carries none), so n = 1. Hence
   α = -q_2 - n/d = -7/3. The identity orbit_count(F_m) = m holds only for
   m ∈ {2,3,4}, selecting the small-denominator cascades and excluding the
   deeper Z_6 (d=6, orbit count 7) and K* (d=14) sectors.

Net: the structural gate is closed; promotion now waits only on a tighter
statistical case, which the p ≈ 0.10 pigeonhole result does not yet
provide.

## Cross-links

- `master_cascade_identity.md` — the (d, n, b) family
- `mass_function_family.md` — α across cascade depths
- `farey_mass_baseline.py` — -q_2 baseline from the Farey mode-count measure
- `mass_entrained_measure.md` — mass = entrained measure, from the cost functional
- `imf_step2_klein_orbit.py` — Step-2 lemma: depth = Klein-orbit count
- `cascade_slope_check.py` — slope vs. observed MF slopes + pigeonhole null
- `RESULTS.md` — Stribeck N = 3 empirical anchor
- `step3_step5_klein_proof.py` — parallel Klein-orbit-counting argument
  in CHAIN_KSTAR Step 3
