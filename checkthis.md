**`[REPORT1]`**
# SecretFlow Client Discovery & Framework Alignment Assessment

## Executive Summary
- The client intake trigger (`docs/brief/jobpost.md`) is empty, so the discovery workflow has no canonical place to capture proposal responses, stakeholder data, or scope assumptions, leaving builders without the inputs required by Protocol 0 and the meta-framework.【56e5ee†L1-L2】【F:.cursor/commands/0-bootstrap-your-project.md†L8-L66】【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L19-L105】
- Meta-Framework Generator and Execution rulebooks share identical phase structure, personas, outputs, validation artifacts, and version/hash metadata, satisfying the strict alignment contract defined in `AGENTS.md` and forming a consistent lifecycle spine.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L4-L198】【F:.cursor/rules/Codex-Meta.mdc†L4-L200】【F:AGENTS.md†L1-L41】
- The operational Protocol commands (0–5) map cleanly onto the meta phases 0–6, providing actionable guidance once discovery inputs exist, but they lack hooks back into intake artifacts and generated schemas promised by the meta-framework.【F:.cursor/commands/0-bootstrap-your-project.md†L13-L80】【F:.cursor/commands/1-create-prd.md†L10-L102】【F:.cursor/commands/5-implementation-retrospective.md†L14-L103】【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L27-L86】
- Workflow assets concentrate on phases 2–6, while workflow indexes still reference "legacy" evidence folders for phases 0–1; without updated templates, developers cannot produce the required discovery evidence or validation logs.【F:workflow1/INDEX.md†L5-L21】
- Quality governance is under-specified: the repo-level `gates_config.yaml` covers lint, security, and coverage only, leaving out the static, dynamic, policy, and ADR gate families required by the rulebooks and hindering automated enforcement.【F:gates_config.yaml†L1-L16】【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L139-L170】【F:.cursor/rules/Codex-Meta.mdc†L401-L424】

## Comparison Matrix (Phase Alignment Snapshot)
| Lifecycle Element | Meta-Framework Generator | Meta Execution Rulebook | Command Protocols | Observations |
| --- | --- | --- | --- | --- |
| Phase 0 | Bootstrap persona, context kit, stakeholder map, tech inventory, validation logs, Builder→Auditor→Challenger loop.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L90-L105】 | Same persona, outputs, and validation artifacts with ✅/❌ examples.【F:.cursor/rules/Codex-Meta.mdc†L24-L88】 | Protocol 0 demands identical outputs but cannot start without populated job post/context kit inputs.【F:.cursor/commands/0-bootstrap-your-project.md†L13-L80】 | Structural alignment is strong; intake artifact missing. |
| Phase 1 | PRD persona with business logic, user journeys, acceptance criteria, validation logs.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L106-L120】 | Mirrors outputs, personas, validation evidence, examples.【F:.cursor/rules/Codex-Meta.mdc†L90-L154】 | Protocol 1 prescribes discovery interviews, PRD template, quality gates.【F:.cursor/commands/1-create-prd.md†L10-L119】 | Requires upstream discovery data to populate sections. |
| Phase 2 | Design persona, architecture pack, ADR catalog, validation schema promises.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L122-L137】 | Execution persona and outputs match.【F:.cursor/rules/Codex-Meta.mdc†L156-L221】 | Workflow1 templates and scripts focus heavily here.【F:workflow1/INDEX.md†L9-L10】 | Well-supported once intake complete. |
| Phases 3–6 | Quality rails through operations align across generator and execution with matching evidence paths and examples.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L138-L198】【F:.cursor/rules/Codex-Meta.mdc†L223-L400】 | Protocols 2–5 provide operational guidance for later phases.【F:.cursor/commands/2-generate-tasks.md†L12-L92】【F:.cursor/commands/3-process-tasks.md†L10-L97】【F:.cursor/commands/4-quality-control-protocol.md†L12-L101】【F:.cursor/commands/5-implementation-retrospective.md†L14-L103】 | Late-phase automation rich; early-phase capture absent. |

## Gap Analysis
### Client Discovery & Intake
1. **Missing Intake Artifact** – `docs/brief/jobpost.md` is blank, so there is no structured intake form for proposal responses, stakeholder lists, constraints, or success metrics, violating generator input expectations and Protocol 0 prerequisites.【56e5ee†L1-L2】【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L19-L25】【F:.cursor/commands/0-bootstrap-your-project.md†L8-L37】
2. **No Conversion from Intake to Brief** – No automation links job post data into the brief parser or scaffolding scripts; developers must manually synthesize inputs before `plan_from_brief.py` or generator workflows can run.【F:project_generator/core/brief_parser.py†L21-L115】【F:scripts/plan_from_brief.py†L4-L53】
3. **Lack of Discovery Evidence Templates** – Workflow indexes mark phases 0–1 as "legacy" with no updated templates or validation manifests, preventing capture of context kit, stakeholder maps, or interview logs mandated by the meta-framework.【F:workflow1/INDEX.md†L5-L21】【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L90-L120】
4. **Validation Loop Orchestration Missing** – There are no builder/auditor/challenger intake playbooks or automation for the discovery phases, so the required validation transcripts under `/var/validation/phase-0` and `phase-1` cannot be produced consistently.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L64-L71】【F:.cursor/rules/Codex-Meta.mdc†L37-L114】

### Framework & Command Alignment
1. **Schema & Phase Map Outputs Not Instantiated** – Generator promises `/docs/plans/<project-id>/phase-map.md` and `/var/schemas/...` assets, but no scripts or commands generate or consume them, breaking the implied automation chain.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L27-L86】【F:.cursor/rules/Codex-Meta.mdc†L389-L404】
2. **Quality Gate Coverage** – Quality gate configuration omits dynamic, policy, and ADR categories, so even aligned documentation cannot be enforced programmatically.【F:gates_config.yaml†L1-L16】【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L138-L170】【F:.cursor/rules/Codex-Meta.mdc†L401-L424】
3. **Command Protocol Outputs Unlinked to Evidence Schema** – Commands describe expected outputs but provide no references to evidence manifests or schema validation, leaving developers to improvise and risking divergence.【F:.cursor/commands/0-bootstrap-your-project.md†L13-L80】【F:.cursor/commands/1-create-prd.md†L13-L119】【F:workflow/templates/evidence_schema.json†L1-L20】

## Implementation Plan (Client Intake Overhaul)
1. **Design Job Post Schema & Template**
   - Create `docs/brief/jobpost.md` form capturing stakeholder roster, business goals, constraints, compliance, tech stack hints, budget/timeline, and acceptance signals aligned with Protocol 0 inputs.【F:.cursor/commands/0-bootstrap-your-project.md†L8-L63】
   - Define JSON schema under `docs/brief/jobpost.schema.json` to validate submissions and feed automation.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L75-L83】
2. **Automate Intake → Brief Conversion**
   - Extend `scripts/scaffold_briefs.py` (or create `scripts/intake_to_brief.py`) to parse `jobpost.md`, generate `docs/brief/brief.md`, and seed Context Kit stubs, ensuring compatibility with `BriefParser` and downstream scripts.【F:scripts/scaffold_briefs.py†L1-L39】【F:project_generator/core/brief_parser.py†L21-L115】
   - Update Protocol 0 to reference the automation command and require validated schema output before proceeding.【F:.cursor/commands/0-bootstrap-your-project.md†L67-L79】
3. **Add Discovery Evidence Templates**
   - Introduce `workflow/templates/context-kit.md`, `stakeholder-map.md`, and interview log templates, plus `var/validation/phase-0/README.md` instructions for builder/auditor/challenger sessions.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L90-L105】
   - Mirror for Phase 1 with PRD interview notes, decision tables, and validation transcripts.【F:.cursor/rules/Codex-Meta.mdc†L90-L154】
