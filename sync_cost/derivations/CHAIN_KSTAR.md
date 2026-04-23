# K_STAR closed form

`K_STAR` is the matter-sector's coupling — the value that makes
the three sector ladders (charged leptons, up-type quarks,
down-type quarks) simultaneously self-consistent under the
generation law `m_{g+1}/m_g = b_1^{d · a_1}`. Its canonical
determination is the joint inverse-variance fit of the three
sectors against PDG 2024 mass ratios:

    K_STAR = 0.86196052                (five-digit joint fit)
    K_STAR_lep = 0.86196057 ± 2.06e-5  (lepton-only, tau-mass-limited)

This document describes a six-step closed-form derivation of
`K_STAR` from framework primitives plus the canonical Klein
bottle topology, ending in the algebraic identity

    K_STAR^14 = q_2^(-q_3) = 1/8

which is consistent with PDG 2024 at 0.594 σ and implies a
forward prediction for the tau lepton mass at ~22 parts per
billion precision (inherited from the muon mass reference).

The chain is a conditional derivation: if the closed form holds
exactly, each step in the chain is forced by canonical
framework L0/L1/L3 structure. Whether the closed form holds
exactly is a precision question, testable by future tau mass
measurements.

## The chain

### Step 1 — `q_2 = 2`

The framework's primary prime. L1 canonical, derived from the
cross-link uniqueness theorem `q_2² − 1 = q_3, q_3² − 1 = q_2³`
whose unique integer solution is `(q_2, q_3) = (2, 3)`
(see `mass_sector_closure.md`). `q_2 = 2` is the order of the
Z₂ factor in the Klein parity `Z_6 = Z_2 × Z_3` and the base of
the octave-scale exponential used throughout.

### Step 2 — `N_lep = q_2² = 4`

The lepton sector's phase-state count. From the Klein bottle's
signature (3,1): {locked, unlocked}² gives four phase states,
three observable (at least one channel locked) and one dark
(both channels unlocked, coupling averages to zero). See
`klein_bottle.md §"Minkowski signature"` and
`FRAMEWORK_TOPOLOGY.md` L1. This is NOT the
integer-conservation-law "lepton depth" from L3 (which is 3 for
leptons); it is the Klein four-group's order from L1 signature.

### Step 3 — Framework Farey index = 4

The Farey index at which the framework's rational phase
structure lives. Derived from the Klein bottle's canonical
antiperiodic identification:

    (0, y) ~ (1, 1 − y)

Projected onto the y-coordinate alone, this gives the
involution `y → 1 − y`. Restricted to rationals in `F_n`, this
is `r → 1 − r`, an involution that preserves `F_n` for every
`n ≥ 1`.

For `n ≥ 2` the involution has exactly one fixed point (`r =
1/2`) and `(|F_n| − 1)/2` pair orbits. The unique `n` at which
the orbit decomposition is `(3 pairs, 1 fixed)` is `n = 4`:

    n = 1: 1 pair, 0 fixed
    n = 2: 1 pair, 1 fixed
    n = 3: 2 pairs, 1 fixed
    n = 4: 3 pairs, 1 fixed     ← matches signature (3,1)
    n = 5: 5 pairs, 1 fixed

The match to signature (3,1) is unique and forced by counting.
`F_4 = {0/1, 1/4, 1/3, 1/2, 2/3, 3/4, 1/1}` with orbits
`{0, 1}, {1/4, 3/4}, {1/3, 2/3}` and fixed point `1/2`.

See `step3_step5_klein_proof.py` §(B) for the explicit
derivation and the unique-match verification.

### Step 4 — `|F_4| = 7`

Elementary number theory: `|F_n| = 1 + Σ_{k=1}^n φ(k)` where φ
is Euler's totient. For `n = 4`, `|F_4| = 1 + 1 + 1 + 2 + 2 = 7`.

### Step 5 — EDO basis = `q_2 · |F_4| = 14`

The framework's natural divisor for the `q_2`-interval (octave)
at framework Farey index 4. Derived from the Klein bottle's
two mode-bearing coordinate directions.

The Klein bottle has independent mode structures in its periodic
(`y`, time-like) and antiperiodic (`x`, space-like) directions.
From `klein_bottle.md §"Mode analysis"`, each direction supports
a Stern-Brocot mode lattice at the framework's Farey index,
giving total rational phase position count

    |F_d|_x + |F_d|_y = 2 · |F_d|

At `d = 4`: `2 · 7 = 14`. The factor `q_2 = 2` is literally "the
Klein bottle has two directions."

An equivalent reading uses the Stern-Brocot tree's self-duality
under `x → 1/x`: the subharmonic subtree on `[0, 1]` and the
harmonic subtree on `[1, ∞)` each contain `|F_d|` nodes, joined
at the self-conjugate root `1/1`. Counting each side
independently gives `2 · |F_d|`. See
`scratch/connection_tree.py` for the supporting intuition. Both
readings yield the same 14.

### Step 6 — `K_STAR = 2^{-q_3 / (q_2 · |F_4|)} = 2^{-3/14}`

The closed-form value of `K_STAR`. Equivalently,

    K_STAR^14 = 2^(-3) = 1/8 = q_2^(-q_3)

This is a single algebraic identity relating `K_STAR`, `q_2`,
`q_3`, and the integer 14 from Step 5. The `q_3 = 3` in the
exponent is the second framework prime; the step index `-3`
means `K_STAR` sits at `−q_3` steps in a 14-EDO basis
(fourteen equal logarithmic divisions of the `q_2`-interval).

This is the load-bearing conjecture. Steps 1–5 derive the
integer 14 from Klein topology; Step 6 asserts that `K_STAR` is
located at `-q_3` steps in this 14-basis without independent
derivation. It is a precision claim, not a structural one.

