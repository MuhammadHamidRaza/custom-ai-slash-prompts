# Contributing to Custom ChatGPT Slash Prompts

First of all, thank you for taking the time to contribute. This project is
built and improved by the community, and every contribution matters — a new
shortcut, a clearer definition, a typo fix, a broken link, or a better way to
organize the library.

By participating, you agree to follow our
[Code of Conduct](CODE_OF_CONDUCT.md).

---

## Table of contents

- [Ways to contribute](#ways-to-contribute)
- [Repository layout](#repository-layout)
- [Adding a new shortcut](#adding-a-new-shortcut)
- [Improving an existing shortcut](#improving-an-existing-shortcut)
- [Running the checks](#running-the-checks)
- [Commit messages](#commit-messages)
- [Pull request checklist](#pull-request-checklist)
- [Reporting bugs](#reporting-bugs)
- [Security issues](#security-issues)
- [License of contributions](#license-of-contributions)

---

## Ways to contribute

You do not need to be a maintainer to help.

| I want to… | Do this |
|---|---|
| Suggest a shortcut that is missing | [Open a command request](https://github.com/MuhammadHamidRaza/custom-ai-slash-prompts/issues/new?template=command_request.yml) |
| Report a wrong, duplicate, or unclear definition | [Open a bug report](https://github.com/MuhammadHamidRaza/custom-ai-slash-prompts/issues/new?template=bug_report.yml) |
| Fix something myself | Open a pull request |
| Improve the skill package | Edit the router, registry, or scripts, then run the checks |
| Improve documentation | Fix wording, add examples, or clarify install steps |
| Share the project | Star the repository and tell someone who would find it useful |

> Replace the placeholder repository URL in the links above with the real one
> once the project is published.

If you are unsure whether an idea fits, open an issue first. A short discussion
saves everyone time.

---

## Repository layout

```text
.
├── README.md                          The library (human-facing specification)
├── LICENSE                            MIT
├── CONTRIBUTING.md                    This file
├── CODE_OF_CONDUCT.md                 Community standards
├── SECURITY.md                        How to report vulnerabilities
├── CHANGELOG.md                       Release history
├── universal-ai-skill-router.zip      Ready-to-upload skill package
└── universal-ai-skill-router/         Skill source
    ├── SKILL.md                       Router instructions
    ├── INSTALL.md                     Install guide (Claude, OpenCode, API)
    ├── VERIFICATION-REPORT.md         Generated completeness report
    ├── references/
    │   ├── command-registry.json      Machine-readable index (763 commands)
    │   ├── command-registry.md        Compact index
    │   ├── router-protocol.md         Routing rules
    │   ├── detailed-definitions-and-examples.md
    │   └── commands/                  Category files (verbatim definitions)
    ├── scripts/                       lookup.py · verify.py · run_tests.py
    ├── tests/                         Hand-written + auto-generated tests
    └── source/README.original.md      Frozen copy of the specification
```

`README.md` is the source of truth for the human-facing library.
`universal-ai-skill-router/source/README.original.md` is a frozen copy used by
the verifier. **Keep the two in sync when you change the library.**

---

## Adding a new shortcut

A shortcut is one row in the README plus its definition in the skill package.
Follow these steps in order.

### 1. Check for duplicates

Search the repository for the name before you add it:

```bash
# macOS / Linux
grep -R "/yourcommand" README.md universal-ai-skill-router/references

# Windows PowerShell
Select-String -Path README.md, universal-ai-skill-router\references\* -Pattern "/yourcommand" -Recurse
```

Also search for an existing command that already means the same thing. The
library must not assign two different names the same meaning.

### 2. Add the row to `README.md`

Put it in the most relevant numbered section, in the existing grid-table style.
Use a short, lowercase, hyphen-free name:

```markdown
  `/yourcommand`                      Explain exactly what ChatGPT should do.
```

Keep the description one sentence, specific, and in the same voice as its
neighbors.

### 3. Add the definition to the right category file

Choose the category from
[`references/command-registry.md`](universal-ai-skill-router/references/command-registry.md)
section mapping, then add exactly one line to that file:

```markdown
- `/yourcommand` — Explain exactly what ChatGPT should do.
```

The text after `—` must match the README row **verbatim**. Do not paraphrase.

### 4. Update the registry

Add an entry to
[`references/command-registry.json`](universal-ai-skill-router/references/command-registry.json)
inside the `commands` array. Copy the shape of a neighboring entry:

```json
{
  "id": 764,
  "name": "/yourcommand",
  "key": "yourcommand",
  "description": "Explain exactly what ChatGPT should do.",
  "section_id": "4",
  "section": "Writing, productivity, coding & research",
  "subsection": null,
  "file": "references/commands/04-writing-productivity-coding-research.md",
  "readme_line": 890,
  "detailed_definition": false
}
```

Then add the name once to the matching section of
[`references/command-registry.md`](universal-ai-skill-router/references/command-registry.md)
and bump the section count.

### 5. Sync the frozen spec

Copy the updated `README.md` over
`universal-ai-skill-router/source/README.original.md`:

```bash
# macOS / Linux
cp README.md universal-ai-skill-router/source/README.original.md

# Windows PowerShell
Copy-Item README.md universal-ai-skill-router\source\README.original.md
```

### 6. Run the checks

See [Running the checks](#running-the-checks). A pull request that changes the
registry or definitions must leave both commands green.

### 7. Open the pull request

Describe the shortcut, why it is useful, and give one example. Link the issue it
closes, if there is one.

---

## Improving an existing shortcut

- Fixing a typo in a definition: edit the README row **and** the category file,
  then run `verify.py`.
- Rewording a definition: make the intention clearer, not longer. Keep the
  README and category-file text identical.
- Deprecating a shortcut: do not silently delete it. Open an issue first so the
  change can be discussed; note the removal in `CHANGELOG.md`.

---

## Running the checks

Requirements: **Python 3.8+**. On Windows the executable is usually `python`;
on macOS/Linux it is usually `python3`.

```bash
cd universal-ai-skill-router

# 1. Completeness and consistency (rewrites VERIFICATION-REPORT.md)
python3 scripts/verify.py            # Windows: python scripts\verify.py

# 1b. Same check in CI mode (no files written, non-zero exit on failure)
python3 scripts/verify.py --check

# 2. All routing/parse tests
python3 scripts/run_tests.py         # 3,860 checks, must report ALL PASS

# 3. Resolve a sample input
python3 scripts/lookup.py "/teacher + /eli5 Explain how DNS works"
```

A pull request is ready when:

- `verify.py --check` prints `VERDICT: COMPLETE` and exits `0`
- `run_tests.py` prints `RESULT: ALL PASS`
- no Markdown fences are unbalanced
- no duplicate command names or descriptions were introduced

If you add a command, also add at least one hand-written case to
[`tests/test-cases.json`](universal-ai-skill-router/tests/test-cases.json) when
the routing is non-obvious.

---

## Commit messages

Use short, imperative subjects in the
[Conventional Commits](https://www.conventionalcommits.org/) style:

```text
feat: add /onepager shortcut
fix: correct duplicate definition of /teacher
docs: clarify OpenCode install steps
test: cover underscore normalization
chore: regenerate verification report
```

Keep each commit focused on one change. Rebase on `main` before opening a pull
request if your branch has fallen behind.

---

## Pull request checklist

- [ ] I searched for an existing command with the same name or meaning.
- [ ] The new or changed definition is one clear sentence.
- [ ] `README.md` and the matching category file contain identical text.
- [ ] `command-registry.json` and `command-registry.md` are updated.
- [ ] `source/README.original.md` is in sync with `README.md`.
- [ ] `python3 scripts/verify.py --check` passes.
- [ ] `python3 scripts/run_tests.py` passes.
- [ ] I updated `CHANGELOG.md` for user-visible changes.
- [ ] I did not describe community shortcuts as official product features.

---

## Reporting bugs

Use the issue templates:

- **Bug report** — wrong definition, broken link, duplicate command, routing
  error, or documentation problem.
- **Command request** — a shortcut that should exist but does not.

Please include the command name, what you expected, what happened, and a minimal
example. Screenshots or terminal output help.

---

## Security issues

Do **not** open a public issue for a security problem. Follow
[SECURITY.md](SECURITY.md).

---

## License of contributions

By submitting a contribution you agree that it is licensed under the
[MIT License](LICENSE), the same license as the rest of the project.
