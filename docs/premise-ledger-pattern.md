# The Premise-Ledger Pattern

A portable design for claim-consistency accounting in any corpus
whose documents cite each other's results — research repositories,
knowledge bases, RAG stores, policy/legal claim systems, wikis.
Reference implementation: `scripts/drift/check_premises.py` +
`sync_cost/derivations/PREMISES.md` in this repository.

---

## 1. What a clean check does NOT mean — read this first

A passing ledger is **not** a soundness certificate. The machine
verifies four bookkeeping facts and nothing else:

1. every cited premise names an anchor that exists where claimed,
2. no anchor name has two providers,
3. no strong status rests (transitively) on an unsettled one,
4. the citation graph is acyclic.

It deliberately does **not** verify:

- that a document's prose actually establishes what its `provides:`
  declares — `status=proven` is a **human attestation**, recorded,
  not checked;
- that a status was assigned honestly or competently;
- that the premise list is **complete** — an undeclared dependency
  is invisible, and propagation is only sound over declared edges;
- that an anchor's name means what a reader assumes it means.

The correct mental model is double-entry bookkeeping: the ledger
cannot detect a fraudulent invoice, only unbalanced books. Its value
is that inconsistency becomes *visible, localized, and cheap to
find* — and that the soundness question is *localized to one place
per claim* (the providing document) instead of diffused across every
citation site.

**Asymmetric confidence rule.** A red result is a theorem — the
declared structure is inconsistent, trust it fully. A green result
is only the absence of *detected* inconsistency. The system is a
falsifier, not a validator. Any UI, report, or summary built on it
must render green as "consistent as declared," never as "verified"
or "sound." If your display layer shows checkmarks, this is the
sentence that keeps them honest.

## 2. Threat model: deterministic theater

The pattern's principal self-inflicted risk is that its machinery
*looks* rigorous — graphs, statuses, exit codes — and that
appearance transfers unearned authority to the content. Observed
instances in this repository's own history, kept here as canonical
counterexamples:

- Verification scripts passed for months while comparing a formula
  with itself (tautological verifier).
- A drift gate was green because its extractor had never matched
  anything (vacuously green gate).
- An aggregate count "confirmed" a rule when an incompatible rival
  rule predicted the identical count (non-discriminating evidence).

None of these are detectable by consistency accounting. They define
the pattern's boundary and motivate its mandatory countermeasures
(§5).

## 3. Core design (format-agnostic)

- **Named anchors.** Every claim that anything else depends on gets
  a globally unique, human-chosen name. A dependency is a reference
  to a name at a provider, never a prose paraphrase.
- **One name, one provider.** Two documents providing the same name
  is a hard error. This forces rival formulations of "the same"
  claim to collide instead of forking — fork-instead-of-collide is
  how contradictory conventions coexist silently.
- **Closed status vocabulary with attestation burdens.** Each status
  is a human claim with a defined evidential burden (this repo:
  axiom, definition, proven, derived, imported, conditional,
  conjectured, fitted). A vocabulary without written burdens decays
  into vibes. `fitted` exists as first-class status because
  "derived" is the label under which observation-inverted values
  launder themselves.
- **A propagation rule.** Here: strong statuses (proven/derived) are
  barred when any premise resolves, transitively, to an unsettled
  status; the ceiling is `conditional`. See §4 for what this rule
  does and does not encode.
- **A carrier channel native to the format** that renderers and
  retrieval chunkers ignore: HTML comments in markdown, fields in
  structured rows (see the MANIFEST integration), properties in a
  graph store, template parameters in a wiki. The anchors must never
  become reading-surface noise, or authors will resist them.
- **Ratchet adoption.** Only documents that declare anchors are
  checked; anything touched by an edit gains anchors. Backfill the
  most load-bearing documents first. This makes adoption incremental
  and makes coverage an explicit, growing number rather than an
  implicit assumption.
