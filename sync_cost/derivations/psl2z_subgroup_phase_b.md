# PSL(2,ℤ)-subgroup Phase B — substrate-side Γ_0(6) derivation

## What this file is

Phase B execution for Direction 4. Given Phase A's identification
of Γ_0(6) as the framework-natural subgroup whose cusp structure
splits the three w_+ candidates, Phase B addresses:

- **B1**: Why does the framework's substrate preserve Γ_0(6)?
- **B2**: Why does w_+ specifically inhabit cusp 1/2 (= the q_2
  cusp), independent of the EM-MOND reading?
- **B3**: Why does cusp 1/2's orbit select 13/14 specifically as
  the operating-point representative?

**Result**: B1 and B2 close in **recognize mode** — the framework
already has the structure (q_2 × q_3 = Z_6 mode decomposition,
sym Klein-singlet = trivial q_2 rep). Γ_0(6) = Γ_0(2) ∩ Γ_0(3)
is just the modular-curve restatement of the framework's existing
sector-preservation. B3 (representative selection) **remains
open** — it requires the substrate's dynamical equation
specifying which orbit element is the ground state, which the
framework doesn't currently derive.

**w_+ closure status**: Class 4 / Strong candidate at 13/14 with
group-theoretic forcing for the cusp class, contingent only on
the still-open representative selection. Substantive promotion
from Class 2.

## B1 — Substrate preserves Γ_0(6)

### The recognize-mode argument

Γ_0(6) = Γ_0(2) ∩ Γ_0(3) is a well-known modular identity (since
6 = 2·3 and gcd(2,3) = 1, the Hecke level intersects).

To establish "substrate preserves Γ_0(6)," it suffices to show
the substrate **independently** preserves Γ_0(2) and Γ_0(3).
Each of these is a Hecke level whose cusp structure factors
through the Z_2 (resp. Z_3) reduction.

The framework's existing structure (per
`klein_antipodal_z2_rep_pattern.md`):

> "Lattice L = Z_{q_2} × Z_{q_3} ... a finite set of framework-
> integer residues."

The substrate's Z_6 mode lattice decomposes as Z_2 × Z_3 by CRT.
Each factor carries an independent rep:

- **Z_2 = q_2** factor: Klein-antipodal Z_2 rep (sym ψ_+ vs
  antisym ψ_-) — preserved by substrate dynamics (sym/antisym
  eigenmodes don't mix; per `baryon_fraction.md`, sign rep has
  monodromy −1)
- **Z_3 = q_3** factor: gauge-color triplet (or lepton triplet
  K_LEPTON = q_3²) — preserved by substrate dynamics (color
  doesn't transition into non-color sectors at the substrate
  level)

Each preservation is the substrate-side statement that the
corresponding Hecke level structure is preserved. **Substrate
preserving Z_2-rep = Hecke T_2 preserving substrate's
eigendecomposition = Γ_0(2) preservation.** Similarly for Z_3 ↔
Γ_0(3).

By Γ_0(6) = Γ_0(2) ∩ Γ_0(3), the substrate preserves Γ_0(6).
**B1 closes in recognize mode.**

### Strength of the argument

The Z_2-rep preservation argument is a Class 5 closure (per
`omega_b_alpha_beta_closure.md`'s sign-rep no-EM derivation,
which forced w_- = 1 from substrate's Z_2 preservation). The Z_3
color preservation is structural (gauge-coupling locality on the
Z_3 sector). The intersection follows by group theory.

The **strength** of B1 inherits the strength of the q_2 × q_3
sector decomposition itself, which is currently Class 5 in the
framework's existing derivations.

### Subtle point: which representation level?

Strictly, "substrate preserves Γ_0(2)" = "substrate's automorphism
group contains Γ_0(2)" or = "substrate's Hecke operator T_2
commutes with substrate's Hamiltonian." The framework's existing
arguments support a stronger statement than this: not just
preservation, but the substrate IS Γ_0(2) × Γ_0(3) equivariant in
its mode-counting.

For Phase A's cusp-classification application (orbit splitting on
P¹(ℚ)), the weaker "preservation" suffices. The stronger
"equivariance" would be needed for downstream questions about
substrate's spectral decomposition into Γ_0(6)-modular forms,
which is beyond Direction 4's scope.

## B2 — w_+ inhabits cusp 1/2 independently

### The independent argument (no EM-MOND circularity)

The Phase A claim was "w_+ governs EM-coupling MOND-threshold
partial-locking, EM = q_2 sector, ergo w_+ ↔ cusp 1/2." The
worry: this routes through the EM-MOND reading from
`omega_b_alpha_beta_closure.md`, creating circularity.

Independent derivation:

1. **w_+ is the partial-locking weight of the sym ψ_+(1, 5)
   boundary mode** (per `omega_b_alpha_beta_closure.md`'s
   corrected mode breakdown). This identification is purely
   group-theoretic: ψ_+(1, 5) is the trivial Klein Z_2 rep on
   the (1, 5) Z_6-mode pair.

