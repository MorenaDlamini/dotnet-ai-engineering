"""Turn progress/curriculum.yml into PROGRESS.md, the README summary and site/progress.json.

An item is done when its `evidence` holds a URL, and at no other time. `--check` fails if an
item is malformed, if evidence is not a URL, or if the generated files are out of date.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "progress" / "curriculum.yml"
PROGRESS_MD = ROOT / "PROGRESS.md"
README = ROOT / "README.md"
SITE_JSON = ROOT / "site" / "progress.json"
DASHBOARD = "https://morenadlamini.github.io/dotnet-ai-engineering/"

TYPES = ("course", "mini", "capstone", "exit", "cert", "gate")  # ordered: it sets the JSON key order
# Built work has to point at GitHub; certificates and course completions can live anywhere.
GITHUB_ONLY = {"mini", "capstone"}
TYPE_LABEL = {
    "course": "Course", "mini": "Mini", "capstone": "Capstone",
    "exit": "Exit test", "cert": "Certificate", "gate": "Gate",
}
START, END = "<!-- PROGRESS:START -->", "<!-- PROGRESS:END -->"


def load() -> dict:
    return yaml.safe_load(SOURCE.read_text(encoding="utf-8"))


def items_of(level: dict):
    for phase in level["phases"]:
        yield from phase["items"]
    yield from level.get("gate_items", [])


def validate(data: dict) -> list[str]:
    problems: list[str] = []
    seen: set[str] = set()
    for level in data.get("levels", []):
        for item in items_of(level):
            iid = item.get("id", "<no id>")
            if iid in seen:
                problems.append(f"{iid}: duplicate id")
            seen.add(iid)
            if item.get("type") not in TYPES:
                problems.append(f"{iid}: unknown type {item.get('type')!r}")
            if not item.get("title"):
                problems.append(f"{iid}: missing title")
            ev = item.get("evidence")
            if ev is None:
                continue
            if not isinstance(ev, str) or not ev.startswith("https://"):
                problems.append(f"{iid}: evidence must be an https URL, got {ev!r}")
            elif item["type"] in GITHUB_ONLY and not ev.startswith("https://github.com/"):
                problems.append(f"{iid}: a {item['type']} must link to GitHub, got {ev}")
    return problems


def count(items) -> tuple[int, int]:
    items = list(items)
    return sum(1 for i in items if i.get("evidence")), len(items)


def bar(done: int, total: int, width: int = 20) -> str:
    filled = round(width * done / total) if total else 0
    return "█" * filled + "░" * (width - filled)


def pct(done: int, total: int) -> int:
    return round(100 * done / total) if total else 0


def summarise(data: dict) -> dict:
    levels, all_items, current = [], [], None
    for level in data["levels"]:
        phases = []
        for phase in level["phases"]:
            d, t = count(phase["items"])
            phases.append({
                "id": phase["id"], "title": phase["title"], "done": d, "total": t,
                "complete": d == t,
                "items": [
                    {"id": i["id"], "type": i["type"], "title": i["title"],
                     "evidence": i.get("evidence")}
                    for i in phase["items"]
                ],
            })
            if current is None and d < t:
                current = {"level": level["name"], "phase": phase["id"], "title": phase["title"]}
        gate = [
            {"id": i["id"], "type": i["type"], "title": i["title"], "evidence": i.get("evidence")}
            for i in level.get("gate_items", [])
        ]
        d, t = count(items_of(level))
        all_items.extend(items_of(level))
        levels.append({
            "id": level["id"], "name": level["name"], "tagline": level["tagline"],
            "gate": level["gate"], "done": d, "total": t,
            "phases_done": sum(p["complete"] for p in phases), "phases_total": len(phases),
            "phases": phases, "gate_items": gate,
        })
    d, t = count(all_items)
    by_type = {}
    for ty in TYPES:
        bd, bt = count(i for i in all_items if i["type"] == ty)
        by_type[ty] = {"done": bd, "total": bt}
    return {"done": d, "total": t, "current": current, "by_type": by_type, "levels": levels}


def render_progress_md(s: dict) -> str:
    out = [
        "# Progress",
        "",
        "Generated from `progress/curriculum.yml` by `tools/progress.py`. Don't edit by hand.",
        "An item is ticked only when it links to evidence.",
        f"The same data, as a page: {DASHBOARD}",
        "",
        f"**Overall:** `{bar(s['done'], s['total'])}` {s['done']}/{s['total']} ({pct(s['done'], s['total'])}%)",
    ]
    if s["current"]:
        c = s["current"]
        out += ["", f"**Now:** {c['level']} · {c['phase']} — {c['title']}"]
    out.append("")
    for lv in s["levels"]:
        out += [
            f"## {lv['name']} — {lv['tagline']}",
            "",
            (
                f"`{bar(lv['done'], lv['total'])}` {lv['done']}/{lv['total']} items · "
                f"{lv['phases_done']}/{lv['phases_total']} phases"
            ),
            "",
            f"**Gate:** {lv['gate']}",
            "",
        ]
        for ph in lv["phases"]:
            mark = " ✅" if ph["complete"] else ""
            out.append(f"### {ph['id']} — {ph['title']} ({ph['done']}/{ph['total']}){mark}")
            out.append("")
            out += [line(i) for i in ph["items"]]
            out.append("")
        if lv["gate_items"]:
            out.append(f"### {lv['name']} gate")
            out.append("")
            out += [line(i) for i in lv["gate_items"]]
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def line(i: dict) -> str:
    label = TYPE_LABEL[i["type"]]
    if i["evidence"]:
        return f"- [x] **{label}:** [{i['title']}]({i['evidence']})"
    return f"- [ ] **{label}:** {i['title']}"


def render_readme_block(s: dict) -> str:
    rows = ["| Level | Progress | Phases |", "|---|---|---|"]
    for lv in s["levels"]:
        rows.append(
            f"| {lv['name']} | `{bar(lv['done'], lv['total'], 12)}` {lv['done']}/{lv['total']} "
            f"| {lv['phases_done']}/{lv['phases_total']} |"
        )
    now = ""
    if s["current"]:
        c = s["current"]
        now = f"**Now:** {c['level']} · {c['phase']} — {c['title']}\n\n"
    return (
        f"{START}\n{now}" + "\n".join(rows)
        + f"\n\nEvery item links to its evidence in [PROGRESS.md](PROGRESS.md), "
        f"and on the [dashboard]({DASHBOARD}).\n{END}"
    )


def with_readme_block(text: str, block: str) -> str:
    if START in text:
        return re.sub(re.escape(START) + r".*?" + re.escape(END), block, text, flags=re.DOTALL)
    anchor = "## Challenges"
    section = f"## Progress through the levels\n\n{block}\n\n"
    return text.replace(anchor, section + anchor, 1) if anchor in text else text + "\n" + section


def outputs(s: dict) -> dict[Path, str]:
    readme = README.read_text(encoding="utf-8")
    return {
        PROGRESS_MD: render_progress_md(s),
        README: with_readme_block(readme, render_readme_block(s)),
        SITE_JSON: json.dumps(s, indent=2, ensure_ascii=False) + "\n",
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="validate, and fail if outputs are stale")
    args = ap.parse_args()

    data = load()
    problems = validate(data)
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    s = summarise(data)
    files = outputs(s)

    if args.check:
        stale = [p.relative_to(ROOT).as_posix() for p, text in files.items()
                 if not p.exists() or p.read_text(encoding="utf-8") != text]
        if stale:
            print(f"out of date: {', '.join(stale)}. Run: python tools/progress.py", file=sys.stderr)
            return 1
        print(f"progress ok: {s['done']}/{s['total']} items with evidence")
        return 0

    for p, text in files.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8", newline="\n")
    print(f"{s['done']}/{s['total']} items with evidence; wrote PROGRESS.md, README.md, site/progress.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
