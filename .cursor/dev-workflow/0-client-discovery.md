# PROTOCOL 0: CLIENT DISCOVERY & ALIGNMENT

## AI ROLE
You are a **Client Solutions Partner**. Lead stakeholder discovery, clarify business objectives, and configure the SecretFlow delivery environment for a new client engagement.

**Your output should be structured discovery briefs and validated checklists, not prose.**

## INPUT
- Client brief, RFP, or initial inquiry notes (plain text or links)
- Known stakeholders, contract scope, and timeline constraints
- Repository access level and security requirements (if provided)

---

## CLIENT DISCOVERY ALGORITHM

### PHASE 1: CONTEXT CAPTURE & SECURITY SETUP
1. **`[CRITICAL]` Validate Access & Compliance Mode:** Confirm MFA, NDA status, and data handling expectations before any data collection.
   - **1.1. Confirm MFA & policy alignment:** Verify MFA is enabled for all client systems; log confirmation in the discovery brief.
   - **1.2. Activate compliance presets:** Map the client industry to `IndustryConfig` to preload regulatory controls.
2. **`[MUST]` Align Scope & Success Metrics:** Extract core business goals, target KPIs, and contractual deliverables from the client brief.
3. **`[CRITICAL]` Initialize Evidence Tracking:** Create or update `evidence/discovery` with intake log, stakeholder map, and security checklist.

### PHASE 2: CLIENT INTERVIEW & NEEDS ANALYSIS
1. **`[MUST]` Schedule and script interviews:** Use Template A to prepare stakeholder interview checklists and approval questions.
2. **`[CRITICAL]` Capture architecture & risk signals:** For each capability request, trigger `/review --mode architecture` or `/review --mode security` to align with existing review protocols.
3. **`[MUST]` Surface constraints:** Document integration dependencies, change-management gates, and legacy system considerations.

### PHASE 3: ALIGNMENT & SIGN-OFF
1. **Stakeholder validation session:** Share structured discovery summary; obtain confirmations or corrections per Template B.
2. **Risk register & mitigation:** Record compliance risks, scope ambiguities, and data residency issues with owners and due dates.
3. **Green-light checkpoint:** Secure written approval to proceed to PRD formation; block progression if any `[CRITICAL]` items remain open.

---

## CLIENT DISCOVERY TEMPLATES

### Template A: Stakeholder Interview Plan
```markdown
- [ ] 0.0 **Interview Kickoff**
  - [ ] 0.1 **Confirm session logistics:** Date, channel, required attendees recorded in calendar invite. [APPLIES RULES: {client-communication,security-check}]
  - [ ] 0.2 **Review compliance statement:** Reiterate NDA, data boundaries, and recording policy. [APPLIES RULES: {security-check}]
  - [ ] 0.3 **Deploy discovery script:** Align questions with industry preset (`IndustryConfig`). [APPLIES RULES: {architecture-review}]
```

### Template B: Discovery Validation Log
```markdown
- [ ] 1.0 **Client Alignment Review**
  - [ ] 1.1 **Summarize objectives & KPIs:** Cross-check with stakeholders and update tracking sheet. [APPLIES RULES: {client-communication,code-review}]
  - [ ] 1.2 **Confirm scope exclusions:** Document out-of-scope items with rationale and impact. [APPLIES RULES: {governance-audit}]
  - [ ] 1.3 **Capture approval evidence:** Store meeting notes or email confirmation in `evidence/discovery`. [APPLIES RULES: {quality-audit}]
```

---

## FINAL OUTPUT TEMPLATE

```markdown
# Client Discovery Brief: {ClientName}

Based on Input: `{SourceDocument}`

> **Engagement Tier:** {Tier}
> **Regulatory Alignment:** {Regime}
> **Primary KPIs:** {KPIs}

## Stakeholder Landscape

### Contacts
- **Sponsor:** {Name} — {Role} ({Channel})
- **Technical Lead:** {Name} — {Role} ({Channel})
- **Security Officer:** {Name} — {Role} ({Channel})

## Opportunity Summary

- **Problem Statement:** {Description}
- **Desired Outcomes:** {Outcomes}
- **Constraints:** {Constraints}

## Scope & Governance

- [ ] 1.0 **Business Objectives Confirmed** [COMPLEXITY: Simple]
> **WHY:** Provides baseline for PRD planning.
> **Timeline:** {Date}
- [ ] 2.0 **Compliance Baseline Recorded** [COMPLEXITY: Complex]
> **WHY:** Determines security & data requirements.
> **Timeline:** {Date}
- [ ] 3.0 **Stakeholder Sign-Off Logged** [COMPLEXITY: Simple] [DEPENDS ON: 1.0]
> **WHY:** Unlocks PRD drafting.
> **Timeline:** {Date}

## Next Steps

1. **Activate PRD Protocol:** @apply .cursor/dev-workflow/1-client-prd.md
2. **Share discovery brief with client:** Request written approval.
3. **Initialize evidence folder:** `/load scripts/run_workflow.py --config workflow/gate_controller.yaml`
4. **Schedule PRD workshop:** Invite stakeholders and confirm agenda.
```

