//! Schema definitions for the harmonics knowledge graph.
//!
//! Two schemas:
//! - `open_question`: an unresolved question from one of the source repos
//! - `claim`: a harmonics derivation that addresses an open question

use canon_d::{FieldKind, Schema};

/// Schema for open questions across the project repos.
///
/// Identity: (source_repo, section_path) — "dynamical equivalence" in
/// proslambenomenos §7.1 vs 201 §7 are distinct nodes, but the topology
/// engine clusters them via identity projection on question_slug.
pub fn open_question_schema() -> Schema {
    Schema::new("open_question", 1)
        .identity("source_repo", FieldKind::String)
        .identity("section_path", FieldKind::String)
        .required("question_text", FieldKind::String)
        .required("question_slug", FieldKind::String)
        .optional("depends_on", FieldKind::List(Box::new(FieldKind::Cid)))
        .optional("first_appeared", FieldKind::String)
}

/// Schema for claims that address open questions.
///
/// Identity: (derivation_path, addresses_slug) — one harmonics derivation
/// addressing one question slug is one claim, even if re-seeded.
pub fn claim_schema() -> Schema {
    Schema::new("claim", 1)
        .identity("derivation_path", FieldKind::String)
        .identity("addresses_slug", FieldKind::String)
        .required("relation", FieldKind::String)
        .required("saturation_delta", FieldKind::Float)
        .required("summary", FieldKind::String)
        .optional("addresses_cids", FieldKind::List(Box::new(FieldKind::Cid)))
}
