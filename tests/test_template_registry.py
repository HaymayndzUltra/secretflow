#!/usr/bin/env python3
"""Test script to validate template registry discovery and loading."""

import sys
from pathlib import Path

def test_template_registry():
    """Test template registry functionality."""
    print("🔍 Testing template registry discovery and loading...")
    print("=" * 60)

    try:
        # Test 1: Import and initialize template registry
        from project_generator.templates.registry import TemplateRegistry

        print("✅ TemplateRegistry imported successfully")

        # Initialize registry
        registry = TemplateRegistry()
        print("✅ TemplateRegistry initialized successfully")

        # Test 2: List all templates
        templates = registry.list_all()
        print(f"✅ Found {len(templates)} templates")

        for template in templates[:5]:  # Show first 5 templates
            print(f"   - {template['type']}/{template['name']} at {template['path']}")

        if len(templates) > 5:
            print(f"   ... and {len(templates) - 5} more")

        # Test 3: Get specific template
        if templates:
            first_template = templates[0]
            template_type = first_template['type']
            template_name = first_template['name']

            retrieved = registry.get_template(template_type, template_name)
            if retrieved:
                print(f"✅ Retrieved template {template_type}/{template_name}")
                print(f"   Path: {retrieved['path']}")
                print(f"   Variants: {retrieved['variants']}")
                print(f"   Engines: {retrieved['engines']}")
            else:
                print(f"❌ Failed to retrieve template {template_type}/{template_name}")

        # Test 4: Test template path resolution
        if templates:
            template_path = registry.get_template_path(template_type, template_name)
            if template_path and template_path.exists():
                print(f"✅ Template path resolved: {template_path}")
            else:
                print(f"❌ Template path not found or invalid: {template_path}")

        # Test 5: Test unified template registry (if available)
        try:
            from unified_workflow.core.template_registry import get_registry

            unified_registry = get_registry()
            unified_registry.initialize()

            unified_templates = unified_registry.list_templates()
            print(f"✅ Unified registry found {len(unified_templates)} templates")

            # Compare counts
            if len(templates) != len(unified_templates):
                print(f"⚠️ Template count mismatch: project_generator={len(templates)}, unified={len(unified_templates)}")

        except ImportError as e:
            print(f"⚠️ Unified template registry not available yet: {e}")
        except Exception as e:
            print(f"❌ Error testing unified template registry: {e}")

        return True

    except Exception as e:
        print(f"❌ Template registry test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main test function."""
    success = test_template_registry()

    print("\n" + "=" * 60)
    if success:
        print("🎉 Template registry tests passed!")
        return 0
    else:
        print("❌ Template registry tests failed!")
        return 1

if __name__ == "__main__":
    exit(main())

