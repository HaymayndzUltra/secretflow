# scripts directory guide

This directory provides the operational tooling that powers project generation,
quality enforcement, evidence gathering, and deployment automation.  The
scripts span Python CLIs, shell helpers, and a small JavaScript utility.  They
are grouped below by operational priority so that urgent fixes can be
triaged quickly.

## Improvements completed in this review

- Refactored `test_policy_decisions.py` into a robust CLI with deterministic
  fixture discovery, structured output, and optional JSON reports.  It now
  accepts custom roots/router locations instead of relying on hard-coded paths.
- Reworked `rules_audit_quick.py` into a reusable module with parameterised CLI
  flags (`--root`, `--output`, `--min-body-lines`, `--fail-on-issues`) so it can
  be embedded in CI pipelines.
- Added `scripts/itest/run_smoke.py`, a lightweight smoke harness that ensures
  the upgraded CLIs respond to `--help` and gives developers a starting point
  for extending automated coverage.

## Running the smoke checks

```bash
python scripts/itest/run_smoke.py          # run all bundled smoke targets
python scripts/itest/run_smoke.py --help   # CLI usage details
```

Extend `SMOKE_TARGETS` in `scripts/itest/run_smoke.py` when you introduce new
CLI entry points that should have automated coverage.

## Priority catalogue

### High-priority automation

| Script | Purpose | Typical usage | Key dependencies |
| --- | --- | --- | --- |
| `aggregate_coverage.py` | Combine frontend (`coverage/coverage-summary.json`) and backend (`coverage/backend-coverage.xml`) coverage into one JSON summary for gates. | `python scripts/aggregate_coverage.py` | Python stdlib (`json`, `xml.etree`). |
| `collect_coverage.py` | Run pytest with coverage and normalise results into `coverage.xml`; exits cleanly when plugins are missing to keep CI resilient. | `python scripts/collect_coverage.py` | `pytest`, `pytest-cov` when available. |
| `collect_perf.py` | Persist latency metrics in `metrics/perf.json` from environment variables or input files so gating thresholds can assess performance. | `PERF_P95_MS=420 python scripts/collect_perf.py` | Python stdlib; reads env/files. |
| `enforce_gates.py` | Evaluate coverage, dependency, and latency metrics against numeric thresholds to decide gate pass/fail. | `python scripts/enforce_gates.py --metrics-root metrics` | Python stdlib, metrics JSON files. |
| `scan_deps.py` | Aggregate critical/high vulnerability counts from Python (`pip-audit`) and Node (`npm audit`) tooling into `metrics/deps.json`. | `python scripts/scan_deps.py` | `pip-audit`, `npm`. |
| `generate_client_project.py` | Top-level generator CLI that assembles industry/compliance-specific client deliverables. | `python scripts/generate_client_project.py --brief docs/briefs/foo/brief.md` | `project_generator` package, `PyYAML`. |
| `generate_from_brief.py` | Orchestrate frontend/backend project generation from a single brief, wiring in appropriate rule packs. | `python scripts/generate_from_brief.py --brief docs/briefs/foo/brief.md --output-root dist` | `project_generator.core.brief_parser`, subprocess access to generator CLIs. |
| `plan_from_brief.py` | Produce `PLAN.md` and `tasks.json` artifacts from a planning brief without touching source code. | `python scripts/plan_from_brief.py --brief docs/briefs/foo/brief.md` | `project_generator.core.brief_parser`, `scripts.lifecycle_tasks`. |
| `pre_lifecycle_plan.py` | Generate pre-lifecycle roadmaps with dynamic gating before the full automation workflow runs. | `python scripts/pre_lifecycle_plan.py --brief docs/briefs/foo/brief.md` | `project_generator.core.brief_parser`, subprocess helpers, `PyYAML`. |
| `generate_prd_assets.py` | Synthesize PRD and architecture summaries from planning logs for compliance evidence. | `python scripts/generate_prd_assets.py --plan-summary artifacts/plan.md` | Python stdlib, planning artifacts. |
| `sync_from_scaffold.py` | Analyse scaffolded repositories to propose/apply updates to `tasks.json` (additions/completions). | `python scripts/sync_from_scaffold.py --input tasks.json --output tasks.json --apply` | `PyYAML`, filesystem scanning. |
| `update_task_state.py` | Safely mutate a task’s state while recording operator notes, ensuring task boards remain accurate. | `python scripts/update_task_state.py --id FE-01 --state completed` | Python stdlib, JSON tasks file. |
| `validate_compliance_assets.py` | Confirm generated compliance docs align with gate configuration expectations. | `python scripts/validate_compliance_assets.py --config gates_config.yaml` | `PyYAML`, JSON, file IO. |
| `validate_prd_gate.py` | Validate PRD gate evidence before proceeding to later lifecycle stages. | `python scripts/validate_prd_gate.py --evidence-root evidence/` | Python stdlib, planning artifacts. |
| `validate_tasks.py` | Validate DAG integrity and metadata of `tasks.json`, including cycle detection and enum validation. | `python scripts/validate_tasks.py --input tasks.json` | Python stdlib. |
| `write_context_report.py` | Persist the project context report consumed by `.cursor/ai-governor/project.json`. | `python scripts/write_context_report.py --project-name demo --industry healthcare` | `PyYAML` (optional), JSON IO. |
| `rules_audit_quick.py` | Perform heuristic QA checks on `.cursor/rules/project-rules/*.mdc` and emit a Markdown audit report. | `python scripts/rules_audit_quick.py --root .cursor/rules/project-rules --fail-on-issues` | `PyYAML`, Python stdlib. |
| `test_policy_decisions.py` | Execute YAML-driven policy router regression fixtures with optional JSON reporting for CI. | `python scripts/test_policy_decisions.py --cases policy-tests/*.yaml --json-report out.json` | `PyYAML`, dynamic import of `router.py`. |
| `run_workflow.py` | Entry point into the workflow automation engine; loads config and orchestrates gates. | `python scripts/run_workflow.py --config workflow.yaml` | Local `workflow_automation` package, `PyYAML`. |
| `workflow_automation/orchestrator.py` | Core orchestration logic coordinating gate execution and evidence capture. | Imported via `scripts/run_workflow.py` | Python stdlib, package internals. |
| `workflow_automation/gates/base.py` | Base classes and utilities shared by gate implementations. | Imported via workflow automation | Python stdlib. |
| `workflow_automation/gates/implementations.py` | Concrete gate implementations (coverage, linting, deployments) invoked by the orchestrator. | Imported via workflow automation | Python stdlib, optional third-party clients per gate. |
| `workflow_automation/gates/__init__.py` | Convenience exports wiring gate implementations into the orchestrator. | Imported via workflow automation | Python stdlib. |
| `workflow_automation/config.py` | Load and validate workflow configuration files. | Imported via workflow automation | `PyYAML`, Python stdlib. |
| `workflow_automation/context.py` | Shared execution context passed between gates. | Imported via workflow automation | Python stdlib. |
| `workflow_automation/evidence.py` | Utilities for persisting evidence artifacts alongside gate outcomes. | Imported via workflow automation | Python stdlib, filesystem IO. |
| `workflow_automation/exceptions.py` | Canonical exception hierarchy used by the automation runtime. | Imported via workflow automation | Python stdlib. |

