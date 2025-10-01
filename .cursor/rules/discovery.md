
---
description: "TAGS: [client,discovery,codex,questions,forms] | TRIGGERS: jobpost,discovery client | SCOPE: global | DESCRIPTION: Reusable rules and instructions for conducting project discovery from client job posts (e.g., Upwork). Provides tailored questions, forms, and Codex integration for flexible, AI-informed processes."
globs: docs/brief/jobpost.md
alwaysApply: false
---


# Client Discovery Guide: Rules and Instructions

## System Overview
This rule defines a structured, understanding-based process for transforming client job posts into actionable discovery insights. It's not automation—it's adaptive guidance for asking questions, clarifying details, and gathering input, tailored to project variability. Integrates with Codex Generator/Execution for seamless brief creation and phase progression.

- **Purpose**: Ensure discovery is thorough, client-specific, and Codex-aligned without rigid scripts.
- **Scope**: Covers questions, forms, and Codex handoff. Adapt based on job post (e.g., web vs. ML).
- **Usage**: Reference for interviews; synthesize outputs into `docs/brief/jobpost.md` before prompting Codex Generator.

## Strict Rules for Discovery
Adhere to these [STRICT] directives for effective, evidence-based discovery. Each rule enforces Codex compliance and flexibility.

1. **[STRICT] Input Analysis**  
   - Review the client's job post for key elements (e.g., scope, constraints). Identify gaps (e.g., vague requirements) and tailor questions accordingly. Evidence: Aligns with Codex Phase 0 (Bootstrap) – extract implicit needs from unstructured inputs.

2. **[STRICT] Question Prioritization**  
   - Start with broad questions, then narrow to specifics. Probe for examples, edge cases, and metrics. Clarify ambiguities immediately (e.g., "What does 'user-friendly' mean?"). Evidence: Mirrors Codex Phase 1 (PRD) – ensures acceptance criteria are measurable and tied to user journeys.

3. **[STRICT] Form Usage**  
   - Use provided forms for structured client input if preferred. Customize fields based on project type. Log all responses for traceability. Evidence: Supports Codex validation loops – builder/auditor/challenger can reference documented inputs.

4. **[STRICT] Synthesis and Documentation**  
   - Compile responses into a brief (e.g., `docs/brief/jobpost.md`) with sections: Goals, Stakeholders, Constraints, Requirements. Cite evidence from discovery. Evidence: Feeds Codex Generator (Step 1: Project Fingerprinting) for schema generation.

5. **[STRICT] Codex Integration**  
   - Post-discovery, prompt Codex Generator: "Analyze this brief and generate full project system: Personas, protocols, schemas for [project type]." Run Execution phases for validation. Evidence: Ensures outputs satisfy Codex invariants (e.g., evidence paths, quality gates).

6. **[STRICT] Iteration and Quality**  
   - Conduct 1–2 sessions; refine based on feedback. Achieve Codex-style "PASS" via self-review. Evidence: Enforces session management (Builder → Auditor → Challenger) from Codex rules.

## Tailored Questions by Project Type
These questions are adaptive—select based on the job post. Ask verbally or via email for AI-level understanding.

### 1. Web Application/Full-Stack
   - Core Questions:
     - What specific problem does this app solve, and who are the main users? (Probe: Daily pain points?)
     - What are the must-have features? (E.g., User login, dashboards, integrations?)
     - Any tech preferences or constraints? (E.g., Frontend framework, database type?)
     - Timeline, budget, and success metrics? (E.g., "App loads in <2s"?)
     - Who are the stakeholders? (E.g., Who approves changes?)
     - Edge cases or risks? (E.g., What if users have slow internet?)
   - Clarification Prompts: "Can you walk me through a typical user journey?" or "What happens in error scenarios?"

### 2. Data Pipeline/Analytics
   - Core Questions:
     - What data sources will we use, and what's the end goal? (E.g., Dashboards, predictions?)
     - Data quality or regulations? (E.g., Privacy laws, accuracy needs?)
     - Who accesses the outputs? (E.g., Analysts, executives?)
     - Scale and frequency? (E.g., Data volume, daily processing?)
     - Transformations needed? (E.g., Cleaning, aggregation?)
     - Risks? (E.g., What if data is delayed?)
   - Clarification Prompts: "Give an example of a data flow" or "How do you measure success here?"

### 3. Machine Learning/AI
   - Core Questions:
     - What's the ML objective? (E.g., Classification, recommendations?)
     - Training data details? (E.g., Sources, size, quality?)
     - Ethical or deployment needs? (E.g., Bias checks, cloud vs. on-premise?)
     - Who evaluates the model? (E.g., Data scientists, end-users?)
     - Metrics for success? (E.g., Accuracy >95%?)
     - Retraining or maintenance? (E.g., If performance drops?)
   - Clarification Prompts: "What does 'accurate' mean in your context?" or "Any explainability requirements?"

### 4. General/Other Projects
   - Core Questions (Adaptable):
     - Core problem and goals? (E.g., Automate X to achieve Y?)
     - Key deliverables? (E.g., Code, docs, training?)
     - Constraints? (E.g., Budget, tech limits?)
     - Stakeholders? (E.g., Input providers, approvers?)
     - Success metrics? (E.g., Measurable outcomes?)
     - Dependencies or risks? (E.g., Third-party tools?)
   - Clarification Prompts: "Can you specify what 'efficient' means?" or "What if [scenario] happens?"

## Forms for Client Input
Use these templates (e.g., in Google Forms or shared docs) for structured responses. Copy-paste and adapt.

### Basic Project Form (Universal)
- **Project Overview**:
  - Problem Statement: [Text box]
  - Target Users/Audience: [Dropdown: Consumers, Businesses, Internal Team]
- **Scope & Features**:
  - Must-Have Features: [Checkboxes]
  - Nice-to-Haves: [Rating scale: 1-5]
- **Technical & Constraints**:
  - Preferred Tech Stack: [Multiple choice]
  - Timeline: [Date picker]
  - Budget: [Range slider]
  - Regulations/Compliance: [Text box]
- **Stakeholders & Metrics**:
  - Key Contacts: [Table: Name, Role, Email]
  - Success Indicators: [Text box]
- **Additional Notes**: [Open text]

### Advanced Form (For ML/Data)
- Add to Basic Form:
  - Data Sources: [List]
  - Model Type: [Dropdown]
  - Deployment: [Multi-choice]
  - Risks/Ethics: [Text box]

## Step-by-Step Process
1. **Prep**: Analyze job post; select questions/forms.
2. **Engage**: Ask questions; use forms.
3. **Clarify**: Follow up on ambiguities.
4. **Synthesize**: Build brief with evidence.
5. **Codex Handoff**: Prompt Generator; run Execution.
6. **Validate**: Ensure "PASS" per Codex rules.

## Examples and Tips
- **Example Flow**: For a web app, start with "What's the problem?" → Features → Tech → Metrics.
- **Tip**: Record sessions; use "If X, then Y?" for edges.
- **Codex Tie-In**: Brief must cover Phase 0 elements for Generator compatibility.

## Troubleshooting
- Vague Responses: Ask for examples.
- Overload: Limit to 5–7 questions.
- Integration: If Codex fails, check brief completeness.

## Success Criteria
- Discovery complete in ≤3 days.
- Brief includes all Codex Phase 0/1 elements.
- Client responses documented and traceable.

This rule is self-contained—save and reference anytime for permanent use.