# Contributing to DMP

Thank you for considering a contribution to DMP.

DMP is an open-source protocol artifact for preserving consequence-bearing decision memory, reversibility assumptions, observed outcomes, supersession, and irreversibility signals.

## Contribution scope

Good contributions include:

- clearer protocol wording;
- improved examples;
- additional validation fixtures;
- schema corrections;
- tests for validation behavior;
- documentation that clarifies scope and non-claims;
- threat-model improvements;
- reviewer-facing reproducibility improvements.

## Keep claims narrow

Do not describe DMP as:

- full AI alignment;
- certified compliance;
- legal admissibility;
- production governance certification;
- automatic legal, ethical, or policy correctness;
- replacement of human/legal/compliance/safety review;
- universal agent safety.

Use the narrower framing:

```text
DMP is an open-source protocol for preserving consequence-bearing decision memory, reversibility assumptions, observed outcomes, supersession, and irreversibility signals.
```

See [`docs/NON_CLAIMS.md`](docs/NON_CLAIMS.md).

## Local validation

Before opening a pull request, run:

```bash
python scripts/validate_examples.py
python -m unittest discover -s tests -q
python scripts/generate_validation_results.py
```

If `VALIDATION_RESULTS.md` changes, explain whether the change is intentional.

## Documentation changes

For documentation-only changes:

- avoid inflated safety, compliance, legal, or production claims;
- preserve the distinction between DMP and ordinary decision logs;
- preserve the distinction between DMP and governance automation;
- link to `docs/NON_CLAIMS.md` when adding reviewer-facing claims.

## Pull request checklist

Before submitting:

- [ ] examples still validate;
- [ ] tests pass;
- [ ] generated validation results are current or intentionally unchanged;
- [ ] new claims are scoped and supported;
- [ ] README/reviewer docs remain clear for external reviewers.

## Code of conduct

Be constructive, specific, and evidence-oriented.

The goal is to make governance-memory artifacts clearer, safer, and easier to review.
