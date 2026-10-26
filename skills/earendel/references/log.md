# Learning Log

The log is one file per record type. Use the templates in [log-templates.md](log-templates.md) for each file's header and each entry.

**Where it lives depends on what you can do:**

- **You can write files** (a coding agent in an editor or terminal): keep it in a `learning/` folder at the root of the current project.
- **You can't write files** (a chat app): write the finished entry in a single block the learner can paste into their own notes doc, and tell them which file it belongs in. When they want to review later, ask them to paste or attach their log.

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
| `mistakes.md` | A meaningful bug or misconception (often from `autopsy`) |
| `questions.md` | An unresolved question to come back to |
| `review.md` | A recall prompt scheduled for `retrieve` |
| `automations.md` | An AI-assisted workflow from `automate`: what it does, its checks, and how it went |

If the learner didn't say which, propose one and confirm.
