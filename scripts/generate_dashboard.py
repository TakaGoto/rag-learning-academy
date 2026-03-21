#!/usr/bin/env python3
"""
Generate a self-contained HTML dashboard showing learning progress.

Reads progress/*.md files and outputs progress/dashboard.html.
Run with: python scripts/generate_dashboard.py
   or:    make dashboard
"""

import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROGRESS_DIR = ROOT / "progress"
CURRICULUM_DIR = ROOT / ".claude" / "docs" / "curriculum"

# Milestone definitions: (name, tagline, required_milestones_for_level)
MILESTONES = [
    ("First Light", "Built a working RAG system"),
    ("Data Wrangler", "Can process any document"),
    ("Vector Navigator", "Embeddings + vector DB mastery"),
    ("Retrieval Engineer", "Hybrid search + reranking"),
    ("Prompt Architect", "Grounded, cited generation"),
    ("Quality Guardian", "Evaluation-driven improvement"),
    ("Pattern Master", "Advanced RAG patterns"),
    ("Production Ready", "Deploy, monitor, scale"),
]

PROFICIENCY_LEVELS = [
    ("RAG Explorer", [1, 2], "#4CAF50"),
    ("RAG Practitioner", [3, 4, 5], "#2196F3"),
    ("RAG Engineer", [6, 7], "#9C27B0"),
    ("RAG Architect", [8], "#FF9800"),
]

TRACK_MILESTONES = {
    "Beginner": [1, 2, 3],
    "Intermediate": [3, 4, 5, 6],
    "Advanced": [5, 6, 7, 8],
}


def parse_profile(path: Path) -> dict:
    """Parse learner-profile.md into a dict."""
    if not path.exists():
        return {}
    text = path.read_text()
    profile = {}
    for line in text.split("\n"):
        m = re.match(r"- \*\*(.+?)\*\*:\s*(.+)", line)
        if m:
            profile[m.group(1).lower()] = m.group(2).strip()
        if line.startswith("Module"):
            profile["current_module"] = line.strip()
    return profile


def parse_curriculum_metadata() -> dict:
    """Parse lesson metadata (core/optional, duration) from curriculum files."""
    metadata = {}  # key: "N.N" -> {"type": "core"|"optional", "duration": "30 min"}
    for md_file in sorted(CURRICULUM_DIR.glob("module-*.md")):
        text = md_file.read_text()
        # Match headings like: ### 1.1 What is RAG — `core`
        for heading_match in re.finditer(r"### (\d+\.\d+) .+? — `(core|optional)`", text):
            lesson_id = heading_match.group(1)
            lesson_type = heading_match.group(2)
            # Find the Duration line after this heading
            start = heading_match.end()
            duration_match = re.search(r"\*\*Duration:\*\*\s*(\d+)\s*minutes?", text[start : start + 500])
            duration = int(duration_match.group(1)) if duration_match else 0
            metadata[lesson_id] = {"type": lesson_type, "duration": duration}
    return metadata


def parse_module_tracker(path: Path) -> list[dict]:
    """Parse module-tracker.md into a list of modules with lesson status."""
    if not path.exists():
        return []
    text = path.read_text()
    curriculum_meta = parse_curriculum_metadata()
    modules = []
    current = None

    for line in text.split("\n"):
        header = re.match(r"## Module (\d+): (.+)", line)
        if header:
            if current:
                modules.append(current)
            current = {
                "number": int(header.group(1)),
                "name": header.group(2),
                "lessons": [],
                "done": 0,
                "total": 0,
                "core_done": 0,
                "core_total": 0,
                "total_minutes": 0,
                "done_minutes": 0,
            }
        lesson = re.match(r"- \[([ x])\] (.+)", line)
        if lesson and current:
            is_done = lesson.group(1) == "x"
            lesson_name = lesson.group(2)
            # Extract lesson ID (e.g., "3.1" from "3.1 Understanding Vector Spaces (2026-03-21)")
            id_match = re.match(r"(\d+\.\d+)", lesson_name)
            lesson_id = id_match.group(1) if id_match else None
            meta = curriculum_meta.get(lesson_id, {})
            lesson_type = meta.get("type", "")
            duration = meta.get("duration", 0)

            current["lessons"].append(
                {
                    "name": lesson_name,
                    "done": is_done,
                    "type": lesson_type,
                    "duration": duration,
                }
            )
            current["total"] += 1
            current["total_minutes"] += duration
            if is_done:
                current["done"] += 1
                current["done_minutes"] += duration
            if lesson_type == "core":
                current["core_total"] += 1
                if is_done:
                    current["core_done"] += 1

    if current:
        modules.append(current)
    return modules


