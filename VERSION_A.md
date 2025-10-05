# Integration Plan Review

## ✅ Strengths
- The plan catalogues core missing domains (project generator, template packs, workflow1 protocols, review protocols) and explicitly calls out duplicate logic categories, creating a useful inventory for the integration scope.【F:INTEGRATION_PLAN.md†L17-L52】
- Prioritising core infrastructure before ancillary assets (protocols, templates, reviews) demonstrates an intent to stage work from foundational runtime capabilities upward.【F:INTEGRATION_PLAN.md†L55-L182】
- Including success criteria and a five-week high-level timeline shows awareness that completion requires validation checkpoints beyond code merges.【F:INTEGRATION_PLAN.md†L390-L433】

## ❌ Issues Found
- Phase 1 limits “core” integration to four new automation modules but omits numerous high-use scripts (e.g., `generate_client_project.py`, `generate_from_brief.py`, `generate_prd_assets.py`, `pre_lifecycle_plan.py`) and workflow automation helpers such as `context.py` and `templates/` that the unified system will need; these components are acknowledged as missing yet have no integration steps, leaving large functionality gaps.【F:INTEGRATION_PLAN.md†L17-L23】【F:INTEGRATION_PLAN.md†L57-L217】
- The plan proposes importing `scripts.lifecycle_tasks` as a package, but `scripts` is not a package (no top-level `__init__.py`), so those imports will fail without additional path bootstrapping—something the plan neither recognises nor mitigates.【F:INTEGRATION_PLAN.md†L86-L99】【1b0226†L1-L4】【F:scripts/lifecycle_tasks.py†L1-L200】
- Compliance integration assumes generator helpers can be consumed as pure libraries, yet scripts like `validate_compliance_assets.py` rely on repo-relative `sys.path` hacks and internal generator APIs; direct reuse inside a long-lived service demands refactoring or adapters that the plan does not schedule.【F:INTEGRATION_PLAN.md†L211-L217】【F:scripts/validate_compliance_assets.py†L1-L99】
- Copying the standalone `template-packs/` tree into `unified-workflow/templates/` ignores the existing `project_generator/template-packs` assets and the `project_generator.templates` engine, risking drift or duplication without a consolidation strategy.【F:INTEGRATION_PLAN.md†L132-L147】【d46f6a†L1-L2】
- Merging workflow1 protocols directly into phase markdowns risks losing the executable scripts, evidence templates, and automation hooks that live beside those protocols; the plan does not identify how scripts in each `workflow1/codex-phase*/scripts/` directory or `workflow1/evidence/` will be preserved or invoked post-merge.【F:INTEGRATION_PLAN.md†L148-L167】
- The timeline sequences template-pack work (Week 3) after phase protocol edits (Week 2), yet the protocol updates require template availability (e.g., architecture packs, quality rails scripts), creating a dependency inversion that will block execution.【F:INTEGRATION_PLAN.md†L219-L433】

## ⚠️ Risks Identified
- **Import/Packaging failures**: Without addressing non-package modules and `sys.path` manipulation, integrating scripts into new automation modules may break runtime imports, halting the unified CLI.【F:INTEGRATION_PLAN.md†L86-L217】【1b0226†L1-L4】【F:scripts/validate_compliance_assets.py†L1-L99】
- **Template divergence**: Blind copying of template packs could fork template registries between `project_generator` and the unified workflow, making it difficult to apply updates or enforce compliance consistently.【F:INTEGRATION_PLAN.md†L132-L147】【d46f6a†L1-L2】
- **Loss of protocol automation**: Flattening workflow1 protocols into markdown risks losing scripted quality gates and evidence automation, weakening compliance posture.【F:INTEGRATION_PLAN.md†L148-L167】
- **Schedule slippage**: Underestimating the work to reconcile 50+ scripts, tests, and adapters within five weeks increases the probability of unfinished integration or regression debt.【F:INTEGRATION_PLAN.md†L17-L23】【F:INTEGRATION_PLAN.md†L390-L433】

## 🔍 Missing Components
- Integration of `scripts/workflow_automation/context.py`, template helpers, and exception handling pathways is absent even though the plan intends to reuse the orchestrator stack.【F:INTEGRATION_PLAN.md†L106-L128】【3fa602†L1-L1】
- No path covers migrating `project_generator/tests` or broader automation test suites into the unified workflow, leaving the new system without regression protection.【F:INTEGRATION_PLAN.md†L327-L345】【d46f6a†L1-L2】
- The plan omits a unified CLI or packaging migration story even though risk mitigation calls for deprecating legacy commands; there is no work item to build or expose the consolidated entry point.【F:INTEGRATION_PLAN.md†L365-L371】
- Evidence schema and manifest alignment between legacy scripts and `unified-workflow/evidence/` templates is not described, despite duplicate logic being a key integration driver.【F:INTEGRATION_PLAN.md†L25-L52】

## 📋 Recommendations
- Expand Phase 1 to inventory and modularise all high-use scripts (generation, planning, validation, orchestration helpers) and define adapters for modules that currently rely on manual `sys.path` injection before wiring new automation facades.【F:INTEGRATION_PLAN.md†L57-L217】【F:scripts/validate_compliance_assets.py†L1-L99】
- Treat template consolidation as a design task: compare registries under `project_generator` and top-level `template-packs/`, define ownership, and build shared registry services before copying assets to avoid drift.【F:INTEGRATION_PLAN.md†L132-L147】【d46f6a†L1-L2】
- Create an explicit migration plan for workflow1 automation (scripts, evidence templates, CLI runners) so that markdown merges retain executable behaviours and validation hooks.【F:INTEGRATION_PLAN.md†L148-L167】
- Add a packaging and CLI consolidation workstream that introduces a new entry point, updates `requirements.txt`, and removes `sys.path` hacks to mitigate import fragility.【F:INTEGRATION_PLAN.md†L365-L371】【F:scripts/validate_compliance_assets.py†L1-L99】
- Reorder the timeline so shared assets (templates, tests) land before protocol rewrites, and budget extra time for refactoring adapters and regression testing across the 50+ legacy scripts.【F:INTEGRATION_PLAN.md†L219-L433】

## 🎯 Final Assessment
- **Overall plan quality**: 5/10 — strategic intent is clear, but execution details omit critical components and contain technical inaccuracies that will block integration.
- **Readiness for implementation**: Proceed only with substantial modifications to address missing integrations, packaging strategy, and sequencing corrections.
- **Key concerns**: Unresolved import mechanics for legacy scripts, lack of template consolidation design, potential loss of workflow1 automation, and unrealistic sequencing for templates vs. protocol updates.【F:INTEGRATION_PLAN.md†L57-L433】
- **Suggested next steps**: Produce a comprehensive component inventory, define adapter/refactor tasks for legacy scripts, design the unified template and CLI architecture, then revisit the timeline with dependency-aware milestones before implementation.【F:INTEGRATION_PLAN.md†L57-L433】
