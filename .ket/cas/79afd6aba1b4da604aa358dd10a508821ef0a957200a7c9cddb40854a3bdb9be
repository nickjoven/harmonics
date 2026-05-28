# Free-parameter scorecard — the forcing partition applied to physics' inputs

## What this is

The free parameters of physics — the dimensionless inputs the Standard
Model and ΛCDM **measure rather than derive** — listed as the rows, with
the framework's verdict on each. It is the empirical roster of
`algebraic_forcing_partition.md`: *forced ⟹ discrete/combinatorial; the
continuous couplings stay open.*

**This is a pointer-index, not a re-derivation.** Every verdict lives in
the cited canonical doc; this file only collects them against the
external parameter list and must not be read as a source of truth on its
own — *truth is the cited diff*. It is **honesty-forward**: failures
(Class 1) and unforced items (Class 2/3) sit in the same tables as the
forced ones, and there is no "reduced N parameters" accounting (the
"zero free parameters" phrasing is retired repo-wide; this file does not
revive it).

The denominator is the **external** count (SM ~19 + cosmological), not a
framework claim. Dimensionful scales (H₀, v_EW, M_Planck) are a separate
block — they are *out of class* by the Basepoint Principle, not open
forcing targets.

## I. Forced — the discrete / combinatorial layer (Class 5 / Survives)

These are the inputs the framework removes from "free" — and every one
is discrete, group-theoretic, topological, or combinatorial.

| Input (SM/ΛCDM treats as) | Framework verdict | Canonical doc |
|---|---|---|
| Gauge group SU(3)×SU(2)×U(1) | **Survives** — from Z₃ (color) + Z₂ (Klein) + U(1); not assumed | `phenomenology_cross_reference.md` §6 (D41/D42) |
| 6 anomaly-cancellation conditions | **Survives** — each = a substrate mode-count identity | `phenomenology_cross_reference.md` §6 (D41) |
| Strong-CP angle θ_QCD (free; tuned <10⁻¹⁰) | **Survives** — θ=0 forced by substrate symmetry; resolves strong-CP, no axion | `phenomenology_cross_reference.md` §6 (D45) |
| Spatial dimension = 3 | **Survives** | `three_dimensions.md`, §5 |
| Lorentz symmetry | **Survives** | `phenomenology_cross_reference.md` §5 |
| Born-rule exponent = 2 | **Survives** — saddle-node universality (Thom) | `born_rule.md`, `lesson_forced_basin_selection.md` |
| **Ω_Λ = 13/19** | **Survives** — Farey F₆ partition; zero free parameters at closure | `omega_partition_combinatorial.md`, `farey_partition.md` |
| Ω_DM : Ω_b (the 13:5:1 partition) | **Survives** — same combinatorial source | `farey_partition.md` |
| R = 6·13⁵⁴, Λ·ℓ_P² | **Survives** | `numerology_inventory.md` §Class 5 |
| a₀ (MOND scale) = cH₀/(2π) | **Survives** *as a ratio* — absolute value rides H₀ (anchor) | `numerology_inventory.md` §Class 5 |

## II. Open — the continuous couplings / masses

Same open class the SM and the string landscape leave them in. None is
forced; the sub-verdicts grade *how* unforced.

### Class 1 — attempted and failed (value imported)

| Input | Framework attempt | Verdict | Canonical doc |
|---|---|---|---|
| **1/α_em** | tree = q₂³+q₃³ = 35 | **Class 1** — running 35→128 fails ~3.7×; value imported (1/137.036) | `numerology_inventory.md` §Class 1; `negative_results_ledger.md` |
| sin²θ_W | 8/35 = 0.2286 | **Class 1** — SM running rules out Planck-scale origin | `framework_status.md` "Fails"; `sinW_running_check.py` |

> **Reconciled (this PR — the conflict this scorecard surfaced is now
> closed, not left open).** The charged-fermion `26:7:1` hierarchy was
> classified two ways: `numerology_inventory.md` (audit 2026-04-24)
> **Class 1** (bare-tree μ/e `7^(5/2)=129.6` misses 206.8 by **37%**;
> the "K→μ running correction" is an undefined patch) vs
> `fermion_mass_running.md` D50 (2026-04-22) **"closed, 9→1"** via a
> Koide constraint. Attempting the reconciliation rather than recording
> "open": the two judged *different* closures. The bare tree + running-
> correction **is** Class 1 (that null stands). But a *separate* closure
> the audit never evaluated — the **Koide constraint `Q=2/3`** (a
> framework-derived Klein-bottle population ratio, `klein_bottle.md`)
> with the tree τ/e — gives `μ/e ≈ 204.8` (**0.96%**, verified). So the
> honest verdict is **Floor** (row below): a structural mechanism
> reaching the ~1% particle-sector coincidence floor — *but* the Koide
> *form* is imported and the `26:7:1` base / `5/2` exponent are
> un-forced, so not a forced closure and not "9→1" (retired phrasing).
> `numerology_inventory.md` undercredited (→ Class 1), `fermion_mass_running.md`
> overclaimed (→ "closed"); both updated to Floor.