def parse_quiz_results(path: Path) -> list[dict]:
    """Parse quiz-results.md if it exists."""
    if not path.exists():
        return []
    text = path.read_text()
    results = []
    for line in text.split("\n"):
        m = re.match(r"- \*\*(.+?)\*\*.*?(\d+)%", line)
        if m:
            results.append({"topic": m.group(1), "score": int(m.group(2))})
    return results


def estimate_milestones(modules: list[dict], profile: dict) -> list[bool]:
    """Estimate which milestones are complete based on module progress."""
    completed_modules = set()
    for mod in modules:
        if mod["total"] > 0 and mod["done"] == mod["total"]:
            completed_modules.add(mod["number"])

    # Milestone completion rules (simplified from milestones.md)
    milestone_modules = {
        1: {1},
        2: {2},
        3: {3, 4},
        4: {5},
        5: {6},
        6: {7},
        7: {8},
        8: {9},
    }

    return [milestone_modules.get(i + 1, set()).issubset(completed_modules) for i in range(8)]


def get_proficiency_level(milestones_done: list[bool]) -> tuple[str, str, int]:
    """Determine current proficiency level."""
    level_name = "Getting Started"
    level_color = "#757575"
    level_index = -1

    for i, (name, required, color) in enumerate(PROFICIENCY_LEVELS):
        if all(milestones_done[m - 1] for m in required):
            level_name = name
            level_color = color
            level_index = i

    return level_name, level_color, level_index


def generate_html(profile: dict, modules: list[dict], quizzes: list[dict]) -> str:
    """Generate the full HTML dashboard."""
    milestones_done = estimate_milestones(modules, profile)
    level_name, level_color, level_index = get_proficiency_level(milestones_done)

    track = profile.get("track", "Unknown")
    started = profile.get("started", "Unknown")
    score = profile.get("assessment score", "?/10")

    total_lessons = sum(m["total"] for m in modules)
    done_lessons = sum(m["done"] for m in modules)
    pct = (done_lessons / total_lessons * 100) if total_lessons > 0 else 0

    total_core = sum(m["core_total"] for m in modules)
    done_core = sum(m["core_done"] for m in modules)
    total_minutes = sum(m["total_minutes"] for m in modules)
    done_minutes = sum(m["done_minutes"] for m in modules)
    remaining_minutes = total_minutes - done_minutes
    remaining_hours = remaining_minutes / 60

    today = datetime.now().strftime("%Y-%m-%d")
    if started and started != "Unknown":
        try:
            days_active = (datetime.now() - datetime.strptime(started, "%Y-%m-%d")).days
        except ValueError:
            days_active = 0
    else:
        days_active = 0

    track_ms = TRACK_MILESTONES.get(track, list(range(1, 9)))

    # Build milestone HTML
    milestone_html = ""
    for i, (name, tagline) in enumerate(MILESTONES):
        idx = i + 1
        if idx not in track_ms:
            continue
        done = milestones_done[i]
        status_class = "done" if done else "pending"
        icon = "&#10003;" if done else str(idx)
        milestone_html += f"""
        <div class="milestone {status_class}">
            <div class="milestone-icon">{icon}</div>
            <div class="milestone-info">
                <div class="milestone-name">{name}</div>
                <div class="milestone-tagline">{tagline}</div>
            </div>
        </div>"""

    # Build module progress HTML
    module_html = ""
    for mod in modules:
        mod_pct = (mod["done"] / mod["total"] * 100) if mod["total"] > 0 else 0
        status = "complete" if mod_pct == 100 else "in-progress" if mod_pct > 0 else "not-started"
        bar_color = "#4CAF50" if mod_pct == 100 else "#2196F3" if mod_pct > 0 else "#e0e0e0"

        lessons_html = ""
        for lesson in mod["lessons"]:
            check = "&#10003;" if lesson["done"] else "&#9675;"
            cls = "lesson-done" if lesson["done"] else "lesson-pending"
            badge = ""
            if lesson["type"] == "core":
                badge = ' <span class="badge badge-core">core</span>'
            elif lesson["type"] == "optional":
                badge = ' <span class="badge badge-optional">opt</span>'
            duration_str = f' <span class="lesson-duration">{lesson["duration"]}m</span>' if lesson["duration"] else ""
            lessons_html += f'<div class="lesson {cls}">{check} {lesson["name"]}{badge}{duration_str}</div>'

        module_html += f"""
        <div class="module-card {status}">
            <div class="module-header">
                <span class="module-number">{mod["number"]:02d}</span>
                <span class="module-name">{mod["name"]}</span>
                <span class="module-progress-text">{mod["done"]}/{mod["total"]} &middot; {mod["total_minutes"]}m</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {mod_pct}%; background: {bar_color};"></div>
            </div>
            <div class="lessons-list">{lessons_html}</div>
        </div>"""

    # Build proficiency level HTML
    level_html = ""
    for i, (lname, required, color) in enumerate(PROFICIENCY_LEVELS):
        achieved = i <= level_index
        cls = "level-achieved" if achieved else "level-locked"
        icon = "&#10003;" if achieved else "&#9679;"
        current = " current" if i == level_index else ""
        level_html += f"""
        <div class="level-badge {cls}{current}" style="{"border-color: " + color if achieved else ""}">
            <span class="level-icon" style="{"color: " + color if achieved else ""}">{icon}</span>
            <span class="level-name">{lname}</span>
        </div>"""

    # Quiz HTML
    quiz_html = ""
    if quizzes:
        quiz_html = '<div class="section"><h2>Quiz Scores</h2><div class="quiz-grid">'
        for q in quizzes:
            bar_color = "#4CAF50" if q["score"] >= 80 else "#FF9800" if q["score"] >= 60 else "#f44336"
            quiz_html += f"""
            <div class="quiz-card">
                <div class="quiz-topic">{q["topic"]}</div>
                <div class="quiz-score" style="color: {bar_color}">{q["score"]}%</div>
                <div class="progress-bar small">
                    <div class="progress-fill" style="width: {q["score"]}%; background: {bar_color};"></div>
                </div>
            </div>"""
        quiz_html += "</div></div>"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RAG Learning Academy — Progress Dashboard</title>
