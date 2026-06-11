# Open-threads summary + audit — 2026-06-11

**Purpose:** snapshot the framework's *currently-open* threads and audit
each one's latest findings against the substrate (verify-before-assert,
per `CLAUDE.md`). Human-readable record; not a canonical derivation and
not sealed — it points at canonical docs, it does not restate them as
ground truth.

Session snapshot at write time: CAS 377 (0 corrupt) | scorecard 17 +
bare_k1 5 | git 0 dirty | drift 0. Clean — cache entries below were
re-read from the working-tree substrate this session.

---

## What "open threads" means here

Two distinct ledgers were checked:

1. **In-repo thread ledger** — `thread_chronology.md`, the single home
   for resolved-thread history. Its **"Genuinely open" table is empty**;
   the arc is declared *terminal*. What remains there is explicitly *not*
   an open problem: one quantitative correction (`√r_n` sector-coherence
   factor on the K-zoo kink-mass ratio) and one declined disposition (the
   Class-2 soliton observable-identification, correctly not chased). So
   the framework has **no consistency-forced open thread** in its own
   ledger.

2. **Open GitHub PRs** — the live, unresolved investigation threads. Two
   are open, both **draft, awaiting review**, both based on `main`
   @ `64d701c`:
   - **#251** — Third-twist (Z₃) meta-structure audit (scaffold + first-pass catalog)
   - **#252** — FM beat-frequency / CRT composite correspondence (Mihailescu-bounded)

The summaries and audits below cover those two open PRs.

---

## Thread #252 — FM beat / CRT composite correspondence

**Branch:** `fm_beat_crt_correspondence_audit-2026-06-11`
**Verdict in PR:** MODAL ✓ / GENERATIVE ✓; K-class K<1 substrate derivation.

### Summary

With the cyclic-mode convention `ω_n = 2π/n`, the dynamical FM
beat-frequency identity coincides with the algebraic CRT composition for
substrate composite modes:

```
ω_{ab} = |ω_a − ω_b|   iff   |a − b| = 1   (consecutive integers)
```

Restricting to Mihailescu-canonical orders (perfect prime powers of
q₂=2, q₃=3), the consecutive pairs are **exactly three** — (2,3)→Z₆,
(3,4)→Z₁₂, (8,9)→Z₇₂ — bounded by Mihăilescu's theorem (8,9 are the
unique consecutive perfect powers ≥ 2). The substantive finding: **Z₇₂ =
Z_{K_quark} × Z_{K_lepton} is substrate-admitted but framework-unengaged**
— a candidate composite at the Catalan locus the framework hasn't audited.

### Audit of latest findings

| Claim | Substrate check | Result |
|---|---|---|
| `ω_{ab} = \|ω_a − ω_b\|` ⟺ `\|a−b\|=1` under `ω_n=2π/n` | Arithmetic: `ω_a−ω_b = 2π(b−a)/(ab)`, `ω_{ab}=2π/(ab)` ⇒ equality iff `\|b−a\|=1` | ✓ holds exactly |
| Mihailescu pairs are exactly (2,3),(3,4),(8,9) | Powers of 2,3: {2,3,4,8,9,16,27,…}; consecutive pairs are those three; 9→16 gap 7, 16→27 gap 11 | ✓ correct |
| Mihăilescu / Catalan citation | `canonical_glossary.md` §5 — statement verbatim, `(x,p,y,q)=(3,2,2,3)`, Mihăilescu 2002 *J. Reine Angew. Math.* **572** | ✓ matches verbatim |
| Z₆ = Z₂ × Z₃ CRT | `canonical_glossary.md` "Z_6 mode lattice = ℤ/2ℤ × ℤ/3ℤ (CRT)" | ✓ canonical |
| `K_quark = q₂³ = 8`, `K_lepton = q₃² = 9` | `canonical_glossary.md:51,52`; `numerology_count_phase_a.md:74-75` | ✓ canonical, exact |
| Z₇₂ has no substrate-mode references | Not re-run this session (grep claim is internal to the PR); plausible given Z₇₂ absent from glossary mode lattice | ⚠ unverified-this-session |
| Origin sim `scratch/substrate_mode_evolution.py` (cited "verified-this-session" L30) | **Not present on `main`** — PR-branch artifact only | ⚠ verify on PR branch, not main |

**Net:** every load-bearing *substrate* citation that exists on `main`
verifies clean. Two items are PR-branch-local (the origin simulation and
the Z₇₂-grep), so they can only be confirmed against that branch's tree,
not the canonical substrate. The PR is honest about its non-claims
(`ω_n=2π/n` is natural-but-underived; Z₇₂ is a candidate, not established
content; no empirical anchor). No overreach detected.

