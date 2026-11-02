# Installation — Universal AI Skill Router

This folder is a portable **agent skill**: one `SKILL.md` plus supporting
references and scripts. It works with Claude.ai, Claude Code, OpenCode, and any
agent runtime that supports `SKILL.md` folders.

```
universal-ai-skill-router/
├── SKILL.md                 entry point (frontmatter + router instructions)
├── INSTALL.md               this file
├── VERIFICATION-REPORT.md   generated completeness report
├── references/              registry, protocol, detailed definitions, 9 category files
├── scripts/                 lookup.py · verify.py · run_tests.py
├── tests/                   routing tests and results
└── source/README.original.md  frozen copy of the library specification
```

You only need Python if you want to run the optional resolver and self-checks.
The skill itself is pure Markdown.

---

## Claude.ai (web / desktop)

1. Download `universal-ai-skill-router.zip` from the repository root.
2. Open your account settings and find the **Skills** area (under
   Capabilities / Customize; the exact label changes between versions).
3. Choose **Upload skill** and select `universal-ai-skill-router.zip`.
4. Make sure the skill is **enabled**. File creation / code execution may also
   need to be enabled in the same settings area.
5. Start a new chat and run:

```text
/universal-ai-skill-router teacher Teach me Docker from beginner level.
```

Claude.ai does not provide a slash-command menu for skills. It activates a skill
by matching your message to the skill description, so starting with
`/universal-ai-skill-router ...` or a library shortcut such as `/teacher ...`
is what triggers it reliably.

---

## Claude Code

```bash
# Personal: available in every project
mkdir -p ~/.claude/skills
unzip universal-ai-skill-router.zip -d ~/.claude/skills/

# Project: committed with this repository only
mkdir -p .claude/skills
unzip universal-ai-skill-router.zip -d .claude/skills/
```

Windows PowerShell:

```powershell
# Personal
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Expand-Archive -Path .\universal-ai-skill-router.zip -DestinationPath "$HOME\.claude\skills" -Force

# Project
New-Item -ItemType Directory -Force ".\.claude\skills" | Out-Null
Expand-Archive -Path .\universal-ai-skill-router.zip -DestinationPath ".\.claude\skills" -Force
```

Reload the session. The skill is then available as
`/universal-ai-skill-router`.

---

## OpenCode

OpenCode discovers skills in `SKILL.md` folders under these locations:

| Scope | Location |
|---|---|
| Global | `~/.config/opencode/skills/` |
| Global compatibility | `~/.claude/skills/`, `~/.agents/skills/` |
| Project | `.opencode/skills/` |
| Project compatibility | `.claude/skills/`, `.agents/skills/` |

```bash
# Global
mkdir -p ~/.config/opencode/skills
unzip universal-ai-skill-router.zip -d ~/.config/opencode/skills/

# Or project-local
mkdir -p .opencode/skills
unzip universal-ai-skill-router.zip -d .opencode/skills/
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.config\opencode\skills" | Out-Null
Expand-Archive -Path .\universal-ai-skill-router.zip -DestinationPath "$HOME\.config\opencode\skills" -Force
```

OpenCode derives the skill ID from the folder name, so the folder must remain
`universal-ai-skill-router`. Load it explicitly with `@universal-ai-skill-router`
or let the model discover it from the description, then write the command chain:

```text
@universal-ai-skill-router teacher + eli5 Explain how DNS works
```

> If your terminal intercepts a leading `/`, omit it before the skill name
> (`universal-ai-skill-router teacher ...`) or use the `@` form above.

---

## Claude API / Agent SDK

Upload the folder through the Skills API (or place it in your agent's skills
directory) and enable it for the container. See Anthropic's Skills
documentation for the current request format.

---

## Verify the install (30 seconds)

1. `/universal-ai-skill-router help` → usage guide with 9 categories totalling
   763 commands.
2. `/universal-ai-skill-router swot` → explains `/swot` and asks for a task
   (it must not invent one).
3. `/universal-ai-skill-router zzzunknown hello` → says the command is not in
   the library and suggests the nearest ones.
4. `/universal-ai-skill-router teacher + eli5 + analogy Explain how DNS works`
   → combined lesson.
5. `/universal-ai-skill-router imageprompt + cinematicphoto a lighthouse in a
   storm` → one merged prompt, clearly labelled as a prompt.

---

## Optional: run the self-checks locally

Requires **Python 3.8+**. On Windows the executable is normally `python`; on
macOS/Linux it is normally `python3`.

```bash
cd universal-ai-skill-router

# Completeness (rewrites VERIFICATION-REPORT.md)
python3 scripts/verify.py          # Windows: python scripts\verify.py

# Same check, no files written (CI mode)
python3 scripts/verify.py --check

# 3,860 routing/parse tests
python3 scripts/run_tests.py

# Resolve an input
python3 scripts/lookup.py "/teacher + /stepbystep Teach me Git"
```

Expected output:

```text
README commands: 763 | registry.json: 763 | registry.md: 763 | category files: 763
passing all checks: 763 | problems: 0 | extra: 0 0 0 | dups: 0 0
VERDICT: COMPLETE
```

---

## Updating the library

`source/README.original.md` is the specification the verifier reads. To add or
change a command:

1. Edit the matching row in the repository `README.md`.
2. Copy `README.md` over `source/README.original.md`.
3. Add the definition line to the correct file under `references/commands/`.
4. Add the entry to `references/command-registry.json` and the index in
   `references/command-registry.md`.
5. Run `scripts/verify.py` and `scripts/run_tests.py` until both pass.
6. Rebuild the ZIP if you distribute it:

```powershell
Compress-Archive -Path universal-ai-skill-router -DestinationPath universal-ai-skill-router.zip -Force
```

Do not give two commands the same name or the same meaning.

---

## Customizing

- A user-supplied definition in chat overrides a library definition for that
  session only.
- To change a command permanently, edit its line in its category file, its entry
  in `command-registry.json`, and the README row.
- To remove a category, delete its file, its registry entries, and its row from
  the category table in `SKILL.md`; then re-run the verifier.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| The skill never triggers | Confirm the folder contains `SKILL.md` and that its `description` is present. In Claude.ai, enable the skill; in OpenCode, check `@universal-ai-skill-router` and the `skill` permission. |
| `python3: command not found` (Windows) | Use `python` or `py -3`. |
| `python: command not found` (macOS/Linux) | Use `python3`. |
| The ZIP upload is rejected | Make sure the ZIP has one top-level folder named `universal-ai-skill-router` with `SKILL.md` directly inside it. |
| A command is not recognized | It may be misspelled or missing from the registry. Run `scripts/lookup.py "<input>"` to see suggestions, or open a command request. |
| `verify.py` reports a problem | Read the `## 5. Problems` section of the generated report; it names the command and the failed check. |
