# √r_n correction: making the K-zoo kink-mass residual concrete

## Status

**Articulation of an existing flagged correction** —
`proposed_residual_closure.md` §C established that the K<1
sine-Gordon reduction is structurally forced (K-parameterized
Goldstein–Kac) and that the kink-mass ratio carries an honest
`√r_n` correction the bare conjecture omitted. The status entry
read "what is left is a *quantitative correction* (`√r_n`) and
a *declined disposition* (the observable-mapping) — neither is
an open problem to chase." `framework_status.md` Survives row
echoes this as "an honest flagged correction."

This doc makes the flag concrete: the correction's **form** is
exact, the **K-scaling part is structurally forced (Class-3)**,
the **r_n factor is bounded (0, 1]** with `r_1 = 1` set by the
K = 1 full-lock condition, and the **value of r_n at K_n < 1 is
Class-2** absent a structural mode-counting / tongue-width
closure (three candidate routes catalogued below). The K-zoo
mass-ratio table in `master_cascade_identity.md` L40-43 and
`sine_gordon_substrate.md` L142-146 is correctly read as the
**upper bound** of the corrected ratio (saturated only at the
bare-conjecture limit `r_n = 1`).

No new primitive. The contribution is precision: a sharp
statement of what is structurally forced, what is bounded, and
what remains Class-2 by construction. The corpus's honest-
landing discipline (`ansatz_audit_policy.md`,
`numerology_count_phase_b.md` Region C pigeonhole verdict)
forbids upgrading r_n to a prediction without structural forcing
— this doc does not propose to do so.

---

## The corrected K-zoo kink-mass ratio (exact form)

**Statement.** For the cascade master-identity instance
`K_n^d = b^(−n)` (`master_cascade_identity.md`), the kink-mass
ratio between the n-th cascade-locked sector and the K = 1
gravity boundary is

    M_k(d, n, b) / M_k(K = 1)  =  √(K_n r_n / (K_1 r_1))
                               =  b^(−n/(2d)) · √(r_n)        (∗)

where `r_n ∈ (0, 1]` is the Kuramoto order parameter
`|⟨e^{iθ}⟩|` evaluated in the n-th cascade-locked sub-state,
with `r_1 = 1` set by the K = 1 full-lock condition
(`einstein_from_kuramoto.md`'s "locked state K ≈ 1"; see
`sine_gordon_substrate.md` Setup).

### What is structurally forced (Class-3)

The K-scaling factor `√K_n = b^(−n/(2d))` is forced by
two structural inputs jointly:

1. **The kink-mass formula** `M_k = 8σ√(K r)`
   (`sine_gordon_substrate.md` §"Kink mass in framework
   primitives"), itself the standard sine-Gordon result with the
   framework's locked-state expansion (rigorous at K ≈ 1; *now
   forced K-parameterized at every cascade K_n* via the
   K-parameterized Goldstein–Kac construction of
   `tick_continuum_construction.md`, per
   `proposed_residual_closure.md` §C).
2. **The master cascade identity** `K_n^d = b^(−n)`
   (`master_cascade_identity.md`), whose `(d, n, b)` triples are
   framework primitives `{q_2, q_3, |F_4|}`.

Combined: `√K_n = (b^(−n))^(1/(2d)) = b^(−n/(2d))`. This is the
Class-3 part of (∗) — preserved exactly in the corrected ratio.

### What is the honest correction (the √r_n factor)

The order-parameter ratio `√(r_n/r_1) = √r_n` (using `r_1 = 1`)
is the **honest residual correction** the bare conjecture
omitted. Its form is exact — set by Kuramoto's self-consistency
machinery (the order parameter is the standard `|⟨e^{iθ}⟩|`,
defined in `sine_gordon_substrate.md` Setup). Its *value* at
each cascade K_n is not pinned by the master cascade identity
alone, which sets `K_n` but not `r_n`. Bounds:

- `0 < r_n ≤ 1` (Kuramoto magnitude bound).
- `r_1 = 1` (K = 1 full lock — framework definition,
  `einstein_from_kuramoto.md`, `sine_gordon_substrate.md` L41
  and L122).
