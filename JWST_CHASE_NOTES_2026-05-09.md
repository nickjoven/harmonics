# JWST Chase — Recovery Notes — 2026-05-09

Session-snapshot of substantive findings from a long conversation that began
with "evaluate sensational JWST headlines through the harmonics framework"
and turned into an IMF derivation campaign + structural unification. Written
as a recovery artifact after a Remote Control teleport failure made the
branch `claude/review-headline-framework-D8yAg` unrecoverable from this
machine. Action items tracked in a separate GitHub issue.

This is **not a canonical derivation doc**. It's a notes file capturing what
should be promoted to derivation docs once the working environment is stable.

---

## Headline finding — master cascade-lock identity as a family

The framework's K-zoo collapses into a single structural family:

> $K^d = b^{-n}$ with $(d, n, b)$ in framework primitives,
> giving slope $\alpha = -q_2 - n/d$ via the cascade-slope formula.

| Instance         | $(d, n, b)$    | $K$ value          | Slope $\alpha$        | Observable                    | Status              |
|------------------|----------------|--------------------|-----------------------|-------------------------------|---------------------|
| K=1 boundary     | $(-, 0, -)$    | 1.000              | $-q_2 = -2$           | Press-Schechter halo MF       | exact               |
| $K^*$ matter eq. | $(14, 3, 2)$   | $0.86196052$       | $-31/14 \approx -2.214$ | matter-sector running       | exact (CHAIN_KSTAR) |
| $K_\text{IMF}$ (bowed) | $(3, 1, 2)$ | $2^{-1/3} = 0.794$ | $-7/3 \approx -2.333$ | Salpeter IMF                  | 0.33σ vs obs        |
| $K_\text{clarinet}$ | $(2, 1, 3)$ | $3^{-1/2} = 0.577$ | $-5/2 = -2.500$       | predicted, no obs match yet   | open prediction     |
| $K \approx 0.892$ | $(6, 1, 2)?$  | $2^{-1/6} = 0.891?$| $-13/6 \approx -2.167$| subhalo MF ($-1.9$ to $-2.0$)?| suggestive (0.18%)  |

Three instances satisfy the identity exactly. A fourth (the `0.892` in
`beta_from_tongues.md` / `quantum_gravity_interpolation.md`) is suggestive;
needs verification it's exactly $2^{-1/6}$.

---

## Phase II — Salpeter slope derivation (Class 2 candidate)

Master identity at $(d, n, b) = (q_3, 1, q_2)$ gives:

```
K_IMF^q_3 = q_2^(-1)  →  K_IMF = 2^(-1/3)
α = -q_2 - 1/q_3 = -|F_4|/q_3 = -7/3
```

Salpeter: $-2.35 \pm 0.05$ → 0.33σ residual.

**Mechanism:**
- Klein-orbit count at depth $\le q_3 = 3$ on the Stern-Brocot tree: 3 orbits
  (2 pair-orbits ${0/1, 1/1}$ + ${1/3, 2/3}$, plus 1 fixed point ${1/2}$).
- **Lemma needed**: cascade depth = Klein-orbit count. Stribeck N=3 critical
  chain length is the empirical anchor. Lemma is structurally parallel to the
  Klein-signature-from-Farey-index argument in `step3_step5_klein_proof.py`
  but needs its own writeup.
- $n_\text{Klein} = 1$: a path visiting each Klein-orbit once and returning
  contributes one flip per pair-orbit (boundary pair and fixed point
  contribute zero); the genuine depth-$q_3$ pair-orbit is unique → $n=1$.

Cross-check: same combinatorics applied to the lepton sector (Farey index 4,
double-traverse, 3 pair-orbits) gives $K^{*14} = q_2^{-q_3}$ exactly,
matching CHAIN_KSTAR.md.

---

## Phase II.C — van der Pol clarinet-lattice numerics

