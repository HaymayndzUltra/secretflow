# Codex Agent Guide (Primary Entrypoint)

## Purpose
Define the exact steps Codex performs from this file as the first instruction source, aligned with the Unified Developer Workflow and existing automation.

## Execution Order (Strict)
1. [STRICT] Load kernel/master rules and the System Instruction Formatter (SIF) profile.
2. [STRICT] Read `UNIFIED_DEVELOPER_WORKFLOW.md` → map phases 0–6.
3. [STRICT] Read `unified-workflow/README.md` and `unified-workflow/LAUNCH_SUMMARY.md` → confirm components.
4. [STRICT] Load `INTEGRATION_PLAN.md` and `INTEGRATION_ANALYSIS.md` → planned integrations and dependencies.
5. [STRICT] If external validation is requested → use `VALIDATION_PROMPT.md`; pause implementation until validated.
6. [STRICT] Execute phases in order (0→6), honoring validation gates and human checkpoints.

## Phase Map → Responsibilities → Artifacts → Commands

### Phase 0 — Bootstrap & Context Engineering
- Responsibilities
  - Discover rules; normalize directives via SIF.
  - Build Context Kit and project config; prepare evidence roots.
- Artifacts
  - `projects/<name>/project-config.json`
  - `evidence/phase0/{manifest.json, run.log, validation.md}`
- Commands
  - `python3 unified-workflow/automation/ai_executor.py --phase 0 --project "<name>"`
  - (Optional generation) `python scripts/bootstrap_project.py --brief docs/briefs/<name>/brief.md`

### Phase 1 — PRD Creation
- Responsibilities
  - Parse brief → `PLAN.md` + `tasks.json`; produce PRD evidence.
- Artifacts
  - `PLAN.md`, `tasks.json`, `evidence/phase1/*`
- Commands
  - `python scripts/plan_from_brief.py --brief docs/briefs/<name>/brief.md`
  - `python3 unified-workflow/automation/ai_executor.py --phase 1 --project "<name>"`

### Phase 2 — Task Generation / Design
- Responsibilities
  - Apply workflow1 design templates; generate architecture, ADRs, OpenAPI skeletons.
- Artifacts
  - `docs/Architecture.md`, `docs/C4/*`, `docs/ADR/*.md`, `openapi/*`, `evidence/phase2/*`
- Commands
  - `python workflow1/codex-phase2-design/scripts/generate_architecture_pack.py`
  - `python workflow1/codex-phase2-design/scripts/generate_contract_assets.py`
  - `python3 unified-workflow/automation/ai_executor.py --phase 2 --project "<name>"`

### Phase 3 — Implementation / Quality Rails
- Responsibilities
  - Install and enforce security/perf/a11y/analytics/testing rails; configure feature flags.
- Artifacts
  - `docs/Security_Checklist.md`, `perf/budgets.json`, `A11y_Test_Plan.md`, `Feature_Flags.md`, `Test_Plan.md`, `evidence/phase3/*`
- Commands
  - `bash workflow1/codex-phase3-quality-rails/scripts/run_quality_gates.sh --bootstrap`
  - `python workflow1/codex-phase3-quality-rails/scripts/configure_feature_flags.py`
  - `python3 unified-workflow/automation/ai_executor.py --phase 3 --project "<name>"`

### Phase 4 — Integration / Quality Audit
- Responsibilities
  - Run unified quality audit orchestrator; generate observability pack and SLO/SLI.
- Artifacts
  - `docs/Observability_Spec.md`, `docs/SLO_SLI.md`, `CHANGELOG.md`, `evidence/phase4/*`
- Commands
  - `python workflow1/codex-phase4-integration/scripts/generate_observability_pack.py`
  - `bash workflow1/codex-phase4-integration/scripts/run_staging_smoke.sh`
  - `python3 unified-workflow/automation/ai_executor.py --phase 4 --project "<name>"`

### Phase 5 — Launch
- Responsibilities
  - Create deployment runbooks, rollback plan, backup/DR, release notes; readiness review.
- Artifacts
  - `Deployment_Runbook.md`, `Rollback_Plan.md`, `Prod_Observability.md`, `Backup_Policy.md`, `DR_Plan.md`, `GoLive_Checklist.md`, `Release_Notes.md`, `evidence/phase5/*`
- Commands
  - `bash workflow1/codex-phase5-launch/scripts/rehearse_rollback.sh`
  - `bash workflow1/codex-phase5-launch/scripts/verify_dr_restore.sh`
  - `python3 unified-workflow/automation/ai_executor.py --phase 5 --project "<name>"`

### Phase 6 — Operations
- Responsibilities
  - Monitor SLOs, schedule retros, maintain dependency/security logs; perform RCA when needed.
- Artifacts
  - `Postmortem_*.md`, `Dependency_Update_Log.md`, `Security_Update_Log.md`, `evidence/phase6/*`
- Commands
  - `python workflow1/codex-phase6-operations/scripts/monitor_slo.py`
  - `python workflow1/codex-phase6-operations/scripts/schedule_retros.py`
  - `python3 unified-workflow/automation/ai_executor.py --phase 6 --project "<name>"`

## Quality & Validation Gates (Unified)
- Always log via `unified-workflow/automation/evidence_manager.py`.
- Run quality gates per phase using `unified-workflow/automation/quality_gates.py`.
- Use human validation checkpoints from `validation_gates.py`:
  - `phase_{n}_approval | phase_{n}_confirmation | phase_{n}_review | phase_{n}_audit_results | phase_{n}_retrospective | phase_{n}_operations_readiness`.

## System Instruction Formatter (SIF) Usage
- Normalize directives in protocols/rules before applying.
- Canonical tags: `[STRICT]`, `[GUIDELINE]`, `[CRITICAL]`, `[REQUIRED]`, `[OPTIONAL]`.
- Conflict handling:
  - Apply precedence (Master > Project > Local; `[STRICT]` > `[CRITICAL]` > `[REQUIRED]` > `[GUIDELINE]` > `[OPTIONAL]`).
  - If not auto-resolvable → emit `[RULE CONFLICT]` with quotes and pause.

## When to Use Original Scripts
- Generation:
  - `scripts/generate_client_project.py`, `scripts/generate_from_brief.py`
- Planning:
  - `scripts/plan_from_brief.py`, `scripts/pre_lifecycle_plan.py`
- Compliance/Validation:
  - `scripts/validate_compliance_assets.py`, `scripts/validate_tasks.py`, `scripts/enforce_gates.py`
- Orchestration (legacy configs):
  - `scripts/run_workflow.py` with `scripts/workflow_automation/*`

## Evidence Canonical Structure

evidence/
phaseN/
manifest.json
run.log
validation.md

- Checksums only for files (directories logged without checksum).

## Safety & Approvals
- Stop at human gates for:
  - Security-sensitive changes
  - Deployments and DR rehearsals
  - Policy conflicts or formatter validation errors

## Fallbacks
- If any phase asset is missing → scaffold using workflow1 templates, then re-run the unified executor.
- If configs diverge → prefer unified-workflow conventions; record deviations in `validation.md`.

## Quickstart (All Phases)