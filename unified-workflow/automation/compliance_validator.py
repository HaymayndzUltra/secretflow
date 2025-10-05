"""Unified compliance validation module.

This module integrates compliance validation from the legacy scripts
and provides a clean interface for the unified workflow.
"""

from __future__ import annotations

import difflib
from pathlib import Path
from types import SimpleNamespace
from typing import Dict, Optional, Tuple

# Import project generator components using proper package imports
# Since we're in unified-workflow, we need to go up to access project_generator
import sys
root_path = Path(__file__).resolve().parents[2]
if str(root_path) not in sys.path:
    sys.path.append(str(root_path))

from project_generator.core.generator import ProjectGenerator
from project_generator.core.industry_config import IndustryConfig
from project_generator.core.validator import ProjectValidator


class ComplianceValidator:
    """Validates compliance documentation and gate configurations."""
    
    DEFAULT_STACK = {
        "name": "portfolio-dashboard",
        "industry": "saas",
        "project_type": "fullstack",
        "frontend": "nextjs",
        "backend": "fastapi",
        "database": "postgres",
        "auth": "auth0",
        "deploy": "vercel",
        "compliance": "gdpr",
    }
    
    def __init__(self, root_path: Optional[Path] = None):
        """Initialize the compliance validator.
        
        Args:
            root_path: Root path of the project. If None, uses parent of unified-workflow.
        """
        self.root = root_path or Path(__file__).resolve().parents[2]
        self.generator = self._build_generator()
    
    def _build_generator(self) -> ProjectGenerator:
        """Build a project generator instance with default configuration."""
        args = SimpleNamespace(
            **self.DEFAULT_STACK,
            features="",
            output_dir=".",
            no_git=True,
            no_install=True,
            include_cursor_assets=False,
            no_cursor_assets=True,
            minimal_cursor=False,
            rules_manifest=None,
            rules_mode="auto",
            include_project_rules=False,
            workers=2,
            category="example",
            skip_system_checks=True,
            force=False,
        )
        validator = ProjectValidator()
        config = IndustryConfig(args.industry)
        return ProjectGenerator(args, validator, config)
    
    def validate_compliance_docs(self, write: bool = False) -> Tuple[bool, Dict[str, str]]:
        """Validate compliance documentation against generator output.
        
        Args:
            write: If True, update files with generator output instead of just checking.
            
        Returns:
            Tuple of (all_valid, results_dict) where results_dict contains
            validation status and diffs for each file.
        """
        results = {}
        all_valid = True
        
        # Generate expected content
        compliance_doc = self.generator._generate_compliance_documentation().strip() + "\n"
        gates_yaml = self.generator._generate_gates_config()
        
        # Define paths
        compliance_path = self.root / "docs" / "COMPLIANCE.md"
        gates_path = self.root / "gates_config.yaml"
        
        # Validate compliance doc
        doc_valid, doc_diff = self._compare_file(
            compliance_path, compliance_doc, write, "COMPLIANCE.md"
        )
        results["compliance_doc"] = {
            "valid": doc_valid,
            "path": str(compliance_path),
            "diff": doc_diff
        }
        all_valid &= doc_valid
        
        # Validate gates config
        gates_valid, gates_diff = self._compare_file(
            gates_path, gates_yaml, write, "gates_config.yaml"
        )
        results["gates_config"] = {
            "valid": gates_valid,
            "path": str(gates_path),
            "diff": gates_diff
        }
        all_valid &= gates_valid
        
        return all_valid, results
    
    def _compare_file(self, path: Path, expected: str, write: bool, name: str) -> Tuple[bool, Optional[str]]:
        """Compare file content with expected and optionally update.
        
        Args:
            path: Path to the file to check
            expected: Expected content
            write: If True, write expected content to file
            name: Name for logging
            
        Returns:
            Tuple of (is_valid, diff_text)
        """
        current = path.read_text(encoding="utf-8") if path.exists() else ""
        
        if current == expected:
            print(f"[COMPLIANCE] {name} is up to date.")
            return True, None
        
        if write:
            path.write_text(expected, encoding="utf-8")
            print(f"[COMPLIANCE] Updated {name} from generator output.")
            return True, None
        
        print(f"[COMPLIANCE] Drift detected in {name} (run with --write to update).")
        diff = list(difflib.unified_diff(
            current.splitlines(),
            expected.splitlines(),
            fromfile=str(path),
            tofile="generator",
        ))
        diff_text = "\n".join(diff)
        return False, diff_text
    
    def validate_hipaa_compliance(self) -> Tuple[bool, Dict[str, any]]:
        """Run HIPAA-specific compliance checks.
        
        Returns:
            Tuple of (is_compliant, check_results)
        """
        # This would integrate check_hipaa.py logic
        # For now, return placeholder
        return True, {"status": "Not implemented yet"}
    
    def validate_soc2_compliance(self) -> Tuple[bool, Dict[str, any]]:
        """Run SOC2-specific compliance checks.
        
        Returns:
            Tuple of (is_compliant, check_results)
        """
        # Placeholder for SOC2 validation
        return True, {"status": "Not implemented yet"}
    
    def validate_pci_compliance(self) -> Tuple[bool, Dict[str, any]]:
        """Run PCI-specific compliance checks.
        
        Returns:
            Tuple of (is_compliant, check_results)
        """
        # Placeholder for PCI validation
        return True, {"status": "Not implemented yet"}


# CLI compatibility function for direct script replacement
def main() -> int:
    """CLI entry point for backward compatibility with validate_compliance_assets.py."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Validate that compliance docs and gate config match generator output."
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Rewrite compliance assets instead of exiting with an error when drift is detected.",
    )
    args = parser.parse_args()
    
    validator = ComplianceValidator()
    all_valid, results = validator.validate_compliance_docs(write=args.write)
    
    # Print any diffs
    for name, result in results.items():
        if not result["valid"] and result.get("diff"):
            print(result["diff"])
    
    return 0 if all_valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
