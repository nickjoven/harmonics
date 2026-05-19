# Runbook-prompt — initialize an authoritative NUC ket store workspace

**Audience:** a CI job, a scheduled Claude agent, or a human operator.
**Goal:** turn a fresh long-lived host (the NUC) into the *authoritative*
ket-store workspace for this repo, idempotently.
**Complements** `.github/workflows/substrate-maintenance.yml` (which owns
*ongoing* drift reconcile on `main`). This runbook owns *one-time host
initialization*. They share one binary contract: `KET_BIN`.

---

## Why this exists (the CAS rationale — read first)

This repo's derivations are guarded by a **content-addressed
provenance substrate** (`.ket/`): every tracked derivation file is
BLAKE3-hashed into `.ket/cas/<cid>`, its CID logged in `.ket/log`,
with a Merkle DAG of lineage. A **pre-commit hook**
(`scripts/drift/run_all.py --stop-on-fail`) **refuses any commit**
where a tracked file's current BLAKE3 ≠ its last-logged CID.

Consequence, and the reason a ket store is load-bearing at all:
**you cannot land an edited derivation without `ket put`-ing its new
bytes into the CAS and adding a DAG reconciliation node.** That
requires the canonical BLAKE3 path — the `ket` binary (or the
`blake3` module for read-only verification). A host with neither
can *write* derivations but can never *commit* them.

"Authoritative NUC store" means: the NUC holds the canonical working
`.ket/` and the ket toolchain durably; CI is the *integrity verifier*
(not the owner); other machines (e.g. the Moonlight client) are thin
and do not arbitrate substrate truth. Git remains the code SOT; the
NUC is the substrate SOT host.

---

## Invariants (assert, don't assume — Auditor)

1. `KET_BIN` resolves to a `ket` built from `nickjoven/ket` **Tier-1**
   (`cargo build --release -p ket-cli`; *exclude* `ket-py` — it needs
   `libpython` and is not in the minimum stack).
2. `python3 -c "import blake3"` succeeds, and
   `python3 scripts/drift/verify_cas.py` reports **all** CAS entries OK
   — this proves the hashing path is bit-identical to `ket` (canonical,
   not algorithm drift). Never proceed if this fails.
3. The authoritative `.ket/` is the one tracked in this git repo. Do
   **not** initialize a second store over it; do not point handoff /
   experiment stores at it (use an isolated `--home` outside the repo).
4. No Dolt/`ket-sql` runtime is required (Tier-1). Dolt is a deferred,
   additive layer; its absence is expected, not an error.

---

## Procedure (idempotent — each step is a no-op if already satisfied)

### 1. blake3 (read/verify path)

```sh
python3 -c "import blake3" 2>/dev/null && echo "blake3 ok" || {
  # If pip exists:  pip install --user blake3
  # Pip-less host (PEP 668 / no ensurepip), e.g. the NUC: extract the
  # official manylinux wheel into user site-packages. Get the current
  # cp<ver> x86_64 manylinux URL from https://pypi.org/pypi/blake3/json
  python3 - <<'PY'
import urllib.request,zipfile,io,os,sys,json
s=os.path.expanduser(f"~/.local/lib/python{sys.version_info.major}.{sys.version_info.minor}/site-packages")
os.makedirs(s,exist_ok=True)
d=json.load(urllib.request.urlopen("https://pypi.org/pypi/blake3/json",timeout=60))
tag=f"cp{sys.version_info.major}{sys.version_info.minor}"
u=next(r["url"] for r in d["releases"][d["info"]["version"]]
       if tag in r["filename"] and "manylinux" in r["filename"] and "x86_64" in r["filename"])
zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(u,timeout=60).read())).extractall(s)
PY
}
```

### 2. ket Tier-1 binary

```sh
command -v ket >/dev/null || {
  command -v cargo >/dev/null || \
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \
      | sh -s -- -y --profile minimal --default-toolchain stable
  . "$HOME/.cargo/env"
  SRC="${KET_SRC:-/tmp/ket-src}"
  [ -d "$SRC" ] || git clone --depth 1 https://github.com/nickjoven/ket.git "$SRC"
  ( cd "$SRC" && cargo install --path ket-cli --root "$HOME/.local" --force --locked )
}
export KET_BIN="$HOME/.local/bin/ket"
"$KET_BIN" --version
```
`~/.local/bin` must be on `PATH` for the drift hooks/scripts (it is in
the active hook shell; durable in `~/.zshenv` via rustup). The CI
analogue caches this binary — see `substrate-maintenance.yml`.

### 3. (optional, additive) catbus — handoff tooling

```sh
command -v catbus >/dev/null || {
  . "$HOME/.cargo/env"
  D="${CATBUS_DIR:-$HOME/code/catbus}"
  [ -d "$D" ] || git clone --depth 1 https://github.com/nickjoven/catbus.git "$D"
  cargo install --path "$D" --root "$HOME/.local" --force --locked
}
```
Note: a real cross-machine handoff is **subgraph-driven** — ship
`ket export <root>` of the relevant DAG subgraph, not a single-node
catbus packet (single-node packets cannot carry "the whole thing").

### 4. Adopt & verify the authoritative store (do NOT re-init)

```sh
test -d .ket/cas || { echo "::error:: no .ket/ in repo — wrong cwd"; exit 1; }
python3 scripts/drift/verify_cas.py            # MUST be all-OK (invariant 2)
timeout 90 python3 scripts/drift/run_all.py --stop-on-fail
```

### 5. Reconcile only if drift, then it's authoritative

```sh
python3 scripts/drift/session_status.py
python3 scripts/maintenance/reconcile_substrate.py   # idempotent: no-op if clean
```

The host is now an authoritative ket workspace: it can verify the
substrate, reconcile drift via the canonical binary, and therefore
land derivation commits through the pre-commit gate.

---

## Failure handling

- `verify_cas` not all-OK → **stop**. The hashing path is wrong; do
  not write to the substrate (silent algorithm drift previously
  corrupted CAS entries — see `scripts/ket.py` / `_hash.py`).
- `run_all.py` fails on a non-drift check (manifest, orphan,
  fitted-correction) → **stop and escalate**; these need human
  judgment, exactly as the CI workflow declines to auto-fix them.
- ket build fails on `ket-py`/`libpython` → expected; ensure the
  build is scoped to `-p ket-cli` / `--path ket-cli` only.

## Cross-references

- `.github/workflows/substrate-maintenance.yml` — ongoing CI reconcile
  (the recurring counterpart to this one-time init).
- `scripts/maintenance/reconcile_substrate.py` — the sanctioned
  drift-reconcile (shells out to `ket`; never reimplements hashing).
- `scripts/drift/run_all.py`, `verify_cas.py`, `_hash.py` — the gate
  and the read/verify path.
