# ❓ THE TWO-SECTION QUESTION ALGORITHM

**Every problem starts with a `questions.md` file containing two sections.**

---

## ⚠️ CRITICAL RULE: DETAILED ANSWERS

**ALL ANSWERS MUST BE WRITTEN IN FULL DETAIL.**
- Never write short, abbreviated answers.
- Include ALL context, examples, and explanations.
- If the user provides information, record EVERYTHING they said.
- Use bullet points, tables, and sub-sections for clarity.
- **WHY:** Detailed answers prevent forgetting and ensure nothing is lost.

---

## 🚫 CRITICAL RULE: NO DELETION

**QUESTIONS ARE NEVER DELETED.**
- Once a question is written, it stays in the file forever.
- Questions are only MARKED (`[x]`), never removed.
- This creates a permanent record of the investigation.

---

## 1️⃣ SECTION 1: THE CORE STACK (Active)
- This list is **STATIC** during the asking phase.
- We finish this list **ONE BY ONE**.
- **RULE**: New ideas are NEVER added here while asking. They go to Section 2.
- **RULE**: Questions are MARKED `[x]` when answered, NEVER deleted.

## 2️⃣ SECTION 2: THE DISCOVERY STACK (Buffer)
- This list is **DYNAMIC**.
- New questions derived *from user answers* go here.
- **RULE**: We **ONLY APPEND** here. We **NEVER** ask from here yet.
- **RULE**: During FLUSH, questions are MOVED to Section 1 (not deleted).

---

## 📝 THE FILE STRUCTURE (`questions.md`)

```markdown
# Questions for [Problem Name]

## SECTION 1: ACTIVE

### Q1: What is the goal?
- [x] ANSWER:
  - **Primary Goal:** Maximize real estate leads
  - **Secondary Goal:** Improve conversion rate
  - **Context:** User works in cold-calling team
  - **Target:** 2 qualified leads per day

### Q2: Who is the target?
- [x] ANSWER:
  - **Primary Target:** Property buyers and investors
  - **Location:** United States
  - **Property Type:** Residential, Lots, Commercial
  - **Qualification:** Must have Valid Reason OR Asking Price

## SECTION 2: BUFFER (Discovered)
- [ ] What CRM does the company use? (Discovered from Q2 - mentioned tools)
```

---

## 📍 WHERE ANSWERS ARE STORED

**UNDER THE QUESTION AS A DETAILED SECTION.**

**Format:**
```markdown
### Q1: Question text?
- [x] ANSWER:
  - **Key Point 1:** Detailed explanation
  - **Key Point 2:** More context
  - **Example:** Specific instance
  - **Notes:** Additional info from user
```

**WHY:**
1. Keeps question and answer together (no hunting).
2. Creates a permanent Q&A record.
3. AI can re-read answers when writing `reasoning.md`.
4. **Nothing is forgotten** - all details preserved.

---

## 🔄 THE CYCLE (Step-by-Step)

### A. The Asking Phase
1.  Read **Section 1**.
2.  Select the **first `[ ]` or `[*]`** question. Mark it `[*]`.
3.  Ask the user **ONE question at a time**.
4.  Get the answer.

### B. The Recording Phase (Immediate)
1.  **RECORD ANSWER IN DETAIL**: Write full answer with all context.
2.  **USE STRUCTURE**: Bullet points, sub-sections, tables.
3.  **MARK DONE**: Change `[*]` to `[x]`.
4.  **CHECK FOR NEW QUESTIONS**: Did the answer reveal a new unknown?
    - **YES**: Append new question to **Section 2**.
    - **NO**: Do nothing.

### C. The Loop Check
1.  Are there pending items (`[ ]`) in **Section 1**?
    - **YES**: Go back to Step A.
    - **NO**: Go to Step D (The Flush).

### D. The Flush (Moving the Buffer)
1.  **MOVE** all questions from **Section 2** → end of **Section 1**.
2.  Section 2 becomes empty (but the header stays).
3.  Are there new items in Section 1 now?
    - **YES**: Go back to Step A.
    - **NO**: **PROCESS COMPLETE**. All questions answered.

---

## ✅ COMPLETION STATE

When done, `questions.md` is a **COMPREHENSIVE KNOWLEDGE BASE**:

```markdown
# Questions for P1: Telemarketing

## SECTION 1: ACTIVE

### Q1: What is the goal?
- [x] ANSWER:
  - **Primary Goal:** Maximize real estate lead generation
  - **Target:** 2 qualified leads per day, 44 per month
  - **Quality Focus:** Follow campaign guidelines exactly
  - **Escalation:** Tricky leads go to leader for approval

### Q2: What tools are used?
- [x] ANSWER:
  - **Dialer:** ReadyMode (cloud-based)
  - **Data Source:** Zillow (provides owner name, phone, MV)
  - **Integrations:** None currently enabled
  - **Dispositions:** Interested, Not Interested, Call Back, Spanish Speaker, Dead Call, Not Available

### Q3: What campaigns exist?
- [x] ANSWER:
  - **Total Campaigns:** 94+ extracted from PDF
  - **Example Codes:** J&J, AX, OD, MCO, DEV, ICB, NIC
  - **Key Campaigns:**
    - ICB: States CT/MA/RI, requires email, roof/AC ages
    - NIC: Zillow leads only, AP can be 10k above MV

## SECTION 2: BUFFER (Discovered)
(empty - all moved to Section 1)
```

**The file is now a FULL, DETAILED RECORD of the investigation.**
