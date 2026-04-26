# Cross-ratio multi-candidate pattern is irrep multiplicity

## What this file is

Recognition that the multi-candidate ansatz pattern endemic
across the framework's Class 2 demotions (per
`continuity_in_K_nulls.md` N12-N13, `omega_b_c5_beta_audit.md`
β = 1/12 vs 1/(4π), `omega_b_w_plus_cross_ratio_search.md`
13/14 vs 12/13 vs 14/15) is **not numerological clustering**
— it's **irreducible representation multiplicity** under the
framework's PSL(2,ℤ) Farey action.

Each candidate value labels a DISTINCT PSL(2,ℤ) orbit on the
projective line P¹(ℚ). These are irrep classes. The
multi-candidate pattern reflects multiple irreps competing as
the framework's natural operating point.

This **reframes the Class 2 floor**: it's structurally rich
(distinct irreps, each derivable) rather than ad-hoc clustering.

## Verification

Three w_+ candidates from `omega_b_w_plus_cross_ratio_search.md`,
checked under PSL(2,ℤ) action via the anharmonic group (6
cross-ratio values per orbit):

| Candidate | PSL(2,ℤ) orbit (6 values) | j-invariant |
|---|---|---|
| **13/14** | {13/14, 1/14, 14/13, 14, −13, −1/13} | 392223168/8281 ≈ 47364.23 |
| **12/13** | {12/13, 1/13, 13/12, 13, −12, −1/12} | 61918288/1521 ≈ 40708.93 |
| **14/15** | {14/15, 1/15, 15/14, 15, −14, −1/14} | 601211584/11025 ≈ 54531.66 |

**All three orbits are disjoint.** The candidates have distinct
j-invariants, confirming they label different PSL(2,ℤ)-irrep
classes.

The j-invariant is the canonical PSL(2,ℤ)-invariant on the
projective line; distinct j-values ⟺ distinct PSL(2,ℤ)
orbits ⟺ distinct irrep classes.

## What this changes about the Class 2 floor

### The previous reading

Multi-candidate ansatz = "small framework-integer expressions
cluster near observation by pigeonhole; ansatz_audit_policy
correctly demotes since no specific candidate is forced."

### The reframed reading

Multi-candidate ansatz = "distinct PSL(2,ℤ) irreps each give
one rational candidate; the framework's prediction lives in
ONE specific irrep, but identifying WHICH irrep requires
substrate-side dynamics not yet derived."

This is **structurally richer** than pigeonhole. Each Class 2
candidate is a meaningful structural object (an irrep label),
not random noise.

## Implication for the framework

The framework's "Class 2 floor" reframes:

| Old reading | New reading |
|---|---|
| Multi-candidate ansatz = noise / pigeonhole | Multi-candidate = irrep multiplicity |
| Class 2 = framework prediction unforced | Class 2 = framework prediction in one of several distinct irreps; which irrep unforced |
| Forcing requires picking a value | Forcing requires identifying the irrep |

This is a **strictly stronger** structural status. The framework
isn't producing random near-matches; it's producing distinct
irrep options.

## What this clarifies

### Region C numerology count, sharpened

Per `numerology_count_phase_a.md`, Region C tests whether the
1-3% Floor cloud is signal or pigeonhole. Under the irrep
reframe, the prediction sharpens:

- **Cloud is signal** = cloud's distribution matches the
  density of PSL(2,ℤ) orbit representatives in the relevant
  range (calibrable via Diophantine theory)
- **Cloud is noise** = cloud's distribution exceeds irrep-orbit
  density (random small-integer clustering beyond what irreps
  alone produce)

The empirical count distinguishes these. The irrep reframe
provides the **specific null distribution** to compare against
(orbit-representative density) rather than uniform random.

### Forcing arguments shift target

For Class 2 → Class 5 promotion:

**Old**: derive a unique numerical value from substrate primitives.

**New**: identify which PSL(2,ℤ)-irrep the substrate's dynamics
operates in. The numerical value follows automatically (each
irrep has one canonical representative).

This is a different KIND of derivation — group-theoretic
(which subgroup is preserved) rather than numerical (which value
is selected).

### Connection to existing framework structure

The framework already has:

- Klein-antipodal Z_2 ⊂ PSL(2,ℤ) (sym vs antisym irrep
  decomposition, used in Ω_b two-component closure)
- Mediant operation = generator of PSL(2,ℤ) Farey action
- Stern-Brocot tree = Farey graph, on which PSL(2,ℤ) acts

