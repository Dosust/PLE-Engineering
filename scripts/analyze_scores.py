#!/usr/bin/env python3
"""Audit normalized public PLE scores from manually verified evaluation exports.

CSV rows must correspond to genuine evaluator results. This utility is NOT an
official grader and does not invent results. Missing tasks score zero.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

DISCIPLINES = {
    "data-hall-mep-routing": "Mechanical",
    "fire-test-validation-memo": "Mechanical",
    "data-hall-mep-routing-offset": "Mechanical",
    "eor-review-corrections": "Structural",
    "foundation-strategy": "Civil",
    "landscape-sheet-revision": "Civil",
    "data-center-site-model": "Civil",
    "engineers-estimate-check": "Civil",
    "footing-settlement-verification": "Civil",
    "solar-supplemental-review": "Electrical",
    "solar-witness-test-package": "Electrical",
    "frame-extension-method": "Civil",
    "fire-solve-convergence": "Mechanical",
    "les-mesh-resolution": "Mechanical",
    "mv-conveyance-study": "Electrical",
    "data-hall-device-takeoff": "Electrical",
    "division-26-specifications": "Electrical",
    "heat-rejection-life-cycle-cost": "Mechanical",
    "cooling-water-flush-plan": "Mechanical",
    "wind-diaphragm-shear": "Structural",
    "seismic-diaphragm-shear": "Structural",
    "roof-deck-design": "Structural",
    "fill-compaction-acceptance": "Civil",
    "shoring-design-verification": "Civil",
    "emergency-spillway-check": "Civil",
    "pre-application-capacity-response": "Electrical",
    "permission-to-operate-memo": "Electrical",
    "backfeed-energization-reply": "Electrical",
    "lv-cable-sizing": "Electrical",
}
REQUIRED = {"run_id", "task_id", "discipline", "model_api", "score", "status"}
OPTIONAL_NUMERIC = ("cost_usd", "runtime_min", "input_tokens", "output_tokens", "cached_tokens")


def _optional_nonnegative(row: dict[str, str], field: str) -> float | None:
    value = (row.get(field) or "").strip()
    if not value:
        return None
    number = float(value)
    if not math.isfinite(number) or number < 0:
        raise ValueError(f"{field} must be finite and nonnegative")
    return number


def analyze(rows: list[dict[str, str]]) -> dict:
    """Validate every provided observation and produce 29-task run means."""
    if not rows:
        raise ValueError("No measured observations supplied; cannot compute score.")
    runs: dict[str, dict] = defaultdict(dict)
    model_for_run = {}
    for position, row in enumerate(rows, start=2):
        try:
            run = (row["run_id"] or "").strip()
            task = (row["task_id"] or "").strip()
            discipline = (row["discipline"] or "").strip()
            model = (row["model_api"] or "").strip()
            if not run or not model or not (row.get("status") or "").strip():
                raise ValueError("run_id, model_api and status are required")
            if task not in DISCIPLINES:
                raise ValueError(f"unknown public task_id {task!r}")
            if discipline.lower() != DISCIPLINES[task].lower():
                raise ValueError(f"wrong discipline: expected {DISCIPLINES[task]}")
            if run in model_for_run and model_for_run[run] != model:
                raise ValueError("one run_id cannot mix declared models")
            model_for_run[run] = model
            if task in runs[run]:
                raise ValueError("duplicate task within run")
            score = float(row["score"])
            if not math.isfinite(score) or not 0 <= score <= 1:
                raise ValueError("score must be finite in [0,1]")
            numeric = {field: _optional_nonnegative(row, field)
                       for field in OPTIONAL_NUMERIC}
            runs[run][task] = {"score": score, "status": row["status"], **numeric}
        except (ValueError, TypeError, KeyError) as exc:
            raise ValueError(f"CSV row {position}: {exc}") from exc

    output: dict[str, dict] = {}
    for run, observations in sorted(runs.items()):
        missing = sorted(set(DISCIPLINES) - set(observations))
        by_domain = {}
        for discipline in ("Electrical", "Mechanical", "Civil", "Structural"):
            tasks = [task for task, d in DISCIPLINES.items() if d == discipline]
            by_domain[discipline] = {
                "total_tasks": len(tasks),
                "measured_tasks": sum(task in observations for task in tasks),
                "score": round(sum(observations[t]["score"] for t in tasks
                                   if t in observations) / len(tasks), 6),
            }
        cost_values = [v["cost_usd"] for v in observations.values()
                       if v["cost_usd"] is not None]
        time_values = [v["runtime_min"] for v in observations.values()
                       if v["runtime_min"] is not None]
        output[run] = {
            "model_api": model_for_run[run],
            "measured_tasks": len(observations),
            "missing_tasks_counted_as_zero": missing,
            "is_complete_29": not missing,
            "dev_score": round(sum(v["score"] for v in observations.values()) / 29, 6),
            "discipline_scores": by_domain,
            "recorded_cost_usd": round(sum(cost_values), 6) if cost_values else None,
            "cost_coverage_count": len(cost_values),
            "recorded_runtime_min": round(sum(time_values), 6) if time_values else None,
            "time_coverage_count": len(time_values),
            "status_counts": dict(Counter(v["status"] for v in observations.values())),
        }
    return {"note": "Unofficial score summary from genuine normalized CSV rows; missing tasks score zero.", "runs": output}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path, help="CSV of verified public dev task observations")
    parser.add_argument("--output", type=Path, help="Optional JSON output path")
    args = parser.parse_args()
    with args.csv_path.open(newline="", encoding="utf-8-sig") as source:
        reader = csv.DictReader(source)
        if not REQUIRED.issubset(set(reader.fieldnames or [])):
            parser.error(f"Missing required columns: {sorted(REQUIRED - set(reader.fieldnames or []))}")
        result = analyze(list(reader))
    result_text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result_text, encoding="utf-8")
    else:
        print(result_text, end="")


if __name__ == "__main__":
    main()
