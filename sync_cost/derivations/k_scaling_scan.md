# K-scaling scan: tongue spectrum from K = 0 to chaos

## What this tests

`observer_register_closure.md` §7 logs an open candidate:

> "K-variation as unifying axis -- whether H-reg (6·13⁵⁴) and P-reg
> (19 states at Farey depth 7) are K-slices of a single register
> structure, with a dynamic equilibrium principle picking the K
> that produces each."

The previous K-variation probe (commit `f034e69`) tested four
parametric/algebraic angles, all null. This probe takes the
orthogonal angle: scan K itself across [0, ~1.05] and report the
scaling of the tongue spectrum directly.

Driver: `k_scaling_scan.py`.

## What we measure

For each K in a grid, we sample the devil's staircase W(Ω) on a
fine 2001-point grid in Ω ∈ [0, 1], extract plateaus (contiguous
runs where W is constant), and assign each plateau the lowest-q
rational matching its W value. Then for each K:

| Quantity | Definition |
|---|---|
| m(K) | Total Lebesgue measure of plateaus assigned to q ≤ 21 |
| N(K, ε) | Number of plateaus with width > ε |
| top-q(K, ε) | Largest q for which every coprime p/q is a plateau with width > ε |
| W_top(K) | Largest individual plateau width |

(Direct staircase scan rather than `circle_map.tongue_width`: the
latter has a binary-search tolerance of `1e-8` checked against a
winding number computed with 5000 iterations, which is never
satisfied for low-K locked tongues. That bug collapses all widths
to 0; orthogonal to the K-scaling question, noted for cleanup but
not addressed here.)

## Results

```
       K      m(K)   N(0.1) N(0.05) N(0.02) N(0.01) N(0.005) N(0.002) N(0.001)
  0.0500   0.01600       0       0       0       0        2        2        2
  0.1000   0.03200       0       0       0       2        2        2        2
  0.2000   0.06600       0       0       2       2        2        3        3
  0.3000   0.10400       0       0       2       2        3        3        5
  0.4000   0.14300       0       2       2       3        3        5        5
  0.5000   0.18700       0       2       2       3        3        5        7
  0.6000   0.23500       0       2       3       3        5        7        7
  0.7000   0.29800       2       2       3       5        5        9       13
  0.8000   0.36800       2       2       3       5        7       11       17
  0.8620   0.42300       2       3       4       5        7       13       23   <- K_STAR
  0.9000   0.46400       2       3       5       7       11       19       29
  0.9500   0.52600       2       3       5       7       11       21       37
  1.0000   0.60400       2       3       5       8       13       27       50   <- critical
  1.0500   0.72400       2       3       5      11       19       41       84
```

(Truncated at Q_MAX = 21. m(K=1) = 0.604 truncated; the full sum
approaches 1 as Q_MAX → ∞ per Jensen-Bak-Bohr; the complement at
K=1 is a fat fractal of Hausdorff dimension ≈ 0.87.)

## Scaling of m(K)

```
       K      m(K)         m/K
    0.0500    0.0160     0.3200
    0.1000    0.0320     0.3200
    0.2000    0.0660     0.3300
    0.3000    0.1040     0.3467
    0.5000    0.1870     0.3740
    0.7000    0.2980     0.4257
    0.9000    0.4640     0.5156
    1.0000    0.6040     0.6040
```

m(K)/K → **0.32** at small K. Theoretical comparison: the dominant
(1/2) tongue has Adler width w(1/2, K) = K/π = K · 0.3183 in the
small-K limit. Match within sample resolution.

This is universal circle-map physics — Adler scaling of the
fundamental subharmonic — not framework-specific. The 1/π is the
Bessel function J₁(K)/K ≈ 1/2 evaluated at the (1/2) resonance
condition; it would appear identically for any sin-coupled circle
map regardless of any Klein-substrate structure.

## Framework-integer hits

The proposal under test: there exists K and a "natural" ε such
that N(K, ε) equals a framework integer (P-reg = 19, |F_6| = 13).
Hits in the scan:

