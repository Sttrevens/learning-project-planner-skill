# User Learning Project Pattern

Use this reference when creating or updating durable learning projects.

## Typical Files

```text
<Topic>/
├── <slug>-learning-roadmap.md
├── <slug>-learning-context.md
├── <slug>-learning-dashboard.html
└── week-01-<first-topic>.md
```

## Pedagogical Pattern

- The goal is working intuition, not textbook completion.
- Each week has one core question.
- Each week has one math/tool/concept anchor.
- Each week includes a small exercise that must be done by hand, designed, or explained in the user's own words.
- Each week has a review prompt that records how the user's intuition changed.
- Materials are anchors, not the main route.

## Existing Examples

LoRA Learning:

- 12-week technical intuition track.
- Starts with matrices as transformations, then rank, neural networks, PEFT, LoRA, agent memory.
- Strong emphasis on hand calculation to avoid fake understanding.

Quantum Physics:

- 24-week worldview/formalism track.
- Starts with the collapse of classical physics, then linear algebra, quantum formalism, interpretation, information, synthesis.
- Strong emphasis on separating experiment, formalism, interpretation, and philosophy.

Enactive AI Learning:

- 18-week cross-disciplinary agent-intelligence track.
- Starts by separating LLM, agent, world model, and embodied intelligence.
- Connects Sutton/Rafiee, Hofstadter, world models, and game-agent design.
