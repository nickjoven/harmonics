# The graviton's properties in framework terms: a reframing

> Strip away "the spin-2 particle." What remains is the
> tensor-mode fluctuation of the coherence metric at K=1 — and the
> graviton is its quantum, with the same standing the photon has
> for `c`.

## The problem with "a spin-2 massless particle that mediates gravity"

The textbook narrative gives the graviton a stack of primitive
properties: it is a particle (a quantum of a field), it has spin 2,
it is massless, it travels at `c`, and it couples universally to
the stress-energy tensor `T_μν`. Read literally, this is a special
object posited to carry a force, with each property an input.

The framework does not posit a graviton. Derivation 13
(`einstein_from_kuramoto.md`) already produces the Einstein field
equations `G_μν + Λg_μν = 8πG T_μν` as the *unique* K = 1 continuum
output (Lovelock 1971), with the spacetime metric

    ds² = −N² dt² + γ_ij (dx^i + β^i dt)(dx^j + β^j dt)

built from the coherence tensor `γ_ij = C_ij/C_0 = δ_ij −
⟨∂_i θ ∂_j θ⟩` (`adm_dictionary.md` Part I). Gravity is the
**locked-state geometry of the coherence metric**, not a force
carried by a particle.

This document promotes that result to a standing graviton ontology,
the same move as `photon_reframing.md` (the photon is the Ø-mode,
not a carrier) and `higgs_reframing.md` (the Higgs is one locked
mode, not the mass-giver). **The graviton is not a fundamental
object. The tensor mode of `γ_ij` is.**

## What the graviton is

**The graviton is the spin-2 tensor-mode fluctuation of the
coherence metric `γ_ij` about the locked K=1 background.** Write the
metric as background plus fluctuation,

    γ_ij = γ_ij^(0) + h_ij,        h_ij = δ(C_ij/C_0),

where `h_ij` is the transverse-traceless part of the perturbation
of the coherence tensor `C_ij = δ_ij − ⟨∂_i θ ∂_j θ⟩`. The graviton
is the quantum of `h_ij`. There is no separate object to identify:
`γ_ij` is the unique symmetric rank-2 tensor constructible from the
phase field and its first derivatives (`adm_dictionary.md` Part I
uniqueness argument), so its propagating fluctuation is the unique
spin-2 mode of the substrate. Spectral tilt already reads
gravitational waves as "synchronization-cost fluctuations of"
the locked state (`spectral_tilt.md`); the graviton is the quantum
of exactly those fluctuations.

## The precise statement

**The graviton is the tensor mode `h_ij` of the coherence metric
`γ_ij = C_ij/C_0` at K=1; its quantum is the discrete excitation of
that mode. "Spin-2 massless particle mediating gravity at `c`" is
the coarse-grained shadow, with each clause a property of `h_ij`:**

| Stated property | Framework term | Forced by |
|---|---|---|
| **Spin-2** | the symmetric rank-2 tensor character of `h_ij` | `γ_ij` is the unique symmetric rank-2 tensor from the phase field (`adm_dictionary.md` Part I) |
| **Two polarizations (TT)** | the transverse-traceless part of `δC_ij` | linearized-Einstein gauge structure, inherited from D13 general covariance (premise d) |
| **Masslessness** | no compact-`K` (`SO(2)`) eigenfrequency — `h_ij` is a coherence-correlation fluctuation, not an oscillator | absence of a compact-part eigenvalue, identical to the photon's masslessness (`speed_of_light.md`, `photon_reframing.md`) |
| **Propagation at `c`** | the locked-state wave operator on `γ_ij` is the K=1 continuum d'Alembertian | the K=1 continuum limit *is* the Einstein equations (`einstein_from_kuramoto.md`, Lovelock 1971); waves propagate at the gate speed `c = N₊` scale |
| **Universal coupling to `T_μν`** | the source term `8πG T_μν` of the unique D13 field equation | Lovelock 1971 uniqueness on the locked sector (`einstein_from_kuramoto.md` Part II) |
| **Self-interaction (nonlinearity)** | `γ_ij` quadratic in `∂θ` ⟹ `h_ij` self-couples through `C_ij` | the coherence tensor is bilinear in phase gradients (`adm_dictionary.md`) |
| **"Force carrier"** | not a carrier — gravity is the locked-state geometry; `h_ij` is the propagating ripple of that geometry | the metric is the coherence correlation, not a field on a background (D13) |

The "force carrier" clause is the one most sharpened here. The
framework has no force mediated by an exchanged particle; it has a
coherence geometry whose fluctuations propagate. The graviton is
the name for a quantum of that fluctuation, exactly as the photon
is the name for a transit of the gate front — in both cases the
"carrier" picture is the shadow of a substrate mode, not a
fundamental exchange.

## What this does not derive

This is a reframing, not a new prediction. Specifically:

- It does **not** quantize gravity. D13 gives the *classical*
  Einstein equations as the K=1 continuum limit; this reframing
  identifies the graviton as the quantum of `h_ij` but does **not**
  compute graviton scattering amplitudes, loop corrections, or a
  UV completion. **This is the honest residual** — the graviton's
  *quantization* is the open item, exactly parallel to the photon
  reframing leaving the numerical value of `c` open
  (`photon_reframing.md` "What this does not derive"). The framework
  supplies the field (`γ_ij`) and the unique classical dynamics
  (Einstein); it does not yet supply the quantum theory.
- It introduces **no new framework integer and no new O(1) factor**
  (Z2 vacuously satisfied — no numerical claim; C-structural, not
  C-numerical per `statistical_conventions.md`).
- It changes **no entry in MANIFEST.yml**. No scorecard row added or
  modified. `Λ` and `G` remain anchor-side per the two-anchor
  minimality (`anchor_count_reaudit.md`); the absolute graviton
  scale (Planck mass in kg) stays out of class.

## What this changes in the framework's writeups

After this document, avoid in the framework's own voice:

- "The graviton is a spin-2 force carrier" (as the primary object).
- "Gravity is mediated by graviton exchange."

Preferred alternatives:

- "The graviton is the tensor mode `h_ij` of the coherence metric
  `γ_ij` at K=1."
- "Gravity is the locked-state geometry of the coherence metric;
  the graviton is the quantum of its propagating ripple, not a
  carrier exchanged on a background."
- "The graviton is massless for the same reason the photon is —
  no compact-`K` eigenfrequency; it is a correlation fluctuation,
  not an oscillator."

The numerical predictions are unchanged. What changes is the
ontology: the graviton is the framework's name for the spin-2 mode
of the coherence metric, and "spin-2 massless force carrier" is the
shadow that mode casts. The honest residual — *quantizing* that
mode — is named, not hidden.

## Distinct from the photon (sibling Ø vs tensor mode)

The photon (`photon_reframing.md`) is the **Ø-mode**: the nilpotent
radical `ℝ·N₊ ⊂ sl(2,R)`, a *null direction* (rank-1, the gate
front). The graviton is the **tensor mode** of `γ_ij`: a symmetric
rank-2 fluctuation of the locked geometry. Both are massless for the
same structural reason (no compact-`K` eigenfrequency), both
propagate at `c`, but they are different objects — Ø is the
propagation direction itself; the graviton is a fluctuation of the
metric *through which* propagation happens. The shared masslessness
is not a coincidence: it is the common absence of an oscillator
eigenfrequency.

## Status

**Reframing.** Sibling of `photon_reframing.md`, `higgs_reframing.md`,
and `spectral_tilt_reframed.md`: a structural/ontological sharpening
that retains all numerical content of its parent derivation
(`einstein_from_kuramoto.md`, D13) and changes only the language and
the primary object. C-structural per `statistical_conventions.md`;
not C-numerical; not registered in the MANIFEST scorecard.

The graviton's **identification** is closed at the ontological level
by this reframing (it is uniquely the spin-2 mode of `γ_ij` — there
was never a "which graviton" question). The graviton's **full
quantization** (scattering amplitudes, UV completion) is **not**
resolved and remains the honest open residual, parallel to the
numerical value of `c` for the photon. Absolute `G`/Planck-mass
scale stays anchor-side / out of class.

## Cross-references

- `einstein_from_kuramoto.md` — D13, parent: Einstein equations as
  the unique K=1 continuum output; the metric `γ_ij`, the ADM
  decomposition, Lovelock uniqueness. This doc names the graviton as
  the quantum of its tensor mode.
- `adm_dictionary.md` — `C_ij = γ_ij` uniqueness (the spin-2
  character is forced by `γ_ij` being the unique symmetric rank-2
  tensor from the phase field).
- `photon_reframing.md` — sibling reframing; the massless photon as
  the Ø-mode; the shared "no compact-`K` eigenfrequency"
  masslessness mechanism.
- `speed_of_light.md` — D31, `c` as the gate-propagation scale;
  the masslessness-from-no-oscillator argument.
- `spectral_tilt.md` — gravitational waves as synchronization-cost
  fluctuations of the locked state (the classical limit of the
  graviton mode).
- `anchor_count_reaudit.md` — why absolute `G`/Planck-mass stays
  anchor-side (two-anchor minimality).
- `articulation_audit_2026-05.md` — the audit (and post-audit
  revision) that promoted this from a mis-classified "decline" to a
  P1 articulation.

## One-line summary

The graviton is the spin-2 tensor mode `h_ij` of the coherence
metric `γ_ij = C_ij/C_0` at K=1 — uniquely identified (no "which
graviton" question ever existed), massless for the photon's reason
(no compact-`K` eigenfrequency), propagating at `c` because K=1
*is* Einstein. The honest residual is *quantizing* the mode, not
identifying it — exactly parallel to the photon reframing leaving
the numerical value of `c` open.