4. **Generate Phase Map & Schemas**
   - Implement script (e.g., `scripts/generate_phase_map.py`) to emit `/docs/plans/<project-id>/phase-map.md` and `/var/schemas/<project-id>/phase-contracts/*.schema.json`, invoked after intake conversion.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L27-L86】
   - Update command protocols to reference these artifacts, enabling tight coupling between generator outputs and execution steps.【F:.cursor/commands/1-create-prd.md†L100-L119】
5. **Quality Gate Expansion**
   - Expand `gates_config.yaml` to include static (lint/format/type/license), dynamic (unit/integration/perf/a11y), policy (security/compliance), and ADR gates with thresholds; integrate into `scripts/enforce_gates.py` for automatic enforcement.【F:gates_config.yaml†L1-L16】【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L138-L170】
6. **Developer Experience Enhancements**
   - Provide a `docs/brief/README.md` explaining intake workflow, automation commands, and validation expectations.【F:workflow/templates/submission_checklist.md†L1-L12】
   - Add `make` targets or `scripts/run_workflow.py --phase 0` extensions to execute intake validation end-to-end.【F:scripts/run_workflow.py†L1-L30】

## Codex Intake Protocol (Executable Steps)
1. **Capture Job Post** – Populate `docs/brief/jobpost.md` using the structured template; run `scripts/validate_intake.py` to lint schema compliance and ensure all mandatory sections complete.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L19-L83】
2. **Convert to Brief & Context Kit** – Execute `python scripts/intake_to_brief.py --jobpost docs/brief/jobpost.md --out docs/brief/brief.md` to generate the brief, Context Kit, and phase map scaffolds.【F:scripts/plan_from_brief.py†L24-L48】
3. **Initiate Validation Loop** – Trigger `python scripts/run_workflow.py --phase 0 --mode builder` followed by auditor/challenger modes, automatically writing transcripts to `var/validation/phase-0/` and updating evidence manifests.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L64-L71】【F:workflow/templates/evidence_schema.json†L1-L20】
4. **Promote to PRD Discovery** – Once convergence PASS recorded, run `python scripts/run_workflow.py --phase 1 --mode builder` to drive stakeholder interviews using the generated context, capturing outputs in `evidence/phase1/` and transcripts under `var/validation/phase-1/` before moving to Protocol 2.【F:.cursor/rules/Codex-Meta.mdc†L90-L154】

## Validation Framework
- **Success Criteria**
  - Intake schema validation passes with no missing required fields (automation exit code 0).【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L75-L83】
  - Context Kit, stakeholder map, and PRD discovery artifacts exist and match required filenames before Protocol 1 begins.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L90-L120】【F:.cursor/commands/1-create-prd.md†L13-L119】
  - Builder/Auditor/Challenger transcripts exist for phases 0–1 with convergence PASS recorded prior to phase promotion.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L64-L71】【F:.cursor/rules/Codex-Meta.mdc†L37-L114】
  - `gates_config.yaml` includes all four gate categories, and CI tooling enforces them via `scripts/enforce_gates.py` or equivalent automation.【F:gates_config.yaml†L1-L16】【F:.cursor/rules/Codex-Meta.mdc†L401-L424】
- **Checkpoints & Tests**
  1. Run `python scripts/validate_intake.py` (new) to ensure job post compliance.
  2. Run `python scripts/intake_to_brief.py` to confirm conversion completes and outputs expected artifacts.
  3. Execute `python scripts/enforce_gates.py --phases 0,1` to validate expanded gate coverage.
  4. Add CI step to verify presence and freshness of `/docs/plans/<project-id>/phase-map.md` and `/var/schemas/<project-id>/phase-contracts/*.schema.json` after intake automation.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L27-L86】

## Recommendations Summary
- Implement the structured intake template and automation to close the gap between client proposal responses and executable briefs, ensuring Protocol 0 can start with validated data.
- Align workflow assets for phases 0–1 with the meta-framework by delivering templates, manifests, and validation scripts that mirror later phase maturity.
- Expand quality gates and integrate schema outputs to create a frictionless developer experience where Codex agents can execute the intake, validation, and planning pipeline without manual stitching.

---

**`[REPORT2]`**
# SecretFlow Client Discovery & Meta-Framework Alignment Report

## Executive Summary
- The Codex generator and execution rulebooks are structurally aligned: they share the same Phase 0–6 lifecycle, personas, evidence paths, validation artifacts, and `codexAlignmentVersion`/`Hash` metadata, satisfying the invariant requirements from the root alignment policy.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L1-L203】【F:.cursor/rules/Codex-Meta.mdc†L1-L509】【F:AGENTS.md†L5-L38】
- Client discovery is non-operational: `docs/brief/jobpost.md` is empty, and there is no automation to transform a client response into the metadata/brief assets required by intake gates and planning scripts, leaving the discovery pipeline disconnected from downstream tooling.【3d2364†L1-L3】【F:scripts/workflow_automation/gates/implementations.py†L23-L71】【F:scripts/pre_lifecycle_plan.py†L862-L931】
- Developers face friction when moving from discovery to execution: workflow assets reference “legacy evidence folders,” the intake gate expects `metadata.json`, and validation logs are empty, so there is no authoritative path from initial client inputs to the Phase 0–1 evidence required by the Codex lifecycle.【F:workflow1/INDEX.md†L5-L26】【F:workflow1/evidence/phase2/validation.md†L1-L5】【F:workflow/templates/workflow_fullstack.yaml†L1-L33】
- Quality gate coverage remains partial: repository policy only enforces linting, security, and coverage thresholds, leaving performance, accessibility, policy, and ADR controls mandated by the meta-framework unenforced and undocumented for discovery outputs.【F:gates_config.yaml†L1-L16】【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L146-L170】【F:.cursor/rules/Codex-Meta.mdc†L360-L510】

## Validation Result — **Aligned**
The generator (`Codex-Meta-Framework-Genarator.mdc`), execution rulebook (`Codex-Meta.mdc`), and operational command protocols (`.cursor/commands/*.md`) align on structure, logic, and roles:

