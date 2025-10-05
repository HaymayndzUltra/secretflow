# AGENTS.md

## Project Setup
- **Install Dependencies**: Run `pip install -r requirements.txt` to install all necessary packages
- **Verify Week 2**: Ensure Week 2 modules are functional before starting Week 3

## Build & Test
- **Run Tests**: Execute `python3 -m pytest tests/` to run all tests
- **Code Style Check**: Use `python3 -m flake8` to enforce code style guidelines
- **Integration Tests**: Run `python3 -c "from unified_workflow.automation import *"` to verify imports

## Development Guidelines
- **Python Version**: Use Python 3.8+ as specified in requirements
- **File Structure**:
  - Place template registry in `unified_workflow/core/template_registry.py`
  - Place CLI in `unified_workflow/cli.py`
  - Place compliance validator in `unified_workflow/automation/compliance_validator.py`
- **Code Style**:
  - Use type hints for all function parameters and return values
  - Follow PEP 8 naming conventions
  - Add docstrings for all public methods

## Week 3 Implementation Tasks

### Day 1-2: Template Pack Migration
- **Fix Duplicate Templates**: Update `unified_workflow/core/template_registry.py` to handle duplicates
- **Update Project Generator**: Modify `unified_workflow/automation/project_generator.py` to use unified registry
- **Test Template Application**: Verify templates can be applied correctly
- **Document Template Governance**: Create `unified_workflow/templates/TEMPLATE_GOVERNANCE.md`

### Day 3-4: CLI Compatibility Layer
- **Enhance CLI**: Update `unified_workflow/cli.py` with command routing functionality
- **Implement Telemetry**: Add usage tracking for deprecation decisions
- **Test Backward Compatibility**: Ensure legacy scripts still work
- **Verify Command Routing**: Test unified CLI routes correctly

### Day 5-7: Compliance Validation Integration
- **Complete Compliance Validator**: Enhance `unified_workflow/automation/compliance_validator.py`
- **Implement Validators**: Add HIPAA/SOC2/PCI validation methods
- **Test Asset Generation**: Verify compliance assets are generated correctly
- **Update Gates**: Integrate compliance validator with quality gates

## Validation Gate 3 Requirements
- All templates accessible via unified registry
- Legacy CLI commands route correctly
- Compliance validation produces correct assets
- Integration tests pass

## Pull Request
- **Title Format**: Follow Conventional Commits (e.g., `feat: implement Week 3 template migration`)
- **Pre-commit Check**: Run `python3 -m pytest` and `python3 -m flake8` before submitting
- **Documentation**: Update relevant documentation files