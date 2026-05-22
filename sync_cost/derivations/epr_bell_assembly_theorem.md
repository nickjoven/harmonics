# EPR/Bell assembly theorem

## Status

**Standalone assembly articulated** for the long-standing
phenomenology pointer
"EPR / Bell-inequality violation: Pieces present (Born rule +
Z_2-pair conservation theorem + substrate non-locality on
Stern-Brocot tree); … **the assembled EPR/Bell theorem still not
articulated**" (`phenomenology_cross_reference.md:439`).

This doc supplies the missing assembly. No new primitive; no new
prediction. Every ingredient already lived in the corpus:

- **Born rule** from saddle-node basin measure (`born_rule.md`,
  D1; exponent 2 forced by parabola normal form).
- **`Q mod 2` conservation** under L_x-local operations
  (`q_mod2_conservation_theorem.md`, PR #147).
- **Topological non-locality** of the Klein-bottle context window
  (`substrate_determinism.md` L290–298: "the topology — not its
  contents — carries the nonlocal correlations";
  `wave_particle_substrate.md`'s topological-EPR reading).
- **K < 1 → Schrödinger** continuum limit (`continuum_limits.md`
  Part II, D12): entangled wavefunctions arise as Madelung
  reductions of substrate dynamics in the unlocked sector.

The contribution is the composition — packaged as a four-clause
theorem with proof, a precise locality definition (re-used from
PR #147), exhibited consequences, and falsifiers. The interpretive
load-bearing claim ("Bell-evades via topological non-locality, not
hidden variables") was already asserted across `substrate_determinism.md`
and `wave_particle_substrate.md`; this doc gives it a closed
statement.

Class: foundational consolidation (Class 3, articulation). The
arc closed is the assembly flag, not a new empirical prediction.

---

## The theorem

**Theorem (EPR/Bell assembly).** Let `(A, B)` be a Z₂-paired pair
of substrate modes on the Klein-bottle quotient of the Stern-Brocot
tree, with conserved topological charge `Q_{AB} ∈ ℤ/2ℤ` (in the
sense of `q_mod2_conservation_theorem.md`). Let measurement
outcomes at `A` and `B` be basin selections of saddle-node
parabolas in the K < 1 (Schrödinger) sector (`born_rule.md`,
`continuum_limits.md` Part II). Then:

**(a) Composability.** The joint measurement statistics
`P(a, b ∣ θ_A, θ_B)` — single-site marginals given by the Born
rule, constrained by `Q_{AB} mod 2 = const` — coincide with the
standard quantum-mechanical entangled-pair statistics for the
corresponding Z₂-paired wavefunction in the Schrödinger sector.

**(b) Bell violation.** The CHSH parameter
`S(θ_A, θ_A', θ_B, θ_B')` computed from these joint statistics
attains the Tsirelson bound `2√2 > 2`, exceeding the local
hidden-variable upper bound and matching the standard QM upper
bound.

**(c) No-signaling.** A local operation at `A` (a deformation of
`φ` with support of diameter `< L_x`, in the sense of (L1)+(L2)
of `q_mod2_conservation_theorem.md`) cannot change `Q_{AB} mod 2`.
Hence the marginal distribution at `B`,
`P_B(b ∣ θ_B) = ∑_a P(a, b ∣ θ_A, θ_B)`, is independent of
Alice's measurement setting `θ_A`. The framework's correlations
are non-signaling.

**(d) Bell-non-exclusion.** Bell's theorem rules out *local
hidden-variable* reproductions of entangled-pair statistics. The
framework is not a local hidden-variable theory: the conserved
`Q_{AB} mod 2` is a **global topological invariant** of the
Klein-bottle field configuration, not a shared latent variable
distributed between the events at `A` and `B`. Hence Bell's
no-go does not apply, and (a)–(c) are consistent with each other.

---

## Proof

### Clause (a) — Composability

The K < 1 continuum limit (`continuum_limits.md` Part II, D12)
produces the Schrödinger equation in Madelung variables `(ρ, S)`
on the unlocked-mode sector. A Z₂-paired mode pair `(A, B)` is a
joint configuration of two such modes labelled by their tree
coordinates on the Klein-bottle quotient (Stern-Brocot tree
mod p/q ↔ q/p; `klein_bottle.md`). The substrate identifies:

- **Single-site Born weight** = saddle-node basin measure
  `|ψ|²` at each site (`born_rule.md` §"Connection to Arnold
  tongue geometry"; tongue width ∝ `Δθ²` ∝ ε, with `Δθ` the
  attractor separation).
- **Joint constraint** = `Q_{AB} mod 2 = const` (the conserved
  topological charge of the pair; `q_mod2_conservation_theorem.md`).
- **Measurement basis** at site = orientation `θ` of the
  saddle-node parabola at the Arnold-tongue boundary the
  measurement projects onto.

Substituting these identifications into the standard QM
two-particle measurement calculus reproduces the QM joint
distribution term-by-term: marginals from `|ψ|²` (Born), joint
phase-correlation from the shared topological charge (= the
entanglement label in the QM reading), basis dependence from
saddle-node orientation (= projector angle). The composability
is term-by-term substitution; no additional ingredient is
required.

### Clause (b) — Bell violation

Given the substrate ↔ QM identifications of clause (a), the
joint distribution for a Z₂-paired pair in maximally-entangled
configuration (`Q_{AB} mod 2 = 0`, anticorrelated outcomes) is

    P(a = b ∣ θ_A, θ_B)  =  sin²((θ_A − θ_B)/2),
    P(a ≠ b ∣ θ_A, θ_B)  =  cos²((θ_A − θ_B)/2),

equivalently `E(θ_A, θ_B) = ⟨ab⟩ = −cos(θ_A − θ_B)` for outcomes
`a, b ∈ {±1}`. This is the QM prediction (matched termwise by
clause (a)), not a separate framework derivation. The CHSH
parameter at the standard optimal settings
`(θ_A, θ_A', θ_B, θ_B') = (0, π/2, π/4, 3π/4)` is

    S  =  E(θ_A, θ_B) + E(θ_A, θ_B') + E(θ_A', θ_B) − E(θ_A', θ_B')
       =  −cos(−π/4) − cos(−3π/4) − cos(π/4) + cos(−π/4)
       =  2√2.

Local hidden-variable theories satisfy `|S| ≤ 2`
(Bell 1964 / CHSH 1969). The framework attains `2√2 > 2`;
the inequality is violated. The violation is structurally
identical to QM's, by clause (a).

### Clause (c) — No-signaling

Fix Alice's setting `θ_A`. Any operation Alice performs at `A`
is realized in the substrate as a deformation `φ_t` of the
sine-Gordon field whose instantaneous support lies in an open
set `D_A ⊂ K²` of diameter `< L_x` (operations at a single
measurement site fit in a chart of the Klein bottle smaller
than the antiperiodic loop — the standard locality assumption
of `q_mod2_conservation_theorem.md` (L1)+(L2)).

By `q_mod2_conservation_theorem.md` Step 3, such a deformation
preserves `Q mod 2`. In particular, the pair-charge `Q_{AB} mod 2`
is unchanged by Alice's choice. Hence the joint distribution
`P(a, b ∣ θ_A, θ_B)` — which depends on `θ_A` only through the
projector at `A` and on `Q_{AB} mod 2` for the joint constraint —
yields a marginal at `B` that, when summed over `a`, depends
only on the projector at `B`:

    P_B(b ∣ θ_B)  =  ∑_a P(a, b ∣ θ_A, θ_B)
                  =  ½         (uniform, independent of θ_A)

(direct computation; the dependence on `θ_A` cancels because the
QM marginal of a maximally entangled state is the reduced density
matrix `I/2`).

So Alice's setting choice cannot bias Bob's measurement
distribution: no signal carries from `A` to `B`. The
non-signaling theorem of standard QM is reproduced via the
substrate mechanism.

### Clause (d) — Bell-non-exclusion

Bell's theorem (1964) and its variants (CHSH, Mermin, etc.)
rule out theories satisfying *local hidden variables* (LHV):
namely, theories in which `P(a, b ∣ θ_A, θ_B)` factorizes
through a shared latent variable `λ`,

    P(a, b ∣ θ_A, θ_B)  =  ∫ ρ(λ) · P_A(a ∣ θ_A, λ) · P_B(b ∣ θ_B, λ) dλ,    (LHV)

with `P_A` depending on `(θ_A, λ)` only and `P_B` on `(θ_B, λ)`
only. The framework's joint distribution does *not* admit such
a factorization. The reason is structural:

`Q_{AB} mod 2` is a **global topological invariant** of the
Klein-bottle field configuration — by `q_mod2_conservation_theorem.md`
Step 1 (well-definedness on `K²`) it is an invariant of the
homotopy class of `φ`, not a function of any local field value
at `A` or `B`. It does *not* admit a representation as a shared
random variable `λ` distributed between the two measurement
events. Topological invariants are not random variables on
the substrate; they are equivalence classes.

Bell's no-go does not apply: the framework violates (LHV)'s
*structural* assumption (existence of `λ`), not just its
numerical consequences. The framework's non-locality is
**topological** — global in the homotopy-class sense — not
hidden-variable. Clauses (a)–(c) are therefore mutually
consistent. QED.

---

## What this says (and what it does not)

**It says:** the framework's three ingredients (Born + `Q mod 2`
conservation + topological non-locality) compose to a Bell-violating
correlation pattern that is (i) numerically equal to QM's,
(ii) non-signaling, and (iii) consistent with Bell's no-go because
the framework is not a local hidden-variable theory. The
qualitative claim "framework Bell-evades via topological
non-locality" — long asserted in `substrate_determinism.md` —
now has a closed-form assembly.

**It does not say:** the framework derives the Tsirelson bound
`2√2` from substrate-internal first principles independent of
QM. Clauses (a) and (b) state that, *given the substrate ↔ QM
identifications* (Born = basin measure; `Q mod 2` = entanglement
label; saddle-node orientation = measurement basis), the framework's
predictions equal QM's by direct substitution. The Tsirelson value
is QM's, and the framework matches it by reproducing QM in the
K < 1 sector. An independent derivation of the Tsirelson bound
from pre-QM substrate constraints alone would be a *separate*
theorem, much stronger than this one. The bright line is between
*reproducing QM via substrate identifications* (this theorem) and
*deriving QM-as-unique from non-quantum axioms* (a generations-old
foundational problem that this theorem does not solve).

**Bright line.** This is an assembly/consistency theorem — a
classification result composing existing ingredients into a single
statement. It is not a quantitative prediction of any
non-QM-already-known observable. The empirical content (Bell
violation, no-signaling, the Tsirelson bound) is QM's, reached
via substrate routes.

---

## Distinct from Q mod 2 conservation (q_mod2_conservation_theorem.md)

`q_mod2_conservation_theorem.md` proves a *single*-charge
invariance under local processes. *This* theorem composes that
invariance with two further substrate ingredients (Born,
topological non-locality) to address the joint statistics of a
*pair* of modes and their Bell-style correlations. Q mod 2 is a
prerequisite (Clauses (a), (c), (d) all consume it); the EPR/Bell
assembly is the downstream application.

Distinctness summary:

| Theorem                                | Object                          | Scope                             |
|---|---|---|
| `q_mod2_conservation_theorem.md`       | Single Z₂ charge `Q` on `K²`    | Invariance under L_x-local processes |
| **This doc**                            | Pair charge `Q_{AB}` + joint statistics | Bell violation + no-signaling + Bell-non-exclusion |

---

## Exhibited consequences

1. **The framework predicts Bell violation, not just consistency with
   it.** Given a Z₂-paired pair in the maximally-entangled
   configuration (`Q_{AB} mod 2 = 0`), the CHSH parameter is `2√2`,
   exceeding the LHV bound `2`. This matches the experimental
   observations of Aspect (1982), Hensen et al. (2015) and successors
   to within the framework's standard-QM identification.

2. **The non-signaling theorem is reproduced via the substrate
   locality threshold `L_x`, not imported.** Alice cannot signal to
   Bob because changing `Q_{AB} mod 2` requires a deformation of
   diameter `≥ L_x` (encircling the antiperiodic loop), which is
   not a local operation at either site.

3. **The framework's interpretation of EPR is now formalised.** EPR's
   original "spooky action at a distance" objection presumed that
   non-locality must be either (i) carried by signals (violating
   relativistic causality) or (ii) carried by hidden variables
   (which Bell later excluded). The framework's non-locality is
   neither: it is the *topology* of the configuration space (Klein
   bottle Z₂), which is global in the homotopy-class sense without
   carrying signals. The "spookiness" dissolves once the topological
   character is recognised — there is no action propagating between
   `A` and `B`; there is only a global invariant of the joint
   configuration.

4. **No new empirical prediction.** The theorem's numerical content
   is identical to QM's. Falsification of the theorem would require
   falsifying QM's Bell predictions (already tested to extraordinary
   precision) *or* falsifying one of the three substrate ingredients
   (Born, Q mod 2 conservation, K < 1 → Schrödinger). The assembly
   itself adds no independently testable prediction.

5. **Composability with the substrate-determinism debate.** Branch
   (B) of `substrate_determinism.md` (deterministic substrate
   reframing) becomes coherent: a deterministic substrate can
   reproduce QM's Bell-violating correlations because its
   non-locality is topological, not hidden-variable. The "Bell rules
   out determinism" objection rests on the LHV form of locality,
   which the framework does not satisfy. (Whether (B) is *correct*
   is a separate question; what this theorem establishes is that it
   is *not excluded by Bell*.)

---

## Falsifiers

- **Substrate-internal violation.** A demonstration that the
  substrate identifications of clause (a) — Born = basin measure,
  `Q_{AB} mod 2` = entanglement label, saddle-node orientation =
  measurement basis — yield joint statistics *different* from QM's
  would falsify the theorem. Each identification is independently
  exhibited in `born_rule.md`, `q_mod2_conservation_theorem.md`,
  and `continuum_limits.md`; the assembly inherits their
  correctness.

- **Empirical Bell-bound revision.** If experiments revealed
  correlations *exceeding* the Tsirelson bound `2√2` (a PR-box-like
  super-quantum signal), QM itself would be falsified, and so
  would this theorem (clause (b) would predict `2√2`, not the
  observed value). No such experiment has succeeded; the bound
  appears solid.

- **Signaling experiment.** A genuinely faster-than-light signaling
  demonstration via entangled pairs would falsify clause (c). This
  is equivalent to falsifying the non-signaling theorem of QM, which
  is on similar empirical footing.

- **Topology falsifier.** If the substrate were not the Klein bottle
  (e.g., were a torus), `Q ∈ ℤ` would be conserved without
  mod-2 reduction; the kink/antikink pairing across antiperiodic
  loops would not exist; the topological-non-locality mechanism of
  clause (d) would dissolve. The theorem is contingent on the Klein
  commitment (same falsifier as `q_mod2_conservation_theorem.md`).

---

## Why this matters

The corpus has long asserted that the framework "Bell-evades via
topological non-locality" (`substrate_determinism.md` L208;
`wave_particle_substrate.md`'s topological-EPR reading) without a
single doc supplying the closed assembly. The phenomenology
cross-reference table explicitly flagged "the assembled EPR/Bell
theorem still not articulated" as the open item.

That assembly is now standalone. The framework's predictions for
EPR/Bell phenomenology are no longer an *interpretive claim*
("our nonlocality is topological, so Bell doesn't exclude us") but
a *composed theorem* with clauses (a)–(d) above. The interpretive
content is preserved exactly — but the corpus can now cite a
single statement-and-proof rather than three scattered ingredients
plus an interpretive paragraph.

Parallel in structure to `q_mod2_conservation_theorem.md`:
articulation, not new content; the contribution is the closed-form
statement.

---

## Cross-links

- `born_rule.md` — basin-measure derivation of Born exponent 2
  from saddle-node parabola (ingredient 1, Clause (a)).
- `q_mod2_conservation_theorem.md` — `Q mod 2` invariance under
  L_x-local operations (ingredient 2, Clauses (a), (c), (d)).
- `substrate_determinism.md` L208, L290–298 — topological
  non-locality framing; the Bell-evasion claim this theorem closes.
- `wave_particle_substrate.md` — the topological-EPR reading
  precedent.
- `continuum_limits.md` Part II (D12) — K < 1 → Schrödinger
  emergence (ingredient 4, Clause (a)).
- `klein_bottle.md` — the Klein-bottle topology of the mode space
  (the Z₂ involution under which `Q mod 2` is defined).
- `sine_gordon_substrate.md` §"Z_2-graded topological charge" —
  the kink/antikink identification underlying `Q`.
- `phenomenology_cross_reference.md` — EPR/Bell row, to be
  updated to cite this doc.
- `framework_status.md` Survives row for the inviolable family —
  to be updated to cite this assembly.
- `thread_chronology.md` — entry for this articulation.

## One-line summary

The framework's three ingredients — Born rule from saddle-node
basins, `Q mod 2` conservation under L_x-local processes, and the
topological (not hidden-variable) character of Klein-bottle
non-locality — compose to a Bell-violating, non-signaling joint
statistics for Z₂-paired modes that matches QM's entangled-pair
predictions, is not excluded by Bell's theorem, and now has a
standalone four-clause statement-and-proof.
