#!/usr/bin/env python3
"""Display CSV files with nice formatting."""
import sys, csv
from pathlib import Path

def read_csv(path, limit=10):
    rows = []
    with open(path) as f:
        for i, row in enumerate(csv.reader(f)):
            if i >= limit: break
            rows.append(row)
    return rows

if __name__ == "__main__":
    if len(sys.argv) < 2: print("Usage: csv_viewer.py <file.csv>"); sys.exit(1)
    path, limit = Path(sys.argv[1]), 10
    if not path.exists(): print("Error: File not found"); sys.exit(1)
    rows = read_csv(path, limit)
    if not rows: print("Empty CSV"); sys.exit(0)
    widths = [max(len(str(r[i])) if i < len(r) else 0 for r in rows) for i in range(len(rows[0]))]
    print("| " + " | ".join(str(rows[0][i]).ljust(widths[i]) for i in range(len(rows[0]))) + " |")
    print("|-" + "-|-".join("-"*w for w in widths) + "-|")
    for r in rows[1:]: print("| " + " | ".join(str(r[i]).ljust(widths[i]) if i < len(r) else "".ljust(widths[i]) for i in range(len(widths))) + " |")
