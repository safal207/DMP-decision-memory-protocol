# Supersession Semantics (v0.1)

Supersession is the only mechanism by which an accepted Decision Record
may be replaced without rewriting history.

Accepted records are immutable historical artifacts.

## Definitions

- **Active Record**: the most recent accepted record in a supersession chain.
- **Superseded Record**: an accepted record that has been replaced by a newer one.

## Representation

A Decision Record MAY include:
- `supersedes`: ID of the record it replaces.
- `superseded_by`: ID of the record that replaces it.

If record B supersedes record A:
- `B.supersedes = A.id`
- `A.superseded_by = B.id`

## Rules

1. **Immutability**
   - Once a record is `accepted` or `superseded`, it MUST NOT be edited.
   - Superseding a record may require setting its status to `superseded` and adding `superseded_by`. This is a protocol-level transition, not a rewrite of decision content.

2. **Directional Supersession**
   - Supersession flows from newer → older records.

3. **Single Successor (v0.1)**
   - A record MUST NOT be superseded by more than one record.

4. **No Self-Supersession**
   - A record MUST NOT supersede itself.

5. **Acyclic Chains**
   - Supersession chains MUST be acyclic.

6. **Status Transitions**
   - `accepted → superseded` is allowed.
   - `superseded` is terminal.

7. **Rationale Required**
   - A superseding record MUST explain what changed and why.

## Notes

Forked supersession (branching decision histories) is out of scope for v0.1.
