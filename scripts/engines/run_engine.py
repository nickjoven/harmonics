#!/usr/bin/env python3
"""
run_engine.py — deterministic engine runner with output-CID pinning.

The framework's derivation scripts are *engines*: pure, deterministic
computations whose stdout is a result an LLM/HITL session should quote
*from a real run*, not estimate. This runner executes a whitelisted
engine (named in `engines.yaml`), seals its stdout in the ket CAS
(content-addressed, dedup-free), and compares the result's BLAKE3 CID to
the pinned canonical CID in `engines.lock.json`. A match proves the
result is bit-identical to the sealed canonical run — "run the code AND
verify it didn't drift from canonical." That is what removes the
ambiguity: the session cites a verified number, not a guess.

Whitelist: only engines listed in `engines.yaml` run; `cmd` is
git-tracked. No arbitrary command execution.

Separation of concerns (like Cargo.toml / Cargo.lock):
  - engines.yaml      human-authored: cmd, what it computes, timeout
  - engines.lock.json generated pins: name -> canonical expect_cid

Hashing uses the canonical BLAKE3 path (scripts/drift/_hash.py: blake3
module or the ket binary) — never SHA-*, because silent algorithm drift
once corrupted CAS entries (see scripts/ket.py).

Usage:
  python3 scripts/engines/run_engine.py list
  python3 scripts/engines/run_engine.py run  <name> [--json]
  python3 scripts/engines/run_engine.py info <name>
  python3 scripts/engines/run_engine.py pin  <name> [--all]   # set/refresh pins

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
from _hash import hash_bytes, HashingUnavailable  # noqa: E402

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


def load_registry() -> dict:
    if yaml is None:
        raise SystemExit("PyYAML required: pip install --user pyyaml")
    data = yaml.safe_load(REGISTRY.read_text()) or {}
    return data.get("engines", {})


def load_pins() -> dict:
    if LOCKFILE.exists():
        return json.loads(LOCKFILE.read_text()).get("pins", {})
    return {}


def save_pins(pins: dict) -> None:
    LOCKFILE.write_text(
        json.dumps({"pins": dict(sorted(pins.items()))}, indent=2) + "\n"
    )


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


def run_engine(name: str, seal: bool = True) -> dict:
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
    r = run_engine(args.name)
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
        print(f"sealed:   {'yes (ket CAS)' if r['sealed_in_cas'] else 'no'}")
        print("--- output ---")
        print(r["output"], end="" if r["output"].endswith("\n") else "\n")
    if r["expect_cid"] and not r["matches"]:
        return 1
    return 0


def cmd_pin(args) -> int:
    engines = load_registry()
    names = sorted(engines) if args.all else [args.name]
    if not args.all and args.name not in engines:
        print(f"unknown engine: {args.name}", file=sys.stderr)
        return 2
    pins = load_pins()
    rc = 0
    for name in names:
        r = run_engine(name, seal=True)
        if not r.get("ok") and r.get("returncode") not in (0, None):
            print(f"  {name}: NOT pinned (engine error: {r.get('error','rc!=0')})")
            rc = 2
            continue
        pins[name] = r["cid"]
        print(f"  {name}: pinned -> {r['cid']}")
    save_pins(pins)
    print(f"wrote {LOCKFILE.name}")
    return rc


def main() -> int:
    p = argparse.ArgumentParser(description="Deterministic engine runner.")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list").set_defaults(fn=cmd_list)
    pr = sub.add_parser("run"); pr.add_argument("name"); pr.add_argument("--json", action="store_true"); pr.set_defaults(fn=cmd_run)
    pi = sub.add_parser("info"); pi.add_argument("name"); pi.set_defaults(fn=cmd_info)
    pp = sub.add_parser("pin"); pp.add_argument("name", nargs="?"); pp.add_argument("--all", action="store_true"); pp.set_defaults(fn=cmd_pin)
    args = p.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
