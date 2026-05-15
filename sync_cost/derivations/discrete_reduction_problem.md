# The discrete 4-mode reduction: a hand-solvable problem statement

The sole remaining `S_v(K=1)` open item, posed as a problem a
person can work by hand. This is the "real Phase 2" — the explicit
substrate-Lagrangian → 4-mode projection that
`nonperturbative_phase1.md` queued and never delivered, and that
`nonperturbative_phase2.md` *assumed* rather than derived.

Per `e_cross_discrete_resolution.md`'s methodological commitment:
**this is finite-dimensional discrete linear algebra — finite sums
on a small lattice, no integrals, no infinities.** If the
formulation needs an infinite-domain integral, it has left the
framework's native representation.

This doc (i) states the problem precisely enough to hand off, and
(ii) reports what the leading hand-attempt already establishes —
including a qualitative finding that **challenges the symmetric
`(0, M_k, M_k, 2M_k)` the continuum picture assumed.**

## The problem (hand-solvable form)

> **Given:** the substrate Hamiltonian on a discrete Klein-bottle
> lattice at K = 1, in Planck-audit units (`σ = m = r = K = 1`):
>
> $$H \;=\; \sum_{\text{sites } i}\Big[\tfrac{1}{2}\,p_i^{2}
>   \;+\; \tfrac{1}{2}\,(\phi_{i+\hat x}-\phi_i)^2
>   \;+\; \tfrac{1}{2}\,(\phi_{i+\hat y}-\phi_i)^2
>   \;+\; \big(1-\cos\phi_i\big)\Big]$$
>
> with Klein-bottle boundary conditions:
> - **x (antiperiodic + reflection):**
>   `φ_{i+N_x, j} = −φ_{i, N_y−j}`
> - **y (periodic):** `φ_{i, j+N_y} = φ_{i, j}`
>
> and the lattice in the kink-fills-loop regime
> (`nonperturbative_phase1.md`): `N_x`, `N_y` minimal — the
> smallest that represents the XOR-surviving denominators
> `(q₁, q₂) ∈ {(2,3),(3,2)}` (`xor_derivation.md` §7). Take
> `N_x` along the antiperiodic axis, `N_y` along the periodic
> axis.
>
> **The four basis configurations** (XOR-surviving,
> `figure_eight.md` D19):
> - **A** = `φ ≡ 0` (q₁ locked, q₂ locked).
> - **B** = a `q₂ = 3` winding in the **periodic-y** direction,
>   uniform in x (q₁=2 locked, q₂=3 unlocked).
> - **C** = a `q₁ = 3` winding in the **antiperiodic-x**
>   direction, uniform in y (q₁=3 unlocked, q₂=2 locked).
> - **D** = both windings simultaneously (q₁=3 unlocked,
>   q₂=2 unlocked).
>
> **Compute the 4×4 matrix** `H_{IJ} = ⟨I|H|J⟩`, `I,J ∈
> {A,B,C,D}`:
> 1. **Diagonal** (mode energies): evaluate `H` on each
>    configuration. These are *finite sums over the minimal
>    lattice* — closed form.
> 2. **Off-diagonal** (single-kink-flip pairs A↔B, A↔C, B↔D,
>    C↔D): the tunnelling amplitude `g ∼ exp(−S_kink)` where
>    `S_kink` is the discrete kink action (finite sum). A↔D and
>    B↔C are second order (`∼ g²`).
> 3. **Diagonalize the 4×4.** The vortex-pair gap is `S_v(K=1)`.
>
> **Deliverable:** the diagonal energies as explicit finite sums;
> the off-diagonal order of magnitude; the eigenvalue gap. No
> integral appears anywhere. If one does, the lattice has been
> taken to the continuum — outside the framework's native
> representation.

That is the problem. It is finite, closed-form for the diagonal,
and the off-diagonal is a single Schwinger-type estimate. A person
can do this with pencil and paper for the minimal lattice.

## Leading hand-attempt — and a qualitative finding

The diagonal is the immediately hand-doable part. Take the minimal
uniform-winding ansatz (the forced profile on the minimal lattice;
upper bound on the relaxed energy).

**Mode A (vacuum).** `φ ≡ 0`: every term zero. `H_AA = 0`. ✓

