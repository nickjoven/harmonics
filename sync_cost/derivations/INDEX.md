# Derivation Index

Canonical map from derivation D-numbers to filenames under this directory.
`MANIFEST.yml:scorecard.*.source` lists derivations as either D-numbers
(e.g. `D25`) or bare filename stems (e.g. `farey_partition`).  Bare
stems resolve directly via `{name}.md` or `{name}.py`; D-numbers
resolve via this file.

Two layers of provenance:

- **primary** — the mapping is asserted by an explicit `**Dn** (`file.md`)`
  citation in another derivation.
- **inferred** — the mapping follows from MANIFEST scorecard usage
  + subject-matter match.  Named here to make the inference
  auditable.

If a mapping here is wrong, the fix is one line in this file plus the
failing MANIFEST source.  If a new derivation gets a D-number, append
it below (and keep the D-numbering globally unique).

## Mapping

| D# | File | Provenance |
|----|------|------------|
| D1 | [`born_rule.md`](born_rule.md) | inferred: `MANIFEST.born_rule.source[0]` + subject match |
| D3 | [`a0_threshold.md`](a0_threshold.md) | inferred: `MANIFEST.mond_scale.source[0]` + subject match |
| D4 | [`spectral_tilt.md`](spectral_tilt.md) | inferred: `MANIFEST.spectral_tilt.source[0]` + subject match; also cited in `fermion_mass_running.md:99` for staircase scaling |
| D6 | [`planck_scale.md`](planck_scale.md) | primary: `**D6** (`planck_scale.md`)` |
| D7 | [`address_and_quantity.md`](address_and_quantity.md) | inferred: `MANIFEST.uncertainty.source[0]` + subject (address × quantity = τ·Δθ) |
| D8 | [`a1_from_saddle_node.md`](a1_from_saddle_node.md) | inferred: `MANIFEST.mond_scale.source[1]` + saddle-node → a₀ threshold |
| D9 | [`a1_from_saddle_node.md`](a1_from_saddle_node.md) | inferred: `MANIFEST.born_rule.source[1]` + saddle-node universality → \|ψ\|² |
| D10 | [`minimum_alphabet.md`](minimum_alphabet.md) | inferred: `MANIFEST.efolds.source[0]` + alphabet-depth count drives N_efolds |
| D11 | [`rational_field_equation.md`](rational_field_equation.md) | primary: `**D11** (`rational_field_equation.md`)` |
| D12 | [`continuum_limits.md`](continuum_limits.md) | primary (x2): `**D12** (`continuum_limits.md`)` |
| D13 | [`einstein_from_kuramoto.md`](einstein_from_kuramoto.md) | primary: `**D13** (`einstein_from_kuramoto.md`)` |
| D14 | [`three_dimensions.md`](three_dimensions.md) | primary (x4): `**D14** (`three_dimensions.md`)` |
| D15 | [`lie_group_characterization.md`](lie_group_characterization.md) | inferred: PROOF_A P6 "SL(2,R) is unique / Bianchi classification" |
| D19 | [`klein_bottle.md`](klein_bottle.md) | primary (x2): `**D19** (`klein_bottle.md`)` |
| D25 | [`farey_partition.md`](farey_partition.md) | inferred: `MANIFEST.dark_energy.source[0]` + "Farey partition" in multiple contexts |
| D26 | [`hierarchy_gaussian_lattice.md`](hierarchy_gaussian_lattice.md) | inferred: `MANIFEST.hierarchy.source[0]` + file title "Planck–Hubble hierarchy from Gaussian lattice" |
| D27 | [`exponent.md`](exponent.md) | inferred: `exponent.md:184` asserts "exponent = q₂ × q₃^d = 54 (D27, derived)"; `MANIFEST.lambda_planck` chains on that exponent |
| D28 | [`omega_partition_combinatorial.md`](omega_partition_combinatorial.md) | inferred: `MANIFEST.dark_energy.source[1]` paired with D25, matching file title "Ω partition: combinatorial derivation at depth 19" |
| D29 | [`mediant_derivation.md`](mediant_derivation.md) | primary: `PROOF_A_gravity.md:P2 [D29]` + `MANIFEST.proof_chains` |
| D31 | [`speed_of_light.md`](speed_of_light.md) | primary (x3): `**D31** (`speed_of_light.md`)` |
| D32 | [`minkowski_signature.md`](minkowski_signature.md) | primary: `**D32** (`minkowski_signature.md`)` |
| D33 | [`duty_cycle_dictionary.md`](duty_cycle_dictionary.md) | primary (x3): `**D33** (`duty_cycle_dictionary.md`)` |
| D34 | [`generation_mechanism.md`](generation_mechanism.md) | primary (x2): `**D34** (`generation_mechanism.md`)` |
| D36 | [`conservation_computability.md`](conservation_computability.md) | primary: `**D36** (`conservation_computability.md`)` |
| D41 | [`discrete_gauge_resolution.md`](discrete_gauge_resolution.md) | inferred: `gauge_sector_lovelock.md:413` "D41 (discrete gauge resolution: center, confinement)" |
| D42 | [`gauge_sector_lovelock.md`](gauge_sector_lovelock.md) | primary (x2): `**D42** (`gauge_sector_lovelock.md`)` |
| D43 | [`gell_mann_nishijima.md`](gell_mann_nishijima.md) | primary (x2): `**D43** (`gell_mann_nishijima.md`)` |
| D44 | [`higgs_from_tongue_boundary.md`](higgs_from_tongue_boundary.md) | primary (x2): `**D44** (`higgs_from_tongue_boundary.md`)` |
| D45 | [`coupling_scales.md`](coupling_scales.md) | primary: `**D45** (`coupling_scales.md`)` |
| D47 | [`baryon_fraction.md`](baryon_fraction.md) | inferred: `MANIFEST.{dark_matter_fraction,baryon_fraction,dm_baryon_ratio}.source[0]` + file title "Baryon fraction" with Ω partition 13:5:1/19 |
| D48 | [`spatial_coupling_derived.md`](spatial_coupling_derived.md) | primary: `**D48** (`spatial_coupling_derived.md`)` |
| D49 | [`beta_from_tongues.md`](beta_from_tongues.md) | primary: `**D49** (`beta_from_tongues.md`)` |

## Not mapped

- **D37** — referenced only by the demoted `weinberg_angle` entry
  (removed from `MANIFEST.yml:scorecard` per the honest-null
  resolution; the bare identity is now under `bare_k1_identities.sin2_theta_W`).
  No canonical file; mapping unnecessary.

- **D2, D5, D16–D18, D20–D24, D30, D35, D38–D40, D46** — unused in
  `MANIFEST.yml:scorecard` at the time of writing.  Some have
  in-text citations (e.g. `D21`, `D24`) but are not MANIFEST sources,
  so their resolution is not required for `check_manifest.py` to
  pass.  If any of these are later referenced in MANIFEST, add the
  mapping here.

## How this file is consumed

`scripts/drift/check_manifest.py` parses the first column of the
mapping table (a `Dn` token) and the first `[…](file.md)` link in
the second column.  The parse is tolerant — any D-row that does not
match the pattern is ignored — so freeform commentary may be added
without breaking the resolution.
