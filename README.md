# Earendel

**Learn by predicting, trying, and explaining.**

Named after the furthest photographed star away from humanity, Earendel *(WHL0137-LS)* is my branded adaptation of [Manware’s AI Learning Toolkit](https://github.com/i-am-manware/Manware-s-AI-Learning-Toolkit/tree/copilot), packaged as a **Claude Code plugin**. It guides programming practice through questions, incremental hints, experiments, and teach-back.

## Install

Earendel works anywhere Claude Code runs, including the VS Code extension.

1. Add this repo as a plugin marketplace and install the plugin. Run these inside a Claude Code session (VS Code chat panel or terminal):

   ```text
   /plugin marketplace add nxrzd/earendel
   /plugin install earendel@nxrzd
   ```

   Or from a shell: `claude plugin marketplace add nxrzd/earendel` then `claude plugin install earendel@nxrzd`.

2. Run `/reload-plugins` (or start a new session), then type `/earendel:` to see the commands.

To try local edits without installing, start Claude Code with `claude --plugin-dir ./plugins/earendel`. Check changes with `claude plugin validate .`.

## Fork Attribution

Earendel is a derivative adaptation of the original toolkit by **i-am-manware**. The original author receives credit for the teaching workflows, hint ladder, reusable learning behaviors, and log templates. This edition adds Claude Code plugin packaging, a session router, a learning-log command, mode boundaries, a Stoic learning mode, and the Earendel branding.

“Fork” describes the project’s derivation here: a GitHub-hosted fork has not been created. Earendel is independently branded and is not an official upstream release. Previously named `manware-learning-chatgpt` and briefly MoM-z14, then a ChatGPT skill, it now ships as the `earendel` Claude Code plugin.

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

## Commands

Plugin skills are namespaced, so they never collide with Claude Code's built-in commands (e.g. the built-in `/review`). Anything after the command is passed in as your request: `/earendel:debug my loop never ends`.

| Command | Purpose |
| --- | --- |
| `/earendel:learn` | Identify the learning task and choose a suitable workflow. |
| `/earendel:hint` | Provide incremental help after an attempt and prediction. |
| `/earendel:debug` | Diagnose problems through hypotheses and small experiments. |
| `/earendel:autopsy` | Reflect on meaningful fixed bugs and identify prevention habits. |
| `/earendel:read` | Reconstruct unfamiliar code’s behavior through concrete questions. |
| `/earendel:review` | Review your code educationally, starting with your own assessment. |
| `/earendel:test` | Derive contracts, boundaries, failure cases, and tests before implementation. |
| `/earendel:explore` | Compare approaches and challenge designs with additional constraints. |
| `/earendel:arch` | Develop a design through a focused architecture interview. |
| `/earendel:explain` | Test understanding through your explanation, examples, and counterexamples. |
| `/earendel:retrieve` | Revisit past material through active recall and application. |
| `/earendel:api` | Investigate an API’s purpose, assumptions, alternatives, tradeoffs, and failures. |
| `/earendel:log` | Record a concept, mistake, question, or review item in `learning/`. *(Earendel addition)* |
| `/earendel:stoic` | Stoic learning mode. *(Earendel addition)* |

The first twelve are inherited from Manware. Claude can also pick up the tutoring workflows from natural language, such as “teach me this, don’t give me the code” or “give me a hint”. Their descriptions are scoped to learning requests, so tutoring is not imposed on unrelated work. `/earendel:log` and `/earendel:stoic` only run when you type them. `/earendel:explain` is teach-back; an ordinary “explain X” request is answered normally.

To switch from learning to direct implementation, explicitly say **“ship this”**, **“implement it”**, or **“just give me the code.”** Resume tutoring when you want to continue learning.

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

| Behavior | Shared principles | Folded into |
| --- | --- | --- |
| Debugging | Separate expected results, actual results, hypotheses, and evidence; choose the smallest useful experiment. | `debug` |
| Examination | Test prediction, explanation, application, and transfer; correct the smallest misconception first. | `explain` |
| Code review | Prioritize correctness and security; distinguish defects from preferences; verify findings. | `review` |
| Retrieval | Mix recent and older material; favor reasoning over definitions; adapt to demonstrated understanding. | `retrieve` |

## Learning Records

The original [learning directory](https://github.com/i-am-manware/Manware-s-AI-Learning-Toolkit/tree/copilot/learning) contains four templates. Earendel keeps them in `plugins/earendel/skills/log/templates.md`. `/earendel:log` writes them to a `learning/` folder in whichever project you are working in, and `/earendel:retrieve` reads from there.

| Record | Shared information |
| --- | --- |
| Concepts | Your explanation, corrected understanding, an example, and related concepts. |
| Mistakes | The problem, mistake, original model, corrected model, category, prevention, and follow-up exercise. |
| Questions | An unresolved question, context, current hypothesis, evidence to check, and status. |
| Review | A recall prompt, last review date, confidence, and next review or exercise. |

Both preserve original reasoning, use dates, and record meaningful insights or recurring patterns rather than every interaction. Neither should invent previous learning history.

Claude asks before writing any entry and only appends. Installing the plugin does not create automatic reminders.

## File Mapping

| Original toolkit | Earendel |
| --- | --- |
| `.github/copilot-instructions.md` | Core teaching rules and mode boundaries in `skills/learn/SKILL.md`, plus a short ground-rules block in every workflow |
| `.github/prompts/*.prompt.md` | One skill per workflow under `plugins/earendel/skills/` |
| `.github/skills/*/SKILL.md` | Merged into the matching workflow skills (see table above) |
| `.github/instructions/learning-files.instructions.md` | Rules in `skills/log/SKILL.md` |
| `learning/*.md` | Templates in `skills/log/templates.md` |

```text
.claude-plugin/marketplace.json      # makes this repo a plugin marketplace
plugins/earendel/
├── .claude-plugin/plugin.json
└── skills/
    ├── learn/ hint/ debug/ autopsy/ read/ review/ test/
    ├── explore/ arch/ explain/ retrieve/ api/
    ├── log/ (SKILL.md, templates.md)
    └── stoic/
.github/                             # upstream Copilot version, kept for VS Code Copilot users
```

## Stoic Learning — Earendel Extension

Run `/earendel:stoic` to enter Stoic learning mode:

> /earendel:stoic help me handle frustration when learning something difficult

Run it with no request to pick a topic.

This mode teaches one idea or practical situation at a time:

1. Describe what happened and distinguish observations from interpretations.
2. Examine the judgment attached to the event.
3. Identify your available choices and the outcomes you cannot guarantee.
4. Consider wisdom, courage, justice, or moderation.
5. Choose a small practical action.
6. Reflect on the result and revisit the idea through active recall.

The companion asks one question at a time. It treats emotions with care and supports constructive action, boundaries, and responsibility. Stoicism is not framed as emotional suppression or passive acceptance of mistreatment. Historical quotations and specific textual claims require verified sources; paraphrases are identified as such.

It is an Earendel addition, separate from the 12 workflows inherited from Manware. Learning logs remain optional and require authorization to save.

## Source and Scope

- **Upstream:** [i-am-manware/Manware-s-AI-Learning-Toolkit](https://github.com/i-am-manware/Manware-s-AI-Learning-Toolkit)
- **Source branch:** `copilot`
- **Source commit:** `3eb77d0ec8b4835b31e5e848559153daf5f4af59`
- **Adaptation and branding:** https://github.com/nxrzd — Earendel
- **Adaptation date:** October 14, 2026 (Claude Code plugin: October 25, 2026)
- **Scope:** This comparison covers Manware and the Claude Code adaptation. Cognia is not included.

No license file was present in the inspected source tree. This README does not assert a new license for upstream material.
