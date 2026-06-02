# Stack coordination & release runbook

The ket stack is five repos we own. This file documents the dependency
arrows, the version anchors, and the ritual for cutting a new version
without leaving consumers pinned at a stale or off-`main` commit.

## Dependency arrows

```
            ┌─────────────────────────── ket ───────────────────────────┐
            │  ket-cas · ket-dag · ket-sql · ket-cdom · ket-mcp           │
            │  (CAS + Merkle DAG + Dolt SQL + canonical-doc + MCP)        │
            └──┬──────────────┬──────────────┬───────────────┬───────────┘
               │              │              │               │
            canon.d        k-stack        catbus      harmonics-seed
          (canonical-   (MCP server)   (handoff      (seeds the DAG
           doc layer,                   packer)       via canon.d)
           ket optional                                    │
           feature)                                        │
               │                                           │
               └──────────────► k-stack also pins ◄────────┘
                                canon.d
```

Everything points **at ket**. `canon.d` is a *downstream consumer* of
ket (ket is an optional feature of canon.d, not the reverse). `k-stack`
pins both ket and canon.d. `harmonics-seed` (the `seed/` crate) reaches
ket through canon.d.

## Version anchors

Two tags are the whole interface. Every consumer pins one or both.

| Repo     | Tag      | Commit    | Pinned by                                  |
|----------|----------|-----------|--------------------------------------------|
| ket      | `v0.2.0` | `3530ad5` | canon.d, k-stack, catbus, harmonics-seed   |
| canon.d  | `v0.1.0` | `0a18a32` | k-stack, harmonics-seed                     |

All consumers use the single canonical source URL
`https://github.com/nickjoven/ket.git` and pin with `tag = "v0.2.0"`
(not a rev, not a branch). There are **zero rev-pins** in the stack —
keep it that way.

`harmonics` also vendors ket as a git **submodule** (`ket/`), pinned to
the same `v0.2.0` commit `3530ad5`. The `seed/Cargo.toml` carries a
`[patch."https://github.com/nickjoven/ket.git"]` redirecting `ket-cas`
and `ket-dag` to the local `../ket/ket-cas` / `../ket/ket-dag` for
in-tree development; the tag is what a clean checkout resolves.

## Edge kinds (the 0.2.0 interface addition)

ket 0.2.0 added epistemic edge kinds to the DAG: `grounds` / `derives` /
`proposes` (default `derives`), validated by `validate_edge_kind` and
stored in `dag_edges.edge_kind VARCHAR(20)`. The derivation-graph
generator and the MCP write-paths surface these — see the typed-edge
work in `scripts/build_derivation_graph.py` and the `edge_kind` schema
fields in k-stack `ket_store` / ket-mcp `ket_store_reasoning`.

## Cutting a new version

Releases go **in dependency order, ket-first**. A consumer must never
pin a tag that doesn't yet exist or points off `main`.

1. **ket** — land changes on `main`. Tag the *merge commit on `main`*:
   ```sh
   git -C ../ket checkout main && git -C ../ket pull
   git -C ../ket tag -a v0.3.0 -m "ket 0.3.0" && git -C ../ket push origin v0.3.0
   ```
   Verify the tag is on `main`, not a tree-identical off-`main` commit:
   ```sh
   git -C ../ket merge-base --is-ancestor v0.3.0 main && echo "on main"
   ```

2. **canon.d** — bump its ket deps to `tag = "v0.3.0"`, land on `main`,
   then tag canon.d (e.g. `v0.2.0`) at its merge commit and push.

3. **k-stack, catbus** — bump ket (and, for k-stack, canon.d) to the new
   tags. `cargo check` each. Land on `main`.

4. **harmonics** — bump deps in `seed/Cargo.toml`, then advance the `ket`
   submodule pointer to the new tag commit:
   ```sh
   git -C ket fetch && git -C ket checkout 3530ad5   # the v0.3.0 commit
   git add ket && git commit -m "Bump ket submodule to v0.3.0"
   ```

## Rollback

Tags are movable but moving a *published* tag is a force-push everyone
must re-fetch — avoid it. Prefer cutting `v0.3.1`. If a tag was placed
on the wrong commit before anyone consumed it, the recorded fix pattern
is:

```sh
git -C ../ket tag -f v0.3.0 <correct-commit>
git -C ../ket push --force origin v0.3.0
```

To roll a consumer back, re-pin its `tag = "..."` to the prior anchor
and `cargo update -p <crate>`; for harmonics, reset the submodule
pointer and commit.

## Invariants to keep

- One source URL (`…/ket.git`), tag-pinned, no revs, no branches.
- Tags live on `main`.
- Bump in dependency order: ket → canon.d → (k-stack, catbus) → harmonics.
- The submodule commit and the `tag = "vX.Y.Z"` pins agree.
