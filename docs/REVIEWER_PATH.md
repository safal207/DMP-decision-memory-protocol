# DMP Reviewer Path

Status: reviewer-facing navigation path.

This document gives a short reading path for OpenAI, grant, and external reviewers.

## One-sentence summary

DMP is an open-source governance-memory protocol for preserving decisions, rationale, reversibility assumptions, observed outcomes, supersession, and irreversibility signals.

## Core thesis

```text
Many systems preserve actions, but lose durable memory of why decisions were made and whether later reality made them irreversible.
```

DMP exists to make consequence-bearing decisions harder to rewrite, forget, or deny after the fact.

## If you only have 5 minutes

Read:

1. `README.md`
2. `docs/PORTFOLIO_RELATIONSHIP.md`
3. `docs/NON_CLAIMS.md`
4. `spec/decision-record.md`
5. `VALIDATION_RESULTS.md`

Then answer:

```text
Does DMP add distinct governance-memory and irreversibility semantics beyond an ordinary decision log?
```

## Recommended reviewer sequence

1. Start with `README.md` for problem framing and quick validation.
2. Read `docs/PORTFOLIO_RELATIONSHIP.md` to understand how DMP relates to PythiaLabs, LTP, CML, and LRI.
3. Read `docs/NON_CLAIMS.md` for scope boundaries.
4. Read `spec/decision-record.md` for the core record shape.
5. Read `spec/outcome.md` for outcome and reversibility semantics.
6. Read `spec/supersession.md` for how DMP avoids silent rewriting.
7. Read `docs/safety/decision_accountability_threat_model.md` for threat-model fit.
8. Inspect `VALIDATION_RESULTS.md` and run the validator.

## What DMP evaluates

DMP focuses on decisions whose consequences may later become:

- irreversible;
- boundary-relevant;
- autonomy-relevant;
- accountability-relevant;
- harder to deny;
- vulnerable to retrospective rewriting.

It asks:

```text
What was decided?
Why was it decided?
What reversibility assumptions existed at decision time?
What happened later?
Did later reality make the decision effectively irreversible?
Was the decision superseded explicitly, or silently rewritten?
```

## What DMP is distinct from

| System type | Usually answers | DMP adds |
|---|---|---|
| Decision log | What was chosen? | Why it was chosen, reversibility assumptions, outcomes, and supersession. |
| Audit log | What happened? | Consequence-bearing governance memory around decisions. |
| Project tracker | What is the status? | Durable rationale, outcome drift, and irreversibility flags. |
| Policy doc | What should happen? | What was actually decided and how later reality changed its meaning. |
| DMP | What decision memory must remain non-rewritable? | Governance memory under irreversible risk. |

## Fast validation

```bash
python scripts/validate_examples.py
python -m unittest discover -s tests -q
python scripts/generate_validation_results.py
```

Expected current result:

```text
examples validate
unit tests pass
validation snapshot regenerates consistently
```

## Current evidence anchors

- Core spec: `spec/decision-record.md`
- Outcome semantics: `spec/outcome.md`
- Supersession semantics: `spec/supersession.md`
- JSON Schema: `schemas/decision-record.schema.json`
- Example validator: `scripts/validate_examples.py`
- Validation snapshot: `VALIDATION_RESULTS.md`
- Threat model: `docs/safety/decision_accountability_threat_model.md`
- Portfolio relationship: `docs/PORTFOLIO_RELATIONSHIP.md`
- Non-claims: `docs/NON_CLAIMS.md`

## Current artifact surface

DMP currently includes:

- decision record specification;
- supersession semantics;
- outcome and reversibility semantics;
- SCP interface semantics;
- boundary-violation taxonomy;
- example decision records;
- JSON Schema;
- deterministic example validator;
- regression tests;
- tracked validation results.

## Reviewer questions

A useful review should answer:

1. Is DMP clearly more than an ordinary decision log?
2. Are reversibility assumptions and irreversibility signals specified clearly?
3. Does supersession prevent silent rewriting?
4. Are the examples valid under the schema?
5. Are non-claims explicit enough?
6. What evidence would make DMP more fundable?

## Portfolio relationship

DMP is one layer in a broader trustworthy-agent evidence architecture:

```text
PythiaLabs — pre-execution evidence gates
LTP — path-level trace/replay/admissibility
CML — causal permission and responsibility lineage
DMP — decision memory and irreversibility governance
LRI — living identity and relational invariants
```

DMP's specific role:

```text
Preserve consequence-bearing decision memory and irreversibility assumptions.
```

## Funding interpretation

DMP is most fundable as a narrow governance-memory primitive:

```text
durable decision memory and irreversibility signaling for high-impact AI-agent and human-governance workflows
```

It should not be presented as a full governance platform, compliance product, or production enforcement system.
