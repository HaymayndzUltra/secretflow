# Scripts Documentation

## Overview

The `scripts/` folder contains the automation and tooling ecosystem for **SecretFlow**, a sophisticated project generation and lifecycle management framework. This collection of scripts enables the creation of industry-specific, compliance-ready projects with automated quality gates, deployment pipelines, and comprehensive validation workflows.

The framework supports multiple project types (web applications, APIs, mobile apps, microservices) across various industries (healthcare, finance, e-commerce, SaaS) with built-in compliance support for HIPAA, GDPR, SOX, and PCI DSS.

### Core Capabilities

- **Project Generation**: Automated creation of frontend/backend projects from structured briefs
- **Quality Assurance**: Comprehensive validation, testing, and compliance checking
- **Lifecycle Management**: End-to-end workflow orchestration from planning to deployment
- **Compliance Automation**: Industry-specific compliance validation and documentation
- **Development Tooling**: Code generation, dependency management, and performance monitoring

### Architecture Philosophy

The scripts follow a **separation of concerns** principle with dedicated scripts for each phase:
- **Bootstrap & Setup** (`setup.sh`, `bootstrap_project.py`) - Initial configuration
- **Planning & Generation** (`generate_from_brief.py`, `plan_from_brief.py`) - Project creation
- **Validation & Quality** (`validate_tasks.py`, `enforce_gates.py`) - Quality assurance
- **Deployment & Operations** (`deploy_*.sh`, `install_and_test.sh`) - Production readiness
- **Maintenance & Monitoring** (`doctor.py`, `health/`) - Ongoing operations

## File Descriptions

### Bootstrap & Setup Scripts

#### `setup.sh`
**Purpose**: Initial environment setup script that copies `.env.example` files to `.env` files in template directories.

**Core Logic**:
- Checks for existing `.env` files to avoid overwrites
- Copies `.env.example` to `.env` for FastAPI and Django template directories
- Provides feedback on setup completion status

**Usage**: `./scripts/setup.sh`

#### `bootstrap_project.py`
**Purpose**: One-command bootstrap that prepares documentation and runs the end-to-end generation pipeline.

**Core Logic**:
- Loads configuration from `workflow.config.json` or environment variables
- Resolves project settings with fallback hierarchy (args → env → config)
- Scaffolds brief documentation structure
- Orchestrates the complete e2e pipeline execution

**Key Functions**:
- `load_config()`: Parses JSON configuration with type conversion
- `resolve_settings()`: Merges configuration sources with validation
- `bootstrap()`: Main orchestration function

**Usage**: `python scripts/bootstrap_project.py --name my-project --industry healthcare`

### Project Generation Scripts

#### `generate_from_brief.py`
**Purpose**: Brief-driven project orchestration that generates separate frontend and backend projects with curated Cursor rules.

**Core Logic**:
- Parses project brief using `BriefParser`
- Determines appropriate Cursor rules based on tech stack
- Generates separate frontend/backend projects with compliance rules
- Supports industry-specific compliance requirements

**Key Functions**:
- `build_fe_manifest()`: Constructs frontend rules manifest
- `build_be_manifest()`: Constructs backend rules manifest
- `write_rules_manifest()`: Persists rules configuration

**Usage**: `python scripts/generate_from_brief.py --brief docs/briefs/project/brief.md --output-root ../generated`

#### `generate_client_project.py`
**Purpose**: Main CLI script for generating industry-specific, compliance-ready client projects.

**Core Logic**:
- Validates project parameters and industry requirements
- Instantiates `ProjectGenerator` with validated specifications
- Applies industry-specific configurations and compliance rules
- Supports multiple project types and technology stacks

**Key Functions**:
- `parse_arguments()`: Comprehensive CLI argument parsing
- `ProjectGenerator` integration with template registry
- Industry-specific configuration application

**Usage**: `python scripts/generate_client_project.py --name acme-health --industry healthcare --project-type web --frontend nextjs --backend fastapi`

#### `e2e_from_brief.sh`
**Purpose**: Non-interactive, end-to-end workflow from approved brief to delivery with comprehensive quality gates.

**Core Logic**:
- Reads configuration from `workflow.config.json` or environment variables
- Executes complete pipeline: plan → validate → generate → test → deploy
- Implements force overwrite protection and validation checkpoints
- Provides detailed progress reporting and error handling

**Key Functions**:
- Configuration resolution with environment variable precedence
- Pipeline stage orchestration with error propagation
- Quality gate enforcement and compliance validation

**Usage**: `./scripts/e2e_from_brief.sh`

