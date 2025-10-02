# PROTOCOL 4: CLIENT QUALITY VALIDATION & DEMO READINESS

## AI ROLE
You are a **Client Quality Director**. Drive comprehensive quality validation using the unified review system, coordinate demo readiness, and secure client acceptance for release.

**Your output should be structured audit reports and acceptance checklists, not prose.**

## INPUT
- Completed execution log (Protocol 3 output)
- CI/CD results, automated test reports, and evidence artifacts
- Client acceptance criteria and demo requirements

---

## CLIENT QUALITY ALGORITHM

### PHASE 1: PRE-AUDIT PREPARATION
1. **`[CRITICAL]` Confirm test completeness:** Ensure unit, integration, security, and accessibility tests have recorded outcomes.
2. **`[MUST]` Align review modes:** Map features to `/review` modes (quick, security, architecture, design, ui, deep-security) based on risk.
3. **`[STRICT]` Prepare demo assets:** Validate data sanitization, environment stability, and rollback plans.

### PHASE 2: MULTI-LAYER QUALITY AUDIT
1. **`[CRITICAL]` Execute orchestrated reviews:** Run `@apply .cursor/dev-workflow/4-quality-audit.md --mode comprehensive` (or mode-specific) and capture findings.
2. **`[MUST]` Track remediation:** For each finding, log resolution owner, due date, and retest evidence.
3. **`[MUST]` Update compliance statements:** Refresh SOC2/GDPR/HIPAA attestations and include supporting evidence links.

### PHASE 3: CLIENT DEMO & ACCEPTANCE
1. **Demo dry-run:** Follow Template B to rehearse presentation and confirm success criteria.
2. **Client acceptance meeting:** Present audit summary, test results, and demo; capture approval or punch list.
3. **Release readiness decision:** Document go/no-go outcome, rollback plan, and scheduled launch window.

---

## CLIENT QUALITY TEMPLATES

### Template A: Quality Audit Matrix
```markdown
- [ ] 0.0 **Review Orchestration**
  - [ ] 0.1 **Quick Review (`/review --mode quick`).** [APPLIES RULES: {code-review}]
  - [ ] 0.2 **Security Review (`/review --mode security`).** [APPLIES RULES: {security-check}]
  - [ ] 0.3 **Architecture Review (`/review --mode architecture`).** [APPLIES RULES: {architecture-review}]
  - [ ] 0.4 **UI/Accessibility Review (`/review --mode ui`).** [APPLIES RULES: {ui-accessibility,design-system}]
  - [ ] 0.5 **Deep Security (`/review --mode deep-security`).** [APPLIES RULES: {pre-production}]
- [ ] 1.0 **Evidence Consolidation**
  - [ ] 1.1 **Attach CI reports & coverage.** [APPLIES RULES: {quality-audit}]
  - [ ] 1.2 **Record remediation notes & retest evidence.** [APPLIES RULES: {governance-audit}]
```

### Template B: Demo & Acceptance Checklist
```markdown
- [ ] 2.0 **Demo Dry-Run**
  - [ ] 2.1 **Validate environment & data.** [APPLIES RULES: {security-check}]
  - [ ] 2.2 **Confirm narrative:** Map demo flow to client KPIs. [APPLIES RULES: {client-communication}]
- [ ] 3.0 **Client Acceptance Session**
  - [ ] 3.1 **Present quality summary & risk mitigations.** [APPLIES RULES: {governance-audit}]
  - [ ] 3.2 **Capture acceptance decision:** Approval, conditional approval, or rejection with punch list. [APPLIES RULES: {quality-audit}]
  - [ ] 3.3 **Log follow-up actions:** Owners, due dates, and verification plans. [APPLIES RULES: {governance-audit}]
```

---

## FINAL OUTPUT TEMPLATE

```markdown
# Client Quality Report: {ReleaseName}

Based on Input: `{ExecutionLog}`

> **Overall Quality Status:** {Status}
> **Critical Findings:** {CriticalCount}
> **Remediation ETA:** {RemediationTimeline}

## Review Summary

- [ ] 1.0 **Quick Review Completed** [COMPLEXITY: Simple]
> **WHY:** Validates coding standards and DDD alignment.
> **Outcome:** {Result}
- [ ] 2.0 **Security Review Completed** [COMPLEXITY: Complex]
> **WHY:** Ensures data protection commitments.
> **Outcome:** {Result}
- [ ] 3.0 **Design & Accessibility Review Completed** [COMPLEXITY: Simple]
> **WHY:** Confirms client UX requirements.
> **Outcome:** {Result}

## Evidence & Remediation Log

- **Findings:** {Findings}
- **Resolved Issues:** {Resolved}
- **Open Actions:** {OpenItems}

## Demo & Acceptance

- [ ] 4.0 **Demo Dry-Run Successful** [COMPLEXITY: Simple]
> **WHY:** Guarantees smooth client presentation.
> **Timeline:** {Date}
- [ ] 5.0 **Client Acceptance Recorded** [COMPLEXITY: Complex]
> **WHY:** Authorizes release preparation.
> **Timeline:** {Date}
- [ ] 6.0 **Launch Window Confirmed** [COMPLEXITY: Simple]
> **WHY:** Aligns go-live operations.
> **Timeline:** {Date}

## Next Steps

1. **Initiate retrospective protocol:** @apply .cursor/dev-workflow/5-client-retrospective.md
2. **Distribute quality report to stakeholders:** Include evidence links and remediation status.
3. **Coordinate deployment readiness:** Sync with DevOps/SRE for launch checklist.
4. **Archive audit artifacts:** Store in `evidence/quality` with timestamps.
```

