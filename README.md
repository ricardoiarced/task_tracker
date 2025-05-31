# task_tracker

A simple CLI task-tracker built in python.

## Installation

```bash
# 1. Clone the repo:
git clone https://github.com/ricardoiarced/task_tracker.git
cd task_tracker

# 2. Create and activate a virtualenv:
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies:
pip install -r requirements.txt

# (Optional) 4. Install the CLI tool:
pip install -e .
```

## Usage

### Add a task

```bash
python task_tracker.py add "Reading"
```

### Update a task's description

```bash
python task_tracker.py update 1 "Writing Chinese practice"
```

### Delete a task

```bash
python task_tracker.py delete 1
```

### Mark in-progress/done

```bash
python task_tracker.py mark-in-progress 2

python task_tracker.py mark-done 2
```

### List tasks

```bash
python task_tracker list
```

### List tasks by status

```bash
python task_tracker list --status in-progress
python task_tracker list --status done
```
## Commands

| Command | Description |
|---------|-------------|
| `add <desc>` | Create a new task with `<desc>` |
| `update <id> <desc>` | Change the description of task `<id>` |
| `delete <id>` | Remove task `<id>` |
| `mark-in-progress <id>` | Set task `<id>` to "in-progress" |
| `mark-done <id>` | Set task `<id>` to "done" |
| `list` | Show all tasks |
| `list --status STATUS` | Show tasks filtered by todo, in-progress, or done |

## Running Tests

To run tests and make sure everything works perfect you can run the following command on your terminal:

```bash
pytest -q
```