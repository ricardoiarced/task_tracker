import argparse
import json, os
from datetime import datetime
from typing import Literal
from tabulate import tabulate

DATE_FMT = "%Y/%m/%d %H:%M:%S"
DATABASE_PATH = "tasks.json"

def load_database(path: str) -> dict[str, dict]:
    """
    If `path` exists and is valid JSON, load and return it.
    Otherwise returns an empty dict.
    """

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    
def save_database(db: dict[str, dict], path: str) -> None:
    """
    Overwrite (or create) `path` with the JSON dump of `db`.
    """
    with open(path, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

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

def parse_args() -> None:
    parser = argparse.ArgumentParser(prog="task_tracker")
    subs = parser.add_subparsers(dest="command", required=True)

    # add
    p = subs.add_parser("add", help="Add a new task")
    p.add_argument("description", help="Task description")

    # update
    p = subs.add_parser("update", help="Update a task's description")
    p.add_argument("id", help="ID of the task")
    p.add_argument("description", help="New description")

    # delete
    p = subs.add_parser("delete", help="Delete a task")
    p.add_argument("id", help="ID of the task")

    # in-progress
    p = subs.add_parser("mark-in-progress", help="Mark a task in-progress")
    p.add_argument("id", help="ID of the task")

    # done
    p = subs.add_parser("mark-done", help="Mark a task done")
    p.add_argument("id", help="ID of the task")

    # list
    p = subs.add_parser("list", help="List tasks")
    p.add_argument(
        "--status", "-s",
        choices=["all", "todo", "in-progress", "done"],
        default="all",
        help="Filter by status"
    )

    return parser.parse_args()

def dispatch_command(db, args) -> None:
    cmd = args.command

    if cmd == "add":
        add_task(db, args.description)
    elif cmd == "update":
        update_task(db, args.id, args.description)
    elif cmd == "delete":
        delete_task(db, args.id)
    elif cmd == "mark-in-progress":
        mark_task_in_progress(db, args.id)
    elif cmd == "mark-done":
        mark_task_done(db, args.id)
    elif cmd == "list":
        list_tasks(db, status=args.status)
    else:
        raise ValueError(f"Unknown command {cmd}")

def main():

    args = parse_args()

    db = load_database(DATABASE_PATH)

    try:
        dispatch_command(db, args)
    except KeyError:
        sys.exit("Error: no task with that ID")

    
    save_database(db, DATABASE_PATH)

if __name__ == "__main__":
    main()