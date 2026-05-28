# Lesson — 8/35 vs 13/19: telling a derivation from a coincidence

## What this is

A one-hour worked lesson. Two small-integer rationals, each matching
a measured dimensionless number to ~1% or better. One is the
framework's prized survivor (Class 5, **Survives**); the other is
filed under **Fails**. The lesson teaches the framework's keystone
discipline — *forced, not fitted* — by auditing both side by side.

The point is not the two numbers. The point is the **discriminator**:
the set of questions that separates structural signal from numerical
coincidence. Anyone can produce small-integer near-matches (a crowded
field guarantees them — see the pigeonhole result below). What makes
this framework *not* numerology is the discipline that throws out the
hits which don't survive audit — including its own prettiest one.

**Prerequisites** (from the minimum concept set): mode-locking and
"simpler ratio = stronger lock," the mediant/Farey structure, the
parabola threshold, and the habit of asking "forced or fitted?".

---

## Segment 1 — The two suspects (≈10 min)

Put both on the board, cold, with no framing:

| Candidate | Value | Measured | Gap | What it is |
|---|---|---|---|---|
| **8/35** | 0.2286 | `sin²θ_W ≈ 0.231` | ~1% | electroweak mixing angle — a famous SM parameter |
| **13/19** | 0.6842 | `Ω_Λ ≈ 0.6847` | 0.07σ | dark-energy fraction of the universe |

Ask the room: *which one is real?*

Most will pick **8/35** — it's the weak mixing angle, it *feels* more
fundamental than "just" a cosmology ratio. Hold that vote. The
framework's verdict is the reverse, and the hour is about why.

---

## Segment 2 — Board derivation A: 8/35 (≈12 min)

(Source: `figure_eight.md` "The branching ratio".)

The Klein-bottle substrate's figure-8 has two competing sectors:
Loop 1 = sector (2,3) with denominator `q = 3`; Loop 2 = sector (3,2)
with `q = 2`. The mixing angle is *the fraction of crossing-traffic
the weaker sector grabs* — a ratio of two mode-locking strengths,
weighted by the duty cycle `φ(q)/q²` (Euler totient over denominator
squared; `φ(2)=1`, `φ(3)=2`):

```
            φ(3)/3²            2/9            2/9
 raw  =  ───────────────  =  ─────────  =  ────────  =  8/17
         φ(2)/2² + φ(3)/3²   1/4 + 2/9      17/36

 double-cover correction (figure-8 has two sheets at the crossing):
            8 / (17 + 18)  =  8/35  =  0.2286
```

It uses only mode-locking (tongue widths) + simple fractions. It
*feels* completely framework-native. Note that for the room.

---

## Segment 3 — Board derivation B: 13/19 (≈12 min)

(Sources: `farey_partition.md`, `omega_partition_combinatorial.md`.)

The minimum self-predicting resolution on the Klein quotient is the
Farey set `F₆` — every fraction `p/q ∈ [0,1]` with `q ≤ 6`:

```
 0/1, 1/6, 1/5, 1/4, 1/3, 2/5, 1/2, 3/5, 2/3, 3/4, 4/5, 5/6, 1/1
```

Count them: `|F₆| = 1 + Σ_{k=1}^{6} φ(k) = 1 + (1+1+2+2+4+2) = 13`.
Exactly thirteen — not a choice, a count.

Partition these by structural role on the Klein quotient
(Klein-singlet ∩ coprime-to-6 selection): `Ω_Λ : Ω_DM : Ω_b = 13 : 5 : 1`,
total `19`. So

```
 Ω_Λ = 13/19 = 0.6842      (Planck: 0.6847 ± 0.0073  →  0.07σ)
```

It also uses only counting + the mediant/Farey structure. It feels
*exactly as* framework-native as 8/35. By eye, the two derivations
are siblings. That is the trap the audit springs.

---

## Segment 4 — The five-question audit (≈20 min)

Run the discriminator on each. These five questions *are* the
framework's method (`ansatz_audit_policy.md`).