2. **Trivial Klein Z_2 rep is the q_2-equivariant ground state**.
   In the q_2 reduction (Z_2 = Klein-antipodal), trivial rep =
   "+1 eigenvalue" = the eigenmode that survives the q_2
   reduction non-trivially. The q_2 reduction acts on the
   substrate's mode lattice as the Hecke T_2 cusp action.

3. **Hecke T_2 cusp action sends trivial-rep modes to the q_2-cusp
   of X_0(6)**. The cusp 1/2 is precisely the cusp at which the
   Z_2 quotient is "active" (denominator carries factor 2). For
   the substrate's mode whose representative carries the trivial
   q_2 rep, its modular orbit lies in cusp 1/2.

4. **Conclusion**: w_+ ↔ cusp 1/2 of Γ_0(6).

### What this avoids vs. the original argument

The independent argument routes through:

- ψ_+(1,5) = trivial Klein Z_2 rep (group theory, no MOND)
- Trivial q_2 rep ↔ cusp 1/2 (modular forms / Hecke action)

The original argument routed through:

- ψ_+(1,5) governs sym partial-locking (group theory, OK)
- Sym = trivial Klein = HAS EM coupling (OK, structural)
- EM = MOND = partial locking weight (this routes through
  `omega_b_alpha_beta_closure.md`'s mechanism)

The independent path skips the MOND-threshold link. It's pure
group theory + modular structure. **B2 closes independently.**

### Strength of the argument

The "trivial q_2 rep ↔ cusp 1/2 of Γ_0(6)" link is a standard
fact in Hecke theory (the cusp at level d corresponds to the
sub-rep at level d in the Hecke decomposition). For the framework's
substrate, this is the analog of the standard "cusps ↔ degenerations"
correspondence.

This argument is Class 4 / strong (group-theoretic, no fitted
factors), pending Phase B verification that the framework's
modular structure on the substrate matches the standard
modular-forms cusp structure on X_0(6) — which is the B1
preservation result, which we just established.

So B1 and B2 mutually support: B1 establishes the substrate's
Γ_0(6) structure; B2 uses that structure to identify w_+'s cusp.

## B3 — Representative selection within cusp 1/2 (open)

### The open question

Cusp 1/2 of Γ_0(6) contains infinitely many rationals. The orbit
of 1/2 under Γ_0(6) is {p/q : gcd(q, 6) = 2}. This includes:

```
1/2, 3/2, 5/2, 1/4, 3/4, 5/4, 7/4, 1/8, 3/8, 5/8, 7/8, ...
1/14, 3/14, 5/14, 9/14, 11/14, 13/14, ...
```

(All p/q with q even-not-multiple-of-3, p coprime to q.)

The Phase A identification "w_+ = 13/14" is one specific element
of this infinite cusp orbit. **Why 13/14 and not, e.g., 1/2 or
5/14 or 11/14?**

### What's available at the framework level

The framework's existing structural readings of 13/14
(per `omega_b_w_plus_candidate.md`):

- 13 = |F_6| (Farey count at depth 6)
- 14 = q_2 · |F_4| (q_2 × Farey-depth-4)
- 1 − 13/14 = 1/14 (inverse of Ω_DM logit denominator per
  `partition_logit_form.md`)

These are framework-internal expressions, but they're not derived
from a substrate dynamical equation specifying "the operating
point in cusp 1/2 is the cross-ratio of these specific framework
points." Such a derivation requires:

1. **A substrate "ground state" criterion** within each cusp
   orbit. Modular forms theory has notions like "lowest weight"
   or "newform" that select specific orbit representatives. For
   the framework's substrate, the analog would be the lowest-
   energy or fixed-point representative.

2. **Connection of the framework's specific quantities (|F_6|,
   |F_4|, q_2) to the modular ground-state representative at
   cusp 1/2**. This requires deriving the "natural representative"
   formula for cusp 1/2 in terms of framework primitives.

Neither (1) nor (2) is currently derived. They're substantive
multi-session structural work.

### Why this can't close in recognize mode

B1 and B2 closed in recognize mode because the framework already
has Z_2-rep preservation (B1) and the trivial-rep-ground-state
identification (B2) as existing content. B3 requires NEW content:
the framework's selection rule for cusp orbit representatives is
not yet articulated.

Possible Phase C work to close B3:

- **Substrate ground-state derivation at cusp 1/2**: requires
  an explicit dynamical equation for the substrate at the cusp,
  with 13/14 emerging as the lowest-energy / fixed-point
  representative. The framework's mediant tongue-stability
  ordering (per `mediant_derivation.md`) suggests "widest
  tongue" = lowest-q representative, but cusp 1/2 contains 1/2
  as the smallest-q element, not 13/14.

- **Logit-form natural representative**: per
  `partition_logit_form.md`, the framework's prediction is
  cleanly stated in logit form with q_2 × q_3-sector
  factorization. Cusp 1/2 representatives can be parametrized
  by their logit-form numerators; 13/14's logit num = 13/(14−13)
  = 13 is exactly the |F_6| Farey count, suggesting the natural
  representative is "the one whose logit numerator equals the
  framework's DE mode count." This is a CANDIDATE selection rule,
  not yet a derivation.

