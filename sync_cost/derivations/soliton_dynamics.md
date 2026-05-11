# Soliton dynamics: linear sector, breathers, S-matrix, medium class

Dynamics companion to `sine_gordon_substrate.md`. The parent doc derives
sine-Gordon from the framework Lagrangian and the static kink solution
`M_k = 8 σ √(K r)`. It leaves four open items (`sine_gordon_substrate.md`
"Status" → "What this does not yet establish"). This doc closes three of
them — the linear-wave sector, the kink–antikink exchange structure, and
the medium-class assignment — and tightens the fourth (sector
identification) into a sharper falsifier.

No new primitives. Each section uses standard sine-Gordon results with
framework substitutions applied.

## 1. Linear-wave sector (the "meson" gap and dispersion)

Linearise the framework-Lagrangian sine-Gordon equation

    m ∂²_t φ − σ² ∂²_x φ + K r sin(φ) = 0

around the locked vacuum φ = 0. With `sin(φ) ≈ φ`,

    m ∂²_t φ − σ² ∂²_x φ + K r φ = 0

Plane waves `φ = exp(i(k x − ω t))` give

    ω²(k) = c² k² + ω_0²,
        c² = σ²/m,    ω_0² = K r / m

This is a Klein–Gordon dispersion. The substrate has a **mass gap**

    m_meson = ℏ ω_0 = ℏ √(K r / m)

and a propagation speed `c = σ / √m` set by the gradient-stiffness
ratio. Two structural consequences follow without further input:

**(a) The meson gap inherits the K-zoo `√K` ladder.** At fixed `r`,

    m_meson(K) / m_meson(K=1) = √K = b^(-n/(2d))

(`master_cascade_identity.md` slope-formula instances). The linear
sector and the soliton sector share the *same* cross-sector ratio
`√K`; they are not independent predictions.

**(b) The kink width and the meson Compton length coincide.** The kink
width is `ℓ = c / ω_0 = √(σ² / (K r m))` (`sine_gordon_substrate.md`
line 92). The meson reduced Compton length is `λ̄ = ℏ / (m_meson c) =
ℏ / (σ √(K r) · √m / √m) = ℏ / (σ √(K r))`, which equals `ℓ` up to the
ℏ factor that distinguishes the classical from the quantum scale. The
two scales are not independent.

This closes the *first* of the parent doc's structural gaps: there is
a linear sector, it has a mass gap, the gap and the kink are bound
together by the same substrate primitives, and both sectors share the
master-cascade `√K` ladder.

## 2. Breather tower

Sine-Gordon admits, in addition to the kink, a continuous family of
**breather** bound states — localised kink–antikink oscillations. In
the quantised theory the breather mass spectrum is

    M_n = 2 M_k sin(n π γ / 16),    n = 1, 2, …, N_max

with

    γ = β̃² / (1 − β̃² / 8π)

where `β̃²` is the renormalised dimensionless coupling and
`N_max = ⌊8π / β̃²⌋`. At the "free-fermion" point `β̃² = 8π`, no
breathers exist (the model becomes a free massive Dirac fermion under
the Coleman correspondence). Below it, finitely many breathers exist.

### β̃² in framework primitives

The classical action in the locked sector reads (`sine_gordon_substrate.md`
line 53)

    S[φ] = ∫ dx dt [ (m/2)(∂_t φ)² − (σ²/2)(∂_x φ)² + K r cos(φ) ]

Putting it into the canonical sine-Gordon form
`S = (1/β̃²) ∫ dx̃ dt̃ [ ½(∂φ̃)² + m_0² cos(φ̃) ]` by rescaling
`t̃ = ω_0 t`, `x̃ = x / ℓ` (with `ℓ = c/ω_0` and `c²=σ²/m`, `ω_0²=Kr/m`)
and tracking the action prefactor `ℏ` yields

    β̃² = ℏ ω_0 ℓ / σ² ·  (per-mode normalisation)
        = ℏ / (σ √(K r m) · ℓ)  ·  ℓ²
        = ℏ / σ²  ·  √(σ² / (K r m))
        = ℏ / σ  ·  (K r m)^(−1/2)
        = ℏ / (σ √(K r m))

