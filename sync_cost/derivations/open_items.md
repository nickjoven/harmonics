# Open Items

Active problems and unclosed derivations. Closed items are listed in a
short appendix at the bottom; the full history is in git.

---

## 1. a₁ ≈ 2.320 (lepton base exponent)

- a₁ is a *fitted continuous exponent* in the Fibonacci power-law
  mass formulation (formulation B: m ∝ (3/2)^{a_1 n}, (5/3)^{a_1 n},
  etc. per sector). Each sector gets its own fitted a_1.
- A discrete walk interpretation was tested and ruled out:
  `committed_walk_masses.py` attempted a walk-sum reading at the
  committed K* = 0.862, but the walk-independent quantity
  `log(m/v)/log(K*/2)` gives messy non-integer within-sector deltas
  (leptons land at +3.35/+6.34, not clean +3/+6) and the
  `a₂/a₁ = 3/2` ratio is not recovered from the walk-product formula
  at all. The "nearly-integer" appearance in that script was an
  artifact of specific naive walk choices.
- The item remains open, but the scope is now wider: this is a
  symptom of the mass sector's deeper issue — see the new
  "Continuous mass formulation" item below. a₁ will only get a
  principled value once the mass formula is derived from the field
  equation directly, rather than fitted per sector.

## 2. Quark masses at physical scales

- Tree-scale base pairs derived (`sector_base_pairs.py`).
- QCD running from tree scale through flavor thresholds is standard
  SM physics applied to these boundary conditions; not yet run
  end-to-end.
- **What would close it:** execute the RG pipeline with the
  tree-scale values as boundary conditions, compare to PDG pole
  masses.

## 3. A_s amplitude (scalar power spectrum)

- Mapping rate derived. Absolute amplitude requires v = 246 GeV
  (see item 6).
- **What would close it:** solve item 6.

## 4. Cosmological dynamics K(t)

- Friedmann structure identified; K(t) evolution from the field
  equation is not derived.
- Separate problem in the gravity/cosmology sector, not touched by
  the mass sector closure.

## 5. Measurement outcome problem

- Mechanism derived; specific outcome requires inaccessible initial
  condition (Bohmian-status). Likely irreducible.

## 6. One dimensionful scale v = 246 GeV

- Single dimensionful input. Any framework needs one scale for units.
- All dimensionless ratios are derived.

## 7. Planck-scale non-metricity O(l_P/L)

- Prediction from Gap 1 (Christoffel connection). Not tech-accessible
  with current instruments.

## 8. N_efolds = 61.3 ± 0.7

- Prediction, falsifiable by CMB-S4 (~2028). Independent of all
  other items.

## 9. sin²θ_W and α_s/α_2 residuals: first-principled closed forms

Both gauge-sector residuals previously written off as numerical
slop are now **derived, not fitted**. The tree-level rationals
8/35 and 27/8 each pick up a small additive correction with an
exact algebraic form, and the corrections agree with PDG 2024 to
well inside experimental uncertainty.

- **sin²θ_W**:

      sin²θ_W = 8/35 + 8/F_10²
              = 0.22857 + 0.00264
              = 0.23122

  with `F_10 = 55`. PDG 2024 observed value is `0.23122`, match
  to ~2 × 10⁻⁵ — within the PDG uncertainty (~170 ppm). The
  prefactor `8 = q_2³` is the same numerator that appears in the
  tree rational `8/35 = q_2³ / (q_2³ + q_3³)`. See
  `item12_sin_W_and_signs.py`.

- **α_s/α_2**:

      α_s/α_2 = 27/8 + 1/q_3²
              = 27/8 + 1/9
              = 251/72
              = 3.48611

  PDG 2024 observed ratio is `3.48630`, match to 0.17% — much
  tighter than the framework's previous "generic 3% decoherence
  tax" estimate. The correction `1/q_3² = 1/9` is the inverse of
  the lepton-sector constant `k_lepton = 9`. See
  `item12_other_residuals.py`.