**Environment Variables**:
- `CONFIG_FILE` (default: `workflow.config.json`)
- Required if not present in config: `NAME`, `INDUSTRY`, `PROJECT_TYPE`, `FE`/`FRONTEND`, `BE`/`BACKEND`, `DB`/`DATABASE`
- Optional overrides: `AUTH`, `DEPLOY`, `COMPLIANCE`
- Output control: `OUTPUT_ROOT` or `OUTPUT_DIR` (default: `../_generated`), `PROJECT_DIR`
- Force overwrite: `E2E_FORCE_OUTPUT` | `FORCE_OUTPUT` | `FORCE_GENERATION` | `FORCE` (truthy: `1/true/yes/on`)
- Engine substitutions:
  - JSON: `ENGINE_SUBSTITUTIONS_JSON` | `STACK_ENGINE_SUBSTITUTIONS_JSON` | `STACK_ENGINE_SUBSTITUTIONS`
  - File path: `STACK_ENGINE_SUBSTITUTIONS_FILE`

### Planning & Architecture Scripts

#### `plan_from_brief.py`
**Purpose**: Generates structured project plans from brief specifications with task breakdown and dependency mapping.

**Core Logic**:
- Parses brief requirements into structured specifications
- Generates task dependency graphs for project execution
- Creates acceptance criteria and definition of done for each task
- Supports multiple project phases and stakeholder roles

**Key Functions**:
- Brief parsing and requirement extraction
- Task graph generation with dependency resolution
- Acceptance criteria mapping to project phases

**Usage**: `python scripts/plan_from_brief.py --brief docs/briefs/project/brief.md --out PLAN.md`

#### `lifecycle_tasks.py`
**Purpose**: Data-driven task generation for different project lifecycles with technology-specific adaptations.

**Core Logic**:
- Defines task templates for different technology stacks
- Adapts task requirements based on project specifications
- Supports conditional task inclusion based on tech stack features
- Provides structured task definitions with acceptance criteria

**Key Functions**:
- `Task` dataclass for structured task representation
- Stack-specific task generation logic
- Conditional task inclusion based on project requirements

**Usage**: Imported by planning scripts for task generation

### Planning & Documentation Scripts

#### `pre_lifecycle_plan.py`
**Purpose**: Pre-lifecycle roadmap generator with dynamic gating and validation for comprehensive project planning.

**Core Logic**:
- Generates dynamic project roadmaps based on requirements and constraints
- Implements flexible gating strategies for different project phases
- Supports conditional task inclusion based on project specifications
- Provides comprehensive validation and dependency resolution

**Key Functions**:
- Dynamic roadmap generation and customization
- Gating strategy implementation and validation
- Conditional task inclusion and dependency management

**Usage**: `python scripts/pre_lifecycle_plan.py --input [requirements.json] --output [roadmap.md]`

#### `generate_prd_assets.py`
**Purpose**: Generates PRD and architecture documentation from planning artifacts and requirements.

**Core Logic**:
- Transforms planning artifacts into structured PRD documentation
- Generates architecture summaries and technical specifications
- Supports multiple output formats and documentation standards
- Validates generated documentation for completeness and consistency

**Key Functions**:
- PRD document generation from planning data
- Architecture documentation synthesis
- Documentation validation and quality assurance

**Usage**: `python scripts/generate_prd_assets.py --input [planning-artifacts.json] --output [prd.md]`

#### `enrich_tasks.py`
**Purpose**: Enriches task definitions with personas, acceptance criteria, and detailed specifications.

**Core Logic**:
- Adds persona information and role assignments to tasks
- Generates detailed acceptance criteria for each task
- Supports conditional enrichment based on task types and requirements
- Maintains referential integrity across enriched task structures

**Key Functions**:
- Persona assignment and role mapping
- Acceptance criteria generation and validation
- Task enrichment with detailed specifications

**Usage**: `python scripts/enrich_tasks.py --input [tasks.json] --output [enriched-tasks.json]`

#### `write_context_report.py`
**Purpose**: Generates comprehensive context reports for project planning and stakeholder communication.

**Core Logic**:
- Collects and synthesizes project context information
- Generates stakeholder-ready context reports and summaries
- Supports multiple report formats and customization options
- Validates context completeness and accuracy

**Key Functions**:
- Context information collection and synthesis
- Report generation and formatting
- Context validation and completeness checking

**Usage**: `python scripts/write_context_report.py --project [project-name] --output [context-report.md]`

#### `evidence_report.py`
**Purpose**: Generates evidence reports for compliance validation and audit trail maintenance.

**Core Logic**:
- Collects evidence from various project artifacts and processes
- Generates structured evidence reports for compliance requirements
- Supports multiple evidence types and validation frameworks
- Maintains audit trails and evidence chains

**Key Functions**:
- Evidence collection and categorization
- Report generation and evidence linking
- Compliance validation and audit support

**Usage**: `python scripts/evidence_report.py --project [project-name] --compliance [hipaa,gdpr] --output [evidence-report.md]`

### Validation & Quality Scripts

#### `validate_tasks.py`
**Purpose**: Validates task dependency graphs and ensures referential integrity in project plans.

