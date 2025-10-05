# Integration Timeline Project Rules

## Overview

This directory contains Cursor Rules for the 7-week revised integration timeline. These rules guide both AI agents and human developers through the systematic integration of the unified workflow system.

## Structure

```
project-rules/
├── README.md                              # This file
├── integration-timeline-overview.mdc      # Master overview and navigation
├── week1-foundation-infrastructure.mdc    # Week 1: Foundation work
├── week2-core-integration.mdc             # Week 2: Core modules
├── week3-template-cli.mdc                 # Week 3: Templates & CLI
├── week4-protocol-automation.mdc          # Week 4: Protocols & scripts
├── week5-external-services.mdc            # Week 5: External integrations
├── week6-testing-validation.mdc           # Week 6: Comprehensive testing
└── week7-documentation-deployment.mdc     # Week 7: Docs & production
```

## How to Use

### For AI Agents (Claude, etc.)

AI agents should load the appropriate weekly rule based on the current integration phase:

1. **Start with Overview**: First load `integration-timeline-overview.mdc` to understand the full timeline
2. **Load Current Week**: Load the rule for the week you're working on
3. **Follow Prerequisites**: Ensure previous week's validation gate passed before starting
4. **Execute Tasks**: Follow the tasks in order (Day 1-2, Day 3-4, etc.)
5. **Run Checkpoints**: Execute validation checkpoints after task groups
6. **Pass Validation Gate**: Complete ALL validation gate requirements before proceeding

**Example Workflow**:
```
User: "Let's start Week 2 integration"
AI: 
1. Check Week 1 validation gate status
2. If passed, load week2-core-integration.mdc
3. Follow Day 1-2 tasks
4. Run validation checkpoint
5. Continue through week
6. Complete Validation Gate 2
```

### For Human Developers

Use these rules as implementation guides:

1. **Review Timeline**: Start with `integration-timeline-overview.mdc` to understand dependencies
2. **Weekly Planning**: Review the week's rule at the start of each week
3. **Daily Tasks**: Follow the day-by-day task breakdown
4. **Validation**: Use validation checkpoints to ensure quality
5. **Gate Review**: Complete validation gates before moving to next week

### For Project Managers

Use these rules for planning and tracking:

1. **Schedule**: 7-week timeline with clear milestones (validation gates)
2. **Dependencies**: Clear dependency flow prevents parallel work conflicts
3. **Metrics**: Each week has specific success metrics
4. **Risk Management**: Known risks documented with mitigations

## Rule Metadata

Each weekly rule includes:

- **TAGS**: For discoverability (integration, weekN, domain-specific)
- **TRIGGERS**: Keywords that should trigger rule loading
- **SCOPE**: Integration phase
- **DESCRIPTION**: One-sentence summary of the week's purpose

## Validation Gates

Critical checkpoints between weeks:

| Gate | Week | Requirements | Purpose |
|------|------|--------------|---------|
| Gate 1 | Week 1 | Infrastructure ready | Foundation validated |
| Gate 2 | Week 2 | Core modules operational | Integration tested |
| Gate 3 | Week 3 | Templates unified, CLI working | Interfaces ready |
| Gate 4 | Week 4 | Automation preserved | Scripts functional |
| Gate 5 | Week 5 | External services integrated | Full stack ready |
| Gate 6 | Week 6 | All tests passing | Production ready |
| Final Gate | Week 7 | Deployment successful | Operational |

### Gate Passage Criteria

- **[CRITICAL]**: 100% completion required (non-negotiable)
- **[REQUIRED]**: 100% completion required (must pass)
- **[GUIDELINE]**: ≥80% completion recommended (best effort)

## Quick Reference

### Current Week
```bash
# Check current week status
cat CURRENT_WEEK.txt
```

### Load Appropriate Rule
- **Week 1**: Load `week1-foundation-infrastructure.mdc`
- **Week 2**: Load `week2-core-integration.mdc`
- **Week 3**: Load `week3-template-cli.mdc`
- **Week 4**: Load `week4-protocol-automation.mdc`
- **Week 5**: Load `week5-external-services.mdc`
- **Week 6**: Load `week6-testing-validation.mdc`
- **Week 7**: Load `week7-documentation-deployment.mdc`

### Validation Commands
```bash
# Run week validation
python unified-workflow/automation/validate_week.py --week N

# Check gate status
python unified-workflow/automation/gate_status.py --gate N

# Track progress
python unified-workflow/automation/track_progress.py --report
```

## Success Metrics Summary

### Overall Project Success Criteria
- [ ] No runtime import failures
- [ ] All 40+ scripts integrated
- [ ] Single template registry
- [ ] Evidence format unified
- [ ] All automation preserved
- [ ] Performance maintained or improved
- [ ] ≥80% test coverage
- [ ] Zero critical security vulnerabilities
- [ ] Zero production incidents in first week

### Weekly Targets
- **Week 1**: 0 sys.path hacks remain
- **Week 2**: 100% test pass rate
- **Week 3**: CLI telemetry active
- **Week 4**: Evidence compatible
- **Week 5**: Reviews automated
- **Week 6**: 80% coverage, validated
- **Week 7**: 100% documentation, deployed

## Timeline Rationale

### Why 7 Weeks (Not 5)?

The revised timeline adds 2 weeks for:

1. **Week 1 (NEW)**: Foundation work that was missing
   - Fix packaging issues BEFORE building on them
   - Establish infrastructure that everything depends on

2. **Validation Gates**: Catch issues early
   - Original plan had testing only at end
   - New plan validates after each week

3. **Week 7 (NEW)**: Proper deployment
   - Documentation and training
   - Safe production rollout
   - Monitoring and support setup

### Risk of Rushing (5-week timeline)
- Runtime failures from import issues
- Template discovery problems
- Lost automation from workflow1
- Late discovery of integration bugs
- Rushed deployment without validation

## Related Documentation

- [REVISED_INTEGRATION_TIMELINE.md](../../REVISED_INTEGRATION_TIMELINE.md) - Complete timeline document
- [INTEGRATION_ANALYSIS.md](../../INTEGRATION_ANALYSIS.md) - Analysis that led to timeline
- [INTEGRATION_PLAN.md](../../INTEGRATION_PLAN.md) - Detailed integration plan
- [UNIFIED_DEVELOPER_WORKFLOW.md](../../UNIFIED_DEVELOPER_WORKFLOW.md) - Workflow specification

## Version History

- **v1.0.0** (2025-10-05): Initial 7-week timeline rules created
  - Based on REVISED_INTEGRATION_TIMELINE.md
  - Includes all 7 weekly guides
  - Master overview for navigation
  - Comprehensive validation gates

## Support

For questions or issues:
1. Check the specific week's rule for detailed guidance
2. Review the troubleshooting section in each weekly guide
3. Consult the integration timeline overview for dependencies
4. Refer to the main project documentation

## Contributing

When updating these rules:
1. Follow the System Instruction Formatter protocol
2. Maintain consistent structure across weeks
3. Update validation gates if requirements change
4. Keep success metrics measurable
5. Document any timeline adjustments

