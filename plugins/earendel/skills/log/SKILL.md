---
name: log
description: Earendel learning log — record a concept, mistake, open question, or review item in the project's learning/ folder.
argument-hint: "[concepts | mistakes | questions | review] [what to record]"
disable-model-invocation: true
---

# Learning Log

Learner's request: $ARGUMENTS

The log lives in a `learning/` folder at the root of the current project, one file per record type. Templates for each file and entry are in [templates.md](templates.md) — read it before writing.

## Rules

- **Ask before writing.** Show the learner the exact entry you plan to add and wait for a yes. Never write silently.
- If `learning/` or the needed file doesn't exist, ask whether to create it, then create it from the template header.
- **Append, never rewrite.** Preserve historical entries; never overwrite or quietly edit past mistakes.
- Keep the learner's **original explanation** distinct from the **corrected understanding**. Use their words for the original.
- Date every entry (`YYYY-MM-DD`).
- Keep entries concise — this is a log, not a textbook.
- Record meaningful patterns, misconceptions, and durable insights only, not every small interaction. If the item isn't worth keeping, say so.
- Never invent history or fill fields the learner hasn't supported; leave them blank or ask.

## Choosing the file

| Record | Use for |
| --- | --- |
| `concepts.md` | Something now understood: their explanation, corrected understanding, example, related concepts |
| `mistakes.md` | A meaningful bug or misconception (often from `/earendel:autopsy`) |
| `questions.md` | An unresolved question to come back to |
| `review.md` | A recall prompt scheduled for `/earendel:retrieve` |

If the learner didn't say which, propose one and confirm.
