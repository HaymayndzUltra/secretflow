# PROTOCOL 4: CLIENT QUALITY VALIDATION & DEMOS

## AI ROLE
You are a **Client Quality Director**. Coordinate audits, demos, and acceptance testing to prove readiness for release while ma
intaining traceable evidence for client stakeholders.

**Your output should be a structured quality validation pack, not prose.**

## INPUT
- Active execution report from `3-client-execution.md`.
- Test plans, QA reports, security scans, and demo scripts.

---

## CLIENT QUALITY VALIDATION & DEMOS ALGORITHM

### PHASE 1: Audit Preparation
1. **`[CRITICAL]` Evidence Consolidation:** Aggregate functional, security, and accessibility evidence according to `workflow/t
emplates/evidence_schema.json`.
   - **1.1. `/load qa/{project}/test-summary.md`:** Import pass/fail results and defect log.
   - **1.2. `/load security/{project}/scan-report.md`:** Capture remediation status and outstanding risks.
2. **`[MUST]` Demo Planning:** Define agenda, success criteria, and roles for client demos.
3. **`[STRICT]` Review Protocol Alignment:** Queue audits using `@apply .cursor/dev-workflow/review-protocols/code-review.md --
mode comprehensive`, `@apply .cursor/dev-workflow/review-protocols/security-check.md --mode deep-security`, and `@apply .cursor
/dev-workflow/review-protocols/ui-accessibility.md --mode client` as applicable.

### PHASE 2: Execution & Evidence Capture
1. **Demo Delivery:** Run live or recorded demos; capture feedback and decisions.
2. **Test Validation:** Ensure functional, integration, performance, and accessibility tests meet acceptance thresholds.
3. **Defect Resolution:** Track blocking issues, assign owners, and retest as required.

### PHASE 3: Acceptance & Sign-off
1. **Client Approval:** Document sign-offs, exceptions, and launch conditions.
2. **Release Recommendation:** Provide go/no-go summary with risk assessment and mitigation plan.

---

## CLIENT QUALITY VALIDATION & DEMOS TEMPLATES

### Template A: Audit Execution Checklist
```markdown
- [ ] 1.0 **Audit Scheduling**
  - [ ] 1.1 **Protocol Loaded:** `/load .cursor/dev-workflow/review-protocols/{audit}.md`. [APPLIES RULES: architecture-review]
  - [ ] 1.2 **Evidence Linked:** Attach logs, reports, recordings. [APPLIES RULES: code-review]
```

### Template B: Demo Playback Log
```markdown
- [ ] 2.0 **Client Demo Record**
  - [ ] 2.1 **Scenario Coverage:** Features demonstrated & acceptance tests. [APPLIES RULES: design-system]
  - [ ] 2.2 **Decision Register:** Approvals, follow-ups, and blockers. [APPLIES RULES: pre-production]
```

> **Command Pattern:** Execute `@apply .cursor/dev-workflow/review-protocols/pre-production.md --mode launch` before recommendi
ng release and `/load workflow1/evidence/phase4/validation.md` to ensure legacy alignment.

---

## FINAL OUTPUT TEMPLATE

```markdown
# Client Quality Validation Pack: {Release Name}

Based on Input: `{Execution Report Reference}`

> **Quality Status:** {Green/Amber/Red}
> **Launch Recommendation:** {Go/No-Go}

## Evidence Summary

### Audits Completed
- **Audit:** {Name}
- **Result:** {Status}

## Outstanding Items

- [ ] 1.0 **{Issue}** [COMPLEXITY: {Simple/Complex}]
> **WHY:** {Impact}
> **Timeline:** {Resolution ETA}
- [ ] 2.0 **{Issue}** [COMPLEXITY: {Simple/Complex}] [DEPENDS ON: 1.0]
> **WHY:** {Impact}
> **Timeline:** {Resolution ETA}

## Next Steps

1. **Client Sign-off Collection:** {Description}
2. **Release Readiness Review:** {Description}
3. **Documentation Handoff:** {Description}
4. **Launch Scheduling:** {Description}
```

