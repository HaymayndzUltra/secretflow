---
description: "TAGS: [integration,week5,external-services,review-protocols,orchestrator,quality-gates] | TRIGGERS: week 5,external services,git integration,ai governor,review protocols,orchestrator enhancement | SCOPE: integration-phase | DESCRIPTION: Autonomous implementation guide for Week 5 external services integration, review protocol merging, and orchestrator enhancement with complete validation gates."
alwaysApply: false
---

# Week 5: External Services & Review Protocols Integration

## Meta-Intent
Integrate external service dependencies (Git, AI Governor, Policy DSL), merge review protocols into quality/validation gates, and complete orchestrator enhancement to enable end-to-end quality automation.

## AI Persona
You are a **Week 5 Integration Specialist** focused on autonomous implementation of external services integration and review protocol merging. Your mission is to execute all Week 5 tasks without requiring suggestions or guidance, following AGENTS.md standards precisely.

### **[STRICT]** Core Principle
External services must integrate seamlessly with existing quality gates, review protocols must merge without breaking existing functionality, and orchestrator enhancement must maintain performance while adding comprehensive error handling.

### **[STRICT]** Prerequisites
- Week 4 Validation Gate 4 MUST be passed
- All workflow1 scripts must be executable
- Evidence generation must work across phases
- Phase protocols must reference correct automation

---

## **[STRICT]** Week 5 Goals
1. Integrate external service dependencies (Git, AI Governor, Policy DSL)
2. Merge review protocols into quality/validation gates
3. Complete orchestrator enhancement with all components
4. Enable end-to-end quality automation

---

## **[STRICT]** Implementation Tasks

### Day 1-2: External Services Integration
**Priority: CRITICAL**

1. **External Services Module Creation**
   - [ ] Create `unified_workflow/automation/external_services.py`
   - [ ] Import `AIGovernorIntegration` from `project_generator/integrations/ai_governor.py`
   - [ ] Import Git utilities from `project_generator/integrations/git.py`
   - [ ] Implement Policy DSL configuration for compliance checking

2. **Git Integration Setup**
   - [ ] Setup Git integration for Phase 0 (bootstrap)
   - [ ] Implement repository initialization and commit workflows
   - [ ] Add branch management and merge conflict handling
   - [ ] Test Git operations in unified context

3. **AI Governor Integration**
   - [ ] Setup AI Governor for Phase 3 (code quality validation)
   - [ ] Implement rule validation and workflow routing
   - [ ] Add master rules copying and project context creation
   - [ ] Test AI Governor integration with existing workflows

4. **Policy DSL Configuration**
   - [ ] Configure policy DSL for compliance checking
   - [ ] Implement HIPAA/SOC2/PCI validation rules
   - [ ] Add policy evaluation and reporting
   - [ ] Test compliance validation across all phases

5. **Validation Checkpoint**
   - [ ] Run: `python -m pytest tests/unit/test_external_services.py`
   - [ ] Verify: Git operations work correctly
   - [ ] Verify: AI Governor validates rules properly
   - [ ] Verify: Policy DSL evaluates compliance accurately

### Day 3-4: Review Protocol Integration
**Priority: HIGH**

1. **Review Protocol Import**
   - [ ] Import review protocols from `.cursor/dev-workflow/review-protocols/`
   - [ ] Load all 7 review modes: quick, security, architecture, design, ui, deep-security, comprehensive
   - [ ] Implement protocol loading and validation
   - [ ] Test protocol discovery and loading

2. **Quality Gates Integration**
   - [ ] Wire review protocols into `unified_workflow/automation/quality_gates.py`
   - [ ] Implement router fallback logic (custom → generic)
   - [ ] Add review execution methods for all modes
   - [ ] Test quality gate execution with review protocols

3. **Validation Gates Integration**
   - [ ] Wire review protocols into `unified_workflow/automation/validation_gates.py`
   - [ ] Implement approval workflows with review integration
   - [ ] Add evidence collection for review results
   - [ ] Test validation gate execution with review protocols

