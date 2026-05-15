# Orthogonal-kink interaction: decomposition into AB-phase + jog energy

The genuinely-open piece left by `dark_twin_correction.md`: the
interaction between mode D's two orthogonal Klein-bottle kinks
(q₁ antiperiodic/dark-coupled + q₂ periodic/matter). This doc
**narrows** that open item by decomposing it, connecting one part
to the framework's already-existing AB-phase prediction and
isolating the remaining open part as a standard crossed-sine-Gordon
calculation.

No new primitive. The contribution is the decomposition and the
analogy mapping; the residual calc (`E_cross`) is flagged as the
narrowed open item.

## The system

Mode D (`figure_eight.md` D19): `(q₁ = 3 unlocked, q₂ = 2
unlocked)`. Two sine-Gordon kinks in orthogonal Klein-bottle
directions:

- **q₁ kink**: along the antiperiodic-x direction. Carries the
  half-twist (Z₂). Couples to the dark sector (`cone_twist_substrate.md`
  bicone seam; `wave_particle_substrate.md` matter/dark twinning).
- **q₂ kink**: along the periodic-y direction. Matter-sector. No
  half-twist.

They cross at one localized region (where both fields are kinked).
At K=1, `L_x = ℓ_kink` (kink-fills-loop regime). The question:
what is the interaction correction to `E_D = 2 M_k`?

`dark_twin_correction.md` established this is **not** the collinear
kink-antikink attraction `M_k exp(−L/ℓ)` (that formula is for
same-direction opposite-charge solitons; mode D is orthogonal). It
is a different, open quantity. This doc decomposes it.

## Analogous dynamical systems (brainstorm)

| System | Aspect illuminated |
|---|---|
| **Coupled sine-Gordon chains** (Josephson junction ladders, DNA-unzip models) | Dynamical core: two sine-Gordon directions, inter-direction coupling localized at soliton overlap. q₂ matter chain + q₁ dark-coupled chain. |
| **Dislocation forests** (crystal plasticity) | Energy part: a dislocation cutting a forest dislocation forms a **jog** — localized step, jog-formation energy `~μb³`, *not* long-range. q₂ kink cutting q₁ kink = analogous jog. `E_cross` ↔ jog energy. |
| **Aharonov–Bohm flux crossing** | Phase part: q₁ kink = half-twist = π "flux" (Z₂); q₂ kink crossing picks up phase **π**. This *is* `cone_twist_substrate.md` §5.2's AB-phase prediction. |
| **Cosmic-string X-junctions** (Kibble–Vilenkin) | Cosmological-scale picture: two string types at an X-junction. `cone_twist_substrate.md` §5.3's vortex-network cosmology is this at scale. |

The dislocation-forest analogy is the most precise for the energy:
the crossing energy is a **jog energy** — localized at the
intersection, of order the soliton tension times a geometric
factor, *not* the long-range collinear attraction. This is the
correct mental model for `E_cross` and rules out the
`explicit_4x4_reduction.md` collinear `≈ 3`.

## Conservation laws and their mechanisms

| Conserved | Mechanism |
|---|---|
| Z₂ topological charge (mod 2) | Klein-bottle topological rigidity (half-twist is a discrete invariant) |
| Total energy | Noether — substrate Lagrangian time-translation symmetry |
| **AB-phase = π per crossing** | Half-twist discreteness — π is the Z₂ generator's phase, **crossing-detail-independent** |
| Winding number per direction (q₁, q₂ counts) | Integer-valued kink number; no continuous change |
| Information / unitarity | Bicone Z₂ rigidity (`wave_particle_substrate.md`) — no topology change permitted |

The load-bearing point: **the AB-phase π is a topological
invariant independent of crossing geometry.** Whatever the detailed
field configuration at the crossing, the phase the q₂ kink picks
up traversing the q₁ kink's half-twist is exactly π. This is why
the framework's AB-phase prediction is robust — and why the phase
part of the orthogonal-kink interaction is *already in the
framework*, not an open question.

## The decomposition

The orthogonal-kink crossing contributes two structurally distinct
things to mode D:

    E_D  =  2 M_k  +  E_cross         (energy)
    phase  =  π                       (topological)

### Part 1: the phase π — NOT open (already predicted)

The π phase the q₂ kink acquires crossing the q₁ kink's half-twist
**is** `cone_twist_substrate.md` §5.2's Aharonov–Bohm-like
seam-crossing phase. It is topologically protected (Z₂ generator),
crossing-detail-independent, and was a framework prediction long
before this audit thread. **The phase part of the orthogonal-kink
interaction is not an open item — it is the AB-phase prediction,
now seen to also be the phase content of mode D's kink crossing.**

This is a structural unification: the AB-phase prediction and the
mode-D orthogonal-kink phase are the same π, from the same
half-twist. Two framework results that were stated separately are
one.

### Part 2: `E_cross` — the narrowed open item

`E_cross` is the localized **jog-like crossing-overlap energy**:
the field-overlap interaction in the region where both kinks are
simultaneously transitioning. By the sine-Gordon potential's
cross-term:

    V(φ_q1 + φ_q2) − V(φ_q1) − V(φ_q2)
      = −cos(φ_q1+φ_q2) + cos φ_q1 + cos φ_q2 − 1

