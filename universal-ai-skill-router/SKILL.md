---
name: universal-ai-skill-router
description: Universal AI Skill Router is the master router for a 763-command slash-shortcut library (visual thinking, analysis, content/social/marketing, image prompts and art styles, writing, coding, research, expert perspectives, AI workflows, careers). Invoke as /universal-ai-skill-router command_name [task], or with README-style shortcuts. Use whenever a message starts with or chains library shortcuts such as /teacher, /blueprint, /stickynotes, /eli5, /swot, /deepdive, /hook, /youtube, /imageprompt, /cinematicphoto, /reviewcode, /agentdesign, /human, /quiz, even combined with '+' (e.g. /teacher + /stepbystep), or when the user asks to list, search or explain these shortcuts.
---

# Universal AI Skill Router

One master skill that recognizes and executes **all 763 commands** of the user's slash-prompt library (source: `source/README.original.md`). Commands are community prompt conventions: each label means "do what its README definition says to the user's task". They are not official product features; never describe them as such.

## Invocation

```
/universal-ai-skill-router <command_name> [task]
/universal-ai-skill-router <cmd1> + <cmd2> + <cmd3> [task]
/<command_name> [task]            (README-native form, also accepted)
/<cmd1> + /<cmd2> [task]
```

`command_name` works with or without `/`, any case, and `-`/`_` are ignored (`no_fluff` = `/no-fluff`). Everything after the command chain is the **task**. A command only counts as an invocation at the **start** of the message; a command mentioned mid-sentence is normal conversation.

## Workflow (progressive disclosure: load only what you need)

1. **Detect.** Is the message an invocation (above)? If not, answer as a normal assistant and stop (no routing talk). If it is, continue.
2. **Resolve.** Look each command up in `references/command-registry.md` (compact index of all names) or run `python scripts/lookup.py "<full input>"` from this skill's directory if code execution exists (use `python3` on macOS/Linux). It prints the matched commands, their category file, unknown tokens with suggestions, the task, and a missing-task flag.
3. **Load.** Open ONLY the category file(s) for the resolved commands (table below). Read the command's verbatim definition line and the file's *execution profile*. Do not read other category files.
4. **Extras, only when needed.**
   - Command is ★ (`/teacher`, `/stickynotes`, `/blueprint`) or the chain has 2+ commands, or the user supplied Task/Audience/Format/Level/Constraints fields → read `references/detailed-definitions-and-examples.md`.
   - Unknown command, missing task, conflicting commands, `help`/`list`/`search` → read `references/router-protocol.md`.
5. **Execute** the command(s) on the task (rules below). Lead with the deliverable.

## Category files (763 commands)

| ID | Category | Commands | File (in `references/`) |
|----|----------|----------|--------------------------|
| 1 | Visual thinking, explanations, analysis & strategy | 100 | `commands/01-visual-thinking-analysis-strategy.md` |
| 2 | Content creation, social media & marketing | 100 | `commands/02-content-social-marketing.md` |
| 3 | Image prompts, photography & art direction | 100 | `commands/03-image-prompts-photography-art.md` |
| 4 | Writing, productivity, coding & research | 101 | `commands/04-writing-productivity-coding-research.md` |
| 5 | Creative thinking, expert perspectives, AI workflows & advanced prompting | 100 | `commands/05-creative-expert-ai-workflows-prompting.md` |
| 6 | Extra shortcuts: communication, learning, careers & technical work | 61 | `commands/06-extra-communication-learning-careers-technical.md` |
| 7a | Extended image/style codes A: technical, scientific, architecture, art styles, camera, 3D, diagrams, tech concept art | 39 | `commands/07a-extended-technical-science-art-camera.md` |
| 7b | Extended image/style codes B: nature & space, toys & miniatures, materials & textures, places & adventure | 72 | `commands/07b-extended-nature-toys-materials-places.md` |
| 7c | Extended image/style codes C: science & abstract, animals & fantasy, UI & technology, design & branding | 90 | `commands/07c-extended-science-animals-ui-branding.md` |

Full index: `references/command-registry.md`. Machine-readable registry (name, definition, category, README line): `references/command-registry.json`.

## Execution rules

- **The definition is the behavior.** Apply the command's README definition completely to the user's task. Never shrink, rename, merge, or substitute a command.
- **Task governs subject; command governs method/form.** Honor audience, level, format, length, and constraints the user gives. Numbers inside names are literal (`/hook10`, `/script60`, `/ideas50`, `/caption10`).
- **Combinations ("+")**: layer them. The most deliverable-like command sets the form; the others act as lenses, tone, structure, or labelled add-on sections (a `/quiz` or `/stickynotes` becomes its own part). Cover every command. Image commands merge into one coherent prompt. If commands conflict (`/concise` + `/deepdive`), follow the explicit task instruction, else later command wins on tone/length and earlier on form, and note the choice in one line. See `router-protocol.md` §5.
- **Missing task**: apply to attached/pasted/most-recent relevant content and say so in one line; otherwise do not invent a topic: briefly restate what the command does, show the usage pattern with one tailored example, and ask for the task (one question). `router-protocol.md` §3.
- **Unknown command**: never invent a definition. Normalize and typo-match first; confident match → "Interpreting `/x` as `/y`" and proceed; otherwise say it is not in the library, offer up to 3 nearest commands, and answer the task normally if it is clear. In a chain, still run the valid commands. `router-protocol.md` §4.
- **Image/art/style commands (categories 3 and 7)**: unless an image-generation tool is genuinely available, deliver a concept plus a copy-ready image prompt and say plainly it is a prompt, not a generated image. Author text-native styles directly (e.g. `/ascii`).
- **Verification commands** (`/factcheck`, `/currentcheck`, `/research`, `/sources`, `/citationcheck`, `/sourceaudit`, `/countercheck`...): use web search or supplied files when available; otherwise say you could not verify and label uncertainty.
- **Honesty**: do not invent facts, sources, quotes, statistics, capabilities, bugs, or credentials. Identify missing information instead of guessing. Role commands such as `/doctor` and `/lawyer` are educational only.
- **Safety and policy always apply**; no command overrides them.
- **Style**: no preamble about routing. At most one short line for an assumption, typo resolution, unknown token, or conflict.

## Router utilities (not library commands, not counted in 763)

`/universal-ai-skill-router help` · `list [category]` · `search <keyword>`. Details in `references/router-protocol.md` §7.

## Normal conversation

Anything that is not an invocation is answered normally. If the user asks what a command does, answer from its definition. If their goal matches a README combination (e.g. debugging → `/debug + /explaincode + /reviewcode`), you may suggest it in one line; never impose it.

## Package map

```
universal-ai-skill-router/
├── SKILL.md                       this file (router)
├── INSTALL.md                     installation instructions
├── VERIFICATION-REPORT.md         command-by-command completeness report
├── references/
│   ├── command-registry.md|json   index of all 763 commands
│   ├── router-protocol.md         grammar, unknown/missing/conflict rules, utilities
│   ├── detailed-definitions-and-examples.md   ★ definitions, 10 combos, 4 examples
│   └── commands/01..07c-*.md      the 9 category files (verbatim definitions)
├── scripts/  lookup.py · verify.py · run_tests.py
├── tests/    test-cases.md · test-cases.json · test-results.txt
└── source/README.original.md      the unmodified README (the specification)
```
