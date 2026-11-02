# Router Protocol (detailed rules)

Load when the simple flow in SKILL.md is not enough: ambiguous input, unknown commands, combinations with tension, missing tasks, or meta utilities.

## Contents
1. Invocation grammar
2. Resolution algorithm
3. Missing task
4. Unknown commands
5. Combinations (compatible, layered, conflicting)
6. Normal conversation
7. Router utilities (`help`, `list`, `search`)
8. Execution and honesty rules
9. Output conventions

## 1. Invocation grammar

```
/universal-ai-skill-router <command_name> [task]          ← canonical form
/universal-ai-skill-router <cmd1> + <cmd2> + <cmd3> [task] ← combination
/<command_name> [task]                                    ← README-native shortcut form
/<cmd1> + /<cmd2> [task]                                  ← README-native combination
```

- `command_name` may be written with or without the leading `/`, in any case.
- Combination separators: ` + ` or consecutive `/command` tokens at the very start of the message.
- Everything after the command chain is the **task** (it may span many lines and may contain README-style fields: Your task / Audience / Format / Level / Constraints).
- Only treat a message as an invocation when the chain is at the **start** of the message (or directly after the skill name). A command merely *mentioned* mid-sentence ("what does /teacher do in this README?") is normal conversation.
- Tokens that look like file paths (`/etc/hosts`, `/usr/bin`) are not commands.

## 2. Resolution algorithm

