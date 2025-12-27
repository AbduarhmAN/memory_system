# 🪞 THE REFLEXION PROTOCOL (Verbal RL + Global RAG)

**The mechanism for persistent self-improvement.**

---

## 1️⃣ THE PURPOSE
To prevent the AI from making the same mistake twice.
If an error occurs (validation failure, code crash, logical dead-end), it MUST be recorded here.

---

## 2️⃣ THE OBJECT: `reflections.md`
- **Location**: Inside the specific problem folder (e.g., `problems/P1/reflections.md`).
- **Format**:
  ```markdown
  ## [YYYY-MM-DD HH:MM] Error Type
  - **Context**: What was I trying to do?
  - **Failure**: What actually happened? (The Error)
  - **Analysis**: WHY did it fail? (Root Cause)
  - **Lesson**: What will I do differently next time? (The Rule)
  ```

---

## 3️⃣ THE TRIGGER
You MUST run this protocol when:
1. `monitor_project.py` flags a validation error.
2. A script crashes or produces wrong output.
3. You realize a `reasoning.md` plan was flawed and needs rewriting.

---

## 4️⃣ THE LOOP (Wake-Up & Global RAG)
**Before doing ANYTHING in a folder:**

1.  **Local Check:** Read the local `reflections.md` (if exists).
2.  **Global Search (RAG):**
    - Run `grep -r "Lesson" problems/ | grep "keyword"` to find lessons from *other* problems.
    - Example: If writing SQL, search for "SQL" lessons in all `reflections.md` files.
3.  **Integrate:**
    - Incorporate these lessons into your context.
    - > *Self-Correction: "I found a lesson in P3 that says 'Always close DB connections'. I will apply that here."*
