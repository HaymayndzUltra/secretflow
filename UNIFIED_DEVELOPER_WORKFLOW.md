# UNIFIED DEVELOPER WORKFLOW
## End-to-End AI-Driven Development Lifecycle

### Executive Summary
Ang Unified Developer Workflow ay isang comprehensive na system na nag-uugnay ng lahat ng components ng AI Governor Framework sa isang cohesive, end-to-end development lifecycle. Ito ay nagbibigay ng structured na approach mula sa project inception hanggang sa production operations, na may automated quality gates, evidence logging, at governance enforcement.

---

## 🏗️ SYSTEM ARCHITECTURE OVERVIEW

### Core Components Integration Map
```
┌─────────────────────────────────────────────────────────────────┐
│                    UNIFIED DEVELOPER WORKFLOW                  │
├─────────────────────────────────────────────────────────────────┤
│  Phase 0: Bootstrap → Phase 1: PRD → Phase 2: Design         │
│  ↓                                                             │
│  Phase 3: Quality Rails → Phase 4: Integration                │
│  ↓                                                             │
│  Phase 5: Launch → Phase 6: Operations                        │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│                    GOVERNANCE & AUTOMATION                     │
├─────────────────────────────────────────────────────────────────┤
│  Rules Engine (/rules) ← → Dev Workflow (/dev-workflow)       │
│  ↓                                                             │
│  Project Generator ← → Template Packs ← → Scripts Catalog     │
│  ↓                                                             │
│  Evidence Schema ← → Workflow1 Protocols ← → Quality Gates    │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📋 PHASE-BY-PHASE EXECUTION PLAN

### Phase 0: Bootstrap & Repository Readiness
**Objective:** I-establish ang governed context at project-specific rules

**AI Actions:**
- Execute `0-bootstrap-your-project.md` protocol
- Scan repository structure at generate context kits
- Sync master/common/project rules hierarchy
- Validate rule integrity using `rules_audit_quick.py`

**Required Artifacts:**
- Updated `.cursor/rules/project-rules/`
- Context kit documentation
- Bootstrap evidence log
- Rule manifest snapshot

**Human Validation:**
- Confirm rule coverage matches architectural intent
- Approve context kit completeness
- Validate no sensitive information omissions

**Evidence Logging:**
```json
{
  "phase": "0-bootstrap",
  "artifacts": [
    {
      "path": "context-kit/README.md",
      "category": "documentation",
      "description": "Project context summary",
      "checksum": "sha256-hash",
      "created_at": "2025-01-XX"
    }
  ]
}
```

---

### Phase 1: Discovery & PRD Creation
**Objective:** I-convert ang client brief sa validated PRD

**AI Actions:**
- Execute `1-create-prd.md` protocol
- Conduct stakeholder interviews
- Generate PRD using `generate_prd_assets.py`
- Populate workflow1 phase1 evidence structure

**Required Artifacts:**
- PRD markdown document
- Requirement summaries
- Stakeholder mapping
- Acceptance criteria matrix

**Human Validation:**
- Review PRD scope completeness
- Validate requirement accuracy
- Confirm stakeholder alignment
- Approve before proceeding to planning

**Evidence Logging:**
```json
{
  "phase": "1-prd",
  "artifacts": [
    {
      "path": "prd-<feature>.md",
      "category": "requirements",
      "description": "Product Requirements Document",
      "checksum": "sha256-hash",
      "created_at": "2025-01-XX"
    }
  ]
}
```

---

### Phase 2: Technical Planning & Architecture
**Objective:** I-translate ang PRD sa actionable technical plan

**AI Actions:**
- Execute `codex-phase2-design/protocol.md`
- Generate `PLAN.md` at `tasks.json` using `plan_from_brief.py`
- Run `generate_architecture_pack.py` at `generate_contract_assets.py`
- Populate architecture artifacts (C4 diagrams, ADRs, OpenAPI specs)

**Required Artifacts:**
- `PLAN.md` technical roadmap
- `tasks.json` with parent/child hierarchy
- Architecture pack (C4 diagrams, ADRs)
- Contract assets (OpenAPI specs, data models)
- Product backlog CSV
- Sprint 0 plan

**Human Validation:**
- Review architecture decisions
- Validate task sequencing
- Confirm compliance coverage
- Approve before implementation

**Evidence Logging:**
```json
{
  "phase": "2-design",
  "artifacts": [
    {
      "path": "evidence/phase2/outputs/<project>/architecture/Architecture.md",
      "category": "architecture",
      "description": "System architecture documentation",
      "checksum": "sha256-hash",
      "created_at": "2025-01-XX"
    }
  ]
}
```

---

### Phase 3: Quality Rails & Implementation
**Objective:** I-implement ang features na may continuous quality gates

**AI Actions:**
- Execute `codex-phase3-quality-rails/protocol.md`
- Bootstrap quality templates using `run_quality_gates.sh --bootstrap`
- Configure feature flags using `configure_feature_flags.py`
- Implement parent tasks sequentially
- Apply unified `/review` orchestrator per task
- Run quality gates automation

**Required Artifacts:**
- Security checklist with ASVS mapping
- Performance budgets (Lighthouse/Web Vitals)
- Accessibility test plan
- Analytics specification
- Feature flag manifest
- Test plan with coverage thresholds
- Code review checklist

**Human Validation:**
- Review audit outcomes
- Approve each parent task completion
- Validate quality gate compliance
- Confirm evidence completeness

**Evidence Logging:**
```json
{
  "phase": "3-quality-rails",
  "artifacts": [
    {
      "path": "evidence/phase3/outputs/<project>/quality-rails/Security_Checklist.md",
      "category": "security",
      "description": "Security compliance checklist",
      "checksum": "sha256-hash",
      "created_at": "2025-01-XX"
    }
  ]
}
```

---

### Phase 4: Integration & System Validation
**Objective:** I-validate ang cross-service integration at observability

**AI Actions:**
- Execute `codex-phase4-integration/protocol.md`
- Generate observability pack using `generate_observability_pack.py`
- Run staging smoke tests using `run_staging_smoke.sh`
- Update CHANGELOG entries
- Draft SLO/SLI definitions

**Required Artifacts:**
- Observability specification
- SLO/SLI documentation
- CHANGELOG updates
- Staging smoke playbook
- Integration test results

**Human Validation:**
- Review integration evidence completeness
- Validate staging test results
- Confirm observability coverage
- Approve before launch preparation

**Evidence Logging:**
```json
{
  "phase": "4-integration",
  "artifacts": [
    {
      "path": "evidence/phase4/outputs/<project>/integration/Observability_Spec.md",
      "category": "observability",
      "description": "System observability specification",
      "checksum": "sha256-hash",
      "created_at": "2025-01-XX"
    }
  ]
}
```

---

### Phase 5: Launch Readiness & Deployment
**Objective:** I-finalize ang deployment runbooks at release documentation

**AI Actions:**
- Execute `codex-phase5-launch/protocol.md`
- Run rollback rehearsal using `rehearse_rollback.sh`
- Verify DR restore using `verify_dr_restore.sh`
- Complete deployment runbooks
- Generate release notes
- Compile submission checklist

**Required Artifacts:**
- Deployment runbook
- Rollback plan
- DR plan
- Production observability checklist
- Release notes
- Go-live checklist
- SEO checklist (if applicable)

**Human Validation:**
- Confirm deployment readiness
- Validate rollback procedures
- Review DR plan completeness
- Authorize production release

**Evidence Logging:**
```json
{
  "phase": "5-launch",
  "artifacts": [
    {
      "path": "evidence/phase5/outputs/<project>/launch/Deployment_Runbook.md",
      "category": "deployment",
      "description": "Production deployment procedures",
      "checksum": "sha256-hash",
      "created_at": "2025-01-XX"
    }
  ]
}
```

---

### Phase 6: Operations & Continuous Improvement
**Objective:** I-maintain ang system health post-launch

**AI Actions:**
- Execute `codex-phase6-operations/protocol.md`
- Monitor SLOs using `monitor_slo.py`
- Schedule retrospectives using `schedule_retros.py`
- Track dependency updates
- Conduct postmortems
- Update compliance logs

**Required Artifacts:**
- SLO monitoring reports
- Retrospective schedules
- Dependency update logs
- Security update logs
- Postmortem documentation

**Human Validation:**
- Review operational metrics
- Confirm SLA adherence
- Validate incident response procedures
- Authorize automation cycles

**Evidence Logging:**
```json
{
  "phase": "6-operations",
  "artifacts": [
    {
      "path": "evidence/phase6/outputs/<project>/operations/slo_status.json",
      "category": "monitoring",
      "description": "SLO compliance status",
      "checksum": "sha256-hash",
      "created_at": "2025-01-XX"
    }
  ]
}
```

---

## 🔧 AUTOMATION & GOVERNANCE INTEGRATION

### Rules Engine Integration
```yaml
# Master Rules (Foundation Layer)
- Context Discovery Protocol
- AI Collaboration Guidelines
- Code Quality Checklist
- Modification Safety Protocol
- Documentation Guidelines

