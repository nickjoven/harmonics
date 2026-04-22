"""
BLAKE3 helper with graceful environment fallback.

Resolution order:
  1. `blake3` Python package (pip install --user blake3) — portable,
     works in claude.ai web and CI without a Rust toolchain.
  2. `ket` binary via KET_BIN env var or PATH — canonical substrate
     path; also writes log entries.
  3. Clear error — we refuse to fall back to SHA-256 or any other
     hash, because silent algorithm drift is what originally
     corrupted CAS entries `8e23247fd488` and `ba196964d683`.

The blake3 package produces bit-identical CIDs to the `ket` binary.
This was verified by hashing the same input through both on
2026-04-22: "drift-test blob" → 8925373ac006b898c46d57070dc05701f75fe93cef3c0bb3c51b2a71c2ad903b.
"""

import os
import shutil
import subprocess
from pathlib import Path
from typing import Optional


class HashingUnavailable(RuntimeError):
    pass


def _have_blake3_module() -> bool:
    try:
        import blake3  # noqa: F401
        return True
    except ImportError:
        return False


def _ket_binary() -> Optional[str]:
    for candidate in (os.environ.get("KET_BIN"), shutil.which("ket")):
        if candidate and Path(candidate).is_file() and os.access(candidate, os.X_OK):
            return candidate
    return None


def hash_bytes(data: bytes) -> str:
    """Return the BLAKE3 CID of `data` as a 64-char lowercase hex string."""
    if _have_blake3_module():
        import blake3
        return blake3.blake3(data).hexdigest()
    binary = _ket_binary()
    if binary:
        result = subprocess.run(
            [binary, "put", "-"],
            input=data,
            capture_output=True,
            check=True,
        )
        # Binary writes to CAS as a side-effect; caller should not depend
        # on that here. For pure hashing, prefer the blake3 module.
        return result.stdout.decode().strip().split()[0]
    raise HashingUnavailable(
        "Neither the `blake3` Python package nor the `ket` binary is "
        "available. Install blake3 with `pip install --user blake3` or "
        "set KET_BIN to the ket executable."
    )


def hash_file(path: Path) -> str:
    return hash_bytes(Path(path).read_bytes())


def environment_summary() -> str:
    have_module = _have_blake3_module()
    binary = _ket_binary()
    bits = []
    if have_module:
        bits.append("blake3 module")
    if binary:
        bits.append(f"ket binary ({binary})")
    return ", ".join(bits) if bits else "NONE — writes will fail"
