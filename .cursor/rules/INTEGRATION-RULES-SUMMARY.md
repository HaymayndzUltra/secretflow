# Dev-Workflow Integration Rules - Implementation Summary

**Created:** 2025-10-06  
**Status:** ✅ Complete  
**Total Rules:** 7 (1 Master + 6 Common)

---

## Purpose

This rule set provides AI agents with comprehensive, unambiguous guidance for implementing the complete dev-workflow integration roadmap, connecting conversational protocols (Bootstrap → PRD → Tasks → Execution → Quality Audit → Retrospective) with automated tooling (template packs, project generator, automation scripts, CI/CD workflows).

**Core Goal:** Transform the dev-workflow from manual, conversational-only execution into a fully automated, evidence-driven delivery pipeline without gaps or misinterpretation.

---

## Rule Architecture

### Master Rule (Governance Layer)

**File:** `.cursor/rules/master-rules/7-master-rule-dev-workflow-integration-guide.mdc`

**Purpose:** Provides the complete integration architecture, protocol checkpoints, handoff validation, and references to all technical implementation rules.

**Key Sections:**
- The 6 Integration Recommendations overview
- Protocol checkpoint validation (Bootstrap → PRD → Tasks → Execution → Audit → Retro)
- Communication directives for integration status
- Validation & quality gates
- Comprehensive examples (✅ Correct / ❌ Anti-Pattern)

**When to Reference:** 
- Starting any integration implementation
- Understanding overall integration architecture
- Validating checkpoint transitions between protocols
- Troubleshooting integration issues

---

### Common Rules (Technical Implementation Layer)

#### 1. Rule Automation Protocol
**File:** `.cursor/rules/common-rules/rule-automation-protocol.mdc`

**Recommendation:** #1 - Automate Rule Lifecycle  
**Integration Points:** Protocol 0 (Bootstrap), Protocol 5 (Retrospective)

**Purpose:** Eliminate manual rule indexing and metadata validation by embedding `normalize_project_rules.py` and `rules_audit_quick.py` into bootstrap and retrospective workflows.

**Key Capabilities:**
- Automatic rule metadata normalization during bootstrap
- Rule compliance audits before retrospectives
- Audit report generation and storage
- Context kit updates with governance status

**When to Use:**
- Executing Protocol 0 (bootstrap)
- Executing Protocol 5 (retrospective)
- Validating rule metadata quality
- Generating compliance reports

---

#### 2. Template Bootstrap Integration
**File:** `.cursor/rules/common-rules/template-bootstrap-integration.mdc`

**Recommendation:** #2 - Template-Aware Bootstrap  
**Integration Points:** Protocol 0 (Bootstrap)

**Purpose:** Extend bootstrap to automatically discover template packs, recommend scaffolds based on validated stack, and optionally invoke ProjectGenerator for immediate code structure.

**Key Capabilities:**
- Template registry querying and filtering
- Stack-based template recommendations
- Optional generator invocation with brief preparation
- Generated artifact integration into context kit and rules

**When to Use:**
- Onboarding new projects
- Bootstrapping new microservices or modules
- Surfacing scaffold options during context discovery
- Generating initial project structure

---

#### 3. Task Automation Binding
**File:** `.cursor/rules/common-rules/task-automation-binding.mdc`

**Recommendation:** #3 - Task-to-Automation Binding  
**Integration Points:** Protocol 2 (Task Generation), Protocol 3 (Execution)

**Purpose:** Annotate task plans with explicit automation hooks (scripts, CI workflows) that Protocol 3 can execute to capture evidence, run validation, and align with CI/CD pipelines.

**Key Capabilities:**
- Task annotation with `Automation:` metadata
- Script/workflow reference validation
- Automated execution at Protocol 3 checkpoints
- Evidence artifact capture from automation

**When to Use:**
- Generating technical task plans (Protocol 2)
- Executing parent tasks (Protocol 3)
- Validating task automation coverage
- Capturing execution evidence

---

#### 4. CI Quality Gate Alignment
**File:** `.cursor/rules/common-rules/ci-quality-gate-alignment.mdc`

**Recommendation:** #4 - CI/CD Quality Gate Alignment  
**Integration Points:** Protocol 3 (Execution), Protocol 4 (Quality Audit), Protocol 5 (Retrospective)

**Purpose:** Map Protocol 4 quality audit outcomes to GitHub Actions workflows (lint, test, deploy) and feed CI/CD results back into retrospectives for closed-loop validation.

