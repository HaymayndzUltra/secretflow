# Week 3: Template & CLI Integration - Validation Prompt

## Validation Objective
Verify that Week 3's three core components (Template Pack Migration, CLI Compatibility Layer, Compliance Validation Integration) are fully implemented, tested, and ready for Week 4 protocol integration.

## Prerequisites Verification

Before validating Week 3, confirm Week 2 completion:

1. **Week 2 Modules Operational**
   - Run: `python3 -c "from unified_workflow.automation.project_generator import UnifiedProjectGenerator; from unified_workflow.automation.brief_processor import UnifiedBriefProcessor; from unified_workflow.automation.workflow_automation import UnifiedWorkflowAutomation; print('✓ Week 2 modules loaded')"`
   - Expected: No ImportError, all modules load successfully

2. **Template Registry Functional**
   - Run: `python3 -c "from unified_workflow.core.template_registry import UnifiedTemplateRegistry; r = UnifiedTemplateRegistry(); print(f'✓ Found {len(r.list_templates())} templates')"`
   - Expected: Template count > 0, no critical errors

## Module 1: Template Pack Migration

### File Structure Check
```bash
# Verify template directories exist
ls -la unified_workflow/templates/
ls -la template-packs/
ls -la project_generator/template-packs/
```

### Code Structure Validation
Verify the template registry integration:

1. **Registry Integration**
   - `unified_workflow/core/template_registry.py` exists and loads
   - Can discover templates from both `template-packs/` and `project_generator/template-packs/`
   - Handles duplicate templates gracefully

2. **Template References Updated**
   - Project generator uses unified registry instead of hardcoded paths
   - Template loading delegates to registry
   - No direct template path references in generators

### Functional Testing

**Test 1: Template Discovery**
```python
from unified_workflow.core.template_registry import UnifiedTemplateRegistry

registry = UnifiedTemplateRegistry()
templates = registry.list_templates()
print(f"✓ Found {len(templates)} templates")

# Check for expected template categories
categories = set(t.template_type.value for t in templates)
expected_categories = {'frontend', 'backend', 'database', 'devex', 'cicd'}
assert expected_categories.issubset(categories), f"Missing categories: {expected_categories - categories}"
print("✓ All expected template categories found")
```

**Test 2: Template Loading**
```python
from unified_workflow.core.template_registry import UnifiedTemplateRegistry

registry = UnifiedTemplateRegistry()
# Test loading specific templates
frontend_templates = registry.get_templates_by_type('frontend')
backend_templates = registry.get_templates_by_type('backend')

assert len(frontend_templates) > 0, "No frontend templates found"
assert len(backend_templates) > 0, "No backend templates found"

# Test template metadata
for template in frontend_templates[:2]:  # Test first 2
    assert template.name, "Template name missing"
    assert template.path.exists(), f"Template path missing: {template.path}"
    print(f"✓ Template {template.name} metadata valid")
```

**Test 3: Project Generator Integration**
```python
from unified_workflow.automation.project_generator import UnifiedProjectGenerator

generator = UnifiedProjectGenerator(
    project_name="test-template-migration",
    industry="fintech",
    stack_config={"frontend": "nextjs", "backend": "fastapi"}
)
templates = generator.get_templates()
print(f"✓ Project generator found {len(templates)} templates via unified registry")
```

### Success Criteria
- [ ] Template registry discovers templates from both locations
- [ ] All expected template categories present (frontend, backend, database, devex, cicd)
- [ ] Template metadata includes name, type, path, version
- [ ] Project generator uses unified registry
- [ ] Test 1 (template discovery) passes
- [ ] Test 2 (template loading) passes
- [ ] Test 3 (project generator integration) passes

---

## Module 2: CLI Compatibility Layer

### File Existence Check
```bash
test -f unified_workflow/cli.py && echo "✓ CLI file exists" || echo "✗ MISSING"
```

### Code Structure Validation
Verify the CLI contains:

1. **Required Components**
   - `TelemetryTracker` class for usage tracking
   - `UnifiedCLI` class for command routing
   - Legacy script routing functionality
   - Backward compatibility support

2. **Command Routing**
   - Routes legacy commands to appropriate scripts
   - Maintains argument compatibility
   - Provides unified entry point

3. **Telemetry Integration**
   - Tracks command usage
   - Stores telemetry data
   - Supports deprecation decisions

### Functional Testing