### Medium-priority tooling

| Script | Purpose | Typical usage | Key dependencies |
| --- | --- | --- | --- |
| `analyze_project_rules.py` | Parse `.cursor/rules/project-rules` indices to verify categorisation and keyword coverage. | `python scripts/analyze_project_rules.py` | Python stdlib. |
| `audit-versions.mjs` | Ensure template `package.json` files match `expected-versions.json` references. | `node scripts/audit-versions.mjs` | Node.js. |
| `backup_workflows.py` | Back up workflow configuration/evidence for disaster recovery. | `python scripts/backup_workflows.py --dest backups/` | Python stdlib. |
| `benchmark_generation.py` | Benchmark generator throughput (file IO and template rendering). | `python scripts/benchmark_generation.py` | Python stdlib, generator templates. |
| `bootstrap_project.py` | One-command bootstrap that prepares docs and invokes the end-to-end generator. | `python scripts/bootstrap_project.py --brief docs/briefs/foo/brief.md` | `project_generator`, shell utilities. |
| `build_submission_pack.sh` | Assemble `dist/<name>-submission` artifacts (manifest, evidence, checksums). | `bash scripts/build_submission_pack.sh` | `bash`, `jq`, `tar`. |
| `check_compliance_docs.py` | Validate compliance documentation structure and freshness. | `python scripts/check_compliance_docs.py --root compliance/` | `PyYAML`, Python stdlib. |
| `check_hipaa.py` | Run HIPAA-specific compliance checks (session timeout, RBAC modules, audit logs). | `python scripts/check_hipaa.py` | Python stdlib. |
| `doctor.py` | Diagnose local/CI environments (Docker, Node, npm, Python, Go) and print actionable status. | `python scripts/doctor.py` | Python stdlib, subprocess access to toolchains. |
| `doctor-templates.mjs` | Validate generator templates for consistency. | `node scripts/doctor-templates.mjs` | Node.js. |
| `e2e_from_brief.sh` | Shell wrapper to run the full end-to-end generation pipeline from a brief. | `bash scripts/e2e_from_brief.sh path/to/brief.md` | `bash`, generator CLIs. |
| `enrich_tasks.py` | Inject personas and acceptance criteria into `tasks.json` while preserving existing data. | `python scripts/enrich_tasks.py --input tasks.json --output tasks.json` | Python stdlib. |
| `evidence_report.py` | Consolidate workflow evidence into a single report file. | `python scripts/evidence_report.py --input evidence/` | `PyYAML`, Python stdlib. |
| `install_and_test.sh` | Install dependencies and run the project test suite. | `bash scripts/install_and_test.sh` | `bash`, project package managers. |
| `lane_executor.py` | Execute tasks lane-by-lane respecting dependencies and concurrency limits. | `python scripts/lane_executor.py --tasks tasks.json` | Python stdlib, `asyncio`. |
| `lifecycle_tasks.py` | Helper library for lifecycle planning tasks (imported by other scripts). | Imported via other scripts | Python stdlib. |
| `normalize_project_rules.py` | Normalise frontmatter across `.mdc` project rules according to Cursor specs. | `python scripts/normalize_project_rules.py --dry-run` | `PyYAML`, Python stdlib. |
| `optimize_project_rules.py` | Optimise rule metadata/frontmatter for easier consumption. | `python scripts/optimize_project_rules.py` | `PyYAML`, Python stdlib. |
| `restore_workflows.py` | Restore workflow definitions/evidence from backups. | `python scripts/restore_workflows.py --source backups/` | Python stdlib. |
| `router_benchmark.py` | Benchmark router decision latency with and without caching. | `python scripts/router_benchmark.py` | Python stdlib, local router module. |
| `scaffold_briefs.py` | Create stub `docs/briefs/<project>` structures to unblock compliance checks. | `python scripts/scaffold_briefs.py --name demo` | Python stdlib. |
| `scaffold_phase_artifacts.py` | Generate scaffolding for phase deliverables. | `python scripts/scaffold_phase_artifacts.py --output docs/` | Python stdlib. |
| `select_stacks.py` | Recommend stacks based on brief metadata. | `python scripts/select_stacks.py --brief docs/briefs/foo/brief.md` | Python stdlib. |
| `setup_template_tests.sh` | Prepare template integration tests for specified stacks. | `bash scripts/setup_template_tests.sh fastapi` | `bash`, template toolchain. |
| `standardize_frontmatter.py` | Harmonise rule frontmatter with Cursor 2025 specification. | `python scripts/standardize_frontmatter.py --dry-run` | `PyYAML`, Python stdlib. |
| `trigger_plan.py` | Trigger plan regeneration or scheduling via automation hooks. | `python scripts/trigger_plan.py --config workflow.yaml` | Python stdlib. |
| `validate_workflows.py` | Validate workflow configuration files prior to execution. | `python scripts/validate_workflows.py --config workflow.yaml` | `PyYAML`, Python stdlib. |
| `workflow_automation/__init__.py` | Package façade exporting config/orchestrator helpers. | Imported via automation scripts | Python stdlib. |
| `workflow_automation/templates/__init__.py` | Template helper utilities for gate evidence. | Imported via automation scripts | Python stdlib. |

