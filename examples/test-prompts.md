# Test Prompts

Use these prompts to check whether the skill creates durable project artifacts,
not just a study-plan answer.

## Compact Tool Track

```text
Use learning-project-planner to create a 6-week learning project for Playwright
browser automation. My purpose is to test local agent-built web apps without
manually clicking through every flow.
```

Expected behavior: creates roadmap, context, dashboard, and week-01 lesson;
duration is compact; exercises are practical.

## Technical Track

```text
Use learning-project-planner to create a 12-week learning project for real-time
multiplayer netcode in Unity. My purpose is to make better engineering calls in
an AI-native game prototype.
```

Expected behavior: separates concepts, implementation exercises, debugging, and
project risks instead of copying a textbook table of contents.

## Cross-Disciplinary Track

```text
Use learning-project-planner to create an 18-week learning project for enactive
AI and game design. My purpose is to connect cognitive science ideas to
prototype mechanics.
```

Expected behavior: uses a longer route, keeps philosophy/product/technical
layers distinct, and includes concrete weekly outputs.

## Existing Project Continuation

```text
Use learning-project-planner to resume this existing learning project from its
context file and produce Week 02.
```

Expected behavior: reads the context file first, preserves existing state, and
does not overwrite the dashboard or roadmap unless asked.
