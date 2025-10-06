# Operator Quickstart

Welcome! This guide equips new operators to execute daily duties across documentation, workflow automation, and deployments in under two hours.

## 1. Environment Setup (20 minutes)
1. **Clone the repository** and install dependencies:
   ```bash
   git clone <repo-url>
   cd secretflow
   pip install -r requirements.txt
   ```
2. **Verify tooling** using the environment doctor:
   ```bash
   python scripts/doctor.py --strict
   ```
3. **Prime telemetry** by invoking a no-op command:
   ```bash
   python -m unified_workflow.cli --version
   ```

## 2. Understand the Workflow (25 minutes)
1. Read the [Unified Workflow Overview](../unified_workflow/README.md).
2. Review the [CLI Reference](./cli-reference.md) to learn core commands.
3. Skim the [Migration Guide](./migration-guide.md) focusing on backup and rollback expectations.

## 3. Hands-On Exercise (30 minutes)
Follow this mini-scenario to practice the critical tasks.

1. **Generate a demo project**
   ```bash
   python -m unified_workflow.cli generate-project --name demo --industry healthcare
   ```
   - Confirm output directories under `outputs/demo` or the configured destination.
2. **Run the automation workflow in dry-run mode**
   ```bash
   python -m unified_workflow.cli run-workflow -- --config workflow/templates/workflow_backend.yaml --dry-run
   ```
   - Observe console output for gate status and capture notes if any step fails.
3. **Inspect telemetry**
   ```bash
   python -m unified_workflow.cli --show-telemetry
   ```
   - Validate that `generate-project` and `run-workflow` routed through the unified path.
4. **Practice troubleshooting**
   - Intentionally run a legacy path: `python -m unified_workflow.cli --legacy validate-tasks -- --input tasks.json`.
   - Check the [Troubleshooting Guide](./troubleshooting.md) for fallback handling tips.

## 4. Deployment Dry Run (25 minutes)
1. Review the [Deployment Runbook](./deployment-runbook.md) to understand staging vs. production flows.
2. Execute the staging verification steps locally:
   ```bash
   python scripts/health/check_deployment.py --env staging
   ```
   - Review `deploy/aws/task-definition.json` to understand container expectations prior to real deployments.
3. Capture notes in `unified_workflow/test-project/incident-reports/README.md` on any deviations.

## 5. Support Channels & Escalation (10 minutes)
- Bookmark the [Support Playbook](./support-playbook.md) for contact routes and SLAs.
- Join the project Slack/Teams workspace and subscribe to #governor-ops, #deployments, and #support.
- Confirm you can access monitoring dashboards listed in `unified_workflow/test-project/monitoring-dashboards/README.md`.

## Completion Checklist
- [ ] Environment verified with `doctor.py --strict`.
- [ ] CLI commands executed successfully (generate, run-workflow, validate).
- [ ] Telemetry reflects unified routing.
- [ ] Staging health check run without errors.
- [ ] Support resources bookmarked and accessible.

> [!NOTE]
> Capture feedback from each onboarding session in `artifacts/training/retro.md` (create the file if it does not yet exist) to continuously refine the program.
