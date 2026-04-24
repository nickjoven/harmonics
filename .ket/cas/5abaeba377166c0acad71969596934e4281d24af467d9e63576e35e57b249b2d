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

(Direct staircase scan rather than `circle_map.tongue_width`. The
original `winding_number` had a cold-start bug: the measure loop
discarded the post-transient state, restarting from `theta = 0`,
so for orbits that hadn't reached the locked attractor within
n_measure iterations the reported W deviated from p/q by enough
to fail the binary-search tolerance test, collapsing widths to 0.
Fixed in this branch — the measure loop now continues from the
post-transient theta, matching the `winding_number_precise`
pattern. Verification: `w(0/1, K)` from fixed `tongue_width` now
matches the analytic Adler value `K/(2π)` to four decimal places
across `K ∈ [0.05, 0.9]`. The probe inlines the corrected version
to stay self-contained.)

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

m(K)/K → **0.32** at small K. Theoretical comparison: the two
*endpoint tongues* (0/1) and (1/1) each have analytic Adler width
`K/(2π)` in the small-K limit (linear in K, from the saddle-node
of the rotation-number-zero fixed point). Their sum is `K/π =
0.3183 K`. The (1/2) tongue is **quadratic** in K (`~ K² / (2π²)`)
and contributes a small correction; higher-q tongues are even
smaller (`~ K^q`). At K ≤ 0.5, m(K) is dominated by (0/1) + (1/1)
to within a few percent.

(Earlier draft of this writeup mis-attributed the K/π scaling to
the (1/2) tongue; corrected after direct check `w(0/1, K) =
K/(2π)` agrees with `tongue_width` to four decimals across
K ∈ [0.05, 0.9].)

This is universal circle-map physics — saddle-node opening of the
rotation-zero / rotation-one fixed-point tongues — not framework-
specific. It would appear identically for any sin-coupled circle
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

## What would prove structure and mechanics disallow other states?

The deeper question behind the K-scan is: even granting that the
circle map produces tongue-counts hitting framework integers at
some (K, ε), is there a structural reason *the other states are
forbidden*? In the framework's positive examples (Klein-antipodal
Z₂ rep theory, XOR filter on Stern-Brocot, anomaly cancellation),
specific configurations are not just numerically suppressed but
**structurally forbidden** — alternative configurations either
violate a representation-theoretic constraint, fail an XOR parity
test, or carry an anomaly that doesn't cancel.

The bare circle map has no such forbidding mechanism. As K is
swept from 0 to 1, every rational `p/q` eventually opens a tongue
of positive measure — none are forbidden, only ordered by tongue
width. The Stern-Brocot hierarchy that organizes the staircase
is a *ranking*, not a *selection rule*. So the bare circle map
cannot serve as a register-generator in the load-bearing sense
the framework uses elsewhere.

For the circle-map machinery to function as a register, it would
need to be **composed** with the framework's existing forcing
filters:

1. **Klein-antipodal Z₂-rep filter** (`klein_antipodal_z2_rep_pattern.md`):
   the (p, q) lattice carries a Z₂ action `p ↔ q − p`. A filter
   selecting only fixed-point or only swapped pairs would cut the
   tongue spectrum in half along the omega ↔ 1−omega symmetry
   axis. This is structurally available — the symmetry is built
   into the sin-coupled map — but the K-scan in this probe did
   not apply it.

2. **XOR filter on Stern-Brocot** (`xor_asymmetry.py`): cells in
   the Stern-Brocot tree are forbidden by the XOR rule that
   produces (q₂, q₃) = (2, 3) from the cross-link uniqueness
   theorem (`mass_sector_closure.md`). Restricting tongues to XOR-
   admissible (p, q) might leave exactly the framework-integer
   counts. Not yet tested.

3. **Anomaly-cancellation filter** (analogous to gauge-sector):
   tongues whose (p, q) satisfies a triangular sum rule survive;
   others cancel pairwise.

The K-scan in this writeup tested only the *bare* circle map. A
positive register-generator claim requires composing it with
(1)–(3) above and showing that the surviving tongue count at some
canonical K equals a framework integer for *structural* reasons
(not for an unforced ε). This is the natural follow-up probe.

The probe is *not* yet a refutation of the §7 hypothesis, but it
sharpens the requirement: a register claim from circle-map
dynamics must produce *forbidden states*, not just *resolved
states*. The bare K-scan can never do this.

## Verdict

**Class 2 numerology** for the bare K-scan results. The K-
variation axis produces tongue-spectrum scalings (m(K) ∼ K/π at
small K from the (0/1)+(1/1) endpoint tongues, top-q growing
through Farey levels) that are universal circle-map physics. The
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

Either of:

1. **A structural derivation of ε(K)** forced by the substrate
   (e.g., the Klein quotient implies `ε = q₃² / Q_MAX`, or some
   explicit Z₂-rep counting argument), such that `N(K, ε(K))`
   reproduces a register cardinality at a forced K.

2. **Composing the K-scan with a forbidding filter** (Klein-
   antipodal Z₂-rep, XOR on Stern-Brocot, anomaly cancellation)
   such that the surviving tongue count at a canonical K is a
   framework integer for structural reasons. This is the
   substantive open probe; see "What would prove structure and
   mechanics disallow other states?" above.

Neither has been produced; the ansatz audit closes Class 4 →
Class 2 within one sitting per policy.

## Cross-references

- `circle_map.py` — the canonical circle-map utilities. The
  `winding_number` cold-start bug that motivated the inline copy
  is fixed in this branch; both that function and `tongue_width`
  are now reliable across `K ∈ [0.05, 1.05]`.
- `observer_register_closure.md` §7 — origin of the K-variation
  hypothesis
- `klein_antipodal_z2_rep_pattern.md` — the positive forcing
  pattern, candidate composition for a register-generator probe
- `ansatz_audit_policy.md` — the triage applied here
- `numerology_inventory.md` — Class 2 destination
- commit `f034e69` — prior null on parametric/algebraic K-bridges
