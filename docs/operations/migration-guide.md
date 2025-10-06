# Migration Guide: Legacy Workflows to Unified Workflow 2.0

## Overview
This guide walks operators and developers through upgrading existing Workflow1 deployments to the unified workflow stack introduced in Week 7. The process preserves automation scripts, evidence archives, and operator ergonomics while consolidating control under the new governance engine and CLI compatibility layer.

## Audience & Prerequisites
- **Audience:** Platform operators, release engineers, and tech leads responsible for workflow automation.
- **Requires:**
  - Access to the legacy `workflow1` repository and associated evidence storage.
  - Python 3.10+, Docker 24+, and the unified Workflow 2.0 repository checked out locally.
  - Credentials for artifact registries, monitoring backends, and database instances referenced by active projects.

## Key Changes in Workflow 2.0
1. **Unified CLI (`unified_workflow/cli.py`):** Legacy scripts now route through a compatibility layer with telemetry and health checks.
2. **Template Registry Normalization:** Template packs share a single manifest, eliminating divergence between generator and runtime templates.
3. **Evidence Schema Harmonization:** Historical evidence can be upgraded via the evidence schema converter to support richer metadata.
4. **Governed Deployment Runbooks:** Deployment pipelines now follow staged rollout playbooks with automated acceptance gates.

## Migration Timeline
| Phase | Duration | Output |
| --- | --- | --- |
| Preparation | 0.5 day | Inventory of active workflows, dependency matrix, backup confirmation |
| Dry Run | 1 day | Staging environment validated with migrated data |
| Production Cutover | 0.5 day | Unified CLI activated, telemetry baselined |
| Stabilization | 1 day | Monitoring checkpoints completed, rollback window maintained |

## Step-by-Step Migration
1. **Inventory & Backups**
   - Run `python scripts/backup_workflows.py` to archive workflow manifests and produce `backups/last_success.json` for inventory tracking.
   - Snapshot production databases and evidence buckets. Document restore commands in the incident playbook.
2. **Upgrade Local Tooling**
   - Install requirements: `pip install -r requirements.txt`.
   - Build CLI executable: `python -m unified_workflow.cli --help` (verifies dependencies and telemetry path).
3. **Template Registry Sync**
   - Run `python scripts/generate_client_project.py --list-templates > artifacts/template-registry-sync.md` to capture the unified registry inventory.
   - Compare the output with existing workflow manifests to confirm parity. Resolve missing templates before proceeding.
4. **Evidence Schema Conversion**
   - Execute `python unified_workflow/automation/evidence_schema_converter.py --source ./workflow1/evidence --target ./unified_workflow/templates/workflow1_evidence`.
   - Review the generated diff and run unit tests: `pytest tests/test_evidence_schema.py`.
5. **CLI Compatibility Validation**
   - For each legacy command, run `python unified_workflow/cli.py <command> --help` to verify routing.
   - Confirm telemetry entries with `jq '.commands' ~/.unified-workflow/telemetry.json`.
6. **Staging Deployment**
   - Follow the staging runbook (see `deployment-runbook.md`) to deploy the migrated stack.
   - Execute acceptance tests and document results in the release checklist.
7. **Production Cutover**
   - Schedule a 2-hour maintenance window.
   - Switch operators to the new CLI shim via `pipx install .` or container image rollout.
   - Monitor dashboards for 24 hours post-cutover.

## Validation Checklist
- [ ] Telemetry shows traffic routed through unified commands.
- [ ] Acceptance tests pass in staging and production.
- [ ] Evidence converter reports zero failed items.
- [ ] Rollback plan validated (see below).

## Rollback Plan
1. Disable unified CLI entry point (`pipx uninstall unified-workflow`).
2. Restore legacy virtual environment or container image.
3. Revert evidence directories from backup snapshots.
4. Notify stakeholders via the support channels in the operator playbook.

## Frequently Asked Questions
**Q: Can we migrate incrementally per workflow?**  
Yes. The CLI shim supports per-command toggles. Use the telemetry file to confirm when a command no longer uses legacy routing before disabling it.

**Q: How do we handle custom scripts not in the registry?**  
Wrap the script with a compatibility entry in `unified_workflow/cli.py` and document the owner plus retirement date in the support playbook.

**Q: What about compliance evidence that must remain immutable?**  
Use the evidence converter's `--copy-only` flag to stage converted artifacts without deletion. Preserve the original bucket until auditors sign off.