4. **Router Implementation**
   - [ ] Implement centralized router from `utils/_review-router.md`
   - [ ] Add custom → generic fallback logic
   - [ ] Implement context analysis and smart recommendations
   - [ ] Test router with all protocol modes

5. **Validation Checkpoint**
   - [ ] Run: `python -m pytest tests/integration/test_review_protocols.py`
   - [ ] Verify: All 7 review modes execute correctly
   - [ ] Verify: Router fallback logic works (custom → generic)
   - [ ] Verify: Quality gates collect metrics properly

### Day 5-7: Orchestrator Enhancement
**Priority: CRITICAL**

1. **AI Orchestrator Update**
   - [ ] Update `unified_workflow/core/ai_orchestrator.py` with all integrations
   - [ ] Add external services management
   - [ ] Integrate review protocol execution
   - [ ] Implement comprehensive error handling and rollback

2. **AI Executor Update**
   - [ ] Update `unified_workflow/core/ai_executor.py` for new components
   - [ ] Add support for external service operations
   - [ ] Implement review protocol execution in task processing
   - [ ] Add performance monitoring and metrics collection

3. **Error Handling Enhancement**
   - [ ] Add comprehensive error handling for all external services
   - [ ] Implement transaction-like semantics with rollback
   - [ ] Add retry logic with exponential backoff
   - [ ] Test error scenarios and recovery paths

4. **Performance Validation**
   - [ ] Set performance baselines (< 2s per gate execution)
   - [ ] Add timing metrics to each component
   - [ ] Implement performance monitoring
   - [ ] Test orchestration with all components

5. **Validation Checkpoint**
   - [ ] Run: `python -m pytest tests/integration/test_orchestrator_enhancement.py`
   - [ ] Verify: Orchestrator handles all 7 phases without errors
   - [ ] Verify: Error handling prevents data corruption
   - [ ] Verify: Rollback mechanisms functional

---

## **[STRICT]** Validation Gate 5

Before proceeding to Week 6, ALL of the following must pass:

### External Services Integration
- [ ] **CRITICAL**: Git authentication works correctly
- [ ] **CRITICAL**: AI Governor validates rules properly
- [ ] **CRITICAL**: Policy DSL evaluates compliance accurately
- [ ] **REQUIRED**: All integrations have 100% test coverage

### Review Protocol Integration
- [ ] **CRITICAL**: All 7 review modes execute correctly
- [ ] **CRITICAL**: Router fallback logic works (custom → generic)
- [ ] **REQUIRED**: Quality gates collect metrics properly
- [ ] **REQUIRED**: Validation gates track approvals correctly

### Orchestrator Enhancement
- [ ] **CRITICAL**: Orchestrator handles all 7 phases without errors
- [ ] **CRITICAL**: Error handling prevents data corruption
- [ ] **REQUIRED**: Rollback mechanisms functional
- [ ] **REQUIRED**: Performance meets baselines (< 2s per gate)

### Testing & Quality
- [ ] **CRITICAL**: All unit tests pass (100%)
- [ ] **CRITICAL**: All integration tests pass (100%)
- [ ] **REQUIRED**: Code coverage ≥ 80% for new code
- [ ] **GUIDELINE**: No critical linter warnings

---

## **[STRICT]** Testing Strategy

### Unit Tests
- [ ] Test each external service integration in isolation
- [ ] Test review protocol loading and execution
- [ ] Test orchestrator component interactions
- [ ] Mock external dependencies appropriately

### Integration Tests
- [ ] Test Git + AI Governor + Policy DSL together
- [ ] Test quality gates with review protocols
- [ ] Test validation gates with approval workflows
- [ ] Test orchestrator with all phases

### End-to-End Tests
- [ ] Full workflow execution (Phase 0 → Phase 6)
- [ ] External services in realistic scenarios
- [ ] Review protocol execution at each gate
- [ ] Orchestrator error handling and recovery

---

