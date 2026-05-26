# Era-timeline disposition (settling N9 S5)

## Status

**Settles the last residual** left open by the continuity-in-K
disposition (`continuity_in_K_nulls.md`): the cosmological *era
timeline* (N9 S5 — inflation→matter→Λ). It resolves into **three
tiers** with different statuses; it is **not** a single vague "open
frontier." No overclaim: one tier is structural, one is
anchor-declined, and one stays Class-2 (and is explicitly *not*
promoted here).

This completes the disposition of N9:

| Step | Content | Status |
|---|---|---|
| S1–S2 | Friedmann form at `r=1` | **structural** (`k_of_t_friedmann.md`) |
| S3 | `F_locked(K)` as *continuous* `Ω_m(K)` | **not-a-blocker** (deflation; the matter sector runs by the discrete cascade, no continuous `w(K)` needed) |
| S4 | `τ_unlock(n)` in seconds | **anchor-declined** (out-of-class, needs `H_0`) |
| S5 | era timeline | **this doc** — three tiers below |

---

## Tier 1 — era ORDERING: structural

The *sequence* inflation→matter→Λ (and the direction of travel) is
forced, with no continuous `w(K)` required:

- **Direction forced.** `K_eff` decreases monotonically as the
  universe expands (`cosmological_cycle.md` "stick-slip transfer";
  H acts as a decoherence rate). The arrow does not reverse —
  substrate inviolable #9 (arrow-of-time monotonicity,
  `time_axis_split.md`; the antiperiodic-x arrow).
- **Slip-order forced.** As `K_eff` falls, tongues close in order of
  stability: width `∝ (K/2)^q`, so **high-denominator (high-q) modes
  slip first, small-q (simple-ratio) modes persist longest**. This is
  the same Farey / small-denominator ordering that runs the whole
  framework — discrete, forced, *not* a continuous interpolation.
- **Endpoints forced.** Start: `K=1`, all-locked, the Einstein
  continuum. End: the de Sitter equilibrium `Ω_Λ = 13/19` — a fixed
  point (`cosmological_cycle.md`; Survives).
- **Crossover combinatorial.** The roles-reverse point (gap coverage =
  tongue coverage) is computed from the F₆ tongue sum
  `Σ φ(q)/q²` — a combinatorial quantity, not a fit.

So the ordering is a **discrete, forced cascade between forced
endpoints along a forced arrow.** Structural — and, crucially, it
needs *only* the discrete slip-order, consistent with the
continuity-in-K deflation (no continuous `w(z)`).

## Tier 2 — absolute SCHEDULE: anchor-declined

The *durations, times, and temperatures in physical units* are
out-of-class — they need the cosmological anchor `H_0`, and
`framework_status.md` already files them there:

```
 τ_unlock(n) in seconds   | H_0
 Inflation-end time (s)   | H_0
 Reheating temperature    | H_0
 H_inf in GeV             | H_0
```

This is the two-anchor minimality / Basepoint decline (the framework
supplies dimensionless structure, never the dimensionful basepoint).
Correctly declined — not a gap.

## Tier 3 — the K_eff↔epoch/energy MAPPING: the one genuine residual (Class 2)

What is *neither* structural-ordering *nor* absolute-schedule is the
**dimensionless mapping** between `K_eff` and cosmic epoch / energy
scale — the `cosmological_cycle.md` timeline's `K_eff` values
(`~0.98` inflation-end, `~0.95` recombination, `~0.89` present) and
the `K_cross ≈ 0.75 ↔ ~10 GeV` identification. The doc itself marks
these heuristic: *"from the coherence cascade data,"* *"mapped to the
SM."*

This is **Class 2** — and it is the **same object as the
"K↔energy-scale map" struggle**: a dimensionless `K`-to-scale relation
that is not yet forced (and cannot be cured by an anchor, since it's
dimensionless). Its structural candidate is the **discrete cascade**
`K_n^d = b^{−n}` (`master_cascade_identity.md`) — the matter-sector
"running."