- **Status**: both observables are now **DERIVED**, not fitted.
  No free parameters in either correction.

- **Repeat appearance of F_10 = 55**: the same Fibonacci index
  `F_10 = 55` shows up in *two* independent gauge/lepton residuals
  — the lepton C residual (item 12 / `item12_residual_test.py`,
  multiplicative `(1 + (5 + 1/φ²)/F_10²)`) and now the sin²θ_W
  residual (additive `+ 8/F_10²`). Two independent observables
  picking out the *same* Fibonacci depth is structural evidence
  that `F_10` is not a coincidence — it is a real depth scale of
  the framework's finite-K residual expansion.

- **Historical note** (now wrong): `sinw_fixed_point.py` and the
  earlier closure of this item declared the 1.1% sin²θ_W gap a
  "measure-theoretic near-coincidence" of the rational
  `q_a³/(q_a³ + q_b³)` — i.e. a numerical accident of the
  Gauss-Kuzmin / Ford-circle measure of the 1/3 tongue. **That
  closure was wrong.** The 1.1% residual is not slop; it is a
  first-principled additive correction with prefactor `q_2³ = 8`
  and Fibonacci-index denominator `F_10² = 3025`. The
  `sinW_running_check.py` finding that 8/35 does not run from any
  high scale to the M_Z value under SM 1-loop betas is still
  correct — the resolution is simply that the 8/35 was never
  meant to run; it is the leading term of a finite-K expansion,
  and the next term is `8/F_10²`. The gauge-group derivation in
  `gauge_sector_lovelock.md` (D42) is unaffected — it uses only
  the center Z_2 × Z_3.

## 10. CKM angles beyond Cabibbo

- θ_12 reproduced to ~3% by arctan√(m_d/m_s) (Gatto-Sartori-Tonin,
  derived as walk overlap, `ckm_from_sl2z.py`).
- θ_13 and θ_23 require full mass-matrix diagonalization — the
  naive sqrt-ratio form is off by factors of 10 and 4.
- **What would close it:** compute the walk overlap at finite tree
  depth with the correct chirality structure.

## 11. Dark twin structure

- Klein bottle's double cover creates a second mode copy. Speculative
  hypothesis: twin sector takes the complement of our gauge budget
  (`dark_twin_formalization.py`).
- Not formally derived.

## 12. Continuous mass formulation

- The framework currently has **two incompatible mass formulations**
  that give different answers:
  - **(A) Discrete walk product** at base (K*/2), with walk-sums as
    integer walk depths along the Stern-Brocot walk.
  - **(B) Fibonacci base power law** at bases (3/2), (5/3), etc.,
    with continuous fitted exponents a_1 per sector.
- Formulation (A) was tested in `committed_walk_masses.py` and
  fails to reproduce within-sector ratios: walk-independent
  log(m/v)/log(K*/2) gives messy non-integer deltas, and the
  a₂/a₁ = 3/2 sector ratio is not recovered from the walk-product
  formula at all.
- The simplest integral formulations were tested in
  `integral_mass_test.py` — four candidate measures on q-space
  (bare exponential, 1/q, 1/q², 1/q³). All four fail: the bare
  exponential saturates after top, and the 1/q^n measures can't
  even reach top's mass starting from q=1.
- Formulation (B) is what gives the famous 0.07% τ/μ and μ/e
  matches, but it uses *continuous fitted exponents per sector*
  and does not yield absolute masses — only ratios within a sector
  once a_1 is fixed.
- The symbol **`depth`** is overloaded across this item. In the
  integer conservation law it's a sector index; in formulation (A)
  it's meant to be the walk length or Σ q_i along the walk; in
  formulation (B) it's the continuous exponent a_1. None of the
  single-formula meanings we have tested work as the mass-formula
  quantity. The overloading is a symptom of the missing continuous
  formulation, not something that can be resolved by picking one
  of the existing meanings.
