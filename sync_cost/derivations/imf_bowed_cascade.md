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

The two pieces have different status:

- **Baseline -q_2 = -2 — not dynamically grounded (null at the width step).**
  The cost functional gives mass ∝ physical tongue width
  (`mass_entrained_measure.md`), but reaching -2 needs that width to be the
  Farey weight 1/q^2. It is not: a complete K=1 staircase forces the width
  exponent β > 2 (else the tongues over-fill [0,1]), and measurement gives
  β ≈ 2.3, so the dynamical slope is -1 - 2/β ≈ -1.86, not -2
  (`farey_tongue_width_null.py`). The 1/q^2 that gives -2 is the
  combinatorial Stern–Brocot tree weight, not the physical width;
  `farey_mass_baseline.py` computes the slope under that combinatorial
  weight as a reference, not a dynamical derivation. (This does NOT touch
  the Farey **count** |F_n| ~ n^2 that underwrites Ω_Λ — that is pure
  combinatorics.)
- **Correction -n/d = -1/q_3** (the K-dependent part). d = q_3 = Klein-
  orbit count of F_3, n = 1 non-redundant antiperiodic flip
  (`imf_step2_klein_orbit.py`). This piece stands.

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
   about 10% of the time. The sharper held-out test (`held_out_slope_test.py`,
   Region-C Phase C #3) confirms low power: of 10 independent control
   slopes, none land within Salpeter's 0.017 gap of the informative -7/3
   rung (the only control near a rung sits at the pigeonhole-rich -2.0,
   matched by the initial-cluster MF). So the evidential weight is one
   un-replicated match (Salpeter), N = 1 — suggestive of real targeting,
   not statistically decisive. The ladder's range is too narrow and too
   sparsely populated by independent controls for the statistics alone to
   decide.
2. **Step-2 lemma (cascade depth = Klein-orbit count) — satisfied.**
   `imf_step2_klein_orbit.py`: under the canonical Klein involution
   r → 1-r, the Farey set F_{q_3} = F_3 has orbit count 3 = q_3 (the
   cascade depth d) and one non-redundant antiperiodic flip (the {1/3,2/3}
   pair; the boundary {0/1,1/1} is redundant with the y-periodic
   identification, the fixed point {1/2} carries none), so n = 1. Hence
   α = -q_2 - n/d = -7/3. The identity orbit_count(F_m) = m holds only for
   m ∈ {2,3,4}, selecting the small-denominator cascades and excluding the
   deeper Z_6 (d=6, orbit count 7) and K* (d=14) sectors.

Net: the structural derivation is **partial, not end-to-end**. What stands
is the combinatorial skeleton — the Farey **count** |F_n| ~ n^2 and the
Step-2 Klein-orbit count for the -1/q_3 correction — plus mass ∝ physical
tongue width and the q-independent binding ε. What does **not** stand is
the -q_2 baseline: it required the tongue width to be the Farey weight
1/q^2, and the physical critical width decays faster (β ≈ 2.3 > 2, forced
by the complete staircase; `farey_tongue_width_null.py`), giving a
dynamical slope ≈ -1.86, not -2. So -7/3 is not derived end-to-end; the
-7/3 vs Salpeter (0.33σ) match remains an empirical observation lacking a
grounded dynamical baseline. The rung stays Class 2 — now for a structural
reason (the baseline's mass↔width step is null), not only a statistical one.

## Cross-links

- `master_cascade_identity.md` — the (d, n, b) family
- `mass_function_family.md` — α across cascade depths
- `farey_mass_baseline.py` — -q_2 baseline from the Farey mode-count measure
- `mass_entrained_measure.md` — mass = entrained measure, from the cost functional
- `epsilon_residual.py` — q-independence of the per-captured binding ε
- `imf_step2_klein_orbit.py` — Step-2 lemma: depth = Klein-orbit count
- `cascade_slope_check.py` / `held_out_slope_test.py` — pigeonhole + held-out null
- `cascade_slope_check.py` — slope vs. observed MF slopes + pigeonhole null
- `RESULTS.md` — Stribeck N = 3 empirical anchor
- `step3_step5_klein_proof.py` — parallel Klein-orbit-counting argument
  in CHAIN_KSTAR Step 3
