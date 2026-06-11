# FM beat-frequency / CRT composition correspondence — bounded by Mihailescu

> **Question.** With the substrate convention ω_n = 2π/n on cyclic-mode
> phases, does the dynamical FM-beat identity ω_{ab} = |ω_a − ω_b|
> coincide with the algebraic CRT decomposition Z_{ab} = Z_a × Z_b
> (gcd(a, b) = 1) for the framework's composite substrate modes? If so,
> what bounds the chain of substrate composites where both routes agree?

**Verdict: MODAL ✓ / GENERATIVE ✓** on the structural identity.

The dynamical identity ω_{ab} = |ω_a − ω_b| holds if and only if
|a − b| = 1 (consecutive integers). Among Mihailescu-canonical orders,
the consecutive pairs are exactly **three**: (2, 3), (3, 4), (8, 9).
Mihailescu's theorem terminates the chain at (8, 9). The substrate's
"FM-beat-and-CRT-coextensive" composite-mode space has exactly three
elements: Z_6, Z_12, Z_72.

Class: foundational rigor check / substrate-mode structural correspondence.
Resolution-mode throughout — composes existing canonical claims into a
single structural identity. No substrate primitive added.

---

## 0. Verify-before-assert ground

Re-read this session:

**(G1) Substrate primitives.** (q_2, q_3) = (2, 3); Catalan equation
`q_3² − q_2³ = 1`; Mihailescu's theorem forces (q_2, q_3). Source:
`canonical_glossary.md` Section 5 line 109; `substrate_determinism.md`;
PR #214.

**(G2) Mihailescu's theorem statement.** "8 and 9 are the only
consecutive perfect powers in the positive integers" (Mihăilescu 2002,
*J. Reine Angew. Math.* **572**). Source: `canonical_glossary.md`
line 109 verbatim.

**(G3) CRT factorization of substrate composites.**
- Z_6 = Z_2 × Z_3: `canonical_glossary.md` line 53; `CHAIN_KSTAR.md`
  line 37; `README.md` line 140 and others
