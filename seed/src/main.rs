mod schemas;

use canon_d::Canon;
use ket_cas::{Cid, Store as CasStore};
use ket_dag::{DagNode, NodeKind};
use serde_json::json;
use std::collections::HashMap;
use std::path::PathBuf;

fn ket_home() -> PathBuf {
    std::env::var("KET_HOME")
        .map(PathBuf::from)
        .unwrap_or_else(|_| PathBuf::from(".ket"))
}

/// Create a DAG node and store it in CAS, return the node CID.
fn create_dag_node(
    cas: &CasStore,
    kind: NodeKind,
    output_cid: Cid,
    agent: &str,
    schema_cid: Cid,
    saturation: f32,
    parents: Vec<Cid>,
    meta: Vec<(&str, &str)>,
) -> Cid {
    let mut node = DagNode::new(kind, parents, output_cid, agent)
        .with_schema(schema_cid)
        .with_saturation(saturation);
    for (k, v) in meta {
        node = node.with_meta(k, v);
    }
    let node_bytes = serde_json::to_vec(&node).expect("node serialization failed");
    cas.put(&node_bytes).expect("CAS write failed")
}

struct QuestionEntry {
    source_repo: &'static str,
    section_path: &'static str,
    slug: &'static str,
    text: &'static str,
}

struct ClaimEntry {
    derivation: &'static str,
    slug: &'static str,
    relation: &'static str,
    saturation_delta: f64,
    summary: &'static str,
}