Session-only computation; **not yet a script in the repo**. Drives a chain of
van der Pol oscillators (odd-symmetric nonlinearity, parallel to the
clarinet's half-wave-antisym reed) with measurement at chain end.

| Drive ratio   | Critical chain length    | Predicted by master identity              |
|---------------|--------------------------|-------------------------------------------|
| 2:1 (octave)  | $N = 3 = q_3$            | bowed cascade ($q_2$-base, depth $q_3$)   |
| 3:1 (twelfth) | $N = 2 = q_2$            | clarinet cascade ($q_3$-base, depth $q_2$)|

The 3:1 cascade locks at $N=2$ with 83% power at $\omega_0$, 13% at drive
frequency. This validates the master identity on **independent dynamics**
(van der Pol, not the existing Stribeck-friction model).

Belongs in: `clarinet_lattice.py` parallel to existing `stribeck_lattice.py`,
plus a section in `RESULTS.md`.

---

## Mass-function family across cascade depths

Universal slope formula $\alpha = -q_2 - n/d$ (with $n = 1$ except at the
matter-equilibrium instance) gives a one-parameter prediction:

| Scale              | Cascade depth        | Predicted $\alpha$| Observed                  |
|--------------------|----------------------|-------------------|---------------------------|
| Cosmological halos | K=1 (no cascade)     | $-2.000$          | $-2.0$ (Press-Schechter) ✓|
| Galactic subhalos  | $|Z_6| = 6$ (?)      | $-13/6 \approx -2.167$| $-1.9$ to $-2.0$ (close, ~5% high) |
| Stellar IMF        | $q_3 = 3$ (bowed)    | $-7/3 \approx -2.333$ | $-2.35 \pm 0.05$ ✓ Salpeter |
| $q_3$-cascade      | $q_2 = 2$            | $-5/2 = -2.500$   | no clean observational match yet |

Reframes "spread of mass-function slopes from $-1.9$ to $-2.5$" as one
structural prediction evaluated at different framework depths.

---

## Instrument-family taxonomy

Framework's K=1/K<1 split + sym/antisym sectors map onto reed-acoustic
instrument families:

| Sector                   | Instrument | $K$ value          | Predicts                  |
|--------------------------|------------|--------------------|---------------------------|
| K=1 (gravity, full sync) | string     | 1                  | Press-Schechter $\alpha = -2$ |
| Near-K=1 (inflation)     | flute      | $\approx 0.976$    | $n_s = 0.965$ via $K = 2^{n_s-1}$ |
| K<1 $q_2$-cascade (baryon) | bowed    | $0.794$            | Salpeter $\alpha = -7/3$  |
| K<1 $q_3$-cascade        | clarinet   | $0.577$            | predicted $\alpha = -5/2$ |
| (counterfactual) torus   | saxophone  | —                  | reveals Klein necessity   |

**Reasoning chain**:
- Clarinet overblows at the 12th (factor 3 = $q_3$); saxophone at the octave
  (factor 2 = $q_2$). The two natural reed-cascade bases match the
  framework's two primes exactly.
- Klein-bottle commitment ↔ fermion spin-structure commitment: torus admits
  only bosons; Klein admits the antiperiodic 4π-period spinor structure.
  This is why the framework has a non-trivial matter sector at all.

---

## Speculative threads (sketched, not derivation-grade)

### Cone-twist conifold substrate
Geometric morph: substrate as Z_2-twisted bicone (two cones joined apex-to-apex
with a half-twist seam). Reframes K=1/K<1 discontinuity as a **coupling seam**
rather than a hard wall. Dark sector becomes seam-localized.

Cosmological precedents in the literature: Penrose CCC (twin-aeon),
Klebanov-Strassler conifolds (string-theory throat modes), Steinhardt-Turok
ekpyrotic, cosmic strings (conical deficit), Hartle-Hawking conical caps,
Veneziano bicone bouncing cosmologies. None combines all three of bicone +
Z_2 twist + parity-flipped exchange — that combination would be the
framework's geometric realization.

Empirical hooks: cosmic axis-of-evil alignment, dark-matter spatial structure
deviating from pure-NFW, baryon asymmetry from seam pair production.

### Soliton sector via sine-Gordon on Klein bottle
Kuramoto-Hamiltonian density $\frac{m}{2}(\partial_t\theta)^2 -
\frac{K_\text{eff}}{2}(\partial_x\theta)^2 + \mu\cos\theta$ gives sine-Gordon
directly:

```
∂_t² θ - c² ∂_x² θ + ω_0² sin(θ) = 0
```

Kink solutions $\theta(x,t) = 4\arctan[\exp(\gamma(x-vt)/\ell)]$ with
$M_k = 8\sqrt{m\mu}/\omega_0$. On Klein bottle, $b$-loop traversal converts
kink → antikink, so topological charge is **Z_2-graded** not Z-graded.

**Computational corollary**: parametrized soliton scattering with optional
$b$-loop traversal gives a single-primitive computational basis (NAND-like
universality). The substrate is a programmable medium.

Empirical candidates (all sketched, none derived):
- Neutrino oscillation periods as kink-antikink loop conversion
- Baryon asymmetry $\eta_B$ as initial-imbalance mod-2 residue
- Born rule operationalized as soliton-pointer scattering cross-section
- Black-hole mass spectrum quantized by tongue-width × seam-monodromy

---

## What was withdrawn during the chase

- **Phase I** ($M_P/m_p = (q_3/q_2) \cdot 13^{17}$ at 0.28%): numerology.
  Exponent 17 has no structural derivation; $m_p$ isn't a substrate quantity
  in the framework (it's ~95% QCD binding, downstream of $\Lambda_\text{QCD}$
  which itself isn't framework-derived). Pigeonhole search-space rate matches
  the hit rate. **Phase I is upstream-blocked** until a hadronic-sector
  closure exists.

- **Phase IV depth-running form** ($d_\text{grav}(z) = q_3 H(z)/H_0$):
  mechanism fails. Cloud free-fall time $\tau_\text{ff} \propto
  1/\sqrt{G\rho_\text{cloud}}$ decouples from cosmic Hubble time once you're
  inside an overdense cloud, so "more strata visited per Hubble time at
  high z" doesn't hold. The functional form $\alpha(z) = -q_2 - H_0/[q_3 H(z)]$
  survives **if** instead $n_\text{Klein}(z) = H_0/H(z)$ runs (candidate α),
  but that's conjectural.

- **Antisym Farey count = $\Omega_{DM}$ count** (E1): 9 ≠ 5. Clarinet
  symmetry actually lives on the $Z_6$ algebra layer (where 5+1 emerges),
  not the Klein-Farey rationals layer (where 9+10 emerges). The identity
  $\langle q\rangle_\text{antisym}(F_7) = q_2 + q_3 = 5$ holds exactly but
  is an identity, not a derivation of $\Omega_{DM}$.

- **Antisym cascade slope** (E2): $-5/2$ doesn't match observed dark-sector
  mass-function slopes. Clarinet sector contributes **dispersion** (Chabrier
  $\sigma_\text{dex}$), not a fragmentation cascade.

---

## What remains genuinely open

| Gate                                                        | Status                                  |
|-------------------------------------------------------------|-----------------------------------------|
| Phase II Step 2 lemma (orbit count = cascade depth)         | informal; needs writeup                 |
| Pigeonhole audit on master identity family                  | not yet run                             |
| Verify $K \approx 0.892$ is exactly $2^{-1/6}$              | needs recompute in beta_from_tongues    |
| K(t) running for $\alpha(z)$ JWST observable                | blocked at N9 (existing framework null) |
| Hadronic mass closure ($m_p$, $\Lambda_\text{QCD}$)         | blocked, possible master-identity route |
| Cone-twist substrate formal construction                    | sketched only                           |
| Soliton sector formal derivation                            | sketched only                           |
| Subhalo MF reconciliation ($-13/6$ vs $-1.9$ to $-2.0$)     | open                                    |
| Drift on 8 tracked CAS files                                | unenumerable without Dolt               |

---

## What's actually verified

Exact algebraic identities:
- $K^{*14} = q_2^{-q_3} = 1/8$ (CHAIN_KSTAR.md, existing canon)
- $K_\text{IMF}^{q_3} = q_2^{-1}$, hence $K_\text{IMF} = 2^{-1/3}$
- $K_\text{clarinet}^{q_2} = q_3^{-1}$, hence $K_\text{clarinet} = 3^{-1/2}$
- $\alpha = -q_2 - n/d$ slope formula across all cascade-locked instances
- $\langle q\rangle_\text{antisym}(F_7) = q_2 + q_3 = 5$
- Slope gap $\alpha_\text{clarinet} - \alpha_\text{bowed} = -1/(q_2 q_3) = -1/|Z_6|$

Numerical match (single experiment):
- van der Pol 3:1 cascade locks at $N = q_2 = 2$
- van der Pol 2:1 cascade locks at $N = q_3 = 3$ (matches Stribeck RESULTS.md)

Observational residuals:
- Salpeter $\alpha = -7/3$: 0.33σ
- Press-Schechter $\alpha = -2$: exact (within obs precision)
- Chabrier center $M_*/M_\odot = 13/56 = 0.232$: 5% off observed 0.22
  — but inherits Phase I numerology gate
- Chabrier width $\sigma_\text{dex} = 0.585$: 2.6% off observed 0.57

---

*End of recovery notes. See associated GitHub issue for action items.*