- Z_12 = Z_4 × Z_3: `gamma06_cosmological_modular_surface_audit.md`
  line 147 (PR #242); `lambda17_test_gamma06_cosmological_audit.md`
  line 508

**(G4) Cyclic-mode frequency convention.** ω_n := 2π/n on phase
carriers of order n; used in `substrate_mode_evolution.py`
line 30: `OMEGA = {n: 2*math.pi/n for n in PRIMITIVE_MODES}`. This
convention is *natural* but is not derived from substrate primitives
elsewhere in the audit chain. See §6 falsifier F-FM-1.

**(G5) Perfect-prime-power Mihailescu-canonical orders.** Orders of
the form q_2^a · q_3^b with a, b ≥ 0. The "perfect prime powers ≥ 2"
subset is {q_2², q_2³, q_2⁴, ...} ∪ {q_3², q_3³, ...} = {4, 8, 9, 16,
27, 32, 64, 81, 128, 243, 256, 729, ...}.

Session snapshot: CAS 378 (0 corrupt) | drift 0 | substrate clean.

---

## 1. The arithmetic identity

With ω_n = 2π/n on a primitive Z_n mode:

```
ω_a = 2π / a
ω_b = 2π / b
|ω_a − ω_b|  =  2π · |1/a − 1/b|
             =  2π · |b − a| / (ab)
```

The composite mode Z_{ab} (when gcd(a, b) = 1, so Z_{ab} = Z_a × Z_b
by CRT) has natural frequency:

```
ω_{ab}  =  2π / (ab)
```

Setting ω_{ab} = |ω_a − ω_b|:

```
2π / (ab)  =  2π · |b − a| / (ab)
1          =  |b − a|
```

So the **FM-beat identity ω_{ab} = |ω_a − ω_b| holds iff a and b are
consecutive integers**. This is independent of any framework
content — it is pure arithmetic of the ω_n = 2π/n convention.

### 1.1 Counterexamples for non-consecutive pairs

For (a, b) = (3, 5): gcd(3, 5) = 1, so Z_15 = Z_3 × Z_5 by CRT
(algebraically valid). But:

```
|ω_3 − ω_5|  =  2π · |1/3 − 1/5|  =  2π · 2/15  =  4π/15
ω_15         =  2π/15
                                                    
4π/15 ≠ 2π/15
```

Algebraic CRT holds; dynamical beat identity fails. The two routes
disagree when factors are non-consecutive.

For (a, b) = (2, 5): same gcd = 1, but
```
|ω_2 − ω_5|  =  2π · 3/10  =  6π/10
ω_10         =  2π/10  =  π/5
                                                    
6π/10 ≠ 2π/10
```
Same disagreement pattern.

So the coextension of CRT and FM-beating is a **non-trivial joint
constraint**: consecutive integers AND coprime simultaneously.
(Note: consecutive integers are always coprime, since gcd(n, n+1) = 1
trivially. So the joint constraint reduces to "consecutive
integers.")

---

## 2. The Mihailescu-bounded substrate chain

Restricting to Mihailescu-canonical orders {2, 3, 4, 6, 8, 9, 12, 16,
18, 24, 27, 32, 36, ...}, the consecutive pairs (a, a+1) with both
substrate-canonical are:

| Pair (a, a+1) | a | a+1 | Composite Z_{ab} | Substrate role |
|---|---|---|---|---|
| **(2, 3)** | q_2 | q_3 | **Z_6** | substrate primitive pair; cosmological lattice (PR #242) |
| **(3, 4)** | q_3 | q_2² | **Z_12** | cross-scale composite (matter × cosmological; PR #242 Φ_12) |
| **(8, 9)** | q_2³ | q_3² | **Z_72** | Catalan-pair composite (NOT YET FRAMEWORK-ENGAGED) |

After (8, 9), Mihailescu's theorem forbids further consecutive
perfect-power pairs ≥ 2. The next perfect prime powers of Mihailescu
primes are 16 = q_2⁴ (after 9) and 27 = q_3³ (after 16): gaps of 7
and 11. No further consecutive Mihailescu pairs exist where both are
perfect prime powers ≥ 2.

### 2.1 Why no further pairs

Mihailescu's theorem (Mihăilescu 2002): the equation `x^p − y^q = 1`
with x, y, p, q ≥ 2 has the unique solution (x, p, y, q) = (3, 2, 2, 3),
i.e., 3² − 2³ = 9 − 8 = 1. So (8, 9) is the unique consecutive pair
of perfect powers (each exponent ≥ 2) in the positive integers.

The pairs (2, 3) and (3, 4) lie BELOW Mihailescu's domain (one
member is a perfect first power, i.e., a prime). The pair (8, 9) is
EXACTLY at Mihailescu's domain boundary (both perfect powers ≥ 2).

So the three substrate consecutive pairs partition cleanly:
- **(2, 3)**: both primes (perfect first powers)
- **(3, 4)**: one prime, one perfect square
- **(8, 9)**: both perfect powers ≥ 2 (Catalan / Mihailescu's pair)

The chain terminates because there is no fourth substrate-canonical
consecutive pair. Mihailescu bounds it.

### 2.2 The three composite modes

```
(2, 3)  →  Z_6   =  Z_2  × Z_3   =  Z_{q_2}   × Z_{q_3}
(3, 4)  →  Z_12  =  Z_3  × Z_4   =  Z_{q_3}   × Z_{q_2²}
(8, 9)  →  Z_72  =  Z_8  × Z_9   =  Z_{q_2³}  × Z_{q_3²}
```

For each pair, BOTH:
- **Algebraic** route: CRT gives Z_{ab} = Z_a × Z_b (since gcd(a, b) = 1)
- **Dynamical** route: FM beating gives ω_{ab} = |ω_a − ω_b|

The two routes agree exactly. The substrate's composite modes from
consecutive Mihailescu pairs are simultaneously CRT-decomposable and
FM-beat-derivable.

---

## 3. The Catalan composite Z_72 — a candidate not yet engaged

The third consecutive Mihailescu pair (8, 9) produces composite mode
Z_72 = Z_8 × Z_9 = Z_{q_2³} × Z_{q_3²}.

Substrate-survey check (verify-before-assert): grepping the framework
for `Z_72`, `Z₇₂`, `ℤ/72`, or `72 =` in canonical content surfaces
**no instances** of Z_72 as a substrate-mode object. The number 72
appears in arithmetic contexts (`figure_eight.md` continued fractions;
`higgs_from_tongue_boundary.md` coupling ratio 251/72; ratio reductions)
but never as a named substrate cyclic structure.

This is **informative, not a defect**: the substrate carries Z_72 as
a *consequence* of consecutive Mihailescu pairing at the Catalan
locus, but the framework's audit chain has not yet identified what
role Z_72 plays. This audit names Z_72 as a substrate-admitted
candidate; whether it has framework content is a separate question.

### 3.1 What Z_72 could carry

If Z_72 were framework-engaged, candidate roles consistent with its
factorization q_2³ × q_3² = 8 × 9:

- **Mass-hierarchy composite**: `K_quark · K_lepton = q_2³ · q_3² = 72`
  (`numerology_count_phase_a.md` lines 74-75 give K_QUARK = q_2³ = 8,
  K_LEPTON = q_3² = 9). So Z_72 = Z_{K_quark} × Z_{K_lepton}, a
  candidate cross-sector composite.
- **Klein bottle-and-color joint structure**: q_2³ side (Klein
  bottle's signature cubed) × q_3² side (color squared).
- **Cosmological-matter resonance**: q_2³ side = Klein-bottle base
  exponent for octave scale; q_3² side = lepton-sector mode budget.

These are *candidates* the audit surfaces; none are claimed as
verified. The third-twist meta-structure audit's Mode B (Mihailescu-
ratio) instance #15 already references `m_τ/m_e via (q_3³−1)^(d−1/2)`
which uses q_3³ standalone; Z_72 would extend this by joint q_2³ ×
q_3² structure.

### 3.2 Forward audit candidate

A natural follow-up audit: "Z_72 = Z_{K_quark} × Z_{K_lepton} as the
Catalan-pair composite at framework scale" — investigating whether
the cross-sector quark/lepton K product carries Z_72 cyclic content.

---

## 4. AM (K-iteration) — no analogous identity

The simulation also exhibits amplitude modulation through K-iteration
(K relaxing toward K_STAR). Does AM have an analogous identity?

For AM at the substrate level, the "amplitude" is K, evolving via
`dK/dt = (K_STAR − K) / T_relax`. This is exponential relaxation, not
cyclic — there is no AM "beat identity" parallel to FM-beat.

The substrate's K-evolution has no natural cyclic structure, hence no
beat. AM and FM play structurally distinct roles:
- **FM (mode coupling, Kuramoto)**: cyclic-on-cyclic; produces beats
  at difference frequencies
- **AM (K-iteration)**: exponential-on-cyclic; modulates coupling
  strength but doesn't produce beats

So this audit's identity is **FM-specific** — it does not extend to
AM. The framework's K-iteration content remains separately auditable
(per `K_star_iteration.py` and related), unconnected to the FM-beat
correspondence.

---

## 5. Connections to existing audits

| Audit | Connection |
|---|---|
| PR #240 (half-twist meta-structure) | Z_2 = ω_2 generator participates in all three composite pairs; Z_2 is the universal substrate "FM source" |
| PR #241 (PSL(2,ℤ) noncommutative core) | PSL(2,ℤ) = ℤ/q_2 ∗ ℤ/q_3 reflects the same Mihailescu primitives; the Z_6 = Z_2 × Z_3 composite emerges as the *abelianization* of the free product |
| PR #242 (Γ_0(6) cosmological audit) | Z_6 substrate lattice; Φ_12 = Z_4 × Z_3 cross-scale composite — exactly the first two pairs of this audit |
| PR #246 (W_6 Klein-four invariance) | Klein-four W_6 = (Z_2)² acts on Γ_0(6) cusps; not the same as the Z_6 = Z_2 × Z_3 of this audit (cyclic vs Klein four) |
| PR #249 (lepton state group reconciliation) | D_4 envelope contains Z_4; Z_12 = Z_4 × Z_3 connects D_4 to Z_3 cosmological content |
| PR #251 (third-twist meta-structure) | Mode A (cyclic action) includes Z_6 and Z_12 (this audit's first two composites); Mode B (Mihailescu cube) uses q_3³ (one of the Catalan pair factors) |
| `numerology_count_phase_a.md` | K_quark = q_2³ = 8, K_lepton = q_3² = 9; the Catalan pair appears as cross-sector mass-counting |

The audit composes cleanly with the existing chain — it does not
contradict any existing canonical claim.

---

## 6. Falsification anchors

- **F-FM-1** (convention failure): if the substrate's natural mode
  frequency convention is NOT ω_n = 2π/n (e.g., ω_n = π/n, or
  log-period scale, or some Mihailescu-derived value), the FM-beat
  identity may hold under a different consecutive-integer condition,
  or may not hold at all. The convention is natural but not derived
  from substrate primitives elsewhere.

- **F-FM-2** (Z_72 non-canonicity): if Z_72 turns out to lack any
  substrate-canonical content (no framework structure realizes the
  Catalan composite), then the audit's third composite is structurally
  vacuous — the FM-beat / CRT chain effectively terminates at Z_12,
  not Z_72. The audit still holds modally but its substrate-
  generative content reduces from three composites to two.

- **F-FM-3** (Mihailescu's theorem itself): if a fourth consecutive
  pair of perfect powers ≥ 2 were found in the positive integers,
  Mihailescu's theorem would fail. This is impossible per
  Mihăilescu 2002. The audit's "three-composite bound" depends on
  the proven theorem.

- **F-FM-4** (extra Mihailescu-canonical orders): the audit's
  consecutive-pair enumeration assumes Mihailescu-canonical orders =
  {q_2^a · q_3^b : a, b ≥ 0}. If the framework extends to a broader
  prime-power set (e.g., including |F_q| primes 7, 13, 19, 17 etc.),
  more consecutive pairs may surface. The audit currently restricts
  to pure-Mihailescu factorization.

- **F-FM-5** (composite-mode non-coextension): if the framework
  identifies a composite Z_n where CRT and FM-beat give DIFFERENT
  structural content (algebraic = X, dynamical = Y), the
  correspondence breaks. None observed in the surveyed instances; all
  three composites Z_6, Z_12, Z_72 satisfy both routes.

---

## 7. Verdict

**MODAL ✓**: The framework can state the identity (pure arithmetic of
ω_n = 2π/n; consecutive-integer constraint; Mihailescu-canonical
enumeration; all derivable from substrate primitives).

**GENERATIVE ✓**: The substrate forces the three-composite chain
{Z_6, Z_12, Z_72} via the joint constraint (consecutive integers +
Mihailescu-canonical factorization); Mihailescu's theorem bounds the
chain at three elements.

Class: foundational rigor check / FM-beat substrate-mode correspondence.

K-class assessment: **K<1 substrate derivation** (not bare K=1).
The chain depends on Mihailescu's theorem + the cyclic-mode-frequency
convention. Bare K=1 identities like 27/8 use q_3³/q_2³ as values;
this audit uses q_2³ and q_3² as composite-mode orders, structurally
distinct.

---

## 8. What this audit does NOT claim

- **Not a derivation of ω_n = 2π/n**: the convention is natural but
  not derived from substrate primitives. F-FM-1 captures this.
- **Not a claim that Z_72 has framework content**: the third composite
  is substrate-admitted-by-Mihailescu-bound; whether it has framework
  role is a separate question (F-FM-2). The audit surfaces Z_72 as a
  candidate, not as established framework structure.
- **Not an empirical prediction**: the audit does not predict
  observable beats at substrate scale; that would require an empirical
  anchor (Arnold tongue data, modular form eigenvalue spectra, or
  cosmological observables tied to Z_72).
- **Not an AM analog**: AM (K-iteration) has no parallel beat identity
  per §4.
- **Not a substrate primitive addition**: the three composite modes
  are derivable consequences of (q_2, q_3) = (2, 3) + ω_n = 2π/n +
  Mihailescu's theorem.

---

## 9. Forward references

Natural next audits, in order of likely substrate-yield:

1. **Z_72 substrate role audit**: investigate whether Z_72 = Z_{K_quark} ×
   Z_{K_lepton} = Z_{q_2³} × Z_{q_3²} has framework-canonical content,
   given that K_quark = q_2³ = 8 and K_lepton = q_3² = 9 are the
   Catalan pair (PR candidates referenced via
   `numerology_count_phase_a.md`).

2. **ω_n = 2π/n convention derivation**: derive (or reject) the
   convention from substrate primitives. Candidates: Stern-Brocot
   harmonic series, Arnold tongue normalization, modular form natural
   weight scaling.

3. **AM ↔ K-iteration audit**: clarify whether AM (K relaxation) admits
   any substrate-canonical structural identity, parallel to the FM-beat
   correspondence.

4. **Non-Mihailescu prime composites**: extend the consecutive-pair
   analysis to framework-recognized but non-primitive primes (7 = |F_4|;
   13 = |F_6|; 19 = |F_7|). Do consecutive pairs like (6, 7), (7, 8),
   (12, 13), (18, 19) generate substrate-canonical composites under
   broader prime-set?

---

## 10. Cross-references

**Built on:**
- `canonical_glossary.md` Section 5 (Mihailescu's theorem statement)
  and line 53 (Z_6 mode lattice CRT decomposition)
- `CHAIN_KSTAR.md` line 37 (Z_6 = Z_2 × Z_3 Klein parity)
- `gamma06_cosmological_modular_surface_audit.md` lines 145–147
  (cyclotomic Φ_3, Φ_4, Φ_6, Φ_12 polynomial / mode-order table)
- `substrate_determinism.md` and PR #214 (Mihailescu primitives)
- `numerology_count_phase_a.md` lines 74–75 (K_quark = q_2³,
  K_lepton = q_3² — the Catalan pair as cross-sector counts)

**Composes with:**
- PR #241 (PSL(2,ℤ) free product; Z_2 ∗ Z_3 abelianization gives Z_6)
- PR #242 (Γ_0(6) cosmological substrate lattice)
- PR #251 third-twist meta-structure (Mode A and Mode B Z_3 content)

**Simulation reference:**
- `substrate_mode_evolution.py` (repo root, alongside the other
  substrate simulations; ω_n = 2π/n convention used in the multi-mode
  evolution simulation; this audit formalizes the beat-frequency
  observation that simulation surfaces)

**Vocabulary discipline:**
- `vocabulary_is_the_work_pattern.md` — the audit names Z_72 as a
  substrate-admitted candidate without claiming framework content;
  the naming is the work
