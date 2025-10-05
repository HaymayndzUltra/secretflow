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
import sys
unified_path = Path(__file__).resolve().parents[2] / "unified-workflow"
if str(unified_path) not in sys.path:
    sys.path.append(str(unified_path))

from core.template_registry import get_registry, UnifiedTemplateRegistry


class TemplateRegistry:
    """Legacy template registry interface that delegates to unified registry."""

    def __init__(self, root: Optional[Path] = None):
        """Initialize registry (now delegates to unified registry).
        
        Args:
            root: Legacy parameter, kept for compatibility but ignored.
        """
        self._unified_registry = get_registry()
        # Ensure registry is initialized
        self._unified_registry.initialize()

    def _manifest_for(self, template_dir: Path) -> Optional[Dict[str, Any]]:
        """Legacy method kept for compatibility."""
        mf = template_dir / 'template.manifest.json'
        if mf.exists():
            try:
                return json.loads(mf.read_text(encoding='utf-8'))
            except Exception:
                return None
        return None

    def list_all(self) -> List[Dict[str, Any]]:
        """List all templates using unified registry.
        
        Returns:
            List of templates in legacy format.
        """
        templates = self._unified_registry.list_templates()
        results = []
        
        for template in templates:
            entry = {
                'type': template.type.value,
                'name': template.name,
                'variants': template.variants,
                'engines': template.engines,
                'path': str(template.path),
            }
            results.append(entry)
        return results
    
    def get_template(self, template_type: str, template_name: str) -> Optional[Dict[str, Any]]:
        """Get a specific template by type and name.
        
        Args:
            template_type: Type of template.
            template_name: Name of template.
            
        Returns:
            Template dict in legacy format if found, None otherwise.
        """
        template = self._unified_registry.get_template(template_type, template_name)
        if not template:
            return None
        
        return {
            'type': template.type.value,
            'name': template.name,
            'variants': template.variants,
            'engines': template.engines,
            'path': str(template.path),
        }
    
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
        path = self._unified_registry.get_template_path(template_type, template_name, variant)
        return path