| Aspect | Generator Reference | Execution Reference | Command Mapping |
| --- | --- | --- | --- |
| Lifecycle Phases | Canonical Phase 0–6 set with personas, outputs, success criteria.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L86-L203】 | Mirrors Phase 0–6 personas, outputs, validation artifacts, and success criteria.【F:.cursor/rules/Codex-Meta.mdc†L22-L509】 | Protocols 0–5 orchestrate the same lifecycle stages for builders, ensuring upstream discovery, PRD, planning, task execution, QC, and retrospectives follow the Codex flow.【F:.cursor/commands/0-bootstrap-your-project.md†L1-L115】【F:.cursor/commands/1-create-prd.md†L1-L120】【F:.cursor/commands/2-generate-tasks.md†L1-L115】【F:.cursor/commands/3-process-tasks.md†L1-L120】【F:.cursor/commands/4-quality-control-protocol.md†L1-L120】【F:.cursor/commands/5-implementation-retrospective.md†L1-L120】 |
| Personas & Session Order | Builder/Auditor/Challenger loop with convergence artifacts mandated per phase.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L47-L83】 | Provides system instructions and validation outputs for Builder, Auditor, and Challenger roles plus convergence logs per phase.【F:.cursor/rules/Codex-Meta.mdc†L35-L509】 | Commands call for independent discovery, validation, and audit activities, preserving the persona separation implied by the meta lifecycle.【F:.cursor/commands/1-create-prd.md†L31-L120】【F:.cursor/commands/4-quality-control-protocol.md†L51-L120】 |
| Evidence Paths & Outputs | Defines `evidence/phaseN/*` and `var/validation/phase-N/*` directories as mandatory outputs.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L92-L203】 | Enforces identical evidence artifacts, naming, and validation logs for each persona.【F:.cursor/rules/Codex-Meta.mdc†L35-L509】 | Commands reference the same artifacts (Context Kit, PRD, task plan, QA packs), ensuring operational steps feed those paths.【F:.cursor/commands/0-bootstrap-your-project.md†L13-L78】【F:.cursor/commands/1-create-prd.md†L12-L85】【F:.cursor/commands/2-generate-tasks.md†L16-L83】 |
| Quality Gates | Mandates static, dynamic, policy, and ADR categories globally.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L146-L170】 | Integrates the same gate categories into session management and validation expectations.【F:.cursor/rules/Codex-Meta.mdc†L360-L509】 | Protocol 4 details QA/QC activities that map to the gate categories (security, performance, accessibility, ADR updates).【F:.cursor/commands/4-quality-control-protocol.md†L16-L118】 |
| Version & Hash Discipline | Requires synchronized `codexAlignmentVersion` and `codexAlignmentHash`.【F:AGENTS.md†L29-L37】 | Both files include `1.0.0` / `2024-06-05-a`, demonstrating compliance.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L1-L8】【F:.cursor/rules/Codex-Meta.mdc†L1-L8】 | Commands do not override lifecycle metadata, avoiding divergence from generator/execution structure.【F:.cursor/commands/0-bootstrap-your-project.md†L1-L115】 |

## Phase 1: Structural Analysis
### Workflow Inventory & Evolution
| Workflow Version | Location | Status | Strengths | Gaps |
| --- | --- | --- | --- | --- |
| workflow (templates) | `workflow/templates` | Active | Provides baseline YAML and evidence schema references for full-stack/back-end flows, including intake stage expectations.【F:workflow/templates/workflow_fullstack.yaml†L1-L33】 | No concrete discovery automation or scripts; relies on downstream orchestration to supply metadata and briefs. |
| workflow1 | `workflow1/` | Partial | Robust templates and scripts for Phases 2–6 with evidence manifests and automation examples.【F:workflow1/INDEX.md†L12-L39】【F:workflow1/evidence/phase2/manifest.json†L1-L41】 | Phases 0–1 labelled as “legacy evidence folders” without templates; validation logs empty; no tie-in to client intake assets.【F:workflow1/INDEX.md†L8-L17】【F:workflow1/evidence/phase2/validation.md†L1-L5】 |
| workflow2–4 | — | Missing | — | Required by playbook evolution but absent, so there is no documented migration path or delta log. |

### Dependency Mapping
- Intake Gates: Require `metadata.json` and `brief.md`, but no tooling populates these from `docs/brief/jobpost.md`.【F:scripts/workflow_automation/gates/implementations.py†L23-L71】【3d2364†L1-L3】
- Pre-Lifecycle Planning: Expects briefs under `docs/briefs/<client>/brief.md`, not `docs/brief/jobpost.md`, creating a structural disconnect between discovery intake and automation.【F:scripts/pre_lifecycle_plan.py†L862-L931】
- Generator Engine: Parses briefs via `BriefParser`, depending on frontmatter or metadata fields that discovery never collects automatically.【F:project_generator/core/brief_parser.py†L1-L136】

### Command Alignment Observations
- Protocol 0 instructs discovery leads to prepare Context Kit artifacts that map directly to Phase 0 evidence outputs, ensuring generator/execution requirements can be met when data is available.【F:.cursor/commands/0-bootstrap-your-project.md†L13-L78】【F:.cursor/rules/Codex-Meta.mdc†L35-L78】
- Protocol 1’s business discovery mirrors Phase 1 outputs but assumes the existence of a populated brief and stakeholder context, which the current intake pipeline cannot supply automatically.【F:.cursor/commands/1-create-prd.md†L12-L87】【F:.cursor/rules/Codex-Meta.mdc†L86-L140】
- Protocols 2–5 align to later phases but rely on validated upstream artifacts; without intake automation, teams must handcraft bridging assets, increasing onboarding time.【F:.cursor/commands/2-generate-tasks.md†L16-L83】【F:.cursor/commands/3-process-tasks.md†L16-L90】

## Phase 2: Gap Analysis
### Discovery & Intake Gaps
1. **No job post template or metadata capture** – `docs/brief/jobpost.md` is empty and lacks guidance for capturing client goals, stack preferences, or compliance needs, leaving subsequent tools without required inputs.【3d2364†L1-L3】
2. **Missing transformation from job post to brief metadata** – There is no script or workflow that converts the job post into `metadata.json` and `brief.md`, even though intake gates and planning scripts expect those files.【F:scripts/workflow_automation/gates/implementations.py†L23-L71】【F:scripts/pre_lifecycle_plan.py†L862-L931】
3. **Disjoint directory conventions** – Discovery assets live under `docs/brief/`, while planning and generator tooling search `docs/briefs/<client>/`, so client discovery never feeds automation without manual copying.【F:scripts/pre_lifecycle_plan.py†L862-L931】
4. **Stakeholder validation missing** – No process captures stakeholder roles, decision rights, or approvals during intake, yet Phase 0 success criteria require this information.【F:.cursor/rules/Codex-Meta.mdc†L35-L83】

### Workflow & Evidence Gaps
1. **Phase 0–1 evidence scaffolding absent** – Workflow1 references “legacy evidence folders” and lacks templates, manifest schemas, or validation logs for early phases.【F:workflow1/INDEX.md†L8-L26】
2. **Empty validation logs** – Evidence validation files are blank, so auditors lack traceability of PASS/FAIL cycles mandated by the meta-framework.【F:workflow1/evidence/phase2/validation.md†L1-L5】【F:.cursor/rules/Codex-Meta.mdc†L389-L430】
3. **No convergence automation** – There is no script to enforce builder → auditor → challenger loops or to append convergence results, risking violation of session management rules.【F:.cursor/rules/Codex-Meta.mdc†L389-L509】

### Quality Gate & Governance Gaps
1. **Partial gates_config** – Only lint, security scan, and coverage thresholds are defined; performance, accessibility, policy, and ADR gates are missing despite being required.【F:gates_config.yaml†L1-L16】【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L146-L170】
2. **No intake validation** – There is no automated check ensuring the job post collects required fields (industry, stack preferences, compliance), so metadata completeness is not enforced before discovery proceeds.【F:scripts/workflow_automation/gates/implementations.py†L23-L71】

## Phase 3: Implementation Design
### Improved Client Intake Framework
1. **Job Post Template** – Create `docs/brief/jobpost.md` template with:
   - YAML frontmatter capturing `client_name`, `industry`, `project_type`, stack preferences, compliance obligations, timeline, budget, and stakeholder contacts.
   - Guided sections (Problem Statement, Current State, Desired Outcomes, Constraints, Success Metrics) aligned with Protocol 0–1 discovery prompts.
   - Instruction block linking to CLI/script to convert the job post into structured metadata.
2. **Intake Transformer Script** – Implement `scripts/process_jobpost.py` that:
   - Reads `docs/brief/jobpost.md` and emits `docs/briefs/<client>/brief.md` plus `metadata.json`, normalized through `BriefParser` vocab to satisfy generator expectations.【F:project_generator/core/brief_parser.py†L1-L136】
   - Generates placeholder `evidence/phase0/*.md` scaffolds, populating context kit, stakeholder map, and tech inventory using captured metadata.
   - Logs actions and validations to `var/validation/phase-0/builder.md` to seed the session loop.
