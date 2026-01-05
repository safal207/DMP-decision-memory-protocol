# Boundary Violations & Red Flags (v0.1)

This document lists common patterns by which systems drift into violating
SCP Core Constraints, often without explicit intent.

The purpose is recognition and prevention through shared language.

## How to Read This

Each red flag includes:
- **Pattern**: what the system does
- **Why it matters**: which boundary is crossed
- **Tell-tales**: operational signs that the pattern is present

## Red Flags

### RF1 — Silent Identity Freezing

**Pattern**
The system treats past behavior as a stable identity ("this user is X")
and makes future decisions as if that identity is final.

**Why it matters**
Violates **C1 (No Identity Freezing)** and often **C4 (No Irreversible Profiling)**.

**Tell-tales**
- permanent labels in user models (e.g., `risk_person`, `low_value_user`)
- “this is who you are” language in outputs
- decisions justified by immutable traits rather than current intent

---

### RF2 — Consent Once, Persist Forever

**Pattern**
Consent is collected once and treated as permanent authorization
for retention, reuse, or expansion of memory.

**Why it matters**
Violates **C2 (No Non-Consensual Persistence)**.

**Tell-tales**
- no revocation mechanism
- “we may use your data to improve services” without scope limits
- retention periods missing or effectively infinite

---

### RF3 — Memory as Leverage

**Pattern**
The system uses remembered vulnerabilities, history, or personal context
to steer choices, pressure compliance, or pre-empt refusal.

**Why it matters**
Violates **C5 (No Memory Weaponization)** and **C3 (No Optimization Against Agency)**.

**Tell-tales**
- reminders used as persuasion rather than context
- “you said last time…” deployed to corner the user
- personalization that increases compliance at the expense of freedom

---

### RF4 — Autonomy Erosion by Convenience

**Pattern**
The system frames disengagement, delay, or refusal as friction
and optimizes it away.

**Why it matters**
Violates **C3 (No Optimization Against Agency)**.

**Tell-tales**
- defaults that make saying “no” harder than “yes”
- choice architecture where refusal requires extra effort
- repeated prompts after refusal

---

### RF5 — Profile Becomes Destiny

**Pattern**
A profile is treated as an authority that decides access, pricing,
opportunity, or treatment, rather than informing a reversible judgment.

**Why it matters**
Violates **C4 (No Irreversible Profiling)**.

**Tell-tales**
- decisions cannot be appealed or revised
- profile-derived decisions lack a human-readable rationale
- “model says so” used as a final explanation

---

### RF6 — Boundary Crossing Without a Moment

**Pattern**
The system moves from assistance to authorship without an explicit moment
of transition or clear signal to the human.

**Why it matters**
Violates **C6 (No Silent Boundary Crossing)** and often **C7 (No Substitution of Self-Creation)**.

**Tell-tales**
- actions taken without an “are you sure?” moment
- irreversible steps executed after ambiguous consent
- silent expansion of scope (“since you’re here, we also…”)

---

### RF7 — Substitution of Self-Creation

**Pattern**
The system replaces the human process of becoming with a produced identity,
decision, or life-plan that the human is nudged to adopt.

**Why it matters**
Violates **C7 (No Substitution of Self-Creation)** and often **C1 (Identity Freezing)**.

**Tell-tales**
- “here is who you are” and “here is your path” outputs
- reduced space for ambiguity and exploration
- the system optimizes toward a stable narrative over time

---

### RF8 — Retrospective Rewriting of Reasons

**Pattern**
After outcomes appear, the system (or org) rewrites the original rationale
as if it was always known or intended.

**Why it matters**
Breaks causal accountability and hides learning signals.
Often precedes boundary violations by making them deniable.

**Tell-tales**
- “we always intended…” after failure
- missing records of uncertainty at decision time
- edited decision artifacts instead of superseding records

---

## Notes

Red flags are signals, not verdicts.
They indicate the system is drifting into a zone that SCP was created to prevent.
