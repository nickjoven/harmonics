# Direction 4 Phase C — what remains for Class 5 closure

## What this file is

Inventory of what's actually open after Phase B for the w_+ = 13/14
closure. Per `psl2z_subgroup_phase_b.md`, B3 (representative
selection within cusp 1/2 of Γ_0(6)) is the single open item. This
audit reduces B3 to a sharper sub-question and identifies whether
recognize-mode closure is available.

**Headline result of the audit**: Phase C reduces to a single open
question (matter-sector Farey-depth derivation). The other two
sub-arguments close in recognize mode.

## The reduction chain

**Goal**: derive w_+ = 13/14 as the unique cusp-1/2 representative.

### Sub-argument 1 — Cusp-1/2 ground state = (q-1)/q (closes recognize-mode candidate)

Within cusp 1/2 of Γ_0(6) (orbit elements p/q with gcd(q, 6) = 2),
the orbit's "ground state" under the substrate's max-locking
energy functional is the representative closest to 1 — i.e.,
**p = q − 1** (largest numerator coprime to q in (0, q)).

**Physical reading**: the sym Klein-singlet boundary mode wants to
lock fully (w → 1) under matter-sector EM coupling; cusp-1/2
quantization restricts to discrete values {1/q, 3/q, ..., (q-1)/q}
(coprime), so the closest-to-1 representative is the lowest-energy
state.

**Status**: recognize-mode candidate. The "max locking subject to
discrete quantization" rule is a substrate-energy claim that
follows from the framework's existing K < 1 ⟹ substrate is
discrete result (`denomination_boundary.md` §134). Discrete
quantization at cusp-1/2 produces the orbit grain; the substrate's
energy minimum within the grain is the closest-to-1 representative.
This needs articulation but the structural content exists.

### Sub-argument 2 — q = 14 = q_2·|F_4| (open; reduces to deeper open)

Given Sub-argument 1, w_+ = (q-1)/q. For w_+ = 13/14, **q = 14**.

The denominator q in cusp 1/2 is constrained to q ∈ {2, 4, 8, 10,
14, 16, 20, ...} (multiples of 2 coprime to 3). Framework-natural
options:

| q | Framework reading | w_+ predicted | rel.err vs 0.9298 |
|---|---|---|---|
| 2 | q_2 | 1/2 | 46% — FAILS |
| 4 | q_2² | 3/4 | 19% — FAILS |
| 8 | K_QUARK | 7/8 | 5.9% — FAILS |
| 10 | q_2·MEDIANT | 9/10 | 3.2% — close-but-not-1% |
| **14** | **q_2·\|F_4\|** | **13/14** | **0.13% — match** |
| 16 | q_2⁴ | 15/16 | 0.83% |
| 22 | q_2·\|F_5\| | 21/22 | 2.7% |
| 26 | q_2·\|F_6\| | 25/26 | 3.4% |

The framework integers q = 14 = q_2·|F_4| matches observation to
0.13%; alternatives within 5% are q = 16 (q_2⁴, 0.83%) and q = 10
(q_2·MEDIANT, 3.2%). q = 14 is the unique sub-1% candidate.

**Status**: this reduces to "why the matter-sector denominator is
q_2·|F_4| specifically." Per `partition_logit_form.md`, the Ω_DM
logit denominator is exactly q_2·|F_4| = 14. The Phase C question
inherits this: why does the matter sector have q_3-quantity |F_4|
= 7 = (Farey count at depth 4)?

This is the **same** open question flagged in `partition_logit_form.md`
§"Implications" follow-on #2: identify the q_3-sector quantity
pattern (3, 7, 9 for the three sectors). Direction 4 Phase C
inherits this open question; it doesn't introduce a new one.

### Sub-argument 3 — Multi-candidate-14 ansatz check

The integer 14 has multiple framework-integer expressions
(audited in `psl2z_subgroup_phase_c_audit.py`):

```
q_2·|F_4|, |F_7|-MEDIANT, 2·|F_4|, q_3+|F_5|,
K_QUARK+INTERACT, K_LEPTON+MEDIANT, |F_6|+1, INTERACT+K_QUARK
```

Per Region C Phase B (`numerology_count_phase_b.md`), framework-
integer expression density is high enough that 14 having multiple
representations is pigeonhole — NOT structural multiplicity. The
forcing argument must come from one specific framework derivation
that uses q_2·|F_4| AS THE matter-sector Farey count, not from
"14 has many framework integer expressions."

The framework's specific use of q_2·|F_4| = 14 in the Ω partition
(`partition_logit_form.md` Ω_DM logit denominator) IS that
specific derivation. Sub-argument 2's reduction to "matter sector
Farey depth = 4" is the actual structural question, not the
auxiliary multi-candidate-14 issue.