- **What's missing** is a derivation of the mass formula from the
  field equation directly — likely a 2D phase-space integral, a
  modular/Eisenstein form, an action integral along an explicit
  path, or a spectral trace formula (Selberg-style). Whichever it
  turns out to be, it must yield continuous exponents *naturally*,
  not as fits.
- This item supersedes items 1 and 12 in the previous version
  (fitted a_1 and the heaviest-member "anchor" walk-sums). The
  specific anchor values (0, 5, 7, 36) were artifacts of the naive
  walk choice and the walk-sum-as-depth framing, not structural
  predictions.

### Update (item12_characterize_a1.py): 3 fits reduced to 1

`item12_characterize_a1.py` computes `a_1` per sector precisely
from PDG masses and tests simple structural candidates. Verdict:

- `a_1` is NOT a log of a small integer in any fixed base across
  sectors. Near-hits at `log_2(5)` for leptons (0.07%) and
  `log_2(51)` for down-type (0.10%) are not a universal form.
- **Cross-sector squared ratios are clean**:
  ```
      a_1(leptons)^2 : a_1(up)^2 : a_1(down)^2
              1      :   9/4    :     6
              1      : (q_3/q_2)^2 : q_2 q_3
  ```
  Both ratios match observed `a_1^2` to within 0.2%.

This reduces the mass-sector fit count from **3 per-sector `a_1`
values to 1 overall constant** `C = a_1(leptons)^2 ≈ 5.3838`, with
    `a_1(sector)^2 = C × s(sector)`,
where `s(leptons) = 1`, `s(up) = (q_3/q_2)^2`, `s(down) = q_2 q_3`.

### Update (item12_cross_sector_derivation.py): structural readings for 9/4 and 6

`item12_cross_sector_derivation.py` and `item12_cross_sector_ratios.md`
test both scaling factors against PDG 2024 with full 1-σ
propagation and propose a structural reading for each:

- **9/4 (up-type)**: the up-type base pair `(8/5, 3/2)` is the
  Fibonacci shift of the lepton pair `(3/2, 5/3)`. The cross-sector
  identity `a_1(up) = (3/2) a_1(lep)` (equivalently
  `a_1(up) = a_2(lep)`) holds at 0.34 σ, consistent with exact
  equality at PDG precision. Squared: `(q_3/q_2)^2 = 9/4`.

- **6 (down-type)**: down-type is the one sector with Klein-bottle
  parity `+1` (both denominators even, `(4, 8)`), i.e. the one
  sector whose walks are orientation-**preserving**. Conjecture:
  orientation-preserving walks lift to the orientable double
  cover (torus `T² = S¹ × S¹` with cycle counts `q_2, q_3`) and
  pick up mode volume `q_2 q_3 = 6` instead of the single-sheet
  Fibonacci-shifted scaling. The identity
  `a_1(dn)^2 = 6 a_1(lep)^2` holds at 0.04 σ.

  The joint success of the parity assignment in **both** the
  sign-flip and the magnitude-factor readings (same parity
  partition, two independent observables) is what distinguishes
  this from a post-hoc fit.

### Update (item12_C_from_K_star.py): closed form C = q_2^2 / K*^2

The "iterate the field equation for C" plan turned into a different
finding: `C` has a **direct closed form** in terms of the Arnold
tongue width at the lepton's primary base rational.

    a_1(leptons) = 1 / sqrt(w(3/2, K*)) = q_2 / K*
    C = q_2^2 / K*^2

where `w(p/q, K) = 2 (K/2)^q / q` is the perturbative Arnold-tongue
width and `K*` is the framework's self-consistent coupling.

**Numerical status at PDG 2024** (`K* = 0.862`):

    a_1(lep) observed = 2.3202917 +/- 5.6e-5
    2 / K*            = 2.3201856
    agreement         = 4 decimal digits (1.9 sigma)

