# Workflow1 Assets Catalog and Integration Mapping

## Overview
This document catalogs all automation assets in the workflow1/ directory structure and maps them to the appropriate unified-workflow phase executors. These assets would be lost if only protocol.md files are merged as currently planned.

## Phase 2: Design Assets

### Scripts
| Script | Purpose | Language | Integration Target | Migration Strategy |
|--------|---------|----------|-------------------|-------------------|
| `generate_architecture_pack.py` | Generate architecture documentation pack | Python | `unified-workflow/automation/design_generator.py` | Import as module or wrap as subprocess |
| `generate_contract_assets.py` | Generate API contracts and specifications | Python | `unified-workflow/automation/contract_generator.py` | Import as module or wrap as subprocess |

### Templates
- Architecture document templates
- C4 model diagram templates
- ADR (Architecture Decision Record) templates
- OpenAPI specification templates

### Integration Plan
```python
# In unified-workflow/phases/2-task-generation.md
- Call design_generator.generate_architecture_pack()
- Call contract_generator.generate_contract_assets()
- Reference templates from workflow1/codex-phase2-design/templates/
```

## Phase 3: Quality Rails Assets

### Scripts
| Script | Purpose | Language | Integration Target | Migration Strategy |
|--------|---------|----------|-------------------|-------------------|
| `configure_feature_flags.py` | Configure feature flags for gradual rollout | Python | `unified-workflow/automation/feature_flag_manager.py` | Import as module |
| `run_quality_gates.sh` | Execute quality gate checks | Bash | `unified-workflow/automation/quality_gates.py` | Rewrite in Python or subprocess wrapper |

### Quality Configurations
- Security checklist templates
- Performance budget configurations
- Accessibility test plans
- Test coverage requirements

### Integration Plan
```python
# In unified-workflow/phases/3-implementation.md
- Call feature_flag_manager.configure_flags()
- Execute quality gates via quality_gates.run_all()
- Load quality configs from workflow1/codex-phase3-quality-rails/
```

## Phase 4: Integration Assets

### Scripts
| Script | Purpose | Language | Integration Target | Migration Strategy |
|--------|---------|----------|-------------------|-------------------|
| `generate_observability_pack.py` | Generate observability configuration | Python | `unified-workflow/automation/observability_generator.py` | Import as module |
| `run_staging_smoke.sh` | Run staging environment smoke tests | Bash | `unified-workflow/automation/smoke_test_runner.py` | Rewrite in Python |

### Integration Configurations
- Observability specification templates
- SLO/SLI definition templates
- Staging test configurations
- Integration test suites

### Integration Plan
```python
# In unified-workflow/phases/4-quality-audit.md
- Call observability_generator.generate_pack()
- Execute smoke_test_runner.run_staging_tests()
- Load SLO/SLI templates from workflow1/codex-phase4-integration/
```

## Phase 5: Launch Assets

### Scripts
| Script | Purpose | Language | Integration Target | Migration Strategy |
|--------|---------|----------|-------------------|-------------------|
| `rehearse_rollback.sh` | Rehearse rollback procedures | Bash | `unified-workflow/automation/rollback_manager.py` | Python wrapper with subprocess |
| `verify_dr_restore.sh` | Verify disaster recovery restore | Bash | `unified-workflow/automation/dr_validator.py` | Python wrapper with subprocess |

### Launch Configurations
- Deployment runbook templates
- Rollback plan templates
- Production observability configs
- Backup policy templates
- DR plan templates
- Go-live checklist templates

### Integration Plan
```python
# In unified-workflow/phases/5-retrospective.md
- Call rollback_manager.rehearse_rollback()
- Call dr_validator.verify_restore()
- Load runbook templates from workflow1/codex-phase5-launch/
```

## Phase 6: Operations Assets

