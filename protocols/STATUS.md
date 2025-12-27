# 🚦 THE LOCAL STATUS PROTOCOL

**The Manual Safety Net that resides in EVERY problem folder.**

## 1️⃣ THE SYMBOLS
- `[x]` : **DONE** (Completed & Verified)
- `[*]` : **CURRENT** (The precise active step)
- `[ ]` : **PENDING** (Waiting)

**CRITICAL RULE**: There can be only **ONE** `[*]` in the entire file.

---

## 2️⃣ THE FILE STRUCTURE (`status.md`)

Every `status.md` must have these exact two sections.

### SECTION A: THE PROCESS (The "Prep" Phase)
Tracks the mandatory steps before sub-problems.

1. `[ ] Definition` (Creating definition.md)
2. `[ ] Questions` (The Two-Section Algorithm)
3. `[ ] Reasoning` (The 5 Strategies)
4. `[ ] Execution` (The Solve OR The Dive)
5. `[ ] SYNTHESIS` (Combine children into FINAL_SOLUTION.md)

**NOTE**: SYNTHESIS only applies if there are CHILDREN. For atomic problems, skip it.

### SECTION B: THE CHILDREN (The "Sub-Problem" Phase)
Tracks the created sub-folders (if distinct from Atomic Solve).

- `[ ] P1.1`
- `[ ] P1.2`
- ...

---

## 3️⃣ THE LOGIC FLOW

**State 1: Just Entered**
```markdown
## PROCESS
- [*] Definition
- [ ] Questions
- [ ] Reasoning
- [ ] Execution
- [ ] SYNTHESIS
```

**State 2: In Question Cycle**
```markdown
## PROCESS
- [x] Definition
- [*] Questions  <-- AI knows it MUST be working on questions.md
- [ ] Reasoning
- [ ] Execution
- [ ] SYNTHESIS
```

**State 3: Execution (Atomic - No Children)**
```markdown
## PROCESS
- [x] Definition
- [x] Questions
- [x] Reasoning
- [*] Execution (Solving Atomic)
- [ ] SYNTHESIS  <-- Will be SKIPPED (no children)
```

**State 4: Execution (Complex - Has Children)**
```markdown
## PROCESS
- [x] Definition
- [x] Questions
- [x] Reasoning
- [x] Execution
- [ ] SYNTHESIS

## CHILDREN
- [*] P1.1   <-- Focus is here
- [ ] P1.2
```

**State 5: All Children Done, Ready for Synthesis**
```markdown
## PROCESS
- [x] Definition
- [x] Questions
- [x] Reasoning
- [x] Execution
- [*] SYNTHESIS  <-- AI combines all child solutions

## CHILDREN
- [x] P1.1
- [x] P1.2
```

---

## 4️⃣ WHY THIS SAVES TOKENS
If `Current_Focus.txt` is lost, the AI reads **one** `status.md` and sees the `[*]`.
- If `[*]` is on "Questions", it opens `questions.md`.
- If `[*]` is on "P1.1", it opens `P1.1/status.md`.
- If `[*]` is on "SYNTHESIS", it executes Synthesis Protocol.
- It never "guesses".
