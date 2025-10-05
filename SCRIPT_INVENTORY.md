# Script Inventory and Integration Mapping

## Overview
This document inventories all 40+ scripts in the `scripts/` directory, categorizes them by function, identifies sys.path manipulations, and maps them to unified workflow components.

## Script Categories

### 1. Project Generation & Bootstrapping (8 scripts)
| Script | Purpose | sys.path Issues | Integration Target | Status |
|--------|---------|-----------------|-------------------|---------|
| `generate_client_project.py` | Generate new projects from templates | ✅ Uses sys.path.insert | → `unified-workflow/automation/project_generator.py` | HIGH PRIORITY |
| `generate_from_brief.py` | Generate project from brief file | ✅ Uses sys.path.insert | → `unified-workflow/automation/brief_processor.py` | HIGH PRIORITY |
| `bootstrap_project.py` | One-command project bootstrap | ✅ Uses sys.path.insert | → `unified-workflow/automation/project_generator.py` | HIGH PRIORITY |
| `generate_prd_assets.py` | Generate PRD documentation | ❌ Clean imports | → `unified-workflow/automation/prd_generator.py` | MEDIUM |
| `scaffold_briefs.py` | Create brief templates | ❌ Clean imports | → `unified-workflow/automation/brief_processor.py` | LOW |
| `scaffold_phase_artifacts.py` | Generate phase deliverables | ❌ Clean imports | → `unified-workflow/phases/artifact_generator.py` | LOW |
| `select_stacks.py` | Recommend tech stacks | ❌ Clean imports | → `unified-workflow/automation/stack_selector.py` | MEDIUM |
| `trigger_plan.py` | Trigger plan regeneration | ❌ Clean imports | → `unified-workflow/automation/plan_manager.py` | MEDIUM |

### 2. Planning & Task Management (6 scripts)
| Script | Purpose | sys.path Issues | Integration Target | Status |
|--------|---------|-----------------|-------------------|---------|
| `plan_from_brief.py` | Generate plan from brief | ✅ Uses sys.path.insert | → `unified-workflow/automation/brief_processor.py` | HIGH PRIORITY |
| `pre_lifecycle_plan.py` | Pre-lifecycle planning | ✅ Uses sys.path.insert | → `unified-workflow/automation/plan_manager.py` | HIGH PRIORITY |
| `lifecycle_tasks.py` | Task generation library | ❌ Clean (imported by others) | → Keep as library, fix imports | HIGH PRIORITY |
| `enrich_tasks.py` | Add task metadata | ❌ Clean imports | → `unified-workflow/automation/task_enricher.py` | LOW |
| `update_task_state.py` | Update task status | ❌ Clean imports | → `unified-workflow/automation/task_manager.py` | LOW |
| `lane_executor.py` | Execute tasks by lane | ❌ Clean imports | → `unified-workflow/automation/task_executor.py` | MEDIUM |

### 3. Validation & Compliance (8 scripts)
| Script | Purpose | sys.path Issues | Integration Target | Status |
|--------|---------|-----------------|-------------------|---------|
| `validate_compliance_assets.py` | Validate compliance docs | ✅ sys.path.insert(0, str(ROOT)) at line 12-13 | → `unified-workflow/automation/compliance_validator.py` | HIGH PRIORITY |
| `validate_prd_gate.py` | PRD gate validation | ✅ Uses sys.path.insert | → `unified-workflow/automation/validation_gates.py` | HIGH PRIORITY |
| `validate_tasks.py` | Task validation | ✅ Uses sys.path.insert | → `unified-workflow/automation/validation_gates.py` | MEDIUM |
| `validate_workflows.py` | Workflow validation | ❌ Clean imports | → `unified-workflow/automation/validation_gates.py` | LOW |
| `check_compliance_docs.py` | Check compliance structure | ❌ Clean imports | → `unified-workflow/automation/compliance_validator.py` | LOW |
| `check_hipaa.py` | HIPAA compliance checks | ❌ Clean imports | → `unified-workflow/automation/compliance_validator.py` | LOW |
| `enforce_gates.py` | Enforce quality gates | ❌ Clean imports | → `unified-workflow/automation/quality_gates.py` | MEDIUM |
| `test_policy_decisions.py` | Test policy router | ❌ Clean imports | → `unified-workflow/automation/policy_validator.py` | LOW |

### 4. Workflow Orchestration (7 scripts + package)
| Script | Purpose | sys.path Issues | Integration Target | Status |
|--------|---------|-----------------|-------------------|---------|
| `run_workflow.py` | Main workflow entry | ✅ Uses sys.path.insert | → CLI compatibility layer | HIGH PRIORITY |
| `workflow_automation/` (package) | Core orchestration | ❌ Clean (proper package) | → Direct integration | HIGH PRIORITY |
| `workflow_automation/orchestrator.py` | Orchestration logic | ❌ Clean imports | → `unified-workflow/automation/ai_orchestrator.py` | HIGH PRIORITY |
| `workflow_automation/config.py` | Config management | ❌ Clean imports | → `unified-workflow/config/` | MEDIUM |
| `workflow_automation/context.py` | Execution context | ❌ Clean imports | → `unified-workflow/automation/context.py` | MEDIUM |
| `workflow_automation/evidence.py` | Evidence utilities | ❌ Clean imports | → Merge with `evidence_manager.py` | HIGH PRIORITY |
| `workflow_automation/exceptions.py` | Exception hierarchy | ❌ Clean imports | → `unified-workflow/automation/exceptions.py` | LOW |
| `workflow_automation/gates/` | Gate implementations | ❌ Clean imports | → `unified-workflow/automation/quality_gates.py` | HIGH PRIORITY |