### Class 2 / 3 — consistent or suspect, never forced

| Input | Verdict | Canonical doc |
|---|---|---|
| Charged-fermion μ/e (26:7:1 + Koide Q=2/3) | **Floor** — bare tree Class 1 (μ/e 37%); Koide Q=2/3 closes μ/e to ~1% (coincidence floor; Koide form imported, base/exponent un-forced) | `fermion_mass_running.md`, `numerology_inventory.md` §C1, `generation_mechanism.md` |
| CKM matrix (3 angles + phase) | Class 2 — pigeonhole over expression set (Region C) | `phenomenology_cross_reference.md` §7 |
| PMNS / neutrino mixing | Class 2 | `phenomenology_cross_reference.md`; Region C |
| Quark / lepton mass ratios (most) | Class 2 — 0.1–3% fits, pigeonhole | `phenomenology_cross_reference.md` §7–8 |
| m_H/v = 1/2, λ_H = 1/8, α_s/α_2 = 27/8 | Class 3 — duty-cycle dictionary, suspect by association | `numerology_inventory.md` §Class 3 |
| n_s ≈ 0.965 | Class 2 — φ²-self-similarity carries a free pivot x_* | `spectral_tilt_reframed.md` |
| A_s | Floor — Instance-7 acceptance (f_amp anchor-side) | `numerology_inventory.md` §Class 2 |
| N_efolds, tensor-to-scalar r | Class 2 / TBD — awaiting CMB-S4 | `phenomenology_cross_reference.md` §3 |
| v/M_P ≈ 13⁻¹⁵ | Class 2 — 3.1% near-match, `yukawa_mediant_cascade.py` null | `numerology_inventory.md` §Class 2 |
| baryon asymmetry η_B | not addressed (open) | — |

## III. Out of class — dimensionful anchors (separate spot)

Not open forcing targets: declined by the **Basepoint Principle** (the
framework supplies torsorial structure, never the dimensionful
basepoint). Listed for completeness so the denominator is honest.

| Input | Status | Canonical doc |
|---|---|---|
| H₀ (cosmological anchor) | Out of class — feature, obstruction exhibited | `framework_status.md` "Out of class"; `anchor_count_reaudit.md` |
| v_EW (particle anchor) | Out of class | `framework_status.md` |
| M_Planck, absolute masses, ℏ/c/G in units | Out of class (ride the two anchors) | `framework_status.md` |

## The honest reach line

The framework **forces the discrete sector** — gauge group, anomaly
cancellation, θ_QCD=0, spatial dimension, the Born exponent, and the
cosmological *combinatorial* partition (Ω_Λ=13/19, 13:5:1). It **leaves
the continuous sector open** — the gauge couplings and the Yukawa/mixing
parameters sit in Class 1/2, the same open class the SM measures and the
landscape hands to selection. It **failed** outright on α_em and
sin²θ_W (numerology killed by running), **declines** the dimensionful
anchors by principle, and **reconciled the one internal conflict this
index surfaced** (the 26:7:1 Yukawa hierarchy → Floor via Koide Q=2/3,
not the open flag it was first recorded as). No reduction is tallied;
the value is the map, not a score.

## What this confirms

The split is exactly `algebraic_forcing_partition.md`, now read off the
real parameter list: **discrete/combinatorial inputs → forced (§I);
continuous couplings/masses → open (§II)**. This is also the Standard
Model's own forced/free seam — necessity in the group theory and anomaly
structure, contingency in the couplings — so the partition is not a
framework idiosyncrasy but the SM's input structure named as a principle.

## Cross-links

- `algebraic_forcing_partition.md` — the organizing principle (this is its roster).
- `phenomenology_cross_reference.md` — the observable-indexed companion (verdict sources).
- `numerology_inventory.md` — the Class 1–5 definitions and per-item audits.
- `framework_status.md` — Survives / Floor / Fails / Out-of-class.
- `negative_results_ledger.md` — the null record (α_em, sin²θ_W).

## One-line summary

Physics' dimensionless free parameters, indexed and graded: the framework
**forces the discrete/combinatorial ones** (gauge structure, anomalies,
θ=0, Ω_Λ=13/19) and **leaves the continuous couplings open** (α_em and
sin²θ_W failed, Yukawa/mixing Class 1–2) — the same forced/free seam the
Standard Model already has, with one internal conflict (26:7:1) surfaced
by the index and reconciled to **Floor** (Koide Q=2/3 closes μ/e to ~1%;
bare-tree Class-1 null retained).