**Core Logic**:
- Validates unique task IDs across all project phases
- Checks blocked_by reference existence and validity
- Performs cycle detection using Kahn's topological sort algorithm
- Validates state and persona enumerations

**Key Functions**:
- `_collect_tasks()`: Extracts tasks from various data structures
- `validate()`: Comprehensive validation with error reporting
- Topological sort for dependency cycle detection

**Usage**: `python scripts/validate_tasks.py --input tasks.json`

#### `enforce_gates.py`
**Purpose**: Numeric quality gates enforcer for CI/CD pipelines with configurable thresholds.

**Core Logic**:
- Reads quality thresholds from `gates_config.yaml` or legacy formats
- Validates code coverage, dependency vulnerabilities, and performance metrics
- Supports multiple metrics sources (JSON, XML, YAML)
- Provides pass/fail reporting for CI integration

**Key Functions**:
- `read_coverage_pct()`: Extracts coverage from multiple formats
- `read_deps_vulns()`: Parses dependency vulnerability data
- `read_perf_metrics()`: Reads performance measurement data

**Usage**: `python scripts/enforce_gates.py`

#### `validate_prd_gate.py`
**Purpose**: Validates PRD and architecture documents for completeness and consistency.

**Core Logic**:
- Validates PRD document structure and required sections
- Checks architecture documentation for technical completeness
- Ensures alignment between PRD and technical architecture
- Reports missing or inconsistent documentation

**Key Functions**:
- PRD structure validation
- Architecture document completeness checking
- Cross-document consistency validation

**Usage**: `python scripts/validate_prd_gate.py --prd PRD.md --architecture ARCHITECTURE.md`

### Quality Assurance Scripts

#### `collect_coverage.py`
**Purpose**: Collects and aggregates code coverage data from multiple sources for quality reporting.

**Core Logic**:
- Aggregates coverage from unit tests, integration tests, and E2E tests
- Supports multiple coverage formats (JSON, XML, LCOV)
- Generates coverage reports and trends
- Integrates with CI/CD for quality gate enforcement

**Key Functions**:
- Coverage data aggregation across test types
- Report generation with historical trending
- Quality threshold validation

**Usage**: `python scripts/collect_coverage.py`

#### `collect_perf.py`
**Purpose**: Performance metrics collection and analysis for application benchmarking.

**Core Logic**:
- Measures application performance metrics (response times, throughput)
- Tracks performance regressions across builds
- Generates performance reports and alerts
- Supports multiple performance testing frameworks

**Key Functions**:
- Performance metric collection and aggregation
- Regression detection and alerting
- Performance trend analysis

**Usage**: `python scripts/collect_perf.py`

#### `scan_deps.py`
**Purpose**: Dependency scanning for security vulnerabilities and license compliance.

**Core Logic**:
- Scans project dependencies for known vulnerabilities
- Validates license compliance against project policies
- Generates security reports and remediation recommendations
- Supports multiple package managers and ecosystems

**Key Functions**:
- Vulnerability scanning across dependency trees
- License compliance validation
- Security report generation

**Usage**: `python scripts/scan_deps.py`

### Testing & Quality Assurance Scripts

#### `aggregate_coverage.py`
**Purpose**: Aggregates and combines frontend and backend code coverage data for unified reporting.

**Core Logic**:
- Merges Jest (frontend) and pytest (backend) coverage reports
- Generates unified coverage summaries in JSON format
- Supports multiple coverage formats (JSON, XML, LCOV)
- Provides coverage aggregation across different test types

**Key Functions**:
- Coverage data parsing and normalization
- Cross-format coverage merging
- Unified report generation with statistics

**Usage**: `python scripts/aggregate_coverage.py`

#### `benchmark_generation.py`
**Purpose**: Performance benchmarking for project generation processes to identify optimization opportunities.

**Core Logic**:
- Measures file I/O and template processing performance
- Tests generation speed with and without external dependencies
- Provides detailed performance metrics and recommendations
- Supports comparative benchmarking across different configurations

**Key Functions**:
- Generation time measurement and analysis
- Performance regression detection
- Optimization recommendation generation

**Usage**: `python scripts/benchmark_generation.py`

#### `router_benchmark.py`
**Purpose**: Benchmarks the router route_decision functionality with and without caching.

**Core Logic**:
- Tests router decision-making performance under various conditions
- Compares cached vs non-cached routing performance
- Provides detailed timing analysis and recommendations
- Supports multiple routing scenarios and edge cases

**Key Functions**:
- Route decision timing measurement
- Cache performance analysis
- Performance comparison and reporting

**Usage**: `python scripts/router_benchmark.py`

#### `test_policy_decisions.py`
**Purpose**: Tests and validates policy decision routing and workflow automation logic.

**Core Logic**:
- Validates router module functionality and decision accuracy
- Tests policy routing under various conditions and inputs
- Provides detailed testing reports and failure analysis
- Supports integration testing of workflow automation components

