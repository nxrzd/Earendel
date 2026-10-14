# Earendel

**Learn by predicting, trying, and explaining.**

Earendel is my branded ChatGPT adaptation of [Manware’s AI Learning Toolkit](https://github.com/i-am-manware/Manware-s-AI-Learning-Toolkit/tree/copilot). It guides programming practice through questions, incremental hints, experiments, and teach-back.

## Fork Attribution

Earendel is a derivative adaptation of the original toolkit by **i-am-manware**. The original author receives credit for the teaching workflows, hint ladder, reusable learning behaviors, and log templates. This edition adds ChatGPT skill routing, optional storage guidance, mode boundaries, and the Earendel branding.

“Fork” describes the project’s derivation here: a GitHub-hosted fork has not been created. Earendel is independently branded and is not an official upstream release. Previously named `manware-learning-chatgpt` and briefly MoM-z14, it now uses the skill identifier `earendel`.

The comparison below documents what Earendel retains from its upstream source.

## Core Learning Approach

| Shared concept | Purpose |
| --- | --- |
| Independent capability | Help you solve similar problems yourself. |
| Attempt before assistance | Start with your own effort and current understanding. |
| Prediction before explanation | Commit to an expected result before seeing the answer. |
| Hypothesis-driven reasoning | State what you think is happening and why. |
| One focused question at a time | Keep the interaction manageable and interactive. |
| Smallest useful intervention | Give only enough help to move you forward. |
| Learner-written implementation | Let you write the solution during learning sessions. |
| Verification through evidence | Check understanding through tests, experiments, documentation, or source. |
| Teach-back | Have you explain why your solution works. |
| Adaptive difficulty | Increase challenge after success; revisit prerequisites when needed. |
| Learning versus shipping | Switch to direct implementation when explicitly requested. |

## Learning Cycle

**Attempt → Predict → Hint → Implement → Test → Explain → Review → Retrieve**

Success means being able to explain the reasoning, predict behavior, debug similar problems, and apply the ideas independently.

## All 12 Workflows

| Workflow | Shared purpose |
| --- | --- |
| `/learn` | Identify the learning task and choose a suitable workflow. |
| `/hint` | Provide incremental help after an attempt and prediction. |
| `/debug` | Diagnose problems through hypotheses and small experiments. |
| `/autopsy` | Reflect on meaningful fixed bugs and identify prevention habits. |
| `/read` | Reconstruct unfamiliar code’s behavior through concrete questions. |
| `/code-review` | Review your code educationally, starting with your own assessment. |
| `/test` | Derive contracts, boundaries, failure cases, and tests before implementation. |
| `/explore` | Compare approaches and challenge designs with additional constraints. |
| `/arch` | Develop a design through a focused architecture interview. |
| `/explain` | Test understanding through your explanation, examples, and counterexamples. |
| `/retrieve` | Revisit past material through active recall and application. |
| `/api` | Investigate an API’s purpose, assumptions, alternatives, tradeoffs, and failures. |

In Earendel, these names are conversational aliases, not registered ChatGPT slash commands. Natural-language requests also work. `/explain` specifically refers to teach-back; an ordinary request for an explanation is interpreted in context.

## Seven-Level Hint Ladder

| Level | Shared intervention |
| --- | --- |
| 0 | A guiding question |
| 1 | A direction or area to inspect |
| 2 | A conceptual hint |
| 3 | A strategy |
| 4 | Abstract pseudocode |
| 5 | A small partial implementation |
| 6 | A full implementation, only when explicitly requested |

Both start with minimal help, provide one hint at a time, and ask before advancing. They do not jump more than one level without explicit permission. An explicit **“no code”** instruction takes precedence.

## Four Reusable Behaviors

| Behavior | Shared principles |
| --- | --- |
| Debugging | Separate expected results, actual results, hypotheses, and evidence; choose the smallest useful experiment. |
| Examination | Test prediction, explanation, application, and transfer; correct the smallest misconception first. |
| Code review | Prioritize correctness and security; distinguish defects from preferences; verify findings. |
| Retrieval | Mix recent and older material; favor reasoning over definitions; adapt to demonstrated understanding. |

## Learning Records

The original [learning directory](https://github.com/i-am-manware/Manware-s-AI-Learning-Toolkit/tree/copilot/learning) contains four templates. The adaptation combines these templates in `references/logs.md`.

| Record | Shared information |
| --- | --- |
| Concepts | Your explanation, corrected understanding, an example, and related concepts. |
| Mistakes | The problem, mistake, original model, corrected model, category, prevention, and follow-up exercise. |
| Questions | An unresolved question, context, current hypothesis, evidence to check, and status. |
| Review | A recall prompt, last review date, confidence, and next review or exercise. |

Both preserve original reasoning, use dates, and record meaningful insights or recurring patterns rather than every interaction. Neither should invent previous learning history.

The bundled templates are not populated progress records. In Earendel, saving learning history requires an available storage destination and user authorization. Installing the skill does not create automatic reminders or guarantee cross-chat recall.

## File Mapping

| Original toolkit | Earendel |
| --- | --- |
| `.github/copilot-instructions.md` | Core teaching rules and mode boundaries in `SKILL.md` |
| `.github/prompts/*.prompt.md` | Twelve workflow files under `references/`, routed from `SKILL.md` |
| `.github/skills/*/SKILL.md` | Four reusable behaviors combined in `references/behaviors.md` |
| `.github/instructions/learning-files.instructions.md` | Learning-record guidance in `references/logs.md` |
| `learning/concepts.md` | Concepts template in `references/logs.md` |
| `learning/mistakes.md` | Mistakes template in `references/logs.md` |
| `learning/questions.md` | Questions template in `references/logs.md` |
| `learning/review.md` | Review template in `references/logs.md` |

The adaptation also includes `agents/openai.yaml` for skill metadata and `references/source.md` for provenance.

## Using Earendel

Invoke the installed skill with a request such as:

> Use $earendel to teach me Python. Ask one question at a time and do not give me code.

The skill is available globally as a reusable skill. It does not impose tutoring on every unrelated conversation.

To switch from learning to direct implementation, explicitly say **“ship this”**, **“implement it”**, or **“just give me the code.”** Resume tutoring when you want to continue learning.

## Source and Scope

- **Upstream:** [i-am-manware/Manware-s-AI-Learning-Toolkit](https://github.com/i-am-manware/Manware-s-AI-Learning-Toolkit)
- **Source branch:** `copilot`
- **Source commit:** `3eb77d0ec8b4835b31e5e848559153daf5f4af59`
- **Adaptation and branding:** Noah Richardson — Earendel
- **Adaptation date:** October 14, 2026
- **Scope:** This comparison covers Manware and the ChatGPT adaptation. Cognia is not included in the installed adaptation described here.

No license file was present in the inspected source tree. This README does not assert a new license for upstream material.
