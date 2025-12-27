# 🧠 THE REASONING PROTOCOL

**The "Decision Matrix" that bridges Questions and Solutions.**

---

## ⚠️ CRITICAL RULE: DETAILED REASONING

**ALL REASONING MUST BE THOROUGHLY EXPLAINED.**
- Never write brief justifications.
- Reference SPECIFIC answers from `questions.md`.
- Explain WHY each approach was considered or rejected.
- Document the complete decision-making process.
- **WHY:** Detailed reasoning ensures the plan is understood and can be verified.

---

## 1️⃣ THE PURPOSE
- `questions.md` gathers **DATA** (The Raw Facts).
- `reasoning.md` processes **STRATEGY** (The Plan).
- `solution.md` executes **ACTION** (The Code).

## 2️⃣ THE INPUT (From `questions.md`)
Before writing `reasoning.md`, the AI MUST read `questions.md` to get the "5 Ws":
- **Who:** Who is the user? What is their role?
- **What:** What are they trying to accomplish?
- **Why:** Why does this matter? What's the motivation?
- **Where:** Where does the data come from? Where does output go?
- **When:** What are the timelines and frequencies?

---

## 3️⃣ THE 5 POWER APPROACHES (Strategy Matrix)

The AI must evaluate the problem using these 5 rigorous lenses. "Speed" and "Laziness" are FORBIDDEN.

### 1. The Recursive Depth Approach
- **Philosophy**: "Divide and Conquer."
- **Focus**: Break the problem into atomic units. Create sub-folders. Dive deep.
- **Use Case**: Complex problems that cannot be solved in one step.
- **CRITICAL ACTION**: If selected, **YOU MUST UPDATE `status.md`** section "CHILDREN" with the new sub-problems immediately!
- **Example Justification:**
  > "Based on Q3 (94+ campaigns) and Q6 (ICB requires email/ages), the problem has 4 distinct sub-problems: parsing, matching, qualifying, reporting. Each requires different code."

### 2. The Fail-Safe System Approach
- **Philosophy**: "Never Crash, Never Forget."
- **Focus**: Build systems with status files, logs, and pointers. Priority on safety and state tracking.
- **Use Case**: Architecture, File Systems, Long-running logic.

### 3. The Exhaustive Verification Approach
- **Philosophy**: "Prove it with Code."
- **Focus**: Write extensive tests. Execute scripts. Check edge cases. Consume max tokens to verify 100%.
- **Use Case**: Critical code, bug fixes, final solutions.

### 4. The God Mode (Unrestricted) Approach
- **Philosophy**: "No Limits."
- **Focus**: Use every tool available. Ignore standard concise limits. Write massive, complete solutions.
- **Use Case**: Solving hard problems that require maximum power.

### 5. The User-Aligned Protocol Approach
- **Philosophy**: "Follow the Negotiated Rules."
- **Focus**: Strictly adhere to the Two-Section Question cycle and specific user constraints.
- **Use Case**: When the user has defined a specific rigid path.

---

## 4️⃣ THE DECISION & ACTION

**Output Format in `reasoning.md` (DETAILED):**

```markdown
# Reasoning for [Problem Name]

## Selected Approach: [Name]

---

## Justification

### Why This Approach?
Based on the following answers from `questions.md`:
- **Q1 Answer:** [Quote relevant part] → This means...
- **Q3 Answer:** [Quote relevant part] → This indicates...
- **Q7 Answer:** [Quote relevant part] → This requires...

### Why NOT Other Approaches?
- **Fail-Safe:** Not needed because... [specific reason]
- **Exhaustive Verification:** Premature because... [specific reason]
- **God Mode:** Overkill for this stage because... [reason]

---

## Plan of Action

### Child Problems (if Recursive Depth)

| Child | Name | Purpose | Dependencies | Key Questions |
|-------|------|---------|--------------|---------------|
| P1.1 | [Name] | [What it solves] | [What it needs] | [Q# refs] |
| P1.2 | [Name] | [What it solves] | [What it needs] | [Q# refs] |

### Execution Order
1. P1.1 first because [reason]
2. P1.2 next because [depends on P1.1]
3. ...

### Success Metrics
1. **P1.1 Success:** [Specific measurable outcome]
2. **P1.2 Success:** [Specific measurable outcome]
```

---

## 5️⃣ CRITICAL TRIGGER

If the plan involves **DECOMPOSITION** (creating sub-problems):
1. **UPDATE `status.md` IMMEDIATELY**.
2. Add the sub-problems to the `## CHILDREN` section.
   ```markdown
   ## CHILDREN
   - [ ] P1.1: [Name] - [Brief purpose]
   - [ ] P1.2: [Name] - [Brief purpose]
   ```
3. This ensures the EXECUTION phase knows to DIVE instead of solving atomically.