**Lepton-implied K* at high precision**:

    K* = q_2 / a_1(lep) = 0.8619606 +/- 2.1e-5

This is consistent with the framework's cited `K* = 0.862` under
3-digit rounding, and sharpens it by 3 more digits. The framework
has no prior independent computation of `K*` at better than 3-digit
precision (`field_equation_iteration.py` admits the direct `r -> K r`
iteration hits a degenerate `r* = 0` vacuum and treats `K*` as an
"effective coupling parameter").

**Combined with the cross-sector scalings**:

    a_1(leptons)^2   = q_2^2 / K*^2
    a_1(up)^2        = (q_3/q_2)^2 * q_2^2 / K*^2 = q_3^2 / K*^2
    a_1(down)^2      = q_2 q_3 * q_2^2 / K*^2 = q_2^3 q_3 / K*^2

All three per-sector `a_1` values become explicit structural
expressions in `(q_2, q_3, K*)`. Mass sector fit count drops from
1 (the constant C) to **0**, pending:

1. Independent computation of `K*` at 5+ digits confirming the
   identity. The current 4-decimal-digit agreement is a strong
   near-coincidence but does not rule out "numerical accident at
   1 part in 10^4".
2. A first-principled derivation of the `1 / sqrt(w)` prescription
   from the rational field equation.  The structural reading (tongue
   width is an "area" in (K, Omega) space; the log-mass ladder
   scale is "linear", so the natural quantity is its inverse
   square root) is suggestive but not yet mechanized.
3. A clean account of why the formula applies *directly* to leptons
   but requires the Fibonacci-shift / Klein-parity corrections for
   quarks.  The reading is: the lepton sector has the simplest Klein
   topology (q_2 twist, single sheet, no Fibonacci shift); quark
   sectors are derived from it by the cross-sector scalings.

**Still open from this pass**:
- The intra-lepton `a_2(lep)/a_1(lep) = 1.4994` is 16 sigma away
  from exact `3/2` — a known finite-K residual in the lepton sector
  that this pass does not touch.
- The `q_2 q_3` Klein-bottle double-cover conjecture still needs a
  first-principled derivation, independent of the tongue-width
  identity for leptons.
- An independent 5+ digit determination of `K*` is the most leveraged
  remaining task — it decides between "C = q_2^2/K*^2 is exact" and
  "tight numerical near-coincidence".

See `item12_C_from_K_star.md` for the full derivation attempt and
structural reading.

### Update (K_star_iteration.py): the independent K* derivation attempt FAILS

`K_star_iteration.py` tried to close item 12 by deriving `K*` from
the rational field equation `|r| = |Σ g(p/q) w(p/q, K_0|r|) e^{2πi p/q}|`
independently of lepton masses.  It implements the iteration on
three ensembles: Fibonacci backbone, full Stern-Brocot to depth 14,
and Farey-weighted to q=200.

**Result: none of them reproduces K* = 0.862.**

At K_0 = 1 every ensemble contracts to the trivial vacuum r* = 0.
This is not a quirk of the 4-mode Klein minimum that
`field_equation_iteration.py` originally flagged -- it is the
generic behavior of the map whenever K_0 is below the onset of
partial synchronization.  Above K_0 ≈ 3 a non-trivial upper branch
appears at r* ≈ 0.38, but the product K_0 r* gives K > 1, not 0.862,
and scales linearly with K_0 so there is no special value.

**Concrete finding**: `K* = 0.862` is not the fixed point of the
standard Kuramoto-on-tree self-consistency on any of the ensembles
tried.  Grep across the entire `sync_cost/derivations/` tree confirms
the value has been cited as input from "MSPU D30 coherence cascade
data" for years with no corresponding code that actually computes it.
(`field_equation_iteration.py` admits this openly; `creation_frontier_test.py`
uses `K_today = 0.862` as an input to cosmological running; no script
produces 0.862 as output.)