- **Scoreboard integration.** Any summary artifact that assigns
  claims a headline status (here, MANIFEST rows) declares premises
  too, with the rule: a strong headline status plus an unsettled
  premise is a machine violation. Summaries are where neglected
  repercussions hide, because they are written once and believed
  often.

## 4. The propagation rule is an epistemology — document it as one

Weakest-link propagation is a *choice*, and ports must state it,
because readers will otherwise assume semantics that are not there:

- **No aggregation.** Two independent conjectured routes to the same
  conclusion do not upgrade it. The lattice is min(), not Bayesian
  pooling. Deliberately conservative; states so.
- **Coarse quantization.** A 95%-confident derivation and a coin-flip
  hunch are both `conjectured`. The vocabulary quantizes epistemic
  state and loses information by design; nuance lives in the
  document's prose, which the ledger does not read.
- **Transitivity is directional.** Demotion propagates automatically;
  promotion never does. Upgrading a premise does not auto-upgrade its
  consumers — each must be re-attested, because their proofs may use
  the old weaker form.

## 5. Mandatory anti-theater countermeasures

These are part of the pattern, not optional extras. A port that
ships the checker without them ships the misrepresentation risk the
checker's appearance creates.

1. **Coverage denominators, always visible.** "Clean" over 9
   documents of 350 must never display like clean over 350. Every
   report line carries counts (anchors, edges, participating docs);
   dashboards show anchored/total.
2. **Mutation-test the checker itself, red/green, on every
   substantive change.** Demote a real anchor, confirm the expected
   transitive red, revert, confirm green. A gate that has never been
   seen red is not known to work — this repository's vacuously-green
   gate is the standing proof.
3. **Pair the ledger with a mutation gate for verifiers.** The
   ledger checks that claims cite premises; the mutation gate checks
   that *verification scripts actually consume them* (a verifier
   whose verdict is invariant under premise mutation verifies
   nothing). The two are complementary halves: citation integrity
   and evidential sensitivity. Neither substitutes for the other.
4. **Sampled adversarial audit of attestations.** On a schedule, or
   probabilistically per change: pick anchors, read the providing
   document, ask "does the prose meet the declared status's burden?"
   This is the financial-audit sampling step — the only defense
   against dishonest or drifted attestations, and it is human.
5. **Completeness reviews.** The ledger cannot see undeclared edges.
   Reviews of new work include premise-hunting: "what does this
   actually assume that it does not declare?" Repercussion audits
   (this repo, ERRATA E16) are the corrective form of the same
   activity.
6. **Provenance on attestations** where the format allows: who or
   what asserted the status, and when. An attestation without an
   attester cannot be audited or aged.
7. **Statuses travel with retrieval.** In RAG or search contexts,
   the chunk's provenance metadata should carry the providing doc's
   status, so a retrieved conjecture cannot present as settled
   simply because the prose reads confidently.

## 6. What the pattern earned in practice (evidence, not promises)

From this repository's correction campaign — kept here so ports can
calibrate expectations:

- The forced single-status-per-claim rule makes headline/hedge
  divergence *inexpressible*: the March-2026 propagation incident
  (claim traveled, caveat did not, for six weeks) is caught on day
  one, mechanically.
- Scoreboard integration caught real rot on first contact: two
  scorecard rows still claimed "Class 5 (exact)" months after their
  premises were demoted.
- The mutation gate — not the ledger — caught the tautological and
  observation-inverted verifiers. Ledger-only deployments would have
  green-lit both. This division of labor is the strongest argument
  for §5.3.

## 7. Minimum viable port

1. Choose the carrier channel for your format.
2. Write the status vocabulary *with attestation burdens* (start
   from this repo's eight; add `fitted` even if you think you don't
   need it — you do).
3. Implement the four checks (graph algorithms, O(V+E); ~150 lines
   in any language).
4. Print coverage denominators in every report.
5. Red/green test the checker before first real use.
6. Anchor your ten most load-bearing documents; ratchet from there.
7. Write §1 of this document, adapted, at the top of yours — the
   trust boundary is the documentation's headline, not its appendix.
