# Substrate determinism: is probability fundamental or emergent?

Top-level foundational doc, parallel in level to
`wave_particle_substrate.md`, `no_rescaling.md`,
`expressibility_split.md`, `comparison_class.md`. Frames the
framework's deepest open foundational question — **is the substrate
deterministic with emergent probability, or is probability
fundamental?** — records the framework's partial answer, the strong
prior its own structure provides, the computation that would settle
it, and the constraints any resolution must not violate.

This doc does **not** resolve the question. It frames it, argues the
prior, and fixes the inviolables. No new primitive.

## The ontological setup: the mechanics constitute a wave

Standard quantum mechanics: a quantum entity is neither wave nor
particle but *displays* wave-like or particle-like properties
depending on measurement. The framework rejects the "entity
displaying properties" ontology entirely.

**The framework's ontology:** there is the substrate — a medium
(Klein bottle + Kuramoto coupling) carrying phase coherence (the
order parameter `r e^{iψ}`). Configurations of that phase coherence
are:

- **Mediant-side / particle:** localized, fiber-bound, discrete
  (a kink at a cascade fixed point).
- **EML-side / wave:** delocalized, inter-fiber, continuous (a
  wave-amplitude on the K-axis continuum).

There is no "entity." "An electron displaying wave properties" is
the wrong ontology; "the substrate in an EML-side phase-coherence
configuration" is the framework's. The mechanics *constitute* a
wave (or particle) — they do not describe an entity that *has* the
property.

The wave↔particle conversion is the **half-twist** (`J² = −I`),
not a third category of object or measurement. Measurement is one
application of the half-twist at a D-crossing (`figure_eight.md`).

The primary object is the **sine-Gordon kink on the Klein bottle**
(`sine_gordon_substrate.md`), with the **bicone vortex** as its
dark-coupled 2D form (`cone_twist_substrate.md`). This is what
"a localized region of phase coherence through a medium" *is* in
the framework — not an abstraction, a real phase-transition region.

## The question

The framework's dynamics include an autoregressive sampling step:
at each Planck tick the substrate selects a token from an
action-weighted distribution (`exp(−S)`, `f_exit_natural.md`). Is
this selection:

- **(A) Fundamentally stochastic** — the substrate genuinely "rolls
  dice"; probability is a primitive of the framework; or
- **(B) Deterministic** — the token is fixed by the full substrate
  state (including discrete degrees of freedom we coarse-grain
  over); "probability" is the emergent bookkeeping of which
  deterministic branch we are on.

## The framework's partial answer

Probability in the framework is **already second-class**, not a
primitive:

- **The Born rule is derived, not postulated.** `figure_eight.md`
  and `wave_particle_substrate.md` derive `|ψ|²` from `J² = −I`
  (the half-twist's double application). The amplitude-squared
  probability law is a *topological consequence* of the half-twist,
  not a framework axiom.
- **The sampling weights are structural.** The `exp(−S)` Boltzmann
  factor is the path-integral form (`f_exit_natural.md`), itself
  derived from the substrate's action functional, not posited.

So the framework has *already* made the reframing for the Born
rule: probability-as-amplitude-squared is emergent from topology.
What remains open is the **deeper** question — is the discrete-event
selection itself (which token, at each tick) fundamentally
stochastic, or deterministic-but-coarse-grained?

## The prior: the framework's structure leans deterministic

The audit's entire pattern is a strong prior for branch (B):

| Evidence | Direction |
|---|---|
| Every catastrophic finding closed by an **exact structural articulation**, never a distribution | deterministic |
| Every surviving numerical result is an **integer or small-prime ratio** (`S_v ≈ 16`, `R = 6 × 13⁵⁴`, `Ω_Λ = 13/19`), never a probability density | deterministic |
| The **no-rescaling principle** demands *exact identity* between cosmic and substrate observables — a stochastic substrate would not produce exact identities | deterministic |
| The substrate at K=1 is **finite-mode** (4 modes, `nonperturbative_phase1.md`) — finite discrete state spaces admit deterministic trajectories | deterministic |
| The Born rule is **derived from a discrete topological fact** (`J² = −I`), not from an irreducible stochastic postulate | deterministic |

A genuinely stochastic substrate would not keep producing exact
integer identities under audit. The framework behaves like a
**deterministic system whose "probability" is the coarse-grained
description of unresolved discrete degrees of freedom** — the
't Hooft / cellular-automaton class of interpretation, but with
the framework's specific substrate (Klein bottle, mediant + EML,
half-twist) making the "hidden" dynamics *concrete* rather than
postulated.

**This is a prior, not a proof.** The framework leans (B) strongly;
it has not demonstrated it.

## What would settle it

Branch (B) is *demonstrated* if a specific realized token sequence
can be derived from {substrate Lagrangian + BOS initial condition}
with **no irreducible stochastic input**. The framework's
discreteness makes this possible in principle: the K=1 substrate is
finite-mode; a token transition is a finite-dimensional matrix
element, not a continuum amplitude.

The settling computation:

