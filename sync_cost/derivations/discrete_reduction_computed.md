# The discrete 4-mode reduction: computed

> **CANONICAL `S_v(K=1)` DOCUMENT.** This is the single source of
> truth for `S_v(K=1)` and the full history of the thread. Every
> prior value (`16`, `13`, `0<S_v<16`, `≈16`) is recorded once, in
> the "What this supersedes" table below — *not* re-litigated
> per-doc. Other docs (`nonperturbative_phase2.md`,
> `e_cross_discrete_resolution.md`, `inflation_duration.md`,
> `discrete_reduction_problem.md`) point here for the value rather
> than carrying their own supersession arcs.

The "real Phase 2" — the explicit discrete-lattice computation of
the 4×4 reduction matrix at K=1, done by hand (and verified
numerically). This delivers the long-queued calculation that
`nonperturbative_phase1.md` deferred, `nonperturbative_phase2.md`
assumed, and `discrete_reduction_problem.md` posed.

**Result: `S_v(K=1) ≈ 11.5` (Planck units), from a finite hand
sum, no integrals. This supersedes every prior value (`16`, `13`,
`0<S_v<16`, `≈16`).** The diagonal is direction-asymmetric
(`H_BB ≠ H_CC`, confirming `discrete_reduction_problem.md`'s
finding), and the discrete crossing term is `E_cross = −4` exactly
— a finite bounded matrix element, confirming
`e_cross_discrete_resolution.md`'s prediction that the continuum
`−2 M_k = −16` was a representation artifact.

## Setup

Substrate Hamiltonian on the discrete Klein-bottle lattice at K=1
(`σ = m = r = K = 1`, Planck-audit units):

    H = Σ_sites [ ½ p² + ½(Δ_x φ)² + ½(Δ_y φ)² + (1−cos φ) ]

Minimal kink-fills-loop lattice. The four XOR-surviving modes
(`figure_eight.md` D19):

| Mode | Sector | Excitation |
|---|---|---|
| **A** | (2,3) both locked | `φ ≡ 0` |
| **B** | (2,3), q₂=3 unlocked | full 2π kink in **periodic-y**, 3 sites |
| **C** | (3,2), q₁=3 unlocked | π **half-twist** in **antiperiodic-x**, 3 sites |
| **D** | (3,2), q₁=3 & q₂=2 unlocked | q₁=3 antiperiodic half-twist **+** q₂=2 periodic-y kink **+** crossing |

The key structural input: **the periodic-y direction's minimal
excitation is a full 2π kink; the antiperiodic-x direction's
minimal excitation is a π half-twist** (`xor_derivation.md`:
antiperiodic-x → half-integer wavenumbers; the minimal antiperiodic
mode is the π half-twist, not a 2π kink). This is *why* B and C
differ.

## The diagonal — computed by hand

### H_AA (mode A, vacuum)

`φ ≡ 0`: every term zero. **`H_AA = 0`.** ✓

### H_BB (mode B: q₂=3 periodic kink, 2π over 3 sites)

`φ_n = 2πn/3`, n=0,1,2; periodic closure `φ_3 = 2π ≡ 0`.

- Gradient: 3 steps of `2π/3`. `E_grad = ½·3·(2π/3)² = 2π²/3`.
- Potential: `Σ_{n=0}^{2}(1−cos 2πn/3) = 0 + 3/2 + 3/2 = 3`.

**`H_BB = 2π²/3 + 3 ≈ 9.580`.**

### H_CC (mode C: q₁=3 antiperiodic half-twist, π over 3 sites)

The antiperiodic-x identification carries the half-twist
`φ(x+L_x) = φ(x) + π` (`xor_derivation.md` §7). The minimal
excitation is the π half-twist: `φ_n = πn/3`, n=0,1,2; closure
`φ_3 = π = φ_0 + π` ✓.

- Gradient: 3 steps of `π/3`. `E_grad = ½·3·(π/3)² = π²/6`.
- Potential: `Σ_{n=0}^{2}(1−cos πn/3) = 0 + ½ + 3/2 = 2`.

**`H_CC = π²/6 + 2 ≈ 3.645`.**