### 5. Analysis & Reporting (8 scripts)
| Script | Purpose | sys.path Issues | Integration Target | Status |
|--------|---------|-----------------|-------------------|---------|
| `aggregate_coverage.py` | Combine coverage reports | ❌ Clean imports | → `unified-workflow/automation/coverage_aggregator.py` | LOW |
| `collect_coverage.py` | Run pytest coverage | ❌ Clean imports | → `unified-workflow/automation/test_runner.py` | LOW |
| `collect_perf.py` | Collect performance metrics | ❌ Clean imports | → `unified-workflow/automation/perf_collector.py` | LOW |
| `evidence_report.py` | Consolidate evidence | ❌ Clean imports | → `unified-workflow/automation/evidence_manager.py` | MEDIUM |
| `write_context_report.py` | Generate context reports | ❌ Clean imports | → `unified-workflow/automation/report_generator.py` | LOW |
| `analyze_project_rules.py` | Analyze Cursor rules | ❌ Clean imports | → Keep standalone | LOW |
| `rules_audit_quick.py` | Quick rules audit | ❌ Clean imports | → Keep standalone | LOW |
| `router_benchmark.py` | Benchmark router | ❌ Clean imports | → Keep standalone | LOW |

### 6. Deployment & Operations (6 scripts)
| Script | Purpose | sys.path Issues | Integration Target | Status |
|--------|---------|-----------------|-------------------|---------|
| `deploy_backend.sh` | Deploy backend | N/A (shell) | → Keep as shell wrapper | LOW |
| `rollback_backend.sh` | Rollback backend | N/A (shell) | → Keep as shell wrapper | LOW |
| `rollback_frontend.sh` | Rollback frontend | N/A (shell) | → Keep as shell wrapper | LOW |
| `e2e_from_brief.sh` | E2E generation | N/A (shell) | → Wrap in Python | MEDIUM |
| `build_submission_pack.sh` | Build submission | N/A (shell) | → Keep as shell wrapper | LOW |
| `install_and_test.sh` | Install and test | N/A (shell) | → Keep as shell wrapper | LOW |

### 7. Utilities & Maintenance (7 scripts)
| Script | Purpose | sys.path Issues | Integration Target | Status |
|--------|---------|-----------------|-------------------|---------|
| `doctor.py` | Environment diagnostics | ❌ Clean imports | → Keep standalone | LOW |
| `benchmark_generation.py` | Benchmark generator | ❌ Clean imports | → Keep standalone | LOW |
| `backup_workflows.py` | Backup workflows | ❌ Clean imports | → `unified-workflow/automation/backup_manager.py` | LOW |
| `restore_workflows.py` | Restore workflows | ❌ Clean imports | → `unified-workflow/automation/backup_manager.py` | LOW |
| `sync_from_scaffold.py` | Sync from scaffold | ❌ Clean imports | → Keep standalone | LOW |
| `normalize_project_rules.py` | Normalize rules | ❌ Clean imports | → Keep standalone | LOW |
| `optimize_project_rules.py` | Optimize rules | ❌ Clean imports | → Keep standalone | LOW |

## sys.path Manipulation Summary

### Scripts Using sys.path.insert (9 scripts - HIGH PRIORITY)
1. `validate_compliance_assets.py` - Line 12-13: `sys.path.insert(0, str(ROOT))`
2. `generate_client_project.py` - Similar pattern
3. `generate_from_brief.py` - Similar pattern
4. `bootstrap_project.py` - Similar pattern
5. `plan_from_brief.py` - Similar pattern
6. `pre_lifecycle_plan.py` - Similar pattern
7. `validate_prd_gate.py` - Similar pattern
8. `validate_tasks.py` - Similar pattern
9. `run_workflow.py` - Similar pattern

### Fix Strategy
1. **Immediate**: Add `scripts/__init__.py` ✅ DONE
2. **Phase 1**: Create adapter modules in `unified-workflow/automation/` that handle imports properly
3. **Phase 2**: Refactor scripts to use proper package imports
4. **Phase 3**: Deprecate direct script execution in favor of unified CLI

## Integration Priority Matrix

### HIGH PRIORITY (Must fix for basic functionality)
- `generate_client_project.py` → project_generator.py
- `generate_from_brief.py` → brief_processor.py
- `plan_from_brief.py` → brief_processor.py
- `validate_compliance_assets.py` → compliance_validator.py
- `run_workflow.py` → CLI compatibility layer
- `workflow_automation/` package → Direct integration
- Evidence schema conflict resolution

### MEDIUM PRIORITY (Important for full functionality)
- Planning and task management scripts
- Workflow configuration and context
- Evidence reporting
- E2E automation wrapper

### LOW PRIORITY (Can remain standalone or defer)
- Analysis and reporting utilities
- Shell script wrappers
- Maintenance utilities
- Benchmark and diagnostic tools
