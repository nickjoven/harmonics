# The Duty Cycle Dictionary

## Status (honest-null resolution)

The bare K=1 identities in this file — sin²θ_W = 8/35, α_s/α_2 = 27/8,
1/α_em = 35, m_H/v = 1/2, λ = 1/8 — have been **demoted from framework
predictions to K=1 reference identities** in `MANIFEST.yml`. They now
live under `bare_k1_identities` rather than `scorecard`. The framework
does not supply a scale-consistent derivation connecting them to M_Z
observations: the K → μ mapping (§7) does not jointly fit multiple
observables with a single K*, and SM 1-loop running goes the wrong
direction for sin²θ_W from any framework-internal tree scale
(`sinW_running_check.py`, `sinw_fixed_point.md`,
`numerology_inventory.md`). Section-level headings throughout this
file have been updated accordingly.

The dictionary's mathematical content — duty(q) = 1/q^d at K = 1 — is
unchanged and rigorous; it is a consequence of the Gauss-Kuzmin
measure on Farey rationals (`duty_dimension_proof.md`).

## Claim (original, at K = 1 only)

At critical coupling K = 1, the gauge coupling constants of the
Standard Model are numerically equal to specific gate duty cycles of
the Stern-Brocot tree. The coupling of each sector is the duty cycle
of its *partner* sector. All ratios, mixing angles, and the Higgs
mass identities follow from integer arithmetic on the denominators
q = 2 and q = 3.

Originally, the 1-3% residuals to M_Z observations were attributed
to a "decoherence tax" from unlocked modes at K < 1. That attribution
has since been ruled out (§7 and cross-references above); the
residuals are unresolved gaps, not derived corrections.

This file formalizes the K = 1 identities computed in
`gate_duty_cycle.py`, `gate_duty_predictions.py`, and
`decoherence_correction.py`.

---

## 1. The duty cycle: duty(q) = 1/q^d

The gate duty cycle is the fraction of time a sector's gate is open:

    duty(q) = w(q, K) / T(q)

where w is the Arnold tongue width (gate duration) and T = q is the
orbit period (gate repetition interval). At K = 1 (critical coupling):

    w(q) = 1/q^2       (Ford circle diameter, Gauss-Kuzmin measure)
    T(q) = q            (period of a p/q orbit)
    duty(q) = 1/q^3     = 1/q^d

The exponent equals d = 3, the spatial dimension.

**This is proved in `duty_dimension_proof.md`.** The exponent is not a
coincidence. The duty cycle is the d-dimensional volume density at the
Stern-Brocot cusp: a density on a d-dimensional manifold scales as
1/(characteristic length)^d. The factorization into tongue width
(transverse density, 1/q^2) and period (longitudinal density, q) is the
Iwasawa decomposition of SL(2,R) into cusp directions and orbit
directions (D14).

More precisely: duty(q) = 1/q^(dim SL(2,R)) = 1/q^(n^2-1) at n = 2.
The tongue width contributes n^2 - n = 2 to the exponent (the positive
roots of A_1), and the period contributes n - 1 = 1 (the rank).

---

## 2. The coupling ratio: alpha_s / alpha_2 = 27/8 (bare K=1 identity)

**Status: bare reference only, not a prediction at M_Z.** Same honest-
null treatment as §3 (sin²θ_W): declined in `MANIFEST.yml` and recorded
under `bare_k1_identities.alpha_s_over_alpha_2`. See
`numerology_inventory.md` §Class 3.

The two physical sectors of the Klein bottle (D19) have denominators
q_2 = 2 and q_3 = 3. Their duty cycle ratio:

    duty(q_2) / duty(q_3) = (1/q_2^3) / (1/q_3^3)
                           = q_3^3 / q_2^3
                           = 27 / 8
                           = 3.375

Observed at M_Z: α_s/α_2 = 0.1179 / 0.03380 = 3.488. Gap 3.2%. The
framework supplies no scale-consistent derivation connecting the bare
K=1 ratio to the M_Z observation; same obstruction as sin²θ_W
(SM 1-loop running does not close the gap from any framework-internal
tree scale).

---

