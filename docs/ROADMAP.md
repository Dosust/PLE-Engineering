# Execution roadmap and acceptance gates

## Current truth

The public repository starts with **Google's minimal runnable baseline** and new project documentation/tests. There are **no actual benchmark scores or completed task artifacts** as of creation.

## Stage 0: Source and environment setup

- [x] Verify public competition instructions and all 29 task identifiers.
- [x] Include an attributable Apache-2.0 baseline harness.
- [x] Create documentation, analysis script, tests and report template.
- [ ] Obtain gated public Hugging Face data access.
- [ ] Configure local Docker/Harbor, Google-sponsored model gateway and judge.
- [ ] Run `kit check` and archive its actual result.

**Gate:** reproducible baseline starts in the official evaluator.

## Stage 1: Baseline evaluation

- [ ] Run the public dev set (29 tasks) using original starter configuration.
- [ ] Archive `results.json`, `manifest.json`, failures and normalized per-task scores.
- [ ] Record real token, cost, runtime and data-revision provenance.

**Gate:** complete 29-task baseline; no synthetic scores.

## Stage 2: Diagnostics and generic engineering tools

- [ ] Analyze representative tasks: `lv-cable-sizing`, `data-hall-mep-routing`, `foundation-strategy`, `fire-test-validation-memo`.
- [ ] Build task-agnostic MCP discovery and permitted tool interface.
- [ ] Build source/requirements ledger and units/physical-constraint checks.
- [ ] Add document/IFC parsers and generic artifact reopen/validate steps.
- [ ] Add context/checkpoint/recovery controls with tests.

**Gate:** each improvement has unit/integration tests and demonstrated failure-mode reduction.

## Stage 3: A/B and ablation evaluation

- [ ] Run controlled sequential ablations on the same 29 tasks or clearly declare partial runs.
- [ ] Run two different Google-sponsored model families.
- [ ] Compare scores, failure types, cost, tokens and time.
- [ ] Test for regressions and judge variability.

**Gate:** only evidence-backed improvements in final report.

## Stage 4: Reproducibility and release

- [ ] Generate final `artifacts/` via the official runner and the declared model.
- [ ] Pass `uv run python -m kit check`.
- [ ] Pass `uv run python -m kit artifacts`.
- [ ] Record exact Git commit and evaluation task revision.
- [ ] Complete report with real results; follow current official submission directions.

**Gate:** reproducible final commit; no claim of organizer test-set rank without verified external result.