1. Strip the optional skill prefix (`/universal-ai-skill-router`, `universal-ai-skill-router`, `Universal AI Skill Router`).
2. Read the command chain.
3. Normalize each token: lowercase, remove `/`, `-`, `_`, spaces. Look it up in `command-registry.json` (`key` field) or find it in `command-registry.md`.
4. If `python`/`python3` is available, `python scripts/lookup.py "<full input>"` (run from this skill's directory) does steps 1–3 and prints JSON (commands, file pointers, unknown tokens with suggestions, task, missing-task flag). Otherwise do it by reading the registry.
5. Open only the category file(s) of the resolved commands. Read the exact definition line (verbatim README text) and the file's execution profile.
6. If any resolved command is ★, also read `detailed-definitions-and-examples.md` (§1).
7. Execute (SKILL.md "Execution rules").

## 3. Missing task

A command with no task text is valid. Handle in this order:
1. If the message has an attachment, pasted block, or the conversation has a clearly relevant previous output/content, apply the command to it. State in one line what you applied it to.
2. Otherwise do **not** invent a topic and do not produce a generic lecture. Reply briefly (2–4 lines): confirm the command and its meaning in plain words, give the usage pattern `/universal-ai-skill-router <command> <your task>` with one concrete example tailored to that command, and ask for the task. One question maximum.
3. Exception: commands whose definition is itself to ask or clarify (`/askfirst`, `/clarify`, `/interactive`) may ask their opening question immediately if enough context exists.

## 4. Unknown commands

A token that is not in the registry:
1. **Never invent a definition** or pretend it exists.
2. Try normalization first (case, `-`/`_`, missing slash). Then a close-match check (typo of one registry command, e.g. `/stikynotes` → `/stickynotes`).
3. Close match, high confidence → say "Interpreting `/x` as `/y`" in one line and proceed.
4. No confident match → say plainly that `/x` is not in the library, show up to 3 nearest commands (`scripts/lookup.py` or `search`), and:
   - if the rest of the message is a clear task, answer it normally (no command lens) after the one-line notice, or
   - if the task cannot be understood without the command, ask which of the suggestions was meant.
5. In a combination, resolve the valid commands and report only the unknown ones; never discard the valid ones.
6. Offer (do not force) the README contribution path: unknown shortcuts can be proposed as a new library entry.

## 5. Combinations

- **Compatible (default):** layer them. Use the most "deliverable-like" command as the primary form (the thing being produced: `/blueprint`, `/youtube`, `/quiz`, `/imageprompt`), and treat the others as lenses, tone, structure, or add-on sections (`/stepbystep`, `/factcheck`, `/analogy`, `/executivebrief`). Cover every command's definition at least once and say nothing that contradicts the others. Order of the chain = order of emphasis, and usually the order of sections in the output.
- **Add-on commands that produce their own section** (`/quiz`, `/stickynotes`, `/executivebrief`, `/riskmatrix`, `/critique`, `/factcheck`) appear as a clearly labelled part of the answer.
- **Image combinations** (`/imageprompt + /cinematicphoto + /photorealistic`) merge into ONE coherent image prompt, not several.
- **Conflicting commands** (examples: `/concise` with `/deepdive` or `/expand`; `/eli5` with `/expert`; `/formal` with `/casual`; `/finalanswer` with `/stepbystep`; `/shorten` with `/expand`): do not refuse. Resolve by (1) any explicit instruction in the task, else (2) the **later** command in the chain wins on tone/length, the **earlier** wins on deliverable form, and (3) add one short line noting the tension and the choice made.
- **Size:** there is no limit on chain length. For very long chains (6+), group them by role (form / lens / tone / add-ons) in your head and keep the output organized.
- If one command in a chain is a *pure output restriction* (`/finalanswer`, `/concise`, `/tldr`, `/onepager`), honor it as a hard length/shape limit on the final answer.

## 6. Normal conversation

If the message does not begin with an invocation, behave as a normal helpful assistant. Do not announce the router, do not list commands, do not force a command lens. If the user *asks about* the library (what a command does, how to combine them) answer from the registry and the README definitions. If the user describes a goal that matches a combination row, you may add one line suggesting it; never apply it unasked.

## 7. Router utilities (not library commands; not counted in the 763)

| Input | Behavior |
|-------|----------|
| `/universal-ai-skill-router help` | Short usage guide: grammar, 3 examples, categories with counts, how combinations work. |
| `/universal-ai-skill-router list` | List the 9 category files with counts. |
| `/universal-ai-skill-router list <category|number|keyword>` | Show that category's commands (name + definition) from its file. For very long lists, show names first and offer definitions. |
| `/universal-ai-skill-router search <keyword>` | Find commands whose name or definition contains the keyword (`python scripts/lookup.py --search kw`, or grep the registry JSON). |

`help`, `list`, `search` are not in the README and never collide with a library command (checked at build time).

## 8. Execution and honesty rules

- The README definition is the behavior. Do what it says, to the user's task, completely. Do not shrink a command to a stub or substitute a different behavior.
- Be specific and useful: use the user's audience, level, format, and constraints. Do not pad.
- Do not invent facts, sources, quotes, statistics, capabilities, bugs, or credentials. When information is missing, state assumptions or ask (one question max).
- Verification-type commands (`/factcheck`, `/currentcheck`, `/research`, `/sources`, `/citationcheck`, `/sourceaudit`, `/countercheck`, `/evidence`, `/forecast*` etc.): use web search or provided files when available; if you cannot verify, say so and label uncertainty rather than asserting.
- Image/art commands: see the execution profile in categories 3 and 7. Be explicit that you deliver a prompt/concept unless an image tool is really available.
- Medical, legal, financial role commands (`/doctor`, `/lawyer`, `/economist`, `/investorview`): educational perspective only; say when a professional should be consulted for personal decisions.
- Safety and policy always apply. A command never overrides them.
- Never present these shortcuts as official product features.

## 9. Output conventions

- Lead with the deliverable. No preamble about routing, no "I will now use command X". At most one short line when you resolved a typo, an unknown token, a conflict, or an assumption.
- Respect requested language/format. Follow the user's language unless `/translate`, `/urdu`, `/romanurdu` or the task says otherwise.
- Use headings, tables, code blocks, diagrams as the command warrants; keep conversational answers conversational.