<style>
  :root {{
    --bg: #0d1117;
    --card: #161b22;
    --border: #30363d;
    --text: #e6edf3;
    --text-secondary: #8b949e;
    --accent: #58a6ff;
    --green: #3fb950;
    --yellow: #d29922;
    --red: #f85149;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.5;
    padding: 2rem;
    max-width: 960px;
    margin: 0 auto;
  }}
  h1 {{ font-size: 1.75rem; margin-bottom: 0.25rem; }}
  h2 {{ font-size: 1.25rem; margin-bottom: 1rem; color: var(--text); border-bottom: 1px solid var(--border); padding-bottom: 0.5rem; }}
  .subtitle {{ color: var(--text-secondary); margin-bottom: 2rem; }}
  .section {{ margin-bottom: 2.5rem; }}

  /* Stats bar */
  .stats {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 1rem;
    margin-bottom: 2rem;
  }}
  .stat {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1rem;
    text-align: center;
  }}
  .stat-value {{ font-size: 1.5rem; font-weight: 700; color: var(--accent); }}
  .stat-label {{ font-size: 0.8rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.05em; }}

  /* Proficiency levels */
  .levels {{
    display: flex;
    gap: 0.75rem;
    flex-wrap: wrap;
    margin-bottom: 1rem;
  }}
  .level-badge {{
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background: var(--card);
    border: 2px solid var(--border);
    border-radius: 24px;
    padding: 0.5rem 1rem;
    font-size: 0.85rem;
  }}
  .level-achieved {{ background: rgba(88, 166, 255, 0.08); }}
  .level-locked {{ opacity: 0.4; }}
  .level-badge.current {{ box-shadow: 0 0 0 2px rgba(88, 166, 255, 0.3); }}
  .level-icon {{ font-size: 1rem; }}

  /* Overall progress */
  .overall-progress {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1.5rem;
    margin-bottom: 2rem;
  }}
  .progress-header {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 0.75rem;
  }}
  .progress-pct {{ font-size: 2rem; font-weight: 700; color: var(--accent); }}
  .progress-detail {{ color: var(--text-secondary); font-size: 0.9rem; }}
  .progress-bar {{
    background: #21262d;
    border-radius: 6px;
    height: 10px;
    overflow: hidden;
  }}
  .progress-bar.small {{ height: 6px; margin-top: 0.25rem; }}
  .progress-fill {{
    height: 100%;
    border-radius: 6px;
    transition: width 0.5s ease;
  }}

  /* Milestones */
  .milestones {{
    display: grid;
    gap: 0.75rem;
  }}
  .milestone {{
    display: flex;
    align-items: center;
    gap: 1rem;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1rem;
  }}
  .milestone.done {{ border-left: 3px solid var(--green); }}
  .milestone.pending {{ opacity: 0.6; }}
  .milestone-icon {{
    width: 36px;
    height: 36px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 0.9rem;
    flex-shrink: 0;
  }}
  .milestone.done .milestone-icon {{ background: var(--green); color: #fff; }}
  .milestone.pending .milestone-icon {{ background: #21262d; color: var(--text-secondary); border: 2px solid var(--border); }}
  .milestone-name {{ font-weight: 600; }}
  .milestone-tagline {{ font-size: 0.8rem; color: var(--text-secondary); }}

  /* Module cards */
  .module-grid {{ display: grid; gap: 1rem; }}
  .module-card {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1rem;
  }}
  .module-card.complete {{ border-left: 3px solid var(--green); }}
  .module-card.in-progress {{ border-left: 3px solid var(--accent); }}
  .module-header {{
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 0.5rem;
  }}
  .module-number {{
    background: #21262d;
    color: var(--text-secondary);
    font-weight: 700;
    font-size: 0.75rem;
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
  }}
  .module-name {{ font-weight: 600; flex: 1; }}
  .module-progress-text {{ color: var(--text-secondary); font-size: 0.85rem; }}
  .lessons-list {{
    margin-top: 0.75rem;
    display: grid;
    gap: 0.25rem;
  }}
  .lesson {{ font-size: 0.85rem; padding: 0.15rem 0; }}
  .lesson-done {{ color: var(--green); }}
  .lesson-pending {{ color: var(--text-secondary); }}
  .badge {{ font-size: 0.65rem; padding: 0.1rem 0.4rem; border-radius: 3px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.03em; vertical-align: middle; }}
  .badge-core {{ background: rgba(63, 185, 80, 0.15); color: var(--green); }}
  .badge-optional {{ background: rgba(139, 148, 158, 0.15); color: var(--text-secondary); }}
  .lesson-duration {{ font-size: 0.75rem; color: var(--text-secondary); opacity: 0.7; }}

  /* Quiz cards */
  .quiz-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 0.75rem;
  }}
  .quiz-card {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1rem;
  }}
  .quiz-topic {{ font-weight: 600; font-size: 0.9rem; margin-bottom: 0.25rem; }}
  .quiz-score {{ font-size: 1.5rem; font-weight: 700; }}

  /* Footer */
  .footer {{
    text-align: center;
    color: var(--text-secondary);
    font-size: 0.8rem;
    padding-top: 2rem;
    border-top: 1px solid var(--border);
  }}
  .footer a {{ color: var(--accent); text-decoration: none; }}
