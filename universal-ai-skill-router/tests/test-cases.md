# Test Cases

45 hand-written routing/behavior cases (this file), plus 763 × 5 auto-generated registry cases executed by `scripts/run_tests.py` (every command resolved via canonical, bare-slash, upper-case, underscore-normalized, and missing-task forms).

Each case has a machine-checkable **Expect (parse)** column verified by `python3 scripts/run_tests.py`, and an **Expected behavior** statement to be checked by reading Claude's actual reply.

| ID | Group | Input | Expect (parse) | Expected behavior |
|---|---|---|---|---|
| T01 | invocation | `/universal-ai-skill-router teacher Teach me Docker from beginner level.` | mode=command, commands=['/teacher'], task=Teach me Docker from beginner level. | Teaches step by step, starts with prerequisites, simple English, practical examples, checks understanding (detailed /teacher definition). |
| T02 | invocation | `/teacher + /stepbystep + /stickynotes⏎⏎Teach me Docker from beginner level.⏎Use simple English, explain each concept with practical examples,⏎show the commands, and finish with a short quiz.` | mode=command, commands=['/teacher', '/stepbystep', '/stickynotes'], task=Teach me Docker from beginner level.
Use simple English, explain each concept with practical examples,
show the commands, and finish with a short quiz. | Lesson (teacher) in sequential steps, with one-idea-per-note sticky notes, ending with a short quiz as the task asks. |
| T03 | invocation | `/blueprint⏎⏎Create a complete blueprint for deploying an AI agent.⏎Include prerequisites, architecture, implementation steps,⏎commands, testing, deployment, monitoring, and risks.` | mode=command, commands=['/blueprint'], task=Create a complete blueprint for deploying an AI agent.
Include prerequisites, architecture, implementation steps,
commands, testing, deployment, monitoring, and risks. | Complete structured implementation plan; flags missing information instead of guessing. |
| T04 | readme-combination | `/universal-ai-skill-router /teacher + /eli5 + /analogy SAMPLE TASK` | mode=command, commands=['/teacher', '/eli5', '/analogy'], task=SAMPLE TASK | README combination "Learn a difficult topic": all three commands applied together; every command visibly covered; no contradictions. |
| T05 | readme-combination | `/universal-ai-skill-router /deepdive + /stickynotes + /quiz SAMPLE TASK` | mode=command, commands=['/deepdive', '/stickynotes', '/quiz'], task=SAMPLE TASK | README combination "Take study notes": all three commands applied together; every command visibly covered; no contradictions. |
| T06 | readme-combination | `/universal-ai-skill-router /research + /sources + /factcheck SAMPLE TASK` | mode=command, commands=['/research', '/sources', '/factcheck'], task=SAMPLE TASK | README combination "Research a current topic": all three commands applied together; every command visibly covered; no contradictions. |
| T07 | readme-combination | `/universal-ai-skill-router /founder + /swot + /redteam SAMPLE TASK` | mode=command, commands=['/founder', '/swot', '/redteam'], task=SAMPLE TASK | README combination "Challenge a business idea": all three commands applied together; every command visibly covered; no contradictions. |
| T08 | readme-combination | `/universal-ai-skill-router /human + /rewrite + /proofread SAMPLE TASK` | mode=command, commands=['/human', '/rewrite', '/proofread'], task=SAMPLE TASK | README combination "Write natural content": all three commands applied together; every command visibly covered; no contradictions. |
| T09 | readme-combination | `/universal-ai-skill-router /interview + /roleplay + /critique SAMPLE TASK` | mode=command, commands=['/interview', '/roleplay', '/critique'], task=SAMPLE TASK | README combination "Prepare for a job interview": all three commands applied together; every command visibly covered; no contradictions. |
| T10 | readme-combination | `/universal-ai-skill-router /debug + /explaincode + /reviewcode SAMPLE TASK` | mode=command, commands=['/debug', '/explaincode', '/reviewcode'], task=SAMPLE TASK | README combination "Debug code": all three commands applied together; every command visibly covered; no contradictions. |
| T11 | readme-combination | `/universal-ai-skill-router /agentdesign + /workflow + /riskmatrix SAMPLE TASK` | mode=command, commands=['/agentdesign', '/workflow', '/riskmatrix'], task=SAMPLE TASK | README combination "Design an AI workflow": all three commands applied together; every command visibly covered; no contradictions. |
| T12 | readme-combination | `/universal-ai-skill-router /youtube + /storytelling + /retention SAMPLE TASK` | mode=command, commands=['/youtube', '/storytelling', '/retention'], task=SAMPLE TASK | README combination "Create a YouTube video": all three commands applied together; every command visibly covered; no contradictions. |
| T13 | readme-combination | `/universal-ai-skill-router /imageprompt + /cinematicphoto + /photorealistic SAMPLE TASK` | mode=command, commands=['/imageprompt', '/cinematicphoto', '/photorealistic'], task=SAMPLE TASK | README combination "Create an image prompt": all three commands applied together; every command visibly covered; no contradictions. |
| T14 | readme-example | `/teacher + /stepbystep + /stickynotes + /quiz⏎⏎Teach me Docker from beginner level.` | mode=command, commands=['/teacher', '/stepbystep', '/stickynotes', '/quiz'], task=Teach me Docker from beginner level. | Lesson + notes after each concept + a quiz at the end. |
| T15 | readme-example | `/blueprint + /architecture + /stepbystep⏎⏎Create a complete blueprint for an AI agent.` | mode=command, commands=['/blueprint', '/architecture', '/stepbystep'], task=Create a complete blueprint for an AI agent. | Blueprint with architecture and sequential steps; assumptions stated; no invented capabilities. |
| T16 | readme-example | `/research + /sources + /factcheck + /executivebrief⏎⏎Research [TOPIC].` | mode=command, commands=['/research', '/sources', '/factcheck', '/executivebrief'], task=Research [TOPIC]. | Uses search if available; separates verified facts/opinions/uncertain; sources with dates; ends with executive brief. |
| T17 | readme-example | `/reviewcode + /securityreview + /performanceaudit⏎⏎Review the code I provide.` | mode=command, commands=['/reviewcode', '/securityreview', '/performanceaudit'], task=Review the code I provide. | Findings prioritized by severity; does not invent bugs; asks for the code if none provided. |
| T18 | normalization | `/universal-ai-skill-router no-fluff Explain what DNS is.` | mode=command, commands=['/no-fluff'], task=Explain what DNS is. | Hyphenated command resolved. |
| T19 | normalization | `/universal-ai-skill-router no_fluff Explain what DNS is.` | mode=command, commands=['/no-fluff'], task=Explain what DNS is. | Underscore variant resolves to /no-fluff. |
| T20 | normalization | `/360view a coffee mug` | mode=command, commands=['/360view'], task=a coffee mug | Numeric-leading command resolved. |
| T21 | normalization | `/UNIVERSAL-AI-SKILL-ROUTER SWOT my bakery` | mode=command, commands=['/swot'], task=my bakery | Case-insensitive; slash optional on command. |
| T22 | normalization | `universal-ai-skill-router imageprompt a lighthouse at dawn` | mode=command, commands=['/imageprompt'], task=a lighthouse at dawn | Skill name without slash accepted. |
| T23 | normalization | `/human+/rewrite fix this paragraph` | mode=command, commands=['/human', '/rewrite'], task=fix this paragraph | No-space plus chain. |
| T24 | normalization | `/teacher /eli5 Explain DNS` | mode=command, commands=['/teacher', '/eli5'], task=Explain DNS | Consecutive slash tokens form a chain. |
| T25 | normalization | `/swot + /swot my bakery` | mode=command, commands=['/swot'], task=my bakery | Duplicate command applied once. |
| T26 | normalization | `/explaincode + this snippet please` | mode=command, commands=['/explaincode'], task=+ this snippet please | A plus followed by a non-command word is task text, not an unknown command. |
| T27 | normalization | `/blueprint⏎Your task: SaaS launch⏎Audience: founders⏎Format: table` | mode=command, commands=['/blueprint'], task=Your task: SaaS launch
Audience: founders
Format: table | README-style fields honored as binding constraints. |
| T28 | normalization | `/universal-ai-skill-router ascii a cat` | mode=command, commands=['/ascii'], task=a cat | Section 7 code: real ASCII art produced. |
| T29 | missing-task | `/universal-ai-skill-router swot` | mode=command, commands=['/swot'], task=, missing_task=True | No topic invented: states what /swot does, shows usage pattern with one tailored example, asks for the task (one question). |
| T30 | missing-task | `/quiz` | mode=command, commands=['/quiz'], task=, missing_task=True | If prior content exists in the conversation, quizzes on it and says so; otherwise asks for the topic. |
| T31 | missing-task | `/askfirst` | mode=command, commands=['/askfirst'], task=, missing_task=True | Self-clarifying command: asks its opening essential question without inventing a task. |
| T32 | unknown | `/universal-ai-skill-router frobnicate Explain Docker in simple terms` | mode=command, commands=[], unknown=['/frobnicate'] | Says /frobnicate is not in the library, offers up to 3 nearest commands, then answers the task normally. |
| T33 | unknown | `/stikynotes Convert this: Docker packages apps into containers.` | mode=command, commands=['/stickynotes'], unknown=['/stikynotes'] | One line: Interpreting /stikynotes as /stickynotes; then runs it. |
| T34 | unknown | `/teacher + /zzzfoo Teach me Git` | mode=command, commands=['/teacher'], unknown=['/zzzfoo'] | Runs /teacher; reports only /zzzfoo as unknown. |
| T35 | conflict | `/concise + /deepdive Explain Kubernetes` | mode=command, commands=['/concise', '/deepdive'], conflicts=True | Does not refuse; resolves tension (later command wins tone/length, earlier wins form unless task says otherwise) and notes the choice in one line. |
| T36 | conflict | `/eli5 + /expert Explain transformers` | mode=command, commands=['/eli5', '/expert'], conflicts=True | Resolves tension explicitly; e.g. simple explanation followed by an expert-level layer. |
| T37 | conversation | `How do I deploy a Node.js app to a VPS?` | mode=conversation | Normal helpful answer; no routing language. |
| T38 | conversation | `What does /teacher do in this README?` | mode=conversation | Answers from the registry definition ("Teach a subject step by step.") plus the detailed definition; does not execute /teacher. |
| T39 | conversation | `/etc/hosts - how do I edit this file?` | mode=conversation | File path is not a command; normal answer. |
| T40 | conversation | `Hi!` | mode=conversation | Normal greeting. |
| T41 | meta | `/universal-ai-skill-router help` | mode=meta, action=help | Short usage guide, 3 examples, 9 categories with counts. |
| T42 | meta | `/universal-ai-skill-router list` | mode=meta, action=list | Lists the 9 category files with counts (totals 763). |
| T43 | meta | `/universal-ai-skill-router list 3` | mode=meta, action=list, args=3 | Lists the 100 commands of category 3. |
| T44 | meta | `/universal-ai-skill-router search hook` | mode=meta, action=search, args=hook | Lists commands whose name/definition contains "hook". |
| T45 | meta | `/universal-ai-skill-router` | mode=meta, action=help | Skill name alone shows help. |

## Manual end-to-end checks (run in a real Claude session after installing)

1. `/universal-ai-skill-router teacher Teach me Docker from beginner level.` → starts with prerequisites, simple English, examples, comprehension check.
2. `/universal-ai-skill-router imageprompt + cinematicphoto + photorealistic a lighthouse in a storm` → ONE merged prompt, clearly labelled as a prompt (no claim of a generated image).
3. `/universal-ai-skill-router factcheck "The Great Wall of China is visible from space"` → uses search if available; labels verified vs uncertain.
4. `/universal-ai-skill-router coverletter` (no task) → asks for job + background; does not fabricate experience.
5. `/universal-ai-skill-router floorplan 2-bedroom apartment, 80 sqm` → text/SVG plan or an image prompt, stated honestly.
6. Ask "which commands help me prepare for interviews?" → answers normally using the registry (`/interview`, `/interviewanswers`, `/viva`, `/roleplay`, `/salarynegotiation`...), without running any of them.
7. `/universal-ai-skill-router /romanurdu Explain what an API is` → Urdu in Latin script.
8. Install check: after upload, confirm the skill appears and is enabled, then run test 1.