---

## Thread #251 — Third-twist (Z₃) meta-structure audit

**Branch:** `third_twist_meta_structure_audit_scaffold-2026-06-09`
**Verdict in PR:** MODAL ✓ / GENERATIVE PARTIAL; bimodal (cyclic A + Mihailescu-ratio B), explicitly a *first-pass sampling* (~25 instances), not exhaustive.

### Summary

Audits the Z₃ / third-twist substrate modes as a symmetric counter to the
Z₂ / half-twist bias of the recent PR #240–250 chain. Catalog partitions
Z₃ content into four modes (A pure cyclic, B substrate-prime cube/ratio,
C in-composite, D fractional). Five findings P1–P5; headline: the
half-twist's character is *cyclic + fractional* while the third-twist's is
*cyclic + Mihailescu-cube* — complementary substrate functions, not the
same role. Concludes Z₃ is **not** an analog of the half-twist; identity
and signature each need two sub-statements.

### Audit of latest findings

| Claim | Substrate check | Result |
|---|---|---|
| P5: `q₂ × q₃^d = 54` is a substrate-natural exponent | `hierarchy_gaussian_lattice.md:20` — "Exponent: q₂ q₃^d = 54, the gauge cell count of K²"; the exponent in R = 6·13⁵⁴ | ✓ canonical (54 is genuinely the hierarchy/gauge-cell exponent) |
| P2: Aut(Z₃) = Z₂ inversion; substrate prefers `Q = q₂/q₃ = 2/3` | `Q = q₂/q₃` is the canonical framework ratio; arithmetic 2/3 trivially holds | ✓ consistent with canonical `Q` |
| P4: Möbius phase pattern (0, π/3, 2π/3) realizes Z₂+Z₃ on one carrier; gcd(2,3)=1 ⇒ CRT | Consistent with the canonical Z₆ = Z₂ × Z₃ CRT decomposition | ✓ consistent |
| **P1 / Mode B: "the framework has no q₂³-only canonical identity" (Z₂ count = 0)** | `canonical_glossary.md:51` — **`K_QUARK = q₂³ = 8`** is a canonical identity; also `numerology_count_phase_a.md:74` | ⚠ **TENSION** — see below |
| Catalog counts (Mode A 10, Mode B 10, 25 total) | Self-described as a grep *sampling*, not exhaustive | ⚠ unverified-this-session (sampling, by author's own flag) |

### The P1 flag (load-bearing)

PR #251's P1 asserts the q₂³ cube is *uniquely* Z₃-side: "the framework
has no q₂³-only canonical identity" (Mode-B Z₂ count = 0). But the
substrate carries **`K_QUARK = q₂³ = 8`** as a *canonical glossary entry*
(`canonical_glossary.md:51`, "Strong-coupling mode count", source
`down_type_double_cover_closed.md`), echoed in
`numerology_count_phase_a.md:74`. A standalone canonical `q₂³ = 8` is
exactly a "q₂³-only canonical identity," so the bare "0 / none" reading is
in **direct tension with the substrate**.

This is squarely the misclassification the PR's own test plan asks to
re-check ("Independently re-check the Mode A vs Mode B partition for
misclassifications"). It does not sink the thesis — the *cube-qua-cube /
Mihailescu-ratio* distinction (q₃³ and 27/8 = q₃³/q₂³ as operative ratios
vs. K_QUARK as a mode-count) may be the intended finer claim — but P1 must
be **reworded to acknowledge K_QUARK = q₂³**, or the Mode-B partition
criterion sharpened, before the "uniquely Z₃" conclusion is sound. As
written it would not survive a substrate cross-check.

**Net:** the arithmetic/structural anchors (54, Q=2/3, CRT) verify clean.
The catalog is an honest sampling. P1 carries one substrate tension that
should be reconciled in review.

---

## Bottom line

- **Framework's own ledger:** no consistency-forced open threads
  (`thread_chronology.md` terminal).
- **#252:** clean against the substrate as far as `main` allows; two
  items live only on the PR branch (origin sim, Z₇₂ grep) and should be
  checked there. No overreach.
- **#251:** structural anchors verify; **one load-bearing claim (P1, "no
  q₂³-only canonical identity") is contradicted by the canonical
  `K_QUARK = q₂³ = 8`** and needs rewording or a sharper Mode-B criterion.
  Catalog is an explicit first-pass sampling.

*Audit performed against working-tree substrate @ `64d701c`; canonical
references re-read this session. Where a claim could only be checked on a
PR branch, it is marked unverified-this-session rather than asserted.*
