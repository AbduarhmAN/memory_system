# 📝 THE DEFINITION PROTOCOL

**The first step for every problem: Define what we are solving.**

---

## ⚠️ CRITICAL RULE: DETAILED DEFINITIONS

**ALL DEFINITIONS MUST BE COMPREHENSIVE.**
- Never write short, vague descriptions.
- Include ALL context: user role, environment, tools, constraints.
- Document EVERYTHING known about the problem.
- Use sections, bullet points, and tables for clarity.
- **WHY:** Detailed definitions prevent misunderstanding and ensure complete context.

---

## 1️⃣ THE PURPOSE
- Before asking questions, we must know WHAT the problem IS.
- `definition.md` is the "Contract" between AI and User.
- It answers: "What are we trying to achieve?"

---

## 2️⃣ THE STRUCTURE (`definition.md`)

Every `definition.md` MUST contain these sections WITH FULL DETAIL:

```markdown
# [Problem Title]

## Goal
- **Primary Goal:** [Main objective in detail]
- **Secondary Goals:** [Supporting objectives]
- **Target Metrics:** [How success is measured]

## Context

### User Role
- **Position:** [Job title/role]
- **Responsibilities:** [What they do]
- **Team Structure:** [Who they work with]
- **Limitations:** [What they cannot do]

### Environment
- **Tools Used:** [List all tools with details]
- **Data Sources:** [Where data comes from]
- **Integrations:** [What systems connect]

### Background
- **Current State:** [How things work now]
- **Pain Points:** [What problems exist]
- **History:** [Relevant past context]

## Scope

### IN SCOPE (What we WILL solve)
- Item 1 with full explanation
- Item 2 with full explanation
- Item 3 with full explanation

### OUT OF SCOPE (What we will NOT solve)
- Item 1 with reason why excluded
- Item 2 with reason why excluded

## Success Criteria
How do we know when this is DONE?
1. **Criterion 1:** [Specific measurable outcome]
2. **Criterion 2:** [Specific measurable outcome]
3. **Criterion 3:** [Specific measurable outcome]

## Constraints
- **Time:** [Any deadlines or time limits]
- **Technology:** [Any tech restrictions]
- **Resources:** [Any budget or resource limits]
- **Rules:** [Any business rules to follow]

## Dependencies
- **Inputs Needed:** [What this problem needs from elsewhere]
- **Outputs Produced:** [What other problems need from this]
- **Blocking Issues:** [What could block progress]
```

---

## 3️⃣ THE CREATION PROCESS

**Step 1**: Read user's initial problem description THOROUGHLY.
**Step 2**: Extract ALL information: Goal, Context, Scope, Constraints.
**Step 3**: Write `definition.md` with COMPLETE DETAIL.
**Step 4**: Mark `[x] Definition` in `status.md`.
**Step 5**: Move `[*]` to `Questions`.

---

## 4️⃣ VALIDATION

Before marking Definition as DONE, verify:
- [ ] Goal is clear AND detailed (not just one sentence)
- [ ] Context includes user role, environment, tools
- [ ] Scope has IN and OUT sections with explanations
- [ ] Success Criteria are specific and measurable
- [ ] All known constraints documented

If ANY is missing → ASK USER before proceeding.
