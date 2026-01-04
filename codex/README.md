# Decision Memory Protocol (DMP) Codex v0.1

## Purpose
DMP exists to preserve the causal memory of important decisions.
A decision without memory becomes an accident.

## What DMP Is
- A protocol for recording decisions with their intent, context, and consequences.
- A durable memory of why choices were made and what they were expected to change.
- A commitment to accountability over time.

## What DMP Is Not
- Not a task tracker.
- Not an implementation plan.
- Not a storage engine, API, or SDK.

## Core Principles
1. **Causality First**
   - Records capture why the decision happened, not just what happened.
2. **Minimum Sufficient Memory**
   - Only fields required to explain the decision are included.
3. **Immutability by Design**
   - Accepted decision records are not edited.
   - Changes require a new record that links to and supersedes the prior one.
4. **Traceable Impact**
   - Records state intended impact and known tradeoffs.

## Decision Worth Remembering
A decision should be recorded when it is:
- **High impact** (strategy, security, architecture, or cost).
- **Hard to reverse** (long-lived or risky to unwind).
- **Cross-cutting** (affects multiple teams, systems, or stakeholders).

## Non-Editability Principle
A decision record is a historical artifact. It is accepted or superseded, never rewritten.

If a decision changes, create a new record that:
- References the original.
- States the updated decision and rationale.
- Documents what changed and why.