| K | ε | N(K, ε) | Framework integer matched |
|---|---|---|---|
| 0.20 | 0.002 | 3 | q₃ = 3 |
| 0.30 | 0.001 | 5 | q₂ + q₃ = 5 |
| 0.40 | 0.005 | 3 | q₃ |
| 0.70 | 0.001 | 13 | \|F_6\| |
| 0.86  | 0.002 | 13 | \|F_6\|  *(at K_STAR)* |
| 0.90 | 0.002 | 19 | \|F_7\| (P-reg) |
| 1.00 | 0.005 | 13 | \|F_6\| |
| 1.05 | 0.005 | 19 | \|F_7\| (P-reg) |

## Triage

Per `ansatz_audit_policy.md`, the load-bearing piece is the
**forcing argument** for the specific ε at which a framework
integer appears. An (ε, K) pair selected to produce N = 19 is
Class 2 ansatz unless ε follows from a structural condition.

Candidate forcing arguments examined:

1. **ε = 1/Q_MAX**. The natural smallest resolvable width when
   we cap at Q_MAX. With Q_MAX = 21, ε = 1/21 ≈ 0.048; at this ε,
   N(K = 0.9) = 5, not 19. Null.

2. **ε = (1 − K)^β** with β from framework. At K = 0.9, (1−K) =
   0.1; the eight cataloged ε values span 0.001 to 0.1. Multiple β
   produce N = 19; no single β is forced. Null.

3. **K = K_STAR**. At K_STAR = 0.86196052, the ε that produces
   N = 13 is 0.002. The framework gives K_STAR but not a forcing
   for ε = 0.002. The match `N(K_STAR, 0.002) = 13` is suggestive
   but lands as Class 2 ansatz — same pattern as the demoted
   `K_STAR^14 = 1/8` claim from commit `b8911fb`.

4. **K-equilibrium principle**. The original §7 hypothesis was
   that a dynamic principle picks K such that the resolved-state
   count equals a register cardinality. No such principle was
   specified or constructed in this scan; the matches above are
   selected post-hoc.

## Caveats on small-integer near-misses

At every K in [0.05, 1.05], the small-q rationals (1/2, 1/3, 2/3,
1/4, 3/4, ...) are resolved before any high-q rational. The Farey
sequence is exhausted in level order: q = 2 first, then q = 3, then
q = 5, ..., independent of K. So at *some* ε value at *some* K,
the resolved-tongue count will equal almost any positive integer,
including all framework integers. Hitting `19 = |F_7|` is not
diagnostic.

The pigeonhole caveat from `observer_register_closure.md` §7
applies here: at framework-privileged integers, ~1-few % matches
between independently-defined counts are expected.

## Verdict

**Class 2 numerology.** The K-variation axis produces tongue-
spectrum scalings (m(K) ∼ K/π at small K, top-q growing through
Farey levels) that are universal circle-map physics. The
framework-integer hits at (K, ε) pairs are post-hoc selections
without a forcing argument for ε.

The §7 register-unification hypothesis is not refuted (you can't
refute "there exists a K-equilibrium principle" without exhibiting
all candidates), but it is not supported by direct K-scan: no
canonical ε emerges, and the matches that do appear depend on
unforced choices.

H-reg (6·13⁵⁴) is not visible in this scan. Reaching that
resolution would require Q_MAX ~ 13⁵⁴, infeasible by direct
enumeration.

## Status update

**framework_status.md**: no change. K-variation as unifying axis
remains an open candidate at the same status as before — not
falsified, but no positive evidence from the direct K-scan.

**numerology_inventory.md**: log "K-scan tongue counts hitting
framework integers (19, 13)" as Class 2.

## What would change the verdict

A structural derivation of an ε(K) forced by the substrate (e.g.,
the Klein quotient implies ε = q₃²/Q_MAX, or some explicit Z₂-rep
counting argument), such that N(K, ε(K)) reproduces a register
cardinality at a forced K. No such derivation has been found; the
ansatz audit closes Class 4 → Class 2 within one sitting per
policy.

## Cross-references

- `circle_map.py` — the canonical circle-map utilities (note: bug
  in `tongue_width` for low-K, see Method)
- `observer_register_closure.md` §7 — origin of the K-variation
  hypothesis
- `ansatz_audit_policy.md` — the triage applied here
- `numerology_inventory.md` — Class 2 destination
- commit `f034e69` — prior null on parametric/algebraic K-bridges
