# Support Playbook

This playbook defines communication channels, escalation paths, and runbook references to keep the unified workflow platform healthy post-deployment.

## 1. Contact Channels
| Channel | Purpose | Hours | Notes |
| --- | --- | --- | --- |
| `#governor-ops` (Slack/Teams) | Real-time collaboration for operators handling deployments and incidents. | 24/5 (business days) | Primary coordination room; pin current on-call roster. |
| `#governor-support` | End-user and stakeholder requests. | 16/5 | Triage within 30 minutes; escalate to ops if blocking. |
| `ops@company.com` | Formal ticket intake and audit trail. | 24/7 | Auto-creates tickets in service desk. |
| PagerDuty "Governor Platform" | Critical incidents (P0/P1). | 24/7 | Pages on-call engineer; follow incident response guide. |

## 2. Roles & Responsibilities
- **Primary Operator:** Owns daily deployments, monitors telemetry, and updates task boards.
- **Secondary Operator:** Backup for primary; handles documentation updates and retrospective notes.
- **Release Manager:** Approves production pushes and coordinates with stakeholders.
- **SRE Liaison:** Ensures infrastructure-level issues are escalated and tracked.

Maintain an updated roster in `artifacts/support/on-call-roster.md` (create if missing). Include contact methods and coverage windows.

## 3. Triage Workflow
1. **Intake:** Monitor `#governor-support` and service desk tickets. Acknowledge within 15 minutes.
2. **Assess Severity:**
   - P0: Production outage or critical data loss. Page immediately.
   - P1: Degraded functionality affecting multiple users; respond within 15 minutes.
   - P2: Standard support request; respond within 4 hours.
3. **Engage Runbooks:**
   - Consult the [Troubleshooting Guide](./troubleshooting.md).
   - For deployment or migration-related issues, reference the [Deployment Runbook](./deployment-runbook.md) and [Migration Guide](./migration-guide.md).
4. **Status Updates:** Post updates every 30 minutes for P0/P1 incidents, hourly for P2.
5. **Resolution & Handoff:** Document resolution details in the relevant incident report template and update telemetry snapshots if applicable.

## 4. Knowledge Management
- Store root cause analyses in `unified_workflow/test-project/incident-reports/`.
- Capture deployment metrics and health snapshots in `artifacts/operations/metrics/<date>.md`.
- Ensure docs in `docs/operations/` stay current; submit PRs for changes within 24 hours of learning.

## 5. Escalation Matrix
| Severity | Primary | Secondary | Additional Stakeholders |
| --- | --- | --- | --- |
| P0 | PagerDuty on-call | Release Manager | CTO, Head of Product |
| P1 | Primary Operator | Secondary Operator | Release Manager |
| P2 | Primary Operator | Docs Lead | Product Owner |

## 6. Post-Incident Checklist
- [ ] Incident report completed and stored in repo.
- [ ] Telemetry snapshot archived in `artifacts/operations/metrics/`.
- [ ] Lessons learned shared in #governor-ops.
- [ ] Follow-up tasks logged in `tasks.json` or service desk.
- [ ] Documentation updated as necessary.

> [!REMINDER]
> Run a weekly sync between Operators, Release Manager, and SRE Liaison to review outstanding actions and verify support tooling health.
