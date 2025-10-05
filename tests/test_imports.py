#!/usr/bin/env python3
"""Test script to validate import resolution across all modules.

This script tests that all imports work properly without sys.path manipulation.
"""

import sys
import traceback
from pathlib import Path

def test_import(module_name: str, description: str) -> bool:
    """Test if a module can be imported successfully."""
    try:
        __import__(module_name)
        print(f"✅ {description}: {module_name}")
        return True
    except Exception as e:
        print(f"❌ {description}: {module_name} - {e}")
        return False

def test_script_import(script_path: str, description: str) -> bool:
    """Test if a script can be imported as a module."""
    try:
        module_name = f"scripts.{script_path.replace('/', '.').replace('.py', '')}"
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
    if test_import("project_generator.core.generator", "ProjectGenerator"):
        success_count += 1

    total_tests += 1
    if test_import("project_generator.core.validator", "ProjectValidator"):
        success_count += 1

    total_tests += 1
    if test_import("project_generator.core.industry_config", "IndustryConfig"):
        success_count += 1

    total_tests += 1
    if test_import("project_generator.core.brief_parser", "BriefParser"):
        success_count += 1

    total_tests += 1
    if test_import("project_generator.templates.registry", "TemplateRegistry"):
        success_count += 1

    # Test 2: Scripts package imports
    print("\n2. Scripts Package Imports:")
    print("-" * 40)
    total_tests += 1
    if test_import("scripts.lifecycle_tasks", "lifecycle_tasks"):
        success_count += 1

    total_tests += 1
    if test_import("scripts.workflow_automation", "workflow_automation"):
        success_count += 1

    total_tests += 1
    if test_import("scripts.workflow_automation.config", "workflow_automation.config"):
        success_count += 1

    total_tests += 1
    if test_import("scripts.workflow_automation.orchestrator", "workflow_automation.orchestrator"):
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
        if test_script_import(script, f"Script {script}"):
            success_count += 1

    # Test 4: Adapter imports
    print("\n4. Adapter Imports:")
    print("-" * 40)
    total_tests += 1
    if test_import("unified_workflow.automation.adapters.project_generator_adapter", "Project Generator Adapter"):
        success_count += 1

    total_tests += 1
    if test_import("unified_workflow.automation.adapters.workflow_automation_adapter", "Workflow Automation Adapter"):
        success_count += 1

    total_tests += 1
    if test_import("unified_workflow.automation.adapters.lifecycle_tasks_adapter", "Lifecycle Tasks Adapter"):
        success_count += 1

    # Test 5: Unified workflow core imports
    print("\n5. Unified Workflow Core Imports:")
    print("-" * 40)
    total_tests += 1
    if test_import("unified_workflow.core.template_registry", "Template Registry"):
        success_count += 1

    total_tests += 1
    if test_import("unified_workflow.automation.evidence_schema_converter", "Evidence Schema Converter"):
        success_count += 1

    # Test 6: Existing unified workflow imports
    print("\n6. Existing Unified Workflow Imports:")
    print("-" * 40)
    total_tests += 1
    if test_import("unified_workflow.automation.ai_orchestrator", "AI Orchestrator"):
        success_count += 1

    total_tests += 1
    if test_import("unified_workflow.automation.evidence_manager", "Evidence Manager"):
        success_count += 1

    total_tests += 1
    if test_import("unified_workflow.automation.quality_gates", "Quality Gates"):
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

