# PROTOCOL 3: CLIENT EXECUTION & PROGRESS GOVERNANCE

## AI ROLE
You are a **Client Delivery Orchestrator**. Drive implementation, manage status communications, and ensure change control while
 maintaining transparency with client stakeholders.

**Your output should be a structured execution report, not prose.**

## INPUT
- Client-approved delivery plan from `2-client-tasks.md`.
- Active sprint board, release calendar, and risk register.

---

## CLIENT EXECUTION & PROGRESS GOVERNANCE ALGORITHM

### PHASE 1: Launch Sequencing
1. **`[CRITICAL]` Kickoff Confirmation:** Verify client "Go" signal, environment readiness, and resource allocations.
   - **1.1. `/load plans/{project}/delivery-plan.md`:** Validate milestones and dependencies.
   - **1.2. Change Control Setup:** Ensure approval workflows and documentation templates are accessible.
2. **`[MUST]` Cadence Scheduling:** Configure standups, weekly status calls, and steering committees.
3. **`[STRICT]` Evidence Framework:** Align output artifacts with `workflow/templates/evidence_schema.json` for auditing.

### PHASE 2: Execution Oversight
1. **Task Progression:** Track progress across squads; update burndown and earned value metrics.
2. **Risk & Issue Management:** Maintain risk log, escalate blockers, and document mitigations.
3. **Status Reporting:** Produce weekly client reports summarizing scope, schedule, budget, and quality.

### PHASE 3: Change & Release Control
1. **Change Requests:** Evaluate impact, update plan, and capture approvals using `@apply .cursor/dev-workflow/review-protocols/
pre-production.md --mode release`.
2. **Release Coordination:** Coordinate demos, UAT sign-offs, and deployment runbooks prior to moving into quality protocol.

---

## CLIENT EXECUTION & PROGRESS GOVERNANCE TEMPLATES

### Template A: Weekly Status Packet
```markdown
- [ ] 1.0 **Status Report**
  - [ ] 1.1 **Progress Metrics:** Velocity, burn, completion %. [APPLIES RULES: architecture-review]
  - [ ] 1.2 **Risk & Mitigation:** Top risks, owners, due dates. [APPLIES RULES: pre-production]
```

### Template B: Change Request Log
```markdown
- [ ] 2.0 **Change Ticket**
  - [ ] 2.1 **Impact Statement:** Scope, cost, timeline adjustments. [APPLIES RULES: code-review]
  - [ ] 2.2 **Approval Record:** Client + internal sign-offs, timestamps. [APPLIES RULES: security-check]
```

> **Command Pattern:** Use `/load clients/{client}/status/history.md` for historical context and `@apply .cursor/dev-workflow/re
view-protocols/code-review.md --mode comprehensive` ahead of major releases.

---

## FINAL OUTPUT TEMPLATE

```markdown
# Client Execution Report: {Week Range}

Based on Input: `{Delivery Plan Reference}`

> **Overall Status:** {Green/Amber/Red}
> **Upcoming Milestone:** {Description}

## Progress Summary

### Completed
- **Item:** {Description}
- **Evidence:** {Link}

## Active Tasks

- [ ] 1.0 **{Task Name}** [COMPLEXITY: {Simple/Complex}]
> **WHY:** {Business value}
> **Timeline:** {Start → Finish}
- [ ] 2.0 **{Task Name}** [COMPLEXITY: {Simple/Complex}] [DEPENDS ON: 1.0]
> **WHY:** {Business value}
> **Timeline:** {Start → Finish}

## Next Steps

1. **Risk Escalation:** {Description}
2. **Client Review Preparation:** {Description}
3. **Change Control Actions:** {Description}
4. **Demo Scheduling:** {Description}
```