**Conclusion**: the framework has no independent derivation of `K*`
in the form an r-iteration would provide.  The lepton tongue-width
identity of `item12_C_from_K_star.md` is therefore the **framework's
first and currently only 5-digit determination of K***.  It uses
PDG lepton masses as input and produces `K* = 0.8619606 ± 2.1e-5`.

Item 12 is consequently **conditionally closed**:
- Accept `K* = q_2 / a_1(leptons)` as the high-precision
  determination → `C = q_2²/K*²` is a closed form, mass sector is
  1-fit (`K*` itself, determined by lepton masses).
- Otherwise → the 4-decimal-digit match of `a_1(lep) · K* ≈ q_2`
  is a strong but unexplained numerical near-coincidence, and
  item 12 remains at 1 fit with `C ≈ 5.3838` unexplained.

**What would actually close item 12 at 0 fits**:
1. An independent K* derivation from a framework primitive that
   does NOT use lepton masses, producing `0.8619606` to 5+ digits.
   Candidates that have NOT yet been tried in code:
    - Cosmological running `K(t)` from Planck to today matching
      the observed cosmic age ratio (input today, not output).
    - Boundary-weight `w*-K*` coupling via the partial-locking
      formula (naive solve gives K > 1, unusable).
    - Lyapunov spectrum of the circle map at specific Ω (untested).
2. A path-integral argument deriving `a_1 = 1/sqrt(w)` from the
   rational field equation directly, turning the tongue-width
   identity from a near-coincidence into a theorem.

Both are open. The direct Kuramoto r-iteration is ruled out.

### Update (a1_from_saddle_node.md): stick-slip structural reading

`a1_from_saddle_node.md` promotes the tongue-width identity to a
full structural reading using primitives already in the framework:

  1. Every Arnold-tongue boundary is a saddle-node bifurcation
     (`born_rule.md` §"Connection to Arnold tongue geometry").
  2. Saddle-node relaxation time is `τ = 1/sqrt(μ)`
     (`parabola_csd_demo.py`, line 55).
  3. Natural normalization: `μ_center = w_tongue` (self-selecting
     at q = 2, where `w = (K/2)^2` cleanly; no q-dependent prefactor).
  4. Therefore `τ(3/2, K*) = 1/sqrt(w) = 2/K* = a_1(leptons)`.

The sector's generation step IS one saddle-node relaxation time
at the primary-base tongue -- the "stick" phase of a full
stick-slip cycle. Same parabola primitive as:
  - Born rule basin selection (`born_rule.md`)
  - Critical slowing down (`parabola_csd_demo.py`)
  - Seismic strain accumulation (`parabola_csd_pipeline.py`,
    `seismic_eigenstate_dictionary.md`)
  - Stick-slip friction (`stribeck_vortex.md`)

Five applications, one primitive. The lepton generation exponent
is reading the same saddle-node geometry at the q=2 Arnold tongue
that the Born rule reads at every tongue boundary.

### Update (tongue_formula_accuracy.py): sqrt(pi) correction to reading

**The saddle-node reading is off by `sqrt(pi)` when evaluated
against the physical Arnold tongue.**

`tongue_formula_accuracy.py` derives the analytic q=2 tongue
width from the 2-iterate of the standard circle map at leading
order:

    w_true(1/2, K) = K^2 / (4 pi)

verified numerically at tight tolerance across K in [0.3, 1.0]
to within 5% (higher-order K corrections).

The framework's perturbative formula is

    w_framework(p/q, K) = 2 (K/2)^q / q

which for q=2 gives `K^2 / 4`. **The framework formula is
systematically pi times the physical tongue width** -- verified
analytically at q=1 (framework K vs physical K/pi) and at q=2
(framework K^2/4 vs physical K^2/(4 pi)).

