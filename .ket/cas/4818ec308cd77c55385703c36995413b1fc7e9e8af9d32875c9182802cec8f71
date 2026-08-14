# Vacuum stress meta-structure: anchors as stress denominations, complementary slackness, and the de-emergence ordering

**Verdict**: Part I recognize-mode (the stress inventory is already
canonical, piecewise); Part II MODAL ✓ / GENERATIVE ✗ (the
anchors-as-stress-denominations reading is statable and consistent
with the two-anchor feature, but alternatives exist — it is a
framing, not forced); Part III MODAL ✓ on dependency chains (the
reverse ordering is forced wherever emergence is chained),
GENERATIVE open on totality (whether the full de-emergence order is
total is not established).

Class: exploration-audit (Class 3 framing over Class 5 pieces). No
new primitive, no new number, nothing for `MANIFEST.yml`. Extends
PR #254's scoping discipline (`spacetime_dissipative_emergence.md`):
mechanics vs read-out, applied now to *what the anchors read*.

## The audit task

Two informally-posed questions, pressed against the substrate. Per
`vocabulary_is_the_work_pattern.md`, the first move is to name the
objects.

**(Q1)** *"What if the space constraints of the vacuum we exist
inside are a tension or a pressure?"* — named objects: the
**locked-sector tension** and the **unlocked-sector quantum
pressure**, with the anchors as the empirically supplied
**denominations** of these two stress components.

**(Q2)** *"Degree-of-freedom inexistence would be ordered backwards
from emerging order."* — named objects: **complementary slackness**
(stress is supported exactly on the extinguished degrees of
freedom; already structural principle 1 of `FRAMEWORK.md`) and
**LIFO unwinding** (descending toward the fuzzy Planck floor,
structure loses definition in the reverse of its emergence order).

## Part I — the stress inventory already in the substrate

The question "tension or pressure?" turns out to have a
sector-resolved answer: **both, one per anchor sector**, with a
threshold stress between them. All three pieces are already
canonical; this part only assembles them.

### I.1 The locked sector carries a tension (K = 1 side)

The locked modes (|F_6| = 13) are dark energy
(`baryon_fraction.md`); the framework's vacuum sector enters the
field equations as the Λ term, `G_μν + Λ g_μν = 8πG T_μν`
(`PROOF_A_gravity.md`, `quantum_gravity_interpolation.md` §3c). A
constant-Λ stress is, identically, equation of state `p = −ρ`: in
mechanical terms, **negative pressure — a tension**. Observation
concurs: Planck 2018 measures `w_DE = −1.03 ± 0.03`, consistent
with pure tension.

Two precision notes:

