---
name: learning-project-planner
description: Use when a user wants to turn a study topic into a durable self-study project that future agent sessions can resume, with roadmap, context, dashboard, and first-week lesson artifacts.
---

# Learning Project Planner

Use this skill to turn a topic into a durable learning project, not a one-off study plan. The output should preserve long-term context so future agent sessions can resume the learning state quickly.

## Default Project Shape

```text
<topic>/
├── <slug>-learning-roadmap.md
├── <slug>-learning-context.md
├── <slug>-learning-dashboard.html
└── week-01-<first-topic>.md
```

## Workflow

1. Clarify only if necessary. If the user gives a topic and broad intent, proceed with reasonable assumptions.
2. Inspect nearby existing learning projects when available, especially user-specific examples under `~/Documents`.
3. Build the learning route around the user's purpose, not around a textbook table of contents.
4. Generate four artifacts: roadmap, context, dashboard, and first-week lesson.
5. Keep the first version compact enough to use immediately; leave room for future weekly notes.
6. Verify files exist and basic dashboard syntax is sane.

## Roadmap Requirements

- one-paragraph purpose
- 4-6 phases
- each phase has time, goal, themes, output standard
- a week-by-week table
- a fixed weekly template
- suggested prompts the user can say to the agent later

Good week rows use this shape:

```markdown
| Week | Core question | Tool / anchor material | Exercise output |
```

Choose the duration based on topic size:

- 6-8 weeks for compact tool or paper tracks
- 12 weeks for focused technical topics
- 18-24 weeks for cross-disciplinary or worldview topics
- 24+ weeks only when the user clearly wants a long course

## Context File Requirements

Create `<slug>-learning-context.md` with:

- update date
- total course objective
- file list
- current progress
- user current understanding state
- user strengths and risks
- teaching strategy
- key distinctions
- relation to nearby learning projects

This file is for future agent sessions. Write it as persistent state, not marketing copy.

## Week 01 Requirements

Create `week-01-<topic>.md` with:

- the first core question
- one intuitive explanation
- one concrete example
- one connection to the user's purpose
- 2-4 exercises
- 3-5 review questions

Do not overload Week 01 with the whole field. Its job is to start the track.

## Dashboard Requirements

Create `<slug>-learning-dashboard.html` as a local single-file dashboard with:

- progress bar
- phase cards
- week checklist
- anchor resources
- notes and questions textareas
- localStorage persistence

Prefer using `scripts/create_learning_dashboard.py` when generating a dashboard from structured phase/week lists.

Example:

```bash
python3 scripts/create_learning_dashboard.py \
  --title "Example Learning Dashboard" \
  --subtitle "A short purpose statement." \
  --slug "example" \
  --phases-json '[{"title":"1. Foundations","body":"Core concepts and first exercises."}]' \
  --weeks-json '[{"question":"Why does this matter?","tool":"Core distinction","output":"Write a five-sentence explanation"}]' \
  --resources-json '[{"title":"Anchor paper","body":"Read after Week 2."}]' \
  --output "/path/to/example-learning-dashboard.html"
```

## Teaching Bias

- Prefer core questions over chapter lists.
- Use papers, textbooks, videos, and docs as anchors, not the whole learning
  loop.
- Include one small exercise per week.
- Keep technical, philosophical, and product layers separate when the topic
  spans them.

## Common Failure Modes

- Producing only a chat answer instead of files.
- Overloading Week 01 with the whole field.
- Writing a dashboard that has no persistent notes or progress state.
- Losing the user's purpose and copying a generic syllabus.

## Existing User Patterns

When useful, inspect these projects as style anchors:

- `/Users/tianjiaowu/Documents/LoRA Learning`
- `/Users/tianjiaowu/Documents/Quantum Physics`
- `/Users/tianjiaowu/Documents/Enactive AI Learning`

Use `references/pattern.md` for the distilled pattern if you need a quick reminder.
