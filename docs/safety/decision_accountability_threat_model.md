# Decision Accountability Threat Model

## Purpose

This document explains the safety-relevant failure classes that DMP is intended to make visible.

DMP is not a runtime enforcement system. It is a memory protocol for decisions, consequences, and boundary crossings that organizations would otherwise be tempted to forget, soften, or rewrite.

## Why This Matters

Many serious failures are not caused only by one bad action. They are caused by the inability to reconstruct:

- what was decided
- what was known at the time
- what risks were acknowledged
- whether the decision was expected to be reversible
- whether reality later changed that reversibility
- whether a human or ethical boundary had already been reached

Without that memory, organizations can deny learning signals and repeat the same category errors.

## Failure Classes DMP Helps Address

### 1. Retrospective Rewriting

The rationale for a decision is rewritten after outcomes become visible.

Why it matters:
- uncertainty disappears from history
- accountability is replaced by narrative cleanup
- future teams inherit a false memory of confidence

DMP response:
- immutable accepted records
- supersession instead of silent editing

### 2. Invisible Supersession

Decisions change over time, but the chain of replacement is not explicit.

Why it matters:
- active decisions become ambiguous
- responsibility fragments across versions
- organizations lose a stable sense of what is current versus historical

DMP response:
- explicit supersedes and superseded_by links
- acyclic, single-successor semantics

### 3. Reversibility Illusions

A decision is treated as reversible at decision time, but real-world consequences later make it difficult or impossible to undo.

Why it matters:
- organizations continue to reason as if rollback were cheap
- risk accumulates without updated memory
- irreversible consequences become normalized as expected outcomes

DMP response:
- outcome_status
- observed_reversibility
- irreversibility_flags

### 4. Boundary Crossings Without Explicit Review

A decision reaches autonomy-, identity-, or trust-relevant risk without being marked as requiring SCP awareness.

Why it matters:
- high-severity ethical transitions remain implicit
- systems proceed as if no special responsibility exists
- dangerous thresholds are crossed silently

DMP response:
- scp_review_required
- scp_risk_notes
- trigger semantics through the DMP <-> SCP interface

### 5. Boundary Violations Treated as Non-Memory

A violation or red-flag event is treated as an incident or anecdote, but not recorded as part of durable decision memory.

Why it matters:
- the organization learns socially, not structurally
- denial remains easy
- future decisions lose visibility into prior ethical drift

DMP response:
- boundary violations treated as recordable decision events

## What DMP Does Not Solve

DMP does not by itself solve:

- whether a decision is morally correct in every case
- runtime policy enforcement
- model alignment
- transport or storage security
- semantic truth of every claim in a record

It is a memory and accountability layer, not the entire safety stack.

## Bottom Line

DMP matters when the safety question is:

> Can this organization preserve a durable, non-rewritable memory of what it decided, why it decided it, and when the consequences or boundaries changed?

That is the failure class DMP is built to make visible.
