# The explicit 4×4 reduction matrix: real Phase 2

> **CORRECTION NOTE (2026-05) — this doc over-corrected.**
> `dark_twin_correction.md` withdraws this doc's `S_v ≈ 13`
> retraction. Part A applied the **collinear** kink–antikink
> attraction `M_k exp(−L/ℓ)` to mode D, but mode D is **orthogonal**
> Klein-bottle kinks (q₁ antiperiodic/dark-coupled + q₂ periodic),
> not a collinear pair — the formula does not apply. Part C's
> "continuum contamination" was treating dark-sector wave-side
> twins as independent matter modes. With the matter/dark Z₂
> twinning, both concerns are withdrawn. **Corrected state:
> `S_v(K=1) ≈ 16` at leading order** (not `≈ 13`); "exact" still
> not claimable because the *orthogonal*-kink interaction is open
> (but it is parametrically distinct from the spurious collinear
> `≈ 3`). Read this doc as the recorded wrong turn; read
> `dark_twin_correction.md` for the corrected result.

The real Phase 2 deliverable, queued in `nonperturbative_phase1.md`
and not delivered in `nonperturbative_phase2.md` (which *assumed*
the 4-mode reduction and the energies `(0, M_k, M_k, 2 M_k)` rather
than deriving them from the substrate Lagrangian). Audit Finding 3
(`audit_findings_3_4_disposition.md`) qualified Phase 2's "exact"
claim pending this derivation.

This doc attempts the derivation. **Honest outcome: two of the
three pieces close; the third reveals the real open question.**

- **Part A** (kink-mode energies): **closes**. The energies
  `(0, M_k, M_k, 2 M_k)` are derivable from the sine-Gordon kink
  mass + kink counting. Phase 2's assumption was terse, not wrong.
- **Part B** (4×4 eigenvalues): **closes**. Within the 4-mode
  Hilbert space, `S_v = 16` is exact to ~10⁻⁸ precision.
- **Part C** (continuum-mode check): **reveals the open
  question**. At K=1, continuum modes are *interleaved* with the
  kink modes (lowest continuum mode ≈ 6.36, below `E_B = 8`). The
  4-mode reduction is not a clean truncation at K=1. Whether the
  continuum modes are *absorbed* (kink-fills-loop) or *independent*
  (Finding 3) requires a mixing calculation this doc does not
  perform.

The honest verdict sharpens the disposition: `S_v = 16` is exact
*within the kink sector*; the open question is the continuum
sector's status at K=1.

## Setup: the substrate Lagrangian at K=1

From `framework_lagrangian.py` Part 1, reduced to sine-Gordon
about the locked mean phase (`sine_gordon_substrate.md`):

    H = ∫ dx [ (1/2m) π² + (σ²/2)(∂_x φ)² + K r (1 − cos φ) ]

with `φ = θ − ψ` the deviation field, `π` its conjugate momentum.
At K=1 in Planck-audit convention (`σ = m = r = 1`):

    H = ∫ dx [ ½ π² + ½ (∂_x φ)² + (1 − cos φ) ]

Standard sine-Gordon. The 4 XOR-surviving modes
(`figure_eight.md` D19) are configurations of this field on the
Klein bottle, indexed by `(q₁, q₂)` lock state.

## Part A: kink-mode energies — DERIVED

The 4 modes correspond to kink content per direction:

| Mode | `(q₁, q₂)` | Kink content | Energy |
|---|---|---|---|
| A | (2 locked, 3 locked) | no kink either direction; `φ = 0` vacuum | `E_A` |
| B | (2 locked, 3 unlocked) | 1 kink in q₂ direction | `E_B` |
| C | (3 unlocked, 2 locked) | 1 kink in q₁ direction | `E_C` |
| D | (3 unlocked, 2 unlocked) | 1 kink each direction | `E_D` |

The "unlocked direction = one sine-Gordon kink" identification is
`sine_gordon_substrate.md`'s reading: an unlocked direction has the
deviation field winding by 2π (a kink), a locked direction has
`φ = 0` (no winding).