**`H_BB ≠ H_CC`** — quantified. The factor-≈2.6 difference is the
half-twist asymmetry: B is a *full 2π kink* in the periodic
direction; C is a *π half-twist* in the antiperiodic direction.
`discrete_reduction_problem.md`'s structural finding is now a
number: `9.580` vs `3.645`. The continuum-symmetric `E_B = E_C =
M_k = 8` is decisively an artifact.

### H_DD (mode D: q₁=3 antiperiodic half-twist + q₂=2 periodic kink + crossing)

D's components (note D's periodic excitation is **q₂=2**, not B's
q₂=3 — sector (3,2)):

**q₁=3 antiperiodic half-twist** (same as C's excitation):
`= π²/6 + 2 ≈ 3.645`.

**q₂=2 periodic-y kink** (2π over 2 sites): `φ_m = πm`, m=0,1;
closure `φ_2 = 2π ≡ 0`.
- Gradient: 2 steps of `π`. `E_grad = ½·2·π² = π²`.
- Potential: `Σ_{m=0}^{1}(1−cos πm) = 0 + 2 = 2`.
- `E(q₂=2 kink) = π² + 2 ≈ 11.870`.

**The discrete crossing term `E_cross`.** Product configuration
`φ(i,j) = φ_x(i) + φ_y(j)` on the 3×2 minimal lattice, `φ_x =
(0, π/3, 2π/3)`, `φ_y = (0, π)`. From the exact cross-term identity
(`e_cross_calc.md`, now as a **finite sum**):

    E_cross = Σ_{i,j}[ sin φ_x(i) sin φ_y(j)
                       − (1−cos φ_x(i))(1−cos φ_y(j)) ]
            = [Σ_i sin φ_x(i)][Σ_j sin φ_y(j)]
              − [Σ_i(1−cos φ_x(i))][Σ_j(1−cos φ_y(j))]

- `Σ_j sin φ_y(j) = sin 0 + sin π = 0` ⟹ **the sin–sin term
  vanishes exactly** (the q₂=2 kink has `φ_y ∈ {0, π}`,
  `sin = 0` at both).
- `Σ_i(1−cos φ_x(i)) = 0 + ½ + 3/2 = 2`.
- `Σ_j(1−cos φ_y(j)) = 0 + 2 = 2`.

    **E_cross = 0 − (2)(2) = −4**   (exact, finite, no integral)

This is exactly the finite bounded matrix element
`e_cross_discrete_resolution.md` predicted — *not* the continuum
`−2 M_k = −16` (which `e_cross_calc.md` flagged as a representation
artifact). The discrete `E_cross = −4` is finite and `|E_cross| <
M_k`, as the resolution doc anticipated.

**`H_DD = 3.645 + 11.870 + (−4) ≈ 11.515`.**

## The 4×4 matrix and S_v

Diagonal (Planck units, minimal lattice):

| | value |
|---|---|
| `H_AA` | 0 |
| `H_BB` | `2π²/3 + 3 ≈ 9.580` |
| `H_CC` | `π²/6 + 2 ≈ 3.645` |
| `H_DD` | `π²/6 + 2 + π² + 2 − 4 ≈ 11.515` |

Off-diagonal: single-excitation-flip amplitudes are Schwinger-
suppressed, `g ∼ exp(−S_excitation)`. The lightest excitation is
`H_CC ≈ 3.645`, so the largest off-diagonal is `∼ exp(−3.6) ≈
0.027` — small but not utterly negligible relative to the
`O(1)`-spaced diagonal. The off-diagonal corrections to the
eigenvalues are `O(g²/ΔE) ≲ 10⁻⁴`. The matrix is near-diagonal;
eigenvalues ≈ the diagonal.

**The vortex pair = mode D (the doubly-excited configuration). Its
energy/action relative to vacuum is the framework's `S_v`:**

    S_v(K=1) ≈ E_D ≈ 11.515   (Planck units)

with the explicit decomposition

    S_v = (q₁=3 antiperiodic half-twist: 3.645)
        + (q₂=2 periodic kink:        11.870)
        + (discrete crossing:         −4.000)
        = 11.515

## What this supersedes

The full `S_v(K=1)` arc, now terminated by a computed value:

| Stage | `S_v(K=1)` | Representation |
|---|---|---|
| `nonperturbative_phase2.md` | `= 16` exact | continuum, symmetric, assumed |
| `explicit_4x4_reduction.md` | `≈ 13` | continuum, collinear error |
| `dark_twin_correction.md` | `≈ 16` | continuum, orthogonal |
| `e_cross_calc.md` | `0 < S_v < 16` | continuum shadow (pathology) |
| `e_cross_discrete_resolution.md` | `≈ 16` | discrete, symmetric diagonal |
| `discrete_reduction_problem.md` | finite, `E_B ≠ E_C` | discrete, asymmetric (structural) |
| **this computation** | **`≈ 11.515`** | **discrete native, asymmetric, computed** |

The endpoint is **not 16**. It is `≈ 11.5`, computed by hand in
the framework's native discrete representation, with the full
asymmetric decomposition and the finite `E_cross = −4`. Every prior
value was either continuum (16, 13, 0<S_v<16) or used the
superseded symmetric diagonal (≈16). This is the first value
computed entirely in the native discrete representation with the
correct B/C asymmetry and finite crossing.

## Honest caveats

1. **Uniform-winding ansatz.** Each excitation uses the minimal
   forced profile (linear winding). This is an *upper bound* on
   the relaxed energy. On the strictly minimal lattice (2–3 sites
   per direction) the relaxation freedom is small, so `≈11.5` is
   close to the true minimal-lattice value, but a slightly larger
   lattice would relax the kink energies *downward* (toward, but
   staying above in the kink-fills-loop regime, the continuum
   `M_k`). So `S_v(K=1) ≲ 11.5`, with the true value somewhat
   lower if relaxation is allowed.
2. **Half-twist vs full-kink assignment — RESOLVED.** The B/C
   asymmetry rests on: periodic-y minimal excitation = 2π kink;
   antiperiodic-x minimal excitation = π half-twist. This was
   previously flagged as the key open structural input. It is now
   **closed affirmatively** — see "The half-twist assignment,
   resolved" below. The π-half-twist reading is forced by
   `xor_derivation.md` §3.3's homotopy theorem; a 2π x-winding is
   not the antiperiodic sector at all. `H_CC ≈ 3.645` and B≠C
   stand on a derived basis, not an assumption.
3. **Off-diagonal.** `∼ exp(−3.6)` for the C-flip; eigenvalue
   corrections `≲ 10⁻⁴`. Negligible for the leading value.
4. **Lattice size.** The minimal lattice (3 sites antiperiodic-x,
   {2,3} sites periodic-y) is the kink-fills-loop regime the
   framework commits to. A different lattice convention would
   shift the numbers; the *structure* (B≠C, finite E_cross,
   S_v < 16) is robust to that.

## The half-twist assignment, resolved (§3.3 homotopy theorem)

Caveat 2 — whether mode C's `q₁=3` antiperiodic-x excitation is a
π half-twist (`H_CC ≈ 3.645`) or a full 2π winding (`H_CC ≈
9.580`, which would collapse B≠C back to symmetric) — is the one
load-bearing structural input. It is **closed**, in favour of the
π half-twist, by `xor_derivation.md` §3.3.

§3.3 is a homotopy theorem about the physical field, not
frame-dependent bookkeeping: every continuous field on the Klein
bottle's antiperiodic-x direction decomposes as

    θ(x, y) = πx/L₁ + φ(x, y),   φ periodic in x.

The mandatory `πx/L₁` ramp accumulates exactly **π** traversing
the x-loop; periodic φ adds 0 net. So **every** antiperiodic-x
configuration accumulates net π (mod 2π) — the antiperiodic
sector is *defined* by this. A "2π integer x-winding" accumulates
0 (mod 2π): that is the trivial/periodic sector, **not the
antiperiodic one at all**. Hence "mode C = `q₁=3` unlocked in the
antiperiodic-x direction" *cannot* be a 2π kink; it must
accumulate π, realized minimally on the 3-site structure as
`φ_n = πn/3` (closure `φ₃ = π` ✓) — the π half-twist, `H_CC =
π²/6 + 2 ≈ 3.645`.

The apparent tension — `xor_derivation.md` §5.2's "odd `q₁` ⟺
integer wavenumber" — is **explicitly reconciled by §6.3**:
non-orientability lets the even denominator (`q₂=2`) carry the
*parity bookkeeping* while the physical π ramp stays in x. The
combinatorial label "`q₁=3` odd" indexes C's 3-fold Stern-Brocot
modulation; it does not relocate or cancel the §3.3 physical π
accumulation. The bookkeeping does not override the homotopy
theorem.

Therefore B≠C is grounded, not assumed: B is a net-2π kink in
the *periodic* direction (`H_BB ≈ 9.580`), C is a net-π
half-twist in the *antiperiodic* direction (`H_CC ≈ 3.645`); the
asymmetry *is* the half-twist-vs-full-kink distinction, forced by
§3.3. Mode D inherits the same resolution (its `q₁=3` component
is π in antiperiodic-x; its `q₂=2` component is a 2π kink in
*periodic*-y; `E_cross = −4`). `S_v(K=1) ≈ 11.515` stands on a
derived structural basis.

## Downstream consequences (bounded)

With `S_v(K=1) ≈ 11.5` (not 16):

- `f_exit = exp(−S_v) ≈ exp(−11.5) ≈ 1.0×10⁻⁵` (was `exp(−16) ≈
  10⁻⁷`). Larger exit fraction.
- inflation duration `≈ exp(S_v)/H_inflation ≈ exp(11.5)/H` —
  shorter than the `exp(16)/H` estimate by `exp(4.5) ≈ 90×`.
- The `inflation_duration.md` Finding-4 disposition (conditional on
  `K_inflation`, `S_v` K-dependent across epochs) **still stands** —
  this is the K=1 value specifically; the epoch-dependence is a
  separate, compounding point.

The cosmology layer remains bounded and now has a *computed* K=1
anchor (`S_v ≈ 11.5`) rather than the continuum-symmetric `16`.

## Status

Class 3 (computed, hand-derived, numerically verified). No new
primitive. The discrete 4-mode reduction is delivered:

- `H_AA = 0`, `H_BB = 2π²/3 + 3 ≈ 9.580`,
  `H_CC = π²/6 + 2 ≈ 3.645`,
  `H_DD = π²/6 + 2 + π² + 2 − 4 ≈ 11.515`.
- `E_cross = −4` exactly (finite; confirms
  `e_cross_discrete_resolution.md`).
- `S_v(K=1) ≈ 11.515`, superseding all prior values.

The single long-standing open computation of the `S_v` thread is
**closed**: a finite, hand-computed, numerically-verified value in
the framework's native discrete representation, with the full
asymmetric decomposition explicit. The one load-bearing structural
input (caveat 2, the half-twist assignment) is **resolved
affirmatively** by `xor_derivation.md` §3.3's homotopy theorem —
not merely flagged. The continuum-symmetric `16` is decisively
superseded; the framework's `S_v(K=1)` is `≈ 11.5`, an upper bound
that relaxation would lower slightly. This doc is the **canonical
`S_v(K=1)` source**; dependent docs point here rather than
carrying their own supersession arcs.

## Cross-links

- `discrete_reduction_problem.md` — posed this; its `E_B ≠ E_C`
  structural finding is now the numbers `9.580 ≠ 3.645`.
- `nonperturbative_phase2.md` — assumed symmetric `(0,8,8,16)`;
  superseded by the computed asymmetric `(0, 9.58, 3.65, 11.52)`.
- `e_cross_discrete_resolution.md` — predicted a finite bounded
  `E_cross`; confirmed `= −4` exactly.
- `e_cross_calc.md` — its continuum `−2 M_k = −16` is now
  definitively a representation artifact (discrete value: `−4`).
- `xor_derivation.md` — the antiperiodic→half-integer structure
  justifying C's π half-twist (vs B's 2π kink).
- `figure_eight.md` D19 — the four-mode sector definitions.
- `nonperturbative_phase1.md` — the kink-fills-loop minimal-lattice
  regime; this is its delivered computation.
- `inflation_duration.md` — downstream `S_v ≈ 11.5` shortens the
  inflation-duration estimate; Finding-4 disposition unaffected.

## One-line summary

Computed by hand in the native discrete representation:
`H_AA=0`, `H_BB≈9.58` (2π kink, periodic), `H_CC≈3.65` (π
half-twist, antiperiodic — `≠ H_BB`, the half-twist asymmetry
quantified), `E_cross=−4` exactly (finite, confirming the
continuum `−16` was an artifact), giving **`S_v(K=1) ≈ 11.5`** —
superseding `16` and every intermediate value, the `S_v` thread's
single open computation now closed.
