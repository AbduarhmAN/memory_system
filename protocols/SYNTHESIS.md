# 🔗 THE SYNTHESIS PROTOCOL

**The "Assembly Line" that combines child solutions into a final deliverable.**

---

## ⚠️ CRITICAL RULE: THOROUGH DOCUMENTATION

**ALL SYNTHESIS MUST BE COMPREHENSIVE.**
- Never summarize briefly.
- Include ALL relevant details from each child.
- Explain HOW parts connect and WHY.
- Create a standalone document that needs no external references.
- **WHY:** Thorough synthesis ensures nothing is lost and the user has complete information.

---

## 1️⃣ THE PURPOSE
- Each child `solution.md` solves ONE piece of the puzzle.
- The parent needs ONE combined output.
- **SYNTHESIS** = Read all children → Merge → Write `FINAL_SOLUTION.md`.

---

## 2️⃣ THE TRIGGER

Synthesis activates when:
1. ALL children in `status.md` are marked `[x]`.
2. The `[*]` marker moves to "SYNTHESIS".

**Example `status.md`:**
```markdown
## CHILDREN
- [x] P1.1: Lead Parser - Extracted 344 leads
- [x] P1.2: Campaign Matcher - Matched to 94 campaigns
- [x] P1.3: Qualification Engine - Classified all leads
- [x] P1.4: Report Generator - Created output files
- [*] SYNTHESIS  <-- TRIGGER
```

---

## 3️⃣ THE ALGORITHM (Step-by-Step)

### STEP 1: GATHER
1. List all child folders.
2. For each child, read:
   - `definition.md` (What was the goal?)
   - `questions.md` (What was learned?)
   - `solution.md` (What was built?)
3. Store ALL content in memory.

### STEP 2: ANALYZE
1. Identify the **Common Goal** (from parent `definition.md`).
2. Map each child's contribution to the goal.
3. Detect overlaps or contradictions.
4. Note any issues or limitations from each child.

### STEP 3: STRUCTURE
Create a detailed outline:
1. **Introduction** - What was the original problem?
2. **Solution Overview** - How was it solved at high level?
3. **Detailed Sections** - One per child with full explanation
4. **Integration** - How do parts work together?
5. **Usage Guide** - How does user apply this?
6. **Limitations** - What doesn't work or needs improvement?
7. **Next Steps** - What to do after this?

### STEP 4: WRITE
1. Write `FINAL_SOLUTION.md` in the PARENT folder.
2. Format: Complete, standalone document.
3. The user should NOT need to read child files.
4. Include ALL relevant details, examples, and instructions.

### STEP 5: VERIFY
1. Read `FINAL_SOLUTION.md` completely.
2. Check: Does it answer the original `definition.md`?
3. Check: Is any child's content missing?
4. Check: Could a new reader understand everything?

---

## 4️⃣ THE OUTPUT FILE

**Location:** Parent folder (same level as `sub/`).
**Name:** `FINAL_SOLUTION.md`.

**Structure (DETAILED):**
```markdown
# [Parent Problem Title] - FINAL SOLUTION

## Executive Summary
[2-3 paragraphs summarizing the entire solution]

---

## Original Problem
### Goal
[From parent definition.md]

### Context
[Full context from definition]

### Success Criteria
[How we measure success]

---

## Solution Overview
### Approach Taken
[From reasoning.md - which approach and why]

### Components Built
| Component | Purpose | Output |
|-----------|---------|--------|
| P1.1 | [Purpose] | [What it produces] |
| P1.2 | [Purpose] | [What it produces] |

---

## Part 1: [Child 1 Name]

### What It Does
[Detailed explanation]

### How It Works
[Technical details with examples]

### Key Learnings
[From questions.md - what was discovered]

### Output Files
[List of files created]

---

## Part 2: [Child 2 Name]
[Same structure as Part 1]

---

## How Components Connect

### Data Flow
```
P1.1 (Parse) 
    → leads.csv 
        → P1.2 (Match) 
            → matched_leads.csv 
                → P1.3 (Qualify)
                    → qualified_leads.csv
                        → P1.4 (Report)
                            → final_report.csv
```

### Dependencies
[Explain what needs what]

---

## User Guide

### How to Use This Solution

#### Step 1: [First action]
[Detailed instructions]

#### Step 2: [Second action]
[Detailed instructions]

### Files Reference
| File | Location | Purpose |
|------|----------|---------|
| leads.csv | problems/P1/output/ | Parsed leads |
| ... | ... | ... |

---

## Limitations & Known Issues
1. [Issue 1]: [Description and workaround]
2. [Issue 2]: [Description and workaround]

---

## Next Steps
1. [Recommended next action]
2. [Future improvement]
```

---

## 5️⃣ THE COMPLETION

After writing `FINAL_SOLUTION.md`:
1. Mark `SYNTHESIS` as `[x]` in `status.md`.
2. The parent problem is now **COMPLETE**.
3. Execute **POP** (Focus Protocol) to return to grandparent.

---

## 6️⃣ EDGE CASES

### NO CHILDREN (Atomic Problem)
- Skip Synthesis.
- `solution.md` IS the final answer.

### NESTED CHILDREN (P1.1 has P1.1.1, P1.1.2)
- P1.1 must Synthesize FIRST into `P1.1/FINAL_SOLUTION.md`.
- Then P1 reads `P1.1/FINAL_SOLUTION.md` (not the grandchildren).
- **Recursive Synthesis** from bottom-up.