**Key Capabilities:**
- Pre-audit CI workflow status checks
- Workflow results embedded in quality audit reports
- Conditional workflow triggers based on audit findings
- CI/CD outcomes feeding into retrospectives

**When to Use:**
- Starting quality audits (Protocol 4)
- Validating parent task completion (Protocol 3)
- Analyzing CI/CD effectiveness in retrospectives
- Triggering deployment workflows

---

#### 5. Evidence Pipeline Standard
**File:** `.cursor/rules/common-rules/evidence-pipeline-standard.mdc`

**Recommendation:** #5 - Evidence Pipeline Standardization  
**Integration Points:** Protocol 3 (Execution), Protocol 5 (Retrospective)

**Purpose:** Standardize evidence artifact collection, storage, and aggregation to ensure Protocol 5 retrospectives reference tangible, automated evidence rather than manual notes.

**Key Capabilities:**
- Standardized artifact naming and storage conventions
- Evidence capture at defined checkpoints (sub-task, parent task, CI workflows, deployments)
- Pre-retrospective evidence aggregation
- Evidence-driven retrospective analysis

**When to Use:**
- Capturing test results during execution
- Storing quality audit reports
- Aggregating evidence before retrospectives
- Ensuring evidence-based recommendations

---

#### 6. Integration Execution Checklist
**File:** `.cursor/rules/common-rules/integration-execution-checklist.mdc`

**Recommendation:** #6 - Integration Execution Roadmap  
**Integration Points:** All protocols (phased implementation)

**Purpose:** Provide a concrete, phased roadmap (3 phases over 6 weeks) for implementing all integration recommendations with clear acceptance criteria, dependencies, and validation steps.

**Key Phases:**
- **Phase 1 (Weeks 1-2):** Foundation - Rule automation, template discovery
- **Phase 2 (Weeks 3-4):** Core Integration - Generator pipeline, task automation binding
- **Phase 3 (Weeks 5-6):** Enhancement - CI/CD alignment, evidence pipeline

**When to Use:**
- Planning integration implementation
- Tracking implementation progress
- Validating phase completion
- Troubleshooting integration issues

---

## Integration Recommendations Map

| Recommendation | Master Guide Section | Common Rule | Integration Points | Priority |
|----------------|---------------------|-------------|-------------------|----------|
| 1. Automate Rule Lifecycle | Section "Recommendation 1" | `rule-automation-protocol.mdc` | Protocol 0, 5 | High |
| 2. Template-Aware Bootstrap | Section "Recommendation 2" | `template-bootstrap-integration.mdc` | Protocol 0 | High |
| 3. Task-Automation Binding | Section "Recommendation 3" | `task-automation-binding.mdc` | Protocol 2, 3 | Medium |
| 4. CI/CD Quality Gate Alignment | Section "Recommendation 4" | `ci-quality-gate-alignment.mdc` | Protocol 3, 4, 5 | Medium |
| 5. Evidence Pipeline Standard | Section "Recommendation 5" | `evidence-pipeline-standard.mdc` | Protocol 3, 5 | Medium |
| 6. Integration Execution Checklist | Section "Recommendation 6" | `integration-execution-checklist.mdc` | All protocols | High |

---

## Protocol Integration Matrix

| Protocol | Rule 1 (Automation) | Rule 2 (Templates) | Rule 3 (Task Hooks) | Rule 4 (CI/CD) | Rule 5 (Evidence) | Rule 6 (Checklist) |
|----------|---------------------|-------------------|---------------------|---------------|-------------------|-------------------|
| **Protocol 0: Bootstrap** | ✅ Normalize rules, audit | ✅ Discover templates, invoke generator | - | - | - | ✅ Phase 1 |
| **Protocol 1: PRD** | - | Reference templates | - | - | - | - |
| **Protocol 2: Tasks** | Use rule index | Reference scaffolds | ✅ Annotate with automation hooks | - | - | ✅ Phase 2 |
| **Protocol 3: Execution** | - | - | ✅ Execute automation hooks | ✅ Check CI status | ✅ Capture artifacts | ✅ Phase 2-3 |
| **Protocol 4: Quality Audit** | - | - | Reference automation results | ✅ Embed CI results | Reference artifacts | ✅ Phase 3 |
| **Protocol 5: Retrospective** | ✅ Audit rules | - | Analyze automation effectiveness | ✅ Analyze CI outcomes | ✅ Load evidence | ✅ Phase 3 |

