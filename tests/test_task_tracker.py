from task_tracker import (add_task, update_task, delete_task, mark_task_in_progress, mark_task_done, DATE_FMT)
import json
from pathlib import Path
from datetime import datetime

def test_add_task_creates_a_new_id_with_timestamps() -> None:
    db = {}
    add_task(db, "Hello world!")
    assert len(db) == 1 and db["1"]["description"] == "Hello world!"
    add_task(db, "Walk the dog")
    add_task(db, "Study DSA")
    assert len(db) == 3 and db["3"]["description"] == "Study DSA"

def test_update_task_changes_description_and_updated_at() -> None:
    original_date = datetime(2025,5,28,12,30,30)
    original_ts = original_date.strftime(DATE_FMT)

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

    parsed = datetime.strptime(new_ts, DATE_FMT)
    assert isinstance(parsed, datetime)

def test_delete_task() -> None:
    original_date = datetime(2025,5,28,12,30,30)
    original_ts = original_date.strftime(DATE_FMT)
    db = {
        "1": {
            "description": "Do exercise",
            "status": "done",
            "updated-at": original_ts,
            "created-at": original_ts,
        }
    }
    delete_task(db, "1")

    assert "1" not in db

def test_mark_task_in_progress() -> None:
    original_date = datetime(2025,5,28,12,30,30)
    original_ts = original_date.strftime(DATE_FMT)

    db = {
        "1": {
            "description": "Walk my dog",
            "status": "todo",
            "updated-at": original_ts,
            "created-at": original_ts,
        }
    }

    mark_task_in_progress(db, "1")

    assert db["1"]["status"] == "in-progress"
    assert db["1"]["created-at"] == original_ts
    new_ts = db["1"]["updated-at"]
    assert new_ts != original_ts

    parsed = datetime.strptime(new_ts, DATE_FMT)
    assert isinstance(parsed, datetime)

def test_mark_task_done() -> None:
    original_date = datetime(2025,5,28,12,30,30)
    original_ts = original_date.strftime(DATE_FMT)

    db = {
        "1": {
            "description": "Feed the dog",
            "status": "todo",
            "updated-at": original_ts,
            "created-at": original_ts,
        }
    }

    mark_task_done(db, "1")

    assert db["1"]["status"] == "done"
    assert db["1"]["created-at"] == original_ts
    new_ts = db["1"]["updated-at"]
    assert new_ts != original_ts

    parsed = datetime.strptime(new_ts, DATE_FMT)
    assert isinstance(parsed, datetime)