from task_tracker import (add_task, update_task)
import json
from pathlib import Path
from datetime import datetime

DATE_FORMAT = "%Y/%m/%d %H:%M:%S"

def test_add_task_creates_a_new_id_with_timestamps() -> None:
    db = {}
    add_task(db, "Hello world!")
    assert len(db) == 1 and db["1"]["description"] == "Hello world!"
    add_task(db, "Walk the dog")
    add_task(db, "Study DSA")
    assert len(db) == 3 and db["3"]["description"] == "Study DSA"

def test_update_task_changes_description_and_updated_at() -> None:
    original_date = datetime(2025,5,28,12,30,30)
    original_ts = original_date.strftime(DATE_FORMAT)

    db = {
        "1": {
            "description": "Hello, my friend!",
            "status": "todo",
            "updated-at": original_ts,
            "created-at": original_ts
        }
    }

    update_task(db, "1", "Hello, my dog!")

    assert db["1"]["description"] == "Hello, my dog!"
    assert db["1"]["created-at"] == original_ts

    new_ts = db["1"]["updated-at"]
    assert new_ts != original_ts

    parsed = datetime.strptime(new_ts, DATE_FORMAT)
    assert isinstance(parsed, datetime)