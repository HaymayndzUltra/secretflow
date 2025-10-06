# GPT-5-CODEX Investigation Prompt: SecretFlow Dev-Workflow Enhancement

## 🎯 MISSION BRIEFING

You are GPT-5-CODEX, tasked with conducting a comprehensive investigation of the SecretFlow development workflow system. Your mission is to analyze the current AI-driven protocol architecture and determine how to optimize it for complete end-to-end project delivery from client requirements to production deployment.

## 📋 CONTEXT: What is SecretFlow Dev-Workflow?

The SecretFlow dev-workflow is an **AI-driven protocol system** designed to guide development teams through structured project delivery. It consists of:

- **Bootstrap Protocol** (`0-bootstrap-your-project.md`) - Initial project analysis and context engineering
- **PRD Creation** (`1-create-prd.md`) - Product Requirements Document generation
- **Task Generation** (`2-generate-tasks.md`) - Breaking down requirements into actionable tasks
- **Task Processing** (`3-process-tasks.md`) - Implementation workflow
- **Quality Audit** (`4-quality-audit.md`) - Code quality and review protocols
- **Implementation Retrospective** (`5-implementation-retrospective.md`) - Learning and improvement
- **Review Protocols** (`review-protocols/`) - Specialized review frameworks

This system is designed to work with AI assistants to provide consistent, high-quality project delivery.

## 🔍 INVESTIGATION SCOPE

You must thoroughly analyze these components to understand their current state and integration potential:

### Primary Analysis Targets:
1. **Core Workflow** (`/home/haymayndz/secretflow/.cursor/dev-workflow/`)
   - All workflow files and their interconnections
   - Current process flow and dependencies
   - Gaps in the end-to-end delivery pipeline

2. **Rule System** (`/home/haymayndz/secretflow/.cursor/rules/`)
   - Master rules and common rules structure
   - How rules integrate with the workflow
   - Rule enforcement mechanisms

3. **Integration Candidates** (Analyze if these should be part of the workflow):
   - **Template Packs** (`/home/haymayndz/secretflow/template-packs/`)
   - **Scripts** (`/home/haymayndz/secretflow/scripts/`)
   - **Project Generator** (`/home/haymayndz/secretflow/project_generator/`)
   - **GitHub Workflows** (`/home/haymayndz/secretflow/.github/`)

### Secondary Analysis (if needed):
- **Entire Codebase** - Only if primary analysis reveals significant gaps

## 🧠 ANALYSIS FRAMEWORK

### Phase 1: Understanding Current Architecture
1. **Map the Current Workflow**
   - Document each step in the dev-workflow
   - Identify input/output dependencies between steps
   - Understand the AI-human collaboration model
   - Note any existing automation or tooling

2. **Analyze Rule Integration**
   - How do rules guide each workflow step?
   - What enforcement mechanisms exist?
   - Are there gaps in rule coverage?

### Phase 2: Component Analysis
For each integration candidate, determine:
1. **Purpose and Functionality**
   - What does this component do?
   - What problems does it solve?
   - What are its inputs and outputs?

2. **Workflow Integration Potential**
   - Which workflow steps could benefit from this component?
   - How would it enhance the current process?
   - What dependencies would it create?

3. **End-to-End Impact**
   - How does this component contribute to complete project delivery?
   - What gaps would it fill?
   - Would it create new dependencies or complexity?

### Phase 3: Gap Analysis
1. **Identify Missing Capabilities**
   - What's needed for true end-to-end delivery?
   - Where are manual processes that could be automated?
   - What client-facing capabilities are missing?

2. **Integration Opportunities**
   - Which components should be integrated?
   - What new components might be needed?
   - How should the workflow be restructured?

## 📊 REQUIRED DELIVERABLES

### 1. Comprehensive Analysis Report
**Format**: Structured markdown document with sections:

