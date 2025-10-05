from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Ensure the local project_generator package is used during tests
sys.modules.pop("project_generator", None)
_project_generator_pkg = importlib.import_module("project_generator")
assert hasattr(_project_generator_pkg, "__path__"), "Local project_generator package must be a namespace"

from unified_workflow.automation.compliance_validator import ComplianceValidator


@pytest.fixture()
def validator() -> ComplianceValidator:
    """Provide a compliance validator instance for tests."""

    return ComplianceValidator()


def test_generate_compliance_assets_creates_expected_files(
    validator: ComplianceValidator, tmp_path: Path
) -> None:
    """Compliance assets should be generated for all standards."""

    assets = validator.generate_compliance_assets(output_dir=tmp_path)

    expected_keys = {
        "documentation",
        "gates_config",
        "summary",
        "hipaa_report",
        "soc2_report",
        "pci_report",
    }
    assert expected_keys.issubset(assets.keys())

    for name, asset_path in assets.items():
        assert asset_path.exists(), f"Expected asset '{name}' to be created"

    hipaa_report = json.loads(assets["hipaa_report"].read_text(encoding="utf-8"))
    assert hipaa_report["valid"] is True
    assert hipaa_report["summary"]["failed"] == 0


def test_validate_hipaa_compliance_detects_failures(
    validator: ComplianceValidator,
) -> None:
    """HIPAA validation should surface failing controls when toggled off."""

    valid, report = validator.validate_hipaa_compliance(
        {"encryption_at_rest": False, "encryption_in_transit": True}
    )

    assert valid is False
    assert report["summary"]["failed"] >= 1

    status_by_id = {control["id"]: control["status"] for control in report["controls"]}
    assert status_by_id["HIPAA-01"] == "fail"