# Common Rules (Execution Layer)
- UI Foundation Design System
- Interaction Accessibility Performance
- Premium Brand DataViz Enterprise

# Project Rules (Specialization Layer)
- Stack-specific conventions
- Domain-specific constraints
- Client-specific requirements
```

### Quality Gates Automation
```bash
# Quality Rails Execution
python scripts/run_quality_gates.sh --bootstrap
python scripts/run_quality_gates.sh --project <slug>

# Coverage & Performance
python scripts/aggregate_coverage.py
python scripts/collect_perf.py
python scripts/enforce_gates.py --metrics-root metrics

# Security & Dependencies
python scripts/scan_deps.py
python scripts/validate_compliance_assets.py --config gates_config.yaml
```

### Evidence Schema Compliance
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Evidence Manifest",
  "type": "object",
  "properties": {
    "artifacts": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["path", "category", "description", "checksum", "created_at"],
        "properties": {
          "path": {"type": "string"},
          "category": {"type": "string"},
          "description": {"type": "string"},
          "checksum": {"type": "string", "pattern": "^[a-f0-9]{64}$"},
          "created_at": {"type": "string", "format": "date-time"}
        }
      }
    },
    "generated_at": {"type": "string", "format": "date-time"}
  },
  "required": ["artifacts", "generated_at"]
}
```

