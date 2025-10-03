# AI Protocol Integration Guide

## Purpose

This guide explains how to connect the new client-focused workflow protocols with SecretFlow's existing automation, quality, an
d governance infrastructure. It also demonstrates usage examples for managing engagements across the delivery lifecycle.

## Integration Layers

### 1. Workflow Automation
- **Execution:** Use `scripts/run_workflow.py` with a tailored configuration that sequences the client protocols (`0-client-disc
overy.md` → `5-client-retrospective.md`).
- **Planning Hooks:** Leverage `scripts/plan_from_brief.py` and `scripts/trigger_plan.py` during discovery and planning phases f
or automated milestone generation.
- **Rollback & Deployment:** Reference `scripts/rollback_frontend.sh` and `scripts/deploy/` assets during execution phases to a
lign with change management requirements.

### 2. Project Generation
- Run `scripts/generate_client_project.py` to bootstrap industry-aligned assets before starting discovery interviews.
- Use `project_generator/core/industry_config.py` to pre-populate compliance and feature expectations for healthcare, finance,
 or e-commerce engagements.

### 3. Quality & Review Protocols
- Each client workflow template references review guides located in `.cursor/dev-workflow/review-protocols/`.
  - Example: `@apply .cursor/dev-workflow/review-protocols/code-review.md --mode architecture` during quality gates.
- Integrate specialized audits (security, accessibility) by invoking `/load` on the relevant protocol before preparing demo or
 release evidence.

### 4. Evidence and Reporting
- Align evidence artifacts with `workflow/templates/evidence_schema.json` for automated validation via `scripts/evidence_report
.py`.
- Use `.github/workflows/ci-lint.yml` and `ci-test.yml` as mandatory status checks before client demos or release sign-off.

### 5. Workflow1 Alignment
- Map client protocol outputs to `workflow1/evidence/phase{n}` directories to maintain compatibility with historical records.
- Reference `workflow1/PROJECT_EXECUTION_TEMPLATE.md` when translating client milestones into phase-based artifacts.

## Usage Examples

### Kick-off (Discovery → PRD)
1. `/load .cursor/dev-workflow/0-client-discovery.md`
2. Conduct interviews and capture findings in `discovery/client-brief.md` using the protocol's final output template.
3. `/load .cursor/dev-workflow/1-client-prd.md` to convert validated requirements into a client-facing PRD with approval gates.

### Planning & Execution
1. `/load .cursor/dev-workflow/2-client-tasks.md` to generate milestone tasks with budget and resource estimates.
2. `@apply .cursor/dev-workflow/review-protocols/architecture-review.md --mode client` to confirm architectural integrity befor
e implementation.
3. During implementation, `/load .cursor/dev-workflow/3-client-execution.md` to coordinate build activities, weekly status repo
rts, and change control reviews.

### Quality & Retrospective
1. `/load .cursor/dev-workflow/4-client-quality.md` to stage demos, run audits, and gather sign-offs.
2. Invoke `@apply .cursor/dev-workflow/review-protocols/security-check.md --mode deep-security` when high-risk changes are deli
vered.
3. `/load .cursor/dev-workflow/5-client-retrospective.md` to complete satisfaction surveys, contract extensions, and knowledge
 transfer packs.

## Multi-Client Scaling

- Maintain a per-client directory (e.g., `clients/acme-health/`) mirroring the evidence schema and storing protocol outputs.
- Automate progress dashboards by parsing the final output templates (tasks, next steps) to feed into project tracking tools.
- Use Git branches per client or engagement to isolate deliverables while sharing common automation and review assets.

## Governance & Security Notes

- Enforce MFA on all client environments and document verification within the execution protocol outputs.
- Never store secrets directly in protocol outputs; reference environment configurations and secret managers instead.
- Require human review (`.github/pull_request_template.md`) for any code or infrastructure changes surfaced during client execu
tion phases.

Following this guide ensures that the client workflow system integrates seamlessly with SecretFlow's AI Governor framework, pre
serving traceability, compliance, and delivery excellence.

