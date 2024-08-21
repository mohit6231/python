import sqlite3
import json
from pathlib import Path

file = Path("sample3.json").read_text()
colors = json.loads(file)

with sqlite3.connect('db.sqlite3') as conn:
    command = 'Insert into colors values (?, ?, ?)'
    for color in colors:
        print(color)
        conn.execute(command, tuple(color.values))
        conn.commit()