- Continuity at the gravity boundary: `r_n → 1` as `K_n → 1`.

This is exactly the situation `proposed_residual_closure.md` §C
described as "*State the forced part exactly; the `√r_n` is the
honest residual correction (same shape as the S_v uniform-
winding bound — flagged, not buried)*."

---

## K-zoo mass-ratio table — bare vs. corrected as upper bound

The K-zoo table from `sine_gordon_substrate.md` L142-146 and
`master_cascade_identity.md` is correctly read as the **upper
bound** of the corrected ratio (saturated only at `r_n = 1`):

| Sector            | K_n         | (d, n, b)         | Upper bound = bare ratio       | Corrected ratio          |
|---|---|---|---|---|
| String boundary K = 1 | 1.00000  | (—, 0, —)          | 1.0000                          | 1.0000 (`r_1 = 1` exact) |
| Z_6 cascade (conj.)  | 0.89090  | (6, 1, 2)?         | 2^(−1/12) ≈ 0.94387             | 2^(−1/12) · √(r_{Z6})   |
| Matter equilib. K*   | 0.86196  | (14, 3, 2)         | 2^(−3/28) ≈ 0.92842             | 2^(−3/28) · √(r_{K*})   |
| Bowed cascade (IMF)  | 0.79370  | (3, 1, 2)          | 2^(−1/6) ≈ 0.89090              | 2^(−1/6) · √(r_{bowed}) |
| Clarinet cascade     | 0.57735  | (2, 1, 3)          | 3^(−1/4) ≈ 0.75984              | 3^(−1/4) · √(r_{clar.}) |

Reading the bare table as an **upper bound** has two consequences:

- The framework's K-zoo prediction is `≤` the bare value, not
  `=` it. Observational tests should be read as falsifying the
  bare conjecture if the measured ratio exceeds the bare value
  (which would require `r_n > 1`, impossible) — and as
  consistent with the framework if the measured ratio lies in
  `(0, bare-value]`, with the residual gap absorbed into `√r_n`.
- The bowed cascade's claimed Salpeter-IMF match (0.33σ in
  `master_cascade_identity.md` L41) is read against the bare
  exponent (slope `−7/3`), not the mass ratio — so it is
  unaffected by the √r_n correction (the slope follows from
  `α = −q_2 − n/d`, independent of r_n).

---

## Three candidate closure routes (none promoted to prediction)

Each route would, if executed, promote a specific r_n value to
Class-3 (structurally forced). All three remain open candidates
under the framework's honest-landing discipline; none has been
worked through.

### Route A — Mode-counting from the 4-mode reduction

`discrete_reduction_computed.md` exhibits the K = 1 substrate as
a 4-mode system (A, B, C, D) after the XOR collapse, with
diagonal Hamiltonians `H_AA = 0`, `H_BB ≈ 9.580` (q₂ = 3
periodic kink), `H_CC ≈ 3.645` (q₁ = 3 antiperiodic half-twist),
`H_DD ≈ E_BB + E_CC − 4` (mode D with `E_cross = −4`). If a
cascade-locked sector at K_n locks `n_n` of these four modes,
then by mode-counting

    r_n^{(A)}  =  n_n / 4,    n_n ∈ {1, 2, 3, 4}

Candidate identifications (not derived):

- Matter equilibrium K* locks the q₂ (matter) modes → `{A, B}`
  or `{A, B, D}` → r ∈ {2/4, 3/4}.
- Bowed cascade locks the q₃ modes → `{A, C}` or `{A, C, D}` →
  r ∈ {2/4, 3/4}.
- Z_6 cascade locks all of `{A, B, C, D}` → r = 4/4 = 1
  (continuity with K = 1).

**Open obstacle.** No structural argument in the corpus pins
which modes lock in which sector. The cascade master identity
`K_n^d = b^(−n)` is silent on mode partition.

### Route B — Tongue-width derivation