3. **Stakeholder Intake Checklist** – Add `docs/brief/stakeholder-intake.md` referencing required approvals and decision rights for Phase 0 success criteria.【F:.cursor/rules/Codex-Meta.mdc†L35-L83】
4. **Intake Gate Enhancement** – Update `workflow/gate_controller.yaml` to include an intake gate step that runs `process_jobpost.py`, verifies required metadata fields, and attaches evidence snapshots automatically.【F:scripts/workflow_automation/gates/implementations.py†L23-L71】

### Developer Experience Enhancements
- **Unified Directory Convention** – Standardize on `docs/briefs/<client>/` for all discovery artifacts; adjust scripts to accept a `--source jobpost` flag that copies `docs/brief/jobpost.md` into client-specific folders.【F:scripts/pre_lifecycle_plan.py†L862-L931】
- **Phase 0–1 Evidence Templates** – Add Markdown templates for `context-kit.md`, `stakeholder-map.md`, `tech-inventory.md`, `prd.md`, and `business-logic.md` under `workflow1/evidence/phase0` and `phase1`, with placeholders mapped to job post data.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L92-L140】
- **Validation Log Initializers** – Provide CLI to append baseline entries to `var/validation/phase-N/*.md` after each intake automation step, ensuring builder/auditor/challenger transcripts exist from the outset.【F:.cursor/rules/Codex-Meta.mdc†L389-L509】
- **Quality Gate Expansion** – Extend `gates_config.yaml` with performance, accessibility, policy, and ADR sections plus thresholds; link them to Protocol 4 automation scripts for enforcement.【F:gates_config.yaml†L1-L16】【F:.cursor/commands/4-quality-control-protocol.md†L57-L118】

### Codex Execution Protocol
1. **Discovery Kickoff** – Run `process_jobpost.py --client <name>` to generate structured brief, metadata, and Phase 0 evidence.
2. **Protocol 0 Execution** – Use generated artifacts to complete Context Kit, update `var/validation/phase-0/builder.md`, and trigger intake gate validation.
3. **Protocol 1 Execution** – Populate PRD templates with findings from the job post and stakeholder interviews; run `validate_prd_gate.py` to ensure frontmatter metadata is complete.【F:scripts/validate_prd_gate.py†L24-L91】
4. **Protocol 2+** – Leverage existing workflow1 templates and automation scripts; ensure validation logs capture PASS/FAIL results after each persona session.
5. **Continuous Alignment** – After each protocol, run a new `scripts/check_alignment.py` (to be implemented) that compares generator vs execution outputs and updates `codexAlignmentHash` if structure changes.【F:AGENTS.md†L29-L41】

### Quality Gates & Error Handling
- **Intake Errors** – If metadata fields missing, `process_jobpost.py` should emit actionable errors pointing to sections in `jobpost.md` and append failure context to `var/validation/phase-0/builder.md`.
- **Gate Failures** – Update `IntakeGate` to include remediation guidance (e.g., missing compliance tags) and automatically reopen `jobpost.md` for editing.
- **Schema Validation** – Introduce JSON schema under `var/schemas/alignment/alignment.schema.json` (per guideline) and validate evidence manifests after each automation run.【F:AGENTS.md†L42-L76】

## Phase 4: Validation & Testing
### Success Criteria
1. **Discovery Completeness** – `docs/briefs/<client>/brief.md` contains all required sections with metadata recognized by `BriefParser`, and Phase 0 evidence files are populated with job post data.【F:project_generator/core/brief_parser.py†L1-L136】【F:.cursor/rules/Codex-Meta.mdc†L35-L78】
2. **Gate Compliance** – Intake, environment, planning, and quality gates pass with evidence artifacts stored under `evidence/` per meta-framework requirements.【F:scripts/workflow_automation/gates/implementations.py†L23-L199】【F:.cursor/rules/Codex-Meta.mdc†L35-L509】
3. **Validation Logs** – `var/validation/phase-N/` contains builder, auditor, challenger, and convergence entries for each phase, demonstrating session loop enforcement.【F:.cursor/rules/Codex-Meta.mdc†L389-L509】
4. **Quality Gates Coverage** – Expanded `gates_config.yaml` drives automated checks for static, dynamic, policy, and ADR gates with documented outcomes.【F:gates_config.yaml†L1-L16】【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L146-L170】

### Validation Checkpoints & Tests
- **Unit Tests** – Add tests for `process_jobpost.py` covering parsing of frontmatter, normalization, and error handling when required fields are missing.
- **Integration Tests** – Execute workflow automation end-to-end using a sample job post to confirm evidence scaffolds and validation logs are generated.
- **Schema Validation** – Run JSON schema checks on generated manifests and alignment manifest to ensure structural invariants remain intact.【F:AGENTS.md†L42-L76】
- **Regression Guard** – Add CI job invoking alignment checker to prevent drift between generator and execution rulebooks whenever templates change.【F:AGENTS.md†L29-L41】

### Performance Metrics & Monitoring
- **Intake Cycle Time** – Measure elapsed time from job post creation to passing Intake Gate; target <1 hour with automation.
- **Evidence Completeness Rate** – Percentage of required Phase 0–1 artifacts auto-populated from job post metadata; target ≥90% to minimize manual rework.
- **Gate Pass Rate** – Track success/failure per gate to identify systemic gaps in discovery outputs.

### Troubleshooting Guide
- **Metadata Parse Failures** – Verify YAML frontmatter syntax in `jobpost.md`; run `process_jobpost.py --debug` to display normalized fields.
- **Missing Stakeholder Data** – Use `stakeholder-intake.md` checklist to capture decision rights and rerun intake automation.
- **Validation Log Omissions** – If transcripts remain empty, ensure automation hooks append entries after each persona session; failing that, escalate via Protocol 4 QA gate.

## Recommendations Summary
1. **Implement structured job post intake** with templates, transformer script, and intake gate enhancements to produce all Phase 0 artifacts automatically.
2. **Expand workflow1 for early phases** by adding evidence templates, manifests, and validation log automation aligned with Codex requirements.
3. **Strengthen quality governance** through comprehensive gate configuration, schema validation, and CI enforcement, ensuring discovery outputs meet lifecycle expectations before implementation begins.

---

**`[REPORT3]`**
# SecretFlow Client Discovery & Framework Alignment Assessment

## Executive Summary
- Client discovery lacks a structured intake package. The required `docs/brief/jobpost.md` is empty and there is no canonical metadata checklist, so developers start discovery without capture forms, required fields, or evidence directories.【fc2ec4†L1-L3】【F:workflow1/INDEX.md†L6-L18】
- Workflow automation expects validated `metadata.json` and a populated brief before any gates run, but there is no documented path from a job post to those assets, causing IntakeGate failures and inconsistent evidence output.【F:scripts/workflow_automation/gates/implementations.py†L23-L69】【F:scripts/pre_lifecycle_plan.py†L775-L818】
- Codex Generator, Execution, and Commands are only partially aligned. Phases 0–6 exist in Generator and Execution, yet the commands stop at Protocol 5 and provide no operational persona for Phase 6. Evidence, gate definitions, and schema references also diverge, preventing end-to-end automation.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L86-L140】【F:.cursor/rules/Codex-Meta.mdc†L314-L355】【F:.cursor/commands/5-implementation-retrospective.md†L1-L40】
- Quality gate configuration and workflow templates omit required categories (dynamic, policy, ADR) and reference a missing `workflow/gate_controller.yaml`, leaving the lifecycle without enforceable intake-to-brief validation despite repo automation hooks.【F:gates_config.yaml†L1-L15】【F:workflow/templates/workflow_fullstack.yaml†L1-L34】【91f9bf†L1-L2】

