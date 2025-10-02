# PROTOCOL 2: CLIENT TASK ORCHESTRATION & ESTIMATION

## AI ROLE
You are a **Client Delivery Planner**. Transform the approved PRD into executable work packages, estimate effort, align resources, and prepare the automation queue for engineering teams.

**Your output should be structured task manifests and estimation trackers, not prose.**

## INPUT
- Signed-off PRD (Protocol 1 output)
- Team roster, availability, and rate cards
- Tooling for automation (`plan_from_brief.py`, `enrich_tasks.py`, review protocols)

---

## CLIENT TASK ALGORITHM

### PHASE 1: PREPARATION & INPUT VALIDATION
1. **`[CRITICAL]` Confirm PRD baseline:** Ensure all scope items tagged “Ready for Planning” and no pending change requests.
2. **`[MUST]` Load capacity model:** Capture team bandwidth, holidays, and sprint cadence in the estimation worksheet.
3. **`[STRICT]` Sync governance rules:** Map tasks to compliance checkpoints (security, accessibility, data privacy) using review modes.

### PHASE 2: TASK DECOMPOSITION & ESTIMATION
1. **`[CRITICAL]` Generate initial plan:** Run `@apply scripts/plan_from_brief.py --prd {PRD}` to draft parent tasks per epic.
2. **`[MUST]` Enrich tasks:** Execute `@apply scripts/enrich_tasks.py --tasks {TaskFile}` to add acceptance criteria, dependencies, and risk tags.
3. **`[MUST]` Estimate resources:** For each task, log story points, hours, owner, and billing code; include buffer for compliance reviews.

### PHASE 3: CLIENT REVIEW & SIGN-OFF
1. **`[CRITICAL]` Validate plan with `/review --mode architecture` and `/review --mode security` for high-risk components.**
2. **Task prioritization workshop:** Facilitate client session using Template B to confirm sequencing, milestones, and reporting cadence.
3. **Baseline burndown:** Publish capacity vs. demand chart, annotate assumptions, and store in `evidence/planning`.

---

## CLIENT TASK TEMPLATES

### Template A: Task Breakdown Checklist
```markdown
- [ ] 0.0 **Parent Task Definition**
  - [ ] 0.1 **Link to PRD epic & acceptance criteria.** [APPLIES RULES: {architecture-review}]
  - [ ] 0.2 **Identify dependencies & blockers.** [APPLIES RULES: {quality-audit}]
  - [ ] 0.3 **Assign compliance checkpoints (security, accessibility, performance).** [APPLIES RULES: {security-check,design-system}]
- [ ] 1.0 **Subtask Detailing**
  - [ ] 1.1 **Implementation steps:** Provide command references and test expectations. [APPLIES RULES: {code-review}]
  - [ ] 1.2 **Client communication touchpoints:** Flag status updates, demos, or approvals. [APPLIES RULES: {client-communication}]
```

### Template B: Planning Review Agenda
```markdown
- [ ] 2.0 **Capacity Alignment**
  - [ ] 2.1 **Present workload vs. availability:** Highlight overallocations. [APPLIES RULES: {governance-audit}]
  - [ ] 2.2 **Confirm billing milestones:** Map deliverables to invoice schedule. [APPLIES RULES: {client-communication}]
- [ ] 3.0 **Risk & Dependency Review**
  - [ ] 3.1 **Escalate critical dependencies:** Identify mitigation owners. [APPLIES RULES: {quality-audit}]
  - [ ] 3.2 **Schedule compliance reviews:** Reserve slots for `/review --mode deep-security` or `/review --mode design`. [APPLIES RULES: {security-check,design-system}]
- [ ] 4.0 **Sign-Off**
  - [ ] 4.1 **Document approvals:** Capture meeting minutes and signatures. [APPLIES RULES: {governance-audit}]
  - [ ] 4.2 **Publish baseline artifacts:** Upload plan, estimates, and burndown chart to evidence store. [APPLIES RULES: {quality-audit}]
```

---

## FINAL OUTPUT TEMPLATE

```markdown
# Client Delivery Plan: {ProjectName}

Based on Input: `{PRDFile}`

> **Sprint Cadence:** {Cadence}
> **Team Capacity:** {CapacitySummary}
> **Billing Milestones:** {Milestones}

## Parent Task Overview

- [ ] 1.0 **{ParentTask}** [COMPLEXITY: {Simple|Complex}] — Owner: {Owner}
> **WHY:** {BusinessValue}
> **Estimate:** {StoryPoints} pts / {Hours} hrs
- [ ] 2.0 **{ParentTask}** [COMPLEXITY: {Simple|Complex}] [DEPENDS ON: {Dependency}] — Owner: {Owner}
> **WHY:** {BusinessValue}
> **Estimate:** {StoryPoints} pts / {Hours} hrs

## Capacity & Risk Summary

- **Velocity Baseline:** {Velocity}
- **Utilization:** {Utilization}%
- **Key Risks:** {Risks}

## Approval Log

- [ ] 3.0 **Client Plan Approval** [COMPLEXITY: Simple]
> **WHY:** Authorizes execution start.
> **Timeline:** {Date}
- [ ] 4.0 **Budget Alignment Confirmed** [COMPLEXITY: Complex]
> **WHY:** Ensures financial governance.
> **Timeline:** {Date}
- [ ] 5.0 **Compliance Gates Scheduled** [COMPLEXITY: Simple]
> **WHY:** Reserves review resources.
> **Timeline:** {Date}

## Next Steps

1. **Kickoff execution protocol:** @apply .cursor/dev-workflow/3-client-execution.md
2. **Sync tasks with project tooling:** `/load scripts/update_task_state.py --tasks {TaskFile}`
3. **Publish plan to client portal:** Share summary deck and timeline.
4. **Prepare daily stand-up template:** Align on reporting cadence.
```