**Key Functions**:
- Policy decision validation and testing
- Router module integration testing
- Test result aggregation and reporting

**Usage**: `python scripts/test_policy_decisions.py`

### Deployment & Operations Scripts

#### `deploy_backend.sh`
**Purpose**: Backend deployment automation with environment-specific configurations.

**Core Logic**:
- Supports multiple deployment targets (AWS, Azure, GCP)
- Handles environment-specific configuration management
- Implements deployment rollback capabilities
- Provides deployment verification and health checks

**Key Functions**:
- Environment-specific deployment logic
- Configuration management and secret handling
- Deployment verification and rollback procedures

**Usage**: `./scripts/deploy_backend.sh --environment production`

#### `deploy/package_workflow.py`
**Purpose**: Packages workflow automation assets for deployment.

**Core Logic**:
- Copies `workflow_automation/`, `workflow/`, and selected scripts into a bundle directory
- Produces a `.zip` archive for transport/deployment

**Usage**: `python scripts/deploy/package_workflow.py --output deploy/workflow_bundle`

**Outputs**:
- Directory and ZIP archive at the `--output` path (default: `deploy/workflow_bundle.zip`)

#### `health/check_deployment.py`
**Purpose**: Verifies deployment health by probing public endpoints.

**Core Logic**:
- Probes frontend, API, and optional DB endpoints with timeout controls and optional insecure TLS
- Emits a JSON report and prints PASS/FAIL lines with latency and status

**Usage**: `python scripts/health/check_deployment.py --environment staging --frontend-url https://app.example.com --api-url https://api.example.com/health --output-file health.json [--timeout 10] [--insecure]`

**Inputs**:
- `--environment` (required), `--frontend-url` (required), `--api-url` (required), `--db-url` (optional)

**Outputs**:
- JSON report file when `--output-file` is provided; non-zero exit on overall failure

#### `install_and_test.sh`
**Purpose**: Automated installation and testing of generated projects.

**Core Logic**:
- Installs project dependencies using appropriate package managers
- Runs comprehensive test suites (unit, integration, E2E)
- Validates project setup and configuration
- Reports test results and setup issues

**Key Functions**:
- Dependency installation across technology stacks
- Test execution with result aggregation
- Setup validation and error reporting

**Usage**: `./scripts/install_and_test.sh`

### Rollback & Recovery Scripts

#### `rollback_backend.sh`
**Purpose**: Backend deployment rollback automation for AWS ECS environments with safety validations.

**Core Logic**:
- Supports multiple deployment targets (staging, production)
- Implements safe rollback to previous deployment revision
- Validates rollback success and provides detailed logging
- Handles environment-specific configuration and rollback procedures

**Key Functions**:
- Environment-specific rollback logic
- Deployment state validation and verification
- Rollback success confirmation and logging

**Usage**: `./scripts/rollback_backend.sh [environment] [revision]`

#### `rollback_frontend.sh`
**Purpose**: Frontend deployment rollback automation for Vercel deployments with environment management.

**Core Logic**:
- Supports environment-specific rollback targets and configurations
- Uses Vercel API for deployment management and rollback operations
- Provides rollback verification, status reporting, and error handling
- Supports custom rollback targets and environment overrides

**Key Functions**:
- Vercel deployment rollback orchestration
- Environment-specific configuration management
- Rollback verification and status reporting

**Usage**: `./scripts/rollback_frontend.sh [environment] [target]`

### Maintenance & Monitoring Scripts

#### `doctor.py`
**Purpose**: Project health diagnostics and troubleshooting automation.

**Core Logic**:
- Performs comprehensive project health checks
- Identifies configuration issues and missing dependencies
- Validates project structure and file integrity
- Provides remediation recommendations

**Key Functions**:
- Health check orchestration across multiple dimensions
- Issue detection and categorization
- Remediation suggestion generation

**Usage**: `python scripts/doctor.py --strict`

#### `check_compliance_docs.py`
**Purpose**: Validates compliance documentation completeness and accuracy.

**Core Logic**:
- Checks for required compliance documentation
- Validates document structure and completeness
- Ensures compliance evidence is properly documented
- Reports missing or inadequate compliance artifacts

**Key Functions**:
- Compliance document structure validation
- Evidence completeness checking
- Compliance gap identification

**Usage**: `python scripts/check_compliance_docs.py`

#### `validate_compliance_assets.py`
**Purpose**: Validates compliance-related assets and configurations.

**Core Logic**:
- Validates compliance configurations and settings
- Checks for required compliance tooling and processes
- Ensures compliance evidence is properly generated
- Reports compliance validation results

**Key Functions**:
- Compliance configuration validation
- Evidence generation verification
- Compliance gap reporting

**Usage**: `python scripts/validate_compliance_assets.py`

### Workflow Automation Scripts

