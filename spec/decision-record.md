# Decision Record Specification (v0.1)

A Decision Record captures the minimum memory required to explain a decision and its intent.

## Required Fields
- **id**: Unique identifier (e.g., "decision-record-001").
- **title**: Short, human-readable summary.
- **status**: One of `proposed`, `accepted`, `superseded`.
- **date**: ISO-8601 date (`YYYY-MM-DD`).
- **decision**: The decision as a concise statement.
- **context**: The situation and constraints that led to the decision.
- **rationale**: Why this choice was made.
- **consequences**: Expected impact and tradeoffs.

## Optional Fields
- **alternatives**: Considered options and why they were rejected.
- **supersedes**: ID of the record this one replaces.
- **superseded_by**: ID of the record that replaces this one.
- **references**: Links to supporting material.
- **tier**: `tier-0 | tier-1 | tier-2`
- **reversibility**: `reversible | partially-reversible | irreversible`
- **outcome_status**: `unknown | success | partial | failure`
- **outcome_notes**: Short summary of observed outcome
- **observed_reversibility**: `reversible | partially-reversible | irreversible`
- **irreversibility_flags**: Array of concrete reasons (e.g., `trust_loss`)

## Immutability
Once `status` is `accepted`, the record is immutable. Any change requires a new record that supersedes the prior one.

## Supersession

Decision Records are superseded, not edited.

Supersession rules are defined in `spec/supersession.md`.

## Outcome

Outcome semantics are defined in `spec/outcome.md`.
