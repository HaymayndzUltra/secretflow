#!/usr/bin/env python3
"""Unified Project Generator Adapter

This module provides a unified interface for project generation, integrating
the existing project_generator components with the unified workflow system.
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Union

# Add repo root to path for project_generator imports
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

# Import project_generator components using clean imports
from project_generator.core.generator import ProjectGenerator
from project_generator.core.validator import ProjectValidator
from project_generator.core.industry_config import IndustryConfig

# Import unified template registry for template access
from unified_workflow.core.template_registry import get_registry

logger = logging.getLogger(__name__)


class UnifiedProjectGenerator:
    """Unified project generator with integrated template registry and validation."""

    def __init__(self):
        """Initialize the unified project generator."""
        self.project_generator = None
        self.validator = None
        self.template_registry = get_registry()

        # Initialize template registry
        self.template_registry.initialize()

        logger.info("UnifiedProjectGenerator initialized with template registry")

    def create_project(
        self,
        name: str,
        industry: str,
        project_type: str,
        frontend: str,
        backend: str,
        database: str,
        output_dir: Optional[Union[str, Path]] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """Create a new project using the unified interface.

        Args:
            name: Project name
            industry: Industry type (saas, fintech, healthcare, etc.)
            project_type: Project type (fullstack, backend-only, frontend-only)
            frontend: Frontend framework (nextjs, react, vue, angular)
            backend: Backend framework (fastapi, django, nestjs, go)
            database: Database (postgres, mongodb, firebase)
            output_dir: Output directory (default: generated_projects/)
            **kwargs: Additional configuration options

        Returns:
            Project generation results
        """
        try:
            logger.info(f"Creating project: {name} ({industry} {project_type})")

            # Set default output directory
            if output_dir is None:
                output_dir = Path("generated_projects") / name
            else:
                output_dir = Path(output_dir)

            # Create output directory
            output_dir.mkdir(parents=True, exist_ok=True)

            # Create project configuration
            project_config = {
                "name": name,
                "industry": industry,
                "project_type": project_type,
                "frontend": frontend,
                "backend": backend,
                "database": database,
                "output_dir": str(output_dir),
                **kwargs
            }

            # Initialize project generator with industry config and unified template registry
            industry_config = IndustryConfig(industry)

            # Create args object for project generator (matching working direct test)
            from argparse import Namespace

            args = Namespace()
            args.name = name
            args.industry = industry
            args.project_type = project_type
            args.frontend = frontend
            args.backend = backend
            args.database = database
            args.auth = kwargs.get('auth', 'auth0')
            args.deploy = kwargs.get('deploy', 'vercel')
            args.compliance = kwargs.get('compliance', '')
            args.features = kwargs.get('features', '')
            args.output_dir = str(output_dir)
            args.no_git = kwargs.get('no_git', True)
            args.no_install = kwargs.get('no_install', True)
            args.workers = kwargs.get('workers', 2)
            args.force = kwargs.get('force', False)
            args.no_cursor_assets = kwargs.get('no_cursor_assets', False)
            args.minimal_cursor = kwargs.get('minimal_cursor', False)
            args.rules_manifest = kwargs.get('rules_manifest', None)
            args.nestjs_orm = kwargs.get('nestjs_orm', 'typeorm')

            self.project_generator = ProjectGenerator(
                args=args,
                config=industry_config,
                template_registry=self.template_registry  # Use unified template registry
            )

            # Generate project using project generator
            generation_result = self.project_generator.generate()

            # Validate generated project (if validator supports it)
            validation_result = None
            if self.validator is None:
                self.validator = ProjectValidator()

            # Try different validation methods
            if hasattr(self.validator, 'validate'):
                validation_result = self.validator.validate(str(output_dir))
            elif hasattr(self.validator, 'validate_configuration'):
                # Create a mock args object for configuration validation
                from argparse import Namespace
                mock_args = Namespace(
                    name=name,
                    industry=industry,
                    project_type=project_type,
                    frontend=frontend,
                    backend=backend,
                    database=database,
                    output_dir=str(output_dir)
                )
                validation_result = self.validator.validate_configuration(mock_args)
            else:
                # Simple structural validation
                validation_result = self._validate_project_structure(output_dir)

            # Combine results
            result = {
                "success": True,
                "project_name": name,
                "project_path": str(output_dir),
                "generation": generation_result,
                "validation": validation_result,
                "templates_used": self._get_templates_used(project_config),
                "artifacts": self._list_generated_artifacts(output_dir)
            }

            logger.info(f"Project {name} created successfully at {output_dir}")
            return result

        except Exception as e:
            logger.error(f"Project creation failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "project_name": name
            }

    def _get_templates_used(self, project_config: Dict[str, Any]) -> List[str]:
        """Get list of templates used for the project."""
        templates = []

        # Frontend template
        if project_config.get("frontend"):
            templates.append(f"frontend/{project_config['frontend']}")

        # Backend template
        if project_config.get("backend"):
            templates.append(f"backend/{project_config['backend']}")

        # Database template
        if project_config.get("database"):
            templates.append(f"database/{project_config['database']}")

        return templates

    def _list_generated_artifacts(self, project_dir: Path) -> List[Dict[str, Any]]:
        """List all artifacts generated in the project directory."""
        artifacts = []

        if not project_dir.exists():
            return artifacts

        for file_path in project_dir.rglob("*"):
            if file_path.is_file():
                artifacts.append({
                    "path": str(file_path.relative_to(project_dir)),
                    "size": file_path.stat().st_size,
                    "type": self._categorize_file(file_path)
                })

        return artifacts

    def _categorize_file(self, file_path: Path) -> str:
        """Categorize a file based on its path and extension."""
        path_str = str(file_path)

        if "src" in path_str or "lib" in path_str:
            if file_path.suffix in [".js", ".ts", ".jsx", ".tsx", ".py"]:
                return "source_code"
            elif file_path.suffix in [".css", ".scss", ".less"]:
                return "styles"
        elif "test" in path_str or "spec" in path_str:
            return "test_code"
        elif "docs" in path_str or file_path.suffix in [".md", ".txt"]:
            return "documentation"
        elif "package.json" in path_str or "requirements.txt" in path_str:
            return "dependencies"
        elif file_path.suffix in [".json", ".yaml", ".yml"]:
            return "configuration"

        return "other"

    def _validate_project_structure(self, project_dir: Path) -> Dict[str, Any]:
        """Perform basic structural validation of the generated project.

        Args:
            project_dir: Path to the project directory

        Returns:
            Validation results
        """
        if not project_dir.exists():
            return {
                "success": False,
                "errors": [f"Project directory does not exist: {project_dir}"],
                "warnings": []
            }

        errors = []
        warnings = []

        # Check for essential directories based on project type
        artifacts = self._list_generated_artifacts(project_dir)

        # Basic checks
        if len(artifacts) == 0:
            errors.append("No files generated in project directory")
        else:
            # Check for key files based on technology stack
            has_package_json = any(a["path"] == "package.json" for a in artifacts)
            has_requirements_txt = any(a["path"] == "requirements.txt" for a in artifacts)
            has_readme = any(a["path"].endswith("README.md") for a in artifacts)

            if not has_readme:
                warnings.append("No README.md found in project")

            # Check for source directories
            has_frontend = any("frontend" in a["path"] for a in artifacts)
            has_backend = any("backend" in a["path"] for a in artifacts)

            if not has_frontend and not has_backend:
                warnings.append("No frontend or backend directories found")

        return {
            "success": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
            "artifact_count": len(artifacts),
            "validation_type": "structural"
        }

    def validate_project(self, project_path: Union[str, Path]) -> Dict[str, Any]:
        """Validate an existing project.

        Args:
            project_path: Path to the project directory

        Returns:
            Validation results
        """
        try:
            project_path = Path(project_path)

            if not project_path.exists():
                return {
                    "success": False,
                    "error": f"Project directory does not exist: {project_path}"
                }

            if self.validator is None:
                self.validator = ProjectValidator()

            validation_result = self.validator.validate(str(project_path))

            return {
                "success": True,
                "project_path": str(project_path),
                "validation": validation_result
            }

        except Exception as e:
            logger.error(f"Project validation failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "project_path": str(project_path)
            }

    def list_available_templates(self) -> List[Dict[str, Any]]:
        """List all available templates from the unified registry.

        Returns:
            List of template information
        """
        try:
            templates = self.template_registry.list_templates()

            result = []
            for template in templates:
                result.append({
                    "type": template.type.value,
                    "name": template.name,
                    "path": str(template.path),
                    "variants": template.variants,
                    "engines": template.engines
                })

            return result

        except Exception as e:
            logger.error(f"Failed to list templates: {e}")
            return []

    def get_template_info(self, template_type: str, template_name: str) -> Optional[Dict[str, Any]]:
        """Get information about a specific template.

        Args:
            template_type: Type of template (frontend, backend, database)
            template_name: Name of the template

        Returns:
            Template information or None if not found
        """
        try:
            template = self.template_registry.get_template(template_type, template_name)

            if template:
                return {
                    "type": template.type.value,
                    "name": template.name,
                    "path": str(template.path),
                    "variants": template.variants,
                    "engines": template.engines
                }

            return None

        except Exception as e:
            logger.error(f"Failed to get template info: {e}")
            return None


# Convenience function for quick project creation
def create_project(
    name: str,
    industry: str,
    project_type: str,
    frontend: str,
    backend: str,
    database: str,
    output_dir: Optional[Union[str, Path]] = None,
    **kwargs
) -> Dict[str, Any]:
    """Create a project using the unified interface.

    Args:
        name: Project name
        industry: Industry type
        project_type: Project type
        frontend: Frontend framework
        backend: Backend framework
        database: Database type
        output_dir: Output directory
        **kwargs: Additional options

    Returns:
        Project creation results
    """
    generator = UnifiedProjectGenerator()
    return generator.create_project(
        name=name,
        industry=industry,
        project_type=project_type,
        frontend=frontend,
        backend=backend,
        database=database,
        output_dir=output_dir,
        **kwargs
    )


# CLI interface for testing
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Unified Project Generator")
    parser.add_argument("--name", required=True, help="Project name")
    parser.add_argument("--industry", required=True, help="Industry type")
    parser.add_argument("--type", required=True, help="Project type")
    parser.add_argument("--frontend", required=True, help="Frontend framework")
    parser.add_argument("--backend", required=True, help="Backend framework")
    parser.add_argument("--database", required=True, help="Database type")
    parser.add_argument("--output", help="Output directory")

    args = parser.parse_args()

    result = create_project(
        name=args.name,
        industry=args.industry,
        project_type=args.type,
        frontend=args.frontend,
        backend=args.backend,
        database=args.database,
        output_dir=args.output
    )

    if result["success"]:
        print(f"✅ Project {args.name} created successfully!")
        print(f"📁 Location: {result['project_path']}")
        print(f"📋 Artifacts: {len(result['artifacts'])} files generated")
    else:
        print(f"❌ Project creation failed: {result['error']}")
        exit(1)