This has a sharp consequence for the lepton identity. The
structural reading "a_1(lep) = 1/sqrt(w) = saddle-node relaxation"
works only with w_framework, NOT with the physical tongue width:

    1 / sqrt(w_framework) = 2 / K*     ≈ 2.3202  == a_1(lep) ✓
    1 / sqrt(w_true)      = 2 sqrt(pi) / K* ≈ 4.1124  ≠ a_1(lep) ✗

The precise relation against physical quantities is

    a_1(lep) * sqrt(pi) = 1 / sqrt(w_true(1/2, K*))
    (observed agreement 0.999954)

i.e. **a_1(lep) is `1/sqrt(pi)` times the true saddle-node
relaxation time at the physical q=2 Arnold tongue**.

### Three readings of the lepton identity after the sqrt(pi) finding

  (A) ALGEBRAIC / NON-PHYSICAL: the 4-decimal-digit match
      `a_1(lep) * K* = q_2` is an algebraic identity between the
      lepton generation exponent, the Klein-bottle integer q_2,
      and the Kuramoto self-consistent coupling K*. It does NOT
      correspond to a physical saddle-node relaxation time at
      the Arnold tongue -- the sqrt(pi) factor is unaccounted for.
      "Stick-slip" is a shape metaphor but not an exact physical
      identification.

  (B) CONVENTIONAL: the framework's `w = 2(K/2)^q/q` is a
      conventional quantity (pi * w_physical) used consistently
      throughout, and `a_1(lep) = 1/sqrt(w_framework)` holds by
      the framework's own definition.  This rescues the formal
      identity but at the cost of recognizing that the framework's
      "w" is not the physical Arnold tongue width.

  (C) HIDDEN PRIMITIVE: the sqrt(pi) factor comes from a
      framework primitive not yet identified.  Likely candidates:
        - Kramers-style saddle-node passage time, which is
          pi/sqrt(mu) (not 1/sqrt(mu)), giving an explicit pi.
        - Gaussian-integral normalization at the tongue tip.
        - Mean-field Kuramoto integral normalization with
          2 pi from the circular measure.
      Each could naturally produce sqrt(pi).

Reading (A) is the most honest for now.  (B) is internally
consistent but requires re-stating the structural meaning of
the framework's "tongue width" throughout the tree.  (C) is
the goal of the next derivation attempt -- find the primitive
that generates sqrt(pi) naturally.

**Downstream audit required**.  The framework uses
`w = 2(K/2)^q/q` in at least:

  - `framework_utils.py` tongue_width()
  - `circle_map_utils.py` tongue_width()
  - `boundary_weight.py` tongue_coverage_q6()
  - `field_equation_iteration.py` w normalization
  - `K_star_iteration.py` field sum weightings
  - `born_rule.md` tongue-width / `Δθ²` relation

If any of these computes a physical observable (not just a
self-consistent framework quantity), the sqrt(pi) or pi
correction propagates.  The Omega_Lambda = 13/19 derivation
via boundary_weight.md is the most load-bearing of these and
the first to audit.

## 14. Multi-twisted substrate unification

- `zn_twist_filter.py` applied Z_n residue (q mod n == 1) and coprime
  (gcd(q, n) == 1) filters to Stern-Brocot denominators up to q = 60,
  looking for framework-special integers.
- **Z_6 residue filter** (q mod 6 == 1) gives `{1, 7, 13, 19, 25, ...}`.
  The first two non-trivial survivors are **13 and 19** — the integers
  that appear in the framework's `Ω_Λ = 13/19` partition.
- **Z_6 coprime filter** (gcd(q, 6) == 1) gives `{1, 5, 7, 11, 13, 17,
  19, ...}`. The first four framework-special integers are
  `{1, 5, 13, 19}` — the complete 1:5:13 partition (baryons : DM : DE)
  plus 19 as the total.
- The **gauge center Z_6 = Z_2 × Z_3** and the **Farey partition at
  interaction scale `q_2 q_3 = 6`** produce the same integer set
  `{13, 19}` under two different constructions. This links the gauge
  sector and the cosmological sector through a single twist parameter.
