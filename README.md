# Task Manager

A simple command-line Task Manager built in Python. It lets you add, view,
update, delete, and complete tasks, with all data persisted to a local
`data/tasks.json` file.

## Features

- **Add Task** — create a new task with a title (empty titles are rejected).
- **View Tasks** — list all tasks with their ID, title, and status.
- **Update Task** — change a task's title by ID.
- **Delete Task** — remove a task by ID. Remaining tasks keep their original,
  stable IDs (no renumbering).
- **Mark as Completed** — mark a task as done by ID.
- **Exit** — quit the program.

Tasks are stored as JSON objects with the shape:

```json
{"id": 1, "title": "Buy milk", "is_completed": false}
```

## Project Structure

```
task_manager/
├── main.py       # source code
├── data/
│   └── tasks.json  # created automatically on first run
└── README.md
```

## Requirements

- Python 3.10+ (uses `match`/`case`)

## How to Run

```bash
python3 main.py
```

The program reads from and writes to `data/tasks.json`, located next to
`main.py` (resolved via `pathlib`, so it works regardless of the directory
you run the command from). The `data/` folder and file are created
automatically the first time you add a task.

## Error Handling

- Invalid (non-numeric) menu choices and task IDs are caught and reported
  without crashing the program.
- A missing `data/tasks.json` on startup is treated as "no tasks yet."
- A corrupted/unreadable `data/tasks.json` is reported and the program
  starts with an empty task list instead of crashing.
- Failures while writing `data/tasks.json` (e.g. permissions issues) are
  caught and reported instead of crashing the program.

## Manual Testing Checklist

These scenarios were tested to confirm correct behavior:

- Add a task with a non-empty title → succeeds, task saved to `data/tasks.json`.
- Add a task with an empty title → rejected, no task added.
- Delete a task, then add a new one → deleted task's ID is not reused, and
  remaining tasks keep their original IDs.
- Start the program with no `data/tasks.json` present → starts with an empty list.
- Start the program with a corrupted `data/tasks.json` → reports the error and
  starts with an empty list instead of crashing.
- Enter a non-numeric menu choice / task ID → handled gracefully, program
  continues.

## Known Limitations / Possible Improvements

- No unit test suite yet (only manual testing, listed above).
- Single-file structure; could be split into modules (e.g. `storage.py`,
  `tasks.py`, `cli.py`) as the project grows.
