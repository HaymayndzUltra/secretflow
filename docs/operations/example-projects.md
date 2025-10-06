# Example Projects Catalog

Use these curated examples to demonstrate the unified workflow and to train operators on realistic scenarios.

## 1. Test Project (`unified_workflow/test-project`)
- **Purpose:** Hands-on sandbox mirroring a typical mid-size engagement.
- **Highlights:**
  - Pre-populated `context-kit`, `project-rules`, and `monitoring-dashboards` directories for reference.
  - `tests/README.md` lists smoke checks suitable for onboarding exercises.
  - `incident-reports/README.md` contains templates for recording dry-run incidents.
- **Suggested Demo:** Review the README files in each subdirectory, then run:
  ```bash
  python -m unified_workflow.cli generate-project --name demo-test-project
  ```

## 2. Integration Test Project (`unified_workflow/integration-test-project`)
- **Purpose:** Validates cross-module integrations before production deployment.
- **Highlights:**
  - Contains synthetic audit reports and monitoring dashboards for acceptance testing.
  - Mirrors the directory structure of production clients, enabling rehearsal of evidence collection workflows.
- **Suggested Demo:**
  ```bash
  python scripts/run_workflow.py --config workflow/templates/workflow_fullstack.yaml --project-root unified_workflow/integration-test-project
  ```

## 3. Template Packs (`template-packs/`)
- **Purpose:** Provide stack-specific accelerators for backend, frontend, and infrastructure targets.
- **Highlights:**
  - Each pack includes a README with setup steps and migration notes.
  - Use in conjunction with `project_generator` to showcase templated project creation.
- **Suggested Demo:**
  ```bash
  python scripts/generate_client_project.py --template backend/fastapi --output dist/fastapi-demo
  ```

## 4. Workflow Templates (`workflow/templates`)
- **Purpose:** Offer baseline workflow definitions for backend-only and full-stack engagements.
- **Suggested Demo:**
  ```bash
  python scripts/run_workflow.py --config workflow/templates/workflow_fullstack.yaml --verbose
  ```

## Usage Tips
- Capture outputs in the `artifacts/` directory for reuse during training.
- Pair each demo with the [Operator Quickstart](./operator-quickstart.md) so trainees can follow along.
- Log scenario outcomes in the [Training Retro](../../artifacts/training/retro.md) document.
