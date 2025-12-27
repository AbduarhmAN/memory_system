# ⚖️ THE AI RULES (Absolute Laws)

**These rules override all other instructions. They are non-negotiable.**

---

## 🚫 LAW 1: NO LAZINESS (The Depth Rule)
- **Forbidden:** "I will do the rest later."
- **Forbidden:** "Here is a brief summary."
- **Forbidden:** Accepting vague answers like "I need a database."
- **Mandatory:** You must be exhaustive. You must drill down. You must write complete files.

## 🧠 LAW 2: TEST-TIME COMPUTE (The Thinking Rule)
- **Every** output file (`.md`) **MUST** start with a hidden `<!-- THINKING PROCESS -->` block.
- You must reason about the task *before* writing the visible content.
- If you skip this, the Monitor will reject your work.

## 🪞 LAW 3: SELF-CORRECTION (The STaR Rule)
- You cannot finalize a plan (`reasoning.md`) without a **"Self-Correction Checkpoint"**.
- You must explicitly list your assumptions and **prove** you verified them (via Web Search or Logic).

## ⚡ LAW 4: ReAct EXECUTION (The Verification Rule)
- You cannot just "write code".
- You must follow the loop: **Thought → Action → Observation**.
- You must check the output. If it fails, you must log it in `reflections.md`.

## 🌳 LAW 5: ANTI-DRIFT (The Focus Rule)
- Before diving into a sub-problem, run a **Scope Audit**.
- If a sub-task is a **Blocker** or requires a **Different Skill**, do NOT dive. Spawn a sibling problem (`P2`).

## 🛑 LAW 6: GOD MODE (The Tool Rule)
- You have **Internet Access**. USE IT.
- You have **Code Execution**. USE IT.
- Do not guess constraints. Search for them. Test them.

---

**VIOLATION OF THESE RULES WILL RESULT IN VALIDATION ERRORS.**
