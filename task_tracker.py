import argparse
import json, os
from datetime import datetime

def add_task(db: dict[str, dict], description: str) -> None:
    today = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    id = str(int(max("0", *db.keys())) + 1)
    db[id] = {
        "description": description,
        "status": "todo",
        "created-at": today,
        "updated-at": today
    }

def update_task(db: dict[str, dict], id: str, description: str) -> None:
    today = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    db[id]["description"] = description
    db[id]["updated-at"] = today