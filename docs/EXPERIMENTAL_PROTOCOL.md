# Experimental design and analysis protocol

**Purpose:** measure whether harness improvements increase engineering reliability across Google's 29 public PLE tasks, without confusing anecdotal success, task memorization or judge noise with generalizable engineering competence.

## Primary outcome

Let `s_{r,t} in [0,1]` be normalized score for run `r` on public dev task `t`. Define:

```text
DevScore(r) = (1 / 29) * sum_over_all_29_tasks(s[r,t])
```

Missing/unmeasured public tasks count zero. Keep original task IDs and exact dataset revision. The hidden 56 are not used in local analysis.

## Baseline

Run Google's minimal starter unchanged except for the sample entry name; record all 29 task scores, engineering failures, time and cost. Baseline is **not yet run**.

## Planned ablations

| ID | Harness change | Hypothesis | Isolate variables |
| --- | --- | --- | --- |
| B0 | Upstream minimal baseline | Establish starting performance | Same model and task revision |
| A1 | Requirements/constraints ledger | Fewer missing deliverables | B0 + only A1 |
| A2 | File, CAD/IFC and local MCP tool support | Better task completion on document/geometry projects | A1 + only A2 |
| A3 | Deterministic calculation and unit checking | Fewer math/physics failures | A2 + only A3 |
| A4 | Generic output validation/repair cycle | Better artifact and feasibility compliance | A3 + only A4 |
| A5 | Context management, retries and deadline adaptation | Fewer early stops/context errors | A4 + only A5 |

All rows are **planned**. Do not supply scores until runs are measured.

## Failure taxonomy

- `INPUT`: omitted or misread task/source input.
- `REQ`: requirement or deliverable not identified.
- `GEOMETRY`: invalid IFC/CAD geometry, overlap, collision or topology.
- `UNITS`: dimensions, conversion or power/energy misuse.
- `PHYSICS`: unsupported assumptions or incorrect physical laws.
- `NUMERIC`: non-convergent/inaccurate solver or invalid tolerance.
- `CODE`: engineering code or source clause misapplied.
- `FORMAT`: output file missing, invalid or inconsistent.
- `TOOLS`: unavailable or broken execution/MCP interaction.
- `TIME`: timeout, early stop or failure recovery.
- `EVIDENCE`: unsupported validation or source attribution.
- `OTHER`: documented exceptional error.

Annotate each failure with specific evidence; multiple cause codes may coexist. Do not infer causality from a single score increase.

## Cross-model tests

Compare at least two **sponsored** `google-cloud/<id>` models from different families, holding instructions, task revision, harness code, judge and budgets fixed wherever possible. Record differential effects and model-dependent interaction. Only the declared model may be called by a submitted harness.

## Repeated measurements

Where budget permits, repeat stochastic or AI-rubric tasks to assess sensitivity. Report mean, dispersion, run-to-run differences, and raw scores; do not use significance language unsupported by sample size. Budget and costs are recorded **per task** and using a stated billing estimator, not assumed from token counts without prices.

## Efficiency

Compare score against tokens, runtime and actual estimated billed model cost. Study whether added turns or checks saturate. Include failure cases and explicit 360-minute limit effects.

## Evidence outputs

For every experiment commit:
- baseline/improvement identifier, code commit SHA, declared `model_api`;
- run IDs; per-task scores and errors; input/output/cached tokens;
- cost and runtime with accounting convention; task dataset revision;
- artifact manifest provenance and reproducibility checks.

The `scripts/analyze_scores.py` tool accepts a normalized CSV of verified observations. It is not a benchmark evaluator and does not inspect hidden tasks.