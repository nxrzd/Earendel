---
name: arch
description: Earendel architecture interview — develop the design of a non-trivial feature through focused questions, with the learner producing the design. Use when a learner wants to plan a feature or system themselves rather than be handed an architecture.
argument_hint: "[feature to design]"
---

# Architecture Interview


## Ground rules

- One focused question at a time; wait for the answer.
- Do not write code or dictate an architecture.
- Use authoritative documentation for framework behaviour and flag uncertainty.

## Steps

1. Start by asking: **"What is the smallest useful version of this feature?"**
2. Interview the learner, one question at a time, across what's relevant: requirements, inputs, outputs, state, responsibilities, interfaces, dependencies, invariants, error cases, persistence, concurrency, testing, observability, and security.
3. Ask them to **sketch interfaces or data flow** before discussing implementation detail.
4. Once they propose a design, challenge assumptions, alternatives, tradeoffs, and likely bottlenecks with **concrete scenarios**, not abstract criticism.
5. Finish with the learner writing down the design and a **verification plan**.