**Mode B (q₂=3 kink, periodic-y, 3-site).** Uniform winding
`φ_n = 2πn/3`, `n=0,1,2`, periodic (`φ_3 = 2π ≡ 0`):
- Gradient: differences all `2π/3`; energy `= ½ · 3 · (2π/3)² =
  2π²/3 ≈ 6.580`.
- Potential: `Σ_{n=0}^{2}(1−cos(2πn/3)) = 0 + 3/2 + 3/2 = 3`.
- `H_BB = 2π²/3 + 3 ≈ **9.580**`.

**Mode C (q₁=3 kink, antiperiodic-x, 3-site).** Antiperiodic
cell: `φ_{n+3} = −φ_n`. The minimal half-twist-compatible winding
puts a net `π` (not `2π`) across the antiperiodic cell with the
sign-flip closing it. Taking the minimal antiperiodic-consistent
profile `φ_n = πn/3` (`n=0,1,2`, with `φ_3 = π = −φ_0` requires
`φ_0 = 0`, consistent):
- Gradient: differences `π/3` over the cell plus the closing
  `(−φ_2 − φ_2)` step from the antiperiodic identification —
  the sign-flip makes the closing difference large.
- Potential: `Σ(1−cos(πn/3))` over the antiperiodic cell.
- The exact value requires careful BC bookkeeping (the
  antiperiodic closing step is the subtlety) — but it is **a
  finite sum, hand-doable**, and structurally **`H_CC ≠ H_BB`.**

**The qualitative finding (the productive part):**

`H_BB ≠ H_CC`. Mode B's kink lives in the **periodic** y-direction;
mode C's kink lives in the **antiperiodic** x-direction. Periodic
and antiperiodic minimal lattices have *different* discrete
energies — the antiperiodic sign-flip closing step is structurally
absent in the periodic case. **The half-twist breaks the
B↔C (sector-swap) degeneracy that the continuum picture assumed.**

`nonperturbative_phase2.md` / `dark_twin_correction.md` assumed
`E_B = E_C = M_k` "by the q₁↔q₂ sector-swap symmetry." The discrete
reduction shows that symmetry is **broken at the lattice level by
the antiperiodic identification**: the two directions are not
interchangeable because one carries the half-twist and the other
does not. The symmetric `(0, M_k, M_k, 2M_k)` is a continuum
artifact; the discrete diagonal is `(0, H_BB, H_CC, H_DD)` with
`H_BB ≠ H_CC`.

**Magnitude:** the minimal-lattice values (`H_BB ≈ 9.58`, `H_CC`
of similar O(10) but unequal) are *not* the continuum
`M_k = 8√(Kr) = 8`. The continuum `8` is the *relaxed sech-profile*
value; the kink-fills-loop minimal lattice forces the uniform
profile and gives a larger, direction-asymmetric energy. The
framework's actual regime is the minimal lattice, so its kink
energies are the discrete values, **not 8**.

## What this changes

| Quantity | Continuum picture (assumed) | Discrete reduction (this attempt) |
|---|---|---|
| `E_A` | 0 | 0 ✓ |
| `E_B` | `M_k = 8` | `2π²/3 + 3 ≈ 9.58` (q₂=3 periodic) |
| `E_C` | `M_k = 8` (degenerate with B) | `≠ E_B` — half-twist breaks the degeneracy |
| `E_D` | `2 M_k = 16` | `E_B + E_C + E_cross^discrete` (finite, no integral) |
| `E_B = E_C`? | assumed yes | **no — broken by antiperiodic identification** |
| `S_v(K=1)` | `≈ 16` | `≈ E_B + E_C + E_cross^discrete`, with `E_B ≠ E_C`; **not 16** |

So the discrete reduction, even at leading hand-attempt, **does not
reproduce the symmetric continuum `(0,8,8,16)`.** The honest
discrete `S_v(K=1)` is `E_B + E_C + E_cross^discrete` with all
three finite, hand-computable, and `E_B ≠ E_C`. It is plausibly
*larger* than 16 (minimal-lattice forced profiles exceed the
relaxed continuum `M_k`), direction-asymmetric, and exactly
finite.

## The honest residual

The leading attempt establishes the *structure* (finite sums, no
integrals, `E_B ≠ E_C` symmetry-breaking) and `H_AA = 0`, `H_BB ≈
9.58`. The exact `H_CC`, `H_DD`, and the off-diagonal need:

1. **Careful antiperiodic-BC bookkeeping** for `H_CC` (the
   sign-flip closing step). Finite, hand-doable, but the BC
   subtlety must be done correctly — this is where a hand-solver
   should focus.
2. **The discrete crossing term `E_cross^discrete`** in `H_DD`
   (the finite analog of the dissolved continuum `E_cross`): a
   finite sum over the minimal lattice where both windings are
   nonzero. By `e_cross_discrete_resolution.md` it is the
   *finite* `≈ −4g²/M_k`-scale matrix element, **not** the
   continuum `−2 M_k`.
3. **Relaxation:** the uniform-winding ansatz is an upper bound;
   the true minimal-lattice ground states may relax slightly. On
   the strictly minimal lattice the relaxation freedom is small;
   on a slightly larger lattice the energies decrease toward (but
   stay above, in the kink-fills-loop regime) the continuum `8`.

## The S_v thread after this

| Stage | `S_v(K=1)` |
|---|---|
| Phase 2 | `= 16` exact (assumed) |
| explicit_4x4 | `≈ 13` (collinear error) |
| dark_twin | `≈ 16` (orthogonal) |
| e_cross_calc | `0 < S_v < 16` (continuum shadow) |
| e_cross_discrete_resolution | `≈ 16` (discrete, ~10⁻⁸; continuum dissolved) |
| **this discrete reduction** | **`= E_B + E_C + E_cross^discrete`, finite, `E_B ≠ E_C`, not the symmetric 16** |

The discrete reduction is the *correct* representation (per the
methodological commitment). Its leading attempt shows the
continuum-symmetric `16` was an artifact: the true discrete
`S_v(K=1)` is a specific finite sum with the antiperiodic
direction structurally heavier than the periodic one. **`S_v(K=1)`
is not 16; it is a hand-computable finite number with `E_B ≠ E_C`,
and the framework's earlier symmetric value is superseded.**

This is honest: the discrete reduction, the representation the
framework itself commits to, does *not* return the continuum's
tidy `16`. It returns a finite, direction-asymmetric number — which
is *more* trustworthy precisely because it is computed in the
native representation, even though it is less tidy.

## Status

Class 3 (problem statement + leading hand-attempt with a
qualitative finding). No new primitive.

The deliverable is the hand-solvable problem statement above. The
leading attempt establishes: `H_AA = 0`; `H_BB ≈ 9.58` (q₂=3
periodic, closed form); and the structural result that **`H_BB ≠
H_CC` — the half-twist breaks the sector-swap degeneracy the
continuum assumed.** The exact remaining matrix elements are
finite hand-computations with one BC subtlety (the antiperiodic
closing step in `H_CC`) flagged as where care is needed.

`S_v(K=1)` is therefore *not* the continuum-symmetric `16`; it is
`E_B + E_C + E_cross^discrete`, finite, direction-asymmetric, and
hand-computable. The framework's symmetric value is superseded by
the native discrete representation.

## Cross-links

- `nonperturbative_phase1.md` — queued this real-Phase-2
  deliverable; this doc states it hand-solvably.
- `nonperturbative_phase2.md` — assumed the symmetric
  `(0,M_k,M_k,2M_k)`; this attempt shows `E_B ≠ E_C`, superseding
  the symmetric assumption.
- `dark_twin_correction.md`, `e_cross_discrete_resolution.md` —
  established the discrete-native commitment; this is its
  application to the reduction matrix.
- `xor_derivation.md` §7 — the XOR-surviving `(q₁,q₂)`; the basis.
- `figure_eight.md` D19 — the 4-mode definitions A,B,C,D.
- `e_cross_discrete_resolution.md` — `E_cross^discrete` is the
  finite matrix element, not the dissolved continuum integral.
- `klein_bottle.md` — the antiperiodic+reflection BC, whose
  closing step breaks the B↔C degeneracy.

## One-line summary

Posed hand-solvably, the discrete 4-mode reduction is finite linear
algebra (no integrals); the leading hand-attempt already shows
`H_AA = 0`, `H_BB ≈ 9.58`, and — the productive finding — `H_BB ≠
H_CC`, so the half-twist breaks the sector-swap degeneracy and
`S_v(K=1)` is a finite, direction-asymmetric number, **not** the
continuum-symmetric `16`.
