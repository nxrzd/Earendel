#!/usr/bin/env python3
"""Generate every Earendel package from the shared source in src/.

Edit files in src/, then run:  python3 build.py
Check generated files are current (e.g. in CI):  python3 build.py --check

Targets
  plugins/earendel/             Claude Code plugin (one skill per workflow)
  skills/earendel/              Agent Skills bundle: claude.ai upload, Codex, ChatGPT
                                desktop, Gemini CLI (also loaded by the Gemini extension)
  commands/earendel/*.toml      Gemini CLI extension commands (/earendel:<name>)
  gemini-extension.json         Gemini CLI extension manifest
  chat/                         Gemini Gem / Custom GPT / ChatGPT or Claude Project
  dist/earendel-skill.zip       Zipped skills/earendel for uploading
"""
from __future__ import annotations

import json
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
VERSION = "1.1.0"
DESCRIPTION = (
    "Learn to code and to build AI-assisted workflows by predicting, trying, and "
    "explaining: hint ladder, debugging tutor, teach-back, code review, workflow "
    "coaching, retrieval practice, and a Stoic learning mode."
)
# Order shown in menus and the knowledge file.
ORDER = ["learn", "hint", "debug", "autopsy", "read", "review", "test", "explore",
         "arch", "explain", "retrieve", "api", "automate", "log", "stoic"]
CUSTOM_GPT_LIMIT = 8000  # characters allowed in a Custom GPT's instructions field

GENERATED = ["plugins/earendel/skills", "skills", "commands", "chat", "dist",
             "gemini-extension.json", "plugins/earendel/.claude-plugin/plugin.json",
             ".claude-plugin/marketplace.json"]


# --------------------------------------------------------------------------- source

def parse(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        sys.exit(f"{path}: missing frontmatter")
    meta = {}
    for line in m.group(1).splitlines():
        key, _, value = line.partition(":")
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        meta[key.strip()] = value
    meta["user_only"] = meta.get("user_only", "false") == "true"
    body = m.group(2).strip("\n")
    title = re.match(r"# (.+)", body)
    if not title:
        sys.exit(f"{path}: body must start with a '# Title' line")
    meta["title"] = title.group(1)
    meta["rest"] = body[title.end():].strip("\n")
    if meta.get("name") != path.stem:
        sys.exit(f"{path}: name must match file name")
    return meta


def load() -> tuple[str, dict, str]:
    core = (SRC / "core.md").read_text(encoding="utf-8").strip()
    flows = {p.stem: parse(p) for p in (SRC / "workflows").glob("*.md")}
    missing = set(ORDER) ^ set(flows)
    if missing:
        sys.exit(f"ORDER and src/workflows disagree on: {sorted(missing)}")
    templates = (SRC / "templates" / "log-templates.md").read_text(encoding="utf-8").strip()
    return core, flows, templates


def render(text: str, *, cmd, ref: str, core: str) -> str:
    text = text.replace("{{core}}", core)
    text = text.replace("{{ref:log-templates}}", ref)
    text = re.sub(r"`?\{\{cmd:([a-z]+)\}\}`?", lambda m: cmd(m.group(1)), text)
    leftover = re.findall(r"\{\{[^}]*\}\}", text)
    if leftover:
        sys.exit(f"unrendered placeholders: {leftover}")
    return text


def summary(description: str) -> str:
    """First sentence after the 'Earendel <thing> — ' prefix."""
    return description.split(" — ", 1)[-1].split(". ", 1)[0].rstrip(".")


def demote(markdown: str) -> str:
    """Push headings down one level, leaving fenced code blocks untouched."""
    out, fenced = [], False
    for line in markdown.splitlines():
        if line.startswith("```"):
            fenced = not fenced
        elif not fenced and line.startswith("#"):
            line = "#" + line
        out.append(line)
    return "\n".join(out)


def yaml_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)  # JSON strings are valid YAML


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip("\n") + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- targets