#### `workflow_automation/`
**Purpose**: Advanced workflow orchestration and automation framework.

**Core Components**:
- `orchestrator.py`: Main workflow orchestration engine
- `context.py`: Workflow context and state management
- `evidence.py`: Evidence collection and reporting
- `gates/`: Quality gate definitions and enforcement

**Key Functions**:
- Multi-stage workflow orchestration
- Context-aware task execution
- Evidence-based quality assurance

**Usage**: Integrated into main pipeline scripts

### Workflow Management Scripts

#### `backup_workflows.py`
**Purpose**: Creates comprehensive backups of workflow documentation and configurations for disaster recovery.

**Core Logic**:
- Archives workflow documentation and trigger command configurations
- Creates timestamped backup archives with metadata and validation
- Supports selective backup of specific workflow components
- Validates backup integrity and completeness before completion

**Key Functions**:
- Workflow documentation archiving and compression
- Backup metadata generation and tracking
- Archive integrity validation and verification

**Usage**: `python scripts/backup_workflows.py`

#### `restore_workflows.py`
**Purpose**: Restores workflow backups with validation, verification, and safety checks.

**Core Logic**:
- Validates backup integrity and compatibility before restoration
- Safely restores workflow documentation and configurations
- Provides rollback capabilities for failed restoration attempts
- Supports selective restoration of specific workflow components

**Key Functions**:
- Backup validation and compatibility checking
- Safe restoration with conflict detection
- Rollback capabilities for failed operations

**Usage**: `python scripts/restore_workflows.py [backup-file]`

#### `run_workflow.py`
**Purpose**: CLI entry point for executing the workflow automation pipeline with comprehensive orchestration.

**Core Logic**:
- Provides command-line interface for workflow execution
- Orchestrates workflow automation pipeline components
- Supports configuration-based workflow customization
- Implements comprehensive error handling and logging

**Key Functions**:
- Workflow pipeline orchestration and execution
- Configuration-based workflow customization
- Error handling and pipeline state management

**Usage**: `python scripts/run_workflow.py --config workflow/gate_controller.yaml --project-root . [--verbose]`

**Inputs**:
- `--config`: Path to workflow configuration file (default: `workflow/gate_controller.yaml`)
- `--project-root`: Directory containing project artifacts (default: `.`)
- `--verbose`: Enable debug logging

**Outputs**:
- Evidence under `<project-root>/<evidence_root>` as configured (e.g., `evidence/gates/gates_report.json`)
- Exit codes: 0 success; 2 gate failed; 3 config error; 4 unexpected error

#### `validate_workflows.py`
**Purpose**: Validates workflow documentation structure, completeness, and consistency across the project.

**Core Logic**:
- Validates workflow document structure and required sections
- Checks for workflow consistency and cross-references
- Identifies missing or incomplete workflow documentation
- Provides detailed validation reports and recommendations

**Key Functions**:
- Workflow document structure validation
- Cross-workflow consistency checking
- Validation report generation and recommendations

**Usage**: `python scripts/validate_workflows.py`

#### `lane_executor.py`
**Purpose**: Executes tasks by lane respecting dependencies, concurrency limits, and execution order constraints.

**Core Logic**:
- Reads task definitions and dependency graphs from JSON
- Executes tasks respecting lane-based concurrency limits
- Tracks execution order and provides detailed logging
- Supports task state persistence and execution history

**Key Functions**:
- Task dependency resolution and execution planning
- Lane-based concurrency management and execution
- Execution history tracking and state persistence

**Usage**: `python scripts/lane_executor.py --lane [lane-name] --cap [concurrency-limit] --input [tasks.json]`

#### `update_task_state.py`
**Purpose**: Updates task states in workflow management systems with validation and state transition tracking.

**Core Logic**:
- Updates task states based on execution results and conditions
- Validates state transitions and maintains state consistency
- Tracks state change history and provides audit trails
- Supports bulk state updates and state synchronization

**Key Functions**:
- Task state validation and transition management
- State change tracking and audit trail maintenance
- Bulk state update and synchronization capabilities

**Usage**: `python scripts/update_task_state.py --input [tasks.json] --updates [state-updates.json]`

### Template Management Scripts

#### `scaffold_briefs.py`
**Purpose**: Generates project brief templates and documentation scaffolding.

**Core Logic**:
- Creates structured brief documentation
- Generates template files for project initiation
- Supports multiple project types and industries
- Provides brief validation and completion guidance

**Key Functions**:
- Brief template generation
- Documentation scaffolding
- Project type-specific customization

**Usage**: `python scripts/scaffold_briefs.py project-name`

#### `scaffold_phase_artifacts.py`
**Purpose**: Generates phase-specific artifacts and documentation templates.

**Core Logic**:
- Creates templates for each project phase
- Generates documentation structure for deliverables
- Supports artifact customization by project type
- Provides validation checklists for each phase

