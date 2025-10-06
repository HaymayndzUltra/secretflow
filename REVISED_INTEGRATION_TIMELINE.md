# Revised Integration Timeline - Dependency-Aware Sequencing

## Executive Summary

The original 5-week timeline has critical dependency inversions:
- Week 2 (Phase Protocol Enhancement) requires templates from Week 3
- Core infrastructure needs precede all integration work
- Testing scheduled only at end invites late regression discovery

**Revised Timeline: 7 weeks** with proper dependency ordering and incremental validation gates.

## Week 1: Foundation & Infrastructure (NEW)

### Goals
- Fix Python packaging issues
- Establish shared infrastructure
- Create adapter patterns

### Tasks
1. **Day 1-2: Package Structure Fixes**
   - [x] Add `scripts/__init__.py` 
   - [ ] Fix sys.path manipulations in 9 high-priority scripts
   - [ ] Create adapter modules in `unified-workflow/automation/`
   - [ ] Test import resolution

2. **Day 3-4: Unified Template Registry**
   - [x] Create `unified-workflow/core/template_registry.py`
   - [x] Update `project_generator/templates/registry.py` to delegate
   - [ ] Test template discovery and loading
   - [ ] Document template versioning strategy

3. **Day 5-7: Evidence Schema Resolution**
   - [x] Create `evidence_schema_converter.py`
   - [ ] Test legacy to unified conversion
   - [ ] Create migration scripts for historical data
   - [ ] Update evidence managers to use unified schema

### Validation Gate 1
- [ ] All imports resolve without sys.path hacks
- [ ] Template registry finds all templates
- [ ] Evidence converter passes unit tests
- [ ] No regression in existing functionality

## Week 2: Core Integration Modules (Was Week 1)

### Goals
- Integrate project generator
- Integrate brief processor
- Setup workflow automation foundation

### Tasks
1. **Day 1-2: Project Generator Integration**
   - [ ] Complete `unified-workflow/automation/project_generator.py`
   - [ ] Import ProjectGenerator, ProjectValidator, IndustryConfig
   - [ ] Add template registry integration
   - [ ] Test project generation end-to-end

2. **Day 3-4: Brief Processing Integration**
   - [ ] Complete `unified-workflow/automation/brief_processor.py`
   - [ ] Import BriefParser, lifecycle_tasks
   - [ ] Add metadata extraction
   - [ ] Test brief to plan generation

3. **Day 5-7: Workflow Automation Foundation**
   - [ ] Complete `unified-workflow/automation/workflow_automation.py`
   - [ ] Import WorkflowOrchestrator, WorkflowConfig
   - [ ] Integrate gate implementations
   - [ ] Test workflow execution

### Validation Gate 2
- [ ] Project generation works via unified interface
- [ ] Brief processing produces valid plans
- [ ] Workflow orchestration executes gates
- [ ] All unit tests pass

## Week 3: Template & CLI Integration (Was Week 2-3 Split)

### Goals
- Complete template migration
- Implement CLI compatibility layer
- Setup deprecation tracking

### Tasks
1. **Day 1-2: Template Pack Migration**
   - [ ] Verify unified registry loads all templates
   - [ ] Update template references in generators
   - [ ] Test template application
   - [ ] Document template governance

2. **Day 3-4: CLI Compatibility Layer**
   - [ ] Create `unified-workflow/cli.py`
   - [ ] Implement command routing to legacy scripts
   - [ ] Add telemetry for usage tracking
   - [ ] Test backward compatibility

3. **Day 5-7: Compliance Validation Integration**
   - [x] Complete `unified-workflow/automation/compliance_validator.py`
   - [ ] Integrate HIPAA/SOC2/PCI validators
   - [ ] Test compliance asset generation
   - [ ] Update gates to use unified validators

### Validation Gate 3
- [ ] All templates accessible via unified registry
- [ ] Legacy CLI commands route correctly
- [ ] Compliance validation produces correct assets
- [ ] Integration tests pass

## Week 4: Protocol & Automation Integration (Was Week 2)

### Goals
- Merge workflow1 protocols WITH automation
- Preserve all scripts and evidence templates
- Update phase documentation