def claude_code(out: Path, core, flows, templates):
    """Claude Code plugin + marketplace. Commands: /earendel:<name>."""
    write(out / ".claude-plugin/marketplace.json", json.dumps({
        "name": "nxrzd",
        "description": "Noah Richardson's Claude Code plugins",
        "owner": {"name": "Noah Richardson", "url": "https://github.com/nxrzd"},
        "plugins": [{"name": "earendel", "source": "./plugins/earendel",
                     "description": DESCRIPTION}],
    }, indent=2))
    write(out / "plugins/earendel/.claude-plugin/plugin.json", json.dumps({
        "name": "earendel", "version": VERSION, "description": DESCRIPTION,
        "author": {"name": "Noah Richardson", "url": "https://github.com/nxrzd"},
        "homepage": "https://github.com/nxrzd/earendel",
        "repository": "https://github.com/nxrzd/earendel",
        "keywords": ["learning", "tutor", "education", "socratic", "hints", "automation"],
    }, indent=2))
    for name in ORDER:
        f = flows[name]
        fm = [f"name: {name}", f"description: {yaml_str(f['description'])}",
              f"argument-hint: {yaml_str(f['argument_hint'])}"]
        if f["user_only"]:
            fm.append("disable-model-invocation: true")
        body = render(f["rest"], cmd=lambda n: f"`/earendel:{n}`",
                      ref="[templates.md](templates.md)", core=core)
        write(out / f"plugins/earendel/skills/{name}/SKILL.md",
              "---\n" + "\n".join(fm) + "\n---\n\n"
              f"# {f['title']}\n\nLearner's request: $ARGUMENTS\n\n{body}")
        if name == "log":
            write(out / "plugins/earendel/skills/log/templates.md", templates)


BUNDLE_INTRO = """\
## How Earendel is started

Run Earendel only when the user asks for it: by name (`earendel`, `$earendel`, `@earendel`, `/earendel`), by naming one of the workflows below as the first word of a message (for example `hint: my loop never ends` or `earendel debug …`), or by explicitly asking to be tutored rather than given the answer. Without a named workflow, start with the `learn` routing below.

When a workflow is chosen, **read its file in `references/` and follow it**. The core rules above apply to every workflow.
"""


def bundle(out: Path, core, flows, templates):
    """One Agent Skills folder with every workflow under references/."""
    base = out / "skills/earendel"
    cmd = lambda n: f"`{n}` (references/{n}.md)"
    learn = flows["learn"]
    routing = learn["rest"].split("## Route the session", 1)[1]
    routing = render("## Route the session" + routing, cmd=cmd,
                     ref="references/log-templates.md", core=core)
    rows = "\n".join(f"| `{n}` | [references/{n}.md](references/{n}.md) | "
                     f"{summary(flows[n]['description'])} |"
                     for n in ORDER if n != "learn")
    description = (
        "Earendel learning tutor: teaches programming and AI-assisted workflow automation "
        "through questions, predictions, and incremental hints instead of handing over answers. "
        "Workflows: hint, debug, autopsy, read, review, test, explore, arch, explain, retrieve, "
        "api, automate, log, stoic. Use when the user invokes Earendel or one of these workflows "
        "by name, or explicitly asks to be tutored, quizzed, or given hints rather than answers. "
        "Do not use for ordinary requests to write code or do a task."
    )
    assert len(description) <= 1024, len(description)
    skill = (
        f"---\nname: earendel\ndescription: {yaml_str(description)}\n---\n\n"
        f"# Earendel\n\n{core}\n\n{BUNDLE_INTRO}\n{routing}\n\n"
        f"## Workflow files\n\n| Workflow | File | What it does |\n| --- | --- | --- |\n{rows}\n"
    )
    write(base / "SKILL.md", skill)
    for name in ORDER:
        if name == "learn":
            continue
        f = flows[name]
        body = render(f["rest"], cmd=lambda n: f"`{n}`",
                      ref="[log-templates.md](log-templates.md)", core=core)
        write(base / f"references/{name}.md", f"# {f['title']}\n\n{body}")
    write(base / "references/log-templates.md", templates)
    write(base / "agents/openai.yaml",
          "interface:\n"
          "  display_name: \"Earendel\"\n"
          "  short_description: \"Learn to code and automate by predicting, trying, and explaining\"\n"
          "  default_prompt: \"$earendel teach me something I'm working on, one question at a time\"\n"
          "policy:\n"
          "  allow_implicit_invocation: false\n")
    # Zip with the skill folder as the archive's top level (claude.ai requirement).
    zpath = out / "dist/earendel-skill.zip"
    zpath.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(base.rglob("*")):
            if p.is_file():
                info = zipfile.ZipInfo(str(p.relative_to(out / "skills")), (2026, 1, 1, 0, 0, 0))
                info.external_attr = 0o644 << 16
                z.writestr(info, p.read_bytes(), zipfile.ZIP_DEFLATED)


def toml_basic(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)  # JSON escapes are valid TOML basic strings


