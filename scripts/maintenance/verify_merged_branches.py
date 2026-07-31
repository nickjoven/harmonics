#!/usr/bin/env python3
"""
Tool: content-verified branch cleanup (issue #298 follow-up).

This repo squash-merges, so `git branch --merged` never fires — branch
tips are not ancestors of main even when every change landed. ~130
stale branches accumulated exactly this way before the 2026-07-13
sweep. This tool re-derives merged-ness from CONTENT:

  A branch is VERIFIED-MERGED when, for every path it touched vs its
  merge-base with origin/main, the resulting blob is either
    (a) byte-identical to origin/main's current blob at that path, or
    (b) present as the same (blob, path) pair anywhere in origin/main's
        history (it landed, and main evolved past it).
  A branch that deletes a path still present on main, touches nothing,
  or carries any blob that never reached main is NOT verified.

There is a middle tier. The committed .ket ledger carries session seals
into main, so a branch's file-state often survives in main's history as
a CAS object (.ket/cas/<cid>) even when it never landed at its path.
Such branches are CONTENT-ARCHIVED: deleting them loses no bytes (every
unique blob is retrievable from main's git history), but their edits
were never merged. They are deleted only under --include-archived.

Safety guards (both always on in --delete mode):
  - a branch whose newest commit is younger than --min-age-days
    (default 14) is never deleted, verified or not
  - a branch that is the head of an OPEN pull request is never deleted

Every deletion prints a recovery line first:
  git push origin <sha>:refs/heads/<name>

Run:
  python3 scripts/maintenance/verify_merged_branches.py            # report
  python3 scripts/maintenance/verify_merged_branches.py --delete   # sweep
"""

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def git(*args: str) -> str:
    """Run git; RAISE on failure. Deletion decisions must never run on
    a silently-failed command: the review (2026-07-30) found a failed
    `log --format=%ct` fell through to epoch 0, which read as a
    ~20,000-day-old branch and SATISFIED the min-age safety guard —
    fail-old where the guard needed fail-young."""
    proc = subprocess.run(
        ["git", "-C", str(ROOT), *args], capture_output=True, text=True
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"git {' '.join(args)} failed (rc {proc.returncode}): "
            f"{proc.stderr.strip()[:200]}")
    return proc.stdout


def open_pr_heads() -> set:
    proc = subprocess.run(
        ["gh", "pr", "list", "--state", "open", "--json", "headRefName",
         "--jq", ".[].headRefName"],
        capture_output=True, text=True, cwd=str(ROOT),
    )
    if proc.returncode != 0:
        # No gh / no auth: fail safe by protecting nothing extra but say so.
        print("note: could not query open PRs (gh unavailable); "
              "relying on age guard only", file=sys.stderr)
        return set()
    return {l.strip() for l in proc.stdout.splitlines() if l.strip()}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--delete", action="store_true",
                        help="delete verified branches (default: report only)")
    parser.add_argument("--include-archived", action="store_true",
                        help="with --delete: also delete content-archived "
                             "branches (bytes preserved in main history)")
    parser.add_argument("--min-age-days", type=int, default=14,
                        help="never delete branches younger than this")
    parser.add_argument("--json", action="store_true",
                        help="machine-readable report")
    args = parser.parse_args()

    git("fetch", "--prune", "origin")

    # (blob, path) pairs anywhere in main's history — built once. The
    # blob-only set backs the content-archived tier (CAS-preserved bytes).
    ever, ever_blob = set(), set()
    for line in git("rev-list", "--objects", "origin/main").splitlines():
        parts = line.split(" ", 1)
        if len(parts) == 2:
            ever.add((parts[0], parts[1]))
            ever_blob.add(parts[0])

    # main's current blob per path
    current = {}
    for line in git("ls-tree", "-r", "origin/main").splitlines():
        meta, path = line.split("\t", 1)
        current[path] = meta.split()[2]

    protected = open_pr_heads()
    now = time.time()
    verified, archived, kept = [], [], []

    for ref in git("branch", "-r", "--format=%(refname:short)").splitlines():
        ref = ref.strip()
        if not ref or ref in ("origin/HEAD", "origin/main", "origin"):
            continue
        name = ref.split("/", 1)[1]
        mb = git("merge-base", "origin/main", ref).strip()
        problems, cas_only = [], []
        if not mb:
            problems.append("no merge-base with main")
        else:
            touched = 0
            for line in git("diff", "--raw", "--no-abbrev", mb, ref).splitlines():
                if not line.startswith(":"):
                    continue
                meta, path = line.split("\t", 1)
                path = path.split("\t")[-1]
                newsha = meta.split()[3]
                status = meta.split()[4][0]
                touched += 1
                if status == "D" or newsha.startswith("0" * 6):
                    if path in current:
                        problems.append(f"deletes {path}, still on main")
                    continue
                if current.get(path) == newsha or (newsha, path) in ever:
                    continue
                if newsha in ever_blob:
                    cas_only.append(path)
                    continue
                problems.append(f"{path}: blob never reached main")
            if touched == 0:
                problems.append("empty diff vs merge-base")

        tip = git("rev-parse", ref).strip()
        # An unreadable timestamp fails YOUNG (age 0, guard refuses to
        # delete), never old — see git()'s docstring.
        try:
            ts = int(git("log", "-1", "--format=%ct", ref).strip())
        except (RuntimeError, ValueError):
            ts = now
        age_days = (now - ts) / 86400
        entry = {"branch": name, "tip": tip, "age_days": round(age_days, 1),
                 "problems": problems[:5], "cas_only": cas_only[:5],
                 "pr_head": name in protected}
        if problems:
            kept.append(entry)
        elif cas_only:
            archived.append(entry)
        else:
            verified.append(entry)

    pool = verified + (archived if args.include_archived else [])
    deletable = [e for e in pool
                 if e["age_days"] >= args.min_age_days and not e["pr_head"]]
    held = [e for e in pool if e not in deletable]

    if args.json:
        print(json.dumps({"deletable": deletable, "held_by_guard": held,
                          "archived": archived, "unmerged": kept}, indent=1))
    else:
        print(f"verified-merged: {len(verified)} | content-archived: "
              f"{len(archived)} | unmerged: {len(kept)} || deletable now: "
              f"{len(deletable)}, guard-held: {len(held)}")
        for e in deletable:
            print(f"  DELETE {e['branch']}  (recover: git push origin "
                  f"{e['tip']}:refs/heads/{e['branch']})")
        for e in held:
            why = "open PR" if e["pr_head"] else f"age {e['age_days']}d"
            print(f"  hold   {e['branch']}  ({why})")
        if not args.include_archived:
            for e in archived:
                print(f"  archived {e['branch']}  (bytes in main CAS; "
                      f"--include-archived to delete; e.g. {e['cas_only'][0]})")
        for e in kept:
            print(f"  keep   {e['branch']}  ({e['problems'][0]})")

    if args.delete and deletable:
        names = [e["branch"] for e in deletable]
        proc = subprocess.run(
            ["git", "-C", str(ROOT), "push", "origin", "--delete", *names],
            capture_output=True, text=True,
        )
        print(proc.stdout + proc.stderr, file=sys.stderr)
        print(f"deleted {len(names)} branches" if proc.returncode == 0
              else "DELETE FAILED", flush=True)
        return proc.returncode
    return 0


if __name__ == "__main__":
    sys.exit(main())