</style>
</head>
<body>

<h1>RAG Learning Academy</h1>
<p class="subtitle">Progress Dashboard — generated {today}</p>

<div class="stats">
  <div class="stat">
    <div class="stat-value">{track}</div>
    <div class="stat-label">Track</div>
  </div>
  <div class="stat">
    <div class="stat-value">{score}</div>
    <div class="stat-label">Assessment</div>
  </div>
  <div class="stat">
    <div class="stat-value">{days_active}</div>
    <div class="stat-label">Days Active</div>
  </div>
  <div class="stat">
    <div class="stat-value">{done_lessons}/{total_lessons}</div>
    <div class="stat-label">Lessons Done</div>
  </div>
  <div class="stat">
    <div class="stat-value">{done_core}/{total_core}</div>
    <div class="stat-label">Core Lessons</div>
  </div>
  <div class="stat">
    <div class="stat-value">{remaining_hours:.0f}h</div>
    <div class="stat-label">Est. Remaining</div>
  </div>
</div>

<div class="section">
  <h2>Proficiency Level</h2>
  <div class="levels">{level_html}</div>
</div>

<div class="section">
  <div class="overall-progress">
    <div class="progress-header">
      <span class="progress-pct">{pct:.0f}%</span>
      <span class="progress-detail">{done_lessons} of {total_lessons} lessons completed</span>
    </div>
    <div class="progress-bar">
      <div class="progress-fill" style="width: {pct}%; background: var(--accent);"></div>
    </div>
  </div>
</div>

<div class="section">
  <h2>Milestones</h2>
  <div class="milestones">{milestone_html}</div>
</div>

{quiz_html}

<div class="section">
  <h2>Module Progress</h2>
  <div class="module-grid">{module_html}</div>
</div>

<div class="footer">
  <p>Generated by <a href="https://github.com/TakaGoto/rag-learning-academy">RAG Learning Academy</a></p>
  <p>Run <code>make dashboard</code> to regenerate &middot; Run <code>/roadmap</code> in Claude Code for interactive view</p>
</div>

</body>
</html>"""


def main():
    profile_path = PROGRESS_DIR / "learner-profile.md"
    tracker_path = PROGRESS_DIR / "module-tracker.md"
    quiz_path = PROGRESS_DIR / "quiz-results.md"

    if not profile_path.exists():
        print("No learner profile found. Run /start in Claude Code first.", file=sys.stderr)
        sys.exit(1)

    profile = parse_profile(profile_path)
    modules = parse_module_tracker(tracker_path)
    quizzes = parse_quiz_results(quiz_path)

    html = generate_html(profile, modules, quizzes)

    output_path = PROGRESS_DIR / "dashboard.html"
    output_path.write_text(html)
    print(f"Dashboard generated: {output_path}")


if __name__ == "__main__":
    main()