def gemini(out: Path, core, flows, templates):
    """Gemini CLI extension at the repo root. Commands: /earendel:<name>.

    No GEMINI.md on purpose: a context file would load tutoring rules into every
    Gemini session, including normal work. The skill in skills/earendel is also
    picked up by the extension.
    """
    write(out / "gemini-extension.json", json.dumps({
        "name": "earendel", "version": VERSION, "description": DESCRIPTION,
    }, indent=2))
    for name in ORDER:
        f = flows[name]
        body = render(f["rest"], cmd=lambda n: f"`/earendel:{n}`",
                      ref="the templates at the end of this prompt", core=core)
        prompt = f"# {f['title']}\n\nLearner's request: {{{{args}}}}\n\n{body}"
        if name != "learn":
            prompt = f"# Earendel\n\n{core}\n\n---\n\n{prompt}"
        if name == "log":
            prompt += f"\n\n---\n\n{templates}"
        if "'''" in prompt:
            sys.exit(f"{name}: prompt contains ''' and can't be a TOML literal string")
        write(out / f"commands/earendel/{name}.toml",
              f"description = {toml_basic(f['description'])}\n"
              f"prompt = '''\n{prompt}\n'''")


CHAT_INVOKE = """\
## How to start a workflow

The learner starts a workflow by making its name the first word of a message, such as `hint: my loop never ends`, `debug: …`, or `automate: weekly report`. A plain request to be taught or tutored starts with `learn`. Otherwise, behave like a normal assistant.

The full steps for every workflow are in the attached knowledge file **earendel-workflows.md**. Before running a workflow, read its section there and follow it. Its log templates are at the end of that file.
"""


def chat(out: Path, core, flows, templates):
    """Pasteable instructions + one knowledge file, for apps without skills."""
    cmd = lambda n: f"`{n}`"
    routing = flows["learn"]["rest"].split("## Route the session", 1)[1]
    routing = render("## Route the session" + routing, cmd=cmd, ref="", core=core)
    instructions = f"# Earendel\n\n{core}\n\n{CHAT_INVOKE}\n{routing}\n"
    if len(instructions) > CUSTOM_GPT_LIMIT:
        sys.exit(f"chat instructions are {len(instructions)} chars; "
                 f"Custom GPTs allow {CUSTOM_GPT_LIMIT}")
    write(out / "chat/earendel-instructions.md", instructions)
    parts = ["# Earendel workflows\n\nOne section per workflow. Follow the section the "
             "learner names; the core rules in your instructions apply to all of them."]
    for name in ORDER:
        if name == "learn":
            continue
        f = flows[name]
        body = render(f["rest"], cmd=cmd, ref="the Log templates section at the end",
                      core=core)
        body = demote(body)
        parts.append(f"## `{name}` — {f['title']}\n\n{body}")
    tmpl = demote(templates.split("\n", 1)[1].strip())
    parts.append(f"## Log templates\n\n{tmpl}")
    write(out / "chat/earendel-workflows.md", "\n\n---\n\n".join(parts))


# --------------------------------------------------------------------------- main

def build(out: Path) -> None:
    core, flows, templates = load()
    for rel in ["plugins/earendel/skills", "skills", "commands", "chat", "dist"]:
        shutil.rmtree(out / rel, ignore_errors=True)
    claude_code(out, core, flows, templates)
    bundle(out, core, flows, templates)
    gemini(out, core, flows, templates)
    chat(out, core, flows, templates)


def snapshot(base: Path) -> dict[str, bytes]:
    files = {}
    for rel in GENERATED:
        p = base / rel
        for f in ([p] if p.is_file() else sorted(p.rglob("*")) if p.exists() else []):
            if f.is_file():
                files[str(f.relative_to(base))] = f.read_bytes()
    return files


def main() -> None:
    if "--check" in sys.argv:
        with tempfile.TemporaryDirectory() as tmp:
            build(Path(tmp))
            fresh, current = snapshot(Path(tmp)), snapshot(ROOT)
        stale = sorted(k for k in fresh.keys() | current.keys()
                       if fresh.get(k) != current.get(k))
        if stale:
            print("Generated files are out of date. Run: python3 build.py")
            print("\n".join(f"  {s}" for s in stale))
            sys.exit(1)
        print("Generated files are up to date.")
        return
    build(ROOT)
    print("Built: plugins/earendel, skills/earendel, commands/earendel, "
          "gemini-extension.json, chat/, dist/earendel-skill.zip")


if __name__ == "__main__":
    main()