**Key Functions**:
- Phase-specific template generation
- Documentation structure creation
- Artifact validation framework

**Usage**: `python scripts/scaffold_phase_artifacts.py --phase planning`

#### `audit-versions.mjs`
**Purpose**: Audits template package versions against expected versions for consistency and compatibility.

**Core Logic**:
- Scans template directories for package.json files
- Compares actual versions against expected versions
- Reports version mismatches and compatibility issues
- Supports multiple template frameworks and ecosystems

**Key Functions**:
- Package version scanning and comparison
- Version compatibility validation
- Mismatch reporting and recommendations

**Usage**: `./scripts/audit-versions.mjs`

#### `doctor-templates.mjs`
**Purpose**: Template health checking utility for validating template structure and dependencies.

**Core Logic**:
- Performs comprehensive health checks on project templates
- Validates template structure and required files
- Checks dependency compatibility and version conflicts
- Provides remediation recommendations for template issues

**Key Functions**:
- Template structure validation and health assessment
- Dependency compatibility checking and analysis
- Issue detection and remediation recommendations

**Usage**: `./scripts/doctor-templates.mjs`

#### `analyze_project_rules.py`
**Purpose**: Analyzes Cursor project rules and generates validation reports and recommendations.

**Core Logic**:
- Scans and parses Cursor rule files for syntax validation
- Analyzes rule structure and metadata consistency
- Generates validation reports and optimization recommendations
- Supports rule conflict detection and resolution guidance

**Key Functions**:
- Rule syntax validation and parsing
- Metadata consistency analysis
- Validation report generation and recommendations

**Usage**: `python scripts/analyze_project_rules.py`

#### `rules_audit_quick.py`
**Purpose**: Quick audit of project rules for immediate validation and issue detection.

**Core Logic**:
- Performs rapid validation of Cursor rule files
- Identifies common rule issues and inconsistencies
- Provides immediate feedback for rule maintenance
- Supports quick rule health assessments

**Key Functions**:
- Rapid rule validation and issue detection
- Common problem identification and reporting
- Quick feedback for rule maintenance tasks

**Usage**: `python scripts/rules_audit_quick.py`

#### `standardize_frontmatter.py`
**Purpose**: Standardizes YAML frontmatter across documentation files for consistency.

**Core Logic**:
- Scans documentation files for YAML frontmatter
- Validates and standardizes frontmatter format and content
- Ensures consistent metadata structure across files
- Provides frontmatter validation and correction recommendations

**Key Functions**:
- Frontmatter parsing, validation, and standardization
- Metadata consistency enforcement
- Format correction and recommendation generation

**Usage**: `python scripts/standardize_frontmatter.py`

### Utility & Helper Scripts

#### `build_submission_pack.sh`
**Purpose**: Packages project deliverables for submission and archival.

**Core Logic**:
- Collects project artifacts and documentation
- Creates submission-ready packages
- Supports multiple packaging formats
- Provides archival and distribution utilities

**Key Functions**:
- Artifact collection and packaging
- Package format conversion
- Distribution preparation

**Usage**: `./scripts/build_submission_pack.sh`

#### `sync_from_scaffold.py`
**Purpose**: Synchronizes project state with scaffolding templates and updates.

**Core Logic**:
- Applies scaffolding updates to existing projects
- Maintains project-specific customizations
- Supports incremental synchronization
- Provides conflict resolution for modified files

**Key Functions**:
- Template-to-project synchronization
- Customization preservation
- Conflict detection and resolution

**Usage**: `python scripts/sync_from_scaffold.py --input tasks.json --root project-dir`

#### `normalize_project_rules.py`
**Purpose**: Normalizes and validates Cursor rules for consistency.

**Core Logic**:
- Validates rule syntax and structure
- Normalizes rule formatting and metadata
- Checks for rule conflicts and duplicates
- Provides rule optimization recommendations

**Key Functions**:
- Rule syntax validation
- Metadata normalization
- Conflict detection and resolution

**Usage**: `python scripts/normalize_project_rules.py`

#### `optimize_project_rules.py`
**Purpose**: Optimizes Cursor rules for performance and maintainability.

**Core Logic**:
- Analyzes rule usage patterns and performance
- Identifies redundant or conflicting rules
- Optimizes rule loading and application order
- Provides rule consolidation recommendations

**Key Functions**:
- Rule performance analysis
- Redundancy detection
- Optimization recommendation generation

**Usage**: `python scripts/optimize_project_rules.py`

### Development Tools

#### `select_stacks.py`
**Purpose**: Interactive stack selection tool for project configuration and technology stack recommendations.

**Core Logic**:
- Provides interactive prompts for technology stack selection
- Recommends appropriate stacks based on project requirements
- Supports multiple project types and industry-specific configurations
- Validates stack compatibility and provides detailed stack information

