# Workflow Templates

Ang `workflow/` directory ay naglalaman ng reusable na blueprint files na ginagamit ng AI Governor pipelines para bumuo ng project workflows at evidence gates. Mga declarative assets ang nasa loob—walang executable code—kaya ligtas itong i-consume mula sa automation.

## Nilalaman

| File | Deskripsyon |
| --- | --- |
| [`templates/workflow_fullstack.yaml`](templates/workflow_fullstack.yaml) | YAML preset para sa fullstack engagements (Next.js + FastAPI + Postgres + Auth0 + Docker). |
| [`templates/workflow_backend.yaml`](templates/workflow_backend.yaml) | Backend-only variant (FastAPI + Postgres + internal auth + Terraform deploy). |
| [`templates/evidence_schema.json`](templates/evidence_schema.json) | JSON Schema na ginagamit upang i-validate ang evidence `manifest.json` files sa `workflow1/evidence/`. |
| [`templates/submission_checklist.md`](templates/submission_checklist.md) | Markdown checklist na pwedeng kopyahin sa final submission packs. |

> **Tandaan:** Ang `workflow/gate_controller.yaml` na tinutukoy sa mga YAML preset ay inaasahang nasa upper-level automation layer.

## Paano Gamitin

1. **Workflow selection** – Pumili sa pagitan ng `workflow_fullstack.yaml` o `workflow_backend.yaml` depende sa uri ng proyekto.
2. **Evidence structure** – Parehong YAML preset ay naglalarawan ng ordered `evidence_structure` na dapat tularan ng iyong evidence directories.
3. **Stack metadata** – I-customize ang `stacks` block kung mag-iiba ang tech choices; tinitingnan ito ng generator kapag gumagawa ng CI/CD at DevEx assets.
4. **Compliance matrix** – Dagdagan o bawasan ang entries upang tumugma sa target certifications. Ito rin ang baseline na isinasama sa submission checklist.
5. **Readiness checklist** – Opsyonal na palitan ang listahan para tumugma sa internal exit criteria ng iyong koponan.

## Evidence Schema

- Ang schema ay nag-e-enforce na bawat artifact entry ay may `path`, `category`, `description`, `checksum` (SHA-256), at `created_at` timestamp.
- Kapag gumagamit ng Python automation, maaari mong i-validate ang manifest gamit ang `jsonschema` package:
  ```python
  import json
  from jsonschema import validate
  from pathlib import Path

  schema = json.loads(Path("workflow/templates/evidence_schema.json").read_text())
  manifest = json.loads(Path("workflow1/evidence/phase2/manifest.json").read_text())
  validate(instance=manifest, schema=schema)
  ```

## Pag-customize

- Kapag nagde-define ng bagong workflow, kopyahin ang isa sa YAML files bilang panimulang punto at i-update ang `project_type`, `stacks`, at `compliance_matrix`.
- Tiyaking ina-update din ang anumang tooling na umaasa sa `submission_checklist.md` kung babaguhin ang checklist (hal. QA gating bots).
