"""Weekly idea review: writes <project>/تشغيل/المراجعة الأسبوعية - <project>.md (unique name per project) for every project folder in the vault.
Lists new ideas (last 7 days), approved ideas idle more than 30 days, and deferred ideas whose review date has come."""
import datetime as dt, pathlib, re, subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
today = dt.date.today()

def meta(p):
    t = p.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---", t, re.S)
    if not m:
        return {}
    return {k.strip(): v.strip() for k, v in (l.split(":", 1) for l in m.group(1).splitlines() if ":" in l)}

def day(s):
    try:
        return dt.date.fromisoformat((s or "")[:10])
    except ValueError:
        return None

for proj in sorted(d for d in ROOT.iterdir() if (d / "أفكار").is_dir()):
    new, idle, due = [], [], []
    for p in sorted((proj / "أفكار").glob("*.md")):
        m = meta(p)
        if m.get("type") != "idea":
            continue
        link, st = f"[[{p.stem}]]", m.get("status", "")
        created, updated, review = day(m.get("created")), day(m.get("updated")), day(m.get("review_by"))
        if created and (today - created).days <= 7:
            new.append(f"- {link} ({st})")
        if st == "معتمدة" and updated and (today - updated).days > 30:
            idle.append(f"- {link}: بلا حركة منذ {(today - updated).days} يوماً")
        if st in ("مؤجلة", "معتمدة", "قيد الدراسة") and review and review <= today:
            due.append(f"- {link} ({st}): موعد المراجعة {review}")
    out = proj / "تشغيل" / f"المراجعة الأسبوعية - {proj.name}.md"
    out.parent.mkdir(exist_ok=True)
    sec = lambda title, rows: f"## {title}\n" + ("\n".join(rows) if rows else "- لا شيء") + "\n"
    out.write_text(
        f"---\ntype: review\nupdated: {today}\n---\n# المراجعة الأسبوعية: {proj.name}\n\n"
        + sec("أفكار جديدة هذا الأسبوع", new) + "\n"
        + sec("أفكار معتمدة متوقفة أكثر من 30 يوماً", idle) + "\n"
        + sec("أفكار حان موعد مراجعتها", due) + "\n"
        + "القرار لصالح في كل فكرة: نبنيها، نؤجلها بموعد جديد، أو نلغيها مع السبب.\n",
        encoding="utf-8")

subprocess.run(["git", "-C", str(ROOT), "add", "-A"], check=False)
subprocess.run(["git", "-C", str(ROOT), "commit", "-qm", f"المراجعة الأسبوعية {today}"], check=False)
subprocess.run(["git", "-C", str(ROOT), "push", "-q"], check=False)