**Key Functions**:
- Interactive stack selection and recommendation
- Stack compatibility validation and analysis
- Project type-specific stack filtering and suggestions

**Usage**: `python scripts/select_stacks.py --interactive`

#### `setup_template_tests.sh`
**Purpose**: Sets up test environments for project templates with dependency installation and configuration.

**Core Logic**:
- Installs template-specific dependencies and test frameworks
- Configures test environments for different technology stacks
- Supports multiple template types and testing scenarios
- Provides environment validation and troubleshooting

**Key Functions**:
- Template-specific dependency installation
- Test environment configuration and setup
- Environment validation and compatibility checking

**Usage**: `./scripts/setup_template_tests.sh [template-type]`

#### `trigger_plan.py`
**Purpose**: Triggers planning workflows and orchestrates project planning processes.

**Core Logic**:
- Initiates project planning workflows based on requirements
- Orchestrates planning tool execution and coordination
- Supports multiple planning phases and workflow types
- Provides planning progress tracking and status reporting

**Key Functions**:
- Planning workflow initiation and orchestration
- Planning tool coordination and execution
- Progress tracking and status management

**Usage**: `python scripts/trigger_plan.py --project [project-name] --phase [planning-phase]`

### Compliance Scripts

#### `check_hipaa.py`
**Purpose**: Validates HIPAA compliance in project configurations, data handling, and security measures.

**Core Logic**:
- Checks for HIPAA compliance requirements in project setup
- Validates data handling practices and security configurations
- Identifies potential PHI exposure risks and compliance gaps
- Provides remediation recommendations for HIPAA compliance

**Key Functions**:
- HIPAA requirement validation and checking
- PHI exposure risk assessment and identification
- Compliance gap analysis and remediation recommendations

**Usage**: `python scripts/check_hipaa.py --project [project-path] --strict`

## Key Functions and Methods

### Core Generation Functions

#### `ProjectGenerator` (from `generate_client_project.py`)
- `generate()`: Main project generation orchestration
- `apply_industry_config()`: Industry-specific customization
- `validate_requirements()`: Pre-generation validation
- `post_generation_hooks()`: Post-generation cleanup and setup

#### `BriefParser` (from `generate_from_brief.py`)
- `parse()`: Structured brief parsing and validation
- `extract_requirements()`: Requirement extraction and categorization
- `validate_compliance()`: Compliance requirement validation

### Quality Assurance Functions

#### `ProjectValidator` (from `generate_client_project.py`)
- `validate_structure()`: Project structure validation
- `validate_dependencies()`: Dependency validation
- `validate_compliance()`: Compliance validation
- `validate_security()`: Security configuration validation

#### `TaskValidator` (from `validate_tasks.py`)
- `validate_dag()`: Dependency graph validation
- `detect_cycles()`: Cycle detection in task dependencies
- `validate_references()`: Cross-reference validation

### Configuration Management Functions

#### `IndustryConfig` (from `generate_client_project.py`)
- `get_stack_config()`: Technology stack configuration
- `get_compliance_config()`: Compliance requirement configuration
- `get_deployment_config()`: Deployment target configuration

## Usage Instructions

### Prerequisites

1. **Python Environment**: Python 3.8+ with required dependencies
2. **Node.js**: For frontend tooling and build processes
3. **Docker**: For containerized deployment scenarios
4. **Cloud CLI Tools**: AWS CLI, Azure CLI, or GCP CLI for cloud deployments

### Basic Usage Patterns

#### Project Generation
```bash
# Generate a healthcare web application
python scripts/generate_client_project.py \
  --name acme-health \
  --industry healthcare \
  --project-type web \
  --frontend nextjs \
  --backend fastapi \
  --database postgres \
  --auth auth0 \
  --deploy aws \
  --compliance hipaa,gdpr

# Generate from existing brief
python scripts/generate_from_brief.py \
  --brief docs/briefs/acme-health/brief.md \
  --output-root ../generated \
  --force
```

#### End-to-End Pipeline
```bash
# Run complete pipeline from brief to deployment
./scripts/e2e_from_brief.sh

# With custom configuration
NAME=my-project INDUSTRY=healthcare ./scripts/e2e_from_brief.sh
```

#### Validation and Quality Gates
```bash
# Validate project tasks
python scripts/validate_tasks.py --input project/tasks.json

# Enforce quality gates
python scripts/enforce_gates.py

# Validate compliance assets
python scripts/validate_compliance_assets.py
```

#### Deployment Operations
```bash
# Deploy backend to production
./scripts/deploy_backend.sh --environment production

# Note: No dedicated frontend deployment script is included. Use your platform's CLI/CI
# (e.g., Vercel, Netlify, CloudFront invalidations) per your environment's standards.
```

### Configuration