## 3. The Weinberg angle: sin^2(theta_W) = 8/35 (bare K=1 identity)

**Status: bare reference only, not a prediction at M_Z.** The framework
currently declines to predict sin²θ_W at the electroweak scale. See
`sinw_fixed_point.md` (K-scanning ruled out), `sinW_running_check.py`
(SM 1-loop running ruled out — the sign is wrong), and
`numerology_inventory.md` §Class 1.

The bare K=1 identity follows from the duty dictionary:

    sin^2(theta_W) = duty(q_3) / [duty(q_2) + duty(q_3)]
                   = (1/q_3^3) / (1/q_2^3 + 1/q_3^3)
                   = q_2^3 / (q_2^3 + q_3^3)
                   = 8 / (8 + 27)
                   = 8 / 35
                   = 0.22857...

Equivalently:

    sin^2(theta_W) = 1 / [1 + (q_3/q_2)^3]
                   = 1 / [1 + (3/2)^3]
                   = 8 / 35

Observed at M_Z (MS-bar): 0.23121. The 1.1% gap to observation has no
scale-consistent derivation in the framework: SM 1-loop running from
Planck runs sin²θ_W in the *wrong direction*, K-scanning finds no
K* ∈ [0.93, 0.99] reproducing either constraint, and the d_eff = 80/27
correction in `sinw_effective_dimension.md` is conditional on three
unformalized steps. The 8/35 value is recorded as a K=1 reference
identity, not a prediction at M_Z.

---

## 4. The crossed dictionary

The coupling constant of sector q is the duty cycle of its **partner**
sector, not its own:

    alpha_s = duty(q_2) x |r|      (strong coupling from weak gate)
    alpha_2 = duty(q_3) x |r|      (weak coupling from strong gate)

You reach the strong sector through the weak gate and vice versa.

**Origin.** This comes from the Stribeck lattice result
(`decoherence_correction.py`): in a driven lattice of oscillators,
element 1 (the drive end) sets the coupling properties of element N
(the free end). The output coupling is determined by the input's gate
properties. On the Klein bottle (D19), the two sectors q = 2 and q = 3
are the two ends of the lattice, connected by the non-orientable
identification. The coupling OF sector 3 is set BY the gate availability
OF sector 2, and vice versa.

Numerical verification (`decoherence_correction.py`):

    duty(2) / alpha_s = duty(3) / alpha_2 = 1.034

The common ratio is the same for both sectors, confirming the crossed
identification. The excess factor 1.034 is the decoherence correction
(Section 5).

---

## 5. The order parameter and the decoherence tax

The factor |r| connecting bare duty cycles to observed couplings is the
Kuramoto order parameter at M_Z:

    |r| = alpha_s / duty(q_2) = (alpha_s / alpha_2) / (q_3^3 / q_2^3)
        = (alpha_s / alpha_2) x (q_2^3 / q_3^3)
        = 3.488 x (8/27)
        = 3.488 / 3.375
        = 1.0335 ... wait.

More carefully: the crossed dictionary says alpha_s = duty(q_2) x |r|,
so |r| = alpha_s / duty(q_2). But duty(q_2) = 1/8 = 0.125 while
alpha_s = 0.1179, giving |r| = 0.943. This is LESS than 1, as it
should be: the order parameter at finite energy is below the tree
value.

From the ratio perspective:

    |r| = (alpha_s/alpha_2) / (duty(q_2)/duty(q_3))
        = 3.488 / 3.375
        = 1.033

This apparent contradiction resolves as follows. The ratio
alpha_s/alpha_2 = duty(q_2)/duty(q_3) is EXACT in the crossed
dictionary (both couplings carry the same |r| factor, which cancels
in the ratio). The 3.2% residual in the ratio means the bare tree-scale
prediction 27/8 receives a correction from running. The correction IS
the decoherence tax:

    1 - |r| = 1 - 0.968 = 0.032

At M_Z, |r| = 27 / (8 x alpha_s/alpha_2) = 27 / (8 x 3.488) = 0.968.

