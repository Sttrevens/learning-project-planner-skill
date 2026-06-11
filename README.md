# Learning Project Planner Skill

Turn a topic into a self-study project that survives beyond one chat: roadmap,
long-term context, local dashboard, and a first-week lesson.

## 10-Second Proof

One prompt creates a folder like this:

```text
<Topic>/
├── <slug>-learning-roadmap.md
├── <slug>-learning-context.md
├── <slug>-learning-dashboard.html
└── week-01-<first-topic>.md
```

The visible artifact is the local HTML dashboard: phase cards, weekly checklist,
anchor resources, progress bar, notes, questions, and localStorage persistence.

## Why Install It

Ad hoc learning plans die with the conversation. This skill makes the learning
state durable, so a future agent can reopen the context file and continue
teaching from the same project memory instead of starting over.

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

## Minimum Run

```text
Use learning-project-planner to create a 12-week learning project for:
[topic]

My purpose is:
[why I want to learn it]
```

## Dashboard Helper

The repository includes `scripts/create_learning_dashboard.py` so agents can
generate the dashboard from structured phase, week, and resource lists instead
of hand-writing HTML each time.

## Safety Boundary

The skill creates local files. It should not publish a dashboard, overwrite an
existing learning project, or claim progress was completed unless the user
provides that state.

## Verification Assets

- [`examples/test-prompts.md`](examples/test-prompts.md) contains smoke tests
  for compact, technical, and cross-disciplinary learning projects.

## Install

Point your agent or skills CLI at this repository. The skill entrypoint is:

```text
SKILL.md
```

Part of the [4D Games Skills](https://github.com/Sttrevens/4dgames-skills)
index.
