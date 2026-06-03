# The Farey Tree Under Three Problems: Structure, Not Numbers

*Capstone synthesis of the vocabulary-studies notes. Limits-first.*

## What this is NOT (read before the thesis)

This note does **not** solve, or claim progress on, Ramanujan's series,
the Collatz conjecture, or the Riemann Hypothesis. It does **not** claim
the harmonics framework derives any of them. Vocabulary alignments
between a pet framework and famous results are **cheap and infinite** —
you can play that game on any celebrated object, and most who do are
fooling themselves. The only thing that earns this note its place is that
the alignment keeps producing the *same negative*, and a correspondence
that reliably tells you where it **fails** is doing real work. So the
deliverable here is a **viewpoint and its boundary**, classified Class 2
(structural reading), not a result.

## The thesis

> A single object — the **Stern–Brocot / Farey tree**, i.e. the
> `PSL(2,Z)` action on `ℚ`, i.e. the framework's **mediant primitive** —
> gives a common reading of three celebrated problems. In each, the
> **structure** (the tree, its group, its levels and boundary) is forced
> and tractable, while the **arithmetic** (a discriminant, an orbit, a
> distribution) lives at the tree's **boundary** and is exactly the
> hard/open part.

The mediant primitive is a **structure-fixer, not a moduli-fixer.** That
single sentence is the synthesis; the three legs are its evidence.

## The three legs

| Problem | Structure on the tree (forced / tractable) | Arithmetic at the boundary (hard / open) |
|---|---|---|
| **Ramanujan 1/π** | the modular **level** `Γ₀(6)` — a real Ramanujan–Sato level whose divisor lattice {1,2,3,6} is the q₂×q₃ cusp/sector taxonomy; the series is a **convergent path** through the tree to a cusp (π) | the **CM discriminant** `d = 58` that fixes the integer constants `1103, 26390, 9801` (selector prime 29) — never forced |
| **Collatz** | integers are the **q=1 boundary** of a rational (mediant/Ford-circle) Collatz; the **only cycle is {1,2}** because `3^a ≠ 2^b`; residue coverage is provable | which **orbit** converges, and in how many steps — the per-`n` arithmetic — is open |
| **Riemann (RH)** | the tree's **leaves** (Farey fractions): their order and count `|F_N|` are elementary | their fine **equidistribution** — `D(N)=Σ\|r_ν − ν/M\|` — is, by **Franel–Landau (1924)**, *equivalent to RH* |

The three legs are developed in:
`ramanujan_pi_minimum_alphabet.md`, `ramanujan_pi_modular_discriminator.md`,
`ramanujan_pi_structure_not_numbers.md`, `collatz_minimal_chaos.md`; the
RH leg's discrepancy `D(N)` is computed in `farey_tree_synthesis.py`
(`D(N)/√N` stays bounded — the RH-equivalent signal; *proving* the bound
for all `N` is the open problem).

## Why the legs are one statement

Each problem places a different demand on the *same* tree, and each splits
the same way:

- **Ramanujan** asks for a *point* on the tree's modular boundary (a cusp
  / CM point). The framework forces the *level* the point sits on (`Γ₀(6)`,
  because `6 = q₂·q₃`), but the point itself (`d=58`) needs a prime (29)
  off the `{2,3}` hierarchy. **Structure yes, coordinate no.**
- **Collatz** asks whether a *flow* on the tree reaches the root from every
  integer. The framework forces the *structural* facts (one cycle, from
  `{2,3}` incommensurability; the integers as the slow q=1 boundary). The
  *orbit-by-orbit* answer is the open conjecture. **Structure yes, orbit no.**
- **RH** asks whether the tree's *leaves* are evenly spread. Their
  existence and ordering are elementary structure; their *distribution* is
  RH. **Structure yes, distribution no.**

In all three, the forced part is `{2,3}`-smooth / genus-zero / low-depth —
the part the mediant primitive natively generates — and the open part is a
finer arithmetic invariant at the boundary that no structural/group-theoretic
machine selects. This is not a coincidence across three problems; it is one
property of structure-fixing methods, seen three times.

## Honest weight: common cause, not prediction

The framework and these problems share the Farey tree for the **same
underlying reason** (genus-zero modular structure / widest Arnold tongues /
lattice-compatible orders all concentrate on small primes), not because the
framework predicts them. The shared home is real and explains the recurring
near-miss; it does **not** promote to deriving π, Collatz, or RH, because
each of those is a statement about the arithmetic *boundary*, and selecting
boundary arithmetic is precisely what a structure-fixer cannot do. The
synthesis is honest exactly because it includes this ceiling.

## What would make this a theorem vs. an essay

- **Essay (achievable).** As written, this is an expository unification —
  fit for arXiv **math.HO** or a public essay: "three problems on the Farey
  tree, and the line between structure and arithmetic." It needs no physics
  and is stronger without it. The Franel–Landau leg is the anchor (RH *is*
  a Farey-tree statement); Ramanujan and Collatz are the worked legs.
- **Theorem (research moonshot; low odds; stated plainly).** The one leg
  with research potential is **Collatz**: prove that rational Collatz
  **contracts in the hyperbolic (Ford-circle) metric for `q>1`**, making the
  integer conjecture the boundary trace of a proved bulk statement (the
  framework's K<1/K=1 boundary/bulk move). But the substrate's own
  `collatz.html` flags this step as "the conjecture restated," and
  dynamical/2-adic attacks on Collatz are a graveyard. Worth exploring
  numerically; not worth betting on. The RH leg is **not** a research
  opening — Franel–Landau is a century old and the bound is the whole game.

## Status

**Class 2 — expository synthesis (structural reading).** No scorecard
claim, no new constant, no solution claimed. The value is the viewpoint
plus its explicit boundary. The recurring negative ("structure forced,
arithmetic open") is the finding.

## References

- Franel, *Les suites de Farey et le problème des nombres premiers* (1924);
  Landau (1924) — RH ⟺ Farey equidistribution. Huxley, Fujii — extensions.
- Borwein & Borwein, *Pi and the AGM* (1987); Berndt–Bhargava–Garvan (1995)
  — Ramanujan's modular / alternative-bases theory.
- Lagarias, *The 3x+1 problem and its generalizations* (1985).
- Sibling notes (this repo) + harmonics upstream: `minimum_alphabet.md`,
  `mediant_derivation.md`, `psl2z_subgroup_phase_a_results.md`,
  `second_law_topological.md`, `docs/archive/collatz.html`.
- Check: `farey_tree_synthesis.py`.