| # | Question | **8/35** (sin²θ_W) | **13/19** (Ω_Λ) |
|---|---|---|---|
| 1 | **Does the target run?** | **Yes — fatal.** `sin²θ_W` flows with energy (RG running): ≈0.231 at `M_Z`, ≈0.239 at low energy. A *fixed* rational has no scale at which it is "the" value, and the framework supplies no mechanism to pick `M_Z`. | No. A scale-free ratio of mode counts; nothing to run. |
| 2 | **Forced, or selected from a menu?** | **Selected.** Many framework-integer expressions land near 0.23 — the 1–3% near-match cloud is *statistically consistent with a permutation (pigeonhole) null* (`numerology_count_phase_b.md`: ~1–1.7σ over-density, "not significant individually; cloud is noise"). | **Forced.** Counting gives *exactly* 13 fractions at `F₆`. No menu — change the rule and you change the count, not the value. |
| 3 | **What breaks if you perturb it?** | Nothing structural — 8/34 or 9/35 sit about as close to 0.23. Re-description, not constraint. | The **count** breaks. `F₆` has 13 elements; 12 or 14 is simply the wrong Farey set. Rigid. |
| 4 | **Independent corroboration?** | One route (the figure-8 duty cycle). | **Overdetermined.** Farey count, *and* the logit form (complements 6,14,18 = `q₂·{q₃, |F₄|, q₃²}` = 2·{3,7,9}; `partition_logit_form.md`), *and* PSL(2,ℤ) cusp structure, *and* ties to `R = 6·13⁵⁴` and `Λ·ℓ_P²`. |
| 5 | **Survives the automated check?** | **No.** `sinW_running_check.py` → **Fails** (`framework_status.md:116`). | **Yes.** Passes Z1–Z3; **Survives** (`framework_status.md:24-25`). |

**Score: 0-for-5 vs 5-for-5.** Two derivations that looked like
siblings on the board come apart completely under the audit, even
though the naive "~1% hit" was the same — better, if anything, for
the particle-physics one.

---

## Segment 5 — The verdict and the inversion (≈6 min)

The framework files **8/35 under Fails** and **13/19 under Survives**.
It executes its own prettiest particle-physics hit and keeps a
"mere cosmology" ratio.

The lesson students usually have backwards:

> **Rejecting 8/35 is what *certifies* 13/19.**

A framework that kept *both* near-matches would be numerology — it
would be harvesting pigeonhole hits. A framework that *kills* 8/35,
using the same machine that produced 13/19, has demonstrated the
machine has a working discriminator. The willingness to throw out a
1% hit on a famous constant is the evidence that the surviving
results were not cherry-picked. **The discriminator is the
framework**; 8/35 is the sacrifice that makes 13/19 credible.

This is the keystone concept ("forced, not fitted") taught not as a
slogan but as an execution — the framework auditing, and convicting,
itself.

---

## Instructor notes

- **Order is the pedagogy.** Present 8/35 first and let it *win* the
  room's vote. Derive both before auditing either, so they look like
  siblings. Spring the audit only after both are on the board. The
  expectation-reversal (the expert's prized result gets killed) is
  the memory hook.
- **This is the capstone** of the minimum concept set: it is
  concept #6 ("forced, not fitted") as a worked example, with
  mode-locking (#4) and the mediant/Farey structure as the supporting
  cast already taught earlier.
- **Lab tie-in.** Both numbers trace to the small-denominator
  hierarchy a string player feels in their fingers (touch harmonics:
  the reduced denominator of the touch point is the harmonic you
  hear). One survives the nonlinear audit; one does not. Same
  hierarchy, different verdict.
- **The general takeaway**, transferable beyond this framework:
  small-integer near-matches are cheap (pigeonhole guarantees them);
  the only thing that distinguishes signal is a discriminator you are
  willing to let *fail your own results*.

---

## Sources

- `framework_status.md:116` — `sin²θ_W = 8/35` under **Fails**
  (`sinW_running_check.py`, SM running rules out Planck-scale origin).
- `framework_status.md:24-25` — `Ω_Λ = 13/19` (0.07σ) under
  **Survives** (Farey + Z₂ rep theory).
- `figure_eight.md` "The branching ratio" — the 8/35 duty-cycle
  derivation (preserved as a structural-argument record; its
  numerical match is coincidence, per the doc's own disposition note).
- `farey_partition.md`, `omega_partition_combinatorial.md` — the
  13/19 Farey-`F₆` counting and partition.
- `partition_logit_form.md` — the logit corroboration
  (6,14,18 = `q₂·{q₃, |F₄|, q₃²}`).
- `numerology_count_phase_b.md` — the pigeonhole result (the 1–3%
  near-match cloud is statistically consistent with a permutation
  null; "cloud is noise").
- `ansatz_audit_policy.md:58` — the discriminator's Class-4 → Class-2
  default ("if the audit can't produce a forcing mechanism within one
  sitting").
- `numerology_inventory.md`, `statistical_conventions.md` — the
  Class 1–5 / Z1–Z3 definitions the audit applies.

## One-line summary

Two ~1% rational hits — `sin²θ_W = 8/35` and `Ω_Λ = 13/19` — derived
the same way on the board, come apart 0-for-5 vs 5-for-5 under the
five-question audit; the framework kills 8/35 (it runs; it's
pigeonhole) and keeps 13/19 (forced count, overdetermined), and the
willingness to kill the prettier one is exactly what certifies the
survivor.
