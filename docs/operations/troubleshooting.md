# Troubleshooting Guide

Use this guide to diagnose and resolve the most common issues encountered while operating the unified workflow stack and its supporting automation.

## 1. CLI & Tooling Issues
### CLI reports `Legacy script not found`
- **Symptoms:** Command exits with code `1` and log entry `Legacy script not found`.
- **Resolution:**
  1. Run `python -m unified_workflow.cli --show-telemetry` to confirm whether the unified path succeeded.
  2. If both unified and legacy paths fail, verify the repository checkout includes the `scripts/` directory.
  3. Regenerate the environment via `python scripts/doctor.py --strict` to surface missing tooling, then reinstall dependencies using `pip install -r requirements.txt`.

### CLI fallback loops between unified and legacy
- **Symptoms:** Logs show repeated attempts for the same command with alternating `unified` and `legacy` sources.
- **Resolution:**
  1. Inspect `~/.unified-workflow/telemetry.json` for the affected command's `last_exit_code`.
  2. Run the command with `--legacy` to bypass unified routing temporarily.
  3. File an issue with the telemetry snapshot attached; reference the [CLI Reference](./cli-reference.md) for context.

### Telemetry file permissions error
- **Symptoms:** CLI warning `Failed to save telemetry` with an `OSError`.
- **Resolution:** Ensure the directory exists and is writable:
  ```bash
  mkdir -p ~/.unified-workflow
  chmod 700 ~/.unified-workflow
  ```
  Re-run the command and confirm telemetry is recorded.

## 2. Migration & Template Problems
### Evidence converter raises schema mismatch
- **Symptoms:** `evidence_schema_converter.py` exits non-zero with `ValueError` referencing missing fields.
- **Resolution:**
  1. Run `pytest tests/test_evidence_schema.py -k legacy_evidence_migration` to reproduce locally.
  2. Review the offending artifact; ensure required metadata (`phase`, `artifact_type`, `source`) is present.
  3. Update the artifact and rerun the converter.

### Template inventory differs between environments
- **Symptoms:** `python scripts/generate_client_project.py --list-templates` produces divergent results across machines.
- **Resolution:**
  1. Run `git status --short` to ensure there are no untracked template files.
  2. Confirm `TEMPLATE_REGISTRY_ROOT` environment variable is unset or identical across environments.
  3. If differences persist, share the captured inventories in `artifacts/template-registry-sync.md` for comparison.

## 3. Deployment & Infrastructure Issues
### Staging deployment fails health checks
- **Symptoms:** `scripts/health/check_deployment.py --env staging` returns non-zero.
- **Resolution:**
  1. Check staging logs via your platform (e.g., `kubectl logs`, `ecs-cli logs`).
  2. Verify database migrations ran successfully (see [Deployment Runbook](./deployment-runbook.md)).
  3. Roll back using `scripts/rollback_backend.sh` if the service remains unhealthy after 10 minutes.

### Smoke tests time out
- **Symptoms:** `scripts/itest/run_smoke.py` hangs or exceeds the expected runtime.
- **Resolution:**
  1. Execute targeted subsets, e.g. `python scripts/itest/run_smoke.py --filter rules` to isolate the failure.
  2. Re-run with `--verbose` to capture stdout/stderr and attach the output to incident notes.
  3. Escalate to the release manager if blocking for more than one release window.

### Production rollout triggers elevated error rates
- **Symptoms:** Monitoring dashboards show >2% error rate within 15 minutes of deployment.
- **Resolution:**
  1. Initiate rollback using the playbook in [deployment-runbook.md](./deployment-runbook.md#rollback-procedure).
  2. Capture metrics snapshots (latency, error budget burn) and attach to the incident report template in `unified_workflow/test-project/incident-reports/`.
  3. Review telemetry to determine whether unified CLI usage changed during the incident.

## 4. Support & Escalation
- Consult the [Support Playbook](./support-playbook.md) for channel ownership, rotation schedules, and escalation matrices.
- For unresolved issues, open an incident in the monitoring dashboard (see `monitoring-dashboards/README.md`) and page the on-call operator.
