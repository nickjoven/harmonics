# Thread chronology — the single ledger

**This is the one place the framework's resolved-thread history
lives.** Every row is self-contained: the *settled* outcome, the
canonical doc, and the path it took (one terse line). No other
doc should carry its own supersession arc or stacked update
blockquotes — they point here.

RAG-safety rule: each row states the settled answer first and
in full, so a chunk retrieved from this file in isolation is
correct without cross-referencing. Other docs' headlines/Status
sections state the *settled* value (not the historical one); the
*path* exists only here.

Forward discipline: when a claim settles, **overwrite its open
framing in place** (do not stack another "Update:" blockquote)
and add/extend its row here. Settled items compress hard;
genuinely-open items (bottom section) stay loud.

## Resolved threads

| Claim | Settled outcome | Canonical doc | Path (terse) |
|---|---|---|---|
| **S_v(K=1)** | **≈ 11.515** (Planck units), discrete native, direction-asymmetric, computed by hand + numerically verified | `discrete_reduction_computed.md` | 16 (Phase 2, assumed-symmetric) → 13 (collinear-formula error) → 16 (dark-twin restore) → 0<S_v<16 (continuum-shadow bound) → 16 (symmetric discrete placeholder) → **11.515** (computed: `H_BB≈9.580 ≠ H_CC≈3.645`, `E_cross=−4`) |
| **Caveat 2 — half-twist vs full-kink assignment for mode C** | **Resolved**: π half-twist (`H_CC≈3.645`), forced by `xor_derivation.md` §3.3 homotopy theorem; a 2π x-winding is the trivial/periodic sector, not antiperiodic | `discrete_reduction_computed.md` | flagged "key open structural input" → resolved affirmatively (same session) |
| **E_cross (crossing term)** | **= −4 exactly** — finite, bounded discrete matrix element | `discrete_reduction_computed.md` | continuum route → −2 M_k = −16 pathology (representation error) → named discrete-vs-continuum-shadow → computed finite −4 |
| **Audit Finding 1 — rectangle perpendicularity** | **Closed** (catastrophic → articulation gap; pieces implicit, no new primitive) | `rectangle_perpendicularity.md` | raised catastrophic → closed by explicit assembly |
| **Audit Finding 2 — small primes + d origin** | **Closed** (articulation gap) | `qd_origins.md` | raised catastrophic → closed |
| **Audit Finding 5 — f_exit parsimony** | **Closed**: `f_exit=exp(−S_v)` is the natural specialization of the framework's action-weighted path-integral sampling (Boltzmann form) | `f_exit_natural.md` | raised catastrophic → closed |
| **Audit Finding 3 — "4-mode reduction exact"** | **Closed**: the explicit discrete reduction is delivered; `S_v(K=1) ≈ 11.515`, not 16 | `discrete_reduction_computed.md` | "S_v=16 exact" → qualified ("leading-order pending reduction matrix") → **closed (computed 11.515)** |
| **Audit Finding 4 — S_v K-dependent / inflation duration** | **Conditional on the cosmological anchor (closed disposition).** Two-reading problem reconciled to `\|∇K\|_inflation ≈ 2.68`; geometric-seam route proven structurally impossible ∀K — the `√K` cancellation **is** inviolables #1∧#9 borne by the kink (mass–width invariant). The residual (#INF) is now itself closed: `\|∇K\|_inflation` is the Schwinger-image of `H_inflation`, an out-of-class anchor — the framework *correctly declines* (see #INF). Inflation duration stays anchor-conditional, as the disposition always said. | `k_inflation_seam_obstruction.md` → `substrate_determinism.md` #1∧#9 → `inflation_seam_anchor_closure.md` | "parameter-free from S_v=16" → retracted → reconciled to 2.68 → **#INF closed: anchor-conditional, correctly declined** |
| **NAND / primitive parsimony** | Four objects tighten to **2 primitives (mediant + EML) + 2 derived (Klein bottle + half-twist)** | `wave_particle_substrate.md` | NAND-reduction probe undermined → parsimony tightened 4→2 |
| **#TICK — minimal-tick rule / phase advance** | **Structurally closed.** Phase advance = per-tick binary Z₂ winding-sign. (a) selector = the saddle-node branch at the J-symmetric separatrix (deterministic, no noise). (b) Goldstein–Kac: eliminating the binary index *manufactures* `∂²_t` (momentum from context, exact identity); force-biased flip *manufactures* `+ω₀² sinφ` (sign forced by restoring energetics); lattice gives `−c²∂²_xφ`; `β=ω₀²/v` fixed by substrate constants — first-order irreversible tick → sine-Gordon, conservative in the `λ→0` limit. **Stochastic-Kramers competitor #2 ELIMINATED** (no `kT` anywhere). Residual is *quantitative only*: the magnitude of the arrow-friction `λ` at the coarse scale (the `2λ∂_tφ` term is the substrate's predicted irreversibility, inviolable #9 — a feature) + standard mean-field closure. | `born_rule_parameter_free.md` (a; #2 discriminated) → `tick_continuum_construction.md` (b; #2 eliminated) → `substrate_determinism.md` (#9; momentum-dissolution + arrow now jointly constructive) | "phase advance under-determined" → binary-Z₂ hypothesis → (a) closed via saddle-node → **(b) closed via Goldstein–Kac; #2 eliminated; residual = `λ` magnitude only** |
| **#FLOW — mediant vs. continuous flow (competitor #1)** | **Decided (parsimony).** The sole parameter-free discriminator is the K=1 complement. Computed the framework's own total tongue-width `Σ w(p/q,K=1) = 1.5617 > 1` (converged) — **past exact-filling: the complete-tree regime**, far from the critical knife-edge `Σ=1` where the universal `D ≈ 0.8700` lives. The flow's sole fingerprint is **structurally absent**; every flow regime excluded (critical & sub-critical by `Σ`; supercritical by the recorded Adler-only/monotone/not-chaotic eliminations). Continuous flow **eliminable**; `D≈0.8700` is *not* a framework prediction. Residual is *philosophical*: elimination-by-absent-fingerprint + parsimony (corroborated by the independent Finding-3 complete-tree position), **not** a positive discreteness proof. With #2 already eliminated, **no foundational competitor survives**. | `mediant_vs_flow_calc.md` / `mediant_vs_flow_calc.py` ← `mediant_vs_flow_problem.md`; `framework_status.md` "Eliminated" | posed → calculation run → **flow fingerprint absent at K=1; flow eliminable by parsimony; discrete-fundamental favored, not proven** |
| **R1 — "prove the continuum *requires* the discrete generator"** | **Structurally closed: unprovable in principle, ∅-entailed (NOT a parsimony concession, NOT a proof of discreteness).** Requirement (ii) [is "the substrate is coupled S¹ oscillators (1)-(3)" derived or posited?] returned **POSITED**: oscillator (D1) + coupling (D2) are floor definitions; only S¹ is derived, and only *conditional on* that posit; antisymmetry & smoothness are explicit "definition of the physical system" (`mediant_derivation.md` L235-237). Negative on (ii) nulls (i)/(iii). Formalized: every fork = `(B, ι, δ)`; **∅ = (B, ι, 0) = a basepointless Z₂-torsor** = the codimension-1 common apex all forks degenerate to under orientation-forgetting. No ι-equivariant selector exists at δ=0 ⇒ R1 unprovable ⇔ root is ∅ ⇔ the framework's ∅-doctrine. A *provable* R1 would *falsify* ∅. **Bright line: this is self-consistency, not a proof — ∅ explains why no one can force the root; it does not pick the discrete root. Discrete-fundamental stays favored only by downstream `#TICK`/`#FLOW`/parsimony.** | `empty_fork_cap.md`; `mediant_derivation.md` (the (ii) linchpin) ↔ `substrate_determinism.md` (posit-level ontology, independent convergence) ↔ `qd_origins.md` (concrete first mediant) ↔ `figure_eight.md` (the 50/50 δ→0 apex) | R1 decomposed (i/ii/iii) → audit (ii) first (a negative nulls the rest) → (ii) POSITED → formalized ∅ as basepointless Z₂-torsor → **R1 retired: ∅-entailed unprovable; correct permanent phrasing of discrete-fundamental = "favored, not proven, and necessarily not-provable"** |
| **#INF — inflation-era seam structure** | **Closed as the principled option (b).** `\|∇K\|_seam(t)` is *by the framework's own definition* the Schwinger-inverse of `H(t)` (`inflation_duration.md` L120/141); `H_inflation` is **Out-of-class — anchor-dependent** by the framework's own taxonomy (`framework_status.md` L131-138). So `\|∇K\|_inflation` is the Schwinger-image of an out-of-class absolute, **not** a substrate-geometric ratio. The geometric obstruction (inviolables #1∧#9, `empty_fork_cap.md`) is the framework **correctly declining** to manufacture an anchor-side quantity from substrate geometry — same accepted shape as the **A_s/Instance-7 closure** (`framework_status.md` L35), an instance of two-anchor minimality (L32/L150). The cascade-ladder route (a) also reduces to (b) (needs the iteration↔length anchor). **Bright line: a classification result, NOT a prediction of 2.68 and NOT a derivation of inflation duration.** | `inflation_seam_anchor_closure.md` ← `k_inflation_seam_obstruction.md` / `inflation_duration.md` open #2; `framework_status.md` (Out-of-class, two-anchor, A_s/Instance-7); feeds `#ANCHOR` | posed (a derived seam, or honest one-input) → geometric route inviolable-dead ∀K → **(b): `\|∇K\|_inflation` = Schwinger-image of the anchor; correctly declined; two-anchor minimality at the inflation epoch** |
| **#ANCHOR — five anchor-count obstructions, formal re-audit** | **Closed: none open.** Re-audited under `vocabulary_is_the_work_pattern.md` Consequence 1 + the #INF discriminator (forced structural absence = Feature; merely-operational absence = open). **#5** = the one rigorous load-bearing closure (substrate self-consistency K=1 line forces sector decoupling, `path_closures_iter3.md` D.3); **#1=#2** closed as Feature (prime-5 absent from the {2,3} register, `path_a_walkthrough.md`); **#3** upgraded asserted→argued (an anchor cannot be self-derived — the #INF circularity); **#4** dissolved (subsumed by #5; existed only under the rejected "two anchors collapse to one" framing). Two-anchor minimality is an *established* structural feature, one instance of the multiply-verified "structurally-forced decline" pattern shared with #INF, A_s/Instance-7 and the R1/∅ cap. **Bright line: closure by verified structural feature, NOT a derivation of `v/M_P`, `v_EW`, or any anchor (deriving one would contradict the feature).** | `anchor_count_reaudit.md` ← `anchor_count_audit.md` (the 5) / `vocabulary_is_the_work_pattern.md` C1 / `path_closures_iter3.md` D.3 / `path_a_walkthrough.md` / `hierarchy_problem_translation.md`; unifies with `inflation_seam_anchor_closure.md`, `empty_fork_cap.md` | "all five reframed/closed" (asserted, imprecise) → formal per-obstruction re-audit → **#5 rigorous, #1=#2 Feature, #3 argued, #4 dissolved; none open; the decline-pattern triply instantiated** |

