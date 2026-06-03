# Collatz as Minimal Discrete Chaos in the Framework's Vocabulary

## Status / classification

**Class 2 — structural reading, built on existing substrate Collatz work.**
Reads the Collatz map through `minimum_alphabet.md` as a *minimal-degree-of-
freedom* chaotic system, and shows the idea is largely **already in the
substrate**: `docs/archive/collatz.html` and
`gap2_collatz_2d_contraction.py` build the rational extension where integers
are the **q = 1 boundary**, Rule 3 is a **mediant**, and the lone cycle
follows from **{2,3} incommensurability**; `second_law_topological.md`
supplies the chaos mechanism (non-invertibility → no time-reversal →
`h_KS > 0`). One correction to the prompting framing is load-bearing and
made up front. Retrieval-tier; companion check `collatz_minimal_chaos.py`.
No scorecard claim.

**Correction first (honesty gate).** Collatz is an **open conjecture**, not
a proof. The claim "Collatz *is* a formal proof of the minimal requirements
for chaos" overstates it: convergence to 1 is unproven. The defensible
statement is the inverse — Collatz is the **minimal model/instance** that
realizes the framework's chaos ingredients, and its *open* status is exactly
what the framework's own `gap2_collatz` reading predicts: the integer line
is the **"worst" (slowest-contracting) boundary** of the 2D flow, so it is
the hardest case to close. The undecidedness is a feature of the boundary,
not a counterexample to the reading.

---

## The mapping (verified against substrate objects)

The prompting intuition — *whole-integer counting demonstrates phase;
discrete chaos on one line, signaled by parity; minimal degrees of freedom*
— lands on four existing framework objects with little slack:

| Prompt phrase | Framework object | Source |
|---|---|---|
| "whole integer counting … phase" | Z + fixed-point → S¹; the **parity bit (mod 2) is the discrete phase coordinate** (the 2-adic digit) | `minimum_alphabet.md` I.1 |
| "chaos **on one line**" | integers = the **q = 1 boundary** (rightmost Stern–Brocot branch) of rational Collatz on ℚ⁺ | `collatz.html` §1; `gap2_collatz_2d_contraction.py` |
| "signaled / forced by **parity**" | the even/odd fork is the **non-invertible branch point** → no time-reversal → `h_KS > 0` | `second_law_topological.md` §1.3, §2 |
| "**minimal degrees of freedom**" | q = 1 is the minimal/"worst" contracting case; the denominator q is the extra DOF the rational lift adds | `gap2_collatz_2d_contraction.py` Part 3–5 |

### All four primitives, three on the line + the mediant as the lift

The check's ledger (`collatz_minimal_chaos.py`):

| Collatz ingredient | minimum-alphabet primitive |
|---|---|
| the integer line `n ∈ Z` | **Integers Z** (1) |
| parity fork (`÷2` even vs `3n+1` odd) | **two-root / Z₂ orientation** (4), in its *discrete* form |
| iteration to the `{1,2}` cycle | **fixed-point** `x=f(x)` (3) |
| Rule 3 lift `(3p+1)/(q+1)` off `q=1` | **mediant** (2) — the `q>1` dimension |

So **three primitives {Z, Z₂-orientation, fixed-point} act on the integer
line**, and the **fourth — the mediant — is exactly the dimension the
framework's rational extension switches on** to leave the q=1 boundary
(`collatz.html`: "Rule 3 is the mediant of `3(p/q)` with `1/1`"). The
user's "one line" is the slice where the mediant DOF is collapsed to its
boundary.

---

## Why this is genuinely "minimal chaos" — the three forced ingredients

The check verifies each:

1. **Two competing scales, one expanding, one contracting.** `×3` on odd,
   `÷2` on even — the framework's growing/decaying-mode pair (φ/ψ analogue,
   `minimum_alphabet.md` III). The selector is **parity = the minimal
   non-trivial congruence (mod 2)** — the smallest possible state-dependent
   fork on Z. This is the *discrete* analogue of the parabola's role:
   `minimum_alphabet.md` already identifies **orientation = the parabola's
   two roots = Z₂ parity**; here the Z₂ fork is the minimal nonlinearity,
   standing in for the smooth saddle-node. *(This last identification —
   "parity is the discrete minimal nonlinearity the parabola is in the
   smooth circle map" — is the one step that is my proposed reading, not an
   established substrate claim; flagged as such.)*

