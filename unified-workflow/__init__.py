"""Unified Developer Workflow Package.

This package provides a comprehensive workflow automation system for software development,
integrating project generation, planning, compliance validation, and deployment orchestration.

Main Components:
- automation: Core automation modules (orchestrator, evidence manager, quality gates)
- core: Core utilities (template registry, evidence schema converter)
- phases: Phase-specific protocols and documentation
- evidence: Evidence collection and management

Usage:
    from unified_workflow.automation.ai_orchestrator import AIOrchestrator
    from unified_workflow.core.template_registry import TemplateRegistry
"""

__version__ = "1.0.0"
__all__ = ["automation", "core", "phases", "evidence"]