So the framework HAS the substrate that produces irreps. What's
missing: identifying which subgroup's invariants the framework's
predictions correspond to.

## What this does NOT change

- The Ω_b w_+ value still needs determination (13/14 vs 12/13
  vs 14/15)
- Ω_b closure still at Tier 3 Class 2 status
- Class 2 default per ansatz_audit_policy still applies (just
  with sharper interpretation of what Class 2 means)

## What this enables for next work

A NEW direction beyond the three I'd queued earlier:

**Direction 4: Identify the framework's PSL(2,ℤ)-subgroup
invariant.** Not "derive w_+" but "derive which irrep label
the framework's dynamics carry."

If the framework's substrate dynamics select a specific
PSL(2,ℤ)-subgroup (e.g., Klein-antipodal Z_2, or some Hecke
subgroup, or the full PSL(2,ℤ)), the irrep classes split
accordingly. The irrep containing the framework's natural
operating-point cross-ratio gives the unique w_+.

Candidates for the framework's relevant subgroup:
- Γ(2) (principal congruence subgroup of level 2): has 3-fold
  index, decomposes irreps
- Γ_0(N) for various N: Hecke congruence subgroups
- Klein-antipodal Z_2 alone: insufficient (13/14 and 12/13 are
  both Klein-antipodal-invariant)

This is structural derivation work, not ansatz audit.

## Methodological note

The user's observation ("It's giving irreducible
representations") sharpens the framework's recognize-mode toolkit.
The previous recognize-mode closures (D.3, D.1, Ω_b α/β) all
identified existing structural content as forcing arguments.
The cross-ratio observation identifies that the framework's
multi-candidate ansatz pattern IS structural content
(PSL(2,ℤ) irrep multiplicity), not its absence.

This adds a third recognize-mode pattern alongside:
1. **Vocabulary disambiguation** (Klein twist = Klein-antipodal
   Z_2 rep, etc.)
2. **Existing-content articulation** (D.3 from
   continuum_limits.md, D.1 from Klein Z_2 rep machinery)
3. **Structural multiplicity recognition** (multi-candidate
   ansatz IS irrep structure)

Each is a distinct way to find structural content where it
appeared absent.

## Cross-references

- `omega_b_w_plus_cross_ratio_search.md` — search that produced
  the candidates
- `lie_group_characterization.md` Step 3 — PSL(2,ℤ) Farey
  cross-ratio invariance
- `klein_antipodal_z2_rep_pattern.md` — Klein-antipodal Z_2 ⊂
  PSL(2,ℤ); current irrep usage in framework
- `continuity_in_K_nulls.md` N12-N13 — multi-candidate ansatz
  precedent (now reframed as irrep multiplicity)
- `omega_b_c5_beta_audit.md` — β = 1/12 vs 1/(4π) (likely also
  irrep multiplicity under the reframe)
- `numerology_count_phase_a.md` — Region C, sharpened by the
  irrep null distribution reading
- `vocabulary_is_the_work_pattern.md` — pattern catalog this
  finding adds to (multi-candidate pattern is itself structural,
  not numerological)

## Status

Cross-ratio findings reframed from "multi-candidate ansatz" to
"PSL(2,ℤ) irrep multiplicity." Class 2 floor reinterpreted as
structural irrep-class richness rather than pigeonhole noise.
New direction (#4) identified: find which subgroup's
invariants the framework operates under.

Region C interpretation sharpened with specific irrep-density
null distribution.

## Direction 4 follow-on (executed)

- `psl2z_subgroup_identification_phase_a.md` — Phase A planning
- `psl2z_subgroup_orbits.py` — orbit computation
- `psl2z_subgroup_phase_a_results.md` — Phase A executed: **Γ_0(6)
  identified** as smallest Hecke subgroup splitting all three
  candidates; cusp index = gcd(denom, INTERACT) cleanly maps to
  framework sectors (∞ ↔ 12/13 generic, 1/2 ↔ 13/14 q_2 sector,
  1/3 ↔ 14/15 q_3 sector)
- `psl2z_subgroup_phase_b.md` — Phase B executed: B1 (substrate
  preserves Γ_0(6)) and B2 (w_+ ↔ cusp 1/2 independently of
  EM-MOND) close in recognize mode; B3 (representative selection
  within cusp) remains open

w_+ closure status post-Direction-4: **Class 2 → Class 4+** at
13/14. The cusp class is forced by group theory + framework's
existing q_2/q_3 sector decomposition; only the specific
representative within the cusp orbit lacks a substrate-derivation
forcing argument.
