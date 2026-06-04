#!/usr/bin/env python3
"""
preview_server.py — long-lived local preview server with auto-rebuild.

Watches sync_cost/derivations/*.md for changes and regenerates
docs/derivation-graph.json whenever any source file is modified.
Exposes a /preview-version endpoint so the front-end can detect
changes and live-reload (see docs/livereload.js).

Usage:
    python3 scripts/preview_server.py            # foreground
    PREVIEW_PORT=8080 python3 scripts/preview_server.py
    nohup python3 scripts/preview_server.py &    # background

Defaults:
    Port:       8765 (env PREVIEW_PORT)
    Watch dir:  sync_cost/derivations/
    Poll:       2 seconds
    Builder:    scripts/build_derivation_graph.py

Stop with Ctrl-C (foreground) or kill the PID (background).

Stdlib only. No external dependencies.
"""

from __future__ import annotations

import os
import subprocess
import sys
import threading
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

PORT = int(os.environ.get("PREVIEW_PORT", "8765"))
WATCH_DIR = Path("sync_cost/derivations")
BUILD_SCRIPT = "scripts/build_derivation_graph.py"
POLL_INTERVAL = 2.0  # seconds


class State:
    """Shared state between watcher and HTTP threads."""

    def __init__(self) -> None:
        self.version = str(int(time.time()))
        self.lock = threading.Lock()

    def bump(self) -> None:
        with self.lock:
            self.version = str(int(time.time()))

    def current(self) -> str:
        with self.lock:
            return self.version


STATE = State()


def collect_mtimes() -> dict[str, float]:
    """Snapshot mtimes of all watched markdown files."""
    if not WATCH_DIR.is_dir():
        return {}
    return {str(f): f.stat().st_mtime for f in WATCH_DIR.glob("*.md")}


def regenerate_graph() -> None:
    """Run the derivation-graph builder; tolerate failures silently."""
    try:
        subprocess.run(
            [sys.executable, BUILD_SCRIPT],
            check=False,
            capture_output=True,
        )
    except FileNotFoundError:
        pass


def watcher(stop_event: threading.Event) -> None:
    """Poll watched files; regenerate and bump version on change."""
    snapshot = collect_mtimes()
    while not stop_event.is_set():
        time.sleep(POLL_INTERVAL)
        current = collect_mtimes()
        if current != snapshot:
            changed = [
                Path(p).name
                for p in current
                if p not in snapshot or current[p] != snapshot.get(p)
            ]
            print(
                f"[watcher] change detected ({len(changed)} file(s)): "
                f"{', '.join(changed[:3])}"
                + (f", ...+{len(changed) - 3}" if len(changed) > 3 else "")
            )
            regenerate_graph()
            STATE.bump()
            snapshot = current
            print(f"[watcher] graph regenerated; version={STATE.current()}")


class PreviewHandler(SimpleHTTPRequestHandler):
    """SimpleHTTPRequestHandler + /preview-version JSON endpoint."""

    def do_GET(self) -> None:  # noqa: N802 (stdlib API)
        if self.path == "/preview-version":
            body = f'{{"version": "{STATE.current()}"}}'.encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Cache-Control", "no-cache")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        return super().do_GET()

    def log_message(self, fmt: str, *args: object) -> None:
        # Quieter logs; one line per request.
        sys.stderr.write(f"[http] {fmt % args}\n")


def main() -> int:
    if not WATCH_DIR.is_dir():
        print(
            f"==> Warning: watch dir {WATCH_DIR} not found "
            f"(run from repo root).",
            file=sys.stderr,
        )

    # Initial build so the served graph reflects current state.
    print("==> Initial graph build...")
    regenerate_graph()
    STATE.bump()

    # File watcher in background.
    stop = threading.Event()
    watch_thread = threading.Thread(
        target=watcher, args=(stop,), daemon=True
    )
    watch_thread.start()

    # HTTP server in main thread.
    server = HTTPServer(("", PORT), PreviewHandler)
    print(f"==> Preview server listening on http://localhost:{PORT}")
    print(f"==> Open: http://localhost:{PORT}/docs/dag.html")
    print("==> File watcher active. Edits regenerate the graph.")
    print("==> Live-reload version endpoint: /preview-version")
    print("==> Ctrl-C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n==> Stopping...")
    finally:
        stop.set()
        server.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
