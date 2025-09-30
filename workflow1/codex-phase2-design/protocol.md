# Codex Phase 2 — Design & Planning Protocol

This protocol extends `workflow1` Phase 1–2 guidance to satisfy AGENTS Phase 2 deliverables. It builds on [`0-bootstrap-your-project.md`](../0-bootstrap-your-project.md) and [`1-create-prd.md`](../1-create-prd.md) while aligning with the AGENTS instructions in `/workspace/Labs-test2/AGENTS.md`.

## Objectives
- Transform the Phase 1 discovery bundle into executable architecture, backlog, and environment assets.
- Produce contract-first specifications (OpenAPI, data) and repository governance docs.
- Ensure exit gates for ADR approval, OpenAPI validation, CI skeleton readiness, and backlog prioritisation are automated.

## Inputs
- Charter, requirements, initial risks from Phase 1 evidence.
- `docs/LOCAL_DEV_WORKFLOW.md` automation (planning + scaffold commands).
- Existing workflow1 templates for briefs, PRDs, and tasks.

## Required Artefacts
- `templates/Architecture.md`
- `templates/C4/context.mmd`
- `templates/C4/container.mmd`
- `templates/ADR-template.md`
- `templates/Product_Backlog.csv`
- `templates/Sprint0_Plan.md`
- `templates/Env_Strategy.md`
- `templates/Repo_Policy.md`
- `templates/Coding_Standards.md`
- `templates/OpenAPI/README.md`

## Automation Scripts
- `scripts/generate_architecture_pack.py`
  - Copies the architecture templates into a project-specific package and updates the evidence manifest.
- `scripts/generate_contract_assets.py`
  - Generates OpenAPI, backlog, and Sprint 0 scaffolds using `docs/LOCAL_DEV_WORKFLOW.md` commands as defaults.

All scripts emit logs to `../evidence/phase2/run.log` and update the manifest so Codex can report completion.

## Procedure
1. Run planning automation (`make plan-from-brief`) per `docs/LOCAL_DEV_WORKFLOW.md`.
2. Execute `python scripts/generate_architecture_pack.py --project <slug>`.
3. Execute `python scripts/generate_contract_assets.py --project <slug> --service <name>`.
4. Validate outputs:
   - `adr validate` (ensures no TODO decisions remain).
   - `npm run lint` / `pip install -r requirements.txt && pytest -q` to confirm CI skeleton.
   - `npx @redocly/cli lint openapi/<service>.yaml` to ensure contract validity.
5. Document validation status in `../evidence/phase2/validation.md` and attach checksums via manifest script output.

## Exit Criteria
- All required artefacts generated with owner + status filled.
- Evidence files (`run.log`, `validation.md`, `manifest.json`) updated with current timestamps.
- ADRs approved (no `Status: Pending`).
- OpenAPI lints clean; mock server script defined.
- CI skeleton (lint/type/build) succeeds locally.
- Backlog contains ≥2 sprints and AC references for each backlog item.

## Dependencies
- Python 3.10+
- Node tooling for lint/testing (per project stack)
- `redocly-cli` (npm) or `speccy` for OpenAPI validation
- Access to repository to create ADR/backlog branches

## Evidence Logging
Scripts automatically append entries to `../evidence/phase2/run.log` and update `manifest.json`. Manual actions must also be summarised. Validation outcomes (`PASS`/`FAIL` with reason) belong in `validation.md`.

## Related Protocols
- Protocol 0–1 for upstream discovery.
- Protocol 3+ for subsequent quality, integration, launch, and operations gates.
