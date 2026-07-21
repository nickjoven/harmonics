# Experiments: retrodiction harness (canon.d#11 shadow gate)

Retrodiction is the acceptance test for the v2 substrate design
([canon.d#11](https://github.com/nickjoven/canon.d/issues/11)): replay a past
weakening event (the 2026-04 bare-K=1 demotion, harmonics#263) against the
committed projections and check that grounded-closure + divergence detection
rediscovers what the manual audit found months later. Evaluator-zone only:
reads `docs/*.json` projections, never writes to the ledger.

Run the self-test (synthetic 5-node chain, must pass):

    python3 scripts/experiments/retrodict.py --self-test

Run against the real corpus, with weakening fixtures:

    python3 scripts/experiments/retrodict.py --report
    python3 scripts/experiments/retrodict.py --fixtures FILE --report [--json]

Fixture JSON schema: `{"events": [{"id": "...", "demoted": [{"node": "doc_id"}]}],
"expected_findings": [{"doc": "doc_id", "stale": true, "implied_by": "event-id"}]}`
(`expected_findings` optional; when present the run is scored found/missed/extra).
`kind_table.json` is the surface-kind -> primitive compilation table (commitment 3).
