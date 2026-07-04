# F2 scoping — Klein → gauge continuum limit (Yang-Mills target)

## What this doc is — and what it is not

This is a **scoping articulation**, not a derivation attempt. It
converts the audit-at-#263 F2 item (tracked as epic issue #268)
from "conjectural — might be physics, might be coincidence" into
a tractable multi-PR program by:

1. Restating the target (Yang-Mills equations with structure
   constants matching SU(3)×SU(2)×U(1)).
2. Reading what the substrate already says about the starting
   point — including a substantive negative result on the
   frame-bundle approach that the audit's prose did not foreground.
3. Cataloging the remaining open possibilities and what closure
   or refutation would look like for each.
4. Listing techniques on the table, with bright lines on each.
5. Applying the Basepoint Principle discriminator — what would
   force a *decline* rather than a *derivation*.

It does **not** attempt the derivation, propose a specific
technique selection, or commit to a target outcome. Class 3
articulation; the work the doc enables happens in PR-2 onward.

## The target

Show that the XOR-filtered Stern-Brocot continuum limit on the
Klein bottle yields **Yang-Mills field equations** for a gauge
group whose structure constants match SU(3) × SU(2) × U(1) —
the Standard Model gauge content. If achieved, the framework's
charge-sector matches (q₂ = 2 ↔ SU(2), q₃ = 3 ↔ SU(3)) become
*forced* rather than coincidence.

Closure criterion: **structure constants match, not just structure**.
A derivation producing "some non-abelian gauge group" is not
enough; the specific group has to be SU(3)×SU(2)×U(1) and the
coupling constants have to fall out of the substrate at the right
ratios. Anything weaker is partial progress, not closure.

## The substrate-side starting point and what's already shown

`continuum_limits.md` Part I derives the K=1 limit of the
Stern-Brocot fixed-point equation, obtaining the **Einstein field
equations** via the ADM-Kuramoto dictionary. Lovelock's theorem
(D13) closes uniqueness: the only divergence-free rank-2 tensor
in 4D is `G_μν + Λg_μν`.

`xor_continuum_limit.md` takes the same continuum-limit machinery
to the Klein bottle's **XOR-filtered** Stern-Brocot tree. The
substrate read here (full doc, fresh) finds the question is no
longer entirely open — one approach is closed with a **negative
result**:

### What the substrate already establishes (xor_continuum_limit.md)

- The continuum Klein bottle has structure group `O(3)` (not
  `SO(3)`), and its pin cover is `Pin⁺(3) ≅ SU(2) × Z₂`.
- Lovelock still applies locally: Einstein equations are the
  unique output of the K=1 limit on the Klein bottle, same as on
  the torus.
- The Z₂ holonomy of the antiperiodic identification adds
  **topological boundary conditions** to the metric / connection
  / tensor fields, but does **not** produce new dynamical field
  equations.
- The XOR denominator-parity filter does **not** survive the
  continuum limit as smooth structure — it is a property of the
  discrete (finite-depth) description.

### What the substrate already rules out (negative result)

- The Klein bottle continuum limit does **NOT** produce SU(3) or
  Yang-Mills equations *from the frame bundle*.
- The SU(2) factor of `Pin⁺(3)` is the rotation/spin group, not
  the weak gauge group. The Z₂ is parity, not a gauge symmetry.
- The frame bundle of a 3-manifold is a gravitational structure;
  Standard Model gauge fields are connections on **separate
  principal bundles** with structure groups SU(3), SU(2), U(1).
  The frame-bundle reading does not access those bundles.

So the audit's "still conjectural" framing was overgeneral. The
**frame-bundle approach** to F2 is **already a documented
negative result** in the substrate; the F2 question reduces to
whether either of two specific open possibilities lands. The
"if it produces only Einstein, the matches are coincidence"
framing in `continuum_limits.md` Part III #5 prejudges the
outcome of those possibilities and should not be carried forward
unexamined.

## Open possibilities (with closure / refutation criteria)

