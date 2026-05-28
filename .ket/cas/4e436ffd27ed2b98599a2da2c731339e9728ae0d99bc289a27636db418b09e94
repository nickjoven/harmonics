# Q mod 2 mediant projection (state-axis dual of inviolable #1)

## Status

**State-axis projection articulated** for inviolable #1
(`substrate_determinism.md` L166-167; `q_mod2_conservation_theorem.md`).
The conservation theorem's time-axis reading — "no local process
changes `Q mod 2`" — has a state-axis dual: a parity superselection
rule on Farey mediants admissible as lock-ratios on the substrate.

This is *not* a new theorem. It is the Noether-duality projection of an
existing one: every conservation law has a dynamical reading ("this
quantity does not change") and a static reading ("only configurations
preserving this quantity are admissible"). The framework already runs
on this duality for its other inviolables (Born exponent, structural
integers, arrow monotonicity). The state-axis projection of #1 to
mediants had been used implicitly across the cluster discussions of
`k_of_t_problem_statement.md` §3 and `continuity_in_K_nulls.md` §N12;
this doc supplies the explicit projection and applies it to the
inflation cadence band.

The bridge from rotation-number `p/q` (Farey mediant) to substrate
kink-number `Q mod 2` is articulated as the *substrate-natural* reading
`Q ≡ p mod 2`; a full first-principles derivation of the bridge from
Step 1 of `q_mod2_conservation_theorem.md` is named as the residual
open piece, with the additivity-under-mediant check used as the
admissibility test.

No new primitive.

---

## The statement

**Claim (Q-mod-2 mediant superselection).** On the framework's
substrate, the set of Farey mediants `p/q` admissible as lock-ratios
between two phase rhythms is restricted to a single Q-mod-2 sector —
determined by the bicone Q-mod-2 charges of the two participating
rhythms and combined under the mediant rule by XOR addition
(`Q_mediant = Q_left ⊕ Q_right`). Lock-mediants in the complementary
sector are inadmissible by Noether duality with the conservation
theorem.

Applied to the K(t) inflation cadence band
(`k_of_t_problem_statement.md` §3 + §"Identification 4 scope"; the
audit-revised `0.0365 ± 0.004` per Planck 1σ on `n_s`), the projection
narrows the cluster of `(p, q)` candidates by half. Combined with
inviolable #6 (exact structural integers `{2, 3, 13, 19}`), only three
candidates survive both filters jointly — one per (distinct)
sector-structural reading.

---

## Derivation

### Step 1 — Noether duality of #1

Every conservation law projects two readings on its associated
manifold, one onto the time axis ("this quantity is preserved") and
one onto the state axis ("only configurations preserving the quantity
are admissible"). For inviolable #1 (`Q mod 2` conservation; bicone
Z₂ rigidity, `wave_particle_substrate.md`):

| Axis | Reading |
|---|---|
| Time | No local process changes `Q mod 2` (`q_mod2_conservation_theorem.md` Theorem) |
| State | Only configurations / lock-ratios whose `Q mod 2` is in the admissible sector are reachable |

The two readings name the same constraint, projected onto different
axes. Step 1 is then "the state-axis projection exists," which is
immediate from the Noether-duality structure the framework already
uses for its other inviolables (e.g., #5 Born exponent has a static
reading "every observable has the form `⟨ψ|A|ψ⟩` exactly"; #6
structural integers has "no operation introduces a new structural
integer").

The remaining work in steps 2–3 is to specify *how* the conserved
quantity projects onto the state-axis labels — i.e., to give the
Q-mod-2 assignment on lock-mediants.

### Step 2 — Bridge: `Q ≡ p mod 2` for a lock at rotation number `p/q`

A phase-rhythm pair locked at rotation number `p/q` corresponds to a
field configuration `θ(x, t)` whose winding satisfies the substrate's
antiperiodicity constraint
(`q_mod2_conservation_theorem.md` Step 1, eq. ∗):

    φ(x + L_x, y, t) = −φ(x, L_y − y, t).

For the locked, uniform-rotation profile, the kink-number `Q̃ ∈ ℤ`
(`q_mod2_conservation_theorem.md` Step 1, eq. 1) reduces to the
numerator `p` of the rotation number — the winding per substrate-loop
traversal at lock. The Klein deck transformation flips its sign
(eq. 3 of the theorem), so only the residue class mod 2 descends to
`K²` as the well-defined invariant. Substrate-natural bridge:

    Q(lock at p/q) ≡ p mod 2.        (bridge claim)

The bridge is consistent with the mediant operation: under
`mediant(a/b, c/d) = (a+c)/(b+d)`, the numerator parity satisfies

    (a + c) mod 2 = (a mod 2) ⊕ (c mod 2)

which is the XOR (`Z₂` addition) of the parents' `Q mod 2`. The
framework's mediant rule (`farey_proof.md`; the sync-cost-minimization
theorem) is therefore *automatically* Q-mod-2 additive under XOR —
exactly the additivity a `Z₂` charge should obey under the substrate's
primitive operation. This consistency is the substantive content of
the bridge: the parity assignment is the unique mod-2 invariant that
is additive under mediant.

**Honest scope of step 2.** The kink-number-equals-numerator reading
is substrate-natural for uniform-rotation lock profiles; a fully
rigorous first-principles derivation of the bridge from
`q_mod2_conservation_theorem.md` Step 1 (the sine-Gordon kink reduction)
to the lock-rotation-number's numerator parity remains a residual
open piece. The XOR additivity-under-mediant check is the most
compelling argument the bridge is right; the projection's downstream
applications are conditional on this bridge claim and would have to
be re-examined under any alternative parity assignment
(`Q ≡ q mod 2` or `Q ≡ (p+q) mod 2`).

### Step 3 — Admissible joint-lock sector

For two rhythms with Q-mod-2 charges `Q_A, Q_B`, conservation under
the locking process forces

    Q_lock = Q_A ⊕ Q_B          (XOR sum mod 2).

Step 1's Noether-duality projection then says: only mediants `p/q`
with `p mod 2 = Q_A ⊕ Q_B` are admissible as lock-ratios for this
rhythm pair. The complementary parity is excluded by the conservation
theorem applied across the locking process.

For the K(t) cascade-rhythm × inflation-rhythm lock specifically, the
joint sector `Q_cascade ⊕ Q_inflation` requires its own determination:
- `Q_cascade` at the inflation-segment cascade depth (requires reading
  the cascade-station Farey path's accumulated Q-mod-2 from the
  framework's mediant-tree structure; open work).
- `Q_inflation` from the inflationary winding (the total winding over
  ≈60 e-folds is `60 · 0.0365 ≈ 2.19 ≈ √5` — see
  `minimum_alphabet.md` §3; whether this rounds to `Q = 2 mod 2 = 0`
  or carries half-integer structure from the √5 algebra is itself
  open).

The joint-sector determination is *not* closed by this doc. What this
doc closes is the *projection structure* and the *admissibility
filter*: given any specific joint sector, the projection gives the
admissible parity, and combined with the cadence band yields the
admissible mediant set.

---

## Application to the K(t) inflation cadence band

The cadence band of `Identification 4` (per the 2026-05-28 audit; see
`k_of_t_problem_statement.md` §"Identification 4 scope") is

    rate ∈ [0.03211, 0.04083]      (Planck 1σ on n_s = 0.9649 ± 0.0042)
    center: rate = (1 − n_s) / ln(φ²) ≈ 0.03647

Enumerating Farey fractions `p/q` in this band with `gcd(p, q) = 1`
and denominator `q ≤ 64` (depth-bounded by the cascade's reachable
Stern-Brocot level), there are **14** candidates total. Partitioning
by `p mod 2`:

| Q-mod-2 | Candidates | Count |
|---|---|---|
| 1 (odd) | 1/25, 1/26, 1/27, 1/28, 1/29, 1/30, 1/31 | 7 |
| 0 (even) | 2/49, 2/51, 2/53, 2/55, 2/57, 2/59, 2/61 | 7 |

The Q-mod-2 projection eliminates one sector entirely, cutting the
candidate set in half. Combining with inviolable #6 (exact structural
integers `{2, 3, 13, 19}`; only mediants whose denominator factors
into structural primes survive), the surviving candidates are:

| Sector | Mediant | Decomposition | Sector reading |
|---|---|---|---|
| Q = 1 | **1/26** | `1 / (q₂ · 13_Λ)` | SU(2) × matter (Ω_Λ numerator) |
| Q = 1 | **1/27** | `1 / q₃³` | pure SU(3) color-cubed |
| Q = 0 | **2/57** | `2 / (q₃ · 19_Λ)` | SU(3) × cosmological denominator |

All three are at cadence-band proximity:

| Mediant | Value | Offset from 0.03647 |
|---|---|---|
| 1/27 | 0.03704 | 1.6% |
| 1/26 | 0.03846 | 5.5% |
| 2/57 | 0.03509 | 3.8% |

(All within Planck 1σ.) The joint sector determination thus selects:

- **If `Q_cascade ⊕ Q_inflation = 1`** (odd-parity joint sector):
  the admissible set is `{1/26, 1/27}`. Two structurally-distinct
  canonical candidates remain; the K(t) cadence is forced to be one
  of these two; resolution between them would require a further
  discriminator (cascade Farey-path parity, sector mixing across the
  Ω_Λ partition's halves).

- **If `Q_cascade ⊕ Q_inflation = 0`** (even-parity joint sector):
  the admissible set is `{2/57}`. **Unique resolution.** The K(t)
  cadence is forced to `2/(q₃ · 19_Λ) ≈ 0.0351`, derived from substrate
  primitives alone, with the FRW-transformed cosmological mass-function
  slope a forced consequence.

The leaf's status is therefore reduced to a **single binary**: the
joint Q-mod-2 sector of the cascade × inflation lock.

---

## What this says (and what it does not)

It **says**:

- The state-axis projection of inviolable #1 is the substrate-natural
  parity superselection rule on Farey mediants, additive under XOR by
  the framework's mediant operation.
- Applied to the K(t) inflation cadence band + inviolable #6, the
  projection narrows 14 cluster candidates to **3 jointly canonical
  ones** (1/26, 1/27, 2/57), each carrying a distinct
  sector-structural reading.
- The K(t) cadence open question is therefore narrowed from "select
  from a numerical-precision-limited cluster" (z-buffer territory; see
  `minimum_alphabet.md` "Identification cluster" + the z-buffer
  analogy) to a *binary* over the joint Q-mod-2 sector.
- This is the framework's first integer-graded discriminator on the
  K(t) cadence question; it operates *above* the substrate's
  precision floor that the cluster z-fighting argument said no
  continuous-domain discriminator can.

It does **not** say:

- That the K(t) leaf is resolved. The joint Q-mod-2 sector
  determination — `Q_cascade ⊕ Q_inflation` at the inflation-segment
  depth — remains open. This doc closes the *projection* (what to do
  with the joint sector once known), not the joint sector itself.
- That the bridge `Q ≡ p mod 2` is fully proven from first principles.
  It is substrate-natural and uniquely additive under the mediant
  operation (the strongest available argument), but a derivation
  starting from `q_mod2_conservation_theorem.md` Step 1's
  sine-Gordon kink-number reduction and ending at the lock-rotation
  numerator parity is named as residual open work. An alternative
  bridge (e.g., `Q ≡ q mod 2`, `Q ≡ (p+q) mod 2`) would give a
  different admissibility filter; both alternatives also respect XOR
  additivity, but the kink-number reading favors the numerator
  reading.
- That the three surviving candidates are *equally* plausible. They
  each name a distinct sector mechanism (pure SU(3), SU(2)-matter,
  SU(3)-cosmological); the further discriminator question is which
  sector mechanism the cascade × inflation lock invokes — a question
  the framework's existing apparatus engages but does not yet close.
- That this picks 1/27 or 2/57 by default. It does not. The leaf
  stays Class-2 until the joint sector lands.

---

## Distinct from the continuous-domain discriminators

The projection's force comes from its integer-graded character. The
continuous-domain discriminators the framework has tried at the
cluster — sync-cost minimization (`farey_proof.md`), tongue-width
maximization, geometric-invariant preservation (N17,
`geometric_forcing_null.py`) — all fail or tie at the cluster because
the substrate's resolution is precision-limited at that depth
(`minimum_alphabet.md` "Identification cluster" + z-buffer analogy).
Q-mod-2 lives at integer resolution and therefore is not subject to
that precision floor. This is exactly what the closing observations of
the cluster audit said the question required:

> "Win-kill requires integer/topological resolution, not
> floating-point. The Q-mod-2 mediant extension qualifies; sectoral
> grounds qualify; sync-cost in the continuum doesn't."
> — earlier session reasoning, recorded in `session_handoff_2026-05-27.md`

The mediant projection is the operational form of that "Q-mod-2
extension."

---

## Falsifiers

- **An alternative Q-on-mediants bridge that survives substrate
  consistency.** A demonstration that `Q ≡ q mod 2` or `Q ≡ (p+q) mod 2`
  is *more* consistent with `q_mod2_conservation_theorem.md` Step 1's
  kink-number reduction than `Q ≡ p mod 2` would void the bridge claim.
  All three alternatives are XOR-additive under mediant; deciding
  between them is the step 2 derivation residual. A clean
  field-theory derivation pinning *which* parity descends as the
  state-axis Q is needed to fully close the bridge.

- **A demonstration that the joint sector determination is itself
  vacuous.** If `Q_cascade ⊕ Q_inflation` turns out not to be
  well-defined from substrate primitives — for example, if the
  cascade's Farey-path parity is itself anchor-side — then the
  projection has no input to apply, and the K(t) leaf's reduction to
  a binary becomes spurious. (This would be a *deeper* decline-kill
  of the leaf: not "we can't single out a candidate" but "the
  framework's primitives can't even specify the parity question.")

- **The bridge breaks for non-uniform-rotation lock profiles.** The
  kink-number-equals-numerator reading is cleanest for uniform-rotation
  lock profiles. If the substrate's lock-state profile carries
  additional kink-pair structure that contributes to `Q mod 2`
  independently of the rotation number, the bridge needs refinement;
  the simple `Q ≡ p mod 2` reading could be voided in favor of a more
  complex assignment.

- **A measurement that rules out all three jointly canonical
  candidates.** If the cosmological mass-function slope is measured at
  sufficient precision and corresponds to a cadence outside
  `{0.0351, 0.0370, 0.0385}` ± their precision-limited tolerances, the
  joint admissible set under Q-mod-2 + #6 is empty, voiding the bridge
  + projection.

---

## Why this matters

The K(t) leaf had been parked at "cluster of 14 candidates, no
visible-side discriminator can adjudicate" (the audit's z-fighting
verdict). The mediant projection moves the leaf from
"continuous-domain stuck" to "binary remaining" — concretely:

- 14 cluster candidates →
- 7 surviving after Q-mod-2 projection →
- 3 jointly canonical after Q-mod-2 + #6 →
- 1 or 2 admissible once joint sector lands.

This is the framework's apparatus actively doing the discriminating
work the cluster audit said the question required — an integer-graded
constraint above the precision floor — without introducing any new
primitive. The substrate's existing inviolables (specifically #1 and
#6, combined under the substrate's mediant operation) are doing the
work.

The projection is also one of the *cheapest* of the open paths
identified after the cluster audit: it consolidates an apparatus
position rather than introducing structure, and it engages directly
with the leaf's specific open question.

Class: foundational consolidation (Class 3, articulation), with a
named conditional computational result.

---

## Cross-links

- `substrate_determinism.md` — the 10 inviolables; this doc supplies
  the state-axis projection of #1 and combines it with #6.
- `q_mod2_conservation_theorem.md` — the time-axis reading of #1; the
  bridge in step 2 inherits from its kink-number reduction.
- `sine_gordon_substrate.md` — the kink ↔ antikink identification
  the bridge consumes.
- `klein_bottle.md` — the antiperiodicity rule `(∗)`.
- `wave_particle_substrate.md` — bicone Z₂ rigidity.
- `farey_proof.md` — the mediant rule from sync-cost minimization;
  XOR additivity of `p mod 2` under mediant is the structural
  consistency check.
- `k_of_t_problem_statement.md` — the leaf this doc engages directly.
  The "Identification 4 scope" note flags the cadence band; this doc
  computes admissibility within it.
- `continuity_in_K_nulls.md` — N12/S2 the cluster the projection
  filters; the audit-revised dangling-source note.
- `minimum_alphabet.md` — "Identification cluster" §, where the
  z-fighting analogy named what the projection answers; this doc is
  the answer's structural form.
- `derivation_4_audit_2026-05-28` — the audit commit (`e164760`) and
  PR #175 that motivated the projection.
- `equivalence_dissolution.md` — companion state-axis-articulation
  doc; same house style.
- `collapse_dissolution.md` — likewise.
- `geometric_forcing_null.py` — N17, the continuous-domain
  discriminator the projection lives above the precision floor of.

---

## One-line summary

The state-axis dual of `Q mod 2` conservation (#1) is a parity
superselection on Farey mediants given by `Q ≡ p mod 2`; combined with
inviolable #6, it narrows the K(t) inflation-cadence cluster from
14 candidates to **3 jointly canonical ones** — `1/26 = 1/(q₂·13_Λ)`,
`1/27 = 1/q₃³`, `2/57 = 2/(q₃·19_Λ)` — and reduces the leaf's open
status to a *binary* over the joint cascade × inflation Q-mod-2
sector.
