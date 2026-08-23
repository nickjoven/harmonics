#!/usr/bin/env bash
# Owner actions for the 2026-08 correction campaign (run by Nick, not agents:
# resealing writes the substrate; merging touches ket branch state).
#
# Usage:
#   owner_actions_2026-08.sh list        # read-only: show what would be resealed
#   owner_actions_2026-08.sh reseal      # ket put all drifted spine files, verify, commit .ket
#   owner_actions_2026-08.sh ket-merge   # merge porting-instructions into ket main + run tests
#   owner_actions_2026-08.sh push        # push harmonics corrections branch + ket main (publishes)
#
# Exit codes:
#   0  success (verified where applicable)
#   2  reseal ran but post-verification still reports drift
#   3  missing prerequisite (ket binary, repo, or expected branch)
#   4  working tree dirty / merge failed
#   5  merge landed but cargo tests failed (rollback hint printed)
#   6  usage error
set -u -o pipefail

HARMONICS="$HOME/code/harmonics"
KET_REPO="$HOME/code/ket"

say()  { printf '\n== %s\n' "$*"; }
die()  { printf 'ERROR: %s\n' "$*" >&2; exit "${2:-1}"; }

# Derive the drifted set live from the two checks (union), so the script
# reseals exactly what is currently drifted rather than a stale hardcode.
drifted_files() {
  cd "$HARMONICS" || die "harmonics repo not found at $HARMONICS" 3
  {
    python3 scripts/drift/check_enforced_coverage.py 2>/dev/null \
      | awk '/ declared .* actual /{print $1}'
    python3 scripts/drift/check_graph_sealed.py 2>/dev/null \
      | sed -n '/DRIFTED/,/Re-`ket put`/p' \
      | sed '1d;$d' \
      | awk '{print $1}' \
      | while read -r stem; do
          if [ -f "sync_cost/derivations/${stem}.md" ]; then
            echo "sync_cost/derivations/${stem}.md"
          elif [ -f "sync_cost/derivations/${stem}.py" ]; then
            echo "sync_cost/derivations/${stem}.py"
          elif [ -f "${stem}" ]; then
            echo "${stem}"
          else
            echo "UNRESOLVED:${stem}" >&2
          fi
        done
  } | sort -u
}

cmd_list() {
  say "files currently drifted (enforced-coverage ∪ graph-sealed):"
  local files
  files="$(drifted_files)"
  if [ -z "$files" ]; then
    echo "  (none — nothing to reseal)"
    return 0
  fi
  printf '  %s\n' $files
  echo
  echo "count: $(echo "$files" | wc -l)"
}

cmd_reseal() {
  cd "$HARMONICS" || die "harmonics repo not found" 3
  command -v ket >/dev/null 2>&1 || die "ket binary not on PATH" 3

  local files
  files="$(drifted_files)"
  [ -n "$files" ] || { echo "nothing drifted — already sealed"; exit 0; }

  say "resealing $(echo "$files" | wc -l) file(s) via KET_HOME=.ket ket put"
  local f fail=0
  for f in $files; do
    case "$f" in UNRESOLVED:*) die "could not resolve path for ${f#UNRESOLVED:}" 3;; esac
    if KET_HOME=.ket ket put "$f"; then
      echo "  sealed: $f"
    else
      echo "  FAILED: $f" >&2
      fail=1
    fi
  done
  [ "$fail" -eq 0 ] || die "one or more ket put invocations failed" 2

  say "post-verification"
  python3 scripts/drift/check_enforced_coverage.py
  local rc_a=$?
  python3 scripts/drift/check_graph_sealed.py | tail -3
  local rc_b="${PIPESTATUS[0]}"
  if [ "$rc_a" -ne 0 ] || [ "$rc_b" -ne 0 ]; then
    die "reseal ran but a check still reports drift (enforced rc=$rc_a, sealed rc=$rc_b)" 2
  fi

  say "committing substrate updates (.ket only)"
  git add .ket
  if git diff --cached --quiet; then
    echo "  nothing to commit (substrate unchanged?)"
  else
    git commit -m "reseal: re-put drifted spine files after 2026-08 correction editions

All enforced-coverage and graph-sealed drift cleared; verified by both
checks in the same run (see owner_actions_2026-08.sh reseal)." \
      || die "git commit failed" 4
  fi
  say "reseal complete and verified"
}

cmd_ket_merge() {
  cd "$KET_REPO" || die "ket repo not found at $KET_REPO" 3
  git rev-parse --verify porting-instructions >/dev/null 2>&1 \
    || die "branch porting-instructions not found" 3
  git diff-index --quiet HEAD -- || die "ket working tree is dirty — commit or stash first" 4

  local original_branch
  original_branch="$(git rev-parse --abbrev-ref HEAD)"

  say "commits to be merged into main:"
  git log --oneline main..porting-instructions

  say "merging into main"
  git checkout main || die "checkout main failed" 4
  if ! git merge --no-ff porting-instructions \
       -m "Merge porting-instructions: CI workflow + verify/rebuild projection pair"; then
    git merge --abort 2>/dev/null
    git checkout "$original_branch"
    die "merge conflicted — aborted and returned to $original_branch" 4
  fi

  say "running workspace tests"
  if ! cargo test --workspace; then
    echo >&2
    echo "Tests FAILED on merged main. Merge commit is in place." >&2
    echo "To undo: cd $KET_REPO && git reset --hard ORIG_HEAD" >&2
    git checkout "$original_branch"
    exit 5
  fi

  git checkout "$original_branch"
  say "merge complete, tests green; back on $original_branch (push is separate: '$0 push')"
}

cmd_push() {
  # BRANCH defaults to the currently checked-out harmonics branch; pass
  # BRANCH=name to override. The old hard-wired corrections/inexpensive-
  # batch-1 silently reported "up-to-date" for every other branch.
  local branch="${BRANCH:-$(git -C "$HARMONICS" branch --show-current)}"
  [ -n "$branch" ] || die "no branch checked out and BRANCH not set" 6
  say "pushing harmonics branch '$branch' and ket (this publishes)"
  cd "$KET_REPO"        && git push origin main && git push origin log-newline-guard \
    || die "ket push failed" 4
  cd "$HARMONICS"       && git push -u origin "$branch" \
    || die "harmonics push failed" 4
  say "pushed $branch"
}

case "${1:-}" in
  list)      cmd_list ;;
  reseal)    cmd_reseal ;;
  ket-merge) cmd_ket_merge ;;
  push)      cmd_push ;;
  *) sed -n '2,15p' "$0"; exit 6 ;;
esac
