# AI Protocol Examples Reference Guide

This guide documents the canonical structure for AI Protocol System files and points to domain-specific examples included in this repository.

## Protocol Structure Blueprint

Each protocol follows the same high-integrity structure:

1. **Title block** – `# PROTOCOL X: NAME`
2. **AI Role** – Persona definition plus output expectations
3. **Input section** – Required context and artifacts
4. **Algorithm** – Phased steps using `[CRITICAL]`, `[MUST]`, `[STRICT]`, or `[GUIDELINE]`
5. **Templates** – Task checklists using `[APPLIES RULES: {...}]`
6. **Final Output Template** – Markdown template with tasks and metadata fields

Refer to the Content Strategy bootstrap example for a full implementation of this pattern.【F:ai-protocol-examples/content-creation/0-content-strategy-bootstrap.md†L1-L89】

## Domain Example Index

- **Content Creation** – Strategic planning for editorial initiatives.【F:ai-protocol-examples/content-creation/0-content-strategy-bootstrap.md†L1-L89】
- **Data Analysis** – Discovery and planning for analytical projects.【F:ai-protocol-examples/data-analysis/1-data-discovery-planning.md†L1-L91】
- **Project Management** – Cross-functional execution orchestration.【F:ai-protocol-examples/project-management/2-project-execution-orchestration.md†L1-L97】
- **Client Workflow** – Discovery processes for client engagements.【F:ai-protocol-examples/client-workflow/0-client-discovery.md†L1-L87】

## Template Generator

Use `templates/protocol-template.md` as a starter when creating new protocols. It encapsulates the required headings, phase sections, task templates, and output scaffolding.【F:ai-protocol-examples/templates/protocol-template.md†L1-L83】

## Integration Notes

The integration guide outlines how these examples connect to automation scripts, review protocols, and quality gates used across SecretFlow.【F:ai-protocol-examples/integration-guide.md†L1-L95】

