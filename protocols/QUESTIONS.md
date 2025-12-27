# ❓ THE QUESTIONS PROTOCOL (Anti-Laziness Edition)

**The mechanism for extracting Truth from the User.**

---

## ⚠️ CRITICAL RULE: FIGHT LAZINESS

**The AI is prone to "False Confidence" (thinking it understands when it doesn't).**
- **FORBIDDEN:** Accepting vague nouns ("I want a website", "Use a database").
- **MANDATORY:** Unpacking constraints ("What *kind* of website? Static/Dynamic? React/Vue?").
- **MANDATORY:** Calculating Uncertainty before moving on.

---

## 1️⃣ THE BATCHING RULE (Efficiency)
- Do **NOT** ask 1 question at a time (Too slow).
- Do **NOT** ask 20 questions at a time (Overwhelming).
- **GOLDEN MEAN:** Ask **3-5 high-impact questions** in a batch.

---

## 2️⃣ THE DEPTH-FIRST PROBE (ClariQ Method)
If the user gives a high-level answer, you must **DRILL DOWN**.
*   *User:* "I want to scrape data."
*   *Lazy AI:* "Okay."
*   *System 2 AI:* "What source? Is it dynamic (JS)? Rate limits? Auth required?"

---

## 3️⃣ THE UNCERTAINTY THRESHOLD (Stopping Criterion)
**Before moving to the Reasoning Phase, you must score your understanding (0-100%).**

**The "Completeness Score":**
1.  **Goal Clarity:** Do I know *exactly* what "Done" looks like?
2.  **Constraint Clarity:** Do I know what is *forbidden*?
3.  **Edge Case Awareness:** Do I know how to handle failure?

**Rule:**
- If Score < **90%**: You **MUST** ask another batch of probing questions.
- If Score > **90%**: You **MUST** summarize your understanding and ask for confirmation.

---

## 4️⃣ THE REFLECTIVE CONFIRMATION (The Mirror)
**Never just "move on". You must Mirror the user's intent.**

*Format:*
> "Based on your answers, I understand that:
> 1. You want [X].
> 2. You are constrained by [Y].
> 3. Success means [Z].
>
> **Is this 100% correct? Or did I miss something?**"

---

## 5️⃣ THE EXECUTION CYCLE

### Step A: The Initial Probe
1.  Read `definition.md`.
2.  Generate **3-5 Core Questions** targeting the biggest "Unknowns".
3.  Wait for answers.

### Step B: The Scrutiny (Anti-Laziness Loop)
1.  Read the User's Answers.
2.  **Critique:** "Did they actually answer? Or were they vague?"
3.  **Action:**
    - If Vague: Ask **Clarification Questions** (Drill Down).
    - If Clear: Check **Uncertainty Threshold**.

### Step C: The Confirmation
1.  Score > 90%.
2.  Write the **Reflective Confirmation** message.
3.  If User says "Yes" → Update `status.md` to `[*] Reasoning`.