### Recommended Action Themes
1. **Build a complete intake kit** – job post template, discovery interview guide, metadata schema, and automation that converts responses into `metadata.json` and a seed `brief.md`.
2. **Restore phase parity** – extend commands with Phase 6 protocol, align evidence filenames, and publish the gate controller that orchestrates Intake → Environment → Planning.
3. **Automate validation** – generate intake manifests, enforce quality categories, and add convergence logging so Builder → Auditor → Challenger loops produce actionable evidence.

---

## Comparison Matrix — Workflows vs. Target Requirements

| Capability | Target (AGENTS & Meta) | Workflow1 Status | Gap |
| --- | --- | --- | --- |
| Phase Coverage | Phases 0–6 with personas, evidence, validation transcripts【F:.cursor/rules/Codex-Meta.mdc†L22-L355】 | Workflow1 only ships templates for Phases 2–6; Phase 0–1 assets are labeled "legacy" with no evidence structure.【F:workflow1/INDEX.md†L6-L29】【1dc8fe†L1-L11】 | Missing discovery scaffolding and modern evidence directories for phases 0–1. |
| Intake Assets | Job post, stakeholder interviews, metadata capture, brief skeleton | `jobpost.md` empty, no interview scripts, no metadata schema or automation entry point.【fc2ec4†L1-L3】 | Intake cannot reliably produce inputs for Generator/Workflow gates. |
| Gate Orchestration | `workflow/gate_controller.yaml` referencing Intake → Environment → Planning | Template references non-existent controller; orchestrator defaults fail without config.【F:workflow/templates/workflow_fullstack.yaml†L1-L34】【91f9bf†L1-L2】 | Automation cannot run from discovery. |
| Evidence Logging | `evidence/phaseN/{context-kit, validation.md}` + transcripts【F:.cursor/rules/Codex-Meta.mdc†L35-L408】 | Only later phases log evidence; validation tables empty, transcripts absent.【F:workflow1/evidence/phase2/validation.md†L1-L4】【1dc8fe†L1-L11】 | Intake/PRD lacks outputs; even existing phases lack PASS/FAIL history. |
| Automation Hooks | `make plan-from-brief`, metadata normalization, template generation【F:scripts/pre_lifecycle_plan.py†L775-L818】【F:workflow1/codex-phase2-design/protocol.md†L1-L45】 | Hooks start at planning; there is no command to transform job post -> metadata -> brief. | Intake depends on manual work. |
| Quality Gates | Static, dynamic, policy, ADR enforced【F:.cursor/rules/Codex-Meta.mdc†L406-L414】 | Config only defines lint, security, coverage; no dynamic/policy/ADR toggles.【F:gates_config.yaml†L1-L15】 | Non-compliant with framework. |

---

## Gap Analysis — Client Discovery & Intake

### Missing Assets
- **Client-facing job post template** – `docs/brief/jobpost.md` is empty, leaving developers without prompts for target users, value metrics, constraints, or compliance flags.【fc2ec4†L1-L3】
- **Discovery interview scripts** – Commands expect stakeholder interviews, yet no question bank or agenda artifact exists to ensure consistent intake across business, technical, and operational roles.【F:.cursor/commands/1-create-prd.md†L25-L75】
- **Metadata schema & validation** – IntakeGate demands mandatory fields, but no canonical schema or checklist exists. Workflow templates reference a metadata snapshot without defining required keys or data types.【F:scripts/workflow_automation/gates/implementations.py†L23-L69】【F:workflow/templates/workflow_fullstack.yaml†L6-L34】
- **Evidence directories for Phase 0–1** – Workflow1 references "legacy" folders but does not provide modern evidence logs, manifests, or validation transcripts for discovery outputs.【F:workflow1/INDEX.md†L6-L18】【1dc8fe†L1-L11】

### Process Breaks
- **No transition from proposal acceptance to brief** – There is no documented step linking a signed proposal to job post intake, nor automation that converts captured answers into `brief.md` or `metadata.json` consumed by generator scripts.【F:scripts/pre_lifecycle_plan.py†L775-L818】【F:project_generator/core/brief_parser.py†L1-L110】
- **Commands omit environment to job-brief synchronization** – Protocol 0 lists discovery tasks but lacks explicit instructions to produce metadata or run intake gates, resulting in manual, inconsistent outputs.【F:.cursor/commands/0-bootstrap-your-project.md†L1-L74】
- **Quality gates cannot start** – Without the missing `workflow/gate_controller.yaml`, orchestrating IntakeGate fails before developers reach planning, preventing the mandated automated validation loop.【F:workflow/templates/workflow_fullstack.yaml†L1-L10】【91f9bf†L1-L2】

### Insight Gaps
- **Stakeholder mapping** – No artifact ties stakeholder roles to responsibilities or decisions even though Phase 0 success criteria requires it, causing context loss when multiple personas engage.【F:.cursor/rules/Codex-Meta.mdc†L22-L83】
- **Success metrics alignment** – There is no intake step capturing KPIs or measurable outcomes, yet phases downstream depend on these metrics for PRD and quality gates.【F:.cursor/commands/1-create-prd.md†L38-L75】

---

## Framework Alignment Validation

### Current State: **Not aligned**
- Generator and Execution maintain phase parity and shared naming, but Commands end at Protocol 5 and never instantiate Phase 6 (Operations) personas or evidence obligations, breaking the Builder → Auditor → Challenger lifecycle mandated by the Meta files.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L86-L140】【F:.cursor/rules/Codex-Meta.mdc†L314-L355】【F:.cursor/commands/5-implementation-retrospective.md†L1-L40】
- Workflow automation lacks the gate controller and metadata schema promised by the Generator outputs (`/var/schemas/...`, `/docs/plans/...`), so Execution’s success criteria cannot be enforced programmatically.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L25-L83】【F:.cursor/rules/Codex-Meta.mdc†L389-L424】
- Evidence artifacts for discovery phases (Context Kit, Stakeholder Map, Tech Inventory) are not generated or referenced by commands, leaving Execution without actual files to validate.【F:.cursor/rules/Codex-Meta.mdc†L35-L83】【F:workflow1/INDEX.md†L6-L18】

### Proposed Alignment Mapping
| Lifecycle Phase | Generator Output | Execution Requirement | Required Command Update |
| --- | --- | --- | --- |
| Phase 0 – Bootstrap | Context kit, stakeholder map, tech inventory, validation logs.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L86-L105】 | Same artifacts plus transcripts and convergence record.【F:.cursor/rules/Codex-Meta.mdc†L22-L83】 | Extend Protocol 0 with explicit templates, add automation to generate `metadata.json`, `context-kit.md`, `stakeholder-map.md`, and run IntakeGate. |
| Phase 1 – PRD | PRD, business logic, user journeys, acceptance criteria, validation.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L99-L105】 | Identical set in Execution with builder/auditor/challenger outputs.【F:.cursor/rules/Codex-Meta.mdc†L84-L155】 | Provide PRD template (Markdown + JSON schema), integrate stakeholder interview results, append validation transcript commands. |
| Phase 2 – Design | Architecture pack, contracts, environment plan, validation.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L107-L113】 | Aligned but needs schemas referenced in workflow automation.【F:.cursor/rules/Codex-Meta.mdc†L156-L229】 | Wire generator outputs into `workflow/gate_controller.yaml` and manifest checks. |
| Phase 3 – Quality Rails | Security, performance, accessibility plans, test strategy, validation.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L114-L120】 | Execution requires matching files plus PASS/FAIL logs.【F:.cursor/rules/Codex-Meta.mdc†L230-L303】 | Update commands to reference evidence paths and gating scripts (`run_quality_gates.sh`). |
| Phase 4 – Integration | Observability spec, SLO/SLI, deployment readiness, validation.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L121-L126】 | Execution requires same plus convergence log.【F:.cursor/rules/Codex-Meta.mdc†L244-L303】 | Align file naming (SLO_SLI.md) and include gate automation for staging smoke tests. |
| Phase 5 – Launch | Runbooks, rollback, DR, release notes, validation.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L128-L133】 | Execution aligned.【F:.cursor/rules/Codex-Meta.mdc†L296-L335】 | No change beyond schema references. |
| Phase 6 – Operations | SLO monitoring, incident response, retros, validation.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L135-L140】 | Execution aligned but commands missing persona/instructions.【F:.cursor/rules/Codex-Meta.mdc†L314-L355】 | Add Protocol 6 command to mirror Execution instructions and evidence logging. |

