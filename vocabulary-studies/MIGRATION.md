# Migration: lift this directory into its own repo

This directory is **staged inside harmonics** only because the session that
created it could push to `nickjoven/harmonics` only (GitHub scope was
restricted; `list_repos`/`add_repo` were unavailable). It is a complete,
self-contained future repo. Once the target repo exists (or is added to a
session's scope), lift it out and remove it from harmonics.

## One-time lift (preserves history)

```sh
# from a clone of harmonics, split this subtree into its own branch:
git subtree split --prefix=vocabulary-studies -b vocab-split

# create the new repo (gh or web), then:
git clone https://github.com/nickjoven/<new-repo>.git
cd <new-repo>
git pull ../harmonics vocab-split        # or: git fetch + merge the split branch
git push origin main
```

Or, without history (simpler):

```sh
cp -r harmonics/vocabulary-studies/* <new-repo>/
cd <new-repo> && git add . && git commit -m "Import vocabulary-studies" && git push
```

## After lifting

1. `git rm -r vocabulary-studies/` from harmonics; commit on a branch + PR.
   (These files are retrieval-tier, not enforced spine — removal is clean;
   re-run `scripts/drift/run_all.py` to confirm rc 0.)
2. In the new repo's `MANIFEST.yml`, replace the provisional slug
   `nickjoven/vocabulary-studies` with the real repo name.
3. Optionally register the new repo in `harmonics/MANIFEST.yml → repos:` so
   the federation knows about it (role line already drafted there).
4. If any harmonics scorecard/source ever cites a reading here, add the
   cross-repo mapping so `check_manifest.py` resolves it as federated.

## Self-containment check

All five checks are pure-Python (no numpy) and import nothing from
harmonics, so they run as-is in the new repo:

```sh
for f in *.py; do python3 "$f" >/dev/null && echo "ok: $f"; done
```

Unqualified prose references to substrate docs (`minimum_alphabet.md`,
etc.) are **federated upstream** references to harmonics; they are not
expected to resolve as local files.
