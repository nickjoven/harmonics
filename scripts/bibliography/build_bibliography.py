#!/usr/bin/env python3
"""Extract, resolve, and render the framework's external bibliography.

The derivation docs under ``sync_cost/`` cite the external literature
inline, in two notations the repo already uses:

    arXiv:2504.19874            (also arXiv:hep-th/9711200 old-style)
    doi:10.1126/science.aea3321 (also https://doi.org/10.1126/...)

This script is the bibliography substrate for those citations. It:

  1. **Extracts** every arXiv id / DOI from the markdown sources.
  2. **Resolves** each to canonical metadata (title, authors, year,
     venue) via the arXiv Atom API and the CrossRef REST API, caching
     every lookup in ``cache.json`` so resolution is incremental and
     PR-time validation is deterministic and (mostly) offline.
  3. **Renders** three artifacts that travel with the repo:
       - ``sync_cost/derivations/references.bib``  (BibTeX, for papers)
       - ``sync_cost/derivations/REFERENCES.md``   (human index + backlinks)
       - ``docs/bibliography.json``                (machine index, for the site)

Two CLI modes back the CI wiring:

    build   regenerate cache + all artifacts (hits the APIs). The
            main-branch bot runs this and commits the result.
    check   validate without writing: malformed ids fail, citations
            that the APIs report as *not found* fail, and stale
            artifacts (sources changed but artifacts not regenerated)
            fail. Network *unreachability* only warns -- a flaky API
            must not redden an unrelated PR.

Design notes mirror the rest of the repo's CI-owned generated files
(see .github/workflows/regen-derivation-graph.yml): contributors do
not hand-edit the artifacts; CI owns them. The cache is committed so
that ``check`` on a PR can validate already-known citations with no
network at all, and only reaches the network for genuinely new ones.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

# ───────────────────────────── paths ─────────────────────────────

ROOT = pathlib.Path(__file__).resolve().parents[2]
HERE = pathlib.Path(__file__).resolve().parent

# Markdown trees scanned for citations. Order is stable for output.
SOURCE_GLOBS = (
    "sync_cost/derivations/*.md",
    "sync_cost/applications/*.md",
    "sync_cost/*.md",
)

CACHE_PATH = HERE / "cache.json"
BIB_PATH = ROOT / "sync_cost" / "derivations" / "references.bib"
REFS_MD_PATH = ROOT / "sync_cost" / "derivations" / "REFERENCES.md"
JSON_PATH = ROOT / "docs" / "bibliography.json"

# Polite-pool identification for both APIs. CrossRef rewards a mailto
# with the faster pool; arXiv just wants a real UA.
CONTACT = "nicholasjoven@gmail.com"
USER_AGENT = f"harmonics-bibliography/1.0 (+https://github.com/nickjoven/harmonics; mailto:{CONTACT})"

ARXIV_API = "https://export.arxiv.org/api/query"
CROSSREF_API = "https://api.crossref.org/works/"

ATOM_NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

# ──────────────────────────── extraction ────────────────────────────
#
# Each citation normalizes to a canonical id of the form
# "arxiv:<id>" or "doi:<doi>" (DOI lowercased per the DOI handbook,
# which says DOIs are case-insensitive). The version suffix on an
# arXiv id (vN) is dropped for the canonical id so that arXiv:2504.19874
# and arXiv:2504.19874v2 are the same work.

# New-style arXiv: YYMM.NNNNN (4-5 digit serial), optional vN.
_ARXIV_NEW = r"\d{4}\.\d{4,5}"
# Old-style arXiv: archive[.subclass]/NNNNNNN, e.g. hep-th/9711200.
_ARXIV_OLD = r"[a-z][a-z-]+(?:\.[A-Z]{2})?/\d{7}"

ARXIV_INLINE = re.compile(
    rf"\barxiv:\s*((?:{_ARXIV_NEW}|{_ARXIV_OLD}))(v\d+)?\b",
    re.IGNORECASE,
)
ARXIV_URL = re.compile(
    rf"arxiv\.org/(?:abs|pdf)/((?:{_ARXIV_NEW}|{_ARXIV_OLD}))(v\d+)?",
    re.IGNORECASE,
)

# DOI: 10.<registrant>/<suffix>. The suffix runs until whitespace or a
# delimiter that cannot belong to a DOI in prose. Trailing sentence
# punctuation is stripped afterward (DOIs may legitimately contain '.'
# mid-string, so we only trim from the end).
_DOI_CORE = r"10\.\d{4,9}/[^\s\"'<>)\]}]+"
DOI_INLINE = re.compile(
    rf"(?:doi:\s*|https?://(?:dx\.)?doi\.org/)({_DOI_CORE})",
    re.IGNORECASE,
)

_DOI_TRAILING = ".,;:)]}>\"'"


def _clean_doi(raw: str) -> str:
    """Lowercase and strip trailing sentence punctuation from a DOI."""
    doi = raw.strip().rstrip(_DOI_TRAILING)
    return doi.lower()


def extract_citations(text: str) -> set[str]:
    """Return the set of canonical citation ids found in one document."""
    ids: set[str] = set()
    for m in ARXIV_INLINE.finditer(text):
        ids.add("arxiv:" + m.group(1).lower())
    for m in ARXIV_URL.finditer(text):
        ids.add("arxiv:" + m.group(1).lower())
    for m in DOI_INLINE.finditer(text):
        ids.add("doi:" + _clean_doi(m.group(1)))
    return ids


def _excluded_sources() -> set[pathlib.Path]:
    """Generated artifacts that themselves live under a scanned glob.

    REFERENCES.md sits in sync_cost/derivations/ and reproduces every
    arXiv:/doi: string, so scanning it would make the bibliography cite
    itself. Exclude the artifacts this script writes.
    """
    return {REFS_MD_PATH.resolve()}


def scan_sources() -> dict[str, list[str]]:
    """Map canonical citation id -> sorted list of citing doc paths.

    Paths are repo-relative POSIX strings for stable output across OSes.
    """
    cited_by: dict[str, set[str]] = {}
    seen: set[pathlib.Path] = set()
    excluded = _excluded_sources()
    for glob in SOURCE_GLOBS:
        for path in sorted(ROOT.glob(glob)):
            if path in seen or not path.is_file() or path.resolve() in excluded:
                continue
            seen.add(path)
            rel = path.relative_to(ROOT).as_posix()
            text = path.read_text(encoding="utf-8", errors="replace")
            for cid in extract_citations(text):
                cited_by.setdefault(cid, set()).add(rel)
    return {cid: sorted(docs) for cid, docs in sorted(cited_by.items())}


# ──────────────────────────── resolution ────────────────────────────


class ResolveError(Exception):
    """Citation could not be resolved for a reason other than the network."""


class NetworkError(Exception):
    """The API was unreachable; resolution is inconclusive, not failed."""


def _http_get(url: str, *, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except urllib.error.HTTPError as exc:  # 404 etc. -- a definitive answer
        raise ResolveError(f"HTTP {exc.code} for {url}") from exc
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise NetworkError(f"unreachable: {url} ({exc})") from exc


def resolve_arxiv(arxiv_id: str) -> dict:
    """Resolve an arXiv id (version-stripped) to metadata via the Atom API."""
    url = f"{ARXIV_API}?id_list={urllib.parse.quote(arxiv_id)}"
    data = _http_get(url)
    root = ET.fromstring(data)
    entries = root.findall("a:entry", ATOM_NS)
    # arXiv returns one entry per requested id; a missing id yields either
    # no entry or an entry whose <id> does not embed the requested id.
    for entry in entries:
        ent_id = (entry.findtext("a:id", default="", namespaces=ATOM_NS) or "")
        if arxiv_id not in ent_id:
            continue
        title = " ".join(
            (entry.findtext("a:title", default="", namespaces=ATOM_NS) or "").split()
        )
        authors = [
            " ".join((a.findtext("a:name", default="", namespaces=ATOM_NS) or "").split())
            for a in entry.findall("a:author", ATOM_NS)
        ]
        published = entry.findtext("a:published", default="", namespaces=ATOM_NS) or ""
        year = published[:4] if published[:4].isdigit() else ""
        doi = entry.findtext("arxiv:doi", default="", namespaces=ATOM_NS) or ""
        category = ""
        cat_el = entry.find("arxiv:primary_category", ATOM_NS)
        if cat_el is not None:
            category = cat_el.get("term", "") or ""
        return {
            "id": f"arxiv:{arxiv_id}",
            "type": "arxiv",
            "arxiv_id": arxiv_id,
            "title": title,
            "authors": [a for a in authors if a],
            "year": year,
            "venue": "arXiv",
            "category": category,
            "doi": doi.lower(),
            "url": f"https://arxiv.org/abs/{arxiv_id}",
        }
    raise ResolveError(f"arXiv id not found: {arxiv_id}")


def _crossref_year(message: dict) -> str:
    for key in ("published", "published-print", "published-online", "issued", "created"):
        parts = message.get(key, {}).get("date-parts") or []
        if parts and parts[0] and parts[0][0]:
            return str(parts[0][0])
    return ""


def resolve_doi(doi: str) -> dict:
    """Resolve a DOI to metadata via the CrossRef REST API."""
    url = CROSSREF_API + urllib.parse.quote(doi, safe="") + f"?mailto={CONTACT}"
    data = _http_get(url)
    msg = json.loads(data).get("message", {})
    title_list = msg.get("title") or []
    title = " ".join(title_list[0].split()) if title_list else ""
    authors = []
    for a in msg.get("author", []) or []:
        name = " ".join(p for p in (a.get("given", ""), a.get("family", "")) if p).strip()
        if name:
            authors.append(name)
    container = msg.get("container-title") or []
    venue = container[0] if container else (msg.get("publisher") or "")
    return {
        "id": f"doi:{doi}",
        "type": "doi",
        "doi": doi,
        "title": title,
        "authors": authors,
        "year": _crossref_year(msg),
        "venue": venue,
        "volume": msg.get("volume", ""),
        "issue": msg.get("issue", ""),
        "page": msg.get("page", ""),
        "publisher": msg.get("publisher", ""),
        "crossref_type": msg.get("type", ""),
        "url": f"https://doi.org/{doi}",
    }


def resolve(cid: str) -> dict:
    """Resolve a canonical citation id to metadata (raises on failure)."""
    kind, _, ref = cid.partition(":")
    if kind == "arxiv":
        return resolve_arxiv(ref)
    if kind == "doi":
        return resolve_doi(ref)
    raise ResolveError(f"unknown citation kind: {cid}")


# ────────────────────────────── cache ──────────────────────────────


def load_cache() -> dict:
    if CACHE_PATH.exists():
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    return {"entries": {}}


def save_cache(cache: dict) -> None:
    CACHE_PATH.write_text(
        json.dumps(cache, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )


# ────────────────────────── bibtex rendering ──────────────────────────


def _ascii_slug(s: str) -> str:
    """Reduce a name to a bare ASCII alpha slug for a BibTeX key."""
    import unicodedata

    norm = unicodedata.normalize("NFKD", s)
    stripped = norm.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^A-Za-z]", "", stripped)


def _family_name(author: str) -> str:
    """Best-effort surname from a 'Given Family' or 'Family, Given' string."""
    if "," in author:
        return author.split(",", 1)[0].strip()
    parts = author.split()
    return parts[-1] if parts else author


def bibtex_key(meta: dict, taken: set[str]) -> str:
    """Deterministic, collision-free, human-ish BibTeX key: FamilyYYYY[a]."""
    authors = meta.get("authors") or []
    family = _ascii_slug(_family_name(authors[0])) if authors else "Anon"
    family = family or "Anon"
    year = meta.get("year") or "0000"
    base = f"{family}{year}"
    key = base
    suffix = ord("a")
    while key in taken:
        key = f"{base}{chr(suffix)}"
        suffix += 1
    taken.add(key)
    return key


def _bib_escape(s: str) -> str:
    return s.replace("&", r"\&").replace("%", r"\%").replace("_", r"\_")


def render_bibtex(metas: list[dict]) -> str:
    taken: set[str] = set()
    lines = [
        "% references.bib -- external literature cited by the harmonics",
        "% derivation framework. GENERATED by scripts/bibliography/",
        "% build_bibliography.py from inline arXiv:/doi: citations.",
        "% Do not hand-edit; run `make bibliography` (or the CI bot) instead.",
        "",
    ]
    for meta in metas:
        key = bibtex_key(meta, taken)
        meta["_bibkey"] = key
        authors = " and ".join(meta.get("authors") or []) or "Unknown"
        title = _bib_escape(meta.get("title") or "")
        year = meta.get("year") or ""
        if meta["type"] == "arxiv":
            lines.append(f"@misc{{{key},")
            lines.append(f"  title        = {{{title}}},")
            lines.append(f"  author       = {{{authors}}},")
            if year:
                lines.append(f"  year         = {{{year}}},")
            lines.append(f"  eprint       = {{{meta['arxiv_id']}}},")
            lines.append("  archivePrefix= {arXiv},")
            if meta.get("category"):
                lines.append(f"  primaryClass = {{{meta['category']}}},")
            if meta.get("doi"):
                lines.append(f"  doi          = {{{meta['doi']}}},")
            lines.append(f"  url          = {{{meta['url']}}},")
            lines.append("}")
        else:
            venue = _bib_escape(meta.get("venue") or "")
            entry_type = "article" if meta.get("crossref_type") == "journal-article" else "misc"
            lines.append(f"@{entry_type}{{{key},")
            lines.append(f"  title     = {{{title}}},")
            lines.append(f"  author    = {{{authors}}},")
            if year:
                lines.append(f"  year      = {{{year}}},")
            if venue:
                lines.append(f"  journal   = {{{venue}}},")
            if meta.get("volume"):
                lines.append(f"  volume    = {{{meta['volume']}}},")
            if meta.get("issue"):
                lines.append(f"  number    = {{{meta['issue']}}},")
            if meta.get("page"):
                lines.append(f"  pages     = {{{meta['page']}}},")
            lines.append(f"  doi       = {{{meta['doi']}}},")
            lines.append(f"  url       = {{{meta['url']}}},")
            lines.append("}")
        lines.append("")
    return "\n".join(lines)


# ─────────────────────────── markdown rendering ───────────────────────────


def _format_authors_md(authors: list[str]) -> str:
    if not authors:
        return "Unknown"
    if len(authors) > 6:
        return f"{authors[0]} et al."
    return ", ".join(authors)


def render_markdown(metas: list[dict], cited_by: dict[str, list[str]], stamp: str) -> str:
    lines = [
        "# References",
        "",
        "<!-- GENERATED by scripts/bibliography/build_bibliography.py.",
        "     Do not hand-edit; run `make bibliography`. -->",
        "",
        "External literature cited inline (as `arXiv:` / `doi:`) across the",
        "derivation docs, resolved to canonical metadata via the arXiv and",
        f"CrossRef APIs. {len(metas)} reference(s). Generated {stamp}.",
        "",
    ]
    for meta in metas:
        authors = _format_authors_md(meta.get("authors") or [])
        year = meta.get("year") or "n.d."
        title = meta.get("title") or "(title unavailable)"
        venue = meta.get("venue") or ""
        key = meta.get("_bibkey", "")
        head = f"- **[{key}]** {authors} ({year}). *{title}*."
        if venue and venue != "arXiv":
            head += f" {venue}."
        lines.append(head)
        if meta["type"] == "arxiv":
            link = f"  [arXiv:{meta['arxiv_id']}]({meta['url']})"
            if meta.get("doi"):
                link += f" · [doi:{meta['doi']}](https://doi.org/{meta['doi']})"
        else:
            link = f"  [doi:{meta['doi']}]({meta['url']})"
        lines.append(link)
        docs = cited_by.get(meta["id"], [])
        names = ", ".join(f"`{pathlib.PurePosixPath(d).name}`" for d in docs)
        lines.append(f"  Cited by: {names}")
        lines.append("")
    return "\n".join(lines)


def render_json(metas: list[dict], cited_by: dict[str, list[str]], stamp: str) -> str:
    entries = []
    for meta in metas:
        e = dict(meta)
        e["cited_by"] = cited_by.get(meta["id"], [])
        entries.append(e)
    payload = {
        "generated": stamp,
        "generator": "scripts/bibliography/build_bibliography.py",
        "count": len(entries),
        "entries": entries,
    }
    return json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=False) + "\n"


# ──────────────────────────── orchestration ────────────────────────────


def _sort_key(meta: dict):
    """Order: first-author surname, then year, then id."""
    authors = meta.get("authors") or []
    fam = _ascii_slug(_family_name(authors[0])).lower() if authors else "~"
    return (fam or "~", meta.get("year") or "", meta["id"])


def _utc_stamp(now: _dt.datetime | None) -> str:
    now = now or _dt.datetime.now(_dt.timezone.utc)
    return now.strftime("%Y-%m-%d")


def gather(cache: dict, *, offline: bool, refresh: bool) -> tuple[dict, list[dict], list[str], list[str]]:
    """Resolve every cited citation.

    Returns (cited_by, ordered_metas, errors, warnings). ``errors`` are
    definitive failures (malformed/not-found); ``warnings`` are
    network-inconclusive lookups that fell back to a cached or skipped state.
    """
    cited_by = scan_sources()
    entries: dict = cache.setdefault("entries", {})
    metas: list[dict] = []
    errors: list[str] = []
    warnings: list[str] = []

    for cid in cited_by:
        cached = entries.get(cid)
        need = refresh or cached is None or "title" not in (cached or {})
        if need and not offline:
            try:
                meta = resolve(cid)
                entries[cid] = meta
                cached = meta
                time.sleep(0.3)  # be polite to both APIs
            except NetworkError as exc:
                if cached:
                    warnings.append(f"{cid}: {exc} (using cached metadata)")
                else:
                    warnings.append(f"{cid}: {exc} (uncached; skipped)")
            except ResolveError as exc:
                errors.append(f"{cid}: {exc}")
                continue
        elif need and offline:
            if cached:
                warnings.append(f"{cid}: not refreshed (offline); using cache")
            else:
                errors.append(f"{cid}: uncached and offline -- cannot resolve")
                continue
        if cached and "title" in cached:
            metas.append(dict(cached))

    metas.sort(key=_sort_key)
    return cited_by, metas, errors, warnings


def write_artifacts(metas: list[dict], cited_by: dict[str, list[str]], stamp: str) -> None:
    # render_bibtex assigns _bibkey; must run before the md/json renderers.
    bib = render_bibtex(metas)
    BIB_PATH.write_text(bib, encoding="utf-8")
    REFS_MD_PATH.write_text(render_markdown(metas, cited_by, stamp), encoding="utf-8")
    JSON_PATH.write_text(render_json(metas, cited_by, stamp), encoding="utf-8")


# ───────────────────────────── CLI: build ─────────────────────────────


def cmd_build(args) -> int:
    cache = load_cache()
    cited_by, metas, errors, warnings = gather(
        cache, offline=args.offline, refresh=args.refresh
    )
    save_cache(cache)
    stamp = _utc_stamp(None)
    write_artifacts(metas, cited_by, stamp)

    for w in warnings:
        print(f"::warning::bibliography: {w}")
    print(
        f"bibliography: {len(metas)} reference(s) across "
        f"{sum(len(v) for v in cited_by.values())} citation site(s)"
    )
    print(f"  wrote {BIB_PATH.relative_to(ROOT)}")
    print(f"  wrote {REFS_MD_PATH.relative_to(ROOT)}")
    print(f"  wrote {JSON_PATH.relative_to(ROOT)}")
    print(f"  cache {CACHE_PATH.relative_to(ROOT)} ({len(cache['entries'])} entries)")

    if errors:
        print(f"::error::bibliography: {len(errors)} unresolved citation(s):")
        for e in errors:
            print(f"  {e}")
        return 1
    return 0


# ───────────────────────────── CLI: check ─────────────────────────────


def _regen_to_strings(cache: dict, *, offline: bool) -> tuple[dict, list[dict], list[str], list[str], str]:
    cited_by, metas, errors, warnings = gather(cache, offline=offline, refresh=False)
    stamp = _current_stamp_from_existing()
    return cited_by, metas, errors, warnings, stamp


def _current_stamp_from_existing() -> str:
    """Reuse the committed artifacts' date so a pure-content check does not
    spuriously diff on the generation date alone."""
    if JSON_PATH.exists():
        try:
            return json.loads(JSON_PATH.read_text(encoding="utf-8")).get(
                "generated", _utc_stamp(None)
            )
        except (json.JSONDecodeError, OSError):
            pass
    return _utc_stamp(None)


def cmd_check(args) -> int:
    cache = load_cache()
    cited_by, metas, errors, warnings, stamp = _regen_to_strings(cache, offline=args.offline)

    for w in warnings:
        print(f"::warning::bibliography: {w}")

    problems = list(errors)

    # Artifact-freshness check. Skipped with --no-artifacts on PRs, where
    # the artifacts are owned and regenerated by the main-branch bot (same
    # pattern as docs/derivation-graph.json); the PR gate then enforces
    # only that every citation resolves to a real paper. The date line is
    # normalized out (see _current_stamp_from_existing) so only content
    # drift trips the check. render_bibtex must run first: it assigns each
    # meta's _bibkey, which the md/json renderers read.
    if args.artifacts:
        bib = render_bibtex(metas)
        expected = {
            BIB_PATH: bib,
            REFS_MD_PATH: render_markdown(metas, cited_by, stamp),
            JSON_PATH: render_json(metas, cited_by, stamp),
        }
        for path, want in expected.items():
            have = path.read_text(encoding="utf-8") if path.exists() else ""
            if have != want:
                problems.append(
                    f"stale artifact: {path.relative_to(ROOT)} "
                    "(run `make bibliography` and commit)"
                )

    if problems:
        print(f"::error::bibliography check failed ({len(problems)} problem(s)):")
        for p in problems:
            print(f"  {p}")
        return 1

    tail = "all artifacts current" if args.artifacts else "citations only (artifacts not checked)"
    print(
        f"bibliography OK: {len(metas)} reference(s) resolved, {tail}"
        + (f" ({len(warnings)} network warning(s))" if warnings else "")
    )
    return 0


# ───────────────────────────── CLI: list ─────────────────────────────


def cmd_list(args) -> int:
    """Print the citations found in the sources (no resolution)."""
    cited_by = scan_sources()
    for cid, docs in cited_by.items():
        print(f"{cid}\t{len(docs)} doc(s)")
    print(f"\n{len(cited_by)} unique citation(s)")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_build = sub.add_parser("build", help="resolve + write artifacts (hits APIs)")
    p_build.add_argument("--offline", action="store_true", help="do not hit the network")
    p_build.add_argument("--refresh", action="store_true", help="re-resolve even cached ids")
    p_build.set_defaults(func=cmd_build)

    p_check = sub.add_parser("check", help="validate citations + artifact freshness")
    p_check.add_argument("--offline", action="store_true", help="validate from cache only")
    p_check.add_argument(
        "--no-artifacts",
        dest="artifacts",
        action="store_false",
        help="validate citations only; skip the artifact-freshness check "
        "(PR mode -- artifacts are owned by the main-branch bot)",
    )
    p_check.set_defaults(func=cmd_check, artifacts=True)

    p_list = sub.add_parser("list", help="list citations found in sources")
    p_list.set_defaults(func=cmd_list)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