See `octave_doubling.py` (scratch) for the algebraic
equivalences and `step3_step5_klein_proof.py` for the full
derivation chain.

## PDG verification

From `K_star_precision_check.py`, computing `K_STAR_lep` from
PDG 2024 `m_τ = 1776.86 ± 0.12 MeV`, `m_μ = 105.6583755 ±
2.3e-6 MeV` via `K = 2/a_1` with `a_1 = log(m_τ/m_μ)/(d · log(3/2))`:

    K_STAR_lep (PDG 2024)  = 0.8619605739 ± 2.06e-5
    K_STAR_lep^14          = 0.1249751
    1/8                    = 0.1250000
    gap                    = -2.49e-5
    n_sigma                = 0.594

The relation `K^14 = 1/8` holds at 0.594 σ of the PDG-derived
value. Sub-1 σ but not definitive. Precision is dominated by
the tau mass uncertainty (68 ppm of `m_τ`). The individual
experiments that enter the PDG average:

| experiment   | m_τ (MeV)        | K_STAR       | K^14 − 1/8  | n_σ  |
|--------------|------------------|--------------|-------------|------|
| KEDR 2007    | 1776.80 ± 0.23   | 0.86197089   | −3.93e-6    | 0.05 |
| BaBar 2009   | 1776.68 ± 0.43   | 0.86199151   | +3.80e-5    | 0.25 |
| Belle 2007   | 1776.61 ± 0.37   | 0.86200355   | +6.24e-5    | 0.48 |
| PDG 2024 avg | 1776.86 ± 0.12   | 0.86196057   | −2.49e-5    | 0.59 |
| BESIII 2014  | 1776.91 ± 0.16   | 0.86195198   | −4.23e-5    | 0.78 |

`K^14 = 1/8` requires `m_τ ≈ 1776.789 MeV`. KEDR 2007 sits at
0.049 σ from this value. BESIII 2014 sits at 0.776 σ from it
(and pulls the PDG average up). A future measurement at `σ <
0.03 MeV` resolves the question.

## Forward prediction: tau lepton mass

From `tau_mass_prediction.py`, assuming the closed form Step 6
holds exactly:

    K_STAR        = 2^(-3/14)
    a_1(lep)      = 2 / K_STAR = 2^(17/14)
    m_τ / m_μ     = (3/2)^(3 · 2^(17/14)) = 16.816354951480701 …
    m_τ           = m_μ × 16.81635495
                  = 1776.78875 ± 3.87e-5 MeV

The framework precision (22 parts per billion) is inherited
from the muon mass reference (9-digit PDG value); the
relative `σ(m_τ)/m_τ = σ(m_μ)/m_μ`. This is ~3100× tighter
than the current experimental precision on `m_τ` (68 ppm).

## Status and blockers

**Derived from canonical L0/L1/L3 framework objects (structural):**

- Step 1 `q_2 = 2`
- Step 2 `N_lep = 4`
- Step 3 Framework Farey index = 4
- Step 4 `|F_4| = 7`
- Step 5 EDO basis = 14 = q_2 · |F_4|

These steps derive the *integer 14* from Klein topology. All
five are structural; no fitted factors.

**Class 2 coincidence (2026-04-23 audit):**

- Step 6 `K_STAR^14 = 1/8 = q_2^{−q_3}` at 0.594σ vs PDG.

**Audit finding.** Step 6 asserts K_STAR sits at index `−q_3`
in the 14-EDO basis. By the framework's own description above,
this is *"a precision claim, not a structural one"*. Testing
candidate exponents built from framework integers:

| Candidate | Value | K^14 target |
|---|---|---|
| `q_2^{−q_3} = 1/8` | 0.125 | 0.12498 ✓ |
| `q_3^{−q_2} = 1/9` | 0.111 | 0.854 ✗ |
| `q_2^{−(q_3−1)} = 1/4` | 0.25 | 0.912 ✗ |
| `q_2^{−(q_3+1)} = 1/16` | 0.0625 | 0.814 ✗ |

Only `q_2^{−q_3}` is within 1% of observation. No framework
argument forces *this* combination over the alternatives, so
Z2 does not close — the exponent choice is an ansatz.

**Demoted** from Proposed (Class 4) to Class 2 coincidence in
`numerology_inventory.md`, analogous in status to the d_eff =
80/27 ansatz (0.5σ, null on three mechanisms) and to the
Pythagorean comma vs K_Greene 0.17% near-match.

**Observational disposition.** The 2028-horizon precision
target `σ(m_τ) < 0.03 MeV` at Belle II / BESIII is no longer a
scorecard-promotion gate (since Step 6 is now Class 2). A
future central value agreeing with `1776.789 MeV` would tighten
the coincidence but would not convert it to a derivation
without closing Z2; a divergent central value would simply
confirm the coincidence's disposition.

Steps 1–5 are unaffected.

## Load-bearing files

| file | role |
|---|---|
| `step3_step5_klein_proof.py` | derivation of Steps 3 and 5 from Klein L0 topology |
| `tau_mass_prediction.py` | the forward prediction for `m_τ` from Step 6 and `m_μ` |
| `K_star_precision_check.py` | PDG verification of `K^14 = 1/8` at 0.594 σ |
| `framework_constants.py` | canonical framework numerical values |
| `klein_bottle.md` | L0 canonical Klein bottle topology |
| `FRAMEWORK_TOPOLOGY.md` | L0–L5 dependency map |
| `mass_sector_closure.md` | joint-fit `K_STAR` determination and generation law |

The exploratory scripts used to surface this structure are in
`scratch/` alongside a README that indexes them. They are not
required reading.