### Tasks
1. **Day 1-3: Protocol and Script Integration**
   - [ ] Catalog all workflow1/*/scripts/ (DONE in planning)
   - [ ] Create wrapper modules for each script
   - [ ] Update phase protocols to reference wrappers
   - [ ] Test script execution in unified context

2. **Day 4-5: Evidence Template Merge**
   - [ ] Merge workflow1/evidence/ templates
   - [ ] Update evidence schema with extensions
   - [ ] Test evidence generation compatibility
   - [ ] Document evidence format migration

3. **Day 6-7: Phase Documentation Update**
   - [ ] Update all 7 phase markdown files
   - [ ] Add automation entry points
   - [ ] Include template references
   - [ ] Document operator instructions

### Validation Gate 4
- [ ] All workflow1 scripts executable
- [ ] Evidence generation works across phases
- [ ] Phase protocols reference correct automation
- [ ] End-to-end phase execution succeeds

## Week 5: External Services & Review Protocols (Was Week 4)

### Goals
- Integrate external service dependencies
- Merge review protocols
- Complete quality gate enhancements

### Tasks
1. **Day 1-2: External Services Integration**
   - [ ] Integrate `project_generator/integrations/`
   - [ ] Setup Git integration for Phase 0
   - [ ] Setup AI governor for Phase 3
   - [ ] Configure policy DSL for compliance

2. **Day 3-4: Review Protocol Integration**
   - [ ] Import `.cursor/dev-workflow/review-protocols/`
   - [ ] Wire into quality_gates.py
   - [ ] Wire into validation_gates.py
   - [ ] Test review execution

3. **Day 5-7: Orchestrator Enhancement**
   - [ ] Update `ai_orchestrator.py` with all integrations
   - [ ] Update `ai_executor.py` for new components
   - [ ] Add comprehensive error handling
   - [ ] Test orchestration with all components

### Validation Gate 5
- [ ] External services authenticate correctly
- [ ] Review protocols execute in gates
- [ ] Orchestrator handles all phases
- [ ] Quality metrics collected properly

## Week 6: Testing & Validation (Was Week 5)

### Goals
- Build comprehensive test suite
- Validate all integrations
- Performance testing

### Tasks
1. **Day 1-2: Unit Test Suite**
   - [ ] Test all adapter modules
   - [ ] Test converters and registries
   - [ ] Test individual components
   - [ ] Achieve 80% code coverage

2. **Day 3-4: Integration Test Suite**
   - [ ] Test project generation flow
   - [ ] Test brief to deployment flow
   - [ ] Test evidence collection
   - [ ] Test gate execution

3. **Day 5-7: End-to-End Testing**
   - [ ] Full workflow execution test
   - [ ] Performance benchmarking
   - [ ] Load testing
   - [ ] Security validation

### Validation Gate 6
- [ ] All unit tests pass
- [ ] All integration tests pass
- [ ] Performance meets baselines
- [ ] No security vulnerabilities

## Week 7: Documentation & Deployment (NEW)

### Goals
- Complete documentation
- Operator training materials
- Production deployment

### Tasks
1. **Day 1-2: Documentation**
   - [x] Update all README files
   - [x] Create migration guide
   - [x] Document new CLI
   - [x] Create troubleshooting guide

2. **Day 3-4: Training Materials**
   - [x] Create operator quickstart
   - [ ] Record demo videos *(deferred – scripts prepared, recording pending)*
   - [x] Create example projects
   - [x] Setup support channels

3. **Day 5-7: Production Rollout**
   - [ ] Deploy to staging *(runbook authored; execution scheduled in production environment)*
   - [ ] Run acceptance tests *(suite documented; awaiting environment window)*
   - [ ] Deploy to production *(pending go/no-go approval)*
   - [ ] Monitor for issues *(monitoring checklist prepared in runbook)*

### Final Validation Gate
- [x] Documentation complete and reviewed *(Week 7 operations library published)*
- [ ] Training materials tested with users *(pilot session scheduled)*
- [ ] Production deployment successful *(pending environment availability)*
- [ ] Monitoring shows healthy metrics *(monitoring checklist ready for execution)*

## Risk Mitigation Updates

### Addressed Risks
1. **Dependency Inversions**: Fixed by reordering weeks
2. **Late Testing**: Added validation gates between each week
3. **Packaging Issues**: Addressed in Week 1 foundation work
4. **Template Divergence**: Unified registry in Week 1
5. **Evidence Schema Conflicts**: Converter in Week 1

### Remaining Risks
1. **Timeline Extension**: 7 weeks vs original 5 weeks
   - *Mitigation*: Communicate early, show value of proper sequencing
2. **Resource Availability**: More developer time needed
   - *Mitigation*: Can parallelize some tasks across team
3. **Legacy System Downtime**: During cutover
   - *Mitigation*: CLI compatibility layer enables gradual migration

## Success Metrics

### Per-Week Metrics
- Week 1: Infrastructure ready, 0 sys.path hacks remain
- Week 2: Core modules integrated, 100% test pass rate
- Week 3: Templates unified, CLI telemetry active
- Week 4: All automation preserved, evidence compatible
- Week 5: External services connected, reviews automated
- Week 6: 80% test coverage, performance validated
- Week 7: 100% documentation, successful deployment

### Overall Success Criteria
- [ ] No runtime import failures
- [ ] All 40+ scripts integrated or wrapped
- [ ] Single template registry (no divergence)
- [ ] Evidence format unified
- [ ] All workflow1 automation preserved
- [ ] Performance equal or better
- [ ] Zero production incidents in first week

## Recommendation

**APPROVE 7-WEEK REVISED TIMELINE**

The additional 2 weeks are necessary to:
1. Fix foundational issues before building on them
2. Properly sequence dependencies
3. Add validation gates to catch issues early
4. Include documentation and training
5. Ensure safe production deployment

Attempting the original 5-week timeline would result in:
- Runtime failures from import issues
- Template discovery problems
- Lost automation from workflow1
- Late discovery of integration bugs
- Rushed deployment without proper validation

The revised timeline delivers a robust, properly integrated system with minimal production risk.
