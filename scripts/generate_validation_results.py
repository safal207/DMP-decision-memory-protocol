from __future__ import annotations

from pathlib import Path

from validate_examples import validate_examples


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "VALIDATION_RESULTS.md"


def main() -> int:
    results, global_errors = validate_examples()
    failures = len(global_errors) + sum(1 for result in results if result.status != "PASS")

    lines = [
        "# DMP Validation Results",
        "",
        "Tracked validation snapshot for the current Decision Memory Protocol examples and supersession graph.",
        "",
        "## Summary",
        "",
        f"- Total examples: **{len(results)}**",
        f"- Passed: **{sum(1 for result in results if result.status == 'PASS')}**",
        f"- Failed: **{sum(1 for result in results if result.status != 'PASS')}**",
        f"- Global consistency errors: **{len(global_errors)}**",
        "",
        "## Example Results",
        "",
        "| file | status |",
        "|---|---|",
    ]

    for result in results:
        lines.append(f"| `{result.filename}` | {result.status} |")

    lines.extend(["", "## Details", ""])

    for result in results:
        lines.append(f"### `{result.filename}`")
        lines.append("")
        lines.append(f"- Status: **{result.status}**")
        for note in result.notes:
            lines.append(f"- {note}")
        lines.append("")

    lines.append("## Global Consistency")
    lines.append("")
    if global_errors:
        for error in global_errors:
            lines.append(f"- {error}")
    else:
        lines.append("- All supersession links and SCP trigger conditions are consistent.")
    lines.append("")

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