- **Symbol collision.** Cosmology's equation-of-state `w_DE = p/ρ`
  is *not* the framework's partial-locking weight `w` (`w_+ =
  13/14`, Lemma 1). This doc writes `w_DE` for the former,
  always subscripted.
- **Scope.** The framework does not separately derive
  `w_DE = −1`; it derives a cosmological-constant-*form* sector
  (the locked-mode count entering as Λ), and `w_DE = −1` is what
  constant-Λ means in GR. The tension reading inherits exactly
  that status: as good as the Λ-form derivation, no better.

### I.2 The unlocked sector carries a pressure (K < 1 side)

The quantum pressure is **derived**, not posited
(`continuum_limits.md` §6, status table: "Quantum pressure —
Derived (CLT on tree + Nelson)"): the Stern-Brocot tree is the RG
structure; per-level diffusion variance `σ²(d) ~ D₀/φ⁴ᵈ` converges
geometrically; CLT gives constant `D_eff = D₀/(1 − φ⁻⁴)`; Nelson
(1966) then yields the Bohm quantum potential
`Q = −(ℏ²/2m) ∇²√ρ/√ρ` with universal form. Its gravitational
appearance is the ε-dressed stress
(`quantum_gravity_interpolation.md` §3c):

    T_μν^{quantum} = −(ε/(1−ε)) × (quantum pressure terms),

sourced by the **unlocked** oscillator density, with
`ε(K) = 1 − Σ w(p/q, K)` the fraction that fails to lock. At
K = 1: ε = 0, the pressure vanishes, pure Einstein + Λ (tension
only). At K → 0: ε → 1, the pressure dominates (fully quantum).
The decoherence tax at the electroweak operating point is
`ε(K*) ≈ 0.034` at `K* = 0.892` (M_Z). (Provenance correction
2026-08-05: no computation in this repo produces K* = 0.892 — the
value exists only as a hardcoded constant in
`decoherence_correction.py:45`, and `beta_from_tongues.py`'s own
solve returns K* = 1.0; the canonical framework constant is
K* = 2^(−3/14) ≈ 0.862, `framework_constants.py:113`. The ε here
inherits the unsourced input.)

### I.3 The threshold between them carries a shadow price

At the a₀ = cH₀/(2π) boundary the framework already uses dual-
variable language verbatim: dark matter is "the dual variable
(shadow price of the synchronization constraint)"
(`a0_threshold.md`) — the cost of maintaining synchronization
below a₀, not a substance. And the same doc's Open section already
asks whether the threshold condition is KKT complementary
slackness. So the budget's three non-baryonic registers are
already stress-typed, piecewise:

| Sector | Mode content | Stress type | Source |
|---|---|---|---|
| Dark energy (13/19) | locked, |F_6| | tension (`w_DE = −1` form) | `baryon_fraction.md`, `PROOF_A_gravity.md` |
| Dark matter (5/19) | sign-rep, no EM (Lemma 2) | shadow price of the sync constraint at a₀ | `a0_threshold.md` |
| Quantum sector | unlocked density ρ, ε(K) | pressure (Bohm, ε-dressed) | `continuum_limits.md` §6, `quantum_gravity_interpolation.md` |

The K = 1 critical line — the same non-smooth boundary that forces
the two-anchor minimum (Lemma 3) — is the boundary between the
tension-carrying and pressure-carrying sectors. ε(K) is the stress
balance across it.

## Part II — anchors as stress denominations (Q1's meta-structure)

The mechanics fix every *dimensionless* property of both stresses:
the partition ratios (13 : 5 : 1 / 19, refined 13 : 70 : 181 /
264), the ε(K) profile, `g*(1/φ) = 0.697`, the Bohm form of the
pressure, the Λ-form of the tension, `Λℓ_P² = 13⁻¹⁰⁸/12` in Planck
units. What the mechanics cannot fix — by the reaudit's bright
line, *must not* fix — is the absolute denomination of either
stress in laboratory units. That is what the anchors are:

- **H₀ denominates the tension side.** Λ in GeV⁴, a₀ = cH₀/(2π),
  ρ_crit, the cosmic timeline — all K = 1-sector absolutes scale
  with the one cosmological anchor (`anchor_count_audit.md`).
- **v_EW denominates the pressure side.** The quantum pressure's
  scale is ℏ²/m²; ℏ and the absolute mass spectrum are
  particle-sector anchor territory (`anchor_count_audit.md`,
  `continuum_limits.md` §8: ℏ identified from tree geometry × the
  mass scale, "not derived from first principles").

**Restated mechanically, Lemma 3 reads: one medium, two stress
components, non-smoothly separated at K = 1 — so neither stress's
denomination is inferable from the other's, and each requires its
own empirical gauge.** "Anchor" = the empirically supplied
denomination of one vacuum stress component. The meta-structure Q1
suspected is real, and it is *exactly* the two-anchor feature seen
mechanically rather than dimensionally.

Why this does not breach anchor-underivability: in a dimensionless
optimization, dual variables are determined only as ratios;
absolute stress values enter through a unit gauge that the
optimization cannot supply. The structural *form* of each stress is
substrate-derived; its *denomination* cannot be — "deriving it ⇒ it
is not an anchor" (`anchor_count_reaudit.md`). The shadow-price
reading and the Basepoint Principle are the same statement in two
vocabularies.

### Empirical probes at framework-named boundaries

| Boundary (named) | Stress signature | Empirical handle |
|---|---|---|
| K = 1 critical line | tension/pressure separation | `w_DE = −1` purity: any robust `w_DE ≠ −1` (evolving dark energy) presses the locked-sector tension reading |
| a₀ = cH₀/(2π) (EM-MOND threshold) | shadow price activates | RAR at 4%; `a₀(z) = cH(z)/(2π)` rising with z (RC100 direction matches) |
| K* = 0.892 (M_Z operating point — unsourced; see §I.2 provenance correction) | pressure tax ε ≈ 3.4% | decoherence-tax accounting in Ω_b residual (`baryon_fraction.md`) |
| Anchor row, coherence matrix | denomination constancy | H₀ tension already flagged as candidate bifurcation signature in three cells (`coherence_matrix_completion_audit.md`) — a *drifting denomination* would be a stress non-equilibrium, the first meta-structure observable |
| Fuzzy Planck floor | stress support ends | no direct handle; ordering constraints only (Part III) |

## Part III — complementary slackness and the de-emergence ordering (Q2)

### III.1 Stress lives exactly on the extinguished degrees of freedom

KKT complementary slackness (structural principle 1,
`FRAMEWORK.md`): at the optimum, each constraint is either
*slack* (its multiplier is zero) or *active* (its multiplier is
nonzero). Translated: **where a degree of freedom exists, there is
no stress; where a degree of freedom is extinguished, the stress is
nonzero and is carried by exactly that absence.** The framework
instantiates this repeatedly, and had not named the pattern:

| Extinguished DoF (active constraint) | Stress it carries | Source |
|---|---|---|
| Dark state D (the unobservable fourth phase state) | the metric's minus sign — signature (3,1) | `minkowski_signature.md` |
| Sign-rep modes' EM coupling (monodromy −1 kills it) | the DM sector, the a₀ shadow price | Lemma 2, `a0_threshold.md` |
| Global time-reversal operator (non-orientability) | positive entropy rate, the arrow | `second_law_topological.md` |
| Momentum (first-order tick; no conjugate variable) | the manufactured `∂²_t` + arrow friction `2λ∂_tφ` | `tick_continuum_construction.md` |
| Prime 5 in the canonical register | the v/M_P anchor obstruction (forced absence = Feature) | `anchor_count_reaudit.md`, `path_a_walkthrough.md` |
| Unlocked modes' coherence (fail to lock, fraction ε) | the quantum pressure | `quantum_gravity_interpolation.md` |

The pattern is uniform: **forced absence = active constraint =
stress-bearing.** Q2's first half, formalized: degree-of-freedom
inexistence is not a void; it is the support of the dual
variables. The framework's "dark" inventory *is* its dual side.

### III.2 De-emergence runs backwards through the emergence stack

The emergence order is a dependency stack
(`spacetime_dissipative_emergence.md` Part II):

    tick → self-sustenance ≡ Klein topology → Q mod 2
        → coherence/geometry → Einstein + Λ

**Modal (forced) part.** Wherever emergence is dependency-chained —
B exists only given A — the de-emergence order is forced to be the
reverse: descending in scale, B must lose definition before A.
This is LIFO unwinding: last emerged, first extinguished. For
chained DoFs the claim is theorem-shaped, not conjecture.

**The substrate already exhibits it, piecewise:**

1. Einstein (top of stack) corrects *first*: the quantum stress
   enters at O(ε) immediately below K = 1
   (`quantum_gravity_interpolation.md` §3b–3c).
2. Geometry (one level down) degrades next: the coherence tensor
   acquires the unlocked noise term `C_ij^{unlocked}`; "geometry is
   coherence, decoherence is curvature" run in reverse
   (`adm_dictionary.md`, `quantum_gravity_interpolation.md` §3a).
3. Q mod 2 (mid-stack) "emerges *across* the crossover, with
   intermediate scales giving intermediate well-definedness" — and
   so degrades across it descending
   (`q_mod2_planck_emergence_audit.md`).
4. Klein topology ≡ self-sustenance (the bottom rung above the
   tick) fails last: "below the Planck scale, the tree has no
   nodes — there are no modes to lock"
   (`quantum_gravity_interpolation.md` §4c).
5. The tick itself (bottom of stack) never fails; its rank-1
   dissipation structure is the one invariant that survives all
   scales unconditionally, while the mid-stack invariant Q mod 2
   is topology-conditional
   (`conservation_scale_stratification_audit.md`). Invariant
   robustness is ordered by stack depth — which is the same
   statement.

**Generative (open) part.** Whether the full de-emergence order is
*total* is not established: parallel branches (d = 3 and the
signature emerge from different filters on the same Z₆ structure)
are only partially ordered by dependency, and the framework's
prose-built derivation graph is not yet a typed DAG
(`scripts/drift/check_dag_acyclic.py` is advisory for the same
reason). The forced result is the reverse *partial* order; totality
would require the emergence graph itself to be a chain.

### III.3 The joint statement

Combining III.1 and III.2: ascending, each emergence step activates
a constraint, extinguishes a degree of freedom, and deposits a
stress on the absence; descending, the stresses are released in
reverse order of deposition. The vacuum's stress inventory (Part I)
is the *current* layer of this stack — which is why its components
are sector-resolved by the same K = 1 boundary that orders the
stack's top. Q2's suspicion, formalized: **the dual ladder (where
stress lives) is the primal ladder (what emerged) read backwards,
and complementary slackness is the rung-by-rung exchange rate.**

## What this does not establish

1. **`w_DE = −1` is inherited, not independently derived** — the
   tension reading is exactly as strong as the Λ-form derivation
   of the locked sector.
2. **The anchors-as-denominations reading is a framing** (MODAL ✓ /
   GENERATIVE ✗): consistent with and illuminating of Lemma 3, but
   not forced over the plain "address" reading. It earns Class 5
   status only if it produces a prediction the address reading
   does not (candidate: H₀-drift as stress non-equilibrium, the
   coherence-matrix bifurcation row).
3. **Totality of the de-emergence order** — open (III.2); only the
   reverse partial order on dependency chains is forced.
4. **The KKT formalization of the a₀ threshold** — still the open
   item recorded in `a0_threshold.md`; this doc uses its language
   but does not close it.
5. **No quantitative stress accounting** — no computed tension or
   pressure value is matched to data here beyond what the source
   docs already claim.

## Falsifiers

| Test | Falsifier |
|---|---|
| Evolving dark energy | A robust measurement of `w_DE ≠ −1` (time-varying) breaks the pure-tension reading of the locked sector as stated; the stress map would need a dynamical tension component the current Λ-form does not supply. |
| Stress without absence | A vacuum stress component identified with a *slack* constraint — nonzero stress where the corresponding DoF demonstrably exists — violates the complementary-slackness pattern (III.1). |
| Out-of-order de-emergence | A dependent DoF remaining well-defined at a scale where its prerequisite has lost definition (e.g., definite Q mod 2 where Klein topology is not a substrate fact) breaks LIFO unwinding — and would contradict `q_mod2_planck_emergence_audit.md` independently. |
| Non-Bohm quantum pressure | Per `continuum_limits.md`: a demonstrated deviation of the quantum potential from the constant-D Bohm form removes the pressure side of the stress map. |
| Denomination inferable | Any derivation of one anchor's scale from the other's would falsify the two-stress reading *and* Lemma 3 simultaneously (they stand or fall together — by design). |

## Status

Exploration-audit, Class 3 over Class 5 pieces. Recognize-mode in
Part I (assembly of `baryon_fraction.md`,
`quantum_gravity_interpolation.md`, `continuum_limits.md` §6,
`a0_threshold.md` — no new content); framing in Part II (consistent
restatement of Lemma 3, upgrade path named in residual 2); mixed in
Part III (forced on chains, open on totality). Names three objects:
the **sector-resolved stress map** (tension | shadow price |
pressure), **anchors as stress denominations**, and **LIFO
unwinding** with complementary slackness as the DoF-inexistence ↔
stress exchange. Nothing enters `MANIFEST.yml`.

## Cross-links

- `spacetime_dissipative_emergence.md` — the emergence stack this
  doc reads backwards; the mechanics/read-out scoping extended
  here to stresses/denominations.
- `baryon_fraction.md` — locked modes = DE; the locked/unlocked
  two-senses vocabulary note (observed here: tongue-interior sense
  throughout).
- `quantum_gravity_interpolation.md` — ε(K), the ε-dressed quantum
  stress, "below Planck the tree has no nodes."
- `continuum_limits.md` §6–§8 — the quantum pressure derivation
  (CLT on tree + Nelson); ℏ identification status.
- `a0_threshold.md` — DM as dual variable / shadow price; the open
  KKT question this doc's language leans on.
- `anchor_count_audit.md`, `anchor_count_reaudit.md`,
  `basepoint_principle.md` — what anchors are and why underivable.
- `minkowski_signature.md`, `second_law_topological.md`,
  `tick_continuum_construction.md` — rows of the slackness table.
- `conservation_scale_stratification_audit.md` — invariant
  robustness ordered by stack depth.
- `q_mod2_planck_emergence_audit.md` — the crossover
  well-definedness gradient (de-emergence row 3).
- `coherence_matrix_completion_audit.md` — H₀ tension as candidate
  bifurcation signature (the denomination-drift probe).

## One-line summary

The vacuum's space constraints are a tension *and* a pressure,
sector-resolved across the K = 1 line — locked-sector tension
(dark energy), threshold shadow price (dark matter), unlocked-
sector Bohm pressure (quantum) — with the two anchors as the
empirically supplied denominations of the two stress components;
and degree-of-freedom inexistence is the support of these stresses
(complementary slackness), ordered backwards from emergence (LIFO
unwinding): last to emerge, first to lose definition at the fuzzy
floor.
