# Unified Workflow CLI Reference

The Unified Workflow CLI (`unified_workflow/cli.py`) provides a single entry point for automation tasks while preserving compatibility with legacy scripts. This document captures command behaviors, flags, telemetry, and extension guidelines introduced during Week 7.

## Installation & Invocation
```bash
python -m unified_workflow.cli --help
# or install the shim for global usage
pipx install .
unified-workflow --help
```

The CLI auto-detects the project root by searching for sibling `scripts/` and `unified-workflow/` directories. Run commands from any subdirectory inside the repository.

## Global Flags
| Flag | Description |
| --- | --- |
| `--legacy` | Force routing through the legacy script even if a unified module is available. Useful during phased rollouts. |
| `--show-telemetry` | Print a formatted report of CLI usage, including unified vs. legacy routing and fallback counts. |
| `--list-deprecation-candidates` | List commands that have not used the legacy path for 14+ days, indicating readiness for deprecation. |
| `--version` | Display the CLI version stamp embedded in the shim (currently `v1.0.0`). |

## Command Catalog
| Command | Description | Unified Module | Legacy Script | Notes |
| --- | --- | --- | --- | --- |
| `generate-project` | Generate a new project from governed templates. | `unified_workflow/automation/project_generator.py` | `scripts/generate_client_project.py` | Unified path preferred; falls back when template metadata mismatches occur. |
| `generate-from-brief` | Produce project assets directly from a planning brief. | `unified_workflow/automation/brief_processor.py` | `scripts/generate_from_brief.py` | Supports identical arguments as the legacy script. |
| `bootstrap` | Scaffold a workspace and run baseline generation. | `unified_workflow/automation/project_generator.py` | `scripts/bootstrap_project.py` | Unified mode injects telemetry for template choices. |
| `plan-from-brief` | Generate PLAN.md and tasks.json artifacts. | `unified_workflow/automation/brief_processor.py` | `scripts/plan_from_brief.py` | Unified implementation shares metadata extraction pipeline. |
| `pre-lifecycle-plan` | Create pre-lifecycle gating plans. | *(pending unified module — use legacy fallback)* | `scripts/pre_lifecycle_plan.py` | Legacy implementation remains the source of truth; telemetry tracks usage to inform prioritization. |
| `run-workflow` | Execute the full automation workflow. | `unified_workflow/automation/ai_orchestrator.py` | `scripts/run_workflow.py` | Unified mode enforces telemetry-backed gate reporting. |
| `validate-compliance` | Validate compliance evidence bundles. | `unified_workflow/automation/compliance_validator.py` | `scripts/validate_compliance_assets.py` | Unified path normalizes evidence schema prior to checks. |
| `validate-prd` | Validate PRD gate evidence. | `unified_workflow/automation/validation_gates.py` | `scripts/validate_prd_gate.py` | Shares gate execution harness with other validation commands. |
| `validate-tasks` | Verify tasks.json structure and metadata. | `unified_workflow/automation/validation_gates.py` | `scripts/validate_tasks.py` | Telemetry captures frequency of manual DAG edits. |
| `doctor` | Run environment diagnostics. | — | `scripts/doctor.py` | Legacy-only command retained for lightweight checks. |
| `analyze-rules` | Audit project rule metadata. | — | `scripts/analyze_project_rules.py` | Legacy-only due to heavy static analysis dependencies. |

> [!TIP]
> Unified modules are executed as Python scripts to preserve environment parity. Future updates may transition to in-process execution; no changes will be required from operators.

## Telemetry & Observability
- **Storage Location:** `~/.unified-workflow/telemetry.json`
- **Captured Fields:** command name, total calls, unified/legacy counts, fallback counts, last exit code, argument pattern summaries, and attempted routing order.
- **Usage:**
  ```bash
  python -m unified_workflow.cli --show-telemetry
  jq '.commands["run-workflow"]' ~/.unified-workflow/telemetry.json
  ```
- **Deprecation Insights:** Combine `--list-deprecation-candidates` with telemetry to prioritize removal of unused legacy paths.

## Extension Guidelines
1. **Add Mapping Entries:** Extend `LegacyCommandRouter.command_map` with `script`, `unified`, and `description` fields.
2. **Provide Unified Modules:** Place implementations in `unified-workflow/automation/` and ensure they expose CLI-compatible interfaces.
3. **Update Tests:** Add new commands to `scripts/itest/run_smoke.py` so the smoke harness exercises the `--help` path.
4. **Document Changes:** Update this reference and the operator quickstart whenever commands are added or arguments change.

## Operational Playbooks
- Follow the [Migration Guide](./migration-guide.md) before enabling unified-only routes in production.
- Use the [Deployment Runbook](./deployment-runbook.md) to validate telemetry during staging and production rollouts.