The 3.2% residual in the coupling ratio is literally 1 - |r|, the
fraction of gate availability consumed by modes that fail to mode-lock
at K < 1. These are the unlocked (irrational winding number) oscillators
in the gaps between Arnold tongues. They occupy specific places on the
Stern-Brocot tree and consume gate time without contributing to
coupling.

---

## 6. The dynamical tongue width correction

The actual circle map theta_{n+1} = theta_n + Omega - (K/2pi) sin(2pi theta_n)
gives tongue widths approximately 1/(pi q^2) rather than 1/q^2. The
factor 1/pi comes from the coupling normalization K/(2pi) in the sine
term.

This factor **cancels in all ratios**:

    duty(q_2) / duty(q_3) = [1/(pi q_2^3)] / [1/(pi q_3^3)]
                           = q_3^3 / q_2^3
                           = 27/8

    sin^2(theta_W) = [1/(pi q_3^3)] / [1/(pi q_2^3) + 1/(pi q_3^3)]
                   = 8/35

All structural predictions — the coupling ratio, the Weinberg angle,
the Higgs mass ratio — are pi-independent. The normalization convention
in the circle map affects the absolute scale of the couplings but not
the relationships between sectors. This is why the dictionary works at
tree scale without specifying the coupling normalization.

---

## 7. The K -> mu mapping (does not close the tree-to-M_Z gap)

**Status: a K* fit to a single observable exists, but a joint K* that
reproduces multiple duty-dictionary identities at M_Z does not.** The
K → μ mapping is therefore NOT the running mechanism that lifts the
K=1 identities of §2, §3, §8, §9 to predictions at the electroweak
scale.

The coupling constant K at energy scale mu is nominally:

    K_eff(mu) = |r|(d(mu))

where d is the Stern-Brocot depth at energy mu. This comes from the
rational field equation (D11) solved at each truncation depth.

From `gate_duty_predictions.py`: fixing K* from the observed
α_s/α_2 at M_Z gives K* ≈ 0.892. Fitting K* to sin²θ_W at M_Z
requires a different value (`sinw_fixed_point.md`: no K* ∈ [0.93,
0.99] reproduces both simultaneously, and the sin²θ_W curve over that
range runs 0.2003–0.2145, never reaching 0.23121). The two
single-observable fits are mutually inconsistent, so the mapping
cannot be simultaneously supplying all M_Z-scale predictions.

`sinW_running_check.py` also shows SM 1-loop running in the opposite
direction from what "tree = Planck" would require for sin²θ_W, ruling
out the alternative that the K → μ mapping is secretly ordinary SM
running under a change of variables.

Consequence: the tree-to-M_Z gaps listed in §2, §3, §8, §9 are
unresolved by the K → μ mapping. Those identities remain bare K=1
reference values in `MANIFEST.yml:bare_k1_identities`, not predictions.

---

## 8. The Higgs mass and quartic (bare K=1 identities)

**Status: bare reference only, not predictions at M_Z.** Same honest-
null treatment as §3: declined in `MANIFEST.yml` and recorded under
`bare_k1_identities.m_H_over_v` and `bare_k1_identities.lambda_higgs`.
See `numerology_inventory.md` §Class 3.

The Higgs field lives in the q = 2 sector. The bare K=1 identities:

    m_H / v = 1 / q_2 = 1/2         (tongue period identity)
    lambda  = 1 / q_2^3 = 1/8       (duty(q_2), self-coupling)

Numerically: m_H = v/2 = 123.1 GeV (observed 125.25 GeV, gap 1.7%);
lambda = 0.125 (observed ~0.129, gap 3.4%).

Interpretation: the Higgs is the lowest excitation of the q = 2 tongue,
with mass set by the tongue's repetition period; the quartic is the
duty cycle of q = 2 for itself. The VEV v = 246.22 GeV is the
framework's single declared dimensionful input (MANIFEST.yml). The
framework does not supply a derivation connecting these K=1 identities
to the observed values at M_Z.

---

## 9. The electromagnetic coupling (bare K=1 identity)

**Status: bare reference only, not a prediction at M_Z.** Same honest-
null treatment as §3: declined in `MANIFEST.yml` and recorded under
`bare_k1_identities.inv_alpha_em_tree`. See `numerology_inventory.md`
§Class 1.