## Closure status after Phase C inventory

| Sub-question | Status | Reduction path |
|---|---|---|
| Cusp 1/2 ground state = (q-1)/q | Recognize-mode candidate | Articulate "max locking subject to discrete quantization" from `denomination_boundary.md` |
| Denominator q = 14 | Recognize-mode for "= q_2·|F_4|"; **structural for "|F_4| = 7"** | Inherit `partition_logit_form.md` §implications follow-on #2 |
| Multi-candidate 14 readings are pigeonhole | Confirmed (Region C) | Not the actual question |

**Net**: Direction 4 Phase C reduces to ONE open question: derive
the q_3-sector quantity pattern (|F_4| = 7 for matter, q_3 = 3 for
DE, q_3² = 9 for baryon). This is **the same open question already
flagged** in `partition_logit_form.md`. Direction 4's Phase C does
not introduce new open structure beyond what's already on the
framework's open list.

## Reframing: Phase C is not its own open item

The honest landing: **Direction 4 Phase C is not a separate
multi-session open question**. It's the same question as
`partition_logit_form.md` follow-on #2 (the q_3-sector quantity
pattern). The framework had ONE open question all along, but it
appeared at three places:

1. `partition_logit_form.md` follow-on #2: "Identify the
   q_3-sector quantity pattern (3, 7, 9)"
2. `omega_b_w_plus_candidate.md`: "Why 13/14 specifically over
   12/13 or 14/15?"
3. `psl2z_subgroup_phase_b.md` B3: "Why this representative
   within cusp 1/2?"

All three are the same open question, surfaced via different
vocabularies. Closing the q_3-sector quantity pattern derivation
closes ALL THREE simultaneously.

This is a **vocabulary-is-the-work pattern Instance 10 candidate**:
"three apparent open questions are a single underlying open
question expressed in different framework vocabularies."

## What this changes about the open list

`framework_status.md` "currently active" derivations:

**Pre-this-inventory**: Direction 4 Phase C is an open multi-
session item.

**Post-this-inventory**: Direction 4 Phase C IS the q_3-sector
quantity pattern question; it doesn't need a separate slot. The
framework's open list compresses by one item.

The actual single open question for Class 5 closure of w_+ = 13/14
is now sharply named: **"Why does the framework's q_3-sector
quantity pattern give |F_4| = 7 for matter, q_3 = 3 for DE,
q_3² = 9 for baryon?"** This is the deepest open structural
question after the 2026-04 closure round.

## What's needed to close it

A derivation that produces (3, 7, 9) as the q_3-sector quantities
of the three cosmological sectors from the substrate's existing
Z_6 = q_2 × q_3 mode decomposition. Candidate angle:

- Each sector's "q_3-quantity" should be the count of q_3-sector
  modes accessible to that sector's coupling
- Λ sector (DE): couples to q_3 (color triplet), one mode → 3
- DM sector: couples to |F_4| modes (Farey depth 4 = ?) → 7
- Baryon sector: couples to K_LEPTON (lepton triplet sub-modes)
  → 9 = q_3²

The Λ and baryon readings are framework-structural (q_3 and
K_LEPTON = q_3² are existing primitives). The DM reading uses
|F_4| = 7 which doesn't directly correspond to a known coupling
sector. Closing this requires identifying what sector |F_4|
counts.

This is genuinely substantive structural work — not recognize-
mode close-able in a single session. But it's a SHARP question
now, not a diffuse "derive w_+ from substrate dynamics."

## Cross-references

- `psl2z_subgroup_phase_b.md` B3 — the open item this inventory
  reduces
- `psl2z_subgroup_phase_c_audit.py` — orbit + selection-rule audit
- `partition_logit_form.md` — q_2 × q_3-sector factorization;
  follow-on #2 = the same question
- `omega_b_w_plus_candidate.md` — w_+ = 13/14 candidate
- `denomination_boundary.md` §134 — discrete substrate at K < 1
  (Sub-argument 1 source)
- `baryon_fraction.md` — sector mode counts
- `numerology_count_phase_b.md` — Region C verdict (multi-candidate
  14 readings are pigeonhole, confirms Sub-argument 3)
- `vocabulary_is_the_work_pattern.md` — Instance 10 candidate
  (three open questions = one open question)

## Status

Direction 4 Phase C inventoried. **Reduces to the q_3-sector
quantity pattern question** already flagged in
`partition_logit_form.md`. No new open structure introduced.

The framework's actual open list compresses: w_+ closure to
Class 5 depends on the same open derivation as the partition
logit form's q_3-sector pattern, not a separate item.

**Vocabulary-is-the-work Instance 10 candidate**: Phase C, w_+
candidate selection, and the q_3-sector pattern question are
three vocabularies for one underlying open structural question.