2. **Exactly one cycle, from {2,3} incommensurability.** A nontrivial
   k-cycle would require `3^a = 2^b` with `a,b>0`; the check confirms there
   are **no solutions** (unique factorization). This is `collatz.html`
   Step 1 — and it is the *same* incommensurability of the framework's two
   primes `q₂=2, q₃=3` that forbids alternative lock cycles elsewhere. The
   expansion prime (3) and contraction prime (2) never commensurate, so the
   only fixed cycle is the trivial `{1,2}`.

3. **Non-invertibility = the arrow of time.** The check shows the forward
   map is **many-to-one** at parity branch points (`T⁻¹(16) = {32, 5}`,
   etc.). Per `second_law_topological.md` §1.3, a non-invertible map "has no
   candidate for time-reversal at all" → unpaired Lyapunov spectrum →
   `h_KS > 0`. **Parity is precisely where invertibility fails**, so parity
   is the seat of the entropy production / the second law on the line. The
   "thermodynamic self-consistency" of the prompt is this: the check's
   mean log-multiplier is **negative** (geometric mean ≈ 0.91 < 1) — net
   contraction toward the attractor, the dynamical-systems second law.

External corroboration (not substrate): on the 2-adic completion `Z₂`, the
parity sequence is the system's symbolic dynamics and the extended map is
ergodic/mixing (Lagarias 1985) — the rigorous sense in which Collatz
"contains chaos." This is the 2-adic mirror of the framework's Archimedean
`S¹ = R/Z`: same `Z`, completed the other way (mod-2^∞ instead of mod-1).

---

## What this does and does not claim

**Does (supportable):**
- Collatz realizes **all four** minimum-alphabet primitives, three on the
  integer line and the mediant as the lift to ℚ⁺ — a clean, complete
  vocabulary match, and one the substrate *independently* built
  (`collatz.html`, `gap2_collatz`).
- Its minimal-chaos ingredients are framework-native: a Z₂-parity fork
  (minimal nonlinearity), `{2,3}` incommensurability (single cycle), and
  non-invertibility at the fork (positive entropy / arrow of time).
- The integer line being the **hardest** case is *predicted* by the
  framework's reading (q=1 = slowest-contracting boundary), which reframes
  why Collatz is open.

**Does NOT (guard rails):**
- It does **not** prove (or claim to prove) the Collatz conjecture, nor
  does the framework. `collatz.html` is explicitly "a reduction sketch, not
  a completed proof"; Step 2's residue-covering is necessary, not
  sufficient.
- "Parity is the discrete parabola" is a **proposed** reading, marked
  above; the substrate states `orientation = two roots = Z₂` but does not
  assert parity *replaces* the parabola for chaos.
- No new constant, no scorecard/MANIFEST entry. This is a vocabulary /
  structural reading (Class 2), consistent with the substrate's existing
  Collatz material.

---

## Where it could sharpen

The framework-native open question is the substrate's own, not a new one:
`gap2_collatz_2d_contraction.py` asks whether the q>1 (mediant) dimension
**accelerates** contraction so that the 2D rational flow is provably
contracting while the q=1 boundary is merely the slow edge. If the H²
contraction is proved off the boundary (Steps 3–4 of `collatz.html`,
currently the conjecture-restated step), the integer conjecture would be
the boundary trace of a proved bulk statement — the same boundary/bulk move
the framework uses elsewhere (K<1 substrate vs K=1 continuum). That, not a
direct attack on the integer line, is where the framework points.

## References

- Internal: `docs/archive/collatz.html` (rational extension, q=1 boundary,
  Rule-3 mediant, Step 1 = `3^a≠2^b`), `gap2_collatz_2d_contraction.py`
  (H² contraction, q=1 = worst boundary), `second_law_topological.md`
  (non-invertibility → no time-reversal → `h_KS>0`), `minimum_alphabet.md`
  (four primitives; orientation = two roots = Z₂ parity; growing/decaying
  modes), `klein_bottle_derivation.md` (non-orientability).
- External: Lagarias, *The 3x+1 problem and its generalizations* (1985) —
  2-adic ergodicity; Barina (2021) — verification to 10²⁰.
- Check: `collatz_minimal_chaos.py`.