---

## Usage Guide for AI Agents

### Scenario 1: Executing Protocol 0 (Bootstrap)
**Rules to Apply:**
1. **Master Integration Guide** - Understand checkpoint validation
2. **Rule Automation Protocol** - Execute normalization and audit scripts
3. **Template Bootstrap Integration** - Discover templates, optionally invoke generator
4. **Integration Execution Checklist** - Follow Phase 1 tasks

**Expected Outcomes:**
- Normalized rules with audit report
- Template inventory in context kit
- Optional: Generated scaffold structure
- Context kit ready for PRD phase

---

### Scenario 2: Executing Protocol 2 (Task Generation)
**Rules to Apply:**
1. **Master Integration Guide** - Understand task generation checkpoint
2. **Task Automation Binding** - Annotate tasks with automation hooks
3. **Integration Execution Checklist** - Follow Phase 2 Step 2.2 tasks

**Expected Outcomes:**
- Task plan with `Automation:` metadata for every high-level task
- Automation hooks validated (reference actual scripts/workflows)
- Task plan approved and ready for execution

---

### Scenario 3: Executing Protocol 3 (Task Execution)
**Rules to Apply:**
1. **Master Integration Guide** - Understand execution checkpoint
2. **Task Automation Binding** - Execute automation hooks at checkpoints
3. **CI Quality Gate Alignment** - Check CI workflow statuses
4. **Evidence Pipeline Standard** - Capture evidence artifacts
5. **Integration Execution Checklist** - Follow Phase 2-3 validation

**Expected Outcomes:**
- Automation hooks executed successfully
- CI workflows validated and passed
- Evidence artifacts captured and stored
- Quality gate passed before retrospective

---

### Scenario 4: Executing Protocol 4 (Quality Audit)
**Rules to Apply:**
1. **Master Integration Guide** - Understand quality audit checkpoint
2. **CI Quality Gate Alignment** - Embed CI workflow results in audit report
3. **Integration Execution Checklist** - Follow Phase 3 Step 3.1 tasks

**Expected Outcomes:**
- Quality audit report includes CI/CD validation section
- Workflow statuses clearly indicated (✅/⚠️/❌)
- Audit score and recommendations documented
- Critical issues addressed before retrospective

---

### Scenario 5: Executing Protocol 5 (Retrospective)
**Rules to Apply:**
1. **Master Integration Guide** - Understand retrospective checkpoint
2. **Rule Automation Protocol** - Execute rule audit before analysis
3. **CI Quality Gate Alignment** - Analyze CI/CD outcomes
4. **Evidence Pipeline Standard** - Load aggregated evidence
5. **Integration Execution Checklist** - Follow Phase 3 Step 3.2 tasks

**Expected Outcomes:**
- Rule audit complete with compliance status
- Evidence report aggregated and loaded
- CI/CD outcomes analyzed with metrics
- Evidence-based recommendations documented

---

## Quick Reference: File Paths

### Master Rule
```
.cursor/rules/master-rules/7-master-rule-dev-workflow-integration-guide.mdc
```

### Common Rules
```
.cursor/rules/common-rules/rule-automation-protocol.mdc
.cursor/rules/common-rules/template-bootstrap-integration.mdc
.cursor/rules/common-rules/task-automation-binding.mdc
.cursor/rules/common-rules/ci-quality-gate-alignment.mdc
.cursor/rules/common-rules/evidence-pipeline-standard.mdc
.cursor/rules/common-rules/integration-execution-checklist.mdc
```

### Referenced Files
```
.cursor/dev-workflow/README.md                     # Five-protocol overview
.cursor/dev-workflow/0-bootstrap-your-project.md   # Protocol 0
.cursor/dev-workflow/1-create-prd.md               # Protocol 1
.cursor/dev-workflow/2-generate-tasks.md           # Protocol 2
.cursor/dev-workflow/3-process-tasks.md            # Protocol 3
.cursor/dev-workflow/4-quality-audit.md            # Protocol 4
.cursor/dev-workflow/5-implementation-retrospective.md # Protocol 5

template-packs/README.md                           # Template pack documentation
project_generator/README.md                        # Generator documentation
scripts/README.md                                  # Automation scripts
.github/workflows/ci-{lint,test,deploy}.yml       # CI/CD workflows
```

---

## Metadata for Discovery

