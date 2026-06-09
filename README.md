# Learning Project Planner Skill

Create durable self-study projects for any topic by generating a roadmap,
long-term context file, local HTML dashboard, and first-week lesson.

## Use When

- Turning a topic into a reusable study workflow.
- Creating a learning roadmap with weekly core questions and exercises.
- Preserving long-term learning context for future agent sessions.
- Starting a self-study project that should survive beyond one conversation.
- Generating a local visual dashboard with phase cards, weekly checklists,
  progress tracking, notes, questions, and localStorage persistence.

## What It Creates

```text
<Topic>/
├── <slug>-learning-roadmap.md
├── <slug>-learning-context.md
├── <slug>-learning-dashboard.html
└── week-01-<first-topic>.md
```

The dashboard is a single local HTML file. It is not a hosted app or rich
visual editor, but it gives the learning project a visual control surface:
progress bar, phases, week checklist, anchor resources, and persistent notes.

## Dashboard Helper

The repository includes `scripts/create_learning_dashboard.py` so agents can
generate the dashboard from structured phase, week, and resource lists instead
of hand-writing HTML each time.

## Install

Point your agent or skills CLI at this repository. The skill entrypoint is:

```text
SKILL.md
```

Part of the [4D Games Skills](https://github.com/Sttrevens/4dgames-skills)
index.
