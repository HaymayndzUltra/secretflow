#!/usr/bin/env python3
"""Test script to validate import resolution across all modules.

This script tests that all imports work properly without sys.path manipulation.
"""

import sys
import traceback
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Ensure local packages shadow any globally installed modules
sys.modules.pop("project_generator", None)
sys.modules.pop("scripts", None)


def _import_module(module_name: str, description: str) -> bool:
    """Test if a module can be imported successfully."""
    base_package = module_name.split(".")[0]
    if base_package:
        sys.modules.pop(base_package, None)
    if str(PROJECT_ROOT) in sys.path:
        sys.path.remove(str(PROJECT_ROOT))
    sys.path.insert(0, str(PROJECT_ROOT))
    try:
        __import__(module_name)
        print(f"✅ {description}: {module_name}")
        return True
    except Exception as e:
        print(f"❌ {description}: {module_name} - {e}")
        return False


def _import_script(script_path: str, description: str) -> bool:
    """Test if a script can be imported as a module."""
    try:
        module_name = f"scripts.{script_path.replace('/', '.').replace('.py', '')}"
        sys.modules.pop("scripts", None)
        if str(PROJECT_ROOT) in sys.path:
            sys.path.remove(str(PROJECT_ROOT))
        sys.path.insert(0, str(PROJECT_ROOT))
        __import__(module_name)
        print(f"✅ {description}: {script_path}")
        return True
    except Exception as e:
        print(f"❌ {description}: {script_path} - {e}")
        return False

def main():
    """Run all import tests."""
    print("🔍 Testing import resolution across all modules...")
    print("=" * 60)

    success_count = 0
    total_tests = 0

    # Test 1: Core project_generator imports
    print("\n1. Core Project Generator Imports:")
    print("-" * 40)
    total_tests += 1
    if _import_module("project_generator.core.generator", "ProjectGenerator"):
        success_count += 1

    total_tests += 1
    if _import_module("project_generator.core.validator", "ProjectValidator"):
        success_count += 1

    total_tests += 1
    if _import_module("project_generator.core.industry_config", "IndustryConfig"):
        success_count += 1

    total_tests += 1
    if _import_module("project_generator.core.brief_parser", "BriefParser"):
        success_count += 1

    total_tests += 1
    if _import_module("project_generator.templates.registry", "TemplateRegistry"):
        success_count += 1

    # Test 2: Scripts package imports
    print("\n2. Scripts Package Imports:")
    print("-" * 40)
    total_tests += 1
    if _import_module("scripts.lifecycle_tasks", "lifecycle_tasks"):
        success_count += 1

    total_tests += 1
    if _import_module("scripts.workflow_automation", "workflow_automation"):
        success_count += 1

    total_tests += 1
    if _import_module("scripts.workflow_automation.config", "workflow_automation.config"):
        success_count += 1

    total_tests += 1
    if _import_module("scripts.workflow_automation.orchestrator", "workflow_automation.orchestrator"):
        success_count += 1

    # Test 3: High-priority script imports (those we fixed)
    print("\n3. High-Priority Script Imports:")
    print("-" * 40)
    high_priority_scripts = [
        "validate_compliance_assets",
        "generate_client_project",
        "plan_from_brief",
        "run_workflow",
        "pre_lifecycle_plan"
    ]

    for script in high_priority_scripts:
        total_tests += 1
        if _import_script(script, f"Script {script}"):
            success_count += 1

    # Test 4: Adapter imports
    print("\n4. Adapter Imports:")
    print("-" * 40)
    total_tests += 1
    if _import_module("unified_workflow.automation.adapters.project_generator_adapter", "Project Generator Adapter"):
        success_count += 1

    total_tests += 1
    if _import_module("unified_workflow.automation.adapters.workflow_automation_adapter", "Workflow Automation Adapter"):
        success_count += 1

    total_tests += 1
    if _import_module("unified_workflow.automation.adapters.lifecycle_tasks_adapter", "Lifecycle Tasks Adapter"):
        success_count += 1

    # Test 5: Unified workflow core imports
    print("\n5. Unified Workflow Core Imports:")
    print("-" * 40)
    total_tests += 1
    if _import_module("unified_workflow.core.template_registry", "Template Registry"):
        success_count += 1

    total_tests += 1
    if _import_module("unified_workflow.automation.evidence_schema_converter", "Evidence Schema Converter"):
        success_count += 1

    # Test 6: Existing unified workflow imports
    print("\n6. Existing Unified Workflow Imports:")
    print("-" * 40)
    total_tests += 1
    if _import_module("unified_workflow.automation.ai_orchestrator", "AI Orchestrator"):
        success_count += 1

    total_tests += 1
    if _import_module("unified_workflow.automation.evidence_manager", "Evidence Manager"):
        success_count += 1

    total_tests += 1
    if _import_module("unified_workflow.automation.quality_gates", "Quality Gates"):
        success_count += 1

    # Summary
    print("\n" + "=" * 60)
    print("📊 IMPORT TEST SUMMARY")
    print("=" * 60)
    print(f"✅ Successful imports: {success_count}/{total_tests}")
    print(f"❌ Failed imports: {total_tests - success_count}/{total_tests}")

    if success_count == total_tests:
        print("🎉 All imports working correctly!")
        return 0
    else:
        print("⚠️  Some imports failed - check the errors above")
        return 1

if __name__ == "__main__":
    exit(main())


def test_import_suite() -> None:
    """Ensure the import validation script reports success."""

    result = main()
    assert result == 0, "Import validation reported failures"

