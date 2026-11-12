# Benchmark, data access and reproducible setup

**Source verification:** Google's official `README.md`, `docs/rules.md`, `docs/models.md`, `eval/README.md`, `eval/dev_set.yaml`, and sample `minimal/`, at upstream commit `8320f0402fdca9f42476607f72bcfd5271cd50c9`.

## Dataset

- Official [public-development dataset](https://huggingface.co/datasets/google/physical-engineerings-last-exam) is gated. Request access with a Hugging Face account and authorize a read token.
- 29 public dev task folders hold engineering prompts, project files, task definitions and graders. The benchmark reports **56 additional hidden test tasks**, whose contents must not be logged or redistributed.
- Official `eval/dev_set.yaml` references Hugging Face repo `google/physical-engineerings-last-exam`, export revision `b3857a3fea39a695e18f845d4a88f29442e96e75` in the inspected upstream commit. Local evaluator downloads the task revision it selects and records it in `results.json`. Never substitute a guessed revision.
- Full task-source and hidden test files have not been downloaded or inspected for this project's initial commit.

## Local environment

Use Google's official [installation](https://github.com/google-research/ple/blob/main/README.md) and [model gateway](https://github.com/google-research/ple/blob/main/docs/models.md) instructions.

Prerequisites: `git`, Python/`uv`, Docker, Harbor 0.20.0 with websockets, gated-dataset authorization and an eligible model proxy. On macOS/Windows the official docs recommend at least six CPUs and 16.25 GB Docker RAM for the full dev set, plus substantial image storage.

```bash
git clone https://github.com/google-research/ple.git
git clone https://github.com/Dossiya-SE/PLE-Engineering.git
cd ple
uv tool install harbor==0.20.0 --with websockets
# Sign in to Hugging Face (interactive) or use HF_TOKEN from an untracked env file.
uv run hf auth login
# Configure MODEL_PROXY_URL and MODEL_PROXY_KEY securely according to Google docs
uv run python -m kit check ../PLE-Engineering
uv run python eval/run.py ../PLE-Engineering --tasks lv-cable-sizing
uv run python eval/run.py ../PLE-Engineering
```

The official Google Cloud local proxy can be backed by your own Vertex AI project and **may incur usage charges**. A separate judge configuration is necessary for rubric/checks-judge tasks. External network access other than the declared model gateway is not allowed inside the harness.

## Why a single general-purpose harness?

A task's score is normalized to [0,1]; the dev score is the arithmetic mean over **29**, including zero for missing tasks. Solving only nine electrical tasks, even perfectly, caps the mean at 9/29 (about 0.3103). Therefore, strive for broad, constraint-compliant behavior, not only domain-specific expertise.

## Grading

- `checks`: machine grading of relevant artifacts.
- `rubric`: rubric assessment by an AI judge.
- `checks-judge`: both.
- Some constraint-and-objective tasks use `s = 0.4p + 0.6 G O'`; any hard constraint failure sets `G=0`. This is not the formula for every task.
- Per-task limit: 360 minutes. Deadline and cancellation must be handled.

## Run provenance record (mandatory for each experiment)

Record all of:
1. Run identifier and UTC timestamp.
2. Harness Git SHA and whether tree is clean.
3. Upstream kit commit and Hugging Face task revision.
4. Exact `model_api`, proxy and judge model identifier, configuration and budget.
5. Task selection, normalized scores and status, plus raw run path.
6. Input, output and cache tokens, runtime and cost calculation method.
7. Failure classification, artifact paths, and which verifier was used.
8. Whether scores are from checks, rubric or mixed judge; report judgment variability where possible.

No metric, ranking or improvement may be reported without traceable run evidence.

## Data policy

Do not commit Hugging Face private tokens, licensed/gated datasets, task inputs, or private drawing files. Do not commit credentials in `artifacts/`. Allowed competition deliverables must be exported only by Google's eval runner, never manually synthesized.