For a cascade-locked sector around fraction `p/q` at coupling K,
the Arnold-tongue width is `w(K, q) = 2(K/2)^q`
(`mediant_vs_flow_calc.md`, `boundary_weight.md`,
`beta_from_tongues.md` L106-110). The Kuramoto order parameter
inside the locked tongue (with the framework's identical-
oscillator content) is generically `r ≈ 1` *inside* the tongue
and `r ≈ 0` *outside* — but the framework's cascade-locked state
inhabits a definite tongue, so the in/out distinction is
sector-specific.

The natural reading: `r_n` is the fraction of the unit interval
covered by the n-th cascade tongue,

    r_n^{(B)}  =  w(K_n, q_n) / 1  =  2 (K_n / 2)^{q_n}        (B)

with `q_n` the cascade-locking denominator at depth n (e.g.,
`q = 3` at the bowed cascade, `q = 2` at the clarinet). Numerical
values from (B):

- Bowed (K_n = 2^(−1/3), q = 3): `r_B = 2 · (2^(−1/3)/2)^3 = 2 ·
  2^(−1 − 3·1/3) / 2^3 = 2 / (2 · 2 · 2) · (1/2)^{-1+1} = ...`
  computed directly: `(0.79370 / 2)^3 · 2 = (0.39685)^3 · 2 =
  0.06251 · 2 = 0.12501`. So `r_B = 0.125`,
  `√r_B = 0.354`, corrected ratio = `0.891 · 0.354 = 0.315`.
- Clarinet (K_n = 3^(−1/2), q = 2): `r_C = 2 · (3^(−1/2)/2)^2 =
  2 · 3^{−1} / 4 = 1/6 ≈ 0.167`, `√r_C ≈ 0.408`, corrected
  ratio = `0.760 · 0.408 = 0.310`.

