"""
Template registry - Proxy to unified template registry.

This module now serves as a compatibility layer that delegates to the
unified template registry, ensuring consistency across all systems.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Any, List, Optional

# Import the unified template registry
# Note: This file was originally importing from unified-workflow core,
# but that creates circular dependencies. The unified template registry
# should import from this project_generator registry instead.

# For now, we'll implement a basic registry that can be enhanced later


class TemplateRegistry:
    """Legacy template registry interface.

    This is a simplified implementation that will be enhanced to delegate
    to the unified template registry once the integration is complete.
    """

    def __init__(self, root: Optional[Path] = None):
        """Initialize registry.

        Args:
            root: Legacy parameter, kept for compatibility but ignored.
        """
        self._root = root or Path(__file__).resolve().parents[2]
        self._templates = []
        self._load_templates()

    def _load_templates(self):
        """Load templates from template-packs directory."""
        template_packs_dir = self._root / "template-packs"

        if not template_packs_dir.exists():
            print(f"Warning: Template packs directory not found: {template_packs_dir}")
            return

        print(f"Loading templates from: {template_packs_dir}")

        # Scan all subdirectories recursively for template manifests
        for manifest_file in template_packs_dir.rglob('template.manifest.json'):
            try:
                print(f"  Loading manifest: {manifest_file}")
                manifest = json.loads(manifest_file.read_text(encoding='utf-8'))

                # Get the template directory (parent of manifest)
                template_dir = manifest_file.parent

                # Determine template type and name from path or manifest
                rel_path = template_dir.relative_to(template_packs_dir)
                path_parts = rel_path.parts

                # If manifest specifies type and name, use them
                template_type = manifest.get('type', path_parts[0] if len(path_parts) > 0 else 'unknown')
                template_name = manifest.get('name', path_parts[-1] if len(path_parts) > 0 else template_dir.name)

                template_info = {
                    'type': template_type,
                    'name': template_name,
                    'variants': manifest.get('variants', ['base']),
                    'engines': manifest.get('engines', ['default']),
                    'path': str(template_dir),
                }
                self._templates.append(template_info)
                print(f"  Added template: {template_info['type']}/{template_info['name']} at {template_info['path']}")
            except Exception as e:
                print(f"  Error loading manifest {manifest_file}: {e}")

        print(f"Total templates loaded: {len(self._templates)}")

    def list_all(self) -> List[Dict[str, Any]]:
        """List all templates.

        Returns:
            List of templates in legacy format.
        """
        return self._templates.copy()

    def get_template(self, template_type: str, template_name: str) -> Optional[Dict[str, Any]]:
        """Get a specific template by type and name.

        Args:
            template_type: Type of template.
            template_name: Name of template.

        Returns:
            Template metadata or None if not found.
        """
        for template in self._templates:
            if template['type'] == template_type and template['name'] == template_name:
                return template.copy()
        return None

    def get_template_path(self, template_type: str, template_name: str,
                         variant: str = "base") -> Optional[Path]:
        """Get the full path to a template variant.

        Args:
            template_type: Type of template.
            template_name: Name of template.
            variant: Template variant.

        Returns:
            Path to template if found, None otherwise.
        """
        template = self.get_template(template_type, template_name)
        if template:
            template_path = Path(template['path'])
            # For now, return the base template directory
            # In the future, this will resolve specific variants
            return template_path
        return None

