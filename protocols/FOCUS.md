# 📍 THE FOCUS POINTER ALGORITHM (Branching & Pruning + Anti-Drift)

**The mechanism that controls the AI's "Position" in the project tree.**

## 1️⃣ THE OBJECT: `Current_Focus.txt`
- **Location**: Project Root.
- **Content**: **RELATIVE PATH ONLY** from the project root.
- **Example**: `problems/P1/sub/P1.3/` (Correct).
- **Forbidden**: `e:\Projects\...` (Absolute paths break the system).

---

## 🔄 THE CYCLE (Step-by-Step)

### A. THE WAKE-UP (Relative Logic)
1.  **Detect Root**: Get current workspace directory.
2.  **Read Focus**: Read `Current_Focus.txt` (e.g., `problems/P1/`).
3.  **Navigate**: Go to that target folder.

### B. THE STATE CHECK
1.  Read the local `status.md`.
2.  Is there an unchecked `[ ]` item?
    - **YES**: Go to Step C (Dive Check).
    - **NO**: Go to Step D (The Pop).

### C. THE DIVE (Moving Down)
1.  Select the unchecked item (Target).
2.  Is Target **Complex** (needs sub-folder)?
    - **YES**:
        1. **🛑 SCOPE AUDIT (The Anti-Drift Check):**
           - Does this sub-problem require a different **Skill Set**? (e.g., Dev vs. DevOps)
           - Is it a **Blocker** rather than a **Step**?
           - *If YES:* **DO NOT DIVE.**
             1. Create new Sibling/Parent Problem (e.g., `problems/P2_FixServer`).
             2. Mark current item `[ ] BLOCKED by P2`.
             3. Switch Focus to `P2`.
           - *If NO (It fits):*
             1. Create new folder `Target/`.
             2. **CRITICAL**: Overwrite `Current_Focus.txt` with **RELATIVE PATH** `path/to/Target/`.
             3. **STOP**. (Next turn wakes up in Target).
    - **NO** (Atomic):
        1. Solve locally.
        2. Mark `[x]`.
        3. Repeat Step B.

#### 🌳 BRANCHING LOGIC (Tree of Thoughts)
If `status.md` lists **Competing Options** (e.g., `Option_A`, `Option_B`):
1.  Dive into `Option_A` first. Solve it.
2.  Pop back.
3.  Dive into `Option_B` next. Solve it.
4.  Pop back.
5.  **Trigger Synthesis**: Compare A vs B in the parent's `FINAL_SOLUTION.md`.
6.  **Prune**: You may delete the losing folder if desired, or keep it for record.

### D. THE POP (Moving Up)
1.  All items in `status.md` are `[x]`.
2.  Identify **Parent Path** (remove last folder from current relative path).
3.  **CRITICAL**: Overwrite `Current_Focus.txt` with **RELATIVE PATH**.
4.  **STOP**. (Next turn wakes up in Parent).