**Open obstacle.** The tongue-width reading conflates "fraction
of phase space locked" with "Kuramoto magnitude `|⟨e^{iθ}⟩|` in
the locked sub-state" — these coincide only in specific
disorder models, not generically. With identical oscillators
(`canonical_glossary.md` L78: "for identical oscillators K_c =
0; not the framework's K_STAR"), the tongue-width reading is
not strictly the Kuramoto order parameter. (B) is therefore
**a candidate, not a derivation** — the cleanest one available
in current corpus tools, with the caveat that the
identification of "locked-tongue width" with "Kuramoto r"
needs a structural argument the corpus does not yet have.

### Route C — Direct Kuramoto-on-Klein measurement (rfe-style)

The `rfe` numerical engine (federated repo per `MANIFEST.yml`
L297-302) could in principle measure `r_n = |⟨e^{iθ}⟩|` at each
cascade K_n by running the substrate Lagrangian on the Klein-
bottle lattice and reading the equilibrium order parameter
directly. This would not be a *derivation* (the result would be
Class-1 numerics, not Class-3 structurally forced), but it
would calibrate the bound — turning `r_n ∈ (0, 1]` into a
measured value with uncertainty.

**Status.** Not executed in this corpus; flagged here as the
empirical option for those who want numbers without waiting for
a structural argument.

---

## Honest classification

Under `ansatz_audit_policy.md` triage:

- The **form** of (∗) is **Class-3 (structurally forced)** —
  M_k = 8σ√(Kr) plus the master cascade identity, both
  framework-internal.
- The **upper bound** `M_k(n)/M_k(K=1) ≤ b^(−n/(2d))` is
  **Class-3** — derived from `r_n ≤ 1` and (∗).
- The **value** of `r_n` at each K_n < 1 is **Class-2** absent a
  structural argument from Route A / B / C. By the Region C
  pigeonhole verdict (`numerology_count_phase_b.md`,
  `framework_status.md` "Floor (particle numerology cloud)"), a
  Class-2 quantity at the substrate side is **correctly not
  chased** as a prediction; the K-zoo kink-mass ratios are
  reported at the structural upper bound only.

### Bright lines

- **Not a new prediction**. The framework's prediction is the
  *structural upper bound* `b^(−n/(2d))` (already in the corpus)
  plus the *bounded residual* `√r_n ∈ (0, 1]`. Specific corrected
  values are not claimed.
- **Not a Class-3 promotion of r_n**. Routes A/B/C are
  candidates, not derivations. Promotion requires executing one
  of them with a structural forcing argument — which the corpus
  currently lacks.
- **Not an upgrade of the observable-identification**. Which
  observed object is a substrate kink in each sector remains
  Class-2-declined per `proposed_residual_closure.md` §C — that
  disposition is unchanged.

---

## Effect on existing K-zoo statements

The K-zoo ratio table in `sine_gordon_substrate.md` L140-150
and the soliton implication of `master_cascade_identity.md`
L67-74 currently state `M_k(n)/M_k(K=1) = b^(−n/(2d))` *as if
exact*. They are exact *as an upper bound*, the equality holding
only at the bare-conjecture limit `r_n = 1`. The corrected
reading is:

    M_k(n) / M_k(K=1)  ≤  b^(−n/(2d))                          (†)

with the gap to equality given by `(1 − √r_n)`. No predictions
move on the cosmological closure side (`framework_status.md`
Survives entries are anchored at K = 1 and unaffected); the
adjustment is confined to the soliton-sector K-zoo ratios where
the bare formula was already flagged conjectural.

For the IMF claim (`master_cascade_identity.md` L41: "Salpeter
IMF 0.33σ"), the agreement is on the *slope* `α = −q_2 − n/d`,
which is set by the cascade-identity exponents — independent of
r_n. The IMF match is not affected by the √r_n correction.

---

## Falsifiers

- **Direct ratio falsifier**. A measured soliton-mass ratio
  exceeding the structural upper bound `b^(−n/(2d))` in any
  identified K-zoo sector would require `r_n > 1`, impossible
  by the Kuramoto bound. Such an observation would falsify
  either the master cascade identity, the sine-Gordon reduction,
  or the locked-state sub-state identification.
- **r_n = 1 dependence**. If the bare ratio is measured *equal*
  to the upper bound (within experimental error), that would
  imply `r_n = 1` at K_n < 1 — consistent with the K → 1
  continuity boundary, requiring structural explanation of why
  the cascade sector is fully locked despite K < 1.
- **Slope falsifier (unchanged)**. The IMF slope test
  (`master_cascade_identity.md` L41) is independent of r_n; an
  IMF slope disagreement would falsify the cascade identity
  itself, not the √r_n correction.

---

## Cross-links

- `proposed_residual_closure.md` §C — the parent closure that
  established the K-parameterized Goldstein–Kac forcing and
  flagged the √r_n correction; this doc is the precise
  articulation.
- `sine_gordon_substrate.md` §"Kink mass" (L115-130), §"Kink
  mass ratios across the K-zoo" (L135-155) — the corpus's
  bare-formula tables now correctly read as upper bounds.
- `master_cascade_identity.md` §"Soliton-sector implication"
  (L61-74) — the K-zoo ratio statement now reads as an upper
  bound.
- `tick_continuum_construction.md` — the K-parameterized
  Goldstein–Kac that forces the per-sector reduction (Class-3).
- `discrete_reduction_computed.md` — the 4-mode structure
  underlying Route A.
- `mediant_vs_flow_calc.md` / `boundary_weight.md` /
  `beta_from_tongues.md` — the tongue-width machinery
  underlying Route B.
- `ansatz_audit_policy.md` / `numerology_count_phase_b.md`
  Region C — the honest-landing discipline that keeps r_n
  Class-2 absent structural forcing.
- `canonical_glossary.md` L78, L173 — `K_c = 0` for identical
  oscillators (vocabulary disambiguation; why standard Kuramoto
  r-formulas don't directly apply).
- `framework_status.md` Survives row for "Per-sector
  sine-Gordon reduction" — `√r_n` correction explicitly
  articulated here.
- `thread_chronology.md` — entry for this articulation.

## One-line summary

The K-zoo kink-mass ratio is exactly `b^(−n/(2d)) · √r_n` with
`r_n ∈ (0, 1]` and `r_1 = 1`; the K-scaling factor is Class-3
forced; the `√r_n` factor is bounded but Class-2 absent
structural input (three candidate closure routes catalogued, no
promotion claimed); the existing K-zoo mass-ratio tables are
correctly read as upper bounds. Honest-landing discipline
preserved: form exact, bound exact, value declined.