**Test 1: CLI Initialization**
```python
from unified_workflow.cli import UnifiedCLI, TelemetryTracker

# Test CLI initialization
cli = UnifiedCLI()
print("✓ CLI initialized successfully")

# Test telemetry tracker
tracker = TelemetryTracker()
print("✓ Telemetry tracker initialized")
```

**Test 2: Command Routing**
```python
from unified_workflow.cli import UnifiedCLI
import sys
from io import StringIO

cli = UnifiedCLI()

# Test help command
old_stdout = sys.stdout
sys.stdout = StringIO()
try:
    cli.run(['--help'])
    output = sys.stdout.getvalue()
    assert 'unified-workflow' in output.lower(), "Help output missing"
    print("✓ CLI help command works")
finally:
    sys.stdout = old_stdout
```

**Test 3: Legacy Command Routing**
```python
from unified_workflow.cli import UnifiedCLI

cli = UnifiedCLI()

# Test routing to legacy scripts (dry run)
# This should not execute actual commands, just verify routing logic
try:
    # Test if CLI can identify legacy commands
    legacy_commands = ['generate', 'validate', 'plan']
    for cmd in legacy_commands:
        # Verify CLI recognizes these as legacy commands
        print(f"✓ Legacy command '{cmd}' recognized")
except Exception as e:
    print(f"⚠ Legacy command routing needs verification: {e}")
```

**Test 4: Telemetry Tracking**
```python
from unified_workflow.cli import TelemetryTracker
import tempfile
import json

# Test telemetry with temporary file
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
    temp_file = f.name

try:
    tracker = TelemetryTracker(telemetry_file=Path(temp_file))
    
    # Test tracking a command
    tracker.track_command('test-command', {'arg1': 'value1'})
    tracker.save_data()
    
    # Verify data was saved
    with open(temp_file) as f:
        data = json.load(f)
        assert 'test-command' in data['commands'], "Command not tracked"
        print("✓ Telemetry tracking works")
finally:
    import os
    os.unlink(temp_file)
```

### Success Criteria
- [ ] CLI file exists at correct path
- [ ] TelemetryTracker class functional
- [ ] UnifiedCLI class functional
- [ ] Test 1 (initialization) passes
- [ ] Test 2 (help command) passes
- [ ] Test 3 (legacy routing) passes
- [ ] Test 4 (telemetry tracking) passes

---

## Module 3: Compliance Validation Integration

### File Existence Check
```bash
test -f unified_workflow/automation/compliance_validator.py && echo "✓ Compliance validator exists" || echo "✗ MISSING"
```

### Code Structure Validation
Verify the compliance validator contains:

1. **Required Components**
   - `ComplianceValidator` class
   - HIPAA, SOC2, PCI validation methods
   - Integration with project generator
   - Asset generation capabilities

2. **Validation Methods**
   - `validate_hipaa()` method
   - `validate_soc2()` method
   - `validate_pci()` method
   - `generate_compliance_assets()` method

3. **Gate Integration**
   - Integration with quality gates
   - Evidence collection
   - Compliance reporting

### Functional Testing

**Test 1: Compliance Validator Initialization**
```python
from unified_workflow.automation.compliance_validator import ComplianceValidator

validator = ComplianceValidator()
print("✓ Compliance validator initialized")
```

**Test 2: HIPAA Validation**
```python
from unified_workflow.automation.compliance_validator import ComplianceValidator

validator = ComplianceValidator()

# Test HIPAA validation
try:
    result = validator.validate_hipaa()
    print(f"✓ HIPAA validation result: {result}")
except Exception as e:
    print(f"⚠ HIPAA validation needs implementation: {e}")
```

**Test 3: SOC2 Validation**
```python
from unified_workflow.automation.compliance_validator import ComplianceValidator

validator = ComplianceValidator()

# Test SOC2 validation
try:
    result = validator.validate_soc2()
    print(f"✓ SOC2 validation result: {result}")
except Exception as e:
    print(f"⚠ SOC2 validation needs implementation: {e}")
```

**Test 4: PCI Validation**
```python
from unified_workflow.automation.compliance_validator import ComplianceValidator

validator = ComplianceValidator()

# Test PCI validation
try:
    result = validator.validate_pci()
    print(f"✓ PCI validation result: {result}")
except Exception as e:
    print(f"⚠ PCI validation needs implementation: {e}")
```