### Tags
```
[global, workflow, integration, automation, governance, bootstrap, template, 
generator, scaffolding, onboarding, task-generation, execution, ci-cd, 
quality-gates, workflows, deployment, evidence, artifacts, retrospective, 
compliance, audit, roadmap, implementation, checklist, phased-rollout]
```

### Triggers
```
bootstrap, protocol, integration, dev-workflow, automation, template pack, 
project generator, scaffolding, new project, task generation, automation hooks, 
task plan, script binding, workflow integration, quality audit, CI/CD, workflows, 
deployment, quality gate, evidence, artifacts, retrospective, compliance, 
coverage reports, integration checklist, roadmap, phase, rollout
```

### Scopes
```
global, bootstrap, task-generation, execution, quality-audit, retrospective, 
deployment, common-rules
```

---

## Success Criteria

Mark integration rules as successfully implemented when:

✅ **Rule Creation:**
- All 7 rules created with proper YAML frontmatter
- Metadata follows Cursor specification (description, tags, triggers, scope)
- All rules include comprehensive examples (✅ Correct / ❌ Anti-Pattern)
- Cross-references between rules functional

✅ **Content Quality:**
- All 6 integration recommendations covered
- Protocol checkpoints clearly defined
- Acceptance criteria measurable
- Troubleshooting guides complete

✅ **Validation:**
- AI agents can discover rules via metadata
- Rules reference actual file paths correctly
- Examples executable or testable
- No conflicting directives between rules

✅ **User Acceptance:**
- Operator confirms rules clear and actionable
- AI agents tested with integration workflows
- No blocking ambiguities identified

---

## Next Steps for Operators

### Immediate Actions:
1. **Review Rules:** Read master integration guide for architecture overview
2. **Test Discovery:** Verify AI agents can find rules via metadata
3. **Validate References:** Confirm all file paths reference existing files
4. **Plan Implementation:** Use integration execution checklist to plan rollout

### Phase 1 Preparation:
1. Ensure `scripts/normalize_project_rules.py` functional
2. Ensure `scripts/rules_audit_quick.py` functional
3. Verify template registry accessible
4. Confirm Python environment with dependencies

### AI Agent Training:
1. Test Protocol 0 execution with rule automation
2. Test Protocol 2 task generation with automation hooks
3. Test Protocol 3 execution with hook execution
4. Test Protocol 5 retrospective with evidence loading

---

## Support & Troubleshooting

### Common Issues:

**Issue 1: Rules Not Discoverable**
- Check YAML frontmatter valid
- Verify description field includes TAGS, TRIGGERS, SCOPE
- Ensure `.mdc` file extension used

**Issue 2: File References Broken**
- Validate all `[file](mdc:path)` references
- Ensure paths relative to workspace root
- Confirm referenced files exist

**Issue 3: Integration Validation Failures**
- Review integration execution checklist acceptance criteria
- Execute validation commands manually
- Check dependencies (scripts, workflows) available

### Getting Help:
- **Master Rule:** Complete integration architecture and troubleshooting
- **Common Rules:** Specific implementation guidance per recommendation
- **Codex Analysis:** Source recommendations and gap analysis
- **Dev-Workflow Protocols:** Existing protocol documentation

---

## Version History

**v1.0.0** (2025-10-06)
- Initial release: 7 comprehensive integration rules
- Master integration guide with 6 recommendations
- 6 common rules for technical implementation
- Complete phased roadmap (3 phases, 6 weeks)
- Comprehensive examples and troubleshooting

---

## License & Attribution

These rules are part of the AI Governor Framework dev-workflow integration.

**Created for:** SecretFlow Project  
**Created by:** AI Integration Specialist (Claude Sonnet 4.5)  
**Date:** October 6, 2025  
**Purpose:** Enable AI agents to correctly implement dev-workflow integration without misinterpretation

---

**For AI Agents:** This summary provides a complete overview of the integration rule system. When executing any protocol, consult the master integration guide first, then reference the specific common rules relevant to that protocol's integration points. Follow the phased roadmap in the integration execution checklist for implementation.

**Para sa mga AI Agent:** Ang summary na ito ay nagbibigay ng kumpletong overview ng integration rule system. Kapag nag-execute ng anumang protocol, konsultahin muna ang master integration guide, pagkatapos ay i-reference ang mga specific common rules na relevant sa integration points ng protocol na iyon. Sundin ang phased roadmap sa integration execution checklist para sa implementation.

