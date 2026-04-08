from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = ROOT / "examples"
SCHEMA_PATH = ROOT / "schemas" / "decision-record.schema.json"

STATUS_VALUES = {"proposed", "accepted", "superseded"}
TIER_VALUES = {"tier-0", "tier-1", "tier-2"}
REVERSIBILITY_VALUES = {"reversible", "partially-reversible", "irreversible"}
OUTCOME_VALUES = {"unknown", "success", "partial", "failure"}
SCP_TRIGGER_FLAGS = {
    "trust_loss",
    "human_autonomy_impact",
    "identity_freeze",
    "non-consensual_persistence",
}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
RED_FLAG_RE = re.compile(r"^RF\d+$")


@dataclass
class ValidationResult:
    filename: str
    status: str
    notes: list[str]


def load_examples() -> list[dict]:
    records = []
    for path in sorted(EXAMPLES_DIR.glob("decision-record-*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        data["_source_file"] = path.name
        records.append(data)
    return records


def _require_string(record: dict, key: str, errors: list[str]) -> None:
    value = record.get(key)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{key} must be a non-empty string")


def _require_string_list(record: dict, key: str, errors: list[str], pattern: re.Pattern[str] | None = None) -> None:
    value = record.get(key)
    if value is None:
        return
    if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() for item in value):
        errors.append(f"{key} must be an array of non-empty strings")
        return
    if pattern is not None and any(pattern.fullmatch(item) is None for item in value):
        errors.append(f"{key} contains values outside the allowed pattern")


def validate_record_shape(record: dict) -> list[str]:
    errors: list[str] = []

    for key in ("id", "title", "decision", "context", "rationale", "consequences"):
        _require_string(record, key, errors)

    date = record.get("date")
    if not isinstance(date, str) or DATE_RE.fullmatch(date) is None:
        errors.append("date must match YYYY-MM-DD")

    status = record.get("status")
    if status not in STATUS_VALUES:
        errors.append("status must be one of proposed|accepted|superseded")

    tier = record.get("tier")
    if tier is not None and tier not in TIER_VALUES:
        errors.append("tier must be one of tier-0|tier-1|tier-2")

    reversibility = record.get("reversibility")
    if reversibility is not None and reversibility not in REVERSIBILITY_VALUES:
        errors.append("reversibility must be one of reversible|partially-reversible|irreversible")

    outcome_status = record.get("outcome_status")
    if outcome_status is not None and outcome_status not in OUTCOME_VALUES:
        errors.append("outcome_status must be one of unknown|success|partial|failure")

    observed_reversibility = record.get("observed_reversibility")
    if observed_reversibility is not None and observed_reversibility not in REVERSIBILITY_VALUES:
        errors.append("observed_reversibility must be one of reversible|partially-reversible|irreversible")

    for key in ("supersedes", "superseded_by", "outcome_notes", "scp_risk_notes"):
        if key in record:
            _require_string(record, key, errors)

    _require_string_list(record, "alternatives", errors)
    _require_string_list(record, "references", errors)
    _require_string_list(record, "irreversibility_flags", errors)
    _require_string_list(record, "related_red_flags", errors, pattern=RED_FLAG_RE)

    if "scp_review_required" in record and not isinstance(record["scp_review_required"], bool):
        errors.append("scp_review_required must be boolean")

    if record.get("status") == "superseded" and "superseded_by" not in record:
        errors.append("superseded records must declare superseded_by")

    if "superseded_by" in record and record.get("status") != "superseded":
        errors.append("superseded_by is only valid when status is superseded")

    scp_triggered = (
        record.get("tier") == "tier-2"
        or record.get("observed_reversibility") == "irreversible"
        or any(flag in SCP_TRIGGER_FLAGS for flag in record.get("irreversibility_flags", []))
    )
    if scp_triggered and record.get("scp_review_required") is not True:
        errors.append("scp_review_required must be true when SCP trigger conditions are present")
    if record.get("scp_review_required") is True and not isinstance(record.get("scp_risk_notes"), str):
        errors.append("scp_risk_notes must be present when scp_review_required is true")

    return errors


def validate_cross_record_consistency(records: list[dict]) -> list[str]:
    errors: list[str] = []
    by_id = {record["id"]: record for record in records if isinstance(record.get("id"), str)}
    successor_count: dict[str, int] = {}

    for record in records:
        record_id = record.get("id")
        supersedes = record.get("supersedes")
        superseded_by = record.get("superseded_by")

        if supersedes == record_id or superseded_by == record_id:
            errors.append(f"{record_id}: self-supersession is not allowed")

        if supersedes is not None:
            if supersedes not in by_id:
                errors.append(f"{record_id}: supersedes references missing record {supersedes}")
            else:
                target = by_id[supersedes]
                if target.get("superseded_by") != record_id:
                    errors.append(f"{record_id}: supersedes link does not match target.superseded_by")
                successor_count[supersedes] = successor_count.get(supersedes, 0) + 1

        if superseded_by is not None:
            if superseded_by not in by_id:
                errors.append(f"{record_id}: superseded_by references missing record {superseded_by}")
            else:
                target = by_id[superseded_by]
                if target.get("supersedes") != record_id:
                    errors.append(f"{record_id}: superseded_by link does not match target.supersedes")

    for target_id, count in successor_count.items():
        if count > 1:
            errors.append(f"{target_id}: multiple successors are not allowed")

    for record in records:
        seen: set[str] = set()
        current = record.get("id")
        while current is not None:
            if current in seen:
                errors.append(f"{record.get('id')}: supersession cycle detected")
                break
            seen.add(current)
            current_record = by_id.get(current)
            if current_record is None:
                break
            current = current_record.get("superseded_by")

    return errors


def validate_examples() -> tuple[list[ValidationResult], list[str]]:
    records = load_examples()
    results: list[ValidationResult] = []
    global_errors: list[str] = []

    for record in records:
        errors = validate_record_shape(record)
        if errors:
            results.append(ValidationResult(record["_source_file"], "FAIL", errors))
        else:
            results.append(ValidationResult(record["_source_file"], "PASS", ["shape valid"]))

    global_errors.extend(validate_cross_record_consistency(records))
    return results, global_errors


def render_text(results: list[ValidationResult], global_errors: list[str]) -> str:
    lines = [
        "DMP example validation",
        f"schema={SCHEMA_PATH.relative_to(ROOT).as_posix()}",
        "",
    ]
    for result in results:
        lines.append(f"- {result.filename}: {result.status}")
        for note in result.notes:
            lines.append(f"  - {note}")
    if global_errors:
        lines.append("")
        lines.append("Global consistency errors:")
        for error in global_errors:
            lines.append(f"- {error}")
    else:
        lines.append("")
        lines.append("All example files and supersession links are valid.")
    return "\n".join(lines)


def main() -> int:
    results, global_errors = validate_examples()
    print(render_text(results, global_errors))
    has_failures = global_errors or any(result.status != "PASS" for result in results)
    return 1 if has_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