**E_A**: vacuum. `φ = 0` ⟹ `1 − cos 0 = 0`, gradient `= 0`,
momentum `= 0`. **`E_A = 0`** (reference). Derived.

**E_B**: one kink in q₂. The static sine-Gordon kink
`φ_kink(x) = 4 arctan(exp(x/ℓ))` has rest energy computed by the
standard `1 − cos φ_kink = 2 sech²((x−x₀)/ℓ)` identity
(`sine_gordon_substrate.md` lines 100–108):

    E_kink = ∫ [ (σ²/2)(∂_x φ_kink)² + K r (1 − cos φ_kink) ] dx
           = 8 σ √(K r)

At K=1, σ=r=1: **`E_B = M_k = 8`**. Derived from the Lagrangian
(this is `sine_gordon_substrate.md`'s already-derived kink-mass
formula, not an assumption).

**E_C**: one kink in q₁. By the sector-swap symmetry q₁ ↔ q₂
(`figure_eight.md`'s (2,3) ↔ (3,2) loop swap), `E_C = E_B = M_k =
8`. Derived (from the symmetry, which is itself a Klein-bottle
structural fact).

**E_D**: one kink each direction. At leading order (non-interacting
kinks in orthogonal directions on the Klein bottle), energies add:
**`E_D = 2 M_k = 16`**. The kink-kink interaction correction is
`−E_int` where `E_int ∝ M_k exp(−L_x/ℓ_kink)`; at K=1, `L_x =
ℓ_kink`, so `E_int ∝ M_k e⁻¹ ≈ 0.37 M_k ≈ 3`. **This is a real
correction at K=1** — `E_D = 2M_k − E_int ≈ 16 − 3 = 13`, not
exactly 16. See Part C.

**Part A result:** the energies `(E_A, E_B, E_C, E_D) = (0, 8, 8,
16)` are **derivable** from the sine-Gordon kink mass — *except*
`E_D`, where the K=1 kink-fills-loop regime gives a ≈ 3-unit
interaction correction Phase 2 neglected. Phase 2's `(0, 8, 8, 16)`
is the *non-interacting* leading order; the interacting value is
`(0, 8, 8, ≈13)`.

## Part B: the 4×4 Hamiltonian and S_v — DERIVED (within 4-mode space)

Off-diagonal couplings connect single-kink-transition pairs
(A↔B, A↔C, B↔D, C↔D) with amplitude `g` = single-kink nucleation
amplitude. A↔D and B↔C require two kink changes (second order;
≈ `g²`).

    H = | 0    g    g    0   |
        | g    8    0    g   |
        | g    0    8    g   |
        | 0    g    g    E_D |

By the q₁↔q₂ (B↔C) symmetry, eigenvalues split into symmetric and
antisymmetric subspaces. The antisymmetric mode is exactly at
`E = 8`. The symmetric 3×3 block (basis A, (B+C)/√2, D) has
characteristic polynomial whose vortex-pair-relevant gap is:

    gap = (highest eigenvalue) − (lowest eigenvalue)

For `E_D = 16` and `g ≪ M_k`:

    gap = 2 √(M_k² − 4g²) ≈ 2 M_k − 4g²/M_k

The single-kink amplitude `g`: the WKB nucleation factor
`g ∼ exp(−S_kink)` with `S_kink ≈ M_k × τ_kink ≈ 8`. So
`g² ∼ exp(−16) ≈ 10⁻⁷`, and the correction `4g²/M_k ≈ 5 × 10⁻⁸`.

**Part B result:** within the 4-mode Hilbert space, `S_v = gap ≈
2 M_k = 16` to ~10⁻⁸ precision. Phase 2's "exact within the 4-mode
space" claim is **correct** — the g-corrections are utterly
negligible. The eigenvalue structure is derived, not assumed.

## Part C: the continuum check — the REAL open question

Phase 2's "exact" claim requires the 4-mode space to be the
*complete* substrate Hilbert space at K=1. Is it?

In the kink-fills-loop regime (`L_x = ℓ_kink`,
`nonperturbative_phase1.md`), the continuum modes discretize:

    k_n = 2π n / L_x = 2π n   (Planck units, L_x = 1 at K=1)

with sine-Gordon meson dispersion (small-oscillation around
vacuum):

    ω(k) = √(c² k² + ω_0²) = √(k² + 1)   (K=1, r=m=c=1)

The lowest continuum mode (n=1):

    ω(2π) = √(4π² + 1) ≈ √(40.5) ≈ **6.36**

Compare to the kink-mode energies `(0, 8, 8, ≈13)`:

| Energy | Mode |
|---|---|
| 0 | A (vacuum) |
| **6.36** | **lowest continuum meson mode (n=1)** |
| 8 | B, C (single kink) |
| 12.7 | continuum n=2 |
| ≈13 | D (kink pair, with E_int correction) |

**The lowest continuum mode (≈6.36) sits BELOW the single-kink
modes (8).** The continuum is *interleaved* with the kink sector,
not separated above it.

This is exactly Finding 3's deeper point, now made quantitative.
The 4-mode reduction at K=1 is **not a clean truncation** — there
are continuum meson modes at comparable (and lower) energies than
the kink modes. The Phase 1 "kink-fills-loop ⟹ collapse to 4
modes" argument claimed the continuum modes are *absorbed* (mixed
into the kink modes). This doc's calc shows they are at *comparable
energy* to the kink modes (qualitatively consistent with "they
mix") but does **not** show they collapse to exactly 4 — that
requires an explicit mixing/diagonalization calculation across the
combined (kink ⊕ discretized-continuum) Hilbert space, which is
not performed here.

## Honest verdict

| Piece | Status |
|---|---|
| Kink-mode energies derivable | **Yes** (Part A) — but `E_D ≈ 13`, not 16, at K=1 (kink-fills-loop interaction) |
| 4×4 eigenvalue gap = 16 within 4-mode space | **Yes** (Part B) — g-corrections ~10⁻⁸ |
| 4-mode space is the complete K=1 Hilbert space | **NO** (Part C) — continuum modes interleaved (lowest ≈6.36 < E_B=8) |

**The disposition's qualification is sharpened, not removed.** Phase
2's `S_v = 16`:

1. Used the *non-interacting* `E_D = 16`; the interacting value is
   `E_D ≈ 13` (kink-pair attraction at `L_x = ℓ_kink`). The
   vortex-pair gap is therefore closer to `≈ 13`, not 16, *even
   within the kink sector*.
2. Neglected interleaved continuum modes (lowest ≈ 6.36 < 8). The
   true substrate spectrum at K=1 includes meson continuum modes
   the 4-mode picture omits.

**Revised honest claim:** `S_v` at K=1 is **not 16 exactly**. Within
the 4-mode kink sector, the kink-pair gap with the `E_int`
correction is `≈ 2M_k − E_int ≈ 13`. The full substrate spectrum
additionally has interleaved continuum modes. The "S_v = 16 exact"
result is retracted; the honest value is **`S_v ≈ 13` at K=1
within the kink sector, with continuum corrections of undetermined
sign and magnitude.**

## Consequences

This propagates to the cosmology layer:

- `f_exit ≈ exp(−S_v)`: with `S_v ≈ 13` (not 16), `f_exit ≈
  exp(−13) ≈ 2 × 10⁻⁶` (was `≈ 10⁻⁷`). Order of magnitude shift.
- Inflation duration `≈ exp(S_v)/H_inflation`: with `S_v ≈ 13`,
  shorter by `exp(16−13) = exp(3) ≈ 20×`. Inflation duration `≈
  5 × 10⁻³⁴ s` (was `≈ 10⁻³² s`). Still within ~2 orders of
  standard cosmology but no longer the clean `10⁻³²` match.
- `κ_pair = 1` and `|∇K|_seam`: the audit-inversion used `S_v =
  16`; with `S_v ≈ 13` the inferred `|∇K|_seam` shifts. The audit's
  numerical pinnings need recomputation with the corrected `S_v`.

**This is a real downgrade.** Phase 2's exact-precision result and
the inflation-duration's clean `10⁻³²` match both rested on the
non-interacting `E_D = 16`. The kink-fills-loop regime — which the
framework itself committed to via `L_x = ℓ_kink` — produces a
kink-pair *attraction* (`E_int ≈ 0.37 M_k`) that the Phase 2 calc
neglected. The honest `S_v ≈ 13` shifts every downstream
cosmological number.

## What survives

- The *structural* picture: substrate at K=1 is finite-mode-dominated
  (kink sector + interleaved continuum), with a kink-pair gap of
  order `2M_k`.
- The *mechanism*: action-weighted sampling, `f_exit ≈ exp(−S_v)`,
  inflation duration `≈ exp(S_v)/H_inflation` — these forms hold;
  only the numerical `S_v` value is corrected.
- The order-of-magnitude cosmology: inflation duration still lands
  within ~2 orders of `10⁻³²` s. The framework's *qualitative*
  cosmology survives; its *precision* claims do not.

## What is retracted

- `S_v(K=1) = 16` **exact** → `S_v(K=1) ≈ 13` (kink sector, with
  `E_int` correction), continuum corrections undetermined.
- "First Category-A item closed at exact precision" → **not closed
  at exact precision; closed at order-of-magnitude with a derived
  ≈20% interaction correction and undetermined continuum
  corrections.**
- Inflation duration clean `10⁻³²` match → `≈ 5 × 10⁻³⁴` s with the
  corrected `S_v`; order-of-magnitude consistent, not a precision
  match.

## Next-step work

1. **The combined (kink ⊕ continuum) diagonalization at K=1.** Is
   the continuum absorbed (Phase 1's claim) or independent (Finding
   3)? This doc shows the question is real (energies interleaved);
   resolving it needs the explicit mixing calc.
2. **The `E_int` kink-pair correction precisely.** This doc used
   the leading `E_int ≈ M_k e⁻¹`; the exact sine-Gordon
   two-kink-on-a-circle energy at `L = ℓ_kink` is computable
   (Mussardo finite-volume TBA) and would pin `S_v(K=1)` precisely.
3. **Recompute the audit's numerical pinnings** (`κ_pair`,
   `|∇K|_seam`, inflation duration) with the corrected `S_v ≈ 13`.

## Status

Class 3 (honest derivation attempt). The derivation **partially
vindicates Finding 3**: the kink-mode energies are derivable (Part
A) and the 4×4 gap is clean (Part B), but Phase 2 neglected the
kink-fills-loop interaction (`E_D ≈ 13` not 16) and the interleaved
continuum (Part C). The "exact precision" claim is **retracted**;
honest value `S_v(K=1) ≈ 13` with continuum corrections open.

The framework's qualitative cosmology survives; its precision claims
are downgraded. **This is the audit working: a real overstatement,
honestly corrected by attempting the derivation it was deferring.**

## Cross-links

- `nonperturbative_phase1.md` — queued this as the real Phase 2.
- `nonperturbative_phase2.md` — the assumed (not derived) 4-mode
  reduction; "exact" claim now retracted by this derivation.
- `audit_findings_3_4_disposition.md` — qualified Phase 2; this
  doc sharpens the qualification into a retraction.
- `sine_gordon_substrate.md` — the kink-mass formula `M_k = 8σ√(Kr)`
  used in Part A; the `E_int` finite-size form.
- `f_exit_natural.md` — the `exp(−S_v)` form survives; the `S_v`
  value inside it is corrected here.
- `inflation_duration.md` — the `10⁻³²` match is downgraded to
  `≈ 5×10⁻³⁴` with the corrected `S_v ≈ 13`.
- `unitless_audit.md` — numerical pinnings need recomputation with
  `S_v ≈ 13`.
- `audit_report.md` (branch `worktree-agent-aafbee5af7f80796d`) —
  Finding 3, now substantially vindicated by explicit calc.