| **The Basepoint Principle** (meta-pattern → named principle) | The "structurally-forced decline" regularity — verified at R1/∅, the dimensional anchors, #INF, the anchor obstructions, A_s/Instance-7 — **elevated to a first-class named principle** (peer to no-rescaling / the inviolables): the framework supplies torsorial structure, never the basepoints; a declined basepoint is a *feature* iff its missing selecting section is *structurally forced* (obstruction exhibited), else *open*. The dimensional inputs are the canonical scale instance (ℝ₊-torsor: nature/number sayable, value declined, dynamically inert by torsor-invariance). **Bright line: a consistency boundary with a discriminator — not a derivation, not a licence.** | `basepoint_principle.md`; `framework_status.md` (Survives); unifies `empty_fork_cap.md` / `inflation_seam_anchor_closure.md` / `anchor_count_reaudit.md` | meta-pattern observed across closures → proposed for elevation → **named: the Basepoint Principle (discriminator-centered)** |
| **#PROPOSED disposition** (the three Proposed-tier items, triaged) | **A (K_c):** Gap-1 K_c closed (`k_critical_phase_b.md`, deferred-to as authoritative); framework uses `K_map=1` exact; the finite-`n` Fibonacci closed-form is **known-hard external KAM math, out of scope, not a framework gap**; secondary RFE branch born first-order at `K_c^RFE≈1.56`, with `K_c^RFE=Σw(1)=1.5617` an **explicitly-flagged conjecture, NOT claimed**. **B (T2#7):** iteration-to-time anchor **Basepoint-closed** (#INF pattern). **C (K-zoo):** **Class-2 by construction** — K=1 formula Class-3 stands, K<1 mapping correctly not chased. Nothing overreached. | `proposed_items_disposition.md` ← `k_critical_phase_b.md` / `k_critical_phase_a.md` / `rational_field_equation.md`; `inflation_seam_anchor_closure.md`; `sine_gordon_substrate.md`; `ansatz_audit_policy.md` | A deferred + out-of-scope-reframed, B Basepoint-closed, C Class-2-disposed |