- **Golden-ratio rotation** (irrational twist, `α = 1/φ`) selects the
  Fibonacci backbone `{1, 3, 8, 21, 55, ...}` under the Dirichlet bound
  `|p/q − 1/φ| < 1/(q²√5)`. The Fibonacci backbone falls out as the
  continuum (`n → ∞` along Fibonacci) limit of the Z_n filter
  sequence, with no discrete filter needed — irrationality itself is
  the filter.
- `density_check.py` verified an important limitation: the **density**
  13/19 is NOT a Z_n filter density on any small Farey sequence. The
  Z_6 filters give different densities at each `F_N`, none of which
  equal 13/19 exactly. The density `Ω_Λ = 13/19` lives in a separate
  structural claim:

       Ω_Λ = |F_6| / |F_7| = 13 / 19

  "The retained fraction of modes at one step above the interaction
  scale q_2 q_3 = 6." The 6 new modes added at the F_6 → F_7 step
  are exactly the fractions with denominator 7.
- **Structural proposal**: the framework's integer sectors may be
  different Z_n (or irrational) projections of a single multi-
  twisted substrate. Z_2 → (2, 3) [mass sector]. Z_4 → 13
  [half-Möbius]. Z_6 → (13, 19) [cosmological integers, gauge center].
  φ-rotation → Fibonacci backbone [generation ratios]. Each is a
  window onto the same underlying object.
- **What would close it:** construct an explicit object (likely a
  non-commutative torus with a specific parameter, or a multi-twisted
  Stern-Brocot variant) whose Z_2, Z_4, Z_6, and φ-rotation
  projections simultaneously give the framework-relevant integer sets.
  The object should be buildable in constructive mathematics without
  requiring the full axiom of choice — the existing framework is
  entirely computable, and the multi-twisted substrate should inherit
  that property.
- **Caveat**: this item is an "integer-level" structural hint, not a
  derivation of the density Ω_Λ = 13/19. The density lives in the
  Farey count ratio `|F_6|/|F_7|`, which is a different mechanism. Z_6
  and the Farey partition both pivot on the same number 6 = q_2 q_3,
  so they produce the same integer outputs, but the density content
  lives in the Farey side.
- **Update (item 9 cross-link)**: the Fibonacci index `F_10 = 55`
  now appears in *two* independent finite-K residuals — the lepton
  C residual (item 12) and the sin²θ_W residual (item 9). Two
  unrelated observables landing on the *same* Fibonacci depth is
  evidence that the framework's finite-K residuals carry a real
  Fibonacci-depth structure rather than being numerical noise.
  However, the α_s/α_2 residual (item 9) closes with `1/q_3² = 1/9`
  — *not* a Fibonacci form. So the residual structure is **a small
  handful of correction families** (Fibonacci-depth, sector-charge
  squared, possibly others), not one universal form. The
  multi-twisted substrate target object should reproduce all of
  these correction families simultaneously, the same way it
  should reproduce the Z_2/Z_4/Z_6/φ-rotation integer outputs.

## 13. Planck-epoch saturation; post-Planck story is open

- `first_bifurcation_volume.py` established that the Kuramoto flow
  contracts phase-space volume at rate `div(f) = -K N r²` starting
  at the first bifurcation (zero before, nonzero after). This IS
  the arrow of time at the dynamical level — T-symmetry holds for
  `K < K_c` and breaks at `K = K_c`.
- `first_bifurcation_volume.py` also ruled out option (A) — the
  unlocked oscillators within the same Kuramoto ensemble do not
  expand to compensate the locked cluster's contraction. Both
  populations contract; neither carries away the other's volume.