This vanishes wherever either kink is at vacuum (`φ = 0` or `2π`)
and is nonzero only in the crossing region (~`ℓ_kink × ℓ_kink`).
Integrated, it is of order `M_k × c_geom` where `c_geom` is a
geometric coefficient of the crossed-soliton overlap — a **standard
crossed-sine-Gordon / 2D "egg-carton" lattice quantity**, not the
collinear `exp(−L/ℓ)`.

Structural bounds on `E_cross`:

- **Parametrically distinct from the collinear `≈ 3`.** The
  collinear attraction is `M_k e⁻¹ ≈ 3`; `E_cross` is a localized
  overlap, generically smaller and of possibly opposite sign
  (crossed sine-Gordon kinks can repel or attract depending on
  relative phase).
- **Bounded by the single-kink mass.** `|E_cross| ≲ M_k = 8` (the
  crossing can't cost more than creating a kink).
- **Vanishes if the kinks are infinitely separated** (only nonzero
  at the crossing; for `L_x = ℓ_kink` the kinks necessarily cross
  once on the Klein bottle).

So the honest open statement narrows from "the whole orthogonal-
kink interaction is undetermined" to:

    E_D = 2 M_k + E_cross,  with E_cross a localized crossed-
    sine-Gordon jog energy, |E_cross| ≲ M_k, parametrically
    distinct from the spurious collinear ≈3, sign undetermined.
    The phase content (π) is the already-predicted AB-phase.

## Consequence for S_v(K=1)

    S_v(K=1) ≈ 2 M_k + E_cross = 16 + E_cross

with `|E_cross| ≲ 8` and most plausibly `|E_cross| ≪ M_k` (the
crossed-overlap is a sub-region effect). So:

- `S_v(K=1) ≈ 16` remains the **leading value** (Phase 2's number,
  restored by `dark_twin_correction.md`).
- The correction is `E_cross`, a *bounded localized* quantity, NOT
  the spurious collinear `≈ 3` and NOT exact-zero.
- "Exact" is still not claimable until `E_cross` is computed; but
  the open item is now a specific, bounded, standard calc, not a
  vague "needs more work."

## What computing E_cross requires

The 2D crossed-sine-Gordon overlap energy at a right-angle kink
intersection. Standard approaches:

1. **Direct integration** of the cross-term potential over the
   crossing region with the product ansatz `φ = φ_q1(x) + φ_q2(y)`
   (leading order; corrections from the field not being exactly
   separable at the crossing).
2. **The 2D sine-Gordon lattice ("egg-carton") literature**: the
   crossing energy is a known quantity in that context; mapping
   the framework's K=1 crossing onto it gives `E_cross` with a
   specific coefficient.
3. **Lattice numerics**: a small Klein-bottle lattice with crossed
   kink boundary conditions, measuring the energy excess at the
   crossing. (Tractable; the K=1 substrate is finite-mode-
   dominated per `nonperturbative_phase1.md`.)

Each is a contained substrate-Lagrangian-level calc. None requires
new framework primitives.

## Status

Class 3 (decomposition + narrowing). The orthogonal-kink
interaction is decomposed into:

- **Phase π**: the framework's already-existing AB-phase prediction
  (`cone_twist_substrate.md` §5.2). Not open; structurally unified
  with mode D's crossing.
- **`E_cross`**: a localized jog-like crossed-sine-Gordon overlap
  energy. Open, but **narrowed** to a specific bounded standard
  calc (`|E_cross| ≲ M_k`, parametrically ≠ collinear `≈3`).

`S_v(K=1) ≈ 16 + E_cross`, leading value 16, correction bounded and
specific. The framework's `S_v ≈ 16` survives as leading-order;
"exact" awaits the `E_cross` calc, which is now a contained
crossed-sine-Gordon problem rather than an open-ended question.

This continues the audit's productive pattern: each step narrows
what is actually open. The orthogonal-kink interaction went from
"undetermined" (`dark_twin_correction.md`) to "phase = already-
predicted AB-phase + a bounded localized jog energy" (this doc).

## Cross-links

- `dark_twin_correction.md` — established the orthogonal (not
  collinear) configuration; left `E_cross` open. This doc narrows
  it.
- `explicit_4x4_reduction.md` — the over-corrected doc; its
  collinear `≈3` is parametrically distinct from `E_cross`.
- `cone_twist_substrate.md` §5.2 — the AB-phase prediction, now
  unified with mode D's crossing phase (Part 1).
- `cone_twist_substrate.md` §5.3 — vortex-network X-junction
  cosmology (the cosmological-scale analog).
- `nonperturbative_phase2.md` — `S_v ≈ 16` leading; `E_cross` is
  the bounded correction.
- `figure_eight.md` D19 — mode D = orthogonal q₁/q₂ kinks.
- `wave_particle_substrate.md` — matter/dark twinning; q₁
  dark-coupled, q₂ matter.
- `sine_gordon_substrate.md` — the sine-Gordon potential whose
  cross-term gives `E_cross`.

## The genuinely-open item, fully stated

> Compute `E_cross`: the localized crossed-sine-Gordon overlap
> energy at a right-angle kink intersection on the Klein bottle at
> `L_x = ℓ_kink`. Bounded `|E_cross| ≲ M_k = 8`, parametrically
> distinct from the collinear `M_k e⁻¹ ≈ 3`, sign undetermined.
> This is a standard 2D-sine-Gordon-lattice / dislocation-jog
> calculation; the phase content (π) is already the framework's
> AB-phase prediction and is not part of this open item.

That is the bottom reached for this thread: a specific, bounded,
standard calc, with the topological content already accounted for
by an existing framework prediction.
