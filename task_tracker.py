import argparse
import json, os
from datetime import datetime
from typing import Literal
from tabulate import tabulate

DATE_FMT = "%Y/%m/%d %H:%M:%S"

def add_task(db: dict[str, dict], description: str) -> None:
    today = datetime.now().strftime(DATE_FMT)
    id = str(int(max("0", *db.keys())) + 1)
    db[id] = {
        "description": description,
        "status": "todo",
        "created-at": today,
        "updated-at": today
    }

def update_task(db: dict[str, dict], id: str, description: str) -> None:
    db[id]["description"] = description
    db[id]["updated-at"] = datetime.now().strftime(DATE_FMT)

def delete_task(db: dict[str, dict], id: str) -> None:
    del db[id]

def mark_task_in_progress(db: dict[str, dict], id: str) -> None:
    db[id]["status"] = "in-progress"
    db[id]["updated-at"] = datetime.now().strftime(DATE_FMT)

def mark_task_done(db: dict[str, dict], id: str) -> None:
    db[id]["status"] = "done"
    db[id]["updated-at"] = datetime.now().strftime(DATE_FMT)

def list_tasks(db: dict[str, dict], status: Literal["all", "todo", "in-progress", "done"] = "all",
               ) -> None:
    rows = []

    for task_id, props in sorted(db.items(), key=lambda t: int(t[0])):
        if status == "all" or props["status"] == status:
            rows.append({
                "id": task_id,
                "description": props["description"],
                "status": props["status"],
                "created-at": props["created-at"],
                "updated-at": props["updated-at"],
            })

            if rows:
                print(tabulate(rows, headers="keys", tablefmt="rounded_grid"))
            else:
                print("Nothing to display")