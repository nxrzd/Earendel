# Learning Log Templates

Each file starts with its header, then entries are appended below it, newest last.

---

## `learning/concepts.md`

```markdown
# Concepts

Concepts I can now explain. My original explanation is kept separate from the corrected one.
```

Entry:

```markdown
## <Concept> — YYYY-MM-DD

**My explanation:** <in the learner's own words, as first given>
**Corrected understanding:** <what was repaired, if anything>
**Example:** <a concrete example>
**Boundary / counterexample:** <where it stops applying>
**Related:** <related concepts>
```

---

## `learning/mistakes.md`

```markdown
# Mistakes

Meaningful bugs and misconceptions. Entries are never rewritten.
```

Entry:

```markdown
## <Short name> — YYYY-MM-DD

**Problem:** <what happened>
**Mistake:** <what I did>
**Original model:** <what I believed>
**Corrected model:** <what is actually true>
**Category:** <syntax | API knowledge | incorrect mental model | control flow | state | assumptions | environment/configuration | problem decomposition | debugging process | careless error>
**Pattern:** <isolated | repeated pattern | conceptual weakness | missing domain knowledge | weak debugging process>
**Prevention:** <habit, test, or tool>
**Follow-up exercise:** <optional>
```

---

## `learning/questions.md`

```markdown
# Open Questions

Things I don't understand yet.
```

Entry:

```markdown
## <Question> — YYYY-MM-DD

**Context:** <where it came up>
**Current hypothesis:** <best guess right now>
**Evidence to check:** <docs, source, or an experiment>
**Status:** open | answered YYYY-MM-DD — <one-line answer>
```

---

## `learning/review.md`

```markdown
# Review Queue

Recall prompts for /earendel:retrieve.
```

Entry:

```markdown
## <Topic>

**Recall prompt:** <a prediction, why, bug-finding, comparison, or transfer question — not a definition>
**Last reviewed:** YYYY-MM-DD
**Confidence:** low | medium | high
**Next:** <next review date or exercise>
```

---

## `learning/automations.md`

```markdown
# Automations

AI-assisted workflows I've built: what they do, how I check them, and how they went.
```

Entry:

```markdown
## <Task name> — YYYY-MM-DD

**Task:** <what it does, how often, how long it took by hand>
**Tool:** <where it runs: chat + saved prompt, Gem / GPT / skill, Sheets / Apps Script, script, other>
**AI does:** <the steps the AI handles>
**I do:** <the steps kept manual, including the final check>
**Data rules:** <what data it may touch and what must never go in>
**Checks:** <how output is verified, e.g. checklist, spot-check rate>
**Prompt / spec:** <link or location of the learner-written prompt>
**Results:** <time saved, error rate, failures seen>
**Next change:** <one improvement to try>
```
