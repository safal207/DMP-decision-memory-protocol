# Security Policy

## Scope

DMP is currently an open-source protocol artifact for consequence-bearing decision memory, reversibility assumptions, supersession, and irreversibility signals.

This repository is not a production security product, certified compliance system, legal evidence system, or governance automation platform.

## Supported versions

At this stage, security review applies to the current `main` branch and tagged reviewer-ready snapshots.

## Reporting a vulnerability

If you find a security issue, please open a private report through GitHub Security Advisories if available for this repository.

If private advisory reporting is not available, open a minimal public issue that does not include exploit details and state that you have a security concern requiring maintainer follow-up.

Please include:

- affected file or component;
- reproduction steps if safe to share;
- expected behavior;
- actual behavior;
- impact assessment;
- whether the issue affects examples, schemas, tests, or protocol semantics.

## What counts as security-relevant

Security-relevant issues may include:

- validation bypasses;
- schema ambiguity that could hide invalid decision records;
- unsafe examples that overclaim governance or compliance properties;
- documentation that could mislead users into treating DMP as certified legal/compliance/security infrastructure;
- scripts that behave unexpectedly on local files.

## Non-claims

DMP does not claim:

- production security certification;
- certified compliance;
- legal admissibility;
- automatic legal, ethical, or policy correctness;
- replacement of human, legal, compliance, or security review.

See [`docs/NON_CLAIMS.md`](docs/NON_CLAIMS.md) for the full scope boundary.
