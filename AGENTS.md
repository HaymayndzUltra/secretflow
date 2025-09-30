## **`[STRICT]`** SCOPE AND INTENT
- **`[STRICT]`** Covered files: `/.cursor/rules/Codex-Meta-Framework-Genarator.mdc` (Generator), `/.cursor/rules/Codex-Meta.mdc` (Execution).
- **`[STRICT]`** Alignment goal: Generator (meta, “creates the system”) and Execution (operational, “runs the system”) must share the same lifecycle model (phases/personas/protocols/gates) and differ only by perspective (generate vs operate).

## **`[STRICT]`** CANONICAL SOURCE OF TRUTH
- **`[STRICT]`** Structure canon: Generator defines the canonical structure (phases, required artifacts, schemas, validation orchestration).
- **`[STRICT]`** Operational canon: Execution mirrors the Generator structure as actionable, pre-baked rules for immediate use.
- **`[STRICT]`** Any structural change in Generator MUST be reflected in Execution in the same change set (same PR/commit).

## **`[STRICT]`** INVARIANTS (MUST MATCH 1:1)
- **`[STRICT]`** Phase Set and Order: Phases 0–6 with the same names and sequence.
- **`[STRICT]`** Personas: Exact titles and intent per phase (Builder, Auditor, Challenger where applicable).
- **`[STRICT]`** Session Protocol: Builder → Auditor → Challenger → Convergence PASS.
- **`[STRICT]`** Prefix Discipline: All directives use `[STRICT]` or `[GUIDELINE]` consistently.
- **`[STRICT]`** Quality Gates: Same categories (static, dynamic, policy, ADR) present in both.
- **`[STRICT]`** Evidence Paths: Identical output paths (e.g., `evidence/phaseN/...`, `var/validation/phase-N/...`).
- **`[STRICT]`** Contracts/Schemas: Generator lists emitted schemas; Execution must reference and obey them.
- **`[STRICT]`** Examples: Each phase includes ✅/❌ examples in both files.

## **`[STRICT]`** STRUCTURAL MAPPING (GEN → EXEC)
- **`[STRICT]`** Purpose/Overview → System Overview
- **`[STRICT]`** Core Outcomes → Expected Outcomes
- **`[STRICT]`** Meta-Generator Protocol (Steps 1–6) → Phase protocols and session management explained for operation
- **`[STRICT]`** Canonical Phase Set → Per-phase personas + responsibilities + outputs
- **`[STRICT]`** Quality Gates (Global) → Quality rails and audits
- **`[STRICT]`** Invocation Contract → Session management and run order
- **`[STRICT]`** Success Criteria → Phase completion/validation in Execution

## **`[STRICT]`** VERSIONING AND SYNC TAGS
- **`[STRICT]`** Add header fields to both files:
  - `codexAlignmentVersion: <semver>`
  - `codexAlignmentHash: <shared-stable-id>`
- **`[STRICT]`** A PR that updates one file MUST bump `codexAlignmentVersion` in both and set the same `codexAlignmentHash`.

## **`[STRICT]`** CHANGE MANAGEMENT
- **`[STRICT]`** Structural changes (phases/personas/paths/gates) are forbidden unless both files update together.
- **`[STRICT]`** New phases/personas require:
  - Generator: new Inputs/Process/Outputs/Success/Examples + schemas.
  - Execution: corresponding Persona, Responsibilities, Validation, and Outputs.
- **`[STRICT]`** Deletions must remove mirrored content in both files and update references.

## **`[STRICT]`** ALIGNMENT VALIDATION (LIGHTWEIGHT SCHEMAS)
- **`[STRICT]`** Maintain an alignment manifest (implicit, derived from both files) with at least:
  - `phaseSet[]`, `personasByPhase{}`, `evidencePaths[]`, `qualityGateCategories[]`, `hasStrictGuidelinePrefixes: boolean`.
- **`[GUIDELINE]`** Optional JSON schema for automated checks (store under `/var/schemas/alignment/alignment.schema.json`):

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Codex Alignment",
  "type": "object",
  "required": ["phaseSet", "personasByPhase", "evidencePaths", "qualityGateCategories", "hasStrictGuidelinePrefixes"],
  "properties": {
    "phaseSet": {
      "type": "array",
      "items": {"type": "string"},
      "minItems": 7,
      "uniqueItems": true
    },
    "personasByPhase": {
      "type": "object",
      "additionalProperties": {
        "type": "array",
        "items": {"type": "string"},
        "minItems": 1
      }
    },
    "evidencePaths": {
      "type": "array",
      "items": {"type": "string", "pattern": "^(evidence/phase\\d+/|var/validation/phase-\\d+/)"}
    },
    "qualityGateCategories": {
      "type": "array",
      "items": {"enum": ["static", "dynamic", "policy", "adr"]},
      "minItems": 4,
      "uniqueItems": true
    },
    "hasStrictGuidelinePrefixes": {"type": "boolean", "const": true}
  }
}
```

## **`[STRICT]`** CI/GATE ENFORCEMENT (POLICY)
- **`[STRICT]`** Block merges when:
  - Phase sets differ, or ordering differs.
  - Missing any persona in either file for a given phase.
  - Evidence paths mismatch or are missing.
  - `[STRICT]/[GUIDELINE]` prefixes absent in any directive section.
  - `codexAlignmentVersion` or `codexAlignmentHash` do not match across both files.
- **`[GUIDELINE]`** Add a repo check that parses both files to compute a derived alignment manifest and validate via the schema above.

## **`[STRICT]`** ✅/❌ EXAMPLES
- ✅ Update adds “Phase 7 — Sunset”:
  - Generator: adds Step mapping, I/O schemas, outputs, success criteria, examples.
  - Execution: adds Persona, Responsibilities, Validation, Evidence outputs.
  - Both bump `codexAlignmentVersion` and share a new `codexAlignmentHash`.
- ❌ Generator adds a new evidence path but Execution keeps old paths.
- ❌ Execution adds a new persona title differing from Generator’s (e.g., “QA Lead” vs “AI Quality Assurance Specialist”).
- ❌ One file uses gates “security/perf/a11y/test” while the other removes “policy/ADR”.

## **`[GUIDELINE]`** EXTENSIBILITY
- **`[GUIDELINE]`** If regulated domains require extra phases (e.g., Threat Modeling), append in both with identical naming and references.
- **`[GUIDELINE]`** Keep a short “Diff Log” section at the bottom of both files referencing the latest `codexAlignmentHash`.