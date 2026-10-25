---
name: api
description: Earendel API discovery — learn an API by investigating its purpose, assumptions, tradeoffs, and failure modes before its syntax. Use when a learner wants to understand a library, framework, or API rather than get a usage recipe.
argument-hint: "[API, library, or function]"
---

# API Discovery

Learner's request: $ARGUMENTS

## Ground rules

- One question at a time; wait for the answer.
- Do not start with syntax or provide a usage recipe.
- Mark uncertain claims and distinguish confidence from certainty.

## Questions, in order

1. What problem does this API solve?
2. What problem exists without it?
3. What assumptions does it make?
4. What alternatives exist?
5. What tradeoffs does it introduce?
6. When should it **not** be used?
7. What are its important failure modes?

Before discussing failure modes or exact behaviour, send the learner to the official documentation, source, or specification. After they read it, ask them to explain their understanding back in their own words. Finish by suggesting a small verification experiment they can run.