That is: in framework natural units (where the coefficients in the
substrate Lagrangian are taken as the natural units of action and
length), `β̃²` is set entirely by the substrate primitives
`(σ, K, r, m)`. It is not a free parameter.

> **Bookkeeping caveat.** The β̃² prefactor depends on the normalisation
> convention used to canonicalise the kinetic term and on whether ℏ is
> being carried explicitly. The structural statement (β̃² is fixed by
> the substrate, not free) is independent of those conventions; the
> exact numerical coefficient requires fixing the framework's unit
> convention end-to-end with `unitless_check.md`. Tracked as Open 1
> below.

### Consequences

1. **N_max is determined by the substrate, not adjustable.** Once the
   unit convention is pinned down, the number of breathers at each
   cascade depth follows. In particular, whether the locked-state
   (K = 1) sector hosts a free-fermion point — which would deny it a
   breather spectrum entirely — is a substrate-internal question, not
   an empirical input.
2. **Breather masses inherit `√K` ratios at small N.** In the
   semiclassical regime (β̃² → 0, many breathers), `M_n ≈ n m_meson`
   for small `n`, so each breather rung scales as `m_meson ∝ √(K r)`.
   The breather tower and the kink mass move together across the
   K-zoo.
3. **A second, independent prediction emerges.** Whereas
   `master_cascade_identity.md`'s soliton implication gives one ratio
   per cascade pair (`M_k(K_a)/M_k(K_b) = √(K_a/K_b)`), the breather
   tower at fixed cascade gives a *whole ladder*
   `M_1 : M_2 : … : M_{N_max}` constrained by `sin(nπγ/16)`. A
   falsifier on either ladder is independent.

## 3. Kink–antikink exchange (the S-matrix)

The parent doc names "loop-traversal time" (Open 2) as the global
K↔K̄ conversion mechanism on the Klein bottle. That is a *coordinate*-
antiperiodicity effect — kink at one end of the antiperiodic loop,
antikink at the other. It leaves untouched the **local** exchange
dynamic: two solitons in the bulk, scattering or annihilating.

Sine-Gordon in 1+1D is an integrable QFT. Its two-body S-matrix was
derived by Zamolodchikov & Zamolodchikov (1979) from the minimal
solution of crossing + unitarity + the Yang–Baxter equation. There
are three independent two-body amplitudes:

    S_{KK}(θ),     kink–kink elastic
    S_T(θ),        kink–antikink transmission
    S_R(θ),        kink–antikink reflection

all parametrised by a single quantity `ξ = π β̃² / (8 − β̃²)`
("renormalised coupling") and the rapidity `θ`. Bound-state poles of
`S_T` reproduce the breather masses derived in section 2. The
ratios

    S_T(θ) / S_R(θ),    S_R(0)

are pure numbers fixed by `ξ` — they do not depend on the kink mass
or the substrate scale.

### Framework reading

Since `β̃²` is substrate-determined (section 2), so is `ξ`, and so is
the entire elastic K–K and K–K̄ S-matrix at each cascade depth. The
framework has **no free parameter** in the soliton scattering sector.
That is unusually rigid: any future identification of a K = 1 sector
soliton observable (e.g., a massive Z₂ excitation in the gravitational
sector — `sine_gordon_substrate.md` Open 1) brings with it a *prediction
for its self-scattering amplitude*, not just its mass.

### Cross-sector exchange (open)

For a K = 1 kink scattering off a K = 2^(−1/3) ("bowed-cascade")
kink, the situation changes. Each cascade sector hosts its own
sine-Gordon reduction around its own mean phase `ψ_n` (the working
assumption flagged at `sine_gordon_substrate.md` lines 76–86). A
cross-sector scattering process needs a sector-boundary action — a
substrate-level tunnelling between distinct cascade-locked
configurations — for which the framework currently has only the
master-identity *static* structure, not a dynamical bridge.

