# 🧪 THE SYNTHESIS PROTOCOL (Generative Agents)

**The mechanism for merging child solutions into parent knowledge.**

---

## ⚠️ CRITICAL RULE: ABSTRACTION & INSIGHT

**DO NOT JUST SUMMARIZE.**
You must extract **High-Level Insights** from the low-level details of the sub-problems.
This creates a "Memory Stream" of learned truths that persists up the tree.

---

## 1️⃣ THE PURPOSE
- **Combine**: Merge the outputs of `sub/P1.1`, `sub/P1.2`, etc.
- **Abstract**: Turn "I ran SQL query X" into "The database schema requires X."
- **Close**: Mark the parent folder as complete.

---

## 2️⃣ THE INPUT
- Read `status.md` to confirm all children are `[x] DONE`.
- Read `sub/*/FINAL_SOLUTION.md` (or `solution.md`) from all children.

---

## 3️⃣ THE FORMAT: `FINAL_SOLUTION.md`

```markdown
<!-- 
THINKING PROCESS:
... (Internal monologue on how the pieces fit together) ...
-->

# Final Solution for [Problem Name]

## 1. Executive Summary
[Brief high-level description of the solution]

## 2. Component Integration
- **Child P1.1 ([Name]):** [What it did]
- **Child P1.2 ([Name]):** [What it did]
- **Integration:** How do they talk to each other? (e.g., P1.1 provides JSON for P1.2)

## 3. 🧠 HIGH-LEVEL INSIGHTS (Generative Memory)
*What did we learn about the system/world during this process?*
- **Constraint Discovery:** [e.g., "We learned that the API rate limit is 50/min, not 100/min."]
- **Pattern Recognition:** [e.g., "All authentication errors stem from the missing header X."]
- **Best Practice:** [e.g., "Future tasks should use Method B instead of A."]

## 4. The Output
[The actual code, file, or final answer]

```

---

## 4️⃣ THE PRUNING (Tree of Thoughts)
If this synthesis involved **Competing Branches** (`Option_A` vs `Option_B`):
1. Explicitly state the winner in Section 1.
2. Explain *why* A beat B in Section 3 (Insights).
3. (Optional) You may delete the losing folder now to save space, or mark it `[x] REJECTED` in `status.md`.

---

## 5️⃣ THE COMPLETION
1. Write `FINAL_SOLUTION.md`.
2. Update `status.md`: Mark `[x] SYNTHESIS`.
3. **Trigger POP**: Move `Current_Focus` to the parent folder.
