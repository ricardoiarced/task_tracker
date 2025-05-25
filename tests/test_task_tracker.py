from task_tracker import (add_task)
import json
from pathlib import Path


def test_add_task_creates_a_new_id_with_timestamps() -> None:
    db = {}
    add_task(db, "Hello world!")
    assert len(db) == 1 and db["1"]["description"] == "Hello world!"
    add_task(db, "Walk the dog")
    add_task(db, "Study DSA")
    assert len(db) == 3 and db["3"]["description"] == "Study DSA"