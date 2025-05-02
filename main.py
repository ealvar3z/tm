import sqlite3
from datetime import date
from jinja2 import Environment, FileSystemLoader
from pathlib import Path


def main():
    today = date.today()
    month, day = today.month, today.day
    total = month + day
    value = total % 5

    db_path = Path("data/stoic_math.db")
    conn = sqlite3.connect(db_path)
    row = conn.execute("""
        SELECT v.name, v.description, q.quote, q.author
        FROM virtues v
        LEFT JOIN quotes q ON v.id = q.virtue_id
        WHERE v.id = ?
        LIMIT 1
    """, (value,)).fetchone()
    conn.close()

    env = Environment(loader=FileSystemLoader("templates"))
    tmpl = env.get_template("index.html.j2")

    out = tmpl.render(
        intro=True,
        month=month,
        day=day,
        total=total,
        value=value,
        virtue=row[0],
        desc=row[1],
        quote=row[2],
        author=row[3],
        today=today.isoformat(),
    )

    build_dir = Path("build")
    build_dir.mkdir(exist_ok=True)
    (build_dir / "index.html").write_text(out)
    print("Site built [static/index.html]")

if __name__ == "__main__":
    main()
