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
| **Audit Finding 4 — S_v K-dependent / inflation duration** | **Sharpened, conditional** (NOT fully closed — see open #INF below): two-reading problem reconciled to `\|∇K\|_inflation ≈ 2.68`; geometric-seam route to `K_inflation` proven structurally impossible ∀K — the `√K` cancellation **is** `substrate_determinism.md` inviolables #1 (Z₂/winding topological-charge conservation) ∧ #9 (arrow irreversibility) borne by the kink (mass–width invariant); structural protection, **no new input** | `k_inflation_seam_obstruction.md` → `substrate_determinism.md` #1∧#9 | "parameter-free from S_v=16" → retracted → two readings (≈2 vs ≈3.55) flagged inconsistent → **reconciled to 2.68; residual = seam structure only; protection traced to existing inviolables** |
| **NAND / primitive parsimony** | Four objects tighten to **2 primitives (mediant + EML) + 2 derived (Klein bottle + half-twist)** | `wave_particle_substrate.md` | NAND-reduction probe undermined → parsimony tightened 4→2 |
| **#TICK — minimal-tick rule / phase advance** | **Structurally closed.** Phase advance = per-tick binary Z₂ winding-sign. (a) selector = the saddle-node branch at the J-symmetric separatrix (deterministic, no noise). (b) Goldstein–Kac: eliminating the binary index *manufactures* `∂²_t` (momentum from context, exact identity); force-biased flip *manufactures* `+ω₀² sinφ` (sign forced by restoring energetics); lattice gives `−c²∂²_xφ`; `β=ω₀²/v` fixed by substrate constants — first-order irreversible tick → sine-Gordon, conservative in the `λ→0` limit. **Stochastic-Kramers competitor #2 ELIMINATED** (no `kT` anywhere). Residual is *quantitative only*: the magnitude of the arrow-friction `λ` at the coarse scale (the `2λ∂_tφ` term is the substrate's predicted irreversibility, inviolable #9 — a feature) + standard mean-field closure. | `born_rule_parameter_free.md` (a; #2 discriminated) → `tick_continuum_construction.md` (b; #2 eliminated) → `substrate_determinism.md` (#9; momentum-dissolution + arrow now jointly constructive) | "phase advance under-determined" → binary-Z₂ hypothesis → (a) closed via saddle-node → **(b) closed via Goldstein–Kac; #2 eliminated; residual = `λ` magnitude only** |

## Genuinely open (minimized — only what is actually unsettled)

| # | Open item | Where | What would close it |
|---|---|---|---|
| **#INF** | Inflation-era seam **structure**: the geometric `(1−K)√K` form is structurally insufficient ∀K (the insufficiency is *protected* by inviolables #1∧#9 — the mass–width invariant — so it is not a near-miss to be tuned away); a non-geometric seam delivering `\|∇K\|_inflation ≈ 2.68` is needed — *or* an honest one-input boundary | `k_inflation_seam_obstruction.md`, `inflation_duration.md` open #2 | a derived non-geometric inflation-era seam form, or explicit acknowledgement that `\|∇K\|_inflation` is an independent input |
| **#ANCHOR** | Two-anchor minimality re-audit (now read as structural feature, not defect); five original obstructions not formally re-audited under the reframe | `anchor_count_audit.md`, `vocabulary_is_the_work_pattern.md` Consequence 1 | formal re-audit of the five obstructions under the structural-feature reframe |
| **#PROPOSED** | Proposed-tier (longer horizon): `K_c(F_n/F_{n+1})` closed form; T2#7 measurement-arc residuals; K-zoo kink-mass ratios (conjectural at K<1) | `framework_status.md` "Proposed" | the per-item upgrade criteria in `framework_status.md` |

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
- `k_inflation_seam_obstruction.md` — Finding 4 disposition and
  the sole substantive open item (#INF).
- `audit_findings_3_4_disposition.md` — Findings 3 & 4 origin;
  Finding 3 now closed, Finding 4 sharpened (this ledger is the
  current state; that doc is the origin record).

## One-line summary

One ledger: every resolved thread's settled outcome + canonical
doc + one-line path, with a minimized loud list of the only three
genuinely-open items (#INF inflation-era seam structure, #ANCHOR
two-anchor re-audit, #PROPOSED longer-horizon) — so no other doc
needs its own supersession arc and no isolated chunk is wrong.
