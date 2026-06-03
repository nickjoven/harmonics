# Klein-bottle restructure — price ledger for the apparatus-extension fallback

## Status

**Apparatus-extension verdict: STRUCTURALLY DECLINED BY EMPIRICAL
FALSIFIER.** The Klein-bottle restructure path named in
`axial_trajectory_conservation_audit.md` (adding a second
independent antiperiodic cycle to the substrate to get an
independent R-generator) was held in standby by
`klein_z2_decomposition_falsifier_2.md` as fallback if the
vocabulary-bridge approach fails. This document prices that
fallback and finds the price is not just expensive — it is
**already paid by experiment in the wrong direction**.

Two anticommuting J's on the substrate generate quaternionic ℍ
(by Frobenius's theorem and the closure J_1, J_2, K = J_1 J_2).
`complex_amplitude_uniqueness.md` L200-202 already records that
"a confirmed real-amplitude or quaternionic-amplitude quantum
phenomenon ... would falsify the prediction." Extant precision
tests of quaternionic QM (Adler 1995 framework; Peres 1979
proposal; subsequent atomic experiments) have not found
quaternionic phenomena. The framework's substrate-ℂ prediction
is therefore experimentally corroborated, and any extension
that predicts ℍ instead would invert a confirmed prediction.

This **eliminates** the apparatus-extension fallback from
viability. The vocabulary-bridge path (`Task 110` redirect:
substrate y-parity ↔ particle chirality identification) is
not a fallback choice but the **only available path** for
substrate-chirality work.

Class: foundational rigor check (Class 3, scoping document
for an apparatus-extension path that turns out to be empirically
excluded).

---

## Why 2 antiperiodic cycles closes to ℍ

`complex_amplitude_uniqueness.md` Step 1 (L75-92): each
independent antiperiodic cycle supplies one complex structure
J with J² = −I, and distinct antiperiodic cycles supply
anticommuting J's (Clifford relation for independent reflections).

With two such cycles, the substrate carries J_1, J_2 with:

    J_1² = J_2² = −I,   J_1 J_2 = −J_2 J_1

Define K = J_1 J_2. Then:

    K² = J_1 J_2 J_1 J_2 = J_1 (−J_1 J_2) J_2 = −J_1² J_2² = −(−I)(−I) = −I

K anticommutes with both J_1 and J_2, so {J_1, J_2, K} form
three anticommuting complex structures squaring to −I — the
defining relations of quaternionic ℍ (Frobenius's theorem
normal form).

The doc's L188-192 topology falsifier records exactly this:

> "if it carried a second independent antiperiodic cycle,
> a second anticommuting J would force ℍ. The result is
> contingent on the Klein bottle's exactly-one-antiperiodic-cycle
> topology."

There is no third option. 1 cycle → ℂ; 2 cycles → ℍ; 0 cycles → ℝ.
The structure of normed division algebras (Frobenius's theorem)
admits no intermediate.

---

## Price ledger — what survives ℍ vs what breaks

The framework's QM-reconstruction spine depends on the ℂ-amplitude
structure unevenly. Decomposing by load-bearing dependency:

### Survives ℍ (price = 0)

- **Born rule exponent 2** (`born_rule.md`, `born_rule_parameter_free.md`).
  Derived from saddle-node universality at Arnold tongue boundaries:
  the codimension-1 bifurcation normal form x² + μ = 0 gives
  x = ±√μ, hence Δθ ∝ √ε, hence P ∝ Δθ² = |ψ|². The exponent 2
  is a geometric/topological consequence of saddle-node, independent
  of whether |ψ|² is computed over ℂ or ℍ.

- **Q mod 2 conservation** (`q_mod2_conservation_theorem.md`). The
  Z₂ invariant is structural to the substrate's antipodal cycle,
  not to the algebra type of amplitudes.

- **Klein-bottle mode decomposition** (`klein_bottle.md` L107-152).
  The XOR rule p_x + p_y ≡ 1 (mod 2) is a topological constraint
  on mode pairings; it doesn't depend on ℂ.

- **Sector mode budgets** (`mass_sector_closure.md`). k_lepton = q_3²,
  k_quark = q_2³ come from walker round-trip and integer conservation,
  not amplitude algebra. Mass hierarchy survives.

- **Generation count 3** (= 2² − 1 observable phase states from V_4).
  Topological / counting, not amplitude-algebra-dependent.

- **Gauge sector SU(3) × SU(2) × U(1)** (`gauge_sector_lovelock.md`).
  Built from the center Z₂ × Z₃ = Z_6, rank q_i − 1, Cartan
  classification, and Utiyama's theorem. None of these steps
  require ℂ-amplitudes specifically.

### Breaks under ℍ (price = re-derivation + empirical contradiction)

- **Tsirelson bound 2√2** (`bell_bounds_from_substrate.md` L170-199,
  L436-440). Explicitly a theorem of complex Hilbert space.
  Quaternionic Hilbert space gives a different (higher) Tsirelson-like
  bound — well-studied in the literature (Wootters; Aaronson;
  Pawłowski et al. on superqubit-style bounds). The numerical value
  `2√2` is *specifically* the ℂ-bound, not preserved under ℍ.

- **Pauli algebra σ_x σ_z = −i σ_y** (`bell_bounds_from_substrate.md`
  L396-403). The cyclic anticommutation is SU(2)-on-ℂ² structure;
  under ℍ the natural Hermitian generators are different (Sp(1)
  instead of SU(2) effectively).

- **`E(θ_A, θ_B) = −cos(θ_A − θ_B)` correlation formula**
  (`bell_bounds_from_substrate.md` L8, L37, L434). The cos formula
  rides on Bloch-sphere geometry of ℂ². Under ℍ, the analog is
  defined on a different homogeneous space.

- **CHSH derivation** (`bell_bounds_from_substrate.md` L160-194,
  via E(θ_A, θ_B)). All CHSH-numerics depend on the cos formula.

- **GHZ Mermin 4** (`bell_bounds_from_substrate.md` L438-439, via
  Pauli stabilizer products). Depends on σ_α σ_β = i ε_{αβγ} σ_γ.

- **Bloch sphere as state space** (`born_rule.md` L418-424).
  ℂ²-specific; the ℍ-analog is the quaternionic projective space.

- **ℂ-uniqueness theorem** (`complex_amplitude_uniqueness.md` itself).
  By construction. The theorem's conclusion is inverted: substrate
  predicts ℍ, not ℂ.

- **Renou 2021 corroboration** (`complex_amplitude_uniqueness.md`
  L167-170, "exhibited consequences"). The framework's prediction
  that ℂ (not ℝ) holds, confirmed by Renou's network Bell test,
  is now framed against an ℍ prediction. Renou rules out ℝ-QM,
  not ℝ vs ℍ specifically — but the broader experimental literature
  on quaternionic QM tests (atomic precision; absence of triple
  quaternionic interference) effectively rules out ℍ.

### The empirical floor

`complex_amplitude_uniqueness.md` L200-202 already names this as
a falsifier:

> "A confirmed real-amplitude or quaternionic-amplitude quantum
> phenomenon (contra Renou 2021 for ℝ; contra all extant tests
> for ℍ) would falsify the prediction."

This is symmetric: just as a confirmed ℝ-QM phenomenon would
falsify the framework's ℂ-prediction, a confirmed ℍ-QM phenomenon
would. The historical record is that ℍ-QM has been searched for
(Adler's program; Peres-type precision tests on atomic spectra,
muon anomalous magnetic moments at the time of proposal, etc.)
and not found. The framework's ℂ-prediction is therefore the
empirically-corroborated one; an ℍ-prediction would be the
falsified one.

---

## What the restructure would buy

Against this empirical loss, what would the apparatus-extension
buy?

- **Independent R-generator** that can flip y-parity sectors
  without flipping S. This would let the substrate carry a
  symmetry operation that maps R-even modes to R-odd modes
  without involving complex conjugation.

- **Substrate-level chirality-flipping**, mapping onto particle
  chirality in the standard sense (γ⁵ eigenvalue exchange).

These are gains *in the framework's articulation of chirality*.
They do not produce a derived value (mass, mixing angle,
correlation) that the unextended framework cannot — they
provide a *vocabulary* match between the substrate's R-action
and particle physics' chirality.

A vocabulary match purchased at the cost of empirically
falsified amplitude algebra is not a net gain. The same vocabulary
match might be achievable via the **vocabulary-bridge** route
(`Task 110` redirect): showing that the substrate's already-present
y-parity decomposition (cos vs sin y-modes paired complementarily
with antiperiodic vs periodic x-modes) maps onto particle
chirality through a downstream derivation chain — without
modifying the antiperiodic-cycle count.

---

## Verdict — the fallback is closed

The Klein-bottle restructure path is **structurally declined by
empirical falsifier**. This is not a soft "framework cost too high"
verdict; it is a hard "extension predicts already-falsified
physics" verdict.

Decomposed:

1. **Theoretical price**: re-derivation of Tsirelson 2√2, Pauli
   algebra, Bell correlation formula, CHSH bound, GHZ Mermin bound,
   Bloch sphere structure, and the complex_amplitude_uniqueness
   theorem itself. Born rule, Q mod 2, mode decomposition, gauge
   sector, mass sector survive — these are independent of amplitude
   algebra.

2. **Empirical price**: substrate now predicts ℍ-QM, which extant
   tests have not corroborated and which the framework's own
   falsifier (L200-202) names as a confirming-the-other-direction
   verdict.

The first is recoverable in principle (re-derive on ℍ). The second
is not — the experimental record cannot be re-run with a different
substrate prediction in mind.

The vocabulary-bridge path is therefore not "the preferred path
because the alternative is expensive." It is "the only path
that does not require predicting already-falsified physics."

---

## Implications for the falsifier chain verdict

`klein_z2_decomposition_falsifier_2.md` left two paths open:

- (a) Vocabulary-bridge: show substrate y-parity maps onto
  particle chirality through downstream derivation.
- (b) Apparatus extension (second antiperiodic cycle): held as
  fallback if (a) fails.

This price exercise eliminates (b). If (a) fails, the framework's
position becomes:

> **Substrate-chirality is structurally declined.** The
> framework's R-action exists only as the base half of the single
> (S × R) coupled cycle on the Klein bottle. An independent
> R-generator would require a second antiperiodic cycle, which
> would predict empirically-falsified ℍ-QM. Therefore: the
> framework does not carry independent substrate-level chirality
> as a primitive. Whatever particle-chirality is — γ⁵
> eigenstate, weak-interaction handedness preference — must be
> framework-downstream or framework-empirical, not
> framework-primitive.

This is a clean disposition. The basepoint principle distinguishes
operationally-open (no derivation produced, no obstruction proven)
from structurally-declined (torsorial-decline argument exhibited).
The Klein-bottle restructure has now exhibited its own decline
argument: it would predict already-falsified physics. So
substrate-chirality-as-primitive is structurally declined; what
remains operationally open is the vocabulary-bridge derivation.

---

## Implications for pending tasks

- **Task 105 (horn-branch)**: status unchanged from third-caveat
  test. Apparatus is modally sufficient (populated y-parity
  sectors paired with complementary x-mode types). Horn-branch
  proceeds in y-parity vocabulary; chirality language stays
  imported / downstream.

- **Task 110 (vocabulary-bridge)**: status upgraded from
  "redirected, with apparatus-extension fallback" to **"only
  available path; apparatus-extension closed."** This raises the
  task's importance: it is no longer a choice between two
  routes but the sole route to a substrate-chirality story
  at all.

- **Task 107 (audit)**: original verdict APPARATUS INSUFFICIENT
  refined progressively. Composed verdict for substrate
  chirality:
  - MODAL: y-parity sectors populated ✓
  - GENERATIVE: no independent R-generator, only (S × R) coupled J
  - EXTENSION: structurally declined (would predict falsified ℍ-QM)
  - PATH FORWARD: vocabulary-bridge derivation (Task 110), or
    accept substrate-chirality as a structurally-declined
    primitive with particle-chirality framed downstream.

---

## Caveats — where this verdict could be wrong

1. **The exactly-one J ↔ exactly-one antiperiodic cycle
   correspondence.** `complex_amplitude_uniqueness.md` Step 1 is
   the load-bearing claim. If a J could arise from a substrate
   structure that is *not* an antiperiodic cycle (e.g., from a
   non-trivial cohomology class that doesn't manifest as an
   independent topological loop), the count argument would be
   incomplete. The falsifier doc itself names this as the
   "independent-J count falsifier" (L204-207).

2. **The ℍ-QM empirical exclusion.** This is widely accepted but
   not universally formalized. Adler (1995) catalogs constraints
   from precision atomic physics; later work explored quaternionic
   field theory analogs. If a future experiment found a
   quaternionic-amplitude phenomenon, this verdict inverts and the
   apparatus-extension becomes the empirically-confirming path
   (with the framework's current ℂ-prediction falsified). This
   is a structural risk inherent to the prediction-direction of
   the falsifier, not a flaw in the price exercise.

3. **The Born and mode-decomposition survival claims.** If a
   careful re-derivation under ℍ-Hilbert-space showed that Born
   exponent 2 *changes* (it doesn't, but the assertion has been
   made on saddle-node universality grounds without a full
   ℍ-recomputation), the price ledger's "survives ℍ" column
   shortens. The verdict would still hold (empirical exclusion
   is the binding constraint), but the framework's residual
   derivation work under ℍ would be larger.

---

## One-line summary

The Klein-bottle restructure path — adding a second independent
antiperiodic cycle to give the substrate an independent R-generator
— closes to quaternionic ℍ-amplitudes (Frobenius / Clifford),
which the framework's own falsifier in `complex_amplitude_uniqueness.md`
L200-202 already names as empirically-excluded by extant tests of
quaternionic QM; therefore the apparatus-extension is structurally
declined not by framework cost (which would be recoverable) but by
the harder constraint of predicting already-falsified physics, and
the audit's verdict for substrate-chirality settles to "modally
sufficient, generatively insufficient, extension closed,
vocabulary-bridge is the only available substrate-chirality path"
with the fallback path eliminated rather than held in reserve.

---

## Cross-links

- `klein_z2_decomposition_falsifier_2.md` — third-caveat test
  that named the apparatus-extension fallback held in reserve;
  this doc closes that reserve.
- `klein_z2_decomposition_falsifier.md` — first falsifier;
  identified the independent-S-and-R question.
- `axial_trajectory_conservation_audit.md` — original audit
  with three named extension paths (V_4 promotion, cascade-attached
  Z_2, Klein-bottle restructure). This doc prices the third
  out of the space.
- `complex_amplitude_uniqueness.md` L75-124 — exactly-one-J
  theorem; L200-202 — empirical falsifier for ℂ vs ℝ or ℍ;
  L188-192 — topology falsifier naming "second antiperiodic
  cycle → ℍ".
- `bell_bounds_from_substrate.md` L170-199, L379-440 — the
  ℂ-Hilbert-space machinery whose downstream results would
  break under ℍ.
- `born_rule.md`, `born_rule_parameter_free.md` — saddle-node
  derivation of Born exponent 2; survives ℍ.
- `mass_sector_closure.md` — walker round-trip derivation of
  k_lepton = q_3², k_quark = q_2³; survives ℍ.
- `basepoint_principle.md` — operationally-open vs
  structurally-declined discriminator. This doc upgrades the
  apparatus-extension fallback from operationally-open to
  structurally-declined.
