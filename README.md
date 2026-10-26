# Earendel

**Learn by predicting, trying, and explaining.**

Named after the furthest photographed star away from humanity, Earendel *(WHL0137-LS)* is my branded adaptation of [Manware’s AI Learning Toolkit](https://github.com/i-am-manware/Manware-s-AI-Learning-Toolkit/tree/copilot). It guides programming practice — and learning to build AI-assisted workflows for everyday tasks — through questions, incremental hints, experiments, and teach-back.

It runs in **Claude, ChatGPT/Codex, and Gemini**, built from one shared source.

## Pick your tool

| Where you're working | Install | Start a session |
| --- | --- | --- |
| **Claude Code** (VS Code extension or terminal) | [Claude Code plugin](#claude-code) | `/earendel:learn` |
| **Claude** app (web, desktop, mobile) | [Upload the skill](#claude-app) | `earendel hint: …` |
| **Codex** (VS Code extension or CLI) and the **ChatGPT desktop app** | [Copy the skill folder](#codex-and-chatgpt-desktop) | `$earendel hint …` |
| **Gemini CLI** and **Gemini Code Assist** in VS Code | [Gemini extension](#gemini-cli-and-gemini-code-assist) | `/earendel:learn` |
| **Gemini** app / Google Workspace | [Make a Gem](#gemini-app-gem) | `hint: …` |
| **ChatGPT** on the web (Custom GPT or Project) | [Paste the instructions](#chatgpt-web-custom-gpt-or-project) | `hint: …` |

Tutoring only starts when you ask for it, so these don't change how the tool behaves for normal work. Say **“ship this”**, **“just build it”**, or **“just give me the code”** to get a direct answer mid-session.

> **Using it at work:** follow your organisation's AI and privacy policy. Admins can block extensions, Gems, or custom skills, and some data (personal info, student or customer records, credentials) may not be allowed in AI tools at all. The `automate` workflow walks through this check before you share any real data.

### Claude Code

In the Claude Code panel in VS Code (or a terminal session):

```text
/plugin marketplace add nxrzd/earendel
/plugin install earendel@nxrzd
/reload-plugins
```

Type `/earendel:` to see the commands. Anything after a command is passed in as your request: `/earendel:debug my loop never ends`.

### Claude app

1. Download [`dist/earendel-skill.zip`](dist/earendel-skill.zip).
2. In Claude, go to **Customize → Skills**, upload the zip, and turn it on.
3. Start a message with `earendel` or a workflow name, e.g. `earendel automate: my weekly status report`.

Claude can't save files in a chat, so `log` gives you an entry to paste into your own notes instead.

### Codex and ChatGPT desktop

Codex loads skills from `~/.agents/skills`. Copy the folder there:

```bash
git clone https://github.com/nxrzd/earendel
mkdir -p ~/.agents/skills && cp -r earendel/skills/earendel ~/.agents/skills/
```

Restart Codex, then type `$earendel` (or `/skills` to pick it). Earendel is set to explicit invocation only, so Codex won't start tutoring on its own. Standalone skills also show up under **Skills** in the ChatGPT desktop app. To use it in a single repo instead, copy it to `.agents/skills/` in that repo.

### Gemini CLI and Gemini Code Assist

```bash
gemini extensions install https://github.com/nxrzd/earendel
```

This adds the `/earendel:<name>` commands and the Earendel skill. Gemini asks your permission before it activates a skill. Run `/skills` to check that it loaded.

Gemini Code Assist's agent mode in VS Code is powered by Gemini CLI. If the `/earendel:` commands don't show up there, ask for a workflow by name (“use earendel hint”) so the skill can load. As a fallback, copy `skills/earendel` to `~/.gemini/skills/` (or `~/.agents/skills/`, which Gemini CLI and Codex share).

The extension deliberately has no `GEMINI.md`, because that would load tutoring rules into every Gemini session.

### Gemini app (Gem)

1. In Gemini, open **Gems → New Gem** and name it Earendel.
2. Paste the contents of [`chat/earendel-instructions.md`](chat/earendel-instructions.md) into **Instructions**.
3. Add [`chat/earendel-workflows.md`](chat/earendel-workflows.md) as a **Knowledge** file.
4. Start a chat with the Gem and lead with a workflow name: `automate: summarising the helpdesk queue for my manager`.

### ChatGPT web (Custom GPT or Project)

On the web, ChatGPT only runs skills bundled in plugins, so use the instructions here instead:

- **Custom GPT:** paste `chat/earendel-instructions.md` into **Instructions** (it fits the 8,000-character limit) and upload `chat/earendel-workflows.md` under **Knowledge**.
- **Project:** paste the instructions into the project's instructions and add the workflows file to its files.

The same two files also work in a **Claude Project**.

## Workflows

| Workflow | Purpose |
| --- | --- |
| `learn` | Identify the learning task and choose a suitable workflow. |
| `hint` | Provide incremental help after an attempt and prediction. |
| `debug` | Diagnose problems through hypotheses and small experiments. |
| `autopsy` | Reflect on meaningful fixed bugs and identify prevention habits. |
| `read` | Reconstruct unfamiliar code’s behavior through concrete questions. |
| `review` | Review your code educationally, starting with your own assessment. |
| `test` | Derive contracts, boundaries, failure cases, and tests before implementation. |
| `explore` | Compare approaches and challenge designs with additional constraints. |
| `arch` | Develop a design through a focused architecture interview. |
| `explain` | Test understanding through your explanation, examples, and counterexamples. |
| `retrieve` | Revisit past material through active recall and application. |
| `api` | Investigate an API’s purpose, assumptions, alternatives, tradeoffs, and failures. |
| `automate` | Learn to automate a recurring task with AI: map it, split it, check data rules, write and test your own prompt, build a verification step. *(Earendel addition)* |
| `log` | Record a concept, mistake, question, review item, or automation retro. *(Earendel addition)* |
| `stoic` | Stoic learning mode for frustration and setbacks. *(Earendel addition)* |

The first twelve are inherited from Manware. `explain` is teach-back; an ordinary “explain X” request is answered normally.

## Workflow coaching (`automate`)

The `automate` workflow teaches you to build AI-assisted workflows for mundane tasks — not by building them for you, but by coaching you through it:

1. **Pick the task** and describe how you do it today.
2. **Split the steps** into rules (formula/script), judgement (AI drafts, you check), and keep-human.
3. **Check the data** against your organisation's policy before anything real goes in.
4. **Write the spec and prompt yourself**, then get questions that expose the gaps.
5. **Test on 3–5 cases**, predicting each output first.
6. **Iterate** one change at a time.
7. **Build the check** — how output is verified before anyone acts on it.
8. **Choose where it lives** — saved prompt, Gem/GPT/skill, Sheets or Apps Script, an editor agent, or a script.
9. **Run it for a week** and do a short retro.

## Core Learning Approach

| Shared concept | Purpose |
| --- | --- |
| Independent capability | Help you solve similar problems yourself. |
| Attempt before assistance | Start with your own effort and current understanding. |
| Prediction before explanation | Commit to an expected result before seeing the answer. |
| Hypothesis-driven reasoning | State what you think is happening and why. |
| One focused question at a time | Keep the interaction manageable and interactive. |
| Smallest useful intervention | Give only enough help to move you forward. |
| Learner-written implementation | Let you write the solution — code, prompts, formulas — during learning sessions. |
| Verification through evidence | Check understanding through tests, experiments, documentation, or source. |
| Teach-back | Have you explain why your solution works. |
| Adaptive difficulty | Increase challenge after success; revisit prerequisites when needed. |
| Learning versus shipping | Switch to direct implementation when explicitly requested. |

**Cycle:** Attempt → Predict → Hint → Implement → Test → Explain → Review → Retrieve.

## Seven-Level Hint Ladder

| Level | Intervention |
| --- | --- |
| 0 | A guiding question |
| 1 | A direction or area to inspect |
| 2 | A conceptual hint |
| 3 | A strategy |
| 4 | Abstract pseudocode |
| 5 | A small partial implementation |
| 6 | A full implementation, only when explicitly requested |

One hint at a time, asking before advancing, never more than one level without permission. An explicit **“no code”** instruction takes precedence.

## Learning Records

`log` uses the four upstream templates — Concepts, Mistakes, Questions, Review — plus an Earendel **Automations** template. In an editor agent (Claude Code, Codex, Gemini CLI) it appends to a `learning/` folder in your project, after asking. In a chat app it gives you the entry to paste into your own notes; paste or attach the log back when you run `retrieve`. Entries keep your original reasoning, are dated, and are never rewritten.

## Editing Earendel

Everything is generated from `src/`. Edit there, then rebuild:

```bash
python3 build.py          # regenerate every package
python3 build.py --check  # fail if generated files are stale
```

| Path | Purpose |
| --- | --- |
| `src/core.md` | Core rules shared by every package |
| `src/workflows/*.md` | One file per workflow; `{{cmd:name}}` becomes the right command syntax for each tool |
| `src/templates/log-templates.md` | Learning-log templates |
| `plugins/earendel/` + `.claude-plugin/marketplace.json` | *Generated* — Claude Code plugin |
| `skills/earendel/` | *Generated* — Agent Skills bundle (Claude app, Codex, ChatGPT desktop, Gemini) |
| `commands/earendel/` + `gemini-extension.json` | *Generated* — Gemini CLI extension |
| `chat/` | *Generated* — Gem / Custom GPT / Project instructions and knowledge file |
| `dist/earendel-skill.zip` | *Generated* — uploadable skill |
| `.github/` | Upstream Copilot version, unchanged |

Validate with `claude plugin validate .` and [`skills-ref validate skills/earendel`](https://github.com/agentskills/agentskills/tree/main/skills-ref).

## Fork Attribution

Earendel is a derivative adaptation of the original toolkit by **i-am-manware**. The original author receives credit for the teaching workflows, hint ladder, reusable learning behaviors, and log templates. This edition adds multi-platform packaging (Claude, ChatGPT/Codex, Gemini), a session router, the workflow-coaching mode, a learning-log command, mode boundaries, a Stoic learning mode, and the Earendel branding.

“Fork” describes the project’s derivation here: a GitHub-hosted fork has not been created. Earendel is independently branded and is not an official upstream release. Previously named `manware-learning-chatgpt` and briefly MoM-z14.

## Stoic Learning — Earendel Extension

This mode teaches one idea or practical situation at a time:

1. Describe what happened and distinguish observations from interpretations.
2. Examine the judgment attached to the event.
3. Identify your available choices and the outcomes you cannot guarantee.
4. Consider wisdom, courage, justice, or moderation.
5. Choose a small practical action.
6. Reflect on the result and revisit the idea through active recall.

It asks one question at a time, treats emotions with care, and supports constructive action, boundaries, and responsibility. Stoicism is not framed as emotional suppression or passive acceptance of mistreatment. Historical quotations require verified sources; paraphrases are identified as such.

## Source and Scope

- **Upstream:** [i-am-manware/Manware-s-AI-Learning-Toolkit](https://github.com/i-am-manware/Manware-s-AI-Learning-Toolkit)
- **Source branch:** `copilot`
- **Source commit:** `3eb77d0ec8b4835b31e5e848559153daf5f4af59`
- **Adaptation and branding:** https://github.com/nxrzd — Earendel
- **Adaptation date:** October 14, 2026 (multi-platform: October 25, 2026)
- **Scope:** Manware and the Earendel adaptation. Cognia is not included.

No license file was present in the inspected source tree. This README does not assert a new license for upstream material.
