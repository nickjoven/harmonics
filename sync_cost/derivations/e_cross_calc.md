# E_cross calculation: the textbook route gives a pathology

> **SUPERSEDED (2026-05) by `e_cross_discrete_resolution.md`.**
> This doc's continuum `E_cross = −2 M_k` pathology and its
> `0 < S_v(K=1) < 16` bound are **representation errors**: they
> compute a fundamental discrete substrate quantity through the
> framework-foreign continuum shadow (infinite-domain integrals).
> In the framework's native discrete 4-mode representation,
> `E_cross ≈ −5×10⁻⁸` and `S_v(K=1) ≈ 16` to ~`10⁻⁸`. Read this
> doc as the recorded continuum-route attempt; read
> `e_cross_discrete_resolution.md` for the resolved result and the
> (different, well-posed) residual open item.

Item 1 of the remaining bounded work: compute `E_cross`, the
crossed-sine-Gordon jog energy at the q₁/q₂ orthogonal kink
intersection on the Klein bottle (`orthogonal_kink_interaction.md`).
The proposed route was importing the textbook crossed-soliton
(dislocation-junction) formalism.

**Honest outcome: the textbook infinite-domain route gives a clean
but pathological result (`E_cross = −2 M_k`, which zeros out
`E_D`). The pathology is informative — it confirms the
kink-fills-loop regime invalidates the infinite-domain formula and
sharpens the open item to a specific finite-volume calculation.**

This continues the session pattern: each step productive, including
the steps whose product is "this approach fails for *this specific
reason*, so the harder method is required."

## The setup

Mode D's two orthogonal kink lines (`figure_eight.md` D19;
`dark_twin_correction.md`): q₁ kink `φ₁(x)` (antiperiodic-x,
dark-coupled), q₂ kink `φ₂(y)` (periodic-y, matter). Separable
ansatz `φ = φ₁(x) + φ₂(y)`.

The gradient energy has **no cross term** (`φ₁` depends only on x,
`φ₂` only on y, so `∇φ₁ · ∇φ₂ = 0`). The entire interaction comes
from the potential cross-term:

    ΔV = V(φ₁+φ₂) − V(φ₁) − V(φ₂),    V(φ) = K r (1 − cos φ)

Expanding with `cos(φ₁+φ₂) = cos φ₁ cos φ₂ − sin φ₁ sin φ₂` and
simplifying (set `a = 1−cos φ₁`, `b = 1−cos φ₂`):

    ΔV / (K r) = sin φ₁ sin φ₂ − (1 − cos φ₁)(1 − cos φ₂)

This vanishes wherever either kink is at vacuum (`φ = 0, 2π`), so
`ΔV` is localized at the crossing — as a jog energy should be.

## The factorization

Because `φ₁ = φ₁(x)` and `φ₂ = φ₂(y)` separate:

    E_cross = K r { [∫ sin φ₁ dx][∫ sin φ₂ dy]
                    − [∫ (1−cos φ₁) dx][∫ (1−cos φ₂) dy] }

Two integrals over the standard sine-Gordon kink
`φ_kink(x) = 4 arctan(e^{x/ℓ})` (`sine_gordon_substrate.md` line 91):

**(i) `∫ sin φ_kink dx`.** With `t = e^{x/ℓ}`,
`sin φ_kink = 4t(1−t²)/(1+t²)²`, `dx = ℓ dt/t`:

    ∫_{−∞}^{∞} sin φ_kink dx = 4ℓ ∫_0^∞ (1−t²)/(1+t²)² dt
                             = 4ℓ [ 2·(π/4) − (π/2) ] = **0**

The sin–sin cross term **vanishes exactly** by kink symmetry
(positive over the first half of the kink, negative over the
second).

**(ii) `∫ (1−cos φ_kink) dx`.** Using the standard identity
`1 − cos φ_kink = 2 sech²(x/ℓ)` (`sine_gordon_substrate.md` line
102–103):

    ∫_{−∞}^{∞} 2 sech²(x/ℓ) dx = 2 · 2ℓ = 4ℓ

At K = r = 1, `ℓ = ℓ_kink = 1` (Planck units): `= 4`. (Consistent:
this is the potential half of `M_k = 8`, i.e. `M_k/2 = 4`.)

## The result — and the pathology

    E_cross = K r { [0]·[0] − [4]·[4] } = **−16**   (Planck units, K=1)

`E_cross = −16 = −2 M_k` exactly (since `M_k = 8`). Therefore:

    E_D = 2 M_k + E_cross = 16 + (−16) = **0**

**This is pathological.** It would make mode D (both directions
unlocked) energetically degenerate with mode A (vacuum). Two
crossed kink lines cannot perfectly cancel their own combined
tension; a doubly-excited state is not the vacuum. The clean
`−2 M_k` is a signal, not a physical answer.

## Diagnosis: the infinite-domain formula is invalid here

The pathology's origin is precise. `∫(1−cos φ_kink) dx = 4` is the
integral over the **full infinite line**. But the framework's
compact Klein bottle is in the **kink-fills-loop regime**:
`L_x = ℓ_kink = 1` (`nonperturbative_phase1.md`). The kink profile
`4 arctan(e^{x/ℓ})` spreads its `(1−cos)` weight over `~±2ℓ`; on a
loop of length `ℓ` the integral is cut off far below 4.

So the textbook crossed-soliton route — which I proposed importing
from dislocation-junction physics in
`orthogonal_kink_interaction.md` — gives `−2 M_k` **only because it
uses infinite-domain kink integrals**. In the framework's actual
compact regime those integrals are truncated, and the true
`E_cross` is *not* `−16`.

**This is the same kink-fills-loop regime issue that recurred
throughout the audit thread** (`s_v_nlo_attempt.md`,
`audit_findings_3_4_disposition.md`, `explicit_4x4_reduction.md`):
infinite-domain soliton formulas systematically fail when
`L_x = ℓ_kink`. The textbook import is *insufficient*; the calc
requires genuine finite-volume sine-Gordon.

## The sharpened open item

`E_cross` is **not** computable by the textbook (infinite-domain)
crossed-soliton formula — that route gives a pathological `−2 M_k`.
The honest open item is now specific:

> Compute `E_cross` as the crossed-kink interaction energy on the
> compact Klein bottle at `L_x = L_y = ℓ_kink` (finite volume),
> via either:
> (a) finite-volume sine-Gordon TBA (Mussardo and collaborators'
>     cylinder/torus machinery, adapted to the Klein-bottle
>     antiperiodic identification), or
> (b) direct lattice numerics on a small Klein-bottle grid with
>     crossed-kink boundary conditions.
>
> The infinite-domain factorization gives `−16 = −2 M_k`; the
> finite-volume value is bounded `|E_cross| < 2 M_k` (the loop
> cutoff strictly reduces `∫(1−cos)` below 4) and is the genuine
> correction.

The bound from this calc is actually useful: since the
finite-volume `∫(1−cos φ)dx` over a length-`ℓ` window is strictly
less than the infinite value 4, **`|E_cross| < 16`**, and since
`E_cross < 0` (the `(1−cos)(1−cos)` term is strictly negative, the
sin–sin term vanishes), we have:

    −16 < E_cross < 0    ⟹    0 < E_D = 2 M_k + E_cross < 16
    ⟹    0 < S_v(K=1) < 16

So the calc *does* produce a result: **`S_v(K=1)` is strictly less
than 16, strictly greater than 0**, with the infinite-domain limit
(`S_v → 0`) being the unphysical boundary. The honest leading
estimate `S_v ≈ 16` (from `dark_twin_correction.md`) is the
*upper* bound; the true value is somewhere in `(0, 16)`, pulled
down by an attractive crossing interaction whose magnitude requires
the finite-volume calc.

## What this changes

| Claim | Before this calc | After |
|---|---|---|
| `E_cross` route | "import textbook crossed-soliton" | **textbook (infinite-domain) route gives pathological `−2 M_k`; finite-volume required** |
| `E_cross` sign | undetermined | **strictly negative (attractive)** — the `(1−cos)(1−cos)` term, sin–sin vanishes |
| `S_v(K=1)` | `≈ 16` leading | **`0 < S_v < 16`**; 16 is the upper bound, true value pulled down by attractive crossing |
| Open item | "compute `E_cross`" (vague) | **"finite-volume crossed-kink energy on the compact Klein bottle"** (specific: TBA or lattice) |

The `S_v ≈ 16` of `dark_twin_correction.md` is now understood as an
**upper bound**, not a leading estimate. The crossing interaction
is attractive and strictly lowers `S_v`. The framework's `S_v` is
in `(0, 16)`; pinning it requires the finite-volume calc.

## Consequences (bounded, not pathological)

The downstream cosmology numbers shift but stay bounded:

- `f_exit = exp(−S_v)` with `0 < S_v < 16`: `f_exit > exp(−16) ≈
  10⁻⁷`. The exit fraction is *larger* than the prior estimate
  (attractive crossing lowers the barrier).
- inflation duration `≈ exp(S_v)/H_inflation` with `S_v < 16`:
  *shorter* than the `≈10⁻³²` s upper estimate. Still bounded; the
  Finding-4 disposition (conditional on `K_inflation`, K-dependent
  `S_v`) compounds with this.
- The framework's cosmology is now an *interval* prediction
  (`S_v ∈ (0,16)`, narrowing once the finite-volume calc lands),
  not a point. This is honest: a bounded open quantity, not a
  pathology and not a false-precision claim.

## Status

Class 3 (calc attempt with informative negative result + a usable
bound). No new primitive. The textbook crossed-soliton route was
attempted honestly; it produces a pathological infinite-domain
`−2 M_k`, which (i) confirms the kink-fills-loop regime invalidates
infinite-domain formulas (consistent with the recurring audit
finding) and (ii) yields the rigorous bound `0 < S_v(K=1) < 16`
with the crossing strictly attractive. The genuine value requires
finite-volume sine-Gordon (TBA or lattice) — the open item, now
specific.

## Cross-links

- `orthogonal_kink_interaction.md` — proposed the textbook import;
  this doc shows it gives a pathology and sharpens the open item.
- `dark_twin_correction.md` — `S_v ≈ 16` now understood as the
  *upper bound*, not a leading estimate.
- `nonperturbative_phase1.md` — the kink-fills-loop regime
  (`L_x = ℓ_kink`) that invalidates the infinite-domain formula.
- `s_v_nlo_attempt.md`, `audit_findings_3_4_disposition.md`,
  `explicit_4x4_reduction.md` — the recurring kink-fills-loop
  regime issue, here recurring again with the same root cause.
- `sine_gordon_substrate.md` — the kink profile and the
  `1−cos = 2 sech²` identity used in the integrals.
- `substrate_determinism.md` — unaffected; this is an energy
  calc, orthogonal to the determinism fork.

## The honest one-line summary

The textbook crossed-soliton route gives `E_cross = −2 M_k`
(pathological, from infinite-domain integrals invalid in the
compact regime), but the attempt yields the rigorous bound
**`0 < S_v(K=1) < 16`** with the crossing **strictly attractive** —
so `S_v ≈ 16` is an *upper* bound, and the true value awaits a
finite-volume sine-Gordon calculation, now the specific remaining
open item.
