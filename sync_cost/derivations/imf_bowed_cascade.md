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

The slope formula (cascade with mass-halving per stratum):

    α = -1 - log_2(2/K)
      = -1 - log_2(2 · 2^(1/q_3))
      = -q_2 - 1/q_3

Substituting q_2 = 2, q_3 = 3:

    α = -2 - 1/3 = -7/3

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

Class 2 (gated). Promotes to full Class 2 when:

1. Pigeonhole audit on the slope identity passes.
2. The Step-2 lemma (cascade depth = Klein-orbit count) gets a formal
   writeup parallel to `step3_step5_klein_proof.py`.

## Cross-links

- `master_cascade_identity.md` — the (d, n, b) family
- `mass_function_family.md` — α across cascade depths
- `RESULTS.md` — Stribeck N = 3 empirical anchor
- `step3_step5_klein_proof.py` — parallel Klein-orbit-counting argument
  in CHAIN_KSTAR Step 3