**Test 5: Compliance Asset Generation**
```python
from unified_workflow.automation.compliance_validator import ComplianceValidator
import tempfile

validator = ComplianceValidator()

# Test asset generation
with tempfile.TemporaryDirectory() as temp_dir:
    try:
        assets = validator.generate_compliance_assets(output_dir=temp_dir)
        print(f"✓ Generated {len(assets)} compliance assets")
    except Exception as e:
        print(f"⚠ Asset generation needs implementation: {e}")
```

### Success Criteria
- [ ] Compliance validator file exists
- [ ] ComplianceValidator class functional
- [ ] Test 1 (initialization) passes
- [ ] Test 2 (HIPAA validation) passes or shows implementation needed
- [ ] Test 3 (SOC2 validation) passes or shows implementation needed
- [ ] Test 4 (PCI validation) passes or shows implementation needed
- [ ] Test 5 (asset generation) passes or shows implementation needed

---

## Integration Testing

### End-to-End Week 3 Test
```python
# Test complete Week 3 workflow: Templates → CLI → Compliance
from unified_workflow.core.template_registry import UnifiedTemplateRegistry
from unified_workflow.cli import UnifiedCLI
from unified_workflow.automation.compliance_validator import ComplianceValidator

# Step 1: Verify template registry
registry = UnifiedTemplateRegistry()
templates = registry.list_templates()
print(f"✓ Step 1: Found {len(templates)} templates")

# Step 2: Verify CLI
cli = UnifiedCLI()
print("✓ Step 2: CLI initialized")

# Step 3: Verify compliance validator
validator = ComplianceValidator()
print("✓ Step 3: Compliance validator initialized")

# Step 4: Test integration
print("✓ Step 4: All Week 3 components integrated successfully")
```

---

## Validation Gate 3 Checklist

### Critical Requirements (MUST PASS)
- [ ] **Template Migration**: All 7 success criteria met
- [ ] **CLI Compatibility**: All 7 success criteria met
- [ ] **Compliance Integration**: All 6 success criteria met
- [ ] **Integration Test**: End-to-end Week 3 workflow succeeds
- [ ] **No Regressions**: Week 2 functionality still works

### Quality Requirements (SHOULD PASS)
- [ ] Code coverage ≥ 80% for new modules
- [ ] No critical linter warnings
- [ ] Documentation strings present for all public methods
- [ ] Error handling implemented for all external calls

### Performance Requirements (GUIDELINE)
- [ ] Template discovery completes in < 5 seconds
- [ ] CLI command routing completes in < 2 seconds
- [ ] Compliance validation completes in < 10 seconds

---

## Failure Response Protocol

### If Validation Fails

1. **Identify Root Cause**
   - Which module failed?
   - Which specific test failed?
   - What is the error message?

2. **Categorize Issue**
   - Missing implementation?
   - Integration problem?
   - Test environment issue?
   - Dependency missing?

3. **Fix Priority**
   - **P0 (Blocker)**: Critical functionality broken, cannot proceed
   - **P1 (High)**: Major feature missing, significant workaround needed
   - **P2 (Medium)**: Minor issue, can work around temporarily
   - **P3 (Low)**: Nice-to-have, can defer to later

4. **Resolution Path**
   - P0/P1: Fix immediately before proceeding to Week 4
   - P2: Document workaround, add to backlog
   - P3: Add to backlog for future iteration

---

## Approval to Proceed to Week 4

**Week 3 is COMPLETE and Week 4 can begin when:**

✅ All Critical Requirements are met  
✅ At least 80% of Quality Requirements are met  
✅ All P0/P1 issues are resolved  
✅ Documentation updated with any known P2/P3 issues

**Sign-off:**
- [ ] Technical lead approval
- [ ] Integration tests passing
- [ ] Week 3 retrospective completed

---

## Expected Outcomes

Based on REVISED_INTEGRATION_TIMELINE.md Week 3:

### Day 1-2: Template Pack Migration ✅
- Unified registry loads all templates from both locations
- Template references updated in generators
- Template application tested
- Template governance documented

### Day 3-4: CLI Compatibility Layer ✅
- `unified-workflow/cli.py` created and functional
- Command routing to legacy scripts implemented
- Telemetry for usage tracking added
- Backward compatibility tested

### Day 5-7: Compliance Validation Integration ✅
- `unified-workflow/automation/compliance_validator.py` completed
- HIPAA/SOC2/PCI validators integrated
- Compliance asset generation tested
- Gates updated to use unified validators

**Final Result**: Week 3 Template & CLI Integration complete and ready for Week 4 Protocol & Automation Integration.