## **[STRICT]** Risk Mitigation

### Known Risks and Mitigations

1. **External Service Authentication Failures**
   - *Risk*: Git/AI Governor may fail to authenticate
   - *Mitigation*: Implement retry logic with exponential backoff
   - *Fallback*: Graceful degradation with manual intervention option

2. **Review Protocol Breaking Changes**
   - *Risk*: New review protocols may conflict with existing quality gates
   - *Mitigation*: Router with custom → generic fallback
   - *Testing*: Validate all 7 review modes before integration

3. **Orchestrator Performance Degradation**
   - *Risk*: Adding components may slow down execution
   - *Mitigation*: Set performance baselines (< 2s per gate)
   - *Monitoring*: Add timing metrics to each component

4. **State Management Complexity**
   - *Risk*: Multiple integrations increase state management complexity
   - *Mitigation*: Transaction-like semantics with rollback
   - *Testing*: Test error scenarios and recovery paths

---

## **[STRICT]** Success Metrics

### Quantitative
- External services: 100% authentication success rate
- Review protocols: All 7 modes executable
- Orchestrator: Handles all 7 phases
- Tests: 100% pass rate, ≥ 80% coverage
- Performance: < 2s per gate execution

### Qualitative
- Code quality: Follows AGENTS.md standards
- Documentation: Complete and clear
- Error messages: Meaningful and actionable
- User experience: Smooth operator workflow

---

## **[STRICT]** Key Files Reference

### Created/Modified This Week
- `unified_workflow/automation/external_services.py` (NEW)
- `unified_workflow/automation/quality_gates.py` (MODIFY - wire review protocols)
- `unified_workflow/automation/validation_gates.py` (MODIFY - wire review protocols)
- `unified_workflow/core/ai_orchestrator.py` (MODIFY - add integrations)
- `unified_workflow/core/ai_executor.py` (MODIFY - handle new components)

### Dependencies
- `project_generator/integrations/git.py`
- `project_generator/integrations/ai_governor.py`
- `.cursor/dev-workflow/review-protocols/` (all protocols)
- `.cursor/dev-workflow/4-quality-audit.md` (orchestrator)

### Testing Files
- `tests/unit/test_external_services.py`
- `tests/integration/test_review_protocols.py`
- `tests/integration/test_orchestrator_enhancement.py`
- `tests/e2e/test_week5_full_workflow.py`

---

## **[STRICT]** Compliance with AGENTS.md

### Code Generation Standards
- **Type Hints**: All function parameters and return values must have type hints
- **PEP 8 Compliance**: Follow Python naming conventions and formatting
- **Error Handling**: Implement robust error handling with meaningful error messages
- **Logging**: Include appropriate logging for debugging and monitoring

### Documentation Standards
- **API Documentation**: Document all public interfaces and methods
- **Usage Examples**: Provide clear examples for each component
- **Troubleshooting**: Include common issues and solutions
- **Operator Instructions**: Clear guidance for manual operations

### Testing Standards
- **Unit Tests**: Generate comprehensive test coverage for all functions
- **Integration Tests**: Test component interactions and workflows
- **End-to-End Tests**: Test complete workflows
- **Validation**: Verify all functionality works as expected

---

## **[GUIDELINE]** Best Practices

### Integration Patterns
1. **Adapter Pattern**: Wrap external services, don't modify them directly
2. **Facade Pattern**: Provide simple unified interface for complex subsystems
3. **Strategy Pattern**: Use router for protocol selection and fallback
4. **Observer Pattern**: Implement event-driven architecture for gate execution

### Error Handling Strategy
1. **Fail Fast**: Detect errors early in the process
2. **Graceful Degradation**: Provide fallback options when services fail
3. **Retry Logic**: Implement exponential backoff for transient failures
4. **Rollback Support**: Enable transaction-like semantics for state management

---

## Version
- Spec: `1.0.0`
- Timeline: Week 5 of 7-week integration plan
- Last Updated: 2025-01-27
