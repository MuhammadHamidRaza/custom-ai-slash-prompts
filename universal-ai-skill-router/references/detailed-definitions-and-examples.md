# Detailed Definitions, Combinations & Examples (from the README)

Load this file when: (a) the command chain contains `/teacher`, `/stickynotes` or `/blueprint`; (b) two or more commands are combined with `+`; (c) the user asks for the "reusable prompt pattern" or an example; (d) the user supplies structured fields such as Task / Audience / Format / Level / Constraints.

## 1. Explicit behavior definitions (README "Make these shortcuts reusable")

These three commands have longer README definitions. They are **authoritative** and override the one-line category definition wherever they are more specific.

**When the user invokes `/teacher`:**
- Teach the topic step by step.
- Start with prerequisites.
- Use simple English.
- Include practical examples.
- Check my understanding.

**When the user invokes `/stickynotes`:**
- Convert the material into short, clear notes.
- Keep one idea per note.
- Highlight important terms.
- Avoid unnecessary paragraphs.

**When the user invokes `/blueprint`:**
- Create a complete, structured implementation plan.
- Include prerequisites, architecture, steps, examples, testing, deployment, monitoring, and risks.
- Identify missing information instead of guessing.

README rule: "Keep the definitions clear and avoid assigning conflicting meanings to the same shortcut." The user may add their own definitions in the same format at any time; a user-supplied definition for a command in this session overrides the library definition for that session.

## 2. Reusable prompt pattern (README "Quick start")

```text
/SHORTCUT

Your task: [describe what you need]
Audience: [who this is for]
Format: [table, checklist, tutorial, code, etc.]
Level: [beginner, intermediate, advanced]
Constraints: [what to include or avoid]
```

If the user supplies any of these fields, treat each as a binding constraint on the output. If a field is absent, do not interrogate the user: choose a sensible default and state it in one short line (unless the missing field blocks the task).

README tip: "The shortcut is a label; the instruction after it tells [the assistant] what you actually want." The task text always governs the subject; the command governs the method, lens, or form.

## 3. Useful shortcut combinations (README table, all 10)

| # | Goal | Suggested combination |
|---|------|-----------------------|
| 1 | Learn a difficult topic | `/teacher + /eli5 + /analogy` |
| 2 | Take study notes | `/deepdive + /stickynotes + /quiz` |
| 3 | Research a current topic | `/research + /sources + /factcheck` |
| 4 | Challenge a business idea | `/founder + /swot + /redteam` |
| 5 | Write natural content | `/human + /rewrite + /proofread` |
| 6 | Prepare for a job interview | `/interview + /roleplay + /critique` |
| 7 | Debug code | `/debug + /explaincode + /reviewcode` |
| 8 | Design an AI workflow | `/agentdesign + /workflow + /riskmatrix` |
| 9 | Create a YouTube video | `/youtube + /storytelling + /retention` |
| 10 | Create an image prompt | `/imageprompt + /cinematicphoto + /photorealistic` |

Any command may be combined with any other. When the user names a goal that matches one of these rows without giving commands (for example "help me debug this"), the row may be offered as a suggestion, but never imposed.

## 4. Ready-to-copy examples (README, all 4)

**Learn Docker**
```text
/teacher + /stepbystep + /stickynotes + /quiz

Teach me Docker from beginner level.
Explain every important concept in easy English.
Give practical commands and examples.
After each major concept, give me short notes.
At the end, test me with 10 multiple-choice questions.
Do not skip prerequisites.
```

**Create an AI-agent blueprint**
```text
/blueprint + /architecture + /stepbystep

Create a complete blueprint for an AI agent.
Include:
1. Problem and requirements
2. Architecture and components
3. Technology choices and alternatives
4. Implementation phases
5. Example code and commands
6. Testing and evaluation
7. Deployment and monitoring
8. Security, costs, and risks

Explain assumptions and do not invent capabilities.
```

**Research a topic**
```text
/research + /sources + /factcheck + /executivebrief

Research [TOPIC].
Prioritize reliable and recent sources.
Separate verified facts, opinions, and uncertain claims.
Include source links and dates.
Finish with a concise executive summary.
```

**Review code**
```text
/reviewcode + /securityreview + /performanceaudit

Review the code I provide.
Check correctness, security, performance, readability,
maintainability, and edge cases.
Prioritize findings by severity.
Explain each issue and suggest a fix.
Do not invent bugs that are not supported by the code.
```

Also from the README introduction: `/teacher + /stepbystep + /stickynotes` with "Teach me Docker from beginner level. Use simple English, explain each concept with practical examples, show the commands, and finish with a short quiz." and the standalone `/blueprint` example ("Create a complete blueprint for deploying an AI agent. Include prerequisites, architecture, implementation steps, commands, testing, deployment, monitoring, and risks.").

## 5. Important README caveat (honesty rule)

These shortcuts are **community-created prompt conventions, not official built-in product commands**. Never describe them as native features of Claude, ChatGPT, or any product. The router simply interprets each label as the instruction its definition states.
