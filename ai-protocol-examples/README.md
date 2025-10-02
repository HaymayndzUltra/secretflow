# AI Protocol System Format Reference Guide

## Overview

The SecretFlow AI Governor ecosystem relies on structured "AI Protocols" to coordinate autonomous agents. Each protocol follow
s a predictable blueprint so tooling, review systems, and automation scripts can reason about agent responsibilities and valida
tion checkpoints.

This guide documents the canonical structure extracted from `Reviewme.md` and the existing `.cursor/dev-workflow` assets so yo
u can author new protocols that interoperate with SecretFlow's governance, compliance, and quality automation.

## Core Sections

Every protocol must contain the following top-level sections in the order shown:

1.  `# PROTOCOL X: <NAME>` – Unique identifier and title.
2.  `## AI ROLE` – Persona, mission, and explicit output expectations (e.g., "Your output should be a task checklist, not pros
e").
3.  `## INPUT` – Bullet list describing required files, context, or approvals.
4.  Horizontal rule `---` to separate meta-data from execution guidance.
5.  `## <NAME> ALGORITHM` – Ordered phases with numbered steps.
6.  `## <NAME> TEMPLATES` – Canonical checklists and command invocations using `@apply`, `/load`, or similar patterns.
7.  `## FINAL OUTPUT TEMPLATE` – Markdown skeleton for the agent's deliverable.

## Phase and Step Structure

- Algorithms are subdivided into **three phases** (`PHASE 1`, `PHASE 2`, `PHASE 3`). Each phase lists numbered steps (`1.`, `2
.`, etc.).
- Criticality tags use bracketed directives embedded in bold step titles:
  - **`[CRITICAL]`** – Highest priority. Never skip.
  - **`[MUST]`** – Mandatory compliance before continuing.
  - **`[STRICT]`** – Strict constraints, often tied to rules or audit requirements.
  - **`[GUIDELINE]`** – Best practices; follow unless a conflict is explicitly approved.
- Sub-steps are labeled with decimal notation (`1.1`, `1.2`) and clarify actions, commands, or data requirements.

## Command & Tooling Conventions

- Use `@apply` to invoke protocol or rule templates (e.g., `@apply .cursor/dev-workflow/review-protocols/code-review.md --mode
 security`).
- Use `/load` to pull prerequisite artifacts or checklists before executing tasks.
- Reference review protocols through `[APPLIES RULES: {rule-name}]` annotations inside checklist templates to embed audit trace
ability.
- Align evidence capture with `workflow/templates/evidence_schema.json` by specifying required artefact names (`status-update.
md`, `demo-recording.mp4`, etc.).

## Evidence & Validation Requirements

- Phases typically end with checkpoints where agents must halt for validation or gather client approvals.
- Templates should explicitly identify outputs (files, reports, demos) and specify validation owners (e.g., "Client sponsor sig
ns off on milestone report").
- When referencing quality audits, link to review protocols (architecture, security, accessibility) to ensure automated gate c
overage.

## Output Formatting Rules

- Final output templates must be Markdown documents with numbered tasks, dependencies, WHY/TIMELINE metadata, and sections for
 upcoming actions.
- Titles and headings should remain consistent to support downstream parsing by automation scripts.
- Checklists use GitHub task list syntax (`- [ ]`) and incorporate complexity, dependencies, and review references.

## Extension Workflow

1.  Draft new protocol content following the blueprint above.
2.  Validate alignment with client or project requirements.
3.  Cross-reference applicable review protocols using `[APPLIES RULES: ...]` tags.
4.  Run `scripts/validate_workflows.py` to ensure structural compliance before committing.
5.  Document integration points (automation commands, evidence directories) in the protocol's templates or notes section.

By adhering to this reference, newly authored AI Protocols will remain interoperable with SecretFlow's governance framework, en
suring consistent quality, traceability, and automation compatibility across engagements.

