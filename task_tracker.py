import argparse
import json, os
from datetime import datetime

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
    db[id]["updated-at"] = datetime.now().strftime(DATE_FMT)
    db[id]["status"] = "in-progress"

def mark_task_done(db: dict[str, dict], id: str) -> None:
    db[id]["updated-at"] = datetime.now().strftime(DATE_FMT)
    db[id]["status"] = "done"