The structural conjecture: the cross-sector tunnelling rate is
exponentially suppressed in the cascade-distance `|d_a − d_b|`,

    Γ_{a→b} ∝ exp(−S_inst(d_a, d_b)),

with `S_inst` set by the action cost of the cascade transition in
`master_cascade_identity.md`. This is **not** derived here. It is the
sharpest open piece of the soliton sector — tracked below as Open 2.

## 4. Medium class: kinks are contrabass-pitches

`medium_change_demo.md` partitions framework predictions into three
classes:

| Class | Source of frequency | Example |
|---|---|---|
| **Tuba** | medium-dependent | `H_0`, `c`, `c_air` |
| **Contrabass** | structure-locked | `Ω_Λ = 13/19`, `sin²θ_W = 8/35` *(failed — see `figure_eight.md`)*, `K_c = 2/π` |
| **Loudspeaker** | externally driven | post-hoc-fitted SM parameters |

The kink mass `M_k = 8 σ √(K r)` decomposes as:

| Factor | Source | Medium class |
|---|---|---|
| `8` | sech² integral | structural, dimensionless |
| `σ` | gradient stiffness of substrate spatial topology | structural anchor (mechanical, contrabass-side) |
| `K` | cascade depth, fixed by `master_cascade_identity.md` triples | structural (combinatorial) |
| `r` | order parameter at full lock, `r → 1` | structural (self-consistent fixed point) |

Every factor sits on the structural side. **The kink is a contrabass-
pitch**: its mass *ratio* across the K-zoo (the dimensionless quantity
`b^(-n/(2d))`) is the same for every observer at every cosmic epoch,
and the meson gap, breather tower, and S-matrix ratios inherit the same
class.

The kink's absolute mass `M_k` carries a `σ` factor — a dimensional
anchor which an observer at a different cascade depth would scale by
the local `σ`. The relationship is exactly the bowed-string formula
`f = (n/2L) √(T/μ)`: the integer-mode-number-style structural piece
(`√K`, `n` for breathers) is universal; the anchor (`σ`) sits on the
mechanical/structural side, so it is medium-invariant under any
ordinary "swap the substrate medium" comparison — there is no
*surrounding* medium to swap, by construction.

### Falsifier sharpened

`sine_gordon_substrate.md` already records (Falsifiers, line 238):

> A measured soliton-spectrum mass ratio crossing two K-zoo sectors
> that disagrees with `√(K_a / K_b)` falsifies either the master
> identity or the sine-Gordon reduction.

The medium-class assignment sharpens this:

- The falsifier holds for **every observer** at **every cosmic epoch**.
  It is not contingent on local cosmology or units. Any observation of
  a cascade-crossing soliton spectrum disagreeing with `√(K_a/K_b)` —
  in any reference frame, at any redshift — falsifies the framework.
- Conversely, a *frame-dependent* deviation would *not* falsify the
  cascade structure; it would re-identify the spectrum as a tuba-class
  observable misclassified as contrabass-class.

This is the standard frame-discipline cross-link of `medium_change_demo.md`
applied to soliton physics: it tells the empiricist what *kind* of
deviation falsifies what *kind* of claim.

## Status

Class 3 (derivation grade) for sections 1, 3, and 4. The linear
dispersion is exact under linearisation of the parent equation; the
S-matrix structural-rigidity claim is a direct reading of
Zamolodchikov 1979 with framework primitives substituted; the medium-
class assignment is a direct reading of the primitives in
`M_k = 8 σ √(K r)`.

Section 2 is Class 3 modulo the unit-convention bookkeeping caveat:
the structural claim (`β̃²` fixed by substrate, N_max not free) is
robust, but the explicit numerical coefficient awaits the framework's
end-to-end unit pinning per `unitless_check.md`.