---

## 🚀 PROJECT GENERATION & TEMPLATE INTEGRATION

### Generator Workflow
```python
# Project Generation Pipeline
from project_generator.core.generator import ProjectGenerator
from project_generator.core.validator import ProjectValidator

# 1. Parse brief and validate stack compatibility
validator = ProjectValidator()
report = validator.validate_comprehensive(args)

# 2. Generate project scaffold
generator = ProjectGenerator(args=args, validator=validator)
result = generator.generate()

# 3. Post-process (Git init, pre-commit hooks)
generator.post_process()
```

### Template Pack Structure
```
template-packs/
├── frontend/
│   ├── nextjs/
│   ├── nuxt/
│   └── angular/
├── backend/
│   ├── fastapi/
│   ├── django/
│   └── nestjs/
├── database/
│   ├── postgres/
│   ├── mongodb/
│   └── firebase/
├── devex/
│   ├── devcontainer/
│   ├── docker-compose/
│   └── vscode-snippets/
└── cicd/
    ├── github-workflows/
    └── gates-config.yaml
```

---

## 📊 MONITORING & CONTINUOUS IMPROVEMENT

### SLO Monitoring
```python
# SLO Compliance Tracking
python scripts/monitor_slo.py --project <slug>
# Outputs: evidence/phase6/outputs/<project>/operations/slo_status.json
```

### Retrospective Scheduling
```python
# Retrospective Automation
python scripts/schedule_retros.py --project <slug>
# Outputs: evidence/phase6/outputs/<project>/operations/retro_schedule.json
```

### Dependency & Security Updates
```python
# Security Monitoring
python scripts/scan_deps.py
# Outputs: metrics/deps.json with vulnerability counts
```

---

## 🎯 SUCCESS METRICS & VALIDATION

### Phase Completion Criteria
- **Phase 0:** Rule coverage ≥ 95%, context kit completeness
- **Phase 1:** PRD stakeholder approval, requirement traceability
- **Phase 2:** Architecture approval, task DAG validation
- **Phase 3:** Quality gates pass, evidence completeness
- **Phase 4:** Integration tests pass, observability coverage
- **Phase 5:** Deployment readiness, DR validation
- **Phase 6:** SLO compliance, operational excellence

### Evidence Trail Validation
```bash
# Validate evidence completeness
python scripts/evidence_report.py --input evidence/
python scripts/validate_workflows.py --config workflow.yaml
```

---

## 🔄 FEEDBACK LOOPS & ITERATION

### Continuous Improvement Cycle
1. **Retrospectives** → Rule updates
2. **Postmortems** → Process improvements
3. **SLO breaches** → Architecture refinements
4. **Security incidents** → Compliance updates
5. **Performance issues** → Optimization priorities

### Governance Evolution
- Regular rule audits using `rules_audit_quick.py`
- Template pack updates based on project feedback
- Automation script improvements from operational learnings
- Evidence schema refinements for better traceability

---

## 📚 IMPLEMENTATION CHECKLIST

### Pre-Implementation
- [ ] Repository structure validated
- [ ] Rules hierarchy established
- [ ] Template packs available
- [ ] Automation scripts tested
- [ ] Evidence schema validated

### During Implementation
- [ ] Phase protocols followed
- [ ] Quality gates enforced
- [ ] Evidence logged per schema
- [ ] Human validations obtained
- [ ] Automation scripts executed

### Post-Implementation
- [ ] Evidence completeness verified
- [ ] SLO monitoring active
- [ ] Retrospectives scheduled
- [ ] Documentation updated
- [ ] Knowledge transfer completed

---

## 🎉 CONCLUSION

Ang Unified Developer Workflow ay nagbibigay ng:

1. **Structured Approach** - Clear phase-by-phase execution
2. **Automated Quality Gates** - Continuous compliance enforcement
3. **Evidence Trail** - Complete audit trail for all decisions
4. **Human Validation** - Strategic approvals at key milestones
5. **Continuous Improvement** - Feedback loops for system evolution

Ito ay nag-uugnay ng lahat ng components ng AI Governor Framework sa isang cohesive, end-to-end development lifecycle na nagbibigay ng predictable, high-quality software delivery.

---

*Generated by AI Governor Framework Unified Developer Workflow v1.0*
*Last Updated: 2025-01-XX*
