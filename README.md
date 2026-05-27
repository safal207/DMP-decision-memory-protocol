# DMP (Decision Memory Protocol)

DMP (Decision Memory Protocol) is a **governance-memory protocol** for decisions whose consequences may later become **irreversible, boundary-relevant, or harder to deny**.

It preserves not only what was decided, but also the decision context, the original reversibility assumptions, the observed outcomes over time, and whether later reality made the decision materially irreversible.

The core failure DMP addresses is concrete: organizations often preserve actions but lose the durable governance memory of why a decision was made, whether it was believed to be reversible, and whether later outcomes made it effectively irreversible.

When that memory is missing, responsibility becomes deniable, boundary crossings become invisible, and hindsight rewrites the past.

DMP exists to make that harder.

## Review links

- Reviewer path: [docs/REVIEWER_PATH.md](docs/REVIEWER_PATH.md)
- Non-claims: [docs/NON_CLAIMS.md](docs/NON_CLAIMS.md)
- Portfolio relationship: [docs/PORTFOLIO_RELATIONSHIP.md](docs/PORTFOLIO_RELATIONSHIP.md)
- Grant evidence: [docs/GRANT_EVIDENCE.md](docs/GRANT_EVIDENCE.md)
- Core spec: [spec/decision-record.md](spec/decision-record.md)
- Supersession: [spec/supersession.md](spec/supersession.md)
- Outcome semantics: [spec/outcome.md](spec/outcome.md)
- JSON Schema: [schemas/decision-record.schema.json](schemas/decision-record.schema.json)
- Threat model: [docs/safety/decision_accountability_threat_model.md](docs/safety/decision_accountability_threat_model.md)
- Validation snapshot: [VALIDATION_RESULTS.md](VALIDATION_RESULTS.md)

## Problem

Many systems and teams can explain what happened only after the fact. They cannot reliably show:

- what was decided
- why it was decided
- what alternatives were rejected
- whether the decision was expected to be reversible
- whether reality later made it irreversible
- whether the decision crossed a human or ethical boundary

This creates a recurring failure mode:

An organization accumulates actions, policies, and consequences, but not durable, non-rewritable governance memory of responsibility.

## What DMP Does

DMP defines a minimal decision record for preserving consequence-bearing governance memory, including:

- the decision itself
- context and rationale
- expected consequences and outcome status over time
- original reversibility assumptions and observed reversibility
- explicit irreversibility signals (`irreversibility_flags`)
- supersession instead of silent rewriting
- boundary-aware review signals through the DMP <-> SCP interface

In practical terms, DMP is governance-memory infrastructure for irreversible-risk decisions.

## Why DMP Is Not Just a Decision Log

An ordinary decision log may record what was chosen and when.

DMP additionally preserves:

- whether the decision was believed to be reversible at decision time
- whether observed outcomes later contradicted that assumption
- whether boundary-aware SCP review signals were present when autonomy-relevant risk appeared
- whether changes happened through explicit supersession instead of retrospective rewriting

That makes DMP a non-rewritable accountability memory layer, not a generic historical note system.

## DMP vs DRP (Complementary, Not Duplicative)

- **DRP** focuses on structured, machine-checkable decision records, supersession, and conformance.
- **DMP** focuses on durable governance memory of reversibility assumptions, observed outcomes, boundary-relevant review signals, and later irreversibility.

In short:

- **DRP = decision-governance record protocol**
- **DMP = consequence-bearing governance-memory protocol**

DMP complements DRP by preserving consequence memory and accountability lineage when reality changes after the original decision.

## Why This Matters for Safety

Safety failures are often not only runtime failures. They are also failures of consequence memory and governance accountability.

Examples:

- a high-impact decision is made without durable rationale
- a decision is later rewritten instead of superseded
- reversibility is assumed, but observed outcomes become irreversible
- human-autonomy or identity risks emerge without explicit review signals
- boundary violations are noticed only informally and never recorded

DMP makes these transitions visible and durable.

It does not enforce behavior by itself. It ensures that decisions, consequences, reversibility drift, and boundary crossings are not allowed to disappear into narrative revision.

## Current Artifact

This repository already contains a concrete protocol artifact, not just a theme:

- a decision record specification
- supersession semantics
- outcome and reversibility semantics
- SCP interface semantics
- boundary-violation taxonomy
- example decision records
- a project manifest

This repository now also includes:

- a JSON Schema for decision records
- a deterministic example validator
- tracked validation results
- tests for validation behavior

Key files:

- `spec/decision-record.md`
- `spec/supersession.md`
- `spec/outcome.md`
- `spec/dmp-scp-interface.md`
- `spec/scp-core-constraints.md`
- `schemas/decision-record.schema.json`
- `scripts/validate_examples.py`
- `VALIDATION_RESULTS.md`

## Threat Model Fit

DMP is most useful for governance failures under irreversible risk, for example:

- retrospective rewriting of reasons
- missing or inconsistent supersession links
- decisions classified as reversible that later become irreversibly costly
- tier-2 or autonomy-relevant decisions without explicit SCP review signaling
- boundary violations that are observed but not recorded as governance memory

For broader framing, see [docs/safety/decision_accountability_threat_model.md](docs/safety/decision_accountability_threat_model.md).

## Quickstart

Run validation:

```bash
python scripts/validate_examples.py
```

Run tests:

```bash
python -m unittest discover -s tests -q
```

Regenerate the tracked validation snapshot:

```bash
python scripts/generate_validation_results.py
```

## Scope

DMP does not claim to solve all AI safety, governance, legal, or compliance problems.

It contributes one focused primitive:

```text
consequence-bearing decision memory under reversibility and irreversibility risk
```

See [docs/NON_CLAIMS.md](docs/NON_CLAIMS.md) for the full scope boundary.

## Repository Map

- `spec/`: protocol semantics
- `examples/`: canonical decision record examples
- `schemas/`: JSON Schema artifacts
- `scripts/`: validation utilities
- `tests/`: regression coverage
- `docs/`: safety framing and supporting docs

## Research Direction

The strongest research framing for DMP is durable governance memory under irreversible risk.

A useful question is:

> How do we preserve durable, non-rewritable governance memory of decisions whose consequences may later become irreversible, autonomy-relevant, or boundary-crossing?

That makes DMP a strong supporting artifact for safety work concerned with consequence memory, post-hoc accountability, boundary-relevant review, and harder-to-deny decision lineage.
