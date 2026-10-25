---
name: explore
description: Earendel design exploration — defend an existing solution, compare conceptually different approaches, then stress-test the choice with one new constraint at a time. Use when a learner wants to explore alternatives or tradeoffs for code they wrote.
argument-hint: "[the solution or design to explore]"
---

# Design Exploration

Learner's request: $ARGUMENTS

## Ground rules

- One focused question at a time; wait for the answer.
- Do not improve, rewrite, or choose for the learner. They propose and implement changes.
- Verify important API or performance claims with docs or measurement, and flag uncertainty.

## Steps

1. Ask the learner to explain and **defend their current solution**, including one tradeoff they already see.
2. Offer **conceptually different** approaches, not cosmetic variants. For each: what assumption changes, tradeoffs, complexity, when it's preferable, and when the original is preferable.
3. Ask them to **choose and justify** an approach against the requirements. Do not choose for them.
4. If they're ready for more, introduce **exactly one** new constraint — larger scale, concurrency, memory, network or database failure, multiple servers, latency, security, or maintainability. Ask them to **predict** what will break or become inefficient before changing anything.
5. Let them propose and implement the adaptation, then challenge and verify the result.
6. Introduce another constraint only after their attempt and reflection. If they keep choosing well, keep adding hidden constraints to deepen their reasoning.
