# Premise Ledger

Machine-readable dependency anchors for the derivation corpus,
checked by `scripts/drift/check_premises.py`.

## Schema

Anchors are HTML comments (parser-safe, invisible to renderers and
retrieval chunkers), one per line, anywhere in a doc:

```
<!-- provides: <name> status=<status> -->
<!-- premises: <name>@<providing-doc-basename>, <name2>@<doc2> -->
```

- `<name>`: kebab-case, globally unique per corpus — **one name, one
  providing doc**. Two docs providing the same name is a hard error
  (rival conventions must collide, not fork).
- `status` vocabulary:
  - `axiom` — assumed, stated as such
  - `definition` — true by construction; makes no empirical claim
  - `proven` — proof in this doc, checked
  - `derived` — follows from premises in this doc
  - `imported` — external mathematics/data, cited
  - `conditional` — derivation valid, but ≥1 premise is not settled
  - `conjectured` — asserted; no derivation exists
  - `fitted` — value obtained from observation; not a prediction

## Propagation rule

A doc may declare `provides: X status=proven|derived` **only if** no
premise it cites resolves to `conjectured`, `fitted`, or
`conditional`. Otherwise the strongest allowed status is
`conditional` (or weaker). The checker enforces this transitively —
demoting one anchor flags every downstream `proven`/`derived` that
rests on it.

## Checks (all graph algorithms, O(V+E))

1. **Resolution** — every `premises:` entry names an anchor that
   exists in the named doc.
2. **Uniqueness** — no name has two providers.
3. **Propagation** — the rule above, transitively.
4. **Cycles** — the premise graph is acyclic.

## MANIFEST rows

Scorecard rows in `MANIFEST.yml` may declare a `premises:` list of
the same `name@doc` entries. A row whose premises resolve to an
unsettled anchor may not claim `Class 5` / `exact` in its
`closure_status` unless the status text itself carries the hedge
(conditional / retracted / reference / imported / fitted). This is
the repercussive-feedback guard: a demotion at a providing doc
reaches the scorecard mechanically.

## Ratchet policy

Enforcement is incremental: docs that declare anchors are checked;
docs without anchors are not (yet) required to have them. Backfill
order: spine docs first. A doc touched by any correction batch gets
anchors as part of the edit.
