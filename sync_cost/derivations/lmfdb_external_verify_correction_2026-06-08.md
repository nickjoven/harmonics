# External verification correction — LMFDB substrate retrieval for f_{6,4}

> **Surgical correction.** External substrate retrieval (LMFDB
> 6.4.a.a + pure-Python W_d cusp action reproduction) reveals that
> several load-bearing numerical claims in PRs #244, #245, #246 were
> cached from session memory, not retrieved from substrate, and were
> wrong. This document records the verification, the overturned
> values, the corrections applied in place, and the verify-before-
> assert post-mortem. The audit narratives in their original framing
> remain in version control (PRs #244, #245, #246 merged commits).

**Date:** 2026-06-08
**Triggered by:** request to start external comparisons and computations
**Substrate sources:**
- LMFDB newform 6.4.a.a (retrieved 2026-06-08)
- Pure-Python rational arithmetic (`scripts/verify/w6_cusp_action_verify.py`)

Class: external substrate verification / correction. Resolution-mode
throughout — no apparatus modification.

---

## 1. What was retrieved

### LMFDB newform 6.4.a.a (Hecke + Atkin-Lehner)
Full record at `scripts/verify/lmfdb_6_4_a_a_retrieved.md`. Headline:

| Quantity | LMFDB authoritative |
|---|---|
| a_17(f_{6,4}) | **−126** |
| a_19(f_{6,4}) | **+20** |
| (w_2, w_3) | **(+1, +1)** |
| Reduction type at p ∈ {2, 3} | **non-split multiplicative** |
| Root number ε | +1 |
| a_p for p ∈ {2, 3, 5, 7, 11, 13} | (−2, −3, 6, −16, 12, 38) |
| Weight, level, dim | 4, 6, 1 |
| Analytic rank | 0 |

### Pure-Python W_d cusp action
Script at `scripts/verify/w6_cusp_action_verify.py`; output:
- W_2: {∞ ↔ 1/3}, {0 ↔ 1/2} ✓
- W_3: {∞ ↔ 1/2}, {0 ↔ 1/3} ✓
- W_6: {∞ ↔ 0},   {1/2 ↔ 1/3} ✓
- W_2 · W_3 = W_6 composition: confirmed at matrix and cusp-action level

## 2. Overturned cached values

| Quantity | Cached (audit) | LMFDB / verified | PR affected |
|---|---|---|---|
| a_17 | −18 | **−126** | #244 |
| a_19 | −100 | **+20** | #244 |
| w_2 | −1 | **+1** | #245, #246 |
| w_3 | −1 | **+1** | #245, #246 |
| Steinberg type at 2, 3 | split mult. | **non-split mult.** | #245 |

## 3. Surgical corrections applied

Each affected audit doc updated in place with:
1. **Correction notice** at the top — names what was wrong, what's
   right, where the record lives, what survives, what shifts
2. **Inline value replacements** at every load-bearing claim site
3. **Falsifier status updates** — F-cusp-1 closed, F-W6-1 closed,
   F-W6-3 closed, F-pL-1 still open (requires p-adic numerical
   computation, not just retrieval)
4. **One-line summary** updated where it cited the wrong values

The audit *narratives* (the reasoning, the verdicts, the structural
readings) are preserved as written, with corrections targeted only at
the substrate-grounded numerical content.

### Which structural conclusions survive

**PR #244 (cuspidal λ_17):**
- ✓ Cuspidal λ_17 ≠ Eisenstein λ_17 (sign reversal and magnitude
  separation still present)
- ✓ Three-outcome empirical test framework (A/B/C) unchanged
- ✓ Lunar-theory parallel reading unchanged
- ↻ Magnitude ratio revised: 4914/126 = 39 (not 273×)
- ↻ Cuspidal value at the bound: 0.899 of Deligne (the corrected
  value saturates the bound far more tightly than −18 did, which
  *strengthens* the Sato-Tate-near-boundary reading)

**PR #245 (p-adic L-function):**
- ✓ Six-fold confluence at Mihailescu pair (i)–(vi) unchanged
- ✓ Mazur-Manin / Kubota-Leopoldt pairing as outcome resolution
  mechanism unchanged
- ✓ Steinberg-type reduction at both Mihailescu primes (still
  Steinberg-type, just non-split rather than split)
- ↻ MTT exceptional-zero claim **strengthens** (the corrected w_p =
  +1 is exactly the MTT condition for the forced zero; the original
  audit reached the same final claim via a sign-error path that
  should have given the opposite conclusion)
- ↻ Connection to PR #240 half-twist meta-structure **weakens**
  ((+1, +1) is the trivial Z_2 × Z_2 element, not a half-twist)

**PR #246 (W_6 invariance):**
- ✓ §2 W_d cusp action: externally confirmed (pure-Python)
- ✓ §3 Ω partition is W_6-symmetry-broken, all values on single orbit
- ✓ §3.1 Mihailescu/trivial cusp pairing: {1/2, 1/3} ↔ matter,
  {∞, 0} ↔ cosmology (depends only on cusp orbit structure, not on
  Hecke signs)
- ✓ §4 Stern-Brocot opposite-view characterization unchanged
- ↻ §3.2 cuspidal W_6-eigenvalue pattern revised: f_{6,4} is in the
  trivial (+,+) irrep (fully invariant), not "fixed by W_6 but
  flipped by W_2 and W_3" as originally written. The
  cuspidal/Eisenstein contrast survives but as "trivial-irrep vs
  full-orbit" rather than "different sign patterns"
- ↻ (O3) restated: cuspidal lives in one W_6-irrep entirely,
  Eisenstein spans the entire W_6-orbit — opposite *extremes* of
  W_6-symmetry rather than opposite *footings*

## 4. Verify-before-assert post-mortem

Per harmonics CLAUDE.md verify-before-assert protocol: a cache entry
must be re-read from substrate before being asserted at a load-
bearing resolution. Three of the audits in this chain (#244, #245,
#246) asserted Hecke eigenvalues and Atkin-Lehner signs at substrate-
fact resolution without performing substrate retrieval. The values
were cached from session memory of "what LMFDB 6.4.a.a says" — not
from any LMFDB call this session, and not from the harmonics
substrate (which doesn't carry LMFDB tables).

Three observed failure modes contributed:

1. **Confident recall ≠ retrieval.** The session had a strong sense
   that a_17 = −18, w_2 = w_3 = −1 were "well-known LMFDB values for
   6.4.a.a." That sense was confident *and wrong*. The internal
   Hecke-recursion checks passed (they only used a_2 and a_3, both
   correctly cached); the Deligne bound passed (|−18| < 140). Neither
   internal check could falsify the wrong value, because neither
   external check was performed.

2. **Steinberg-sign formula misapplied.** With a_p = −p for the
   Mihailescu primes (correctly cached), the *split-multiplicative*
   reading was asserted — but a_p = +p^((k−2)/2) is the split
   condition; a_p = −p^((k−2)/2) is non-split. The sign analysis was
   inverted at the formula-application step, propagating the wrong
   Atkin-Lehner signs (−1, −1) instead of (+1, +1).

3. **No verification script accompanied the audits.** PRs #244, #245
   could have shipped with a pure-Python LMFDB fetch or a static
   record file; #246 could have shipped with the cusp-action
   verifier. None did. The audits trusted their own internal
   coherence (Hecke recursion, Klein-four composition) as adequate
   proof.

What this changes going forward (no new substrate primitive; this is
a discipline observation):

- LMFDB-cached quantities used as load-bearing in an audit should
  ship with a retrieval-record file (`scripts/verify/lmfdb_*.md`)
  citing URL, date, and verbatim values
- Modular-arithmetic / group-action / matrix-composition checks
  should ship with a runnable verifier script when used as substrate-
  grounded evidence
- Steinberg-type-vs-Atkin-Lehner-sign relations: tabulate the
  sign convention explicitly before applying

## 5. Files in this correction

| Path | Purpose |
|---|---|
| `scripts/verify/lmfdb_6_4_a_a_retrieved.md` | LMFDB substrate retrieval record (this session, 2026-06-08) |
| `scripts/verify/w6_cusp_action_verify.py` | Pure-Python W_d cusp action verification (runnable) |
| `sync_cost/derivations/cuspidal_lambda17_weight4_audit.md` | PR #244 audit — corrected in place |
| `sync_cost/derivations/padic_lfunction_mihailescu_pair_f64_audit.md` | PR #245 audit — corrected in place |
| `sync_cost/derivations/gamma06_w6_invariance_opposite_view_audit.md` | PR #246 audit — corrected in place |
| `sync_cost/derivations/lmfdb_external_verify_correction_2026-06-08.md` | This document — correction overview |

## 6. Remaining gaps

Still open after this correction:
- **F-pL-1** (PR #245): explicit p-adic numerical computation of
  L_2(f_{6,4}) and L_3(f_{6,4}) L-invariants — requires SAGE / PARI
  (not yet available in this environment)
- **F-W6-2** (PR #246): cusp-to-Ω assignment in PR #242 — the
  structural mapping is unchanged; numerical realization via
  Eisenstein constant terms at each cusp remains a gap
- **F-W6-4** (PR #246): numerical W_d-eigenvalues of Eisenstein
  constant terms — same as F-W6-2, the W_d action restricted to the
  Eisenstein piece
- **task 117** (this session): cross-check cusp-Ω assignment via
  Eisenstein constants — pending; same gap as F-W6-2/4

The remaining gaps cluster on the Eisenstein side: the numerical
content of Eisenstein constant terms at the 4 cusps of Γ_0(6).
Closing these will require either SAGE/PARI or implementing the
q-expansion-at-each-cusp computation in pure Python (substantially
more involved than the W_d cusp action verifier).