> **Forward-pointing note (2026-07-03) — F2 was already resolved
> in the substrate at the time this doc was written**. This
> section's framing of A and B as "open possibilities" was inherited
> from audit #263's F2 flag (2026-06-16), which cited
> [[xor_continuum_limit]], [[continuum_limits]] Part III #5, and
> `engineering_targets.md`. Verified against those upstream sources,
> F2 read as open. Not verified against downstream substrate:
>
> - **D42 [[gauge_sector_lovelock]]** (dated 2026-04-07, revised
>   2026-04-13, **before the audit and before this scoping doc**)
>   derives Yang-Mills as the unique gauge dynamics consistent with
>   the Klein bottle's kinematic constraints, via Utiyama + Cartan.
>   Doc status: "Derived, with the wiring verified end-to-end."
>   This IS the Lovelock-analog for gauge that this scoping doc
>   flagged as "remaining." Not remaining.
> - **[[discrete_gauge_resolution]]** downstream-resolved the five
>   D21 sub-computations: Path 1 partially confirmed
>   (anomaly cancellation ✓ `anomaly_check.py` all 6 conditions;
>   Z_6 = Z_2 × Z_3 center ✓ `fiber_bundle.py`; confinement
>   asymmetry ✓ `xor_asymmetry.py` q=2 open / q=3 locked;
>   tongue overlaps abelian only; depth sweep no beta match).
>   Path 2 closed (`jacobian_v2.py`: 2×2 sl(2,R) block structure
>   encoding substrate geometry, not gauge algebra dim 11).
>
> The F2 epic (#268) and this scoping doc are substrate-freshness
> failures: both the audit and this doc verified upstream cites but
> not downstream resolutions. PR-2 (`f2_fm_beat_results.md`) and
> PR-3 (`f2_possibility_b_jacobian.md`) added complementary content
> — K=0 modal-claim confirmation with Kuramoto-pulling tolerance;
> F-agnostic dimension counting; approximate SU(2)-like near-
> degeneracy on the {B, D} endpoint mode pair broken at ~10⁻⁸
> (third-order Schwinger suppression, orthogonal to
> `jacobian_v2.py`'s sl(2,R) finding) — but did not deliver
> headline closure. Closure was in the substrate the whole time.
>
> Read the two-possibility structure below as historical
> articulation, not current work-front. F2 is derived; the epic
> closes as substrate-freshness-consolidation.

### Possibility A — "Discrete is physical"

(`xor_continuum_limit.md` §"Where the argument stands" reading 1.)

**Claim**: the Stern-Brocot tree at finite depth `d` (per D16,
`d ~ 19` Hubble cycles) **is** the physical configuration space,
not an approximation to a smooth manifold. The XOR constraint is
a physical selection rule at finite `d`. The denominator classes
`{2, 3}` are physical quantum numbers. The continuum limit is a
*mathematical convenience* that discards the physical structure
responsible for gauge symmetry.

**Closure criterion**: show that the finite tree reproduces gauge
theory predictions (cross-sections, anomaly cancellation,
coupling running) **without taking the continuum limit**. The
gauge structure is a property of the discrete configuration
space, not of any continuum limit.

**Refutation criterion**: show that finite-depth predictions
diverge from observation in a way that requires the continuum
description to close. (E.g., a finite-depth cross-section that
fails to reproduce a measured quantity that the continuum gauge
theory reproduces.)

**Why this would matter**: this is a **paradigm shift**, not a
gap closure. The framework would commit to "the universe is
discrete at depth `d`; gauge groups live in finite combinatorics,
not Lie algebras." The audit's "if Einstein only, matches are
coincidence" framing is wrong under this reading — the matches
are real but live in the discrete regime.

**Why this might fail**: anomaly cancellation in the SM uses
continuum Lie-algebra technology (Adler-Bell-Jackiw). Discrete
configurations would need an analog. The framework has done some
of this work (`anomaly_cancellation` is in the scorecard) — but
the connection to the discrete substrate is not articulated for
the gauge sector specifically.

### Possibility B — "Mean-field structure"

(`xor_continuum_limit.md` §"Where the argument stands" reading 2.)

**Claim**: gauge groups emerge from the **Kuramoto mean-field
functional `F[N]`** (D11, `rational_field_equation.md`) in the
continuum limit, **not** from the tangent bundle / frame bundle.
The XOR constraint on `F[N]` produces non-abelian structure
through the coupling between different denominator classes.

**Closure criterion**: show that the Jacobian of the field
equation at the 4-mode XOR-filtered fixed point produces
Yang-Mills equations with structure constants matching
SU(3)×SU(2)×U(1). The mean-field functional, not the frame
bundle, is the home of the gauge structure.

**Refutation criterion**: show that the Jacobian's structure
group is not SU(3)×SU(2)×U(1) — that the coupling-between-
denominator-classes either produces an abelian structure
(insufficient for non-abelian gauge), produces a non-abelian
structure with wrong constants, or fails to produce field
equations at all.

**Why this would matter**: this is the **headline F2 closure**.
A positive result here lands the framework's gauge-sector matches
as forced rather than coincidence and answers the audit's #263
high-leverage question affirmatively.

**Why this might fail**: the mean-field functional is a scalar
quantity (sum over modes); it is not obvious that its Jacobian
encodes the kind of structure-constant data Yang-Mills needs.
The XOR filter is a parity constraint, not a Lie algebra
ingredient. The technical work — Jacobian analysis at the 4-mode
fixed point in the continuum limit — has not been attempted on
the substrate as of this scoping read.

## Techniques on the table

Each technique has a bright line; not all are substrate-aligned.

1. **Kuramoto-ensemble averaging at the 4-mode XOR fixed point**
   (Possibility B's natural starting technique). Apply the same
   averaging procedure that gave the K=1 → Einstein limit (`continuum_limits.md` Part I)
   to the XOR-filtered substrate, but track the Jacobian rather
   than the ADM dictionary's scalar quantities. **Bright line**: if
   the averaging produces a scalar (rather than non-abelian-valued)
   coupling, Possibility B is refuted regardless of the structure
   constants that might appear in a more detailed analysis.

2. **RG flow on the XOR-filtered tree** (also Possibility B). The
   variance fixed point of the RG flow on the unfiltered Stern-Brocot
   tree gave ℏ form (`continuum_limits.md` Part II). The XOR
   filter changes the measure (44.4% of pairs survive at depth 6
   per `xor_continuum_limit.md` §3). Running the same RG analysis
   on the filtered measure could produce running couplings that
   match SM gauge running — or fail to. **Bright line**: this
   technique tests *running*, not *structure constants*; a positive
   result here is partial closure, not full closure.

3. **Lattice-to-continuum via discrete gauge theory** (Possibility A
   feeds this; could also feed Possibility B). Take the finite
   tree at depth `d` and construct a discrete gauge theory
   (Wilson-action style) on it. Either (A) the discrete theory is
   the physical theory and the continuum limit is unnecessary, or
   (B) the continuum limit of the discrete gauge theory recovers
   Yang-Mills. **Bright line**: the choice between A and B is not
   forced by the technique — it requires substrate-level commitment
   to one paradigm or the other.

4. **Direct Pin⁺(3) → SM structure** (would have been the
   natural extension of the frame-bundle approach). Now **closed
   as a starting technique** by the negative result above. Listed
   only to flag: do not re-attempt without a new substrate
   ingredient.

## Bright lines (Basepoint Principle discriminator)

The framework's Basepoint Principle (`basepoint_principle.md`)
says: a structural feature only counts as *declined* (rather than
*open*) if the obstruction is **exhibited**, not just suspected.

For F2, the discriminator applies to:

- **What would force a positive closure** — Yang-Mills equations
  derived from the substrate with structure constants forced
  (not fitted) to SU(3)×SU(2)×U(1). Anything short of this stays
  Class 3 articulation.

- **What would force an honest-null closure** — multiple
  substrate-aligned techniques (1, 2, 3 above) tried; each
  refuted with named obstruction; q₂/q₃ identifications stay
  Class 3 (structural coincidence within the framework's
  combinatorial substrate, but not derived as forced).

- **What would force a discriminator-decline** — show that gauge
  structure necessarily requires an **observational anchor**
  parallel to the two-anchor minimum's disposition in
  `anchor_count_reaudit.md`. This would be a *structural feature*,
  not a derivation gap — the gauge group is sayable but not
  derivable from substrate primitives alone. Bright line: such a
  decline must come with the same kind of obstruction inventory
  the anchor count carries (five named obstructions), not as a
  fallback when techniques 1–3 fail.

## Class assignment

This doc is **Class 3 articulation** — no new derivation, no new
prediction. It restructures the F2 open question by foregrounding
substrate state that the audit summary did not (the frame-bundle
negative result), and lays out the two-possibility decision the
work in PR-2+ must navigate.

## What success / failure looks like (downstream)

A **positive F2 closure** updates:
- `framework_status.md` Survives ledger — new entry for the
  XOR-filtered continuum limit → Yang-Mills derivation
- `MANIFEST.yml::scorecard::gauge_group::closure_status` — promote
  from "Class 5 (exact) — SU(3)×SU(2)×U(1) from Klein-bottle
  mode lattice Z₆ = Z₂ × Z₃" to a Class 5 grounding that
  references the continuum-limit derivation, not just the
  combinatorial identification
- `xor_continuum_limit.md` §"Where the argument stands" — update
  the two-possibilities framing to "Possibility B closed"

An **honest-null F2 closure** updates:
- New negative-result doc (e.g. `f2_mean_field_jacobian_null.md`)
  with named obstruction
- `framework_status.md` — add an entry to "Eliminated" or to a
  new section flagging q₂/q₃ ↔ SU(2)/SU(3) as Class 3 articulation,
  not forced
- The framework's gauge-sector public statement (README L92-105
  "Three generations and SU(3) × SU(2) × U(1)") may need a
  forward-pointing note that the **combinatorial identification**
  (Z₆ = Z₂ × Z₃) stands; only the **continuum-limit derivation**
  fails

A **discriminator-decline** updates:
- New doc articulating the obstruction (parallel to
  `anchor_count_reaudit.md` for the gauge sector)
- `basepoint_principle.md` — add the gauge-structure decline as
  an 8th/9th instance

## Cross-references

| File | Role |
|---|---|
| `continuum_limits.md` Part I | K=1 → Einstein derivation (the parallel technique that succeeded) |
| `continuum_limits.md` Part III #5 | The audit's F2 framing — "if not gauge structure, matches are coincidence" |
| `xor_continuum_limit.md` | The substrate's existing frame-bundle attempt with negative result + two-possibility framing |
| `rational_field_equation.md` (D11) | The mean-field functional F[N] central to Possibility B |
| `klein_bottle.md` / `klein_bottle_derivation.md` | The Klein-bottle structure the XOR filter implements |
| `gauge_factorization.md` | The combinatorial Z₆ = Z₂ × Z₃ identification that F2 either lifts to forced or leaves as Class 3 |
| `basepoint_principle.md` | The discriminator framework for declined-vs-open |
| `anchor_count_reaudit.md` | Template for a discriminator-decline closure |
| `engineering_targets.md` | Benchtop validation of D18/D19; orthogonal to F2's derivation question but confirms the discrete-substrate side is physically realizable (relevant to Possibility A) |
| `framework_status.md` | Where positive / null F2 results would update |
| `MANIFEST.yml::scorecard::gauge_group` | Where positive F2 closure would refine the existing Class 5 grounding |

## Status

**Class 3 articulation; superseded by
[[gauge_sector_lovelock]] (D42, Yang-Mills derived) and
[[discrete_gauge_resolution]] (five sub-computations resolved),
both landed in April 2026 — before this doc and before the
audit that triggered it.** This doc's original framing
(F2 as two open possibilities, four candidate techniques with
bright lines) was Class 3 preparatory articulation at ship
(2026-06-28). Subsequent substrate archaeology (2026-07-03)
revealed that both docs above had already resolved F2 in April
2026.

**Substrate-freshness failure chain.** Audit #263 (2026-06-16)
flagged F2 as "conjectural" citing `continuum_limits.md` Part III
#5, `xor_continuum_limit.md`, and `engineering_targets.md`.
Those upstream sources do read F2 as open, and the audit noted
"all sources verified against the substrate at audit time." But
downstream resolutions (D42, `discrete_gauge_resolution.md`)
were not consulted. This scoping doc inherited the audit's flag
without independently verifying downstream substrate state — the
same failure mode compounded. Both failures are documented in
[[canonical_glossary]] §8 vocabulary as **substrate-freshness
failure**: upstream cites verified, downstream resolutions
missed. This audit-hygiene gap may warrant framework-level
attention independent of F2 itself.

Side: substrate-side, scoping / articulation only.
Class: preparatory (no closure claimed); superseded by D42 and
`discrete_gauge_resolution.md`.
Downstream: F2 epic (#268) closes with consolidation note;
D42 already delivers the Lovelock-analog uniqueness theorem the
scoping doc identified as "remaining" — the same theorem, derived
2+ months before this doc was written.