#### Environment Variables
- `NAME`: Project/client name
- `INDUSTRY`: Industry vertical (healthcare, finance, ecommerce, etc.)
- `PROJECT_TYPE`: Project type (web, api, mobile, fullstack)
- `FE`/`FRONTEND`: Frontend technology stack
- `BE`/`BACKEND`: Backend technology stack
- `DB`/`DATABASE`: Database technology
- `AUTH`: Authentication provider
- `DEPLOY`: Deployment target
- `COMPLIANCE`: Comma-separated compliance requirements

#### Configuration Files
- `workflow.config.json`: Main project configuration
- `gates_config.yaml`: Quality gate thresholds
- `.env`: Environment-specific settings

## Examples

### Healthcare Web Application
```bash
# Complete healthcare application generation
python scripts/bootstrap_project.py \
  --name medtech-app \
  --industry healthcare \
  --project-type web \
  --frontend nextjs \
  --backend fastapi \
  --database postgres \
  --auth auth0 \
  --deploy aws \
  --compliance hipaa \
  --update-config
```

### Financial API Service
```bash
# Financial services API with compliance
python scripts/generate_client_project.py \
  --name fintech-api \
  --industry finance \
  --project-type api \
  --backend nestjs \
  --database postgres \
  --auth cognito \
  --deploy azure \
  --compliance sox,pci,gdpr \
  --features audit-logging,encryption
```

### E-commerce Mobile Application
```bash
# Mobile commerce application
python scripts/generate_from_brief.py \
  --brief docs/briefs/shop-mobile/brief.md \
  --output-root ../generated \
  --force \
  --workers 4
```

### Development Workflow
```bash
# Local development setup and testing
./scripts/e2e_from_brief.sh

# Quality assurance pipeline
python scripts/collect_coverage.py
python scripts/collect_perf.py
python scripts/scan_deps.py
python scripts/enforce_gates.py

# Deployment to staging
./scripts/deploy_backend.sh --environment staging
## Frontend: use your platform's deployment tooling (no `deploy_frontend.sh` in this repo)
```

## Design Notes

### Architecture Decisions

1. **Separation of Concerns**: Each script has a single, well-defined responsibility
2. **Configuration Hierarchy**: Environment variables → config files → command-line arguments
3. **Idempotent Operations**: Scripts can be run multiple times safely
4. **Comprehensive Error Handling**: Detailed error reporting with actionable remediation steps
5. **Quality-First Approach**: Built-in validation and quality gates at every stage

### Technology Stack Choices

- **Python**: Primary scripting language for complex logic and data processing
- **Bash**: Shell scripting for simple file operations and system integration
- **JSON/YAML**: Configuration and data interchange formats
- **Template Engine**: Custom templating system for code generation

### Error Handling Strategy

- **Graceful Degradation**: Operations continue where possible despite individual failures
- **Detailed Logging**: Comprehensive logging with context and remediation suggestions
- **Exit Codes**: Meaningful exit codes for CI/CD integration
- **Rollback Support**: Built-in rollback capabilities for deployment operations

### Security Considerations

- **Secret Management**: Secure handling of credentials and sensitive configuration
- **Input Validation**: Comprehensive validation of all user inputs and configuration
- **Dependency Scanning**: Automated vulnerability scanning and remediation tracking
- **Compliance Automation**: Built-in compliance validation and evidence generation

## Maintenance Tips

### Regular Updates

1. **Dependency Management**: Keep Python/Node.js dependencies updated
2. **Template Maintenance**: Regularly update project templates for new best practices
3. **Rule Optimization**: Periodically run `optimize_project_rules.py` for performance
4. **Configuration Validation**: Validate configuration files after updates

### Troubleshooting

1. **Use Doctor Script**: Run `python scripts/doctor.py --strict` for comprehensive diagnostics
2. **Check Logs**: Review script output and log files for detailed error information
3. **Validate Inputs**: Ensure all required configuration is properly set
4. **Test Incrementally**: Test scripts individually before running full pipelines

### Performance Optimization

1. **Parallel Execution**: Use `--workers` parameter for CPU-intensive operations
2. **Caching**: Leverage existing caches for repeated operations
3. **Selective Execution**: Run only necessary validation steps for faster feedback
4. **Resource Monitoring**: Monitor system resources during intensive operations

### Extension Guidelines

1. **Follow Naming Conventions**: Use descriptive names following existing patterns
2. **Include Documentation**: Add docstrings and usage examples for new scripts
3. **Add Validation**: Include input validation and error handling
4. **Update This README**: Document new scripts in this file

### Best Practices

1. **Atomic Operations**: Design scripts to be atomic and reversible where possible
2. **Comprehensive Testing**: Test scripts thoroughly before production use
3. **Configuration Management**: Use version control for configuration files
4. **Monitoring Integration**: Include monitoring and alerting for production scripts

---

This documentation provides a comprehensive guide to the scripts ecosystem. For questions or contributions, please refer to the project's main documentation or contact the development team.
