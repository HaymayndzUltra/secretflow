# SecretFlow Client Workflow Infrastructure Analysis

## Overview

This document captures the reusable building blocks inside the SecretFlow repository that can power a client-focused workflow system and highlights the gaps that the upcoming client protocols must close. The analysis covers automation scripts, project generation assets, workflow templates, quality review infrastructure, CI/CD pipelines, and extended governance playbooks.

## Directory Insights

### `scripts`
- **Workflow automation orchestration** – `run_workflow.py` provides a CLI wrapper around the workflow orchestration engine, wiring configuration loading, logging, and gate failure handling for automated runs.【F:scripts/run_workflow.py†L1-L73】
- **Client project generation** – `generate_client_project.py` exposes an opinionated CLI that assembles industry-compliant starter projects with configurable stacks, compliance packs, and `.cursor` assets, making it a ready-made bootstrap path for client engagements.【F:scripts/generate_client_project.py†L1-L170】

### `project_generator`
- **Generator core** – The `ProjectGenerator` class drives project scaffolding, DevEx asset creation, CI workflows, compliance rules, and AI Governor assets, ensuring client projects start with governance baked in.【F:project_generator/core/generator.py†L1-L117】
- **Industry guardrails** – `IndustryConfig` codifies vertical-specific defaults, required features, compliance regimes, and security expectations (HIPAA, SOC2, PCI, etc.), enabling sector-aware workflow tailoring.【F:project_generator/core/industry_config.py†L1-L198】

### `workflow/templates`
- **Evidence-driven workflow blueprints** – Templates such as `workflow_fullstack.yaml` describe gate controllers, evidence folders, compliance matrices, and readiness checklists that can be reused for client delivery governance.【F:workflow/templates/workflow_fullstack.yaml†L1-L41】

### `.github`
- **CI/CD quality enforcement** – Reusable workflows (e.g., `ci-test.yml`) set up language runtimes, install dependencies, execute the unified `make test`, and publish coverage artifacts, demonstrating how client workflows can hook into automated verification.【F:.github/workflows/ci-test.yml†L1-L53】

### `.cursor/dev-workflow` and `review-protocols`
- **Protocol library & orchestrator** – Existing development protocols and the unified review orchestrator offer phased tasking, command syntax (`@apply`, `/review`), router-based protocol selection, and master rule alignment that the client workflows must adopt for consistency.【F:.cursor/dev-workflow/1-create-prd.md†L1-L152】【F:.cursor/dev-workflow/review-protocols/README.md†L1-L160】

### `workflow1`
- **Extended engagement governance** – The `PROJECT_EXECUTION_TEMPLATE.md` lays out Phase 0–6 checklists, evidence expectations, and automation hooks that inform client delivery cadence and reporting checkpoints.【F:workflow1/PROJECT_EXECUTION_TEMPLATE.md†L1-L53】

## Reusable Assets for Client Workflows

- **Automation backbone** – Leverage `run_workflow.py` and related scripts to execute client gates, collect evidence, and generate compliance artifacts on demand.【F:scripts/run_workflow.py†L1-L73】
- **Client-ready scaffolds** – Use `generate_client_project.py` plus `ProjectGenerator` to spin up sector-aligned repos with the correct AI Governor assets, reducing onboarding time.【F:scripts/generate_client_project.py†L1-L170】【F:project_generator/core/generator.py†L1-L117】
- **Compliance & quality frameworks** – Adopt workflow templates and review protocols to enforce evidence capture, compliance matrices, and review automation within the client lifecycle.【F:workflow/templates/workflow_fullstack.yaml†L1-L41】【F:.cursor/dev-workflow/review-protocols/README.md†L1-L160】
- **Governance cadence** – Mirror the phase-driven structure from `workflow1` to maintain consistent reporting, sign-offs, and retrospective practices for client engagements.【F:workflow1/PROJECT_EXECUTION_TEMPLATE.md†L1-L53】

## Identified Gaps & Required Enhancements

1. **Client communication checkpoints** – Existing protocols focus on internal engineering steps; new workflows must insert explicit client briefing, approval, and progress update moments.
2. **Contracted deliverable tracking** – Need artifacts that trace scope, change requests, and acceptance criteria tied to client agreements.
3. **Client-facing evidence packaging** – Current evidence structures are engineering-centric; client workflows require presentation-ready reports and sign-off logs.
4. **Resource and billing awareness** – Task planning should surface effort estimates, staffing roles, and potential budget implications.
5. **Post-engagement relationship management** – Add loops for feedback collection, testimonial gathering, and upsell opportunities beyond the existing retrospectives.

## Integration Map for Client Workflow System

| Client Workflow Phase | Reused Infrastructure | Planned Extension |
| --- | --- | --- |
| Discovery & Scoping | Use `IndustryConfig` presets and project generator prompts to contextualize sector needs.【F:project_generator/core/industry_config.py†L1-L198】 | Add client interview scripts, stakeholder mapping, and qualification checkpoints. |
| PRD & Planning | Align with Protocol 1 structure and workflow templates for architecture mapping.【F:.cursor/dev-workflow/1-create-prd.md†L1-L152】【F:workflow/templates/workflow_fullstack.yaml†L1-L41】 | Introduce client approval gates, budget/resource summaries, and change control logs. |
| Task Generation | Reuse automation scripts (`plan_from_brief`, `enrich_tasks`) and review router commands.【F:scripts/generate_client_project.py†L1-L170】【F:.cursor/dev-workflow/review-protocols/README.md†L1-L160】 | Layer on client-prioritized scoring, dependencies, and communication cadence. |
| Execution & Quality | Apply `run_workflow.py` plus quality orchestrator for audits.【F:scripts/run_workflow.py†L1-L73】【F:.cursor/dev-workflow/review-protocols/README.md†L1-L160】 | Embed status reporting templates and acceptance test sign-offs. |
| Delivery & Retrospective | Follow `workflow1` operational phases for evidence and governance.【F:workflow1/PROJECT_EXECUTION_TEMPLATE.md†L1-L53】 | Add client satisfaction surveys, renewal planning, and lessons learned packaging. |

## Next Actions

1. Draft client-specific workflow protocols (`0`–`5`) mirroring existing format conventions while injecting client communication controls.
2. Wire each protocol to the review orchestrator and automation scripts identified above for seamless adoption.
3. Produce integration and usage documentation demonstrating how client teams invoke the new workflows alongside existing tools.

