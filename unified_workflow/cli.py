#!/usr/bin/env python3
"""Unified Workflow CLI - Compatibility layer for legacy scripts with telemetry.

This CLI provides a unified entry point while maintaining backward compatibility
with legacy scripts. It tracks usage to inform deprecation decisions.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Telemetry file location
TELEMETRY_FILE = Path.home() / ".unified-workflow" / "telemetry.json"


class TelemetryTracker:
    """Tracks CLI usage for deprecation decisions."""
    
    def __init__(self, telemetry_file: Path = TELEMETRY_FILE):
        """Initialize telemetry tracker.
        
        Args:
            telemetry_file: Path to store telemetry data
        """
        self.telemetry_file = telemetry_file
        self.telemetry_file.parent.mkdir(parents=True, exist_ok=True)
        self._load_data()
    
    def _load_data(self) -> None:
        """Load existing telemetry data."""
        if self.telemetry_file.exists():
            try:
                self.data = json.loads(self.telemetry_file.read_text())
            except Exception as e:
                logger.warning(f"Failed to load telemetry: {e}")
                self.data = {"commands": {}, "migrations": {}}
        else:
            self.data = {"commands": {}, "migrations": {}}
    
    def _save_data(self) -> None:
        """Save telemetry data."""
        try:
            self.telemetry_file.write_text(
                json.dumps(self.data, indent=2),
                encoding="utf-8"
            )
        except Exception as e:
            logger.warning(f"Failed to save telemetry: {e}")
    
    def track_command(self, command: str, args: List[str], legacy: bool = False) -> None:
        """Track a command execution.
        
        Args:
            command: Command name
            args: Command arguments
            legacy: Whether this was a legacy command
        """
        timestamp = datetime.utcnow().isoformat() + "Z"
        
        if command not in self.data["commands"]:
            self.data["commands"][command] = {
                "count": 0,
                "legacy_count": 0,
                "first_seen": timestamp,
                "last_seen": timestamp,
                "args_patterns": {}
            }
        
        cmd_data = self.data["commands"][command]
        cmd_data["count"] += 1
        if legacy:
            cmd_data["legacy_count"] += 1
        cmd_data["last_seen"] = timestamp
        
        # Track argument patterns
        args_key = " ".join(args[:2]) if args else "no_args"
        if args_key not in cmd_data["args_patterns"]:
            cmd_data["args_patterns"][args_key] = 0
        cmd_data["args_patterns"][args_key] += 1
        
        self._save_data()
    
    def get_deprecation_candidates(self, days: int = 14) -> List[str]:
        """Get commands that haven't been used in N days via legacy path.
        
        Args:
            days: Number of days to check
            
        Returns:
            List of command names that are deprecation candidates
        """
        candidates = []
        cutoff = datetime.utcnow().timestamp() - (days * 86400)
        
        for cmd, data in self.data["commands"].items():
            if data["legacy_count"] > 0:
                last_seen = datetime.fromisoformat(
                    data["last_seen"].replace("Z", "+00:00")
                ).timestamp()
                if last_seen < cutoff:
                    candidates.append(cmd)
        
        return candidates


class LegacyCommandRouter:
    """Routes legacy commands to their implementations."""
    
    def __init__(self, project_root: Optional[Path] = None):
        """Initialize the legacy command router.
        
        Args:
            project_root: Root directory of the project
        """
        self.project_root = project_root or self._find_project_root()
        self.scripts_dir = self.project_root / "scripts"
        self.unified_automation = self.project_root / "unified-workflow" / "automation"
        self.tracker = TelemetryTracker()
        
        # Define command mappings
        self.command_map = {
            # Project generation commands
            "generate-project": {
                "script": "generate_client_project.py",
                "unified": "project_generator.py",
                "description": "Generate a new project from templates"
            },
            "generate-from-brief": {
                "script": "generate_from_brief.py",
                "unified": "brief_processor.py",
                "description": "Generate project from a brief file"
            },
            "bootstrap": {
                "script": "bootstrap_project.py",
                "unified": "project_generator.py",
                "description": "Bootstrap a new project"
            },
            
            # Planning commands
            "plan-from-brief": {
                "script": "plan_from_brief.py",
                "unified": "brief_processor.py",
                "description": "Generate plan from brief"
            },
            "pre-lifecycle-plan": {
                "script": "pre_lifecycle_plan.py",
                "unified": "plan_manager.py",
                "description": "Create pre-lifecycle plan"
            },
            
            # Workflow commands
            "run-workflow": {
                "script": "run_workflow.py",
                "unified": "ai_orchestrator.py",
                "description": "Execute workflow automation"
            },
            
            # Validation commands
            "validate-compliance": {
                "script": "validate_compliance_assets.py",
                "unified": "compliance_validator.py",
                "description": "Validate compliance documentation"
            },
            "validate-prd": {
                "script": "validate_prd_gate.py",
                "unified": "validation_gates.py",
                "description": "Validate PRD gate"
            },
            "validate-tasks": {
                "script": "validate_tasks.py",
                "unified": "validation_gates.py",
                "description": "Validate task definitions"
            },
            
            # Utility commands
            "doctor": {
                "script": "doctor.py",
                "unified": None,  # Keep as standalone
                "description": "Check environment health"
            },
            "analyze-rules": {
                "script": "analyze_project_rules.py",
                "unified": None,  # Keep as standalone
                "description": "Analyze project rules"
            }
        }
    
    def _find_project_root(self) -> Path:
        """Find the project root directory."""
        current = Path.cwd()
        while current.parent != current:
            if (current / "scripts").exists() and (current / "unified-workflow").exists():
                return current
            current = current.parent
        return Path.cwd()
    
    def list_commands(self) -> List[Tuple[str, str]]:
        """List all available commands.
        
        Returns:
            List of (command, description) tuples
        """
        return [(cmd, info["description"]) for cmd, info in self.command_map.items()]
    
    def route_command(self, command: str, args: List[str], use_legacy: bool = False) -> int:
        """Route a command to its implementation.
        
        Args:
            command: Command name
            args: Command arguments
            use_legacy: Force use of legacy implementation
            
        Returns:
            Exit code
        """
        if command not in self.command_map:
            logger.error(f"Unknown command: {command}")
            return 1
        
        cmd_info = self.command_map[command]
        
        # Track command usage
        self.tracker.track_command(command, args, legacy=use_legacy)
        
        # Determine which implementation to use
        if use_legacy or cmd_info["unified"] is None:
            # Use legacy script
            script_path = self.scripts_dir / cmd_info["script"]
            if not script_path.exists():
                logger.error(f"Legacy script not found: {script_path}")
                return 1
            
            logger.info(f"Running legacy command: {command}")
            return self._run_legacy_script(script_path, args)
        else:
            # Use unified implementation
            unified_path = self.unified_automation / cmd_info["unified"]
            if unified_path.exists():
                logger.info(f"Running unified command: {command}")
                return self._run_unified_module(unified_path, args)
            else:
                # Fall back to legacy if unified not ready
                logger.warning(f"Unified implementation not found, falling back to legacy")
                self.tracker.track_command(command, args, legacy=True)
                script_path = self.scripts_dir / cmd_info["script"]
                return self._run_legacy_script(script_path, args)
    
    def _run_legacy_script(self, script_path: Path, args: List[str]) -> int:
        """Run a legacy Python script.
        
        Args:
            script_path: Path to the script
            args: Script arguments
            
        Returns:
            Exit code
        """
        cmd = [sys.executable, str(script_path)] + args
        logger.debug(f"Executing: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(cmd, cwd=self.project_root)
            return result.returncode
        except Exception as e:
            logger.error(f"Failed to run legacy script: {e}")
            return 1
    
    def _run_unified_module(self, module_path: Path, args: List[str]) -> int:
        """Run a unified workflow module.
        
        Args:
            module_path: Path to the module
            args: Module arguments
            
        Returns:
            Exit code
        """
        # For now, run as subprocess - later can import and call directly
        cmd = [sys.executable, str(module_path)] + args
        logger.debug(f"Executing: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(cmd, cwd=self.project_root)
            return result.returncode
        except Exception as e:
            logger.error(f"Failed to run unified module: {e}")
            return 1


def create_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser.
    
    Returns:
        Configured argument parser
    """
    parser = argparse.ArgumentParser(
        description="Unified Developer Workflow CLI with legacy compatibility",
        epilog="Use 'unified <command> --help' for command-specific help"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="Unified Workflow CLI v1.0.0"
    )
    
    parser.add_argument(
        "--legacy",
        action="store_true",
        help="Force use of legacy script implementation"
    )
    
    parser.add_argument(
        "--show-telemetry",
        action="store_true",
        help="Show telemetry data and exit"
    )
    
    parser.add_argument(
        "--list-deprecation-candidates",
        action="store_true",
        help="List commands that are candidates for deprecation"
    )
    
    # Subcommands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add subcommands dynamically from router
    router = LegacyCommandRouter()
    for cmd, desc in router.list_commands():
        subparser = subparsers.add_parser(cmd, help=desc)
        # Add a catch-all for arguments to pass through
        subparser.add_argument(
            "args",
            nargs="*",
            help="Arguments to pass to the command"
        )
    
    return parser


