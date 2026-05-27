# DMP Reviewer-Ready Snapshot Notes

Status: reviewer-ready snapshot draft.

This document summarizes the current DMP state for OpenAI, grant, and external reviewers.

## Snapshot summary

DMP is an open-source governance-memory protocol for consequence-bearing decisions whose outcomes may later become irreversible, boundary-relevant, or harder to deny.

Its current reviewer-safe thesis is:

```text
Many systems preserve actions, but lose durable memory of why decisions were made and whether later reality made them irreversible.
```

DMP exists to make consequence-bearing decisions harder to rewrite, forget, or deny after the fact.

## Current reviewer claim

Reviewer-safe claim:

```text
DMP provides a deterministic protocol artifact for preserving decision context, reversibility assumptions, observed outcomes, supersession, and irreversibility signals.
```

Do not overstate this as full AI alignment, certified compliance, production governance certification, legal admissibility, or automatic resolution of irreversible-risk decisions.

## Portfolio role

DMP is the decision-memory and irreversibility-governance layer in the broader trustworthy-agent evidence architecture:

```text
PythiaLabs — pre-execution evidence gates
LTP — path-level trace/replay/admissibility
CML — causal permission and responsibility lineage
DMP — decision memory and irreversibility governance
LRI — living identity and relational invariants
```

DMP preserves durable governance memory around decisions and later consequences. LTP preserves path evidence. CML validates causal permission and responsibility lineage. PythiaLabs gates proposed actions before execution. LRI protects human identity and revisability boundaries.

## Recent reviewer-ready upgrades

### Portfolio relationship

Added and linked:

```text
docs/PORTFOLIO_RELATIONSHIP.md
```

This explains DMP's role relative to PythiaLabs, LTP, CML, and LRI.

### Reviewer path

Added and linked:

```text
docs/REVIEWER_PATH.md
```

This gives a short reading path for OpenAI, grant, and external reviewers.

### Non-claims

Added and linked:

```text
docs/NON_CLAIMS.md
```

This explicitly states that DMP does not claim:

- full AI alignment;
- complete governance automation;
- certified compliance;
- legal admissibility;
- automatic legal, policy, or ethical correctness;
- automatic resolution of irreversible-risk decisions;
- replacement of human/legal/compliance/safety review;
- prediction of all future consequences;
- prevention of all bad decisions;
- universal agent safety.

### README review links

Updated:

```text
README.md
```

README now links directly to:

- reviewer path;
- non-claims;
- portfolio relationship;
- core spec;
- validation snapshot;
- threat model.

## Current evidence anchors

| Evidence | Location |
|---|---|
| Reviewer path | `docs/REVIEWER_PATH.md` |
| Non-claims | `docs/NON_CLAIMS.md` |
| Portfolio relationship | `docs/PORTFOLIO_RELATIONSHIP.md` |
| Grant evidence | `docs/GRANT_EVIDENCE.md` |
| Core decision-record spec | `spec/decision-record.md` |
| Supersession semantics | `spec/supersession.md` |
| Outcome semantics | `spec/outcome.md` |
| JSON Schema | `schemas/decision-record.schema.json` |
| Validation snapshot | `VALIDATION_RESULTS.md` |
| Threat model | `docs/safety/decision_accountability_threat_model.md` |
| Examples | `examples/` |
| Validation script | `scripts/validate_examples.py` |
| Tests | `tests/` |

## Validation command

Recommended reviewer validation:

```bash
python scripts/validate_examples.py
python -m unittest discover -s tests -q
python scripts/generate_validation_results.py
```

Expected current result:

```text
validation passes
tests pass
tracked validation snapshot can be regenerated
```

## Reviewer interpretation

DMP should be evaluated as a focused governance-memory protocol, not as a full governance automation platform.

Correct interpretation:

```text
DMP preserves consequence-bearing decision memory, reversibility assumptions, observed outcomes, supersession, and irreversibility signals.
```

Incorrect interpretation:

```text
DMP automatically decides what is legally, ethically, or strategically correct.
```

## Funding relevance

DMP is strongest as the governance-memory extension after LTP, CML, and PythiaLabs.

Where PythiaLabs asks:

```text
Should this proposed AI-agent action be allowed, blocked, or escalated before execution?
```

Where LTP asks:

```text
Was the execution path grounded, replayable, and admissible?
```

Where CML asks:

```text
Why was this action allowed, and is the causal permission/responsibility chain intact?
```

DMP asks:

```text
What was decided, why, and did later reality make the decision irreversible?
```

Together, they support a staged evidence architecture for trustworthy agentic systems and high-impact governance review.

## Remaining recommended hardening

Before a formal reviewer-ready tag, complete:

- clean-checkout validation;
- confirm validation scripts/tests pass;
- confirm regenerated validation snapshot is unchanged or intentionally updated;
- confirm LICENSE / SECURITY / CONTRIBUTING exist and are linked or explicitly noted;
- update this snapshot with clean-checkout results;
- add a reviewer-ready tag after validation.

## Bottom line

DMP is now substantially clearer for external review:

```text
clear governance-memory framing + reviewer path + non-claims + portfolio relationship + validation path
```

It is ready for the next step: clean-checkout validation and optional reviewer-ready tag.
