# DMP ↔ SCP Interface (v0.1)

This document defines how Decision Memory Protocol (DMP) interacts
with Self-Creation Protocol (SCP) at points of elevated or irreversible risk.

## Purpose

DMP preserves causal memory of decisions.
SCP defines constraints that protect human agency, presence,
and non-optimization of identity.

This interface allows DMP to signal when SCP constraints must be considered.

## Trigger Conditions

DMP MUST signal SCP-awareness when any of the following are true:

1. `tier = tier-2`
2. `observed_reversibility = irreversible`
3. `irreversibility_flags` contain at least one of:
   - `trust_loss`
   - `human_autonomy_impact`
   - `identity_freeze`
   - `non-consensual_persistence`

## Signal Semantics

Decision Records MAY include:

- `scp_review_required`: `true | false` (default absent)
- `scp_risk_notes`: short human explanation

These fields do not invoke SCP automatically.
They indicate that proceeding without SCP consideration is unsafe.

## Non-Enforcement Principle

DMP does not enforce SCP.
DMP does not block execution.
DMP does not evaluate compliance.

It records that a boundary has been reached.

## Rationale

Systems fail not because constraints were absent,
but because crossings were invisible.

This interface makes boundary crossings explicit and non-deniable.

## Notes

The absence of `scp_review_required` does not imply safety.
Its presence implies heightened responsibility.