---

## Implementation Plan

### Intake Kit Deliverables
1. **Job Post Blueprint** (`docs/brief/jobpost.md`)
   - Sections: Business context, success metrics, stakeholder roster, compliance/regulatory constraints, tech baseline, timeline/budget, known integrations, risk appetite.
   - Include front-matter keys that match metadata schema (name, industry, project_type, frontend/backend/auth/deploy, compliance[], features[]).【F:project_generator/core/brief_parser.py†L12-L77】
2. **Interview Playbooks** (`docs/brief/interviews/*.md`)
   - Persona-specific question sets (Sponsor, Product, Engineering, Operations, Compliance) referencing Protocol 0/1 requirements.【F:.cursor/commands/0-bootstrap-your-project.md†L25-L74】【F:.cursor/commands/1-create-prd.md†L25-L90】
3. **Metadata Schema** (`workflow/schemas/intake-metadata.schema.json`)
   - JSON Schema enumerating required keys for IntakeGate (industry, project_type, personas, deadlines, compliance flags, budget).【F:scripts/workflow_automation/gates/implementations.py†L23-L69】
4. **Brief Assembly Script** (`scripts/intake/build_brief.py`)
   - Parse job post + interview notes → generate `docs/brief/current/brief.md` and `metadata.json` with normalization shared with `pre_lifecycle_plan`.【F:scripts/pre_lifecycle_plan.py†L775-L818】

### Workflow & Automation Updates
- Publish `workflow/gate_controller.yaml` with Intake, Environment, Planning gates configured to output evidence under `evidence/intake`, `evidence/environment`, `evidence/planning`.【F:workflow/templates/workflow_fullstack.yaml†L1-L34】
- Extend `gates_config.yaml` to add dynamic (tests, performance, accessibility), policy (security, compliance), and ADR gates per Codex requirements.【F:.cursor/rules/Codex-Meta.mdc†L406-L414】【F:gates_config.yaml†L1-L15】
- Update `workflow1` to include Phase 0–1 evidence directories (`evidence/phase0`, `evidence/phase1`) with `validation.md`, `manifest.json`, and transcripts (`builder.md`, `auditor.md`, `challenger.md`, `convergence.md`).【F:.cursor/rules/Codex-Meta.mdc†L35-L83】
- Add automation hooks in Protocol 0 to trigger IntakeGate and generate context kit/stakeholder map assets.

### Codex Command Enhancements
- Add `6-operations-protocol.md` mapping Execution Phase 6 instructions to command form, including monitoring scripts, incident response, and retrospective evidence logging.【F:.cursor/rules/Codex-Meta.mdc†L314-L355】
- Update existing commands with explicit evidence outputs (paths, filenames) and references to generated schemas so practitioners know how to validate deliverables.
- Embed convergence checklists in each command to document Builder → Auditor → Challenger → PASS loop.【F:.cursor/rules/Codex-Meta.mdc†L389-L404】

### Developer Experience Improvements
- Provide `make intake` target that:
  1. Copies job post template to `docs/brief/current/jobpost.md`.
  2. Prompts for required metadata fields and writes `metadata.json`.
  3. Calls `scripts/intake/build_brief.py` to assemble the initial brief and context kit skeleton.
- Generate `docs/plans/current/phase-map.md` summarizing phases, personas, and evidence directories for quick onboarding.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L70-L83】
- Add guidance in README linking new intake process to existing workflow automation (`python scripts/run_workflow.py --config workflow/gate_controller.yaml`).【F:README.md†L46-L92】

---

## Codex Execution Protocol (Proposed)
1. **Initiate Intake Session**
   - Trigger `make intake` to capture metadata and brief; store evidence under `evidence/intake/`.
   - Run IntakeGate → EnvironmentGate → PlanningGate via `scripts/run_workflow.py`.
2. **Generate Context Kit**
   - Execute Protocol 0 commands with new templates to produce context kit, stakeholder map, tech inventory, and validation logs.
3. **PRD Discovery**
   - Use interview notes + job post fields to complete PRD and associated evidence; run Builder/Auditor/Challenger validations.
4. **Design through Operations**
   - Follow existing workflow1 automation for phases 2–6, augmented with schema validation and convergence transcripts.
5. **Quality & Convergence Reporting**
   - After each phase, append PASS/FAIL entries to `var/validation/phase-<n>/` transcripts and update manifests for auditability.【F:.cursor/rules/Codex-Meta.mdc†L389-L404】

---

## Validation Framework
- **Success Criteria**
  - Intake artifacts generated (job post → metadata → brief → context kit) without manual file creation.
  - Workflow orchestrator completes IntakeGate, EnvironmentGate, and PlanningGate with evidence stored and linked in manifests.
  - Each phase (0–6) has populated `validation.md` tables and transcript files.
  - `gates_config.yaml` enforces static, dynamic, policy, ADR gates with actionable thresholds.

- **Testing Procedures**
  1. Run `make intake` (or equivalent script) and confirm output files match schema.
  2. Execute `python scripts/run_workflow.py --config workflow/gate_controller.yaml --project-root .` to validate gate orchestration.
  3. Review generated manifests to ensure evidence paths align with Codex expectations.
  4. Perform dry-run Builder/Auditor/Challenger sessions for Phase 0–1 using templates, verifying transcripts update correctly.

- **Performance Metrics**
  - Time from proposal acceptance to validated brief ≤ 2 hours with automation.
  - Zero IntakeGate failures due to missing metadata after template adoption.
  - 100% of phases include PASS/FAIL entries before progression.

- **Troubleshooting**
  - If IntakeGate fails, run schema validator on `metadata.json` to identify missing fields.
  - Missing evidence manifests indicate automation scripts did not run; re-run protocol macros and confirm output paths.
  - Divergent file names between Generator and Execution trigger CI alignment check; resolve by updating both files and schemas simultaneously.

---

## Next Steps & Ownership
1. **Workflow Steward** – build intake templates, metadata schema, and automation within one sprint.
2. **Codex Maintainer** – extend command set, align meta files, and add CI alignment check.
3. **Developer Experience Lead** – document new intake process in README, create onboarding guide, and integrate with template packs.
4. **Quality Engineer** – enhance `gates_config.yaml`, add performance/accessibility/policy checks, and configure workflow orchestrator.

Delivering these changes closes discovery gaps, restores Codex alignment, and enables repeatable, auditable engagement kickoff.

---

**`[REPORT4]`**
# SecretFlow Client Discovery & Workflow Alignment Assessment

