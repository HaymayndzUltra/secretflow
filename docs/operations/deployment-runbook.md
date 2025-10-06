# Deployment Runbook

This runbook standardizes staging and production deployments for the unified workflow stack. Follow each checklist sequentially and record evidence in the referenced locations.

## 1. Pre-Deployment Checklist
- [ ] Change log reviewed and approved by Release Manager.
- [ ] `git status` clean on deployment workstation.
- [ ] Dependencies installed (`pip install -r requirements.txt`).
- [ ] Telemetry baseline captured:
  ```bash
  python -m unified_workflow.cli --show-telemetry > artifacts/operations/metrics/$(date +%Y%m%d)_predeploy_telemetry.txt
  ```
- [ ] Backups validated (`python scripts/backup_workflows.py`).

## 2. Staging Deployment (Day 5)
1. **Build & Package**
   ```bash
   python scripts/deploy/package_workflow.py --output dist/workflow.zip
   ```
2. **Publish Task Definition**
   - Review `deploy/aws/task-definition.json` and update image tags.
   - Register with AWS:
     ```bash
     aws ecs register-task-definition --cli-input-json file://deploy/aws/task-definition.json
     ```
3. **Deploy to Staging Cluster**
   ```bash
   aws ecs update-service --cluster governor-staging --service workflow --force-new-deployment
   ```
4. **Run Smoke Suite**
   ```bash
   python scripts/itest/run_smoke.py --verbose
   ```
5. **Health Verification**
   ```bash
   python scripts/health/check_deployment.py --env staging
   ```
6. **Acceptance Validation**
   ```bash
   pytest tests/test_template_registry.py tests/test_evidence_schema.py
   ```
7. **Record Evidence**
   - Save logs and command outputs under `artifacts/operations/metrics/<date>_staging.md`.

## 3. Production Deployment (Day 6-7)
1. **Go/No-Go**
   - Confirm staging sign-off documented in `artifacts/operations/metrics/<date>_staging.md`.
   - Notify stakeholders via `#governor-ops` and schedule maintenance window.
2. **Deploy**
   ```bash
   aws ecs update-service --cluster governor-prod --service workflow --force-new-deployment
   ```
3. **Post-Deployment Checks**
   ```bash
   python scripts/health/check_deployment.py --env production
   python -m unified_workflow.cli --show-telemetry > artifacts/operations/metrics/$(date +%Y%m%d)_postdeploy_telemetry.txt
   ```
4. **Monitoring**
   - Observe error rate, latency, and throughput dashboards for 60 minutes.
   - Capture snapshots or export metrics to `artifacts/operations/metrics/<date>_prod.md`.
5. **Stakeholder Update**
   - Post summary in `#governor-ops` with links to telemetry and health reports.

## 4. Rollback Procedure
1. **Trigger rollback**
   ```bash
   aws ecs update-service --cluster governor-<env> --service workflow --force-new-deployment --deployment-configuration maximumPercent=0 minimumHealthyPercent=0
   ```
   Or execute `scripts/rollback_backend.sh` if available for the target stack.
2. **Restore Evidence**
   ```bash
   python scripts/restore_workflows.py --source backups/workflows_backup.tar.gz
   ```
3. **Communicate**
   - Page on-call via PagerDuty if user impact observed.
   - Document incident in `unified_workflow/test-project/incident-reports/` within 1 hour.
4. **Post-Rollback Validation**
   - Run smoke tests and telemetry capture to confirm system stability.

## 5. Monitoring Checklist (Final Gate)
- [ ] Error rate < 1% for 60 minutes post-deploy.
- [ ] Latency within SLO thresholds (document values in metrics report).
- [ ] Telemetry shows unified command routing for `run-workflow`, `validate-compliance`, and `generate-project`.
- [ ] Support channels notified of deployment status.

> [!IMPORTANT]
> Archive all command output logs alongside the metrics report for audit readiness. Use consistent filenames with timestamps to simplify traceability.
