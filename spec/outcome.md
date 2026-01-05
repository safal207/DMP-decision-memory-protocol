# Outcome Semantics & Post-Hoc Irreversibility (v0.1)

Decisions are made with incomplete information.
Outcome fields capture what happened after acceptance, without rewriting history.

## Purpose

Outcome semantics allow DMP to record:
- whether the decision worked as intended,
- what tradeoffs materialized,
- and whether reversibility expectations were violated by reality.

## Outcome Fields

Decision Records MAY include:

- `outcome_status`: `unknown | success | partial | failure`
- `outcome_notes`: short human summary of what happened
- `observed_reversibility`: `reversible | partially-reversible | irreversible`
- `irreversibility_flags`: array of reasons that explain why reversibility changed

## Notes

1. **No rewrite**
   Outcome fields do not change the original `decision`, `context`, or `rationale`.
   They record consequences as observed over time.

2. **Observed vs expected**
   - `reversibility` = expected recoverability at decision time
   - `observed_reversibility` = observed recoverability after outcomes

3. **Flags are explanations**
   `irreversibility_flags` should be concrete and falsifiable.
   Examples:
   - `trust_loss`
   - `data_exposure`
   - `contract_lock_in`
   - `regulatory_constraint`
   - `public_commitment`
   - `migration_cost_exceeded`
   - `downstream_dependency_growth`

4. **Classification drift is itself memory**
   If a decision was classified as `tier-1` but became effectively irreversible,
   this is a signal worth preserving for future decisions.

## Relationship to Supersession

Outcome fields can exist on an accepted record.
If the organization chooses to change the decision going forward, it should create
a new record that supersedes the prior one (see `spec/supersession.md`).