U(1)_em is not a separate mode on the Stern-Brocot tree. It is the
cross-channel mixture of q = 2 and q = 3 via the Weinberg angle:

    alpha_em = alpha_2 × sin^2(theta_W)

At the K = 1 reference:

    1/alpha_0 = q_2^3 + q_3^3 = 8 + 27 = 35

The observed value at M_Z is 1/127.95, roughly a factor 3.7 away.
The K → μ mapping claimed in §7 does not close this gap — see
`sinW_running_check.py` for the explicit demonstration that SM 1-loop
running cannot connect K=1 identities at the Planck scale to the M_Z
observations.

---

## Summary table

Bare K=1 identities only. The "M_Z residual" column records the gap
to observation for reference; it is **not** accounted for by any
derivation in the framework (see `numerology_inventory.md` §Class 1/3).

| Quantity | K=1 bare value | Observed (M_Z) | M_Z gap | Bare source |
|----------|----------------|-----------------|---------|-------------|
| alpha_s / alpha_2 | 27/8 = 3.375 | 3.488 | 3.2% | q_3^3/q_2^3 |
| sin^2(theta_W) | 8/35 = 0.22857 | 0.23121 | 1.1% | q_2^3/(q_2^3+q_3^3) |
| m_H / v | 1/2 | 0.5087 | 1.7% | 1/q_2 |
| lambda (Higgs quartic) | 1/8 = 0.125 | 0.129 | 3.4% | 1/q_2^3 = duty(q_2) |
| 1/alpha_0 (tree EM) | 35 | — | — | q_2^3 + q_3^3 |

Previous fitted corrections (`+ 8/F_10^2`, `+ 1/q_3^2`, `+ 1/228`)
have been removed from this table: they are not derived in the
repository. The K=1 bare values are measure-theoretic consequences
of the duty theorem (`duty_dimension_proof.md`); the gap to M_Z is
unresolved. The previous "decoherence tax" row identifying 1 − |r|
with the residual has been dropped along with its derivation claim
(§7).

---

## Proof dependencies

- **D14** (`three_dimensions.md`): d = 3 from mediant -> SL(2,R) ->
  self-consistent adjacency. The exponent in 1/q^d = 1/q^3 is the
  spatial dimension, not an independent input.

- **D19** (`klein_bottle.md`): The Klein bottle XOR filter selects
  q = 2 and q = 3 as the only surviving sectors. Without D19, we would
  not know WHICH denominators to use.

- **D31** (`speed_of_light.md`): The gate picture. c is the rate at
  which gates propagate; the duty cycle is the fraction of time each
  gate is open. The coupling constant is the gate's availability for
  information transfer.

- **`duty_dimension_proof.md`**: The proof that the duty exponent equals
  dim SL(2,R). The tongue width 1/q^2 comes from Ford circles
  (Gauss-Kuzmin); the period q comes from the orbit definition. Their
  ratio 1/q^3 has exponent 3 = dim SL(2,R) because the duty cycle is
  the full d-dimensional volume element at the cusp.

---

## The dictionary in one sentence

The coupling constant of sector q is the duty cycle of its partner
sector: the fraction of time the partner's gate is open for
information exchange, computed from the Stern-Brocot tree at critical
coupling, with the exponent set by the spatial dimension and the
denominators set by the Klein bottle topology.

---

## Status

The K = 1 identities in this file are exact rational numbers derived
from `duty_dimension_proof.md`. Numerical computations are in:
- `gate_duty_cycle.py` (bare duty cycles, Klein bottle field equation)
- `gate_duty_predictions.py` (single-observable K* fits; does not
  supply joint multi-observable fits)
- `decoherence_correction.py` (crossed dictionary, K = 1 reference)

The M_Z-scale gaps (1-3%) are unresolved in the framework. Previously
this file attributed them to a K → μ running mechanism; that
attribution has been withdrawn (§7). The honest-null resolution is
that these are bare K = 1 identities, moved to
`MANIFEST.yml:bare_k1_identities`, not predictions at the
electroweak scale.