> Given the substrate Lagrangian and the BOS state (K=1, no
> realized tokens), compute the first N tokens of the realized
> sequence. If they are determined (no free stochastic choice at
> any step), probability is emergent (B). If any step requires an
> irreducible random input not fixed by the substrate state,
> probability is fundamental (A).

This is the same queued real-Phase-2-class work (the explicit
reduction matrix + event-by-event evolution) that the audit thread
kept reaching. It has not been done. Until it is, the fork is
**open**, with the structural prior strongly favoring (B).

## What "empirical probability has evaded the framework" means

The framework has the *mechanism* (Born from `J² = −I`,
action-weighted sampling) but has **not** produced a computed
probability *distribution* matched to a measured *histogram*.
Every framework prediction is a structural ratio or discrete count,
never a probability density compared to data. This gap is real and
independent of the (A)/(B) fork: even under (B), the framework
would still owe specific computed distributions for empirical
observables (cross-sections, decay rates). The (A)/(B) resolution
tells you *what probability is*; it does not by itself produce the
*empirical numbers*. Both are open; they are different opens.

## What can be confidently discretized

| Confidently discrete (mediant-side) | Not discretizable (EML-side) |
|---|---|
| Stern–Brocot tree (rationals, cascade fixed points) | Continuous phase `ψ` |
| Klein-bottle mode count at K=1 (4 after XOR) | Wave-side continuum (meson modes) |
| Arrow-time integer count (`N_events × τ_tick`) | Transcendentals (`π, e, φ` — limits, not discrete) |
| Token sequence (autoregressive) | Inter-fiber dark-sector currents |
| Topological charges (`Z₂`, winding numbers) | The path-integral measure as a whole |

The discretizable side is exactly the mediant/particle side; the
non-discretizable side is the EML/wave side. This is the
two-primitive split (`wave_particle_substrate.md`) seen through the
discretization question. **Determinism, if it holds, lives on the
mediant side; the EML side is the continuous shadow.**

## The inviolables — what any resolution must not violate

If the determinism investigation hits a dead end, or if any
resolution (A or B) is proposed, it must preserve **all** of the
following. These are the framework's hard constraints; a resolution
violating any one is wrong, regardless of how attractive it is
otherwise:

1. **Z₂ topological charge conservation (mod 2).** Klein-bottle
   topological rigidity. No local process changes `Q mod 2`.
2. **The no-rescaling identity.** Cosmic observable = substrate
   observable, *exact*, in Planck units (`no_rescaling.md`). Any
   resolution introducing a structural rescaling prefactor is
   excluded.
3. **Unitarity / information conservation.** Bicone Z₂ rigidity
   (`wave_particle_substrate.md`). No topology-changing process;
   no information loss.
4. **The two-primitive closure.** Mediant + EML, with Klein bottle
   and half-twist as derived consequences. No third primitive
   (`wave_particle_substrate.md`, revised). A resolution requiring
   a third independent primitive falsifies the synthesis.
5. **Born rule `= |ψ|²` exactly.** From `J² = −I`. The exponent is
   exactly 2 (`figure_eight.md`). A resolution shifting the Born
   exponent is excluded.
6. **The exact structural integers.** `Ω_Λ = 13/19`,
   `R = 6 × 13⁵⁴`, small primes `(2, 3)`, `d = 3` — derived from
   the four objects (`qd_origins.md`, `hierarchy_gaussian_lattice.md`).
   A resolution requiring different structural integers is excluded.
7. **Half-twist phase `= π` exactly.** Topological (Z₂ generator);
   the AB-phase prediction (`cone_twist_substrate.md` §5.2;
   `orthogonal_kink_interaction.md`). Crossing-detail-independent.
8. **Natural-irrationals closure `{φ, π, e, √n}`.** No other
   transcendental class (`expressibility_split.md`,
   `no_rescaling.md`). A resolution introducing, e.g., Khinchin's
   or Catalan's constant falsifies notational invariance.
9. **Arrow-of-time monotonicity.** Repair events accumulate; the
   antiperiodic-x arrow does not reverse (`time_axis_split.md`).
   A resolution permitting arrow reversal is excluded.
10. **The Planck floor.** Nothing below it; the substrate is the
    bottom (`wave_particle_substrate.md`). A resolution invoking
    sub-Planck structure exits the framework.

