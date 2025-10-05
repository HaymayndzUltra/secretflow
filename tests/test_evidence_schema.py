#!/usr/bin/env python3
"""Test script to validate evidence schema conversion between legacy and unified formats."""

import json
import tempfile
from pathlib import Path

def create_sample_legacy_evidence():
    """Create sample legacy evidence for testing."""
    return [
        {
            "path": "docs/README.md",
            "category": "documentation",
            "description": "Project readme file",
            "checksum": "abc123def456",
            "created_at": "2025-01-01T00:00:00Z"
        },
        {
            "path": "src/main.py",
            "category": "source_code",
            "description": "Main application file",
            "checksum": "def789ghi012",
            "created_at": "2025-01-01T00:01:00Z"
        },
        {
            "path": "tests/test_main.py",
            "category": "test_code",
            "description": "Unit tests for main module",
            "checksum": "ghi345jkl678",
            "created_at": "2025-01-01T00:02:00Z"
        }
    ]

def create_sample_unified_evidence():
    """Create sample unified evidence for testing."""
    return {
        "manifest": {
            "artifacts": [
                {
                    "path": "docs/README.md",
                    "category": "documentation",
                    "description": "Project readme file",
                    "checksum": "abc123def456",
                    "created_at": "2025-01-01T00:00:00Z",
                    "phase": 0
                },
                {
                    "path": "src/main.py",
                    "category": "source_code",
                    "description": "Main application file",
                    "checksum": "def789ghi012",
                    "created_at": "2025-01-01T00:01:00Z",
                    "phase": 1
                }
            ],
            "metadata": {
                "project_name": "test-project",
                "workflow_version": "1.0.0",
                "generated_at": "2025-01-01T00:00:00Z",
                "total_artifacts": 2
            }
        },
        "run_log": {
            "entries": [
                {
                    "timestamp": "2025-01-01T00:00:00Z",
                    "phase": 0,
                    "action": "bootstrap",
                    "status": "completed",
                    "details": {"duration": "5s"}
                }
            ],
            "metadata": {
                "project_name": "test-project",
                "workflow_version": "1.0.0",
                "total_entries": 1,
                "last_updated": "2025-01-01T00:00:00Z"
            }
        },
        "validation": {
            "phases": [
                {
                    "phase": 0,
                    "status": "passed",
                    "score": 8.5,
                    "findings": [],
                    "recommendations": [],
                    "validated_at": "2025-01-01T00:00:00Z"
                }
            ],
            "metadata": {
                "project_name": "test-project",
                "workflow_version": "1.0.0",
                "total_phases": 1,
                "overall_score": 8.5,
                "last_updated": "2025-01-01T00:00:00Z"
            }
        }
    }

def test_evidence_schema_converter():
    """Test evidence schema conversion functionality."""
    print("🔍 Testing evidence schema conversion...")
    print("=" * 60)

    try:
        # Import the converter
        from unified_workflow.automation.evidence_schema_converter import EvidenceSchemaConverter

        print("✅ EvidenceSchemaConverter imported successfully")

        # Test 1: Legacy to Unified conversion
        print("\n1. Testing Legacy → Unified Conversion:")
        print("-" * 50)

        legacy_evidence = create_sample_legacy_evidence()
        print(f"Legacy evidence: {len(legacy_evidence)} artifacts")

        unified_evidence = EvidenceSchemaConverter.legacy_to_unified(
            legacy_evidence,
            project_name="test-project",
            workflow_version="1.0.0",
            phase=0
        )

        print("✅ Legacy → Unified conversion completed")

        # Validate unified structure
        assert "manifest" in unified_evidence
        assert "run_log" in unified_evidence
        assert "validation" in unified_evidence

        # Check manifest
        manifest = unified_evidence["manifest"]
        assert manifest["metadata"]["project_name"] == "test-project"
        assert len(manifest["artifacts"]) == len(legacy_evidence)
        assert manifest["metadata"]["total_artifacts"] == len(legacy_evidence)

        # Check that artifacts have phase information
        for artifact in manifest["artifacts"]:
            assert "phase" in artifact
            assert artifact["phase"] == 0

        # Check run log
        run_log = unified_evidence["run_log"]
        assert len(run_log["entries"]) == 1
        assert run_log["entries"][0]["action"] == "legacy_evidence_migration"

        # Check validation
        validation = unified_evidence["validation"]
        assert len(validation["phases"]) == 1
        assert validation["phases"][0]["status"] == "passed"

        print("✅ Unified evidence structure validated")

        # Test 2: Unified to Legacy conversion
        print("\n2. Testing Unified → Legacy Conversion:")
        print("-" * 50)

        legacy_from_unified = EvidenceSchemaConverter.unified_to_legacy(unified_evidence)

        print(f"✅ Unified → Legacy conversion completed: {len(legacy_from_unified)} artifacts")

        # Validate legacy structure
        assert len(legacy_from_unified) == len(legacy_evidence)

        # Check that phase information is removed (not in legacy format)
        for artifact in legacy_from_unified:
            assert "phase" not in artifact
            # But original fields should be preserved
            assert "path" in artifact
            assert "category" in artifact
            assert "description" in artifact
            assert "checksum" in artifact
            assert "created_at" in artifact

        print("✅ Legacy evidence structure validated")

        # Test 3: Round-trip conversion (legacy → unified → legacy)
        print("\n3. Testing Round-trip Conversion:")
        print("-" * 50)

        # Convert back to unified from the legacy we just created
        unified_again = EvidenceSchemaConverter.legacy_to_unified(
            legacy_from_unified,
            project_name="test-project-roundtrip",
            workflow_version="1.0.0",
            phase=1
        )

        # Convert back to legacy
        legacy_final = EvidenceSchemaConverter.unified_to_legacy(unified_again)

        print("✅ Round-trip conversion completed")

        # Validate that we get back what we started with (minus phase info)
        assert len(legacy_final) == len(legacy_evidence)
        for original, final in zip(legacy_evidence, legacy_final):
            assert original["path"] == final["path"]
            assert original["category"] == final["category"]
            assert original["description"] == final["description"]
            assert original["checksum"] == final["checksum"]
            assert original["created_at"] == final["created_at"]

        print("✅ Round-trip conversion validated")

        # Test 4: File I/O operations
        print("\n4. Testing File I/O Operations:")
        print("-" * 50)

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            # Save unified evidence to file
            unified_file = temp_path / "unified_evidence.json"
            with open(unified_file, 'w') as f:
                json.dump(unified_evidence, f, indent=2)

            # Load it back
            with open(unified_file, 'r') as f:
                loaded_unified = json.load(f)

            # Convert to legacy
            legacy_from_file = EvidenceSchemaConverter.unified_to_legacy(loaded_unified)

            print(f"✅ File I/O operations completed: {len(legacy_from_file)} artifacts")

            # Validate loaded data matches original
            assert len(legacy_from_file) == len(legacy_evidence)

        print("✅ File I/O operations validated")

        return True

    except Exception as e:
        print(f"❌ Evidence schema conversion test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main test function."""
    success = test_evidence_schema_converter()

    print("\n" + "=" * 60)
    if success:
        print("🎉 Evidence schema conversion tests passed!")
        return 0
    else:
        print("❌ Evidence schema conversion tests failed!")
        return 1

if __name__ == "__main__":
    exit(main())

