#!/usr/bin/env python3

import sqlite3
from pathlib import Path

db_path = Path(__file__).parent / "stoic_math.db"


try:
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS virtues")
        c.execute("DROP TABLE IF EXISTS quotes")

        sql_statements = [
            """CREATE TABLE virtues (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT
            );""",

            """CREATE TABLE quotes (
                id INTEGER PRIMARY KEY,
                virtue_id INTEGER,
                quote TEXT,
                author TEXT,
                FOREIGN KEY (virtue_id) REFERENCES virtues(id)
            );"""
        ]

        for s in sql_statements:
            c.execute(s)


        virtues = [
            (0, "God / Logos", "The divine order, rational nature, and source of all virtue."),
            (1, "Justice", "Fairness, giving others their due, acting for the common good."),
            (2, "Discipline", "Self-mastery over desires and aversions; the discipline of assent."),
            (3, "Courage", "The moral strength to do what is right in the face of fear or pain."),
            (4, "Wisdom", "Sound judgment; the ability to distinguish what is good, bad, or indifferent.")
        ]
        c.executemany("INSERT INTO virtues (id, name, description) VALUES (?, ?, ?)", virtues)

        quotes = [
            (0, 0, "To follow nature is to follow God.", "Marcus Aurelius"),
            (1, 1, "Injustice anywhere is a threat to justice everywhere.", "Seneca"),
            (2, 2, "No man is free who is not master of himself.", "Epictetus"),
            (3, 3, "You have power over your mind—not outside events.", "Marcus Aurelius"),
            (4, 4, "Wisdom begins in wonder.", "Socrates")
        ]
        c.executemany("INSERT INTO quotes (id, virtue_id, quote, author) VALUES (?, ?, ?, ?)", quotes)

    conn.commit()
    print(f"Initialized db at {db_path}")
except sqlite3.OperationalError as e:
    print(f"Failed to create tables: {e}")
