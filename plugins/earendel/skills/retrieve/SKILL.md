---
name: retrieve
description: "Earendel retrieval practice — a short, varied active-recall session drawn from the learner's learning log. Use when a learner wants to review or practise what they learned before."
argument-hint: "[optional topic to focus on]"
---

# Retrieval Review

Learner's request: $ARGUMENTS

## Ground rules

- One question at a time; withhold the answer until the learner commits.
- **Never invent history.** Only use material from the learning log or what the learner tells you now.

## Source material

If you can read files, read the learning log in the current project's `learning/` folder if it exists (`concepts.md`, `mistakes.md`, `questions.md`, `review.md`, `automations.md`). In a chat app, ask the learner to paste or attach their log. If there's no log, say so and ask which topics they want to review — or offer to start one with `/earendel:log`.

## Steps

1. Pick a small mix of **recent and older** meaningful topics (favour items due in `review.md` and recurring mistakes).
2. Ask in varied forms: predict the output of a snippet, explain why a pattern works or fails, find a bug in a short example, compare two approaches, or apply a concept in a new context. **Avoid definition-only questions.**
3. Keep it short and practical. After repeated success, add novelty or constraints; after repeated struggle, revisit prerequisites.
4. End with one confidence judgement, one weak area, and one suggested practice action. Offer to update `review.md` via `/earendel:log`.