### Scripts
| Script | Purpose | Language | Integration Target | Migration Strategy |
|--------|---------|----------|-------------------|-------------------|
| `monitor_slo.py` | Monitor SLO compliance | Python | `unified-workflow/automation/slo_monitor.py` | Direct import |
| `schedule_retros.py` | Schedule retrospective meetings | Python | `unified-workflow/automation/retro_scheduler.py` | Direct import |

### Operations Configurations
- Postmortem templates
- Dependency update log templates
- Security update log templates
- Operations runbook templates

### Integration Plan
```python
# In unified-workflow/phases/6-operations.md
- Call slo_monitor.check_compliance()
- Call retro_scheduler.schedule_next()
- Load postmortem templates from workflow1/codex-phase6-operations/
```

## Evidence Templates (Shared Across Phases)

### Location: `workflow1/evidence/`
| Template | Purpose | Integration Target |
|----------|---------|-------------------|
| `manifest-template.json` | Evidence manifest structure | Merge with `unified-workflow/evidence/manifest-template.json` |
| `run-log-template.json` | Execution log format | Merge with `unified-workflow/evidence/run-log-template.json` |
| `validation-template.md` | Validation report format | Merge with `unified-workflow/evidence/validation-template.md` |
| Phase-specific evidence formats | Per-phase evidence requirements | Extend unified evidence schema |

## Migration Implementation Plan

### Step 1: Create Wrapper Modules
Create Python wrapper modules in `unified-workflow/automation/` for each script:

```python
# unified-workflow/automation/design_generator.py
import subprocess
from pathlib import Path

class DesignGenerator:
    def __init__(self):
        self.workflow1_path = Path(__file__).parents[2] / "workflow1"
    
    def generate_architecture_pack(self, project_name: str):
        script_path = self.workflow1_path / "codex-phase2-design/scripts/generate_architecture_pack.py"
        result = subprocess.run([sys.executable, str(script_path), "--project", project_name], 
                               capture_output=True, text=True)
        return result
```

### Step 2: Update Phase Protocols
Update each unified-workflow phase markdown to reference the new automation entry points:

```markdown
## Phase 2: Task Generation

### Automation Steps
1. Generate architecture pack: `design_generator.generate_architecture_pack()`
2. Generate contract assets: `contract_generator.generate_contract_assets()`
3. Load templates from workflow1 design phase
```

### Step 3: Preserve Script Functionality
Options for preserving scripts:
1. **Direct Import**: For Python scripts, import as modules
2. **Subprocess Wrapper**: For shell scripts or complex Python scripts
3. **Rewrite**: For simple shell scripts, rewrite in Python
4. **Symlink**: Create symlinks in unified automation directory

### Step 4: Evidence Schema Extension
Extend unified evidence schema to include workflow1 evidence types:
```json
{
  "schema_version": "2.0.0",
  "includes_workflow1_extensions": true,
  "phase_specific_evidence": {
    "phase2": ["architecture_pack", "contract_assets"],
    "phase3": ["quality_gates_report", "feature_flags_config"],
    "phase4": ["observability_pack", "smoke_test_results"],
    "phase5": ["rollback_verification", "dr_test_results"],
    "phase6": ["slo_compliance_report", "retro_schedule"]
  }
}
```

## Risk Mitigation

### Identified Risks
1. **Script Loss**: Direct markdown merge would lose all automation scripts
2. **Template Orphaning**: Templates referenced by scripts would become orphaned
3. **Evidence Format Drift**: Different evidence formats between systems
4. **Execution Context**: Scripts may rely on workflow1 directory structure

### Mitigation Strategies
1. **Preserve Scripts**: Use wrapper strategy to maintain all scripts
2. **Link Templates**: Update template references to use unified registry
3. **Schema Merge**: Create unified evidence schema with extensions
4. **Path Resolution**: Add path resolution logic to handle both structures

## Next Steps

1. Create wrapper modules for all identified scripts
2. Update phase protocols with automation references
3. Test script execution in unified context
4. Validate evidence generation compatibility
5. Document migration for operators