### Lower-priority operational helpers

| Script | Purpose | Typical usage | Key dependencies |
| --- | --- | --- | --- |
| `deploy/package_workflow.py` | Package workflow automation assets for deployment. | `python scripts/deploy/package_workflow.py --output dist/workflow.zip` | Python stdlib, filesystem. |
| `deploy_backend.sh` | Deploy backend services via the configured provider (expects env-specific overrides). | `bash scripts/deploy_backend.sh` | `bash`, provider CLIs (e.g., Vercel, AWS). |
| `rollback_backend.sh` | Roll back backend deployment to a previous revision. | `bash scripts/rollback_backend.sh` | `bash`, provider CLIs. |
| `rollback_frontend.sh` | Roll back frontend deployment with optional environment overrides. | `bash scripts/rollback_frontend.sh` | `bash`, provider CLIs. |
| `setup.sh` | Project bootstrap helper to install dependencies and prepare the workspace. | `bash scripts/setup.sh` | `bash`, package managers. |
| `health/check_deployment.py` | Lightweight deployment health verification helper. | `python scripts/health/check_deployment.py --env staging` | Python stdlib (`urllib`). |
| `itest/run_smoke.py` | Smoke-check key CLIs by executing zero-side-effect commands (`--help`). | `python scripts/itest/run_smoke.py` | Python stdlib, subprocess. |

## Subdirectories at a glance

- `deploy/`: Deployment packaging helpers (see `deploy/package_workflow.py`).
- `health/`: Health probes for deployed services (`health/check_deployment.py`).
- `itest/`: Smoke tests for CLI entry points (`itest/run_smoke.py`).
- `workflow_automation/`: Core workflow automation package consumed by
  `run_workflow.py` and generator tooling.
