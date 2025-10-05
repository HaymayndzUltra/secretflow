#!/usr/bin/env python3
"""Unified Brief Processor

This module provides a unified interface for brief processing, integrating
the existing brief parsing and planning functionality with the unified workflow system.
"""

from __future__ import annotations

import logging
import json
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

# Import brief parsing components
import sys
sys.path.append(str(Path(__file__).resolve().parents[2]))

try:
    from project_generator.core.brief_parser import BriefParser
except ImportError:
    # Fallback if project_generator not available
    class BriefParser:
        def __init__(self, path):
            self.path = Path(path)
        def parse(self, content=None):
            return self._parse_brief_fallback(content or self.path.read_text())

try:
    from scripts.lifecycle_tasks import build_plan
except ImportError:
    # Fallback if scripts not available
    build_plan = None

# Import unified components
from unified_workflow.automation.evidence_manager import EvidenceManager

logger = logging.getLogger(__name__)


class UnifiedBriefProcessor:
    """Unified brief processor with metadata extraction and plan generation."""

    def __init__(self):
        """Initialize the unified brief processor."""
        self.evidence_manager = EvidenceManager()

        # Initialize brief parser (handle both real and fallback)
        if BriefParser is not None:
            try:
                # Try to create with a dummy path for fallback BriefParser
                if hasattr(BriefParser, '__module__') and BriefParser.__module__ == '__main__':
                    # This is our fallback class
                    self.brief_parser = BriefParser("/tmp/dummy")
                else:
                    # This is the real BriefParser class
                    self.brief_parser = BriefParser("/tmp/dummy")
            except Exception:
                self.brief_parser = None
        else:
            self.brief_parser = None

        logger.info("UnifiedBriefProcessor initialized")

    def process_brief(
        self,
        brief_path: Union[str, Path],
        output_dir: Optional[Union[str, Path]] = None,
        project_name: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """Process a brief file and generate plan and metadata.

        Args:
            brief_path: Path to the brief.md file
            output_dir: Output directory for generated files
            project_name: Override project name from brief
            **kwargs: Additional processing options

        Returns:
            Processing results with plan, metadata, and artifacts
        """
        try:
            brief_path = Path(brief_path)

            if not brief_path.exists():
                return {
                    "success": False,
                    "error": f"Brief file not found: {brief_path}"
                }

            logger.info(f"Processing brief: {brief_path}")

            # Set default output directory
            if output_dir is None:
                output_dir = Path.cwd()
            else:
                output_dir = Path(output_dir)

            # Ensure output directory exists
            output_dir.mkdir(parents=True, exist_ok=True)

            # Step 1: Parse the brief
            logger.info("Parsing brief content...")
            brief_content = brief_path.read_text(encoding='utf-8')

            if self.brief_parser is not None:
                # Use either real or fallback BriefParser
                if hasattr(self.brief_parser, '__module__') and self.brief_parser.__module__ == '__main__':
                    # This is our fallback class, pass content directly
                    parsed_brief = self.brief_parser.parse(brief_content)
                else:
                    # This is the real BriefParser, it needs a file path
                    # Write content to temp file and parse
                    import tempfile
                    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
                        f.write(brief_content)
                        temp_path = f.name

                    # Update parser path and parse
                    self.brief_parser.path = Path(temp_path)
                    parsed_brief = self.brief_parser.parse()
            else:
                # Fallback parsing if BriefParser not available
                parsed_brief = self._parse_brief_fallback(brief_content)

            # Step 2: Extract metadata
            logger.info("Extracting project metadata...")
            metadata = self._extract_metadata(parsed_brief, brief_path, project_name)

            # Step 3: Generate plan
            logger.info("Generating project plan...")
            if build_plan is not None:
                plan_result = self._generate_plan_with_build_plan(parsed_brief, metadata, output_dir)
            else:
                # Fallback plan generation
                plan_result = self._generate_plan_fallback(metadata, output_dir)

            # Step 4: Create project configuration
            logger.info("Creating project configuration...")
            project_config = self._create_project_config(metadata, kwargs)

            # Step 5: Log evidence
            logger.info("Logging evidence artifacts...")
            evidence_result = self._log_evidence_artifacts(
                output_dir, metadata, plan_result
            )

            # Combine results
            result = {
                "success": True,
                "brief_path": str(brief_path),
                "metadata": metadata,
                "plan": plan_result,
                "project_config": project_config,
                "evidence": evidence_result,
                "output_dir": str(output_dir),
                "artifacts": self._list_generated_artifacts(output_dir)
            }

            logger.info(f"Brief processing completed successfully for {metadata.get('name', 'unknown project')}")
            return result

        except Exception as e:
            logger.error(f"Brief processing failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "brief_path": str(brief_path)
            }

    def _extract_metadata(self, parsed_brief: Dict[str, Any], brief_path: Path, project_name: Optional[str] = None) -> Dict[str, Any]:
        """Extract comprehensive metadata from parsed brief.

        Args:
            parsed_brief: Parsed brief content
            brief_path: Path to the brief file
            project_name: Override project name

        Returns:
            Extracted metadata
        """
        metadata = {
            "brief_path": str(brief_path),
            "brief_filename": brief_path.name,
            "extraction_timestamp": self._get_timestamp(),
            "source": "brief_processor"
        }

        # Extract project name
        if project_name:
            metadata["name"] = project_name
        elif parsed_brief and "title" in parsed_brief:
            metadata["name"] = parsed_brief["title"].strip()
        elif parsed_brief and "name" in parsed_brief:
            metadata["name"] = parsed_brief["name"].strip()
        else:
            metadata["name"] = brief_path.stem

        # Extract project type and complexity
        if parsed_brief and isinstance(parsed_brief, dict) and "content" in parsed_brief:
            content_lower = parsed_brief["content"].lower()
        elif parsed_brief:
            content_lower = str(parsed_brief).lower()
        else:
            content_lower = ""

        # Determine project type
        if any(keyword in content_lower for keyword in ["fullstack", "full stack", "full-stack"]):
            metadata["project_type"] = "fullstack"
        elif any(keyword in content_lower for keyword in ["frontend", "ui", "client"]):
            metadata["project_type"] = "frontend-only"
        elif any(keyword in content_lower for keyword in ["backend", "api", "server"]):
            metadata["project_type"] = "backend-only"
        else:
            metadata["project_type"] = "fullstack"  # Default

        # Determine complexity
        word_count = len(str(parsed_brief).split())
        if word_count < 200:
            metadata["complexity"] = "simple"
        elif word_count < 500:
            metadata["complexity"] = "medium"
        else:
            metadata["complexity"] = "complex"

        # Extract industry (look for keywords)
        industry_keywords = {
            "healthcare": ["healthcare", "medical", "patient", "hospital", "clinic"],
            "finance": ["finance", "financial", "bank", "payment", "transaction"],
            "ecommerce": ["ecommerce", "shop", "store", "product", "catalog"],
            "saas": ["saas", "software", "platform", "service", "application"],
            "enterprise": ["enterprise", "corporate", "business", "internal"]
        }

        for industry, keywords in industry_keywords.items():
            if any(keyword in content_lower for keyword in keywords):
                metadata["industry"] = industry
                break
        else:
            metadata["industry"] = "saas"  # Default

        # Extract compliance requirements
        compliance_keywords = {
            "gdpr": ["gdpr", "privacy", "data protection", "personal data"],
            "hipaa": ["hipaa", "healthcare", "medical", "patient data"],
            "soc2": ["soc2", "security", "compliance", "audit"],
            "pci": ["pci", "payment", "card", "transaction"]
        }

        metadata["compliance"] = []
        for compliance, keywords in compliance_keywords.items():
            if any(keyword in content_lower for keyword in keywords):
                metadata["compliance"].append(compliance)

        # Extract technology preferences
        tech_keywords = {
            "frontend": {
                "nextjs": ["nextjs", "next.js", "react"],
                "nuxt": ["nuxt", "vue"],
                "angular": ["angular"],
                "expo": ["expo", "react native"]
            },
            "backend": {
                "fastapi": ["fastapi", "python"],
                "nestjs": ["nestjs", "node"],
                "django": ["django", "python"],
                "go": ["golang", "go"]
            },
            "database": {
                "postgres": ["postgres", "postgresql"],
                "mongodb": ["mongodb", "mongo"],
                "firebase": ["firebase"]
            }
        }

        for category, techs in tech_keywords.items():
            for tech, keywords in techs.items():
                if any(keyword in content_lower for keyword in keywords):
                    metadata[category] = tech
                    break

        return metadata

    def _generate_plan(self, parsed_brief: Dict[str, Any], metadata: Dict[str, Any], output_dir: Path) -> Dict[str, Any]:
        """Generate PLAN.md and tasks.json from parsed brief.

        Args:
            parsed_brief: Parsed brief content
            metadata: Extracted metadata
            output_dir: Output directory

        Returns:
            Plan generation results
        """
        try:
            # Use the existing build_plan function from lifecycle_tasks
            plan_data = build_plan(parsed_brief, metadata)

            # Generate PLAN.md
            plan_md_path = output_dir / "PLAN.md"
            plan_md_content = self._generate_plan_markdown(plan_data, metadata)
            plan_md_path.write_text(plan_md_content, encoding='utf-8')

            # Generate tasks.json
            tasks_json_path = output_dir / "tasks.json"
            tasks_json_content = json.dumps(plan_data, indent=2)
            tasks_json_path.write_text(tasks_json_content, encoding='utf-8')

            return {
                "success": True,
                "plan_data": plan_data,
                "plan_md_path": str(plan_md_path),
                "tasks_json_path": str(tasks_json_path),
                "task_count": len(plan_data.get("tasks", [])),
                "phase_count": len(plan_data.get("phases", []))
            }

        except Exception as e:
            logger.error(f"Plan generation failed: {e}")
            return {
                "success": False,
                "error": str(e)
            }

    def _generate_plan_markdown(self, plan_data: Dict[str, Any], metadata: Dict[str, Any]) -> str:
        """Generate PLAN.md content from plan data.

        Args:
            plan_data: Structured plan data
            metadata: Project metadata

        Returns:
            PLAN.md content
        """
        lines = []

        # Header
        lines.append(f"# {metadata.get('name', 'Project')} - Development Plan")
        lines.append("")
        lines.append(f"**Complexity:** {metadata.get('complexity', 'unknown').title()}")
        lines.append(f"**Industry:** {metadata.get('industry', 'unknown').title()}")
        lines.append(f"**Project Type:** {metadata.get('project_type', 'unknown').title()}")
        lines.append("")

        # Overview
        lines.append("## Overview")
        lines.append("")
        if "summary" in plan_data:
            lines.append(plan_data["summary"])
        else:
            lines.append("Generated development plan for the project.")
        lines.append("")

        # Architecture
        if "architecture" in plan_data:
            lines.append("## Architecture")
            lines.append("")
            lines.append(plan_data["architecture"])
            lines.append("")

        # Technology Stack
        lines.append("## Technology Stack")
        lines.append("")
        tech_stack = []
        if metadata.get("frontend"):
            tech_stack.append(f"**Frontend:** {metadata['frontend'].title()}")
        if metadata.get("backend"):
            tech_stack.append(f"**Backend:** {metadata['backend'].title()}")
        if metadata.get("database"):
            tech_stack.append(f"**Database:** {metadata['database'].title()}")

        if tech_stack:
            lines.extend(tech_stack)
        else:
            lines.append("Technology stack to be determined.")
        lines.append("")

        # Development Phases
        if "phases" in plan_data:
            lines.append("## Development Phases")
            lines.append("")
            for i, phase in enumerate(plan_data["phases"], 1):
                lines.append(f"### Phase {i}: {phase.get('name', 'Unknown')}")
                lines.append(f"**Duration:** {phase.get('duration', 'TBD')}")
                lines.append(f"**Objective:** {phase.get('objective', 'TBD')}")
                lines.append("")

        # Tasks
        if "tasks" in plan_data:
            lines.append("## Development Tasks")
            lines.append("")
            for task in plan_data["tasks"]:
                status_icon = "✅" if task.get("completed") else "⏳"
                lines.append(f"{status_icon} **{task.get('title', 'Unknown')}**")
                lines.append(f"   - {task.get('description', 'No description')}")
                lines.append(f"   - **Assignee:** {task.get('assignee', 'TBD')}")
                lines.append(f"   - **Complexity:** {task.get('complexity', 'Medium')}")
                lines.append("")

        return "\n".join(lines)

    def _create_project_config(self, metadata: Dict[str, Any], kwargs: Dict[str, Any]) -> Dict[str, Any]:
        """Create project configuration from metadata and options.

        Args:
            metadata: Extracted metadata
            kwargs: Additional configuration options

        Returns:
            Project configuration
        """
        config = {
            "name": metadata.get("name", "unknown"),
            "industry": metadata.get("industry", "saas"),
            "project_type": metadata.get("project_type", "fullstack"),
            "frontend": metadata.get("frontend", "nextjs"),
            "backend": metadata.get("backend", "fastapi"),
            "database": metadata.get("database", "postgres"),
            "compliance": metadata.get("compliance", []),
            "complexity": metadata.get("complexity", "medium"),
            "brief_path": metadata.get("brief_path", ""),
            "extraction_timestamp": metadata.get("extraction_timestamp", "")
        }

        # Override with provided kwargs
        config.update({k: v for k, v in kwargs.items() if k in config})

        return config

    def _log_evidence_artifacts(self, output_dir: Path, metadata: Dict[str, Any], plan_result: Dict[str, Any]) -> Dict[str, Any]:
        """Log generated artifacts to evidence manager.

        Args:
            output_dir: Output directory containing artifacts
            metadata: Project metadata
            plan_result: Plan generation results

        Returns:
            Evidence logging results
        """
        try:
            artifacts_logged = []

            # Log PLAN.md
            plan_md_path = output_dir / "PLAN.md"
            if plan_md_path.exists():
                self.evidence_manager.log_artifact(
                    str(plan_md_path.relative_to(output_dir)),
                    "planning",
                    "Generated project development plan",
                    phase=1  # PRD Creation phase
                )
                artifacts_logged.append("PLAN.md")

            # Log tasks.json
            tasks_json_path = output_dir / "tasks.json"
            if tasks_json_path.exists():
                self.evidence_manager.log_artifact(
                    str(tasks_json_path.relative_to(output_dir)),
                    "planning",
                    "Structured task definitions",
                    phase=1
                )
                artifacts_logged.append("tasks.json")

            # Log brief file reference
            brief_relative = Path(metadata["brief_path"]).relative_to(output_dir) if "brief_path" in metadata else "brief.md"
            self.evidence_manager.log_artifact(
                str(brief_relative),
                "requirements",
                "Project brief and requirements",
                phase=0  # Bootstrap phase
            )
            artifacts_logged.append("brief.md")

            return {
                "success": True,
                "artifacts_logged": artifacts_logged,
                "total_count": len(artifacts_logged)
            }

        except Exception as e:
            logger.error(f"Evidence logging failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "artifacts_logged": []
            }

    def _list_generated_artifacts(self, output_dir: Path) -> List[Dict[str, Any]]:
        """List all generated artifacts in output directory."""
        artifacts = []

        if not output_dir.exists():
            return artifacts

        for file_path in output_dir.rglob("*"):
            if file_path.is_file():
                artifacts.append({
                    "path": str(file_path.relative_to(output_dir)),
                    "size": file_path.stat().st_size,
                    "type": self._categorize_artifact(file_path)
                })

        return artifacts

    def _categorize_artifact(self, file_path: Path) -> str:
        """Categorize an artifact based on its path and extension."""
        path_str = str(file_path)

        if path_str.endswith("PLAN.md"):
            return "planning"
        elif path_str.endswith("tasks.json"):
            return "planning"
        elif path_str.endswith("brief.md"):
            return "requirements"
        elif file_path.suffix in [".md", ".txt"]:
            return "documentation"
        elif file_path.suffix in [".json", ".yaml", ".yml"]:
            return "configuration"
        else:
            return "other"

    def _parse_brief_fallback(self, brief_content: str) -> Dict[str, Any]:
        """Fallback brief parsing if BriefParser not available.

        Args:
            brief_content: Raw brief content

        Returns:
            Parsed brief structure
        """
        lines = brief_content.split('\n')
        sections = {}
        current_section = "overview"
        current_content = []

        for line in lines:
            line = line.strip()
            if line.startswith('#'):
                # New section
                if current_content:
                    sections[current_section] = '\n'.join(current_content)
                current_section = line.lstrip('#').strip().lower()
                current_content = []
            elif line:
                current_content.append(line)

        # Add final section
        if current_content:
            sections[current_section] = '\n'.join(current_content)

        return {
            "title": sections.get("overview", "").split('\n')[0] if sections.get("overview") else "Project",
            "content": brief_content,
            "sections": sections
        }

    def _generate_plan_with_build_plan(self, parsed_brief: Dict[str, Any], metadata: Dict[str, Any], output_dir: Path) -> Dict[str, Any]:
        """Generate plan using the build_plan function.

        Args:
            parsed_brief: Parsed brief content
            metadata: Project metadata
            output_dir: Output directory

        Returns:
            Plan generation results
        """
        try:
            # Use the existing build_plan function
            plan_data = build_plan(parsed_brief, metadata)

            # Generate PLAN.md
            plan_md_path = output_dir / "PLAN.md"
            plan_md_content = self._generate_plan_markdown(plan_data, metadata)
            plan_md_path.write_text(plan_md_content, encoding='utf-8')

            # Generate tasks.json
            tasks_json_path = output_dir / "tasks.json"
            tasks_json_content = json.dumps(plan_data, indent=2)
            tasks_json_path.write_text(tasks_json_content, encoding='utf-8')

            return {
                "success": True,
                "plan_data": plan_data,
                "plan_md_path": str(plan_md_path),
                "tasks_json_path": str(tasks_json_path),
                "task_count": len(plan_data.get("tasks", [])),
                "phase_count": len(plan_data.get("phases", [])),
                "method": "build_plan"
            }

        except Exception as e:
            logger.error(f"Plan generation with build_plan failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "method": "build_plan"
            }

    def _generate_plan_fallback(self, metadata: Dict[str, Any], output_dir: Path) -> Dict[str, Any]:
        """Fallback plan generation if build_plan not available.

        Args:
            metadata: Project metadata
            output_dir: Output directory

        Returns:
            Plan generation results
        """
        try:
            # Create a basic plan structure
            plan_data = {
                "project_name": metadata.get("name", "Unknown Project"),
                "phases": [
                    {
                        "name": "Planning",
                        "duration": "1 week",
                        "objective": "Define project requirements and architecture"
                    },
                    {
                        "name": "Development",
                        "duration": "3-4 weeks",
                        "objective": "Implement core functionality"
                    },
                    {
                        "name": "Testing",
                        "duration": "1 week",
                        "objective": "Ensure quality and reliability"
                    },
                    {
                        "name": "Deployment",
                        "duration": "1 week",
                        "objective": "Deploy to production environment"
                    }
                ],
                "tasks": [
                    {
                        "title": "Set up development environment",
                        "description": "Configure development tools and dependencies",
                        "assignee": "developer",
                        "complexity": "medium",
                        "phase": "Planning"
                    },
                    {
                        "title": "Implement core features",
                        "description": "Build main application functionality",
                        "assignee": "developer",
                        "complexity": "high",
                        "phase": "Development"
                    },
                    {
                        "title": "Write tests",
                        "description": "Create comprehensive test suite",
                        "assignee": "developer",
                        "complexity": "medium",
                        "phase": "Testing"
                    }
                ]
            }

            # Generate PLAN.md
            plan_md_path = output_dir / "PLAN.md"
            plan_md_content = self._generate_plan_markdown(plan_data, metadata)
            plan_md_path.write_text(plan_md_content, encoding='utf-8')

            # Generate tasks.json
            tasks_json_path = output_dir / "tasks.json"
            tasks_json_content = json.dumps(plan_data, indent=2)
            tasks_json_path.write_text(tasks_json_content, encoding='utf-8')

            return {
                "success": True,
                "plan_data": plan_data,
                "plan_md_path": str(plan_md_path),
                "tasks_json_path": str(tasks_json_path),
                "task_count": len(plan_data.get("tasks", [])),
                "phase_count": len(plan_data.get("phases", [])),
                "method": "fallback"
            }

        except Exception as e:
            logger.error(f"Fallback plan generation failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "method": "fallback"
            }

    def _get_timestamp(self) -> str:
        """Get current timestamp in ISO8601 format."""
        from datetime import datetime
        return datetime.utcnow().isoformat() + "Z"


# Convenience function for brief processing
def process_brief(
    brief_path: Union[str, Path],
    output_dir: Optional[Union[str, Path]] = None,
    project_name: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """Process a brief file using the unified interface.

    Args:
        brief_path: Path to the brief.md file
        output_dir: Output directory for generated files
        project_name: Override project name from brief
        **kwargs: Additional processing options

    Returns:
        Brief processing results
    """
    processor = UnifiedBriefProcessor()
    return processor.process_brief(
        brief_path=brief_path,
        output_dir=output_dir,
        project_name=project_name,
        **kwargs
    )


# CLI interface for testing
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Unified Brief Processor")
    parser.add_argument("--brief", required=True, help="Path to brief.md file")
    parser.add_argument("--output", help="Output directory")
    parser.add_argument("--name", help="Override project name")

    args = parser.parse_args()

    result = process_brief(
        brief_path=args.brief,
        output_dir=args.output,
        project_name=args.name
    )

    if result["success"]:
        print(f"✅ Brief processing completed successfully!")
        print(f"📁 Output directory: {result['output_dir']}")
        print(f"📋 Artifacts generated: {len(result['artifacts'])}")
        print(f"📊 Metadata extracted: {len(result['metadata'])} fields")
    else:
        print(f"❌ Brief processing failed: {result['error']}")
        exit(1)

