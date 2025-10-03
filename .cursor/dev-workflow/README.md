# Upwork-Aligned AI Development Workflow Protocols

## Overview

The SecretFlow AI Governor framework now provides a six-protocol workflow optimized for Upwork project briefs and autonomous ex
ecution. Each protocol adheres to the standardized AI Protocol System format—persona-driven roles, strict directive hierarchy,
 three-phase algorithms, reusable templates, and structured outputs. Outputs cascade seamlessly: every protocol’s deliverables
are the next protocol’s required inputs, enabling end-to-end delivery with minimal human intervention while preserving mandator
y validation checkpoints.

## Lifecycle Summary

| Protocol | Focus | Primary Output | Feeds Into |
|----------|-------|----------------|------------|
| **0** | Upwork Project Bootstrap & Context Engineering | `context/context-kit.md`, `handoff/protocol-1-input.md` | Protocol 1 |
| **1** | Upwork Implementation-Ready PRD Creation | `deliverables/prd/{project}-v1.md`, `handoff/protocol-2-input.md` | Protocol 2 |
| **2** | Upwork Technical Task Generation | `deliverables/tasks/{project}-tasks.md`, `handoff/protocol-3-input.md` | Protocol 3 |
| **3** | Upwork Controlled Task Execution | `deliverables/execution/{project}-implementation.md`, `handoff/protocol-4-input.md` | Protocol 4 |
| **4** | Upwork Quality Audit Orchestration | `deliverables/audit/{project}-quality-report.md`, `handoff/protocol-5-input.md` | Protocol 5 |
| **5** | Upwork Implementation Retrospective | `deliverables/retrospective/{project}-retro.md`, governance update tickets | Future cycles |

### Shared Resources

- **Automation Scripts:** `scripts/plan_from_brief.py`, `scripts/lifecycle_tasks.py`, `scripts/doctor.py`, `scripts/evidence_report.py`.
- **Quality Gates:** `gates_config.yaml`, `.cursor/dev-workflow/review-protocols/` templates.
- **Evidence Schema:** `workflow/templates/evidence_schema.json` ensures audit compatibility across protocols.
- **Handoff Directory:** `handoff/` hosts the structured packets that transition between phases.

## Protocol Highlights

### Protocol 0 – Context Engineering
- Persona: Project Context Orchestrator.
- Automates brief ingestion, repository inventory, and context kit publication.
- Establishes shared scripts, review assets, and evidence expectations consumed downstream.

### Protocol 1 – PRD Creation
- Persona: Upwork Product Requirements Strategist.
- Converts context kit insights into a layered PRD with acceptance criteria and architecture matrix.
- Introduces the first validation halt for architecture sign-off.

### Protocol 2 – Task Generation
- Persona: Upwork Technical Planning Lead.
- Produces dependency-aware task registers using automation scripts and governance rules.
- Embeds review hooks and tests at the planning stage to reduce downstream rework.

### Protocol 3 – Task Execution
- Persona: Upwork Delivery Engineer.
- Executes tasks with enforced review protocols, evidence logging, and blocker escalation.
- Generates implementation logs that anchor the unified quality audit.

### Protocol 4 – Quality Audit
- Persona: Upwork Senior Quality Auditor.
- Runs unified and specialized review protocols, logs findings, and compiles audit certification.
- Validates readiness for client delivery and feeds lessons into Protocol 5.

### Protocol 5 – Retrospective
- Persona: Upwork Process Improvement Lead.
- Synthesizes audit and execution data into actionable improvements and governance updates.
- Ensures context assets remain current for future engagements.

## Execution Guidance

1. Start by loading `0-bootstrap-your-project.md` with an approved Upwork brief.
2. Follow each protocol in numeric order; do not skip validation checkpoints.
3. Use the included templates to maintain audit trails and align with SecretFlow automation.
4. Before moving to the next protocol, confirm the required handoff file exists in the `handoff/` directory.

By respecting this structure, autonomous agents can deliver Upwork engagements end-to-end with traceable quality, consistent docu
mentation, and streamlined human oversight.

