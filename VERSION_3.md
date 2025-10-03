The AI Governor Framework turns the repository into an in-repo knowledge base of governance rules and architectural READMEs so assistants can follow project-specific standards without external infrastructure.

Development is organized around a five-protocol workflow (bootstrap, PRD, planning, implementation with integrated reviews, and retrospectives) that keeps the AI responsible for execution while reserving key approvals for the operator.

A unified quality review orchestrator (4-quality-audit.md) routes mode-specific audits, auto-selects stack-aware protocols, and exposes /review or @review entry points across tools, supported by context analyzers and rule-filtering utilities for targeted checks.

Governance rules follow a three-layer hierarchy (foundation, execution, specialization) to encode architectural decisions, best practices, and project constraints in machine-readable form for safe AI autonomy.

Workflow templates describe reusable evidence gates, compliance matrices, and submission checklists, while the Workflow1 playbook packages phase-specific protocols, templates, scripts, and manifests spanning bootstrap through operations.

Template packs supply opinionated frontend, backend, database, DevEx, CI/CD, and policy scaffolds for the generator, while enforcing a no-dependency-install constraint inside the template source.

The project_generator package parses briefs, validates stack/compliance combinations, and assembles complete codebases using the template registry, industry presets, and optional post-processing hooks.

A rich scripts catalog prioritizes automation for planning, generation, gating, evidence collection, and deployment, enabling end-to-end orchestration and evidentiary logging for audits.

End-to-End AI-Driven Development Approach
In-Repo Governance & Context Bootstrapping – Use the bootstrap protocol to let the AI synthesize project rules and context kits from the repo’s rule hierarchy and workflows, ensuring assistants enter with project-aware guidance.

Managed Lifecycle Protocols – Drive each SDLC stage through the dev-workflow protocols, keeping the AI in charge of PRD generation, planning, task execution, and quality audits while you approve outputs at each gate.

Automated Quality Controls – Invoke the unified review orchestrator and utilities to enforce code, security, architecture, UX, and compliance audits with intelligent fallback and context-aware targeting before human sign-off.

Scaffold-to-Delivery Automation – Leverage project generator templates, workflow evidence schemas, and scripts to transform briefs into production-ready repositories, populate evidence manifests, and package client deliverables with minimal manual effort.

Template & Policy Governance – Maintain standardized, dependency-free template packs and policy DSL assets so generated projects inherit compliant infrastructure, ready for automated gate checks and operator validation.

Phase-by-Phase Execution Plan (AI-Run with Human Validation)
Phase	Objective	AI Actions & Tooling	Expected Artifacts	Human Validation
0. Bootstrap	Transform the generic assistant into a project-aware expert by generating context kits and rules.	Run dev-workflow/0-bootstrap-your-project.md; analyze repo to compile project rules and context summaries; sync findings into .cursor assets.	Updated .cursor/rules/project-rules, context kit docs, initial evidence manifest entries.	Confirm rules capture architectural constraints and no sensitive omissions; approve context kit before proceeding.
1. Define (PRD)	Capture product scope and requirements via AI-led interviews producing a PRD.	Apply dev-workflow/1-create-prd.md; AI drafts PRD, links to briefs, and logs outputs into Workflow1 phase 1 structures.	PRD markdown, requirement summaries, evidence manifest updates.	Validate PRD completeness, requirement accuracy, and stakeholder alignment before sign-off.
2. Plan & Design	Convert PRD into actionable plans, architecture packs, and task boards.	Use plan_from_brief.py, dev-workflow/2-generate-tasks.md, and phase 2 scripts to create PLAN.md, tasks.json, architecture artifacts, and contract assets while updating manifests.	PLAN.md, tasks.json, architecture pack, contract/API docs, manifest/log updates.	Check plan-task coherence, architectural decisions, and compliance mapping before approval.
3. Quality Rails Execution	Implement tasks with integrated quality gates and produce QA evidence.	For each parent task, run dev-workflow/3-process-tasks.md; generate code via template packs; execute @review orchestrator; log QA artifacts with phase 3 scripts and manifests.	Updated codebase, quality audit reports, security/accessibility checklists, run logs, manifests.	Ensure code meets standards, audits have no blocking issues, and evidence aligns with gating thresholds prior to continuing.
4. Integration Readiness	Prepare deployment pathways with observability, SLOs, and staging validation.	Generate observability packs and run staging smoke tests using phase 4 scripts; ensure workflow templates capture evidence structure.	Observability specs, SLO/SLI docs, staging smoke results, manifest/log updates.	Review integration evidence for completeness and staging results for acceptable risk before launch prep.
5. Launch Enablement	Finalize deployment runbooks, DR rehearsals, and release documentation.	Execute phase 5 scripts (rollback rehearsal, DR verification), compile release notes, and package submission checklist via workflow templates.	Deployment/rollback runbooks, DR validation logs, submission pack drafts, manifest updates.	Validate that launch runbooks are executable, DR rehearsals succeed, and submission checklist items are satisfied.
6. Operations & Continuous Compliance	Maintain post-launch health with monitoring, retros, and compliance updates.	Run SLO monitoring and retro scheduling scripts; log dependency/security updates; maintain evidence manifests per schema.	SLO reports, retro schedules, dependency logs, updated manifests & validation notes.	Review operational metrics, ensure incident responses meet thresholds, and authorize continued automation cycles.
This plan empowers AI to execute each SDLC phase autonomously using the repository’s governance assets while inserting explicit human validation gates aligned with the framework’s workflows, evidence schemas, and automation tooling.