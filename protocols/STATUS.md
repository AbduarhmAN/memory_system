# 🚦 THE STATUS PROTOCOL (v7.5)

**The State Machine that drives the project.**

---

## 1️⃣ THE PURPOSE
To track the progress of every problem and sub-problem in a machine-readable format.
The `monitor_project.py` script reads this to tell the AI what to do.

---

## 2️⃣ THE OBJECT: `status.md`
- **Location**: Every problem folder (e.g., `problems/P1/status.md`).
- **One per folder**: Essential.

---

## 3️⃣ THE FORMAT (Strict)

```markdown
# Status: [Problem Name]

## PHASES
- [x] Definition
- [x] Questions
- [?] Reasoning   <-- Requesting Verification
- [ ] Execution
- [ ] SYNTHESIS

## CHILDREN
- [ ] P1.1: [Name] - [Description]
- [ ] P1.2: [Name] - [Description]
```

---

## 4️⃣ THE RULES

1.  **Single Active Pointer**: ONLY ONE line can have `[*]` or `[?]` at a time.
2.  **Sequential Flow**: You cannot move to Reasoning until Questions are `[x]`.
3.  **Blocking**: If a child problem exists in "CHILDREN", the "Execution" phase of the parent is usually blocked until children are done.

---

## 5️⃣ SYMBOLS KEY
- `[ ]` **Pending**: Waiting to be done.
- `[*]` **Active**: Currently working on this.
- `[?]` **VERIFY**: Work is drafted. Waiting for Monitor/Human to check quality.
    - *If Monitor passes:* It changes to `[x]` (or you manually change it).
    - *If Monitor fails:* It reverts to `[*]`.
- `[x]` **Done**: Completed and verified.
- `[-]` **Blocked**: Waiting on dependency.
