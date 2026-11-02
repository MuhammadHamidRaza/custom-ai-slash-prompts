<div align="center">
# ⚡ 763 Custom ChatGPT Slash Prompts

### A community-built prompt shortcut library for learning, creating, researching, coding, and getting work done.

[![Custom
Prompts](https://img.shields.io/badge/Prompts-763-7C3AED?style=for-the-badge)](#-complete-command-library)
[![Platform](https://img.shields.io/badge/Platform-ChatGPT%20%7C%20Claude-10A37F?style=for-the-badge)](https://chatgpt.com/)
[![Skill](https://img.shields.io/badge/Skill-Claude%20%7C%20OpenCode-00A67E?style=for-the-badge)](universal-ai-skill-router/INSTALL.md)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge)](CONTRIBUTING.md)

**One shortcut. One clear instruction. A better starting point for your
next task.**

⭐ If this collection helps you, please **star this repository** and
share it with others!
</div>

------------------------------------------------------------------------

## 👋 Welcome

This repository is a practical collection of **custom slash-style prompt
shortcuts** for ChatGPT. It brings together prompts for:

-   📚 Learning, teaching, explanations, and study notes
-   🔎 Research, fact-checking, critical thinking, and analysis
-   ✍️ Writing, editing, communication, and content creation
-   📣 YouTube, social media, marketing, and storytelling
-   🎨 Visual concepts, image prompts, design, and creative direction
-   💻 Programming, debugging, software architecture, and AI workflows
-   🧠 Productivity, planning, decision-making, and business strategy
-   🗂️ Notes, checklists, blueprints, roadmaps, and documentation

The goal is simple: make useful prompting patterns easier to discover,
reuse, customize, and share.

## 🚀 Use it as an AI skill

This repository also ships a complete **agent skill** —
[`universal-ai-skill-router`](universal-ai-skill-router/) — that teaches
Claude, OpenCode, or any `SKILL.md`-compatible assistant to recognize and
execute all 763 shortcuts, including `+` combinations, missing tasks, and
unknown commands.

| Platform | Install |
|---|---|
| Claude.ai | Upload [`universal-ai-skill-router.zip`](universal-ai-skill-router.zip) in **Settings → Skills** |
| Claude Code | `unzip universal-ai-skill-router.zip -d ~/.claude/skills/` |
| OpenCode | `unzip universal-ai-skill-router.zip -d ~/.config/opencode/skills/` |
| API / Agent SDK | Upload the folder through the Skills API |

```text
/universal-ai-skill-router teacher + eli5 Explain how DNS works
/universal-ai-skill-router help
/universal-ai-skill-router search image
```

See [`INSTALL.md`](universal-ai-skill-router/INSTALL.md) for step-by-step
instructions, Windows commands, and troubleshooting. The skill is optional:
every shortcut still works as a plain prompt label.

## ⚠️ Important: What these shortcuts are (and aren't)

These are **community-created prompt conventions**, not official
built-in ChatGPT slash commands.

For example, typing `/teacher` does not install or activate a special
ChatGPT feature by itself. It is simply a convenient label for an
instruction. ChatGPT may interpret it from context, but for consistent
results, include the description after the shortcut or define your
preferred shortcuts in Custom Instructions or project instructions.

**Example:**

``` text
/teacher + /stepbystep + /stickynotes

Teach me Docker from beginner level.
Use simple English, explain each concept with practical examples,
show the commands, and finish with a short quiz.
```

You can also use a shortcut on its own:

``` text
/blueprint

Create a complete blueprint for deploying an AI agent.
Include prerequisites, architecture, implementation steps,
commands, testing, deployment, monitoring, and risks.
```

> **Tip:** The shortcut is a label; the instruction after it tells
> ChatGPT what you actually want.

## 🚀 Quick start

1.  Browse the command library below.
2.  Copy a shortcut that matches your task.
3.  Add your request after it.
4.  Be specific about audience, format, length, constraints, and desired
    output.
5.  Combine two or three compatible shortcuts when useful.

### A reusable prompt pattern

``` text
/SHORTCUT

Your task: [describe what you need]
Audience: [who this is for]
Format: [table, checklist, tutorial, code, etc.]
Level: [beginner, intermediate, advanced]
Constraints: [what to include or avoid]
```

------------------------------------------------------------------------

# 📚 Complete command library

The shortcuts are grouped by purpose. Definitions explain the behavior
to request from ChatGPT. They are not guaranteed capabilities or
commands built into the product.

## 1. Visual thinking, explanations, analysis & strategy

  -----------------------------------------------------------------------
  Shortcut                            Ask ChatGPT to...
  ----------------------------------- -----------------------------------
  `/handwritten`                      Make notebook-style notes.

  `/visualize`                        Explain an idea visually.

  `/stickynotes`                      Split information into short
                                      sticky-note points.

  `/infographic`                      Organize information as an
                                      infographic.

  `/diagram`                          Create a concept diagram.

  `/flowchart`                        Show a process as a flowchart.

  `/mindmap`                          Build a mind map.

  `/xray`                             Reveal the internal parts of
                                      something.

  `/blueprint`                        Create a detailed blueprint for a
                                      project, system, product, or plan.

  `/explodedview`                     Separate something into its
                                      components.

  `/thenvsnow`                        Compare how something was before
                                      and is now.

  `/timeline`                         Arrange events chronologically.

  `/beforeafter`                      Show a before-and-after comparison.

  `/cutaway`                          Explain using a cutaway view.

  `/anatomy`                          Explain the parts of something.

  `/layers`                           Explain something layer by layer.

  `/ecosystem`                        Show the connected parts of an
                                      ecosystem.

  `/journey`                          Explain an end-to-end journey.

  `/process`                          Explain a complete process.

  `/cycle`                            Show a repeating cycle.

  `/roadmap`                          Create a learning or execution
                                      roadmap.

  `/dashboard`                        Arrange key information as a
                                      dashboard.

  `/comparison`                       Compare options side by side.

  `/versus`                           Compare two things head to head.

  `/scale`                            Compare sizes, levels, or scale.

  `/evolution`                        Explain how something changed over
                                      time.

  `/future`                           Explore possible future scenarios.

  `/inside`                           Explain how something works
                                      internally.

  `/microscopic`                      Examine tiny details.

  `/macroscopic`                      Explain the bigger picture.

  `/crosssection`                     Explain with a cross-sectional
                                      view.

  `/map`                              Create a geographic or concept map.

  `/heatmap`                          Show areas of intensity.

  `/network`                          Map relationships and connections.

  `/architecture`                     Design or explain a system
                                      architecture.

  `/wireframe`                        Plan a website or app layout.

  `/mockup`                           Describe a realistic product
                                      mockup.

  `/prototype`                        Develop an early product concept.

  `/schematic`                        Create a simple technical
                                      schematic.

  `/isometric`                        Present an isometric-style concept.

  `/birdseye`                         Show a top-down overview.

  `/360view`                          Consider a subject from all sides.

  `/storyboard`                       Break a story into visual scenes.

  `/comic`                            Explain through comic-style panels.

  `/poster`                           Organize information as a poster.

  `/cover`                            Create a book or report cover
                                      concept.

  `/adcreative`                       Develop an advertising concept.

  `/thumbnail`                        Develop a video thumbnail concept.

  `/carousel`                         Plan a multi-slide social media
                                      carousel.

  `/socialvisual`                     Plan a social media graphic.

  `/quotevisual`                      Turn a quote into a visual concept.

  `/eli5`                             Explain in very simple language.

  `/expert`                           Explain at an expert level.

  `/firstprinciples`                  Break a topic down to its
                                      fundamentals.

  `/deepdive`                         Give a comprehensive explanation.

  `/simplify`                         Make a difficult topic easier.

  `/analogy`                          Explain through a relatable
                                      comparison.

  `/socratic`                         Teach by asking guiding questions.

  `/teachme`                          Provide a structured lesson.

  `/cheatsheet`                       Create quick-reference notes.

  `/flashcards`                       Make question-and-answer
                                      flashcards.

  `/quiz`                             Test understanding with a quiz.

  `/viva`                             Prepare oral-exam questions.

  `/interview`                        Conduct a mock interview.

  `/devilsadvocate`                   Challenge an idea from the opposite
                                      side.

  `/factcheck`                        Check claims against evidence.

  `/mythvsfact`                       Separate myths from facts.

  `/proscons`                         List advantages and disadvantages.

  `/swot`                             Perform a SWOT analysis.

  `/pestle`                           Analyze political, economic,
                                      social, technological, legal, and
                                      environmental factors.

  `/fiveforces`                       Apply Porter's Five Forces.

  `/rootcause`                        Find the underlying cause of a
                                      problem.

  `/fivewhys`                         Investigate a problem using five
                                      whys.

  `/decisionmatrix`                   Compare choices using weighted
                                      criteria.

  `/scenario`                         Explore possible scenarios.

  `/simulate`                         Run a hypothetical simulation.

  `/roleplay`                         Act out a realistic situation.

  `/consultant`                       Give consultant-style
                                      recommendations.

  `/executivebrief`                   Prepare a short executive brief.

  `/insights`                         Extract useful insights.

  `/recommendations`                  Suggest practical next steps.

  `/prioritize`                       Rank tasks or choices by
                                      importance.

  `/benchmark`                        Compare performance against a
                                      standard.

  `/marketmap`                        Map an industry or market.

  `/strategy`                         Build a strategy.

  `/businessmodel`                    Explain or design a business model.

  `/pitch`                            Prepare a pitch.

  `/investor`                         Evaluate something from an
                                      investor's perspective.

  `/redteam`                          Stress-test a plan for weaknesses.

  `/premortem`                        Imagine failure and identify
                                      possible causes.

  `/reverseengineer`                  Work backwards to understand how
                                      something was built or achieved.

  `/promptengineer`                   Improve a prompt.

  `/research`                         Conduct structured research.

  `/sources`                          Find supporting sources.

  `/summarize`                        Summarize information.

  `/extract`                          Pull out specified information.

  `/table`                            Convert information into a table.

  `/presentation`                     Create a presentation outline.

  `/dashboardanalysis`                Interpret dashboard information.

  `/actionplan`                       Turn a goal into an action plan.
  -----------------------------------------------------------------------

## 2. Content creation, social media & marketing

  -----------------------------------------------------------------------
  Shortcut                            Ask ChatGPT to...
  ----------------------------------- -----------------------------------
  `/viral`                            Make content more engaging and
                                      shareable.

  `/viralreel`                        Plan an engaging Instagram Reel.

  `/viralshorts`                      Optimize a YouTube Short.

  `/viralhook`                        Create a strong opening hook.

  `/hook`                             Write attention-grabbing opening
                                      lines.

  `/hook10`                           Generate 10 hook options.

  `/hook50`                           Generate 50 hook ideas.

  `/retention`                        Improve audience retention.

  `/retentioncurve`                   Plan engagement throughout a video.

  `/patterninterrupt`                 Add moments that regain attention.

  `/openloop`                         Create curiosity that encourages
                                      people to continue.

  `/curiosity`                        Make content more curiosity-driven.

  `/psychology`                       Apply relevant audience psychology.

  `/dopamine`                         Make content more rewarding to
                                      follow.

  `/emotion`                          Strengthen emotional impact.

  `/fear`                             Use fear-based messaging
                                      responsibly.

  `/surprise`                         Add an unexpected element.

  `/shock`                            Create a surprising opening.

  `/storytelling`                     Turn information into a story.

  `/herojourney`                      Use a Hero's Journey structure.

  `/script`                           Write a script.

  `/script30`                         Write a 30-second script.

  `/script60`                         Write a 60-second script.

  `/script90`                         Write a 90-second script.

  `/script180`                        Write a three-minute script.

  `/narration`                        Write a narration.

  `/voiceover`                        Write natural voice-over lines.

  `/monologue`                        Write a single-speaker script.

  `/dialogue`                         Write a conversation between
                                      speakers.

  `/podcast`                          Plan a podcast episode.

  `/youtube`                          Create a long-form YouTube video
                                      plan.

  `/shorts`                           Format content for YouTube Shorts.

  `/reels`                            Format content for Instagram Reels.

  `/tiktok`                           Format content for TikTok.

  `/linkedin`                         Write a LinkedIn post.

  `/twitter`                          Write an X post or thread.

  `/facebook`                         Write a Facebook post.

  `/instagram`                        Write an Instagram caption.

  `/caption`                          Generate captions.

  `/caption10`                        Generate 10 caption options.

  `/hashtags`                         Suggest relevant hashtags.

  `/cta`                              Write a call to action.

  `/engagement`                       Encourage meaningful audience
                                      engagement.

  `/shareworthy`                      Make content more worth sharing.

  `/saveworthy`                       Make content useful enough to save.

  `/commentbait`                      Create a discussion prompt that
                                      encourages comments.

  `/poll`                             Create a poll.

  `/communitypost`                    Write a YouTube Community post.

  `/newsletter`                       Draft a newsletter.

  `/blog`                             Write a blog post.

  `/seo`                              Improve search optimization.

  `/keywords`                         Generate relevant keywords.

  `/headline`                         Write headlines.

  `/titles`                           Generate multiple title ideas.

  `/thumbnailtext`                    Suggest thumbnail wording.

  `/thumbnailaudit`                   Critique a thumbnail concept.

  `/titleaudit`                       Evaluate a title.

  `/contentaudit`                     Review content quality.

  `/copywriter`                       Write persuasive marketing copy.

  `/landingpage`                      Draft landing-page content.

  `/salespage`                        Draft sales-page content.

  `/emailmarketing`                   Write a marketing email.

  `/coldemail`                        Write a cold outreach email.

  `/sales`                            Improve sales messaging.

  `/branding`                         Develop brand positioning.

  `/brandvoice`                       Define or maintain a brand voice.

  `/positioning`                      Clarify market positioning.

  `/offer`                            Create a compelling offer.

  `/usp`                              Define a unique selling
                                      proposition.

  `/valueprop`                        Write a value proposition.

  `/campaign`                         Plan a marketing campaign.

  `/launch`                           Plan a product or service launch.

  `/contentcalendar`                  Build a content calendar.

  `/postingplan`                      Create a posting schedule.

  `/series`                           Generate ideas for a content
                                      series.

  `/challenge`                        Design a challenge campaign.

  `/trend`                            Explore relevant trends.

  `/evergreen`                        Create content that stays useful
                                      over time.

  `/repurpose`                        Convert existing content into other
                                      formats.

  `/broll`                            Suggest B-roll footage.

  `/shotlist`                         Create a list of required video
                                      shots.

  `/cameraangles`                     Suggest camera angles.

  `/cinematic`                        Give content a cinematic treatment.

  `/cinematicsketch`                  Describe a cinematic visual
                                      concept.

  `/storyboardpro`                    Create a detailed storyboard.

  `/sceneplan`                        Plan a video scene by scene.

  `/transitions`                      Suggest scene transitions.

  `/motiongraphics`                   Suggest motion-graphics ideas.

  `/vox`                              Use an explanatory documentary
                                      approach.

  `/johnnyharris`                     Use map-led, investigative
                                      documentary techniques.

  `/magnatesmedia`                    Use a business-documentary
                                      structure.

  `/kurzgesagt`                       Use a colorful, simplified
                                      science-explainer approach.

  `/netflix`                          Plan a streaming-documentary-style
                                      presentation.

  `/bbc`                              Use a factual documentary
                                      presentation.

  `/natgeo`                           Use a nature and exploration
                                      documentary approach.

  `/applekeynote`                     Structure a polished product
                                      presentation.

  `/minimal`                          Use a minimal visual approach.

  `/modern`                           Use a modern, clean presentation.

  `/premium`                          Give content a premium editorial
                                      feel.

  `/aesthetic`                        Develop a consistent visual
                                      aesthetic.
  -----------------------------------------------------------------------

## 3. Image prompts, photography & art direction

  -----------------------------------------------------------------------
  Shortcut                            Ask ChatGPT to...
  ----------------------------------- -----------------------------------
  `/photorealistic`                   Describe a photorealistic image.

  `/hyperrealistic`                   Aim for highly realistic visual
                                      details.

  `/cinematicphoto`                   Create a cinematic photography
                                      concept.

  `/portrait`                         Plan a portrait.

  `/headshot`                         Plan a professional headshot.

  `/editorial`                        Create a magazine-editorial
                                      concept.

  `/fashion`                          Develop a fashion photography
                                      concept.

  `/lifestyle`                        Plan a lifestyle photograph.

  `/streetphoto`                      Describe a street photograph.

  `/travelphoto`                      Plan travel photography.

  `/wildlife`                         Plan wildlife photography.

  `/macrophoto`                       Describe extreme close-up
                                      photography.

  `/droneview`                        Plan an aerial drone view.

  `/360drone`                         Plan a 360-degree aerial view.

  `/topdown`                          Use a directly overhead camera
                                      angle.

  `/lowangle`                         Use a low camera angle.

  `/highangle`                        Use a high camera angle.

  `/wideangle`                        Use a wide-angle composition.

  `/telephoto`                        Describe a telephoto-lens look.

  `/fisheye`                          Use a fisheye perspective.

  `/depthoffield`                     Control foreground and background
                                      focus.

  `/bokeh`                            Add soft background blur.

  `/goldenhour`                       Use warm golden-hour lighting.

  `/bluehour`                         Use blue-hour lighting.

  `/sunset`                           Create a sunset atmosphere.

  `/sunrise`                          Create a sunrise atmosphere.

  `/nightmode`                        Plan a night photograph.

  `/neon`                             Use neon lighting.

  `/moody`                            Create a moody atmosphere.

  `/dramaticlighting`                 Use dramatic light and shadow.

  `/volumetriclight`                  Add visible beams of light.

  `/rimlight`                         Light the edges of the subject.

  `/silhouette`                       Create a silhouette composition.

  `/backlit`                          Light the subject from behind.

  `/blackandwhite`                    Use monochrome photography.

  `/filmgrain`                        Add a film-grain effect.

  `/kodak`                            Use a classic film-photography
                                      feel.

  `/fujifilm`                         Use a film-inspired color palette.

  `/polaroid`                         Create an instant-photo look.

  `/vintage`                          Use an old-fashioned visual
                                      aesthetic.

  `/retro`                            Use a retro design direction.

  `/80s`                              Use an 1980s-inspired look.

  `/90s`                              Use a 1990s-inspired look.

  `/cyberpunk`                        Create a cyberpunk setting.

  `/steampunk`                        Create a steampunk setting.

  `/dieselpunk`                       Create a dieselpunk setting.

  `/solarpunk`                        Create an optimistic green-future
                                      setting.

  `/postapocalyptic`                  Create a post-apocalyptic scene.

  `/fantasy`                          Create fantasy artwork.

  `/scifi`                            Create science-fiction artwork.

  `/space`                            Create an outer-space scene.

  `/planet`                           Illustrate a planet.

  `/galaxy`                           Illustrate a galaxy.

  `/nebula`                           Create a nebula scene.

  `/underwater`                       Create an underwater scene.

  `/ocean`                            Create an ocean landscape.

  `/mountains`                        Create a mountain landscape.

  `/forest`                           Create a forest landscape.

  `/desert`                           Create a desert landscape.

  `/cityscape`                        Create an urban skyline.

  `/architecturephoto`                Plan architectural photography.

  `/interior`                         Visualize an interior space.

  `/minimalinterior`                  Create a minimal interior concept.

  `/luxury`                           Use a luxury visual direction.

  `/productphoto`                     Plan professional product
                                      photography.

  `/packaging`                        Design a packaging concept.

  `/advertising`                      Plan an advertising visual.

  `/billboard`                        Create a billboard concept.

  `/posterdesign`                     Plan a poster design.

  `/brandingmockup`                   Present a brand identity mockup.

  `/logo`                             Generate logo concepts.

  `/iconset`                          Design a consistent icon set.

  `/mascot`                           Develop a mascot concept.

  `/characterdesign`                  Design an original character.

  `/conceptart`                       Create concept-art directions.

  `/environmentart`                   Design a fictional environment.

  `/mattepainting`                    Describe a matte-painting scene.

  `/digitalpainting`                  Plan a digital painting.

  `/oilpainting`                      Use an oil-painting technique.

  `/watercolor`                       Use a watercolor illustration
                                      approach.

  `/acrylic`                          Use an acrylic-painting approach.

  `/charcoal`                         Use a charcoal-drawing approach.

  `/pencilsketch`                     Create a pencil-sketch concept.

  `/inkdrawing`                       Create an ink-drawing concept.

  `/crosshatching`                    Use cross-hatching techniques.

  `/comicbook`                        Create comic-book artwork.

  `/manga`                            Create manga-inspired artwork.

  `/anime`                            Create anime-inspired artwork.

  `/ghibli`                           Describe a whimsical, hand-painted
                                      animation feel.

  `/pixar`                            Describe expressive, polished 3D
                                      animation qualities.

  `/lowpoly`                          Create low-poly 3D artwork.

  `/voxel`                            Create voxel-style artwork.

  `/pixelart`                         Create pixel art.

  `/clayrender`                       Create a clay-render concept.

  `/3drender`                         Describe a 3D-rendered scene.

  `/octanerender`                     Describe a polished 3D-render
                                      aesthetic.

  `/unrealengine`                     Plan a real-time-engine visual
                                      concept.

  `/blender`                          Prepare a Blender 3D scene concept.

  `/midjourneystyle`                  Write a detailed image prompt using
                                      descriptive visual attributes.

  `/imageprompt`                      Turn an idea into a detailed
                                      image-generation prompt.
  -----------------------------------------------------------------------

## 4. Writing, productivity, coding & research

  Shortcut                Ask ChatGPT to...
  ----------------------- ------------------------------------------------
  `/rewrite`              Rewrite while preserving the original meaning.
  `/improve`              Improve clarity and quality.
  `/polish`               Make writing smoother.
  `/proofread`            Correct spelling and grammar.
  `/grammar`              Correct grammar only.
  `/copyedit`             Edit writing for professional quality.
  `/expand`               Add useful detail.
  `/shorten`              Make text shorter.
  `/paraphrase`           Express the same idea differently.
  `/simplifytext`         Rewrite in easier language.
  `/formal`               Use a formal tone.
  `/casual`               Use a casual conversational tone.
  `/friendly`             Use a warm, friendly tone.
  `/professional`         Use a professional business tone.
  `/persuasive`           Make the writing more persuasive.
  `/convincing`           Strengthen the argument.
  `/academic`             Use an academic writing format.
  `/journalistic`         Use a journalistic format.
  `/story`                Present information as a story.
  `/essay`                Write an essay.
  `/article`              Write an article.
  `/report`               Prepare a professional report.
  `/whitepaper`           Structure a white paper.
  `/casestudy`            Write a case study.
  `/proposal`             Create a proposal.
  `/sop`                  Write a standard operating procedure.
  `/playbook`             Create a practical playbook.
  `/manual`               Write a user manual.
  `/guide`                Create a step-by-step guide.
  `/faq`                  Create frequently asked questions.
  `/checklist`            Turn information into a checklist.
  `/template`             Create a reusable template.
  `/outline`              Create a structured outline.
  `/bulletpoints`         Organize the answer into bullet points.
  `/keypoints`            Show only the most important points.
  `/highlights`           Highlight important information.
  `/notes`                Create study or reference notes.
  `/minutes`              Write meeting minutes.
  `/agenda`               Create a meeting agenda.
  `/meetingsummary`       Summarize a meeting.
  `/todo`                 Create a to-do list.
  `/kanban`               Arrange tasks as a Kanban board.
  `/gantt`                Create a text-based Gantt plan.
  `/okr`                  Define objectives and key results.
  `/kpi`                  Identify key performance indicators.
  `/smartgoals`           Write SMART goals.
  `/roadmap90`            Create a 90-day roadmap.
  `/roadmapyear`          Create a one-year roadmap.
  `/milestones`           Identify project milestones.
  `/risks`                Identify project risks.
  `/riskmatrix`           Rank risks by likelihood and impact.
  `/dependencies`         Identify task dependencies.
  `/estimate`             Estimate effort or resources.
  `/budget`               Plan a budget.
  `/forecast`             Forecast possible outcomes.
  `/metrics`              Suggest useful metrics.
  `/dashboardmetrics`     Suggest dashboard measurements.
  `/decisiontree`         Create a decision tree.
  `/fishbone`             Analyze causes with a fishbone diagram.
  `/pareto`               Apply the 80/20 principle.
  `/lean`                 Apply Lean principles.
  `/sixsigma`             Apply Six Sigma methods.
  `/agile`                Apply an Agile approach.
  `/scrum`                Organize work using Scrum.
  `/kanbanflow`           Design a Kanban workflow.
  `/productivity`         Improve productivity.
  `/timemanagement`       Improve time management.
  `/pomodoro`             Create a Pomodoro work schedule.
  `/studyplan`            Create a study plan.
  `/revisionplan`         Create a revision timetable.
  `/learningpath`         Build a progressive learning path.
  `/feynman`              Explain using the Feynman technique.
  `/memory`               Suggest ways to remember information.
  `/mnemonics`            Create memory aids.
  `/practice`             Generate practice exercises.
  `/challengequestions`   Generate challenging questions.
  `/coding`               Write code for a task.
  `/explaincode`          Explain existing code.
  `/debug`                Find and explain bugs.
  `/refactor`             Improve code structure.
  `/optimizecode`         Improve code performance.
  `/reviewcode`           Review code quality.
  `/pseudocode`           Convert logic into pseudocode.
  `/algorithm`            Design an algorithm.
  `/datastructure`        Choose or explain a data structure.
  `/sql`                  Write or explain SQL.
  `/regex`                Create a regular expression.
  `/api`                  Design or explain an API.
  `/json`                 Generate or format JSON.
  `/yaml`                 Generate or format YAML.
  `/csv`                  Generate CSV data.
  `/xml`                  Generate or format XML.
  `/researchplan`         Plan a research project.
  `/literaturereview`     Summarize existing literature.
  `/hypothesis`           Develop research hypotheses.
  `/experiment`           Design an experiment.
  `/peerreview`           Critically review a piece of work.
  `/critic`               Give constructive criticism.
  `/audit`                Conduct a detailed audit.
  `/framework`            Select and apply an analytical framework.
  `/onepager`             One-page summaries.

## 5. Creative thinking, expert perspectives, AI workflows & advanced prompting

  Shortcut              Ask ChatGPT to...
  --------------------- --------------------------------------------------
  `/brainstorm`         Generate a wide range of ideas.
  `/ideas10`            Generate 10 ideas.
  `/ideas50`            Generate 50 ideas.
  `/creative`           Approach a task creatively.
  `/innovate`           Suggest innovative solutions.
  `/outofthebox`        Explore unconventional ideas.
  `/inspiration`        Generate creative inspiration.
  `/random`             Suggest unexpected ideas.
  `/combine`            Combine multiple concepts.
  `/remix`              Rework an existing idea.
  `/alternate`          Suggest alternative approaches.
  `/variants`           Create multiple versions.
  `/options`            Give several options.
  `/compareideas`       Compare different ideas.
  `/bestoption`         Identify the strongest option.
  `/decision`           Help make a decision.
  `/advisor`            Give general advisory guidance.
  `/mentor`             Act as a mentor.
  `/coach`              Use a coaching approach.
  `/teacher`            Teach a subject step by step.
  `/tutor`              Provide personal tutoring.
  `/professor`          Explain at university level.
  `/scientist`          Analyze from a scientific perspective.
  `/engineer`           Apply engineering thinking.
  `/doctor`             Explain medical topics educationally.
  `/lawyer`             Explain legal topics educationally.
  `/psychologist`       Explain from a psychology perspective.
  `/economist`          Analyze from an economic perspective.
  `/historian`          Explain from a historical perspective.
  `/journalist`         Investigate and report a topic.
  `/editor`             Improve and edit written material.
  `/designer`           Apply design thinking.
  `/architect`          Think about system architecture.
  `/productmanager`     Evaluate from a product-management perspective.
  `/founder`            Consider a startup founder's perspective.
  `/ceo`                Consider executive-level decisions.
  `/investorview`       Evaluate from an investor's perspective.
  `/customer`           Evaluate from a customer's perspective.
  `/beginner`           Explain for a complete beginner.
  `/advanced`           Explain at an advanced level.
  `/stepbystep`         Give sequential instructions.
  `/interactive`        Work through the task interactively.
  `/walkthrough`        Provide a detailed walkthrough.
  `/simulation`         Simulate a situation.
  `/negotiation`        Practice a negotiation.
  `/debate`             Present opposing viewpoints.
  `/counterargument`    Develop counterarguments.
  `/critique`           Evaluate strengths and weaknesses.
  `/improveidea`        Strengthen an existing idea.
  `/validate`           Test whether an idea is viable.
  `/assumptions`        Identify underlying assumptions.
  `/constraints`        Identify limitations and constraints.
  `/tradeoffs`          Explain compromises and trade-offs.
  `/opportunities`      Identify possible opportunities.
  `/risksfuture`        Analyze future risks.
  `/trendanalysis`      Analyze trends.
  `/forecastfuture`     Explore possible future developments.
  `/signals`            Identify early warning signals.
  `/emergingtech`       Explore emerging technologies.
  `/futureproof`        Make a plan more adaptable to the future.
  `/automation`         Identify automation opportunities.
  `/workflow`           Design a workflow.
  `/pipeline`           Design a process pipeline.
  `/systemthinking`     Analyze interconnected parts of a system.
  `/mentalmodels`       Apply useful mental models.
  `/heuristics`         Use practical decision-making rules.
  `/principles`         Explain the fundamental principles.
  `/frameworkcompare`   Compare analytical frameworks.
  `/bestpractice`       Suggest established best practices.
  `/mistakes`           Identify common mistakes.
  `/dosanddonts`        List recommended and discouraged actions.
  `/quickwins`          Find improvements that can be made quickly.
  `/optimization`       Optimize a process or solution.
  `/efficiency`         Improve efficiency.
  `/automationplan`     Create an automation roadmap.
  `/aiworkflow`         Design an AI-assisted workflow.
  `/promptaudit`        Review and improve a prompt.
  `/promptlibrary`      Organize prompts into a library.
  `/promptchain`        Connect prompts into a sequence.
  `/metaprompt`         Write a prompt that generates other prompts.
  `/systemprompt`       Draft system-level instructions.
  `/persona`            Define an AI persona.
  `/role`               Respond using a specified role.
  `/simulateexpert`     Simulate an expert perspective.
  `/multiexpert`        Analyze using multiple expert perspectives.
  `/consensus`          Identify areas of agreement.
  `/disagreement`       Identify conflicting viewpoints.
  `/evidence`           Support conclusions with evidence.
  `/confidence`         Explain confidence in an assessment.
  `/uncertainty`        Identify what remains uncertain.
  `/limitations`        State limitations clearly.
  `/assess`             Conduct a comprehensive assessment.
  `/scorecard`          Evaluate using a scoring system.
  `/ranking`            Rank choices.
  `/matrixcompare`      Compare choices in a matrix.
  `/finalanswer`        Give only the final answer.
  `/thinking`           Explain the reasoning approach at a high level.
  `/executemode`        Focus on completing the requested output.
  `/masterprompt`       Combine several prompt techniques.
  `/allinone`           Combine the most useful approaches for one task.

## 6. Extra shortcuts: communication, learning, careers & technical work

  Shortcut                Ask ChatGPT to...
  ----------------------- ------------------------------------------------------
  `/human`                Make writing sound more natural and human.
  `/humanize`             Remove robotic or unnatural wording.
  `/no-fluff`             Remove filler and unnecessary explanation.
  `/concise`              Answer briefly and directly.
  `/brief`                Give a short brief.
  `/tldr`                 Give the main points in a quick summary.
  `/eli10`                Explain in language a 10-year-old can understand.
  `/eli12`                Explain simply without making it childish.
  `/plainenglish`         Use everyday English.
  `/nontechnical`         Explain for a non-technical audience.
  `/technical`            Use precise technical language.
  `/romanurdu`            Explain or translate into Roman Urdu.
  `/urdu`                 Explain or translate into Urdu.
  `/translate`            Translate while preserving meaning and tone.
  `/localize`             Adapt language for a particular country or audience.
  `/tonecheck`            Identify and assess the tone of a text.
  `/audiencecheck`        Adapt content to its intended audience.
  `/stylematch`           Follow the style of a sample supplied by the user.
  `/askfirst`             Ask essential questions before solving.
  `/clarify`              Identify and resolve ambiguity.
  `/assumptionscheck`     Identify assumptions that may be incorrect.
  `/factsonly`            Separate established facts from opinions.
  `/citationcheck`        Check whether citations support the claims.
  `/sourceaudit`          Evaluate the reliability of sources.
  `/currentcheck`         Verify information that may have changed recently.
  `/countercheck`         Look for evidence that challenges a conclusion.
  `/uncertaintylabel`     Mark uncertain information clearly.
  `/privacycheck`         Identify possible privacy concerns.
  `/accessibility`        Make content more accessible.
  `/readability`          Improve readability and reading level.
  `/readaloud`            Format text for natural spoken delivery.
  `/quicknotes`           Create short notes for quick reference.
  `/meetingnotes`         Organize meeting notes.
  `/actionitems`          Extract tasks, owners, and deadlines.
  `/followup`             Draft a follow-up message.
  `/emailreply`           Write an appropriate email reply.
  `/dm`                   Draft a direct message.
  `/coverletter`          Write a job-specific cover letter.
  `/resume`               Improve a CV or résumé.
  `/ats`                  Make a résumé more ATS-friendly.
  `/jobmatch`             Compare a résumé against a job description.
  `/interviewanswers`     Prepare interview answers.
  `/salarynegotiation`    Practice salary negotiation.
  `/portfolio`            Improve a professional portfolio.
  `/projectbrief`         Create a clear project brief.
  `/userstories`          Write software user stories.
  `/acceptancecriteria`   Define acceptance criteria.
  `/testcases`            Generate software test cases.
  `/testplan`             Create a software test plan.
  `/securityreview`       Review a system for security weaknesses.
  `/threatmodel`          Identify potential threats and attack paths.
  `/performanceaudit`     Review performance bottlenecks.
  `/accessibilityaudit`   Review accessibility issues.
  `/database`             Design or explain a database.
  `/devops`               Explain or plan DevOps practices.
  `/dockerexplain`        Explain Docker concepts and commands.
  `/clouddeploy`          Plan cloud deployment steps.
  `/agentdesign`          Design an AI-agent workflow.
  `/mcpworkflow`          Plan a workflow using Model Context Protocol.
  `/n8nworkflow`          Design an n8n automation workflow.
  `/automationaudit`      Review a workflow for automation opportunities.

------------------------------------------------------------------------

## 7. Extended image, style & photo codes

Additional slash-style prompt shortcuts collected from community image and style libraries. They focus on visual styles, materials, subjects, scenes, camera angles, rendering techniques, and technical views.

### Technical & engineering

  Shortcut                            Ask ChatGPT to...
  ----------------------------------- -----------------------------------
  `/cad`                              CAD-style visualization.

  `/orthographic`                     Orthographic technical views.

  `/technicaldrawing`                 Technical illustration.

  `/transparent`                      Transparent/see-through object.


### Scientific & medical

  Shortcut                            Ask ChatGPT to...
  ----------------------------------- -----------------------------------
  `/ctscan`                           CT scan visualization.

  `/electronmicroscope`               Electron microscope style.

  `/microscope`                       Microscopic visualization.

  `/mri`                              MRI-style visualization.

  `/ultrasound`                       Ultrasound-style visualization.


### Industrial & architecture

  Shortcut                            Ask ChatGPT to...
  ----------------------------------- -----------------------------------
  `/elevation`                        Architectural elevation.

  `/floorplan`                        Floor plan.

  `/section`                          Architectural section view.

  `/siteplan`                         Site/landscape plan.


### Art & drawing styles

  Shortcut                            Ask ChatGPT to...
  ----------------------------------- -----------------------------------
  `/ascii`                            Creates image from keyboard text.

  `/claymation`                       Generates clay animation style.

  `/lego`                             Renders subject made from LEGO
                                      bricks.

  `/mangacover`                       Creates manga-style book cover.

  `/origami`                          Creates folded paper art style.

  `/papercut`                         Creates layered paper cutout art.

  `/stainedglass`                     Generates colorful glass window
                                      art.

  `/vaporwave`                        Generates retro pink-blue neon
                                      aesthetic.


### Art & illustration

  Shortcut                            Ask ChatGPT to...
  ----------------------------------- -----------------------------------
  `/noir`                             Noir cinematic style.

  `/popart`                           Pop-art aesthetic.


### Camera & photography

  Shortcut                            Ask ChatGPT to...
  ----------------------------------- -----------------------------------
  `/aerial`                           Aerial perspective.

  `/macro`                            Macro photography.

  `/wormseye`                         Low-angle perspective.


### 3D & rendering

  Shortcut                            Ask ChatGPT to...
  ----------------------------------- -----------------------------------
  `/chrome`                           Chrome material.

  `/claymodel`                        Clay-model appearance.

  `/glass`                            Glass/transparent material.

  `/glossy`                           Glossy material.

  `/highpoly`                         Detailed high-poly model.

  `/matte`                            Matte material.

  `/photoreal`                        Photorealistic rendering.

  `/studiolighting`                   Studio lighting.


### Diagrams & infographics

  Shortcut                            Ask ChatGPT to...
  ----------------------------------- -----------------------------------
  `/annotated`                        Annotated technical image.

  `/labeled`                          Labeled components.


### Technology & concept art

  Shortcut                            Ask ChatGPT to...
  ----------------------------------- -----------------------------------
  `/environmentdesign`                Environment concept.

  `/mech`                             Mechanical/mecha design.

  `/productdesign`                    Product concept.


### Nature & space

  Shortcut                            Ask ChatGPT to...
  ----------------------------------- -----------------------------------
  `/astronaut`                        Creates space explorer imagery.

  `/jungle`                           Generates tropical forest scenes.

  `/mars`                             Generates red planet landscapes.

  `/moonlight`                        Creates moonlit night scenes.

  `/nightcity`                        Creates city at night imagery.

  `/rain`                             Generates rainy atmosphere.

  `/snow`                             Creates snowy landscape scenes.

  `/storm`                            Creates thunderstorm scenes.

  `/volcano`                          Generates lava and fire scenes.


### Toys & miniatures

  Shortcut                            Ask ChatGPT to...
  ----------------------------------- -----------------------------------
  `/actionfigure`                     Creates collectible action figure.

  `/funko`                            Generates Funko Pop style figure.

  `/miniature`                        Creates tiny world diorama style.

  `/toybox`                           Generates toy figure look.


### Materials & textures

  Shortcut                            Ask ChatGPT to...
  ----------------------------------- -----------------------------------
  `/bronze`                           Generates bronze sculpture style.

  `/carbonfiber`                      Creates carbon fiber texture.

  `/ceramic`                          Creates ceramic finish appearance.

  `/crystal`                          Creates transparent crystal look.

  `/diamond`                          Generates diamond texture.

  `/doubleexposure`                   Generates two images blended.

  `/glassart`                         Generates artistic glass style.

  `/goldleaf`                         Creates gold foil appearance.

  `/holographic`                      Generates rainbow hologram effect.

  `/icecarving`                       Generates ice sculpture style.

  `/iridescent`                       Creates color-shifting surface.

  `/liquidmetal`                      Generates flowing metal style.

  `/marble`                           Creates marble statue appearance.

  `/mirror`                           Creates mirror reflection effect.

  `/moltengold`                       Creates melted gold appearance.

  `/oxidized`                         Generates green copper effect.

  `/pearlescent`                      Generates pearl shine effect.

  `/porcelain`                        Generates fine porcelain style.

  `/rusted`                           Creates rusty metal appearance.

  `/silverchrome`                     Generates chrome metal style.

  `/woodcarving`                      Creates wooden sculpture style.


### Places & adventure

  Shortcut                            Ask ChatGPT to...
  ----------------------------------- -----------------------------------
  `/artdeco`                          Creates elegant geometric design.

  `/bauhaus`                          Generates simple geometric art.

  `/boho`                             Generates bohemian style.

  `/brutalist`                        Creates raw concrete style.

  `/castle`                           Generates fantasy castle imagery.

  `/chalk`                            Creates chalk drawing style.

  `/cottagecore`                      Generates cozy rural aesthetic.

  `/crayon`                           Creates wax crayon art style.

  `/crochet`                          Generates yarn crochet art.

  `/dungeon`                          Creates dark dungeon scene.

  `/embroidery`                       Generates stitched artwork.

  `/fairytale`                        Creates fairy tale world imagery.

  `/felt`                             Creates felt fabric art style.

  `/fresco`                           Generates wall painting style.

  `/gouache`                          Creates gouache paint style.

  `/gradientmesh`                     Creates smooth color gradients.

  `/harbor`                           Generates port scene imagery.

  `/impasto`                          Creates thick paint texture.

  `/knitted`                          Creates knitted cloth style.

  `/lighthouse`                       Creates lighthouse scene.

  `/mandala`                          Generates circular pattern art.

  `/marker`                           Generates marker illustration.

  `/memphis`                          Generates colorful 80s design.

  `/mosaic`                           Creates tile art style.

  `/pastel`                           Generates soft pastel artwork.

  `/pirate`                           Generates pirate theme imagery.

  `/puppet`                           Generates wooden puppet style.

  `/quilling`                         Creates rolled paper art.

  `/sandart`                          Generates sand sculpture art.

  `/shipwreck`                        Generates sunken ship imagery.

  `/storybook`                        Generates children's book art.

  `/storybook3d`                      Creates 3D storybook style.

  `/tattoo`                           Generates tattoo design style.

  `/throneroom`                       Creates royal throne hall scene.

  `/treasure`                         Creates treasure chest scene.

  `/tribal`                           Creates tribal pattern art.

  `/village`                          Creates countryside village scene.

  `/zentangle`                        Creates detailed line art.


### Science & abstract

  Shortcut                            Ask ChatGPT to...
  ----------------------------------- -----------------------------------
  `/airport`                          Generates airport terminal scene.

  `/bonsai`                           Creates bonsai tree art.

  `/boombox`                          Creates 80s music player style.

  `/brain`                            Creates brain illustration.

  `/bridge`                           Creates bridge imagery.

  `/camera`                           Creates camera setup imagery.

  `/cassette`                         Generates cassette tape art.

  `/cinemalens`                       Generates camera lens close-up.

  `/equalizer`                        Generates audio bar visual.

  `/factory`                          Generates smart factory scene.

  `/flowerfield`                      Generates flower field scene.

  `/fractal`                          Creates infinite pattern imagery.

  `/garden`                           Generates garden imagery.

  `/geometry`                         Creates geometric shape art.

  `/headphones`                       Generates headphone showcase.

  `/infinity`                         Creates infinity symbol art.

  `/kaleidoscope`                     Generates colorful symmetry.

  `/laboratory`                       Creates science lab imagery.

  `/library`                          Generates grand library scene.

  `/musicvisualizer`                  Creates music animation style.

  `/neuralnetwork`                    Generates AI network visualization.

  `/sacredgeometry`                   Generates sacred pattern art.

  `/skyisland`                        Generates floating island imagery.

  `/skyscraper`                       Generates tall modern building.

  `/soundwave`                        Generates sound wave imagery.

  `/spiral`                           Generates spiral pattern art.

  `/subway`                           Generates metro station scene.

  `/trainstation`                     Creates railway station imagery.

  `/treehouse`                        Creates tree house scene.

  `/typewriter`                       Creates vintage typewriter imagery.

  `/vinylplayer`                      Creates record player imagery.

  `/warehouse`                        Creates industrial warehouse scene.

  `/waveform`                         Creates audio waveform visual.


### Animals & fantasy creatures

  Shortcut                            Ask ChatGPT to...
  ----------------------------------- -----------------------------------
  `/butterfly`                        Creates butterfly imagery.

  `/cat`                              Creates cat imagery.

  `/dog`                              Generates dog imagery.

  `/eagle`                            Generates eagle imagery.

  `/fox`                              Generates fox imagery.

  `/griffin`                          Generates griffin fantasy creature.

  `/horse`                            Creates horse imagery.

  `/kraken`                           Creates giant sea monster imagery.

  `/lion`                             Creates lion imagery.

  `/owl`                              Creates owl imagery.

  `/phoenix`                          Generates phoenix fantasy creature.

  `/unicorn`                          Creates unicorn fantasy creature.

  `/wolf`                             Generates wolf imagery.


### UI & technology

  Shortcut                            Ask ChatGPT to...
  ----------------------------------- -----------------------------------
  `/appui`                            Creates mobile app screen design.

  `/atom`                             Generates atom structure imagery.

  `/cell`                             Generates microscopic cell imagery.

  `/controlpanel`                     Creates futuristic controls.

  `/darkmode`                         Creates dark UI design.

  `/datacenter`                       Generates enterprise data center.

  `/dna`                              Creates DNA strand visual.

  `/glassui`                          Generates glass-style UI design.

  `/hacker`                           Generates hacker workspace scene.

  `/hud`                              Generates sci-fi display design.

  `/molecule`                         Creates molecule structure visual.

  `/nanotech`                         Generates nanotechnology imagery.

  `/neonui`                           Generates neon interface design.

  `/quantum`                          Creates quantum computing visual.

  `/serverroom`                       Creates data server room imagery.

  `/terminal`                         Creates hacker terminal style.

  `/website`                          Generates website layout design.

  `/wireframeui`                      Creates UI blueprint wireframe.


### Design & branding

  Shortcut                            Ask ChatGPT to...
  ----------------------------------- -----------------------------------
  `/albumcover`                       Generates music album cover.

  `/badge`                            Creates award badge design.

  `/bookcover`                        Generates hardcover book design.

  `/coatofarms`                       Generates royal coat of arms.

  `/coin`                             Creates coin design imagery.

  `/crest`                            Creates family crest design.

  `/currency`                         Generates banknote design.

  `/emblem`                           Generates premium emblem design.

  `/emoji`                            Creates 3D emoji design.

  `/icon`                             Generates app icon design.

  `/idcard`                           Generates ID card design.

  `/magazinecover`                    Creates magazine cover design.

  `/magicalbook`                      Generates magic ancient book.

  `/monogram`                         Generates letter-based logo.

  `/newspaper`                        Generates newspaper print style.

  `/passportphoto`                    Creates passport photo style.

  `/playingcard`                      Generates playing card design.

  `/scroll`                           Creates old scroll imagery.

  `/stamp`                            Generates postage stamp design.

  `/sticker`                          Generates sticker design.

  `/storybookcover`                   Creates children's book cover.

  `/tarotcard`                        Creates tarot card design.

  `/tradingcard`                      Creates trading card design.

  `/treasuremap`                      Creates pirate map design.

  `/vinyl`                            Creates vinyl record cover design.

  `/waxseal`                          Creates wax seal design.


---

# 🧩 Useful shortcut combinations

Combine a few compatible shortcuts to describe the outcome you want.

  ----------------------------------------------------------------------------------------
  Goal                                Suggested combination
  ----------------------------------- ----------------------------------------------------
  Learn a difficult topic             `/teacher + /eli5 + /analogy`

  Take study notes                    `/deepdive + /stickynotes + /quiz`

  Research a current topic            `/research + /sources + /factcheck`

  Challenge a business idea           `/founder + /swot + /redteam`

  Write natural content               `/human + /rewrite + /proofread`

  Prepare for a job interview         `/interview + /roleplay + /critique`

  Debug code                          `/debug + /explaincode + /reviewcode`

  Design an AI workflow               `/agentdesign + /workflow + /riskmatrix`

  Create a YouTube video              `/youtube + /storytelling + /retention`

  Create an image prompt              `/imageprompt + /cinematicphoto + /photorealistic`
  ----------------------------------------------------------------------------------------

## 🧪 Ready-to-copy examples

### Learn Docker

``` text
/teacher + /stepbystep + /stickynotes + /quiz

Teach me Docker from beginner level.
Explain every important concept in easy English.
Give practical commands and examples.
After each major concept, give me short notes.
At the end, test me with 10 multiple-choice questions.
Do not skip prerequisites.
```

### Create an AI-agent blueprint

``` text
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

### Research a topic

``` text
/research + /sources + /factcheck + /executivebrief

Research [TOPIC].
Prioritize reliable and recent sources.
Separate verified facts, opinions, and uncertain claims.
Include source links and dates.
Finish with a concise executive summary.
```

### Review code

``` text
/reviewcode + /securityreview + /performanceaudit

Review the code I provide.
Check correctness, security, performance, readability,
maintainability, and edge cases.
Prioritize findings by severity.
Explain each issue and suggest a fix.
Do not invent bugs that are not supported by the code.
```

------------------------------------------------------------------------

# 🛠️ Make these shortcuts reusable

For consistent results, save your preferred shortcut definitions in
Custom Instructions or in a ChatGPT Project's instructions.

For example, you can define:

``` text
When I begin a message with /teacher:
- Teach the topic step by step.
- Start with prerequisites.
- Use simple English.
- Include practical examples.
- Check my understanding.

When I begin a message with /stickynotes:
- Convert the material into short, clear notes.
- Keep one idea per note.
- Highlight important terms.
- Avoid unnecessary paragraphs.

When I begin a message with /blueprint:
- Create a complete, structured implementation plan.
- Include prerequisites, architecture, steps, examples,
  testing, deployment, monitoring, and risks.
- Identify missing information instead of guessing.
```

You can add more definitions in the same format. Keep the definitions
clear and avoid assigning conflicting meanings to the same shortcut.

------------------------------------------------------------------------

# 🤝 Contributing

This is an **open-source** project, and contributions of every size are
welcome. Add a missing shortcut, refine a definition, fix a typo, or improve
the skill package — every contribution makes the library more useful.

### 💭 Found a command that is missing?

You do not need to be a maintainer to suggest one:

- **Open an Issue** describing the shortcut, what it should do, and a short
  example.
- **Open a Pull Request** if you would like to add it yourself.

No contribution is too small. Even a single, well-described shortcut is
valuable.

### How to contribute

1. **Fork** the repository and create a branch for your change.
2. Add or improve the shortcut in `README.md` and in the skill package.
3. Search for duplicates and follow the definition format.
4. Run `python scripts/verify.py --check` and `python scripts/run_tests.py`
   (use `python3` on macOS/Linux).
5. Open a Pull Request explaining the change and giving one example.

The full guide — exact files to edit, commit conventions, and the review
checklist — is in [`CONTRIBUTING.md`](CONTRIBUTING.md).

Please follow our [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md). Report security
issues privately as described in [`SECURITY.md`](SECURITY.md).

------------------------------------------------------------------------

# ⭐ Support the project

This library is free and open source. If it helps you, here is how you
can give back:

- ⭐ **Star this repository** — it is the single best way to help others
  discover it.
- 🍴 **Fork it** and build your own personalized prompt library.
- 🔁 **Share it** with developers, students, creators, and AI
  enthusiasts.
- 💡 **Open an Issue or Pull Request** to add a shortcut we are
  missing — your contribution keeps the library growing.

Every star, contribution, and share helps the community discover better
ways to work with AI.

Useful links:
[Contributing](CONTRIBUTING.md) ·
[Code of Conduct](CODE_OF_CONDUCT.md) ·
[Security](SECURITY.md) ·
[Changelog](CHANGELOG.md) ·
[License](LICENSE)

------------------------------------------------------------------------

# 📄 License

This project is released under the **MIT License**. See
[LICENSE](LICENSE) for details.

You are welcome to use, copy, modify, and share this collection under
the license terms.

------------------------------------------------------------------------

<div align="center">
### Built for the community. Improved by the community. ⚡

**If it helps you, give it a ⭐ and help someone else discover it.**
</div>
