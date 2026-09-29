// Renders site/progress.json, which tools/progress.py generates from progress/curriculum.yml.
const TYPE_LABEL = {
  course: "Course", mini: "Mini", capstone: "Capstone",
  exit: "Exit test", cert: "Certificate", gate: "Gate",
};

const el = (tag, attrs = {}, ...kids) => {
  const n = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === "class") n.className = v;
    else if (k === "text") n.textContent = v;
    else n.setAttribute(k, v);
  }
  for (const kid of kids) if (kid != null) n.append(kid);
  return n;
};

const pct = (d, t) => (t ? Math.round((100 * d) / t) : 0);
const bar = (d, t, label) => {
  const b = el("div", { class: "bar", role: "progressbar", "aria-valuemin": "0",
    "aria-valuemax": String(t), "aria-valuenow": String(d), "aria-label": label });
  const fill = el("span");
  fill.style.width = `${pct(d, t)}%`;
  b.append(fill);
  return b;
};

function item(i) {
  const li = el("li", { class: i.evidence ? "done" : "todo" });
  li.append(el("span", { class: "tick", "aria-hidden": "true", text: i.evidence ? "✓" : "" }));
  const title = i.evidence
    ? el("a", { class: "title", href: i.evidence, rel: "noopener", text: i.title })
    : el("span", { class: "title", text: i.title });
  li.append(title);
  li.append(el("span", { class: "chip", text: TYPE_LABEL[i.type] || i.type }));
  li.setAttribute("aria-label", `${i.evidence ? "Done" : "Not done"}: ${i.title}`);
  return li;
}

function phase(p, open) {
  const d = el("details", { class: `phase${p.complete ? " complete" : ""}` });
  if (open) d.open = true;
  const t = el("div", { class: "ptitle" }, el("span", { text: p.title }), bar(p.done, p.total, `${p.id} progress`));
  d.append(el("summary", {},
    el("span", { class: "pid", text: p.id }), t,
    el("span", { class: "pcount", text: `${p.done}/${p.total}` })));
  d.append(el("ul", { class: "items" }, ...p.items.map(item)));
  return d;
}

function render(data) {
  const overall = document.getElementById("overall");
  overall.append(
    el("div", { class: "num" }, el("strong", { text: `${pct(data.done, data.total)}%` }),
      ` · ${data.done} of ${data.total} items have evidence`),
    bar(data.done, data.total, "Overall progress"));
  if (data.current) {
    overall.append(el("div", { class: "now" }, "Now: ",
      el("b", { text: `${data.current.level} · ${data.current.phase}` }), ` — ${data.current.title}`));
  }

  const levels = document.getElementById("levels");
  const detail = document.getElementById("detail");
  data.levels.forEach((lv) => {
    const card = el("button", { class: "level", type: "button" },
      el("h2", { text: lv.name }), el("p", { class: "tag", text: lv.tagline }),
      bar(lv.done, lv.total, `${lv.name} progress`),
      el("span", { class: "count", text: `${lv.done}/${lv.total} items · ${lv.phases_done}/${lv.phases_total} phases` }));
    card.addEventListener("click", () => document.getElementById(`level-${lv.id}`).scrollIntoView({ behavior: "smooth" }));
    levels.append(card);

    const block = el("section", { class: "level-block", id: `level-${lv.id}` },
      el("h2", { text: `${lv.name} — ${lv.tagline}` }),
      el("p", { class: "gate", text: `Gate: ${lv.gate}` }));
    lv.phases.forEach((p) => block.append(phase(p, data.current && p.id === data.current.phase)));
    if (lv.gate_items.length) {
      const g = lv.gate_items.filter((i) => i.evidence).length;
      block.append(phase({ id: "Gate", title: `${lv.name} gate: certificates and interview proof`,
        done: g, total: lv.gate_items.length, complete: g === lv.gate_items.length, items: lv.gate_items }, false));
    }
    detail.append(block);
  });

  const legend = document.getElementById("legend");
  Object.entries(TYPE_LABEL).forEach(([k, label]) => {
    const t = data.by_type[k];
    if (t && t.total) legend.append(el("span", { class: "chip", text: `${label} ${t.done}/${t.total}` }));
  });

  const toggle = document.getElementById("remaining-only");
  toggle.addEventListener("change", () => {
    document.querySelectorAll("li.done").forEach((li) => { li.hidden = toggle.checked; });
    document.querySelectorAll("details.phase.complete").forEach((d) => { d.hidden = toggle.checked; });
  });
}

fetch("progress.json", { cache: "no-store" })
  .then((r) => { if (!r.ok) throw new Error(r.status); return r.json(); })
  .then(render)
  .catch(() => {
    document.getElementById("detail").append(el("p", {},
      "Couldn't load the progress data. The same checklist is in ",
      el("a", { href: "https://github.com/MorenaDlamini/dotnet-ai-engineering/blob/master/PROGRESS.md", text: "PROGRESS.md" }), "."));
  });