fn main() {
    let home = ket_home();
    let cas_path = home.join("cas");

    // Init or open CAS
    let cas = if cas_path.exists() {
        CasStore::open(cas_path).expect("failed to open CAS")
    } else {
        CasStore::init(&cas_path).expect("failed to init CAS")
    };

    // ── Store schemas ───────────────────────────────────────────────────
    let oq_schema = schemas::open_question_schema();
    let cl_schema = schemas::claim_schema();

    let oq_schema_cid = cas.put(&oq_schema.to_canonical_bytes()).expect("schema write failed");
    let cl_schema_cid = cas.put(&cl_schema.to_canonical_bytes()).expect("schema write failed");

    println!("open_question schema CID: {}", oq_schema_cid.as_str());
    println!("claim schema CID:         {}", cl_schema_cid.as_str());

    let oq_canon = Canon::new(&oq_schema);
    let cl_canon = Canon::new(&cl_schema);

    // ── Open question inventory ─────────────────────────────────────────
    let questions: Vec<QuestionEntry> = vec![
        // ── proslambenomenos ────────────────────────────────────────────
        QuestionEntry {
            source_repo: "proslambenomenos",
            section_path: "kuramoto_einstein_mapping.md§7.1",
            slug: "dynamical-equivalence",
            text: "Show that the Kuramoto evolution equations, with coupling kernel = gravitational Green's function and r ↔ N, reproduce the ADM evolution equations as an identity, not just a structural parallel. Requires fixing the normalization and verifying all numerical prefactors.",
        },
        QuestionEntry {
            source_repo: "proslambenomenos",
            section_path: "kuramoto_einstein_mapping.md§7.2",
            slug: "stribeck-coupling-function",
            text: "Replacing sin(·) with a Stribeck-weighted coupling function and setting δ = 1/2 reproduces the MOND interpolation. Verify within the full dynamical proof.",
        },
        QuestionEntry {
            source_repo: "proslambenomenos",
            section_path: "kuramoto_einstein_mapping.md§7.3",
            slug: "strong-field-regime",
            text: "The mapping works perturbatively (small phase gradients). Near black holes, r → 0, and the perturbative expansion breaks down. The Feigenbaum cascade (period-doubling toward the stuck singularity) should emerge from the Kuramoto dynamics in the r → 0 limit.",
        },
        QuestionEntry {
            source_repo: "proslambenomenos",
            section_path: "kuramoto_einstein_mapping.md§7.4",
            slug: "gravitational-waves-as-sync",
            text: "Linearizing the mapping around flat space should produce wave equations for coherence perturbations that match the linearized Einstein equations. Prediction: gravitational waves are propagating synchronization disturbances in the vacuum.",
        },
        QuestionEntry {
            source_repo: "proslambenomenos",
            section_path: "proslambenomenos.md§7",
            slug: "uniqueness-via-lyapunov",
            text: "The proslambenomenos identification gives a₀ from Λ but does not guarantee that the resulting galactic structure is unique. Requires the Lyapunov dissipation proof.",
        },

        // ── 201 ─────────────────────────────────────────────────────────
        QuestionEntry {
            source_repo: "201",
            section_path: "renzos_rule_derivation.md§1.1",
            slug: "objective-function",
            text: "KKT conditions are consequences of an optimization problem. What is being minimized, subject to what?",
        },
        QuestionEntry {
            source_repo: "201",
            section_path: "renzos_rule_derivation.md§1.2",
            slug: "primal-dual-coupling",
            text: "The coupled fixed-point — where the metric responds to λ and λ responds to the metric — is undemonstrated.",
        },
        QuestionEntry {
            source_repo: "201",
            section_path: "renzos_rule_derivation.md§1.3",
            slug: "renzos-rule-inverse",
            text: "Every rotation curve feature has a baryonic origin requires ruling out phantom structure in λ(r) that has no baryonic counterpart.",
        },
        QuestionEntry {
            source_repo: "201",
            section_path: "renzos_rule_derivation.md§3.2",
            slug: "fixed-point-uniqueness",
            text: "Schauder fixed-point theorem gives existence, not uniqueness. The smooth background level of ρ_dark is not guaranteed uniquely determined by ρ_bary.",
        },
        QuestionEntry {
            source_repo: "201",
            section_path: "renzos_rule_derivation.md§7.1",
            slug: "transition-zone-scatter",
            text: "Prediction: maximum Renzo's Rule scatter at a ~ a₀. Independent of mapping, independent of uniqueness. Testable with SPARC data.",
        },
        QuestionEntry {
            source_repo: "201",
            section_path: "renzos_rule_derivation.md§7.3",
            slug: "dynamical-equivalence",
            text: "The mapping identifies fields and derivatives but does not verify numerical prefactors. Requires matching all prefactors, not just structure.",
        },
        QuestionEntry {
            source_repo: "201",
            section_path: "joven_unifying_framework.md§10.1",
            slug: "cosmological-scales",
            text: "Extend to homogeneous expanding background to reproduce CMB acoustic peaks, baryon acoustic oscillations, and matter power spectrum at sub-percent accuracy.",
        },
        QuestionEntry {
            source_repo: "201",
            section_path: "joven_unifying_framework.md§10.2",
            slug: "bullet-cluster",
            text: "Requires quantitative simulation showing synchronization decoupling from baryonic gas during violent merger while tracking collisionless component.",
        },
        QuestionEntry {
            source_repo: "201",
            section_path: "joven_unifying_framework.md§10.3",
            slug: "mathematical-foundations",
            text: "Category theory (structure of forward map), ergodic theory (synchronization equilibrium conditions), information geometry (measure over paths to synchronization).",
        },
        QuestionEntry {
            source_repo: "201",
            section_path: "joven_unifying_framework.md§10.4",
            slug: "universal-rosin",
            text: "Is the vacuum's Stribeck curve measurable independently of gravitational phenomenology? Candidate: relationship between Λ and a₀.",
        },
        QuestionEntry {
            source_repo: "201",
            section_path: "joven_unifying_framework.md§10.5",
            slug: "decoherence-rates",
            text: "Can the Stribeck-Kuramoto model reproduce measured decoherence timescales for superconducting qubits, photon polarization, trapped ions?",
        },
        QuestionEntry {
            source_repo: "201",
            section_path: "joven_unifying_framework.md§10.6",
            slug: "bell-tsirelson",
            text: "Must reproduce Bell violation at the correct quantitative level (2√2 Tsirelson bound).",
        },

        // ── intersections ───────────────────────────────────────────────
        QuestionEntry {
            source_repo: "intersections",
            section_path: "joven_stick_slip_dark_matter.md§7.1",
            slug: "cosmological-scales",
            text: "The framework has not been applied at cosmological scales. Particle CDM earns its strongest results there — CMB, BAO, matter power spectrum with sub-percent precision.",
        },
        QuestionEntry {
            source_repo: "intersections",
            section_path: "joven_stick_slip_dark_matter.md§7.2",
            slug: "bullet-cluster",
            text: "The Bullet Cluster requires quantitative simulation showing that the constraint's spatial profile evolves independently during violent merger.",
        },
        QuestionEntry {
            source_repo: "intersections",
            section_path: "joven_stick_slip_dark_matter.md§7.3",
            slug: "cluster-convergence",
            text: "Galaxy clusters: MOND underpredicts. Lagrangian relaxation framing predicts multi-constraint optimization is needed. Cluster dark matter requires a multi-constraint formulation.",
        },
        QuestionEntry {
            source_repo: "intersections",
            section_path: "joven_stick_slip_dark_matter.md§7.4",
            slug: "coupled-solution-on-profiles",
            text: "Solve the coupled problem on observed baryonic mass profiles to produce rotation curves without free parameters.",
        },
        QuestionEntry {
            source_repo: "intersections",
            section_path: "joven_stick_slip_dark_matter.md§7.5",
            slug: "square-wave-odd-harmonics",
            text: "If gravitational stick-slip has cascaded through period-doublings toward the square wave limit, the halo's radial profile should contain the odd-harmonic signature.",
        },
        QuestionEntry {
            source_repo: "intersections",
            section_path: "fundamental_forces_planck_scale.md§III.A",
            slug: "qcd-stribeck-gradient",
            text: "Can the QCD beta function be rewritten as the gradient of a Stribeck-type potential: β = -dV/dg?",
        },
        QuestionEntry {
            source_repo: "intersections",
            section_path: "fundamental_forces_planck_scale.md§III.B",
            slug: "qcd-feigenbaum-cascade",
            text: "Prediction: QCD at finite baryon chemical potential shows a Feigenbaum cascade. Testable if the lattice QCD sign problem is resolved.",
        },
        QuestionEntry {
            source_repo: "intersections",
            section_path: "fundamental_forces_planck_scale.md§III.C",
            slug: "yang-mills-confinement",
            text: "The specific constraint whose Lagrange multiplier produces confinement has not been identified. Candidates: norm condition, Pontryagin index, center symmetry.",
        },
        QuestionEntry {
            source_repo: "intersections",
            section_path: "fundamental_forces_planck_scale.md§III.D",
            slug: "superposition-from-noninjectivity",
            text: "Whether the Born rule is the uniform measure over the preimage equivalence class remains to be derived, not assumed.",
        },
        QuestionEntry {
            source_repo: "intersections",
            section_path: "fundamental_forces_planck_scale.md§III.E",
            slug: "information-at-horizon",
            text: "Reframing of the information paradox: no calculation demonstrates that gravitational evolution near a horizon is non-injective.",
        },
        QuestionEntry {
            source_repo: "intersections",
            section_path: "fundamental_forces_planck_scale.md§III.F",
            slug: "electroweak-stribeck",
            text: "Whether the quartic Higgs shape constitutes a 'different Stribeck curve' or a fundamentally different mechanism is unresolved. Universality class mapping to 1D iterated map not constructed.",
        },
    ];

    // ── Seed open questions ─────────────────────────────────────────────
    // slug → list of (source_repo, node_cid) for cross-repo linking
    let mut slug_to_cids: HashMap<String, Vec<(String, Cid)>> = HashMap::new();

    println!("\n── Seeding {} open questions ──", questions.len());

    for q in &questions {
        let value = json!({
            "source_repo": q.source_repo,
            "section_path": q.section_path,
            "question_text": q.text,
            "question_slug": q.slug,
        });

        let canonical = oq_canon.encode(&value).expect("canonical encoding failed");
        let content_cid = cas.put(&canonical).expect("CAS write failed");

        let node_cid = create_dag_node(
            &cas,
            NodeKind::Reasoning,
            content_cid,
            "claude",
            oq_schema_cid.clone(),
            0.0,
            vec![],
            vec![
                ("source_repo", q.source_repo),
                ("section_path", q.section_path),
                ("question_slug", q.slug),
            ],
        );

        slug_to_cids
            .entry(q.slug.to_string())
            .or_default()
            .push((q.source_repo.to_string(), node_cid.clone()));

        println!("  [{}/{}] {} → {}", q.source_repo, q.section_path, q.slug, &node_cid.as_str()[..16]);
    }

    // ── Harmonics claims ────────────────────────────────────────────────
    let claims: Vec<ClaimEntry> = vec![
        ClaimEntry {
            derivation: "sync_cost/FRAMEWORK.md",
            slug: "objective-function",
            relation: "resolves",
            saturation_delta: 0.8,
            summary: "The synchronization cost framework identifies the objective: minimize total synchronization cost (coupling + drift), subject to the Hamiltonian constraint. The KKT conditions of this optimization produce the dark-matter dual variable.",
        },
        ClaimEntry {
            derivation: "sync_cost/derivations/01_born_rule.md",
            slug: "superposition-from-noninjectivity",
            relation: "partially_addresses",
            saturation_delta: 0.5,
            summary: "Derives Born rule from basin-of-attraction measure in the synchronization landscape. Shows probability emerges from the geometry of the cost surface rather than from non-injectivity of the forward map.",
        },
        ClaimEntry {
            derivation: "sync_cost/derivations/03_a0_threshold.md",
            slug: "universal-rosin",
            relation: "partially_addresses",
            saturation_delta: 0.6,
            summary: "Derives a₀ = cH₀/2π from the synchronization cost framework: a₀ is the acceleration at which coupling cost equals drift cost. Establishes the Λ-a₀ relationship as a cost equality rather than coincidence.",
        },
        ClaimEntry {
            derivation: "sync_cost/derivations/03_a0_threshold.md",
            slug: "cosmological-scales",
            relation: "partially_addresses",
            saturation_delta: 0.3,
            summary: "The a₀ threshold derivation connects synchronization cost to cosmological parameters (H₀, Λ) but does not yet reproduce CMB peaks or BAO at sub-percent accuracy.",
        },
        ClaimEntry {
            derivation: "sync_cost/derivations/06_planck_scale.md",
            slug: "qcd-stribeck-gradient",
            relation: "partially_addresses",
            saturation_delta: 0.3,
            summary: "The Planck scale derivation shows N=3 emerges as a threshold from the synchronization cost geometry. Connects to QCD structure but does not directly verify β = -dV/dg.",
        },
        ClaimEntry {
            derivation: "sync_cost/derivations/04_spectral_tilt_reframed.md",
            slug: "cosmological-scales",
            relation: "partially_addresses",
            saturation_delta: 0.2,
            summary: "Derives spectral tilt from mode-locking structure (devil's staircase at 1/φ, self-similar with φ²). Connects to CMB observables via k↔Ω mapping. Partial progress toward cosmological predictions.",
        },
        ClaimEntry {
            derivation: "sync_cost/derivations/05_two_forces.md",
            slug: "cluster-convergence",
            relation: "partially_addresses",
            saturation_delta: 0.2,
            summary: "The two-force (synchronization vs. decoherence) framing may explain why single-constraint relaxation fails at cluster scales — the multi-mode structure requires a different convergence path.",
        },
        ClaimEntry {
            derivation: "sync_cost/FRAMEWORK.md",
            slug: "primal-dual-coupling",
            relation: "partially_addresses",
            saturation_delta: 0.4,
            summary: "The framework establishes the variational structure from which primal-dual coupling follows, but the coupled fixed-point iteration on observed profiles remains undemonstrated.",
        },
        ClaimEntry {
            derivation: "sync_cost/derivations/03_a0_threshold.md",
            slug: "uniqueness-via-lyapunov",
            relation: "partially_addresses",
            saturation_delta: 0.3,
            summary: "The cost equality at a₀ provides a uniqueness argument via convexity of the synchronization cost surface. Complements but does not replace the Lyapunov dissipation proof.",
        },
    ];

    println!("\n── Writing {} harmonics claims ──", claims.len());

    for c in &claims {
        // Collect all question node CIDs this claim addresses (across repos)
        let addresses_cids: Vec<Cid> = slug_to_cids
            .get(c.slug)
            .map(|entries| entries.iter().map(|(_, cid)| cid.clone()).collect())
            .unwrap_or_default();

        let cid_strings: Vec<String> = addresses_cids.iter().map(|c| c.as_str().to_string()).collect();

        let value = json!({
            "derivation_path": c.derivation,
            "addresses_slug": c.slug,
            "relation": c.relation,
            "saturation_delta": c.saturation_delta,
            "summary": c.summary,
            "addresses_cids": cid_strings,
        });

        let canonical = cl_canon.encode(&value).expect("claim encoding failed");
        let content_cid = cas.put(&canonical).expect("CAS write failed");

        let node_cid = create_dag_node(
            &cas,
            NodeKind::Reasoning,
            content_cid,
            "claude",
            cl_schema_cid.clone(),
            c.saturation_delta as f32,
            addresses_cids.clone(),
            vec![
                ("derivation_path", c.derivation),
                ("addresses_slug", c.slug),
                ("relation", c.relation),
            ],
        );

        let repo_count = slug_to_cids
            .get(c.slug)
            .map(|e| e.len())
            .unwrap_or(0);

        println!(
            "  [{}] {} → {} (addresses {} question node{})",
            c.relation,
            c.slug,
            &node_cid.as_str()[..16],
            repo_count,
            if repo_count == 1 { "" } else { "s" },
        );
    }

    // ── Summary ─────────────────────────────────────────────────────────
    let mut cross_repo_slugs: Vec<&String> = slug_to_cids
        .iter()
        .filter(|(_, entries)| entries.len() > 1)
        .map(|(slug, _)| slug)
        .collect();
    cross_repo_slugs.sort();

    println!("\n── Summary ──");
    println!("  Questions seeded:    {}", questions.len());
    println!("  Claims written:      {}", claims.len());
    println!("  Cross-repo slugs:    {} {:?}", cross_repo_slugs.len(), cross_repo_slugs);
    println!("  Schemas stored at:");
    println!("    open_question: {}", oq_schema_cid.as_str());
    println!("    claim:         {}", cl_schema_cid.as_str());
}