**Update (2026-05, #163): the cascade's *structural* gate is now
closed; the residual stays Class 2 on the *statistical* gate.** For the
first cascade↔observable link, the Salpeter IMF slope
(`imf_bowed_cascade.md`):
- **Structural gate — closed.** `α = −q₂ − n/d = −7/3` with the depth
  lemma proven (`imf_step2_klein_orbit.py`: `d = 3 = q₃` = Klein-orbit
  count of F₃, `n = 1` non-redundant flip), and — a genuine forcing —
  `orbit_count(F_m) = m` holds *only* for `m ∈ {2,3,4}`, **selecting the
  small-denominator cascades and excluding** the Z₆ (d=6) and K\* (d=14)
  sectors. So the cascade is a *structurally-grounded* K↔scale candidate
  with a *forced* depth, not a free fit.
- **Statistical gate — open.** The pigeonhole audit
  (`cascade_slope_check.py`) gives `p ≈ 0.10` for the Salpeter rung —
  suggestive, not decisive; it does not clear `α = 0.05`.

So the mapping is now a **structurally-forced candidate that remains
Class 2 for lack of statistical decisiveness** — *not* promoted to
structural. The live residual is now sharply localized: **the
statistical case, not the structure.** Still tracked with the
discrete-cascade work, not with "continuous K(z)."

---

## Net

The era timeline is fully characterized, not vaguely open:

- **ordering** → structural (forced cascade between forced endpoints);
- **absolute schedule** → anchor-declined (out-of-class, `H_0`);
- **K↔epoch/energy mapping** → the one genuine residual, **Class 2**,
  identical to the K↔energy-map question, whose structural candidate
  is the discrete cascade (not continuous running).

So N9 S5 contributes **no open *structural* gap**: its derivable part
(ordering) is structural, its undelegatable part (schedule) is
correctly declined, and what remains (the K↔energy mapping) is a
*dimensionless Class-2 item* that lives with the cascade thread — not
a "continuous-K-in-cosmology" blocker. With S1–S2 structural, S3
deflated, and S4 anchor-declined, **N9 is fully dispositioned.**

## What this does NOT claim

- Does **not** promote the K↔energy mapping past Class 2, nor the
  cascade↔Salpeter datum (gated, `imf_bowed_cascade.md`).
- Does **not** derive absolute durations (Tier 2 stays declined).
- The structural-ordering claim rests on the *forced* pieces (arrow,
  slip-order, endpoints, combinatorial crossover) — **the specific
  `K_eff` numerical values are explicitly Tier 3, not part of the
  structural claim.**

## Cross-links

- `continuity_in_K_nulls.md` — the disposition this completes (the
  residual it flagged "plausibly anchor-conditional" is now tiered).
- `cosmological_cycle.md` — stick-slip transfer, the timeline,
  `K_cross`, the de Sitter equilibrium.
- `framework_status.md` "Out of class" — the anchor-declined schedule
  items (Tier 2); two-anchor minimality / Basepoint Principle.
- `time_axis_split.md`, `substrate_determinism.md` (inviolable #9) —
  the forced arrow.
- `master_cascade_identity.md`, `imf_bowed_cascade.md` — the discrete
  cascade `K_n^d = b^{−n}` and the gated Salpeter datum (Tier 3's
  structural candidate; tracked separately).
- `k_of_t_friedmann.md` — S1–S2; the N9 disposition table.

## One-line summary

The cosmological era timeline (N9 S5) settles into three tiers —
**ordering structural** (a forced discrete cascade between forced
endpoints `K=1 → Ω_Λ=13/19` along a forced arrow), **absolute schedule
anchor-declined** (out-of-class, needs `H_0`), and the
**K_eff↔epoch/energy mapping the one genuine Class-2 residual**
(identical to the K↔energy-map question, structural candidate = the
discrete cascade, not promoted here) — so N9 contributes no open
*structural* gap and is fully dispositioned.
