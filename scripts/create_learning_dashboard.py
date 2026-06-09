#!/usr/bin/env python3
import argparse
import html
import json
from pathlib import Path


def load_json(value, name):
    try:
        data = json.loads(value)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid {name}: {exc}") from exc
    if not isinstance(data, list):
        raise SystemExit(f"{name} must be a JSON list")
    return data


def esc(value):
    return html.escape(str(value), quote=True)


def main():
    parser = argparse.ArgumentParser(description="Create a local learning dashboard HTML file.")
    parser.add_argument("--title", required=True)
    parser.add_argument("--subtitle", required=True)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--phases-json", required=True)
    parser.add_argument("--weeks-json", required=True)
    parser.add_argument("--resources-json", default="[]")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    phases = load_json(args.phases_json, "phases-json")
    weeks = load_json(args.weeks_json, "weeks-json")
    resources = load_json(args.resources_json, "resources-json")
    storage_slug = "".join(ch if ch.isalnum() else "_" for ch in args.slug)

    phase_cards = "\n".join(
        f'        <div class="phase"><strong>{esc(item.get("title", ""))}</strong><p>{esc(item.get("body", ""))}</p></div>'
        for item in phases
    )
    resource_cards = "\n".join(
        f'        <div class="resource"><h3>{esc(item.get("title", ""))}</h3><p>{esc(item.get("body", ""))}</p></div>'
        for item in resources
    )
    weeks_js = json.dumps(
        [[w.get("question", ""), w.get("tool", ""), w.get("output", "")] for w in weeks],
        ensure_ascii=False,
        indent=6,
    )

    document = f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(args.title)}</title>
  <style>
    :root {{
      --ink: #202124;
      --muted: #626a73;
      --line: #d7dce2;
      --paper: #f6f7f8;
      --panel: #ffffff;
      --accent: #0f766e;
      --accent-2: #9f4d1e;
      --accent-3: #344f9f;
      --done: #15803d;
      --shadow: 0 12px 34px rgba(32, 33, 36, 0.08);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      color: var(--ink);
      background: var(--paper);
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.55;
    }}
    header {{
      padding: 32px 24px 20px;
      border-bottom: 1px solid var(--line);
      background: #fbfcfd;
    }}
    .wrap {{
      width: min(1120px, calc(100% - 32px));
      margin: 0 auto;
    }}
    h1 {{
      margin: 0 0 8px;
      font-size: clamp(28px, 4vw, 48px);
      letter-spacing: 0;
      line-height: 1.1;
    }}
    h2 {{ margin: 0 0 14px; font-size: 22px; letter-spacing: 0; }}
    h3 {{ margin: 0 0 6px; font-size: 16px; letter-spacing: 0; }}
    p {{ margin: 0; }}
    .subtitle {{
      max-width: 820px;
      color: var(--muted);
      font-size: 17px;
    }}
    .topbar {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
      justify-content: space-between;
      margin-top: 24px;
    }}
    .progress-shell {{
      flex: 1 1 280px;
      height: 12px;
      overflow: hidden;
      border: 1px solid var(--line);
      background: #fff;
      border-radius: 999px;
    }}
    .progress-fill {{
      width: 0%;
      height: 100%;
      background: var(--accent);
      transition: width 180ms ease;
    }}
    .progress-text {{
      min-width: 128px;
      color: var(--muted);
      font-size: 14px;
      text-align: right;
    }}
    main {{ padding: 28px 0 44px; }}
    .section {{ margin-bottom: 28px; }}
    .grid, .resources {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 14px;
    }}
    .phase, .resource {{
      border: 1px solid var(--line);
      background: var(--panel);
      border-radius: 8px;
      padding: 16px;
      box-shadow: var(--shadow);
    }}
    .phase strong {{ display: block; margin-bottom: 6px; color: var(--accent); }}
    .phase:nth-child(2n) strong {{ color: var(--accent-2); }}
    .phase:nth-child(3n) strong {{ color: var(--accent-3); }}
    .phase p, .resource p {{ color: var(--muted); font-size: 14px; }}
    .weeks {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 12px;
    }}
    .week {{
      display: grid;
      grid-template-columns: 34px 1fr;
      gap: 12px;
      align-items: start;
      border: 1px solid var(--line);
      background: var(--panel);
      border-radius: 8px;
      padding: 14px;
    }}
    .week input {{
      width: 22px;
      height: 22px;
      margin: 2px 0 0;
      accent-color: var(--done);
    }}
    .week.done {{
      border-color: rgba(21, 128, 61, 0.35);
      background: #f2fbf3;
    }}
    .meta {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 9px;
    }}
    .tag {{
      display: inline-flex;
      align-items: center;
      min-height: 24px;
      padding: 2px 8px;
      border: 1px solid var(--line);
      border-radius: 999px;
      color: var(--muted);
      background: #fbfbfb;
      font-size: 12px;
    }}
    .notes {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
    }}
    textarea {{
      width: 100%;
      min-height: 180px;
      resize: vertical;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px;
      color: var(--ink);
      background: var(--panel);
      font: inherit;
    }}
    .button-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 12px;
    }}
    button {{
      min-height: 38px;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 0 14px;
      color: var(--ink);
      background: #fff;
      font: inherit;
      cursor: pointer;
    }}
    button.primary {{ color: #fff; border-color: var(--accent); background: var(--accent); }}
    @media (max-width: 860px) {{
      .grid, .weeks, .resources, .notes {{ grid-template-columns: 1fr; }}
      .progress-text {{ width: 100%; text-align: left; }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="wrap">
      <h1>{esc(args.title)}</h1>
      <p class="subtitle">{esc(args.subtitle)}</p>
      <div class="topbar">
        <div class="progress-shell" aria-label="progress">
          <div class="progress-fill" id="progressFill"></div>
        </div>
        <div class="progress-text" id="progressText">0 / {len(weeks)} weeks</div>
      </div>
    </div>
  </header>
  <main class="wrap">
    <section class="section">
      <h2>Phases</h2>
      <div class="grid">
{phase_cards}
      </div>
    </section>
    <section class="section">
      <h2>Weekly Track</h2>
      <div class="weeks" id="weeks"></div>
    </section>
    <section class="section">
      <h2>Anchor Resources</h2>
      <div class="resources">
{resource_cards}
      </div>
    </section>
    <section class="section">
      <h2>Current Notes</h2>
      <div class="notes">
        <textarea id="notes" placeholder="本周复盘：我原来的直觉是什么？现在能不能用自己的话讲出来？"></textarea>
        <textarea id="questions" placeholder="仍然不懂的问题：下次直接拿这些问我。"></textarea>
      </div>
      <div class="button-row">
        <button class="primary" id="saveNotes">保存笔记</button>
        <button id="resetProgress">重置勾选</button>
      </div>
    </section>
  </main>
  <script>
    const weeks = {weeks_js};
    const weeksEl = document.getElementById("weeks");
    const progressFill = document.getElementById("progressFill");
    const progressText = document.getElementById("progressText");
    const notes = document.getElementById("notes");
    const questions = document.getElementById("questions");
    const checked = JSON.parse(localStorage.getItem("{storage_slug}Weeks") || "{{}}");
    function renderWeeks() {{
      weeksEl.innerHTML = "";
      weeks.forEach((week, index) => {{
        const id = `week-${{index + 1}}`;
        const item = document.createElement("label");
        item.className = `week ${{checked[id] ? "done" : ""}}`;
        item.innerHTML = `
          <input type="checkbox" ${{checked[id] ? "checked" : ""}} data-week="${{id}}">
          <span>
            <h3>Week ${{index + 1}}: ${{week[0]}}</h3>
            <p>${{week[2]}}</p>
            <span class="meta"><span class="tag">${{week[1]}}</span></span>
          </span>
        `;
        weeksEl.appendChild(item);
      }});
      updateProgress();
    }}
    function updateProgress() {{
      const total = weeks.length;
      const done = Object.values(checked).filter(Boolean).length;
      progressFill.style.width = `${{(done / total) * 100}}%`;
      progressText.textContent = `${{done}} / ${{total}} weeks`;
      localStorage.setItem("{storage_slug}Weeks", JSON.stringify(checked));
    }}
    weeksEl.addEventListener("change", (event) => {{
      const box = event.target;
      if (!box.matches("input[type='checkbox']")) return;
      checked[box.dataset.week] = box.checked;
      box.closest(".week").classList.toggle("done", box.checked);
      updateProgress();
    }});
    document.getElementById("saveNotes").addEventListener("click", () => {{
      localStorage.setItem("{storage_slug}Notes", notes.value);
      localStorage.setItem("{storage_slug}Questions", questions.value);
    }});
    document.getElementById("resetProgress").addEventListener("click", () => {{
      Object.keys(checked).forEach((key) => delete checked[key]);
      renderWeeks();
    }});
    notes.value = localStorage.getItem("{storage_slug}Notes") || "";
    questions.value = localStorage.getItem("{storage_slug}Questions") || "";
    renderWeeks();
  </script>
</body>
</html>
"""

    output = Path(args.output).expanduser()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(document, encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