## Genuinely open (minimized — only what is actually unsettled)

| # | Open item | Where | What would close it |
|---|---|---|---|
| **#PROPOSED residual** (reduced after disposition) | Only what genuinely remains after `proposed_items_disposition.md`: (i) T2#7's two *dynamical* sub-residuals — continuous K(t) during measurement, multi-tongue cascade — **operational, not forced** (so by the Basepoint discriminator: open, *not* declined); (ii) the K<1 K-zoo kink-mass mapping — a **standing Class-2-flagged conjecture**, correctly *not chased* per the framework's honest-landing discipline. Neither is consistency-forced; both are longer-horizon. | `proposed_items_disposition.md`; `sine_gordon_substrate.md` (C); measurement-arc docs (B) | (i) a derived collapse-dynamics for continuous K(t)/multi-tongue; (ii) a *structural forcing* for the K<1 sine-Gordon-per-sector reduction (absent which it stays Class-2, not pursued) |

## Status

Class 3 (consolidation / record hygiene). No new primitive, no
new physics. This ledger is the single chronology home; the
catalog (`framework_status.md`) carries settled state only; other
docs' headlines/Status state settled values with the path here.

## Cross-links

- `discrete_reduction_computed.md` — canonical S_v(K=1); its
  "What this supersedes" table is mirrored into this ledger's
  S_v row (this ledger is now the authoritative chronology).
- `framework_status.md` — the settled-state catalog; points here
  for "how it settled".
- `k_inflation_seam_obstruction.md` / `inflation_seam_anchor_closure.md`
  — Finding 4 disposition; #INF now closed (anchor-conditional,
  correctly declined).
- `audit_findings_3_4_disposition.md` — Findings 3 & 4 origin;
  Finding 3 now closed, Finding 4 sharpened (this ledger is the
  current state; that doc is the origin record).

## One-line summary

One ledger: every resolved thread's settled outcome + canonical
doc + one-line path. After the #PROPOSED disposition the genuine
residual is only the **#PROPOSED residual** row — T2#7's two
dynamical sub-residuals and the Class-2-flagged K<1 K-zoo
conjecture (both longer-horizon, neither consistency-forced;
#INF, #ANCHOR, and the bulk of #PROPOSED closed/disposed) — so no
other doc needs its own supersession arc and no isolated chunk is
wrong.