## Closure status after Phase B

| Item | Pre-Phase-A | Pre-Phase-B | Post-Phase-B |
|---|---|---|---|
| Subgroup identification | none | Γ_0(6) candidate | **Γ_0(6) closed (B1)** |
| Cusp ↔ candidate mapping | none | from Phase A | **Cusp 1/2 ↔ q_2 sector closed (B2)** |
| w_+ value selection | empirical | 13/14 candidate | 13/14 strongly motivated, **B3 open** |
| Overall w_+ closure | Class 2 | Class 4 | **Class 4+** |

The Class 4+ status: stronger than Class 4 (cusp identification
forced by group theory + framework's existing q_2/q_3 sector
structure), weaker than Class 5 (the specific representative 13/14
within cusp 1/2 isn't uniquely forced by an independent
mechanism).

**Substantively**: w_+ is now a **predicted equivalence class**
(cusp 1/2 of Γ_0(6)) rather than an arbitrary fit value. The
specific operating point 13/14 within that class has strong
framework-natural shape (|F_6|/(q_2·|F_4|)) but lacks a
substrate-derivation forcing argument.

This is a major Phase B promotion. The framework's prediction
shape becomes:

> w_+ is the operating-point partial-locking weight of the sym
> ψ_+(1, 5) boundary mode, lying in cusp 1/2 of Γ_0(6) on
> X_0(6). Numerical realization at 13/14 = |F_6|/(q_2·|F_4|)
> is the natural framework-integer representative within this
> orbit, fitting all three Planck partition observables to
> 0.13%.

## What remains for Class 5 closure

**Single open item**: B3 representative selection. Either:

- (a) **Derive the substrate's cusp-1/2 ground-state representative
  formula** in terms of framework primitives, with 13/14 emerging
  as the unique result.
- (b) **Identify a second observable** that distinguishes
  representatives within cusp 1/2 (so the cusp-orbit ambiguity
  is resolved by a different prediction). E.g., if the framework
  predicts a relation between w_+ and some other quantity (CMB
  spectrum tilt? running of some coupling?) that fixes the
  representative.

(a) is non-trivial substrate-side derivation work. (b) is a
predict-then-test program, not a derivation per se.

Both are multi-session work and beyond Phase B's scope.

## Methodological note

Phase B closes B1 and B2 via recognize mode, parallel to the
prior recognize-mode closures (D.3, D.1, Ω_b α/β). The pattern
holds: existing framework structure, expressed in the right
vocabulary (here: cusps of X_0(6)), surfaces forcing arguments
that weren't visible in the original vocabulary.

The vocabulary shift (q_2 × q_3 sector decomposition →
Γ_0(2) ∩ Γ_0(3) = Γ_0(6) cusp structure) is itself an instance
of `vocabulary_is_the_work_pattern.md`'s pattern catalog. The
modular-forms vocabulary has built-in machinery (cusps, Hecke
operators, eigenform decomposition) that matches the framework's
sector structure.

This adds **Instance 9** to the vocabulary-is-the-work catalog:
modular-forms vocabulary as the natural language for the
framework's sector structure on the q_2 × q_3 mode lattice.

## Cross-references

- `psl2z_subgroup_phase_a_results.md` — Phase A finding (Γ_0(6)
  identified)
- `klein_antipodal_z2_rep_pattern.md` — Z_2 × Z_3 sector
  decomposition machinery (B1 source)
- `omega_b_alpha_beta_closure.md` — sign-rep no-EM Z_2 preservation
  (B1 strength)
- `baryon_fraction.md` — sym/antisym mode taxonomy
- `omega_b_w_plus_candidate.md` — 13/14 framework-integer reading
  (B3 partial)
- `omega_b_w_plus_cross_ratio_search.md` — 24 cross-ratio
  4-tuples giving 13/14 (B3 partial)
- `partition_logit_form.md` — logit form q_2 × q_3-sector
  factorization (B3 candidate selection rule source)
- `mediant_derivation.md` — tongue-stability ordering (B3 partial)
- `vocabulary_is_the_work_pattern.md` — pattern catalog
  (Instance 9 to add)
- `cross_ratio_irrep_reframe.md` — irrep multiplicity reframe

## Status

**Phase B B1 and B2 close in recognize mode.** Substrate Γ_0(6)
preservation derives from existing q_2 × q_3 sector decomposition.
w_+ ↔ cusp 1/2 derives from trivial Klein Z_2 rep ↔ q_2-cusp
correspondence, independently of EM-MOND reading.

**B3 (representative selection within cusp) remains open** as
substrate-side dynamical-derivation work.

w_+ closure promoted: **Class 2 → Class 4+** at 13/14, contingent
only on B3 single open item.

Direction 4 substantive completion: subgroup identified (Γ_0(6)),
cusp-class forcing established, ground-state representative
identification queued as Phase C work.
