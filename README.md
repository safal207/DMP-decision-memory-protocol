# DMP (Decision Memory Protocol)

DMP is a protocol for recording decision memory: context, intent, acknowledged risk, reversibility, supersession, and observed outcomes over time.

The core idea is simple: organizations often remember actions, but fail to preserve the decision context that made those actions possible. When that memory is missing, responsibility becomes deniable, boundary crossings become invisible, and hindsight rewrites the past.

DMP is built to make that harder.

## Problem

Many systems and teams can explain what happened only after the fact. They cannot reliably show:

- what was decided
- why it was decided
- what alternatives were rejected
- whether the decision was expected to be reversible
- whether reality later made it irreversible
- whether the decision crossed a human or ethical boundary

This creates a recurring failure mode:

An organization accumulates actions, policies, and consequences, but not a durable memory of responsibility.

## What DMP Does

DMP defines a minimal decision record for preserving:

- the decision itself
- context and rationale
- expected consequences
- supersession rather than silent editing
- outcome tracking without rewriting history
- boundary-awareness through the DMP <-> SCP interface

In practical terms, DMP is decision-accountability infrastructure.

## Why This Matters for Safety

Safety failures are often not only runtime failures. They are also failures of memory and accountability.

Examples:

- a high-impact decision is made without durable rationale
- a decision is later rewritten instead of superseded
- reversibility is assumed, but observed outcomes become irreversible
- human-autonomy or identity risks emerge without explicit review signals
- boundary violations are noticed only informally and never recorded

DMP makes these transitions visible and durable.

It does not enforce behavior by itself. It ensures that decisions, consequences, and boundary crossings are not allowed to disappear into narrative revision.

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

DMP is most useful for failures of decision accountability, for example:

- retrospective rewriting of reasons
- missing or inconsistent supersession links
- decisions classified as reversible that later become irreversibly costly
- tier-2 or autonomy-relevant decisions without explicit SCP review signaling
- boundary violations that are observed but not recorded as memory

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

## Repository Map

- `spec/`: protocol semantics
- `examples/`: canonical decision record examples
- `schemas/`: JSON Schema artifacts
- `scripts/`: validation utilities
- `tests/`: regression coverage
- `docs/`: safety framing and supporting docs

## Research Direction

The strongest research framing for DMP is decision accountability under irreversible risk.

A useful question is:

> How do we preserve durable, non-rewritable memory of decisions whose consequences may later become irreversible, autonomy-relevant, or boundary-crossing?

That makes DMP a strong supporting artifact for safety work concerned with governance memory, post-hoc accountability, and non-deniable decision lineage.