### What this **does** establish

- A linear-wave sector exists, with a Klein–Gordon dispersion and a
  mass gap `m_meson = ℏ√(Kr/m)` that inherits the master cascade's
  `√K` ladder.
- The breather tower and the kink–antikink S-matrix are entirely fixed
  by the substrate; there are no free parameters in the local elastic
  soliton-sector dynamics.
- The kink (and meson, and breather) sector is contrabass-class;
  cross-sector ratios are observer-independent and epoch-independent.

### What this does **not** yet establish (open)

1. **Unit-convention pinning of β̃².** The structural statement
   (β̃² determined by substrate) is established; the explicit
   coefficient — and hence the absolute count `N_max` of breathers at
   each cascade depth — requires the framework's complete unit
   convention as audited by `unitless_check.md`. This is a single
   bookkeeping item, not a derivation gap.
2. **Cross-sector tunnelling action `S_inst(d_a, d_b)`.** The local
   in-sector dynamics are fully fixed; inter-cascade exchange is
   conjectural. The right computation is a Euclidean instanton bouncing
   between two cascade-locked vacua of `master_cascade_identity.md`.
   This is the sharpest open piece.
3. **Sector-to-observable identification.** Inherited from
   `sine_gordon_substrate.md` Open 1. The contrabass-class assignment
   tightens *what kind of observable* counts as a successful match, but
   does not name the observable.
4. **Beyond-1+1D corrections.** Sine-Gordon's integrability is a
   strictly 1+1D feature. Higher-dimensional substrate excitations
   admit kink-string and kink-sheet generalisations whose stability
   and scattering structure is well outside the closed-form Zamolodchikov
   regime. Tracked as a separate thread.

## Falsifiers

- **Meson gap ratio.** A measured meson-class excitation in two cascade
  sectors with mass ratio incompatible with `√(K_a / K_b)`: falsifies
  the linear-sector identification (and either the master identity or
  the sine-Gordon reduction).
- **Breather tower presence/absence.** If the K = 1 sector is found to
  permit (forbid) a breather spectrum incompatible with the substrate-
  determined `N_max`: falsifies the bookkeeping of section 2 or the
  underlying β̃²(σ, K, r, m) relation.
- **S-matrix ratios.** Any measured deviation of `S_T(θ) / S_R(θ)` or
  `S_R(0)` from the Zamolodchikov form at substrate-determined `ξ`
  falsifies the sine-Gordon reduction *or* the integrability assumption
  (i.e., reveals an unmodelled non-integrable correction).
- **Frame-dependence of cross-sector ratios.** Any observation that the
  ratio `M_k(K_a)/M_k(K_b)` depends on the observer's reference frame
  or cosmic epoch falsifies the contrabass-class assignment and rebuts
  the cross-sector structural identification.

## Cross-links

- `sine_gordon_substrate.md` — parent doc, source Lagrangian reduction
  and static kink. This doc adds the linear sector, breathers, S-matrix,
  and medium class.
- `master_cascade_identity.md` — K-zoo identity that supplies the
  cross-sector `√K` ratio inherited here by the meson, breather, and
  kink towers.
- `medium_change_demo.md` — three-class partition (tuba / contrabass /
  loudspeaker) into which the soliton sector is here assigned.
- `unitless_check.md` — the unit-convention audit that closes Open 1
  by pinning the explicit coefficient in `β̃²(σ, K, r, m)`.
- `klein_bottle.md`, `klein_bottle_derivation.md` — substrate topology;
  the Z₂-graded global kink↔antikink mechanism that the local S-matrix
  here complements rather than replaces.
- `einstein_from_kuramoto.md` — locked-state expansion at K = 1, the
  validity scope under which section 1's linearisation is rigorous.
- `framework_lagrangian.py` — substrate Lagrangian primitives (σ, K, r,
  m) and the Euler–Lagrange equation linearised in section 1.