Any deterministic-substrate reframing (branch B) must reproduce
*all ten*. The strong prior for (B) is only admissible if (B) can
be realized without violating any inviolable — in particular,
without breaking the no-rescaling exact-identity (#2) or the Born
exponent (#5), both of which a naïve hidden-variable determinism
classically struggles with (Bell). The framework's escape, if (B)
holds, is that its nonlocality is **topological** (Klein-bottle
Z₂), not hidden-variable — so Bell's theorem does not exclude it
(consistent with `wave_particle_substrate.md`'s topological-EPR
reading). This is the consistency condition the settling
computation must respect.

## The momentum-dissolution argument (the strongest case for B)

A reframing that materially sharpens the prior for (B): **the
substrate needs no momentum, because it is first-order
autoregressive, not second-order Hamiltonian.**

Pose the question operationally: given the *position* of everything
(the full substrate configuration / realized token sequence), the
*tilt* (the half-twist Z₂ conversion structure / seam orientation),
and the *anchors* (the two observational scales `H₀`, `v_EW` plus
the BOS initial condition) — **but not momentum** — can the next
frame be computed?

A second-order system (classical Hamiltonian) answers *no*:
position alone underdetermines the trajectory; momentum is
required. But the framework's substrate, read autoregressively, is
**first-order discrete**: the next token depends on the prior token
sequence within the context window `L_x`, not on a conjugate
momentum. **In an autoregressive process, the realized history
substitutes for momentum.** (This is the `nonperturbative_phase1.md`
/ wave-particle "linear token generation" reading made rigorous: a
language model has no momentum variable; the next token is fixed by
prior tokens + weights. The substrate is structurally identical.)

So the operational answer is **yes**: position + tilt + anchors +
context (prior tokens within `L_x`) → next frame, deterministically,
*with no momentum and no irreducible stochastic input* — which is
exactly branch (B).

### The apparent paradox, resolved

The substrate Lagrangian *is* second-order (`(∂_t θ)²` →
`m ∂²_t θ`). How is it also first-order autoregressive? **The
second-order continuum Lagrangian is the coarse-grained shadow of
the first-order discrete process.** Discretizing a first-order
context-dependent update rule produces a continuum PDE that *looks*
second-order: the context-dependence becomes the time-derivative
term. The continuum "momentum" is an emergent artifact of
coarse-graining the discrete context-dependence, not a fundamental
conjugate variable. (Standard lattice→continuum: a discrete update
with memory yields a continuum wave equation; the "velocity" is the
coarse-grained memory.)

The framework therefore needs no momentum at the fundamental level.
Momentum is what the continuum approximation *invents* to summarize
the discrete context the autoregressive process actually uses.
"Position but not momentum, but the tilt and the anchors" is the
operational statement of branch (B): the universe computes its next
frame the way a language model computes its next token —
deterministically given context + weights — and the apparent need
for momentum is an artifact of the continuum description.

### What this changes for the prior

This is the strongest single argument for (B) so far. It does not
*prove* (B) — the autoregressive reading is a framework commitment,
and the settling computation (explicit token-sequence derivation)
is still required — but it removes the classical objection that
"position without momentum is underdetermined": that objection
assumes second-order dynamics, which the framework's discrete
substrate is not. The prior for (B) strengthens from "the audit
keeps producing exact integers" to "the audit keeps producing
exact integers *and* the dynamics are structurally first-order
(context, not momentum), so determinism is the natural reading and
the classical underdetermination objection does not apply."

The nonlocality, under this reading, is precisely the **finite
context window `L_x` being topologically structured** (Klein
bottle) — not hidden variables. This is the same Bell-evasion
condition as inviolable consistency above, now with a concrete
mechanism: the context window *is* the substrate's memory, and its
topology (not its contents) carries the nonlocal correlations.

## Status

Class 3 (foundational framing). No new primitive. The doc:

- Fixes the wave-constitution ontology (mechanics constitute a
  wave; no entity displaying properties).
- Frames the (A)/(B) fork (fundamental vs emergent probability).
- Records the framework's partial answer (Born rule already
  emergent from `J² = −I`).
- Argues the strong structural prior for (B) (the audit's
  exact-integer pattern).
- Specifies the settling computation (explicit token-sequence
  derivation from BOS).
- Enumerates the ten inviolables any resolution must preserve.

The question is **open**; the prior is **(B), strongly**; the
inviolables are **fixed**. This is the framework's deepest
foundational thread, recorded at the level it deserves.

## Cross-links

- `wave_particle_substrate.md` — the two-primitive ontology; Born
  rule emergent from `J² = −I`.
- `no_rescaling.md` — the exact-identity principle (inviolable #2);
  evidence for the deterministic prior.
- `figure_eight.md` — `J² = −I`, the Born rule's topological origin.
- `f_exit_natural.md` — action-weighted sampling as the
  path-integral form (the mechanism, not a stochastic primitive).
- `nonperturbative_phase1.md` — finite-mode K=1 substrate
  (deterministic-trajectory-admitting).
- `expressibility_split.md` — the `{φ, π, e, √n}` closure
  (inviolable #8).
- `time_axis_split.md` — arrow monotonicity (inviolable #9).
- `cone_twist_substrate.md` — AB-phase = π (inviolable #7).
- `orthogonal_kink_interaction.md` — the AB-phase unification;
  the `E_cross` open item, separate from this fork.
- `qd_origins.md`, `hierarchy_gaussian_lattice.md` — the exact
  structural integers (inviolable #6).

## The honest statement

The framework is *probably* deterministic at the substrate level,
with probability emergent as coarse-graining over unresolved
discrete degrees of freedom — the Born rule already demonstrates
this reframing for amplitude-squared specifically. The audit's
exact-integer pattern is a strong prior. But this is not proven;
the settling computation (explicit token-sequence derivation) has
not been done; and any resolution must preserve all ten
inviolables, in particular the topological (not hidden-variable)
character of the framework's nonlocality. Empirical probability —
computed distributions matched to histograms — remains a separate,
also-open gap. Two opens, one strong prior, ten fixed constraints.
