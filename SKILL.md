---
name: learning-project-planner
description: Create durable self-study projects for any topic by generating a roadmap, long-term context file, dashboard, and first-week lesson.
---

# Learning Project Planner

Use this skill to turn a topic into a durable self-study project rather than a
one-off study plan.

## Default Project Shape

```text
<topic>/
├── <slug>-learning-roadmap.md
├── <slug>-learning-context.md
├── <slug>-learning-dashboard.html
└── week-01-<first-topic>.md
```

## Workflow

1. Clarify only if necessary.
2. Inspect nearby existing learning projects when available.
3. Build the route around the user's purpose, not a textbook table of contents.
4. Generate four artifacts:
   - roadmap;
   - long-term context;
   - dashboard;
   - first-week lesson.
5. Keep Week 01 small enough to start immediately.
6. Verify files exist and the dashboard is syntactically sane.

## Roadmap Requirements

- One-paragraph purpose.
- 4-6 phases.
- Week-by-week table with core question, anchor material, and output.
- Recurring review template:
  - current intuition;
  - new understanding;
  - concrete worked example;
  - remaining confusion;
  - next gap.

## Teaching Bias

- Prefer core questions over chapter lists.
- Use papers, textbooks, videos, and docs as anchors, not the whole learning
  loop.
- Include one small exercise per week.
- Keep technical, philosophical, and product layers separate when the topic
  spans them.

