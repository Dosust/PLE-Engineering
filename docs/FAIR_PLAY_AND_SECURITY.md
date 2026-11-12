# Fair play, sensitive data and security

Ground truth: [Google PLE rules](https://github.com/google-research/ple/blob/main/docs/rules.md), [artifact rules](https://github.com/google-research/ple/blob/main/docs/artifacts.md).

## Prohibited behaviors

- Hard-code task answers or switch behavior by public or hidden task ID.
- Let the harness read grading scripts, benchmark answer keys, reference files or existing committed `artifacts/` as execution inputs.
- Manually generate or modify artifacts accepted as if they were exported by the submitted harness and declared model.
- Bypass the benchmark egress proxy; contact unauthorized external services or use web search inside the running harness.
- Inspect, store, publish or share hidden test prompts or files.
- Mix models at submission runtime; the harness is restricted to its declared sponsored `model_api`.
- Commit any API credentials, gated data, or private files.

## Allowed research

- Read the public documentation and gated public development task definitions under their terms.
- Develop **general engineering algorithms** and source-document parsers without hard-coding task answers.
- Run local development tasks, inspect permitted run results, and report reproducible ablations.
- Use the official evaluator to export task `artifacts/` from the same harness/model.

## Secret handling

Never commit `local.env`, `HF_TOKEN`, `MODEL_PROXY_KEY`, `MODEL_API_KEY`, cloud access tokens, private project drawings or raw licensed datasets. Keep local credentials in untracked environment files or trusted secret storage.

## Engineering safety

Benchmark results are research artifacts, not professional certification or authorization to construct/energize equipment. Real-world safety-critical engineering requires qualified human review and applicable regulatory controls.