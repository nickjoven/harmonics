#!/usr/bin/env python3
"""
run_engine.py — deterministic engine runner with output-CID pinning.

The framework's derivation scripts are *engines*: pure, deterministic
computations whose stdout is a result an LLM/HITL session should quote
*from a real run*, not estimate. This runner executes a whitelisted
engine (named in `engines.yaml`), computes the BLAKE3 CID of its stdout,
and compares it to the pinned canonical CID in `engines.lock.json`. A
match proves the result is bit-identical to the sealed canonical run —
"run the code AND verify it didn't drift from canonical." That is what
removes the ambiguity: the session cites a verified number, not a guess.

`run` is READ-ONLY by default (#328 Card 10: checking never mutates):
it executes the engine, hashes, compares, and reports {cid, expect_cid,
matches} — it writes NOTHING (no CAS write, no ledger line). Sealing is
explicit: `run --seal` seals stdout in the ket CAS as before, and `pin`
always seals internally, because a pin without a sealed canonical is
meaningless.

Whitelist: only engines listed in `engines.yaml` run; `cmd` is
git-tracked. No arbitrary command execution.

Separation of concerns (like Cargo.toml / Cargo.lock):
  - engines.yaml      human-authored: cmd, what it computes, timeout
  - engines.lock.json generated lock (written only by `pin`):
      pins:    name -> canonical expect_cid (BLAKE3 of stdout)
      scripts: name -> BLAKE3 of the engine's script file at pin time

The `scripts` map backs the FATAL pin gate (#328 Card 5,
scripts/drift/check_engine_pins.py): a changed engine script invalidates
its pin until the engine is reviewed and re-pinned.

Hashing uses the canonical BLAKE3 path (scripts/drift/_hash.py: blake3
module or the ket binary) — never SHA-*, because silent algorithm drift
once corrupted CAS entries (see scripts/ket.py).

Usage:
  python3 scripts/engines/run_engine.py list
  python3 scripts/engines/run_engine.py run  <name> [--json] [--seal]
  python3 scripts/engines/run_engine.py info <name>
  python3 scripts/engines/run_engine.py pin  <name> [--all]   # set/refresh pins (seals)

Exit codes for `run`: 0 = ran and matches pin (or unpinned); 1 = ran but
CID != pin (DRIFT); 2 = engine error / environment error.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
REGISTRY = HERE / "engines.yaml"
LOCKFILE = HERE / "engines.lock.json"
KET_HOME = ROOT / ".ket"

sys.path.insert(0, str(ROOT / "scripts" / "drift"))
from _hash import hash_bytes, hash_file, HashingUnavailable  # noqa: E402

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


def load_registry() -> dict:
    if yaml is None:
        raise SystemExit("PyYAML required: pip install --user pyyaml")
    data = yaml.safe_load(REGISTRY.read_text()) or {}
    return data.get("engines", {})


def load_lock() -> dict:
    """The full lock: {'pins': {name: output_cid},
    'scripts': {name: blake3 of engine script at pin time}}."""
    if LOCKFILE.exists():
        data = json.loads(LOCKFILE.read_text())
        return {"pins": data.get("pins", {}),
                "scripts": data.get("scripts", {})}
    return {"pins": {}, "scripts": {}}


def load_pins() -> dict:
    return load_lock()["pins"]


def save_lock(lock: dict) -> None:
    LOCKFILE.write_text(
        json.dumps(
            {
                "pins": dict(sorted(lock.get("pins", {}).items())),
                "scripts": dict(sorted(lock.get("scripts", {}).items())),
            },
            indent=2,
        )
        + "\n"
    )


def engine_script(e: dict) -> Path | None:
    """The engine's script file: the first `cmd` token after the
    interpreter that resolves to a file under the repo root. This is the
    file whose BLAKE3 is recorded in the lock's `scripts` map and gated
    by scripts/drift/check_engine_pins.py."""
    for tok in e.get("cmd", [])[1:]:
        p = ROOT / tok
        if p.is_file():
            return p
    return None


def _ket_put(data: bytes) -> str | None:
    """Seal bytes in the CAS via the ket binary (stdin). Best-effort; the
    CID is logged with path '-' (drift checker ignores stdin puts)."""
    ket = os.environ.get("KET_BIN") or shutil.which("ket")
    if not ket:
        return None
    try:
        r = subprocess.run(
            [ket, "--home", str(KET_HOME), "put", "-"],
            input=data, capture_output=True, check=True,
        )
        return r.stdout.decode().split()[0]
    except Exception:
        return None


def run_engine(name: str, seal: bool = False) -> dict:
    """Execute a whitelisted engine and VERIFY its output against the pin.

    Read-only by default (#328 Card 10): computes the stdout's BLAKE3 CID
    and compares it to the pinned canonical CID — no CAS write, no ledger
    line. Pass seal=True (CLI: `run --seal`, or the `pin` command) to also
    seal the stdout in the ket CAS."""
    engines = load_registry()
    if name not in engines:
        return {"name": name, "ok": False,
                "error": f"unknown engine; not listed in {REGISTRY.name}"}
    e = engines[name]
    cmd = e["cmd"]
    timeout = int(e.get("timeout", 120))
    env = {**os.environ, "PYTHONPATH": str(ROOT)}
    try:
        proc = subprocess.run(
            cmd, cwd=ROOT, env=env, capture_output=True, timeout=timeout
        )
    except FileNotFoundError as ex:
        return {"name": name, "ok": False, "error": f"cmd not found: {ex}"}
    except subprocess.TimeoutExpired:
        return {"name": name, "ok": False, "error": f"timeout after {timeout}s"}

    out = proc.stdout
    try:
        cid = hash_bytes(out)
    except HashingUnavailable as ex:
        return {"name": name, "ok": False, "error": str(ex)}

    sealed = _ket_put(out) if seal else None
    expect = load_pins().get(name)
    matches = (cid == expect) if expect else None
    return {
        "name": name,
        "ok": proc.returncode == 0,
        "computes": e.get("computes", ""),
        "cmd": cmd,
        "returncode": proc.returncode,
        "cid": cid,
        "expect_cid": expect,
        "matches": matches,
        "sealed_in_cas": bool(sealed),
        "output": out.decode("utf-8", "replace"),
        "stderr": proc.stderr.decode("utf-8", "replace")[:2000],
    }


def _verdict(r: dict) -> str:
    if not r.get("ok", False) and r.get("returncode") not in (0, None):
        return "ENGINE-ERROR"
    if r.get("expect_cid") is None:
        return "UNPINNED"
    return "MATCH ✓" if r.get("matches") else "DRIFT ✗"


def cmd_list(_args) -> int:
    engines, pins = load_registry(), load_pins()
    print(f"{len(engines)} engine(s) in {REGISTRY.name}:\n")
    for name in sorted(engines):
        pinned = "pinned" if name in pins else "UNPINNED"
        print(f"  {name:<28} [{pinned}]  {engines[name].get('computes','')}")
    return 0


def cmd_info(args) -> int:
    engines = load_registry()
    if args.name not in engines:
        print(f"unknown engine: {args.name}", file=sys.stderr)
        return 2
    e = dict(engines[args.name])
    e["expect_cid"] = load_pins().get(args.name)
    print(json.dumps({args.name: e}, indent=2))
    return 0


def cmd_run(args) -> int:
    r = run_engine(args.name, seal=args.seal)
    if "error" in r and not r.get("ok"):
        if args.json:
            print(json.dumps(r, indent=2))
        else:
            print(f"{args.name}: ERROR — {r['error']}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(r, indent=2))
    else:
        v = _verdict(r)
        print(f"engine:   {r['name']}")
        print(f"computes: {r['computes']}")
        print(f"cid:      {r['cid']}  [{v}]")
        if r["expect_cid"] and not r["matches"]:
            print(f"expected: {r['expect_cid']}")
        sealed = "yes (ket CAS)" if r["sealed_in_cas"] else \
            "no (verify-only; pass --seal to seal)"
        print(f"sealed:   {sealed}")
        print("--- output ---")
        print(r["output"], end="" if r["output"].endswith("\n") else "\n")
    if r["expect_cid"] and not r["matches"]:
        return 1
    return 0


def cmd_pin(args) -> int:
    """Pin an engine: run it, seal its stdout in the CAS (a pin without a
    sealed canonical is meaningless), and record BOTH the output CID and
    the BLAKE3 of the engine's script file (the pin-gate baseline)."""
    engines = load_registry()
    names = sorted(engines) if args.all else [args.name]
    if not args.all and args.name not in engines:
        print(f"unknown engine: {args.name}", file=sys.stderr)
        return 2
    lock = load_lock()
    pins, scripts = lock["pins"], lock["scripts"]
    rc = 0
    for name in names:
        script = engine_script(engines[name])
        if script is None:
            print(f"  {name}: NOT pinned (no engine script found in cmd)")
            rc = 2
            continue
        r = run_engine(name, seal=True)
        if not r.get("ok") and r.get("returncode") not in (0, None):
            print(f"  {name}: NOT pinned (engine error: {r.get('error','rc!=0')})")
            rc = 2
            continue
        pins[name] = r["cid"]
        scripts[name] = hash_file(script)
        print(f"  {name}: pinned  -> {r['cid']}")
        print(f"  {name}: script  -> {scripts[name]}  ({script.relative_to(ROOT)})")
    save_lock(lock)
    print(f"wrote {LOCKFILE.name}")
    return rc


def main() -> int:
    p = argparse.ArgumentParser(description="Deterministic engine runner.")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list").set_defaults(fn=cmd_list)
    pr = sub.add_parser("run"); pr.add_argument("name"); pr.add_argument("--json", action="store_true"); pr.add_argument("--seal", action="store_true", help="also seal stdout in the ket CAS (default: verify-only, writes nothing)"); pr.set_defaults(fn=cmd_run)
    pi = sub.add_parser("info"); pi.add_argument("name"); pi.set_defaults(fn=cmd_info)
    pp = sub.add_parser("pin"); pp.add_argument("name", nargs="?"); pp.add_argument("--all", action="store_true"); pp.set_defaults(fn=cmd_pin)
    args = p.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
