"""Unified Template Registry - Single source of truth for all templates.

This module provides a consolidated template registry that serves both
the project_generator and unified-workflow systems, preventing template
divergence and ensuring consistency.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

logger = logging.getLogger(__name__)


class TemplateType(Enum):
    """Template categories."""
    BACKEND = "backend"
    FRONTEND = "frontend"
    DATABASE = "database"
    DEVEX = "devex"
    CICD = "cicd"
    POLICY_DSL = "policy-dsl"


@dataclass
class TemplateMetadata:
    """Metadata for a template."""
    name: str
    type: TemplateType
    path: Path
    variants: List[str] = field(default_factory=lambda: ["base"])
    engines: Optional[List[str]] = None
    version: str = "1.0.0"
    description: str = ""
    dependencies: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    manifest_data: Dict[str, Any] = field(default_factory=dict)


class UnifiedTemplateRegistry:
    """Unified template registry that consolidates all template sources.
    
    This registry serves as the single source of truth for templates,
    preventing divergence between project_generator and unified-workflow.
    """
    
    def __init__(self, root_path: Optional[Path] = None):
        """Initialize the unified template registry.
        
        Args:
            root_path: Root path of the project. If None, auto-detects.
        """
        self.root = root_path or self._find_root()
        self._templates: Dict[str, TemplateMetadata] = {}
        self._template_paths: Set[Path] = set()
        self._initialized = False
        
        # Define template search paths in priority order
        self.search_paths = [
            self.root / "template-packs",  # Top-level templates (primary)
            self.root / "project_generator" / "template-packs",  # Legacy location
            self.root / "unified-workflow" / "templates",  # Unified workflow templates
        ]
    
    def _find_root(self) -> Path:
        """Find the project root directory."""
        current = Path(__file__).resolve()
        while current.parent != current:
            if (current / "README.md").exists() and (current / "scripts").exists():
                return current
            current = current.parent
        raise RuntimeError("Could not find project root")
    
    def initialize(self, force: bool = False) -> None:
        """Initialize the registry by scanning all template locations.
        
        Args:
            force: Force re-initialization even if already initialized.
        """
        if self._initialized and not force:
            return
        
        logger.info("Initializing unified template registry...")
        self._templates.clear()
        self._template_paths.clear()
        
        # Scan each search path
        for search_path in self.search_paths:
            if search_path.exists():
                logger.info(f"Scanning template path: {search_path}")
                self._scan_template_path(search_path)
        
        # Resolve conflicts and duplicates
        self._resolve_conflicts()
        
        self._initialized = True
        logger.info(f"Registry initialized with {len(self._templates)} templates")
    
    def _scan_template_path(self, base_path: Path) -> None:
        """Scan a template directory for templates.
        
        Args:
            base_path: Base path to scan for templates.
        """
        for type_enum in TemplateType:
            type_dir = base_path / type_enum.value
            if type_dir.exists() and type_dir.is_dir():
                for template_dir in type_dir.iterdir():
                    if template_dir.is_dir():
                        self._register_template(template_dir, type_enum)
    
    def _register_template(self, template_path: Path, template_type: TemplateType) -> None:
        """Register a single template.
        
        Args:
            template_path: Path to the template directory.
            template_type: Type of the template.
        """
        # Check for manifest file
        manifest_path = template_path / "template.manifest.json"
        manifest_data = {}
        
        if manifest_path.exists():
            try:
                manifest_data = json.loads(manifest_path.read_text(encoding="utf-8"))
            except Exception as e:
                logger.warning(f"Failed to read manifest at {manifest_path}: {e}")
        
        # Detect variants (subdirectories)
        variants = []
        for item in template_path.iterdir():
            if item.is_dir() and not item.name.startswith("."):
                variants.append(item.name)
        
        if not variants:
            variants = ["base"]
        
        # Create metadata
        metadata = TemplateMetadata(
            name=manifest_data.get("name", template_path.name),
            type=template_type,
            path=template_path,
            variants=manifest_data.get("variants", variants),
            engines=manifest_data.get("engines"),
            version=manifest_data.get("version", "1.0.0"),
            description=manifest_data.get("description", ""),
            dependencies=manifest_data.get("dependencies", []),
            tags=manifest_data.get("tags", []),
            manifest_data=manifest_data,
        )
        
        # Register with conflict tracking
        key = f"{template_type.value}/{metadata.name}"
        if key in self._templates:
            # Track duplicate for conflict resolution
            existing = self._templates[key]
            logger.warning(
                f"Duplicate template '{key}' found at:\n"
                f"  - {existing.path}\n"
                f"  - {template_path}"
            )
        else:
            self._templates[key] = metadata
            self._template_paths.add(template_path)
    
    def _resolve_conflicts(self) -> None:
        """Resolve template conflicts using priority rules.
        
        Priority order (highest to lowest):
        1. Top-level template-packs/ (newest, primary location)
        2. unified-workflow/templates/ (unified system templates)
        3. project_generator/template-packs/ (legacy location)
        """
        # For now, first registration wins (search_paths are in priority order)
        # In the future, we could implement more sophisticated conflict resolution
        pass
    
    def get_template(self, template_type: str, template_name: str) -> Optional[TemplateMetadata]:
        """Get a specific template by type and name.
        
        Args:
            template_type: Type of template (backend, frontend, etc.)
            template_name: Name of the template.
            
        Returns:
            TemplateMetadata if found, None otherwise.
        """
        if not self._initialized:
            self.initialize()
        
        key = f"{template_type}/{template_name}"
        return self._templates.get(key)
    
    def list_templates(self, template_type: Optional[str] = None) -> List[TemplateMetadata]:
        """List all templates, optionally filtered by type.
        
        Args:
            template_type: Optional type filter.
            
        Returns:
            List of template metadata.
        """
        if not self._initialized:
            self.initialize()
        
        templates = list(self._templates.values())
        
        if template_type:
            templates = [t for t in templates if t.type.value == template_type]
        
        return sorted(templates, key=lambda t: (t.type.value, t.name))
    
    def get_template_path(self, template_type: str, template_name: str, 
                         variant: str = "base") -> Optional[Path]:
        """Get the full path to a template variant.
        
        Args:
            template_type: Type of template.
            template_name: Name of the template.
            variant: Template variant (default: "base").
            
        Returns:
            Path to template variant directory if found, None otherwise.
        """
        template = self.get_template(template_type, template_name)
        if not template:
            return None
        
        if variant not in template.variants:
            logger.warning(
                f"Variant '{variant}' not found for {template_type}/{template_name}. "
                f"Available variants: {template.variants}"
            )
            return None
        
        variant_path = template.path / variant
        if variant_path.exists():
            return variant_path
        
        # Fallback to template root if variant directory doesn't exist
        return template.path
    
    def add_template_location(self, path: Path, priority: int = 10) -> None:
        """Add a new template search location.
        
        Args:
            path: Path to add to search locations.
            priority: Priority (lower number = higher priority).
        """
        # Insert based on priority
        self.search_paths.append(path)
        # Re-initialize to pick up new templates
        self.initialize(force=True)
    
    def validate_template(self, template_type: str, template_name: str) -> Dict[str, Any]:
        """Validate a template's structure and dependencies.
        
        Args:
            template_type: Type of template.
            template_name: Name of template.
            
        Returns:
            Validation results dictionary.
        """
        template = self.get_template(template_type, template_name)
        if not template:
            return {"valid": False, "error": "Template not found"}
        
        issues = []
        
        # Check if template path exists
        if not template.path.exists():
            issues.append(f"Template path does not exist: {template.path}")
        
        # Check variants exist
        for variant in template.variants:
            variant_path = template.path / variant
            if not variant_path.exists() and len(template.variants) > 1:
                issues.append(f"Variant directory missing: {variant}")
        
        # Check for required files based on template type
        if template.type == TemplateType.FRONTEND:
            required_files = ["package.json", "README.md"]
        elif template.type == TemplateType.BACKEND:
            required_files = ["requirements.txt", "README.md"]
        else:
            required_files = ["README.md"]
        
        for req_file in required_files:
            file_path = template.path / req_file
            if not file_path.exists():
                # Check in first variant
                if template.variants:
                    variant_path = template.path / template.variants[0] / req_file
                    if not variant_path.exists():
                        issues.append(f"Required file missing: {req_file}")
        
        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "template": template.name,
            "type": template.type.value,
            "path": str(template.path),
        }
    
    def export_manifest(self) -> Dict[str, Any]:
        """Export the complete registry manifest.
        
        Returns:
            Dictionary containing all template metadata.
        """
        if not self._initialized:
            self.initialize()
        
        manifest = {
            "version": "1.0.0",
            "templates": {},
            "search_paths": [str(p) for p in self.search_paths],
        }
        
        for key, template in self._templates.items():
            manifest["templates"][key] = {
                "name": template.name,
                "type": template.type.value,
                "path": str(template.path),
                "variants": template.variants,
                "version": template.version,
                "description": template.description,
                "dependencies": template.dependencies,
                "tags": template.tags,
            }
        
        return manifest


# Global registry instance
_registry: Optional[UnifiedTemplateRegistry] = None


def get_registry() -> UnifiedTemplateRegistry:
    """Get the global unified template registry instance.
    
    Returns:
        The global registry instance.
    """
    global _registry
    if _registry is None:
        _registry = UnifiedTemplateRegistry()
    return _registry


# Backward compatibility functions for project_generator
def list_all() -> List[Dict[str, Any]]:
    """List all templates (backward compatibility for project_generator).
    
    Returns:
        List of template dictionaries in legacy format.
    """
    registry = get_registry()
    templates = registry.list_templates()
    
    # Convert to legacy format
    results = []
    for template in templates:
        results.append({
            "type": template.type.value,
            "name": template.name,
            "variants": template.variants,
            "engines": template.engines,
            "path": str(template.path),
        })
    
    return results


def get_template_path_legacy(template_type: str, template_name: str) -> Optional[str]:
    """Get template path in legacy format.
    
    Args:
        template_type: Type of template.
        template_name: Name of template.
        
    Returns:
        String path if found, None otherwise.
    """
    registry = get_registry()
    path = registry.get_template_path(template_type, template_name)
    return str(path) if path else None
