# 📖 THE DEFINITION PROTOCOL

**The foundation of the entire problem-solving tree.**

---

## ⚠️ CRITICAL RULE: NO AMBIGUITY

**A definition must be so clear that a stranger could solve it without asking the user.**
- **Bad:** "Fix the bug."
- **Good:** "Fix the `IndexError` in `data_loader.py` line 42 when parsing CSVs with missing headers."

---

## 1️⃣ THE RESEARCH PHASE (Contextual Retrieval)
**Before defining the problem, you MUST search for existing knowledge.**

1.  **Local Search:** Run `grep -r "keywords" problems/` to check for prior art in this project.
2.  **Web Search:** Run `google_search` for:
    - Best practices ("What is the standard way to do X?")
    - Libraries ("Is there a Python library for X?")
    - Solutions ("How to fix error Y")
3.  **Integrate:** Reference these findings in the Context section.

---

## 2️⃣ THE OBJECT: `definition.md`
- **Location**: Inside the problem folder (e.g., `problems/P1/definition.md`).
- **Format**:

```markdown
<!-- 
THINKING PROCESS:
... (Internal monologue on scope and retrieval results) ...
-->

# Problem Definition: [Name]

## 1. Goal
[One specific, measurable sentence describing the desired outcome.]

## 2. Scope
- **In-Scope:** [List what we WILL do]
- **Out-of-Scope:** [List what we will NOT do]

## 3. Context (Research Results)
- **Background:** [Why are we doing this?]
- **Local Findings:** [Results from grep search. e.g., "Similar to P4."]
- **Web Findings:** [Results from Google. e.g., "Found library `pandas` is best for this."]
- **Constraints:** [Hard rules, e.g., "Must use Python 3.9"]

## 4. Success Criteria
The problem is solved when:
1. [Metric A] is true.
2. [Metric B] is true.
3. User approves output.
```

---

## 3️⃣ THE TRIGGER
1.  **Create** `definition.md`.
2.  **Update** `status.md`:
    - Mark `[x] Definition`.
    - Mark `[*] Questions` (Move to next step).
