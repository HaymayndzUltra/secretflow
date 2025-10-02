# PROTOCOL {index}: {Protocol Name}

## AI ROLE
You are a **{Persona Title}**. {Mission statement summarizing responsibilities and success criteria.}

**Your output should be {Output Type}, not prose.**

## INPUT
- {Primary input artifacts}
- {Additional context or approvals required}

---

## {Protocol Name} ALGORITHM

### PHASE 1: {Phase 1 Title}
1. **`[CRITICAL]` {Step Name}:** {Step description}
   - **1.1. {Sub-step}:** {Sub-step instructions or command}
   - **1.2. {Sub-step}:** {Sub-step instructions or command}
2. **`[MUST]` {Step Name}:** {Step description}
3. **`[STRICT]` {Step Name}:** {Step description}

### PHASE 2: {Phase 2 Title}
1. **{Step Name}:** {Step description}
2. **{Step Name}:** {Step description}
3. **{Step Name}:** {Step description}

### PHASE 3: {Phase 3 Title}
1. **{Step Name}:** {Step description}
2. **{Step Name}:** {Step description}

---

## {Protocol Name} TEMPLATES

### Template A: {Template Name}
```markdown
- [ ] X.0 **{Task Name}**
  - [ ] X.1 **{Sub-task}:** {Description and validation} [APPLIES RULES: {rule-name-1}]
  - [ ] X.2 **{Sub-task}:** {Description and validation} [APPLIES RULES: {rule-name-2}]
```

### Template B: {Template Name}
```markdown
- [ ] Y.0 **{Task Name}**
  - [ ] Y.1 **{Sub-task}:** {Description and validation} [APPLIES RULES: {rule-name-1}]
  - [ ] Y.2 **{Sub-task}:** {Description and validation} [APPLIES RULES: {rule-name-2}]
```

> **Command Pattern:** Use `/load {resource}` to load prerequisite assets and `@apply {path-to-protocol} --mode {mode}` to invo
ke review or quality gates.

---

## FINAL OUTPUT TEMPLATE

```markdown
# {Output Title}: {Variable Name}

Based on {Input}: `{Reference}`

> **{Key Info}:** {Value}
> **{Key Info}:** {Value}

## {Section Name}

### {Subsection}
- **{Item}:** {Description}
- **{Item}:** {Description}

## {Section Name}

- [ ] 1.0 **{Task 1}** [COMPLEXITY: {Simple/Complex}]
> **WHY:** {Business value and impact}
> **Timeline:** {Estimated duration}
- [ ] 2.0 **{Task 2}** [COMPLEXITY: {Simple/Complex}] [DEPENDS ON: 1.0]
> **WHY:** {Business value and impact}
> **Timeline:** {Estimated duration}

## Next Steps

1. **{Step 1}:** {Description}
2. **{Step 2}:** {Description}
3. **{Step 3}:** {Description}
4. **{Step 4}:** {Description}
```