```markdown
# SecretFlow Dev-Workflow Analysis Report

## Executive Summary
- Current state assessment
- Key findings
- Recommended approach

## Current Architecture Analysis
### Workflow Mapping
- Step-by-step process flow
- Dependencies and handoffs
- AI-human collaboration points

### Rule System Analysis
- Rule coverage and enforcement
- Integration with workflow steps
- Effectiveness assessment

## Component Analysis
### Template Packs
- Purpose and capabilities
- Integration potential
- Recommendation

### Scripts
- Purpose and capabilities
- Integration potential
- Recommendation

### Project Generator
- Purpose and capabilities
- Integration potential
- Recommendation

### GitHub Workflows
- Purpose and capabilities
- Integration potential
- Recommendation

## Gap Analysis
- Missing capabilities for end-to-end delivery
- Process inefficiencies
- Automation opportunities

## Integration Recommendations
- Which components to integrate
- How to integrate them
- New components needed
- Workflow modifications required
```

### 2. Gap Analysis Matrix
**Format**: Table showing gaps and solutions

| Gap Category | Current State | Missing Capability | Proposed Solution | Priority |
|--------------|---------------|-------------------|-------------------|----------|
| Client Onboarding | Manual | Automated project setup | Template integration | High |
| ... | ... | ... | ... | ... |

### 3. Integration Roadmap
**Format**: Step-by-step implementation plan

```markdown
# Integration Implementation Roadmap

## Phase 1: Foundation (Weeks 1-2)
### Step 1.1: [Specific Action]
- **Objective**: [Clear goal]
- **Implementation**: [Specific steps]
- **Acceptance Criteria**: [Measurable outcomes]
- **Dependencies**: [What's needed first]

### Step 1.2: [Next Action]
- [Same format]

## Phase 2: Core Integration (Weeks 3-4)
[Continue pattern]

## Phase 3: Enhancement (Weeks 5-6)
[Continue pattern]
```

### 4. Acceptance Criteria Matrix
**Format**: Detailed criteria for each recommendation

| Recommendation | Success Criteria | Validation Method | Priority | Effort |
|----------------|------------------|-------------------|----------|---------|
| Integrate Template Packs | 1. Templates auto-load in bootstrap<br>2. Project structure generated<br>3. AI can customize templates | Manual testing + AI validation | High | Medium |
| ... | ... | ... | ... | ... |

## ✅ SUCCESS CRITERIA

Your investigation will be considered successful if you deliver:

1. **Complete Understanding**: You can explain how every component works and fits together
2. **Clear Recommendations**: Specific, actionable steps for integration
3. **End-to-End Vision**: A complete picture of how the enhanced workflow delivers projects from client request to production
4. **Implementation Clarity**: Detailed steps that another developer could follow
5. **Measurable Outcomes**: Clear acceptance criteria for each recommendation

## 🚨 INVESTIGATION PROTOCOL

### Critical Instructions:
1. **DO NOT MAKE ASSUMPTIONS** - Read and analyze actual files
2. **INVESTIGATE THOROUGHLY** - Don't skip any component
3. **THINK SYSTEMATICALLY** - Consider the entire workflow, not just individual pieces
4. **FOCUS ON END-TO-END** - Always consider how changes affect complete project delivery
5. **BE SPECIFIC** - Provide concrete, actionable recommendations

### Investigation Process:
1. **Start with Core Workflow** - Understand the current system completely
2. **Analyze Each Component** - Determine purpose and integration potential
3. **Identify Gaps** - What's missing for complete delivery?
4. **Propose Solutions** - How to fill gaps and optimize workflow
5. **Create Implementation Plan** - Specific steps with acceptance criteria

### If You Need More Information:
- **First**: Analyze the entire codebase structure
- **Then**: Ask specific questions about unclear areas
- **Finally**: Propose additional investigation if needed

## 🎯 FINAL DELIVERABLE

Provide a single comprehensive document that includes:
1. Complete analysis report
2. Gap analysis matrix
3. Integration roadmap
4. Acceptance criteria matrix

**Format**: Save as `secretflow-workflow-enhancement-analysis.md`

---

**Remember**: Your goal is to help create the most effective, complete end-to-end project delivery system possible. Take your time, investigate thoroughly, and provide recommendations that will genuinely improve the workflow for real-world project delivery.
