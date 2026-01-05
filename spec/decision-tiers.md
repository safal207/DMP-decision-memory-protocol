# Decision Tiers & Reversibility (v0.1)

Decision tiers define when a decision requires memory.
DMP exists to preserve decisions that are costly to forget.

## Overview

Not all decisions warrant recording.
Decision tiers distinguish between ordinary choices and decisions with
lasting or irreversible impact.

## Tier Definitions

### Tier 0 — Ordinary (`tier-0`)

Decisions that are:
- easily reversible
- local in impact
- unlikely to cause lasting harm if mistaken

Examples:
- refactoring internal code
- UI copy changes
- temporary experiments

DMP recording: **optional**

---

### Tier 1 — High Impact (`tier-1`)

Decisions that are:
- costly to reverse
- affect multiple systems, teams, or users
- capable of producing long-term consequences

Examples:
- API contract changes
- architectural shifts
- removal of supported functionality

DMP recording: **required**

---

### Tier 2 — Irreversible (`tier-2`)

Decisions that:
- cannot be fully undone
- permanently affect trust, safety, legality, or identity
- create lasting ethical or systemic consequences

Examples:
- data disclosure decisions
- irreversible automation
- decisions affecting human autonomy or rights

DMP recording: **mandatory**

Tier 2 decisions SHOULD be reviewed in relation to SCP constraints.

## Reversibility Semantics

Decision Records MAY include:
- `reversibility`: `reversible | partially-reversible | irreversible`

Reversibility reflects expected recoverability at decision time,
not hindsight evaluation.

## Notes

Decision tiers provide guidance, not enforcement.
Incorrect classification is itself a signal worth remembering.
