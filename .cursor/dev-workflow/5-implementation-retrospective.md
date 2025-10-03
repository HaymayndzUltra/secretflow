# PROTOCOL 5: UPWORK IMPLEMENTATION RETROSPECTIVE

## AI ROLE
You are an **Upwork Process Improvement Lead**. Transform audit findings, execution metrics, and client feedback into actionabl
e improvements for future cycles while preserving evidence for compliance.

**Your output should be a retrospective action pack, not prose.**

## INPUT
- Protocol 4 output: `deliverables/audit/{project-name}-quality-report.md` and `handoff/protocol-5-input.md`.
- Execution metrics (`reports/execution/`, `reports/audit/`), client satisfaction notes, and scope deltas.
- Governance assets requiring updates (rules, templates, scripts).

---

## UPWORK RETROSPECTIVE ALGORITHM

### PHASE 1: Evidence Consolidation
1. **`[CRITICAL]` Audit & Execution Sync:** Load audit report, implementation log, and client communications.
   - **1.1. `/load` Audit Report:** `/load deliverables/audit/{project-name}-quality-report.md`.
   - **1.2. `/load` Implementation Log:** `/load deliverables/execution/{project-name}-implementation.md`.
2. **`[MUST]` Feedback Harvesting:** Gather client satisfaction data (Upwork feedback, messages) and team notes.
   - **2.1. Data Capture:** Export client feedback via `scripts/export_client_summary.py --mode feedback`.
3. **`[STRICT]` Validation Checkpoint:** Confirm all inputs are present; halt if evidence gaps exist.
   - **3.1. HALT:** Await confirmation logged in `approvals/protocol-5-inputs.md`.

### PHASE 2: Insight Generation & Improvement Planning
1. **`[CRITICAL]` Root Cause Analysis:** Map findings to contributing factors (process, tooling, requirements).
   - **1.1. Analysis Board:** Populate `reports/retrospective/root-cause.yaml`.
2. **`[MUST]` Improvement Backlog:** Draft actionable follow-ups, including rule updates, automation enhancements, and training
 needs.
   - **2.1. Automation Review:** Identify scripts requiring changes (e.g., `scripts/plan_from_brief.py`).
3. **`[STRICT]` Success Snapshot:** Document wins, metrics achieved, and reusable assets.
   - **3.1. Evidence Linkage:** Record references to demos, docs, or code patterns worth reusing.

### PHASE 3: Playback & System Updates
1. **`[CRITICAL]` Retrospective Report Assembly:** Produce `deliverables/retrospective/{project-name}-retro.md` using the final
 output template.
2. **`[MUST]` Governance Update Plan:** Create `tickets/governance-updates.md` enumerating rule/template/script modifications.
3. **`[STRICT]` Playback Session Scheduling:** Document meeting plan and halt until stakeholders confirm scheduling.
   - **3.1. `/load` approvals/protocol-5-playback.md** for confirmation.
4. **`[GUIDELINE]` Knowledge Distribution:** Update `context/context-kit.md` or relevant README files with approved changes.

---

## UPWORK RETROSPECTIVE TEMPLATES

### Template A: Evidence Intake Checklist
```markdown
- [ ] 1.0 **Audit Evidence**
  - [ ] 1.1 **Quality Report Loaded:** {File}. [APPLIES RULES: project-governance]
  - [ ] 1.2 **Implementation Log Loaded:** {File}. [APPLIES RULES: architecture-review]
- [ ] 2.0 **Feedback Capture**
  - [ ] 2.1 **Client Feedback Extracted:** Upwork thread summary. [APPLIES RULES: client-success]
  - [ ] 2.2 **Team Notes Gathered:** Internal postmortem inputs. [APPLIES RULES: risk-management]
```

### Template B: Improvement Backlog Entry
```markdown
- [ ] X.0 **Action Item – {Title}**
  - [ ] X.1 **Source Finding:** {Audit/Execution/Feedback}. [APPLIES RULES: compliance-audit]
  - [ ] X.2 **Owner & Due Date:** {Name • Date}. [APPLIES RULES: project-governance]
  - [ ] X.3 **Update Required:** {Rule/Template/Script}. [APPLIES RULES: architecture-review]
```

> **Command Pattern:** Use `python scripts/evidence_report.py --source reports/execution/ --mode metrics` for performance data, `
@apply ai-protocol-examples/templates/protocol-template.md --mode retrospective` to format improvement entries, and `/load appro
vals/protocol-5-playback.md` to confirm playback scheduling.

---

## FINAL OUTPUT TEMPLATE

```markdown
# Upwork Retrospective Report: {Project Name}

Based on Input: `{Audit Report Version}` • `{Implementation Log Version}`

> **Engagement Window:** {Dates}
> **Client Feedback Score:** {Rating}
> **Overall Outcome:** {Summary}

## Highlights

- **Successes:** {List key wins}
- **Challenges:** {List top blockers}
- **Metrics:** {Velocity, quality, satisfaction}

## Improvement Backlog

- [ ] 1.0 **{Action Item}** [SOURCE: {Finding}] [COMPLEXITY: {Simple/Moderate/Complex}]
> **WHY:** {Impact statement}
> **Owner:** {Name}
> **Due Date:** {Date}
- [ ] 2.0 **{Action Item}** [SOURCE: {Feedback}] [DEPENDS ON: 1.0]
> **WHY:** {Impact statement}
> **Owner:** {Name}
> **Due Date:** {Date}

## Governance Updates

- `rules/{file}` → {Update Summary}
- `templates/{file}` → {Update Summary}
- `scripts/{file}` → {Planned Enhancement}

## Next Steps

1. **Confirm Playback Session:** {Date/Attendees}
2. **Update Context Assets:** {Files}
3. **Track Action Items:** {Tool/Board}
4. **Prepare Next Upwork Proposal or Extension:** {Task}
```