## 1. Executive Summary
- **Validation Outcome:** The Codex generator, execution rulebook, and Cursor command protocols are **not aligned**; evidence paths, artifact names, and validation assets diverge in multiple phases, breaching the strict invariants in the repository guardrails.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L27-L170】【F:.cursor/rules/Codex-Meta.mdc†L37-L200】【F:AGENTS.md†L10-L41】【F:.cursor/commands/0-bootstrap-your-project.md†L13-L80】
- **Client Discovery Risk:** The discovery pipeline stalls immediately after proposal acceptance because the canonical job post template is empty, so no structured intake data flows into the framework or generator.【ae9cf8†L1-L3】
- **Workflow Coverage:** Workflow assets exist only for phases 2–6; discovery phases (0–1) lack populated evidence logs, automation, and transcripts, so developers cannot complete the context or PRD cycles defined by the meta-framework.【F:workflow1/PROJECT_EXECUTION_TEMPLATE.md†L5-L53】【F:workflow1/evidence/phase2/validation.md†L1-L4】
- **Quality Gates:** The live `gates_config.yaml` enforces only linting, security scan, and coverage checks, while the README and rulebooks demand full static/dynamic/policy/ADR coverage, leading to inconsistent developer expectations and compliance gaps.【F:gates_config.yaml†L1-L16】【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L134-L170】【F:.cursor/rules/Codex-Meta.mdc†L197-L410】【F:README.md†L139-L200】
- **Automation Debt:** Generator outputs (schemas, phase maps, `_generated` rulebooks) are not produced or referenced anywhere else in the repo, blocking Codex automation from orchestrating discovery-to-delivery handoffs.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L27-L83】【F:.cursor/rules/Codex-Meta.mdc†L389-L404】【F:workflow1/INDEX.md†L5-L53】

## 2. Alignment Validation
### 2.1 Result
> **Status: Not aligned.** Generator and execution documents diverge on evidence paths, persona outputs, quality gate coverage, version/hash metadata, and transcript schemas; command protocols implement a different lifecycle (0–5) and omit key validation assets.

### 2.2 Generator ↔ Execution Mapping Gaps
| Invariant | Generator Expectation | Execution Reality | Conflict |
| --- | --- | --- | --- |
| Evidence paths | `evidence/phaseN/<artifact>.md` with exact filenames (e.g., `tech-inventory.md`, `a11y-plan.md`).【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L94-L146】 | Uses alternate names such as `tech-inventory.md` (match) but later phases rename to `accessibility-test-plan.md`, `slo-sli-definitions.md` without generator updates.【F:.cursor/rules/Codex-Meta.mdc†L37-L249】 | Breaks 1:1 mapping mandated by AGENTS invariants.【F:AGENTS.md†L10-L23】 |
| Validation artifacts | `/var/validation/phase-<n>/{builder,auditor,challenger,convergence}.md` for all phases.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L66-L101】 | Execution references extra files (e.g., diff logs) but never defines builder transcripts or convergence artifacts per schema.【F:.cursor/rules/Codex-Meta.mdc†L37-L200】 | Transcript schema mismatch prevents automated PASS/FAIL loops. |
| Metadata | Shared `codexAlignmentVersion` & `codexAlignmentHash` front matter updated together.【F:AGENTS.md†L29-L41】 | Both files carry default values and have not been bumped for divergent edits.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L1-L6】【F:.cursor/rules/Codex-Meta.mdc†L1-L6】 | Alignment versioning contract broken. |
| Examples | Each phase must provide ✅/❌ examples in both files.【F:AGENTS.md†L14-L18】 | Generator covers some phases; execution replicates none beyond Phase 0 persona sections.【F:.cursor/rules/Codex-Meta.mdc†L24-L200】 | Violates invariants, reducing clarity. |
| Quality gates | Must list static, dynamic, policy, ADR categories with automation hooks.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L134-L170】 | Execution summarises gates but repo config enforces only lint, security scan, and coverage, no ADR/policy/perf coverage.【F:.cursor/rules/Codex-Meta.mdc†L197-L404】【F:gates_config.yaml†L1-L16】 | Fails to operationalise mandated gates. |

### 2.3 Generator ↔ Command Protocol Alignment
| Phase | Generator Persona & Outputs | Command Protocol Coverage | Gap |
| --- | --- | --- | --- |
| 0 — Bootstrap | Requires context kit, stakeholder map, tech inventory, validation logs.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L90-L105】 | Protocol 0 gathers context and risks but never references specific evidence outputs or validation transcripts.【F:.cursor/commands/0-bootstrap-your-project.md†L13-L80】 | Developers do not know where to store artifacts or how to trigger builder/auditor loops. |
| 1 — PRD | Requires PRD, business logic, user journeys, acceptance criteria, validation log.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L106-L120】 | Protocol 1 produces PRD, logic, testing plan, but lacks guidance for writing `validation.md` or transcripts.【F:.cursor/commands/1-create-prd.md†L14-L140】 | Intake lacks validation hand-off, breaking generator contract. |
| 2 — Design | Full alignment on outputs and automation references.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L122-L137】【F:.cursor/commands/2-generate-tasks.md†L14-L106】 | Commands emphasise task generation, not architecture evidence; requires cross-references to `workflow1` assets. |
| 3–5 | Generator expects quality rails → operations artifacts.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L138-L198】 | Protocols 3–5 focus on task execution, QC, retrospective rather than generator’s artifact list.【F:.cursor/commands/3-process-tasks.md†L1-L120】【F:.cursor/commands/4-quality-control-protocol.md†L1-L120】【F:.cursor/commands/5-implementation-retrospective.md†L1-L160】 | Lifecycle numbering (0–5) stops at retrospective; generator has Phases 0–6 with operations. |

## 3. Client Discovery Gap Analysis (Phase 1 Instructions)
### 3.1 Intake Workflow Trace
1. **Proposal Accepted → jobpost.md creation:** Template is empty, so no domain, scope, risk, or stakeholder data enters the system.【ae9cf8†L1-L3】
2. **Protocol 0 execution:** Collects context but lacks instructions for persisting outputs in mandated evidence paths or launching validation sessions.【F:.cursor/commands/0-bootstrap-your-project.md†L13-L80】
3. **Protocol 1 execution:** Captures PRD narrative yet omits data ingestion back to generator (no schema, manifest, or transcript references).【F:.cursor/commands/1-create-prd.md†L14-L140】
4. **Workflow assets:** `workflow1` still references “legacy” evidence for phases 0–1, confirming that new generator mandates were never implemented.【F:workflow1/PROJECT_EXECUTION_TEMPLATE.md†L5-L20】
5. **Automation hand-off:** No script consumes `docs/brief/jobpost.md`, leaving generator Step 1 (project fingerprint) without structured inputs.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L44-L63】

### 3.2 Missing Components
- Intake template fields (domain, stakeholders, constraints, regulatory requirements, success metrics).【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L19-L25】
- Discovery outputs for builder/auditor/challenger loops (Context Kit, risk log, validation transcripts).【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L66-L105】
- Schema definitions linking intake data to generator outputs (no JSON schema for job post ingestion).【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L70-L83】
- Instructions to run automation scripts after discovery (e.g., `write_context_report.py`) to publish artifacts.【F:README.md†L170-L200】

### 3.3 Practical Developer Pain Points
- No canonical place to store stakeholder interviews or risk decisions; manual note-taking results in inconsistent briefs.
- Ambiguity about when discovery is “complete” because validation gates are undefined for phases 0–1.
- Generator expects `_generated` personas and schemas but there is no tool or script to produce them, causing confusion when downstream commands reference missing assets.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L27-L83】【F:workflow1/INDEX.md†L5-L21】

