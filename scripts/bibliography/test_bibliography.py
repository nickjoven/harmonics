"""
test_bibliography.py

Unit tests for the citation parsing + BibTeX-key layer of
build_bibliography.py. These are the parts that must be exactly
right and that run with no network: extraction of arXiv ids and
DOIs from prose, canonicalization, and deterministic key
generation. API resolution is exercised live by the `check`
command in CI, not mocked here.

Run:
    python3 -m pytest scripts/bibliography/test_bibliography.py
    python3 scripts/bibliography/test_bibliography.py   # pytest-less
"""

from __future__ import annotations

import importlib.util
import pathlib
import sys

_HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location(
    "build_bibliography", _HERE / "build_bibliography.py"
)
bib = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bib)


# ============================================================
# arXiv extraction
# ============================================================

def test_arxiv_new_style():
    assert bib.extract_citations("see arXiv:2504.19874 for details") == {
        "arxiv:2504.19874"
    }


def test_arxiv_version_suffix_stripped():
    # arXiv:2504.19874 and ...v2 are the same work.
    assert bib.extract_citations("arXiv:2504.19874v2") == {"arxiv:2504.19874"}


def test_arxiv_case_insensitive():
    assert bib.extract_citations("ARXIV:2504.19874") == {"arxiv:2504.19874"}


def test_arxiv_space_after_colon():
    assert bib.extract_citations("arXiv: 2504.19874") == {"arxiv:2504.19874"}


def test_arxiv_old_style():
    assert bib.extract_citations("the classic arXiv:hep-th/9711200") == {
        "arxiv:hep-th/9711200"
    }


def test_arxiv_old_style_subclass():
    assert bib.extract_citations("arXiv:math.AG/0309285") == {
        "arxiv:math.ag/0309285"
    }


def test_arxiv_url_abs_and_pdf():
    text = "https://arxiv.org/abs/2601.21704 and https://arxiv.org/pdf/2502.11902v3"
    assert bib.extract_citations(text) == {"arxiv:2601.21704", "arxiv:2502.11902"}


def test_arxiv_five_digit_serial():
    assert bib.extract_citations("arXiv:2504.19874") == {"arxiv:2504.19874"}
    assert bib.extract_citations("arXiv:0704.0001") == {"arxiv:0704.0001"}


# ============================================================
# DOI extraction
# ============================================================

def test_doi_prefix():
    assert bib.extract_citations("doi:10.1126/science.aea3321") == {
        "doi:10.1126/science.aea3321"
    }


def test_doi_url():
    assert bib.extract_citations("https://doi.org/10.1126/science.aea3321") == {
        "doi:10.1126/science.aea3321"
    }


def test_doi_dx_url():
    assert bib.extract_citations("http://dx.doi.org/10.1103/PhysRevLett.116.061102") == {
        "doi:10.1103/physrevlett.116.061102"
    }


def test_doi_lowercased():
    # DOIs are case-insensitive per the DOI handbook; we canonicalize lower.
    assert bib.extract_citations("doi:10.1126/Science.AEA3321") == {
        "doi:10.1126/science.aea3321"
    }


def test_doi_trailing_punctuation_stripped():
    # A DOI ending a sentence must not swallow the period/paren.
    assert bib.extract_citations("(doi:10.1126/science.aea3321).") == {
        "doi:10.1126/science.aea3321"
    }
    assert bib.extract_citations("ref doi:10.1000/abc;") == {"doi:10.1000/abc"}


def test_doi_internal_dot_kept():
    assert bib.extract_citations("doi:10.1126/science.aea3321 ok") == {
        "doi:10.1126/science.aea3321"
    }


# ============================================================
# Mixed / negative
# ============================================================

def test_multiple_and_dedup():
    text = "arXiv:2504.19874 again arXiv:2504.19874v1 and doi:10.1126/science.aea3321"
    assert bib.extract_citations(text) == {
        "arxiv:2504.19874",
        "doi:10.1126/science.aea3321",
    }


def test_no_false_positive_on_plain_numbers():
    assert bib.extract_citations("the ratio 13/19 = 0.6842 at depth 6") == set()


def test_no_false_positive_on_version_like():
    assert bib.extract_citations("Python 3.11 and section 2.3.4") == set()


# ============================================================
# BibTeX key generation
# ============================================================

def test_bibtex_key_family_year():
    meta = {"authors": ["Amir Zandieh", "Majid Daliri"], "year": "2025"}
    assert bib.bibtex_key(meta, set()) == "Zandieh2025"


def test_bibtex_key_unicode_stripped():
    meta = {"authors": ["Igor Rončević"], "year": "2026"}
    assert bib.bibtex_key(meta, set()) == "Roncevic2026"


def test_bibtex_key_family_comma_form():
    meta = {"authors": ["Zandieh, Amir"], "year": "2025"}
    assert bib.bibtex_key(meta, set()) == "Zandieh2025"


def test_bibtex_key_collision_disambiguation():
    taken: set[str] = set()
    k1 = bib.bibtex_key({"authors": ["Smith"], "year": "2020"}, taken)
    k2 = bib.bibtex_key({"authors": ["Smith"], "year": "2020"}, taken)
    k3 = bib.bibtex_key({"authors": ["Smith"], "year": "2020"}, taken)
    assert (k1, k2, k3) == ("Smith2020", "Smith2020a", "Smith2020b")


def test_bibtex_key_missing_author():
    assert bib.bibtex_key({"authors": [], "year": "2020"}, set()) == "Anon2020"


def test_bibtex_key_missing_year():
    assert bib.bibtex_key({"authors": ["Smith"]}, set()) == "Smith0000"


# ============================================================
# Self-citation guard
# ============================================================

def test_generated_references_md_excluded():
    # The generated REFERENCES.md must not be scanned as a source, or the
    # bibliography would cite itself.
    assert bib.REFS_MD_PATH.resolve() in bib._excluded_sources()


# ============================================================
# Runner (pytest-less)
# ============================================================

def _collect_tests():
    mod = sys.modules[__name__]
    return [
        (name, getattr(mod, name))
        for name in sorted(dir(mod))
        if name.startswith("test_") and callable(getattr(mod, name))
    ]


def _main() -> int:
    tests = _collect_tests()
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  PASS  {name}")
        except AssertionError as e:
            failed += 1
            print(f"  FAIL  {name}: {e}")
        except Exception as e:  # noqa: BLE001
            failed += 1
            print(f"  ERROR {name}: {type(e).__name__}: {e}")
    print()
    print(f"  {len(tests) - failed}/{len(tests)} tests passed")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(_main())
