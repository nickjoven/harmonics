# /substrate-audit — adversarial audit, revision, and advancement over the sealed substrate

You are adversarially auditing the harmonics derivation corpus, revising what fails, and advancing what stands. The substrate, not your context and not your prior, is the authority. This session is also an instrument: you are measuring whether the substrate's surfaces are sufficient, and your telemetry feeds the next tooling round. $ARGUMENTS

## Bootstrap (before any audit work)

1. `corpus_health` first. If non-clean (corrupt > 0, drift > 0), stop and repair or report; never audit a dirty substrate.
2. Record the baseline, verbatim, for end-of-session deltas: `class_query` (no args) coverage totals; superseded-doc count and `rule8_flags` from `docs/corpus-index.json`; claim count and the top-10 table by `corroboration_frontier` (`claim_search`, `min_corroboration: 5`); `python3 scripts/drift/check_downstream_resolution.py` output; `has_lineage` count.
3. Open the session read-log: append one JSON line per substrate retrieval to `.claude/session-read-log.jsonl` (fields: tool, key, cid if any, t). Uncommitted; it is the working prototype for issue #295, and its summary is part of your report.

## Assertion discipline

- Label every corpus assertion in your prose: `[read: <tool> <key-or-cid>]` retrieved fresh this session at the resolution asserted; `[cached]` held from earlier this session; `[speculative]` not substrate-backed. An unlabeled corpus assertion is a protocol violation; correct it when noticed.
- Never characterize a doc without `resolve` first. Superseded docs are historical sources, only reachable knowingly (`historical: true`).
- Quantitative claims cite proposition CIDs (`claim_get`), never remembered values. MANIFEST rows via `manifest_claim`; treat `source_frontier_warning` as a finding.

## The adversarial loop

For each target: one visible line `HYPOTHESIS: … TEST: …`, then run the test, then `VERDICT: …` with evidence. Work in this order unless directed otherwise.

1. **Support inversion.** `claim_search` across the major subjects. Any claim with `corroboration_frontier < corroboration / 2` is presumptively over-stated: attack whether the frontier support alone establishes it, or the strength was living in superseded docs.
2. **Divergence queue.** Every `check_downstream_resolution` entry is a pre-found target; audit it to ground truth.
3. **Class 4 docket.** `class_query {class: 4}`: each is a self-declared unresolved judgment with named hypotheses. Attack the conditionality: can any H be discharged or refuted from the current substrate?
4. **Registry consistency.** `manifest_claim` over every name: sources must resolve frontier; computed values must have a matching sealed claim in `claims-index` (witness agreement). Mismatches are findings.
5. **Ingest coverage.** Sample the 189 unstructured frontier docs: claims the ratio route missed (prose-stated quantities, non-ratio claims). Product: route-improvement proposals or write-for-ingest edits, not hand-waving.
6. **Deep chain audit** (at least one): pick a Class 5 claim, walk its full support via `graph_walk {direction: deps}` and `claim_get`; every load-bearing step that is prose-only (no committed edge, no sealed claim) is a finding.
7. **Engine verification.** `list_engines`, then `run_engine` every pinned engine: `matches: false` (output diverges from its sealed canonical CID) is a finding of the highest class, a computation the corpus cites no longer reproduces. Where a deep-chain step (target 6) cites a numeric result an engine covers, recompute rather than trust.
8. **Global selection accounting** (the look-elsewhere ledger; a per-claim loop is structurally blind to this, so it is an explicit target). Maintain or refresh the trials ledger: enumerate every observable the program has EVER attempted, using the graveyard the substrate preserved (Class 1-3 docs, `bare_k1_identities`, retracted and declined claims, closed null arcs like koide), alongside the survivors; for each surviving Class 5 construction, estimate the admissible candidate space (how many low-complexity rationals the construction could have produced); report the trials-corrected picture of the surviving set. Output is a dossier for owner review and, when mature, a standalone derivation doc (`selection_accounting.md`), because it is the single highest-credibility artifact the program can produce before external data arrives. Aggregate honestly: attempted-and-killed counts are evidence FOR the survivors only if the counting includes everything.

Before acting on any finding that would change substrate content, spawn one subagent skeptic instructed to refute it. Only surviving findings go forward.

Out of audit scope by design: the substrate posit's abductive standing (why coupled oscillators at all) is foundational assessment, owed a dedicated theory session, not an auditor's pass; note it if touched, do not adjudicate it.

## Revision rules

- Mechanical fixes (broken refs, text contradicted by substrate, missing lineage): branch, fix, reseal (`KET_HOME=.ket ket put <file>`), verify with local projection regen, PR. On-touch policy: any doc you touch gains `## Lineage` if it lacks one.
- Supersessions: `declare_succession` only. Never banners, never stamps; content changes only when the work itself changes (canon.d#11 commitment 8).
- Class/status judgments: never committed unilaterally. Produce dossier cards (claim, current state, contradiction if any, recommendation, effort) for owner ruling.
- Advancing theory: author new claims in ratio-extractable form (`subject = num/den` on its own line), with `## Lineage` from birth, so the next ingest seals them with no route changes. State the expected new claim subjects in your report.

## Debugging protocol

- On any surprise (tool output contradicts your expectation): stop; log `SURPRISE: expected X, got Y`; classify substrate-bug | stale-projection | genuine-finding. Substrate bugs are findings; file them.
- If the surfaces cannot answer a question and you fall back to raw file reads, log `BYPASS: <the question>`. Bypass count is the primary surface-debt metric; each unique bypass is a candidate new tool.
- If a tool errors or a projection is stale relative to the working tree, say so in the report; do not silently regenerate and continue.

## End-of-session telemetry (report all, with deltas vs bootstrap baseline)

```
SUBSTRATE PERFORMANCE
  reads by tool (from read-log), total | bypasses: n + the questions
  assertions: read=… cached=… speculative=…
  speculative later verified: n | contradicted on verification (fabrication catches): n
COVERAGE DELTAS
  classified, has_lineage, superseded count, divergence queue before -> after
  corroboration_frontier changes on every touched claim
WORK PRODUCT
  findings: confirmed / refuted-by-skeptic | PRs opened | dossier cards | theory docs authored + expected next-ingest claims
CHAIN
  if content changed: re-ingest owed (canon-demo --prior-heads sync_cost/ingest/report.json); expected heads_superseded
```

Append the telemetry as one JSON line to `.claude/session-telemetry.jsonl` (uncommitted) so sessions are comparable over time.