## 4. Workflow Version Comparison Matrix
| Dimension | Workflow Templates (`workflow/templates`) | Workflow1 Implementation | Gap / Evolution Insight |
| --- | --- | --- | --- |
| Coverage | Generic backend/fullstack templates outline evidence structure from intake to submission.【F:workflow/templates/workflow_backend.yaml†L1-L33】【F:workflow/templates/workflow_fullstack.yaml†L1-L37】 | Workflow1 implements phases 2–6 with automation and evidence manifests; phases 0–1 flagged as “legacy” and lack actual assets.【F:workflow1/PROJECT_EXECUTION_TEMPLATE.md†L5-L20】【F:workflow1/INDEX.md†L5-L21】 | Evolution stalled after later phases; discovery modernization never happened. |
| Evidence Schema | Templates include JSON schema for manifests.【F:workflow/templates/evidence_schema.json†L1-L23】 | Workflow1 manifest for phase 2 follows ad-hoc structure, no validation tooling attached.【F:workflow1/evidence/phase2/manifest.json†L1-L67】 | Need shared schema & automation to validate manifests. |
| Automation | Templates reference `gate_controller.yaml` (missing). | Workflow1 uses bespoke scripts per phase but not orchestrated by commands or generator outputs.【F:workflow1/INDEX.md†L5-L53】 | Introduce orchestrator that ties generator outputs to workflow scripts. |
| Validation Logs | Templates assume `validation.md` per phase. | Logs exist but empty tables, no automation writes results.【F:workflow1/evidence/phase2/validation.md†L1-L4】 | Implement CLI to append builder/auditor/challenger entries. |

## 5. Recommended Client Intake Framework
1. **Job Post Schema (`docs/brief/jobpost.md`):** Introduce a structured template capturing domain, stakeholders, constraints, compliance needs, data sources, technical stack, success metrics, and timeline. Validate against a JSON schema stored under `docs/brief/jobpost.schema.json` to guarantee generator-ready data.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L19-L83】
2. **Discovery Checklist:** Embed Protocol 0/1 tasks referencing evidence paths (`evidence/phase0`, `evidence/phase1`) and `var/validation` transcripts; include builder/auditor/challenger prompts to finalize gating.【F:.cursor/commands/0-bootstrap-your-project.md†L13-L80】【F:.cursor/commands/1-create-prd.md†L24-L140】
3. **Automation Hooks:** After job post completion, run `python scripts/write_context_report.py --source docs/brief/jobpost.md` to populate `evidence/phase0/context-kit.md`, `stakeholder-map.md`, and `tech-inventory.md` automatically; follow with `python scripts/generate_from_brief.py` to prime generator Step 1.【F:README.md†L73-L200】
4. **Validation Loop:** Provide CLI commands (e.g., `scripts/log_validation.py --phase 0 --role builder`) that append to `var/validation/phase-0/*.md` and enforce PASS/FAIL gating before moving to Phase 1.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L66-L101】
5. **Handoff Manifest:** Generate `/docs/plans/<project-id>/phase-map.md` summarizing discovery outputs and ready-to-run personas to guarantee Protocol 2 receives structured context.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L27-L86】

## 6. Developer Experience Enhancements
- **Unified Lifecycle Guide:** Update README and Workflow1 index to explain how job posts feed generator outputs, referencing evidence directories and automation scripts explicitly.【F:README.md†L33-L200】【F:workflow1/INDEX.md†L5-L53】
- **Command Extensions:** Extend Cursor command files with sections for evidence output paths and validation transcript commands, ensuring each phase instructs developers where to store artifacts.【F:.cursor/commands/0-bootstrap-your-project.md†L13-L80】【F:.cursor/commands/1-create-prd.md†L14-L140】
- **Quality Gate Expansion:** Align `gates_config.yaml` with README expectations by adding static (formatting/type checks), dynamic (performance/accessibility), policy (privacy/compliance), and ADR verification toggles, then document corresponding scripts in `scripts/enforce_gates.py` usage notes.【F:gates_config.yaml†L1-L16】【F:README.md†L139-L200】
- **Alignment Guardrail:** Implement a CI script that parses generator and execution files to ensure identical phase sets, artifact names, and metadata hashes, blocking merges that reintroduce drift.【F:AGENTS.md†L42-L91】【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L27-L198】

## 7. Implementation Plan
| Phase | Tasks | Owners | Duration |
| --- | --- | --- | --- |
| Phase A – Alignment (Week 1) | Normalize artifact names across generator/execution; add missing ✅/❌ examples; update `codexAlignmentVersion/hash`; create alignment CI check.| Meta-framework maintainers | 3 days |
| Phase B – Discovery Framework (Week 2) | Populate `jobpost.md` template + schema; build automation to write phase 0/1 evidence; update Cursor protocols with validation instructions; backfill workflow1 evidence directories.| Discovery tooling team | 4 days |
| Phase C – Quality Gates (Week 2) | Expand `gates_config.yaml`; document gating workflow; integrate into `scripts/enforce_gates.py`.| DevEx/DevOps | 2 days |
| Phase D – Automation & Handoff (Week 3) | Generate `_generated` personas/protocols, phase map, and schemas; create CLI for validation transcripts; integrate manifests into workflow templates.| Automation team | 4 days |

## 8. Codex Execution Protocol (Post-Implementation)
1. **Intake Trigger:** When `docs/brief/jobpost.md` is updated, run `scripts/validate_brief.py` (new) against the intake schema; on success, call generator to emit `_generated` artifacts.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L27-L83】
2. **Phase 0 Cycle:** Execute Protocol 0 while concurrently logging builder/auditor/challenger transcripts; fail fast if any `var/validation` file lacks PASS result.
3. **Phase 1 Cycle:** Use updated PRD protocol to fill `evidence/phase1/*.md`, run validation CLI, and append outputs to the phase map.
4. **Pre-Phase 2 Gate:** Alignment CI verifies generator/execution parity, schema validity, and gate coverage before enabling task generation.
5. **Downstream Execution:** Workflow1 automation now consumes generated schemas and manifests, ensuring consistent evidence for phases 2–6.

## 9. Validation Framework & Success Metrics
- **Success Criteria:**
  - 100% of discovery engagements produce populated `evidence/phase0` and `evidence/phase1` directories plus `var/validation` logs before Protocol 2 starts.
  - Alignment CI passes with zero drift between generator and execution files every commit.
  - Quality gates enforce linting, tests, policy, performance, accessibility, and ADR checks with documented PASS/FAIL outcomes.
- **Checkpoints:**
  1. **Schema Validation:** Automated check ensures `docs/brief/jobpost.md` complies with intake schema before generator runs.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L70-L83】
  2. **Evidence Audit:** Script verifies required artifacts exist and are non-empty for phases 0–1; fails pipeline if missing.【F:.cursor/rules/Codex-Meta-Framework-Genarator.mdc†L90-L120】
  3. **Alignment Manifest:** Derived JSON manifest compares generator/execution phases, personas, evidence paths, and gates, enforcing AGENTS invariants.【F:AGENTS.md†L42-L91】
  4. **Quality Gate Report:** `scripts/enforce_gates.py` outputs coverage metrics; threshold <100% blocks progression to Protocol 2.【F:gates_config.yaml†L1-L16】
- **Metrics:** Time to complete discovery (target ≤3 days), percentage of briefs passing schema on first attempt, number of validation loop failures per engagement, and gate coverage adherence.

## 10. Troubleshooting & Recovery
- **Schema Failure:** Run `scripts/debug_brief.py` to surface missing intake fields; provide inline instructions in the job post template.
- **Alignment Drift:** Use CI report to pinpoint mismatched artifacts; auto-generate PR suggestions to rename files or add missing examples.
- **Validation Log Gaps:** CLI warns when builder/auditor/challenger files are empty; rerun interviews or audits before continuing.
- **Gate Failures:** Provide quickstart docs to execute missing tests (e.g., performance, accessibility) with recommended tooling.


---