def show_telemetry() -> None:
    """Display telemetry data."""
    tracker = TelemetryTracker()
    
    print("\n=== Unified Workflow Telemetry ===\n")
    
    if not tracker.data["commands"]:
        print("No telemetry data collected yet.")
        return
    
    # Sort commands by usage
    commands = sorted(
        tracker.data["commands"].items(),
        key=lambda x: x[1]["count"],
        reverse=True
    )
    
    print(f"{'Command':<25} {'Total':<8} {'Legacy':<8} {'Last Used':<20}")
    print("-" * 70)
    
    for cmd, data in commands:
        last_used = data["last_seen"][:19].replace("T", " ")
        print(f"{cmd:<25} {data['count']:<8} {data['legacy_count']:<8} {last_used:<20}")
    
    print(f"\nTotal unique commands: {len(commands)}")
    total_calls = sum(d["count"] for _, d in commands)
    total_legacy = sum(d["legacy_count"] for _, d in commands)
    print(f"Total command calls: {total_calls}")
    print(f"Legacy command calls: {total_legacy} ({total_legacy/total_calls*100:.1f}%)")


def main() -> int:
    """Main CLI entry point.
    
    Returns:
        Exit code
    """
    parser = create_parser()
    args = parser.parse_args()
    
    # Handle special flags
    if args.show_telemetry:
        show_telemetry()
        return 0
    
    if args.list_deprecation_candidates:
        tracker = TelemetryTracker()
        candidates = tracker.get_deprecation_candidates()
        if candidates:
            print("\nDeprecation candidates (unused for 14+ days via legacy):")
            for cmd in candidates:
                print(f"  - {cmd}")
        else:
            print("\nNo deprecation candidates found.")
        return 0
    
    # Handle commands
    if not args.command:
        parser.print_help()
        return 0
    
    # Route command
    router = LegacyCommandRouter()
    command_args = args.args if hasattr(args, 'args') else []
    return router.route_command(args.command, command_args, use_legacy=args.legacy)


if __name__ == "__main__":
    raise SystemExit(main())