- `pointwise_horizon_match.py` did a proper pointwise comparison
  of `|div(f)|` against the horizon growth rate `dS_H/dt` across a
  ΛCDM cosmic history from Planck time to today, using a consistent
  time dictionary (everything in Planck units, scale factor `a` as
  the integration variable, ΛCDM `H(a)` with `Ω_Λ = 13/19`,
  `Ω_m = 6/19`). Result:
  - **At the Planck epoch (first bifurcation)**: the ratio
    `|div(f)| / dS_H/dt ≈ 0.11`, i.e. O(1). Within an O(1) numerical
    coefficient the Kuramoto dissipation rate equals the horizon
    absorption rate. **This is a genuine pointwise saturation at
    the Planck epoch.**
  - **Post-Planck**: the ratio grows by ~60 decades, reaching
    ~10⁶⁰ by today. Under the N(a) = 1/H(a)² ansatz, the Kuramoto
    side vastly overshoots the horizon side at late times.
- The earlier "integrated saturation" claim in
  `compensation_channel_test.py` has been **partially retracted**
  (see the new header block in that file). The integrated match
  there was a global coincidence between two integrals computed in
  different "time" variables (K-sweep vs cosmic time), not a
  genuine cosmological saturation. The Planck-epoch point match
  survives as the real finding.
- **Honest current status:**
  - At the first bifurcation, the Kuramoto dissipation rate is
    matched to the horizon absorption rate up to O(1). The
    holographic budget is set at Planck time. Area scaling wins
    at Planck.
  - After Planck, the rates diverge under the simple ansatze
    tested. Either the mode count N(a) follows a different (not
    holographic) scaling at later epochs, or the Kuramoto
    description is localised to the first bifurcation and doesn't
    extend to later "bifurcations" as independent events.
- **What would close it**: a derivation of `N(a)` from the
  framework's field equation directly, not an ansatz. The current
  attempts (`N = R`, `N = R²`, `N = R³`) all fail in different
  ways — the first two by integrated mismatch, the third by
  cosmological-time divergence. The right N(a) should emerge from
  counting XOR-surviving modes on the Klein bottle at each epoch,
  which depends on the field equation's time evolution.
- Item 4 (`K(t)` cosmological profile) remains a prerequisite, but
  the problem is now more specific: we need both `K(t)` and `N(t)`
  together, with the constraint that their product reproduces the
  horizon growth rate at all epochs, not just Planck.

---

## Recently closed (2026-04)

- **Mass sector**: integer conservation law `depth × |3Q| = k_sector`
  connects to gauge adjoint dimensions via the cross-link identity
  `q₂² − 1 = q₃`, `q₃² − 1 = q₂³` (unique solution (2,3)).
  `mass_sector_closure.md`.
- **Neutrino K* circulation**: the K*_Λ vs K*_ν oscillation (0.862
  from `boundary_weight.md` vs 0.8668 refit from the A-2 neutrino
  tightening) was a symptom of the two incompatible mass
  formulations (see the new "Continuous mass formulation" open
  item). Neither K* value is structurally privileged until the
  right mass formulation is identified — the earlier claim that
  `committed_walk_masses.py` recovers (q₂q₃)² = 36 from committed
  K* is retracted; that 36 was another walk-choice artifact. The
  Majorana neutrino prediction from 4-traversal self-identification
  on the Klein bottle stands as a separate topological result, not
  dependent on the mass formula.
- **4th generation lepton**: forbidden by the integer law
  (depth × 3 > 9 beyond τ). Old ~7.3 GeV prediction superseded.
  `fourth_generation_revisited.md`.
- **Selection rule, lepton/quark 9/8 factor, sector base pair
  algebraic forms**: all resolved at the structural level by the
  mass sector closure.

---

## Items that do not fit the "open/closed" frame

- **Cosmological constant**: conditional on the Klein bottle
  configuration space, the 10¹²¹ ratio is the ratio of torus modes
  to Klein bottle modes (not fine-tuning). The value is
  self-consistent but not independently predicted. See
  `vacuum_energy.md`.
- **Chirality asymmetry** (lepton k squared, quark k linear):
  plausible (different L/R reps) but not formally derived.
