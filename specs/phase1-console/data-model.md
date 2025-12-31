# Data Model: Phase 1 - Console Todo App

## Overview

This document defines the data model for the in-memory console todo application. All entities are designed to be simple, type-annotated Python dataclasses that persist in memory for the duration of the session.

## Entities

### Task

Represents a single todo item in the system.

**Attributes**:

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `id` | int | Yes | Auto-generated | > 0, unique | Unique identifier for the task |
| `title` | str | Yes | N/A | 1-200 chars, not empty | Short task description |
| `description` | str | No | "" | 0-1000 chars | Detailed task information |
| `completed` | bool | No | False | N/A | Completion status |

**Validation Rules**:
- `title` must not be empty after `strip()`
- `title` must not exceed 200 characters
- `description` must not exceed 1000 characters
- `id` must be unique and never reused during session

**State Transitions**:

```
created (completed=False) <---> toggled ---> completed (completed=True)
                              ^
                              |
                        (toggle again)
```

### TaskList

Manages the collection of tasks in memory.

**Attributes**:

| Field | Type | Description |
|-------|------|-------------|
| `tasks` | List[Task] | List of all tasks |
| `next_id` | int | Counter for generating unique IDs |

**Methods**:

| Method | Parameters | Returns | Description |
|--------|------------|---------|-------------|
| `add_task(title, description)` | title: str, description: str | Task | Creates and returns a new task |
| `get_task(task_id)` | task_id: int | Task or None | Retrieves task by ID |
| `list_tasks()` | None | List[Task] | Returns all tasks |
| `delete_task(task_id)` | task_id: int | bool | Removes task, returns success |
| `update_task(task_id, title, description)` | task_id: int, title: str, description: str | Task or None | Updates task fields |
| `toggle_complete(task_id)` | task_id: int | Task or None | Toggles completion status |

**Relationships**:

```
TaskList "1" --> "*" Task : contains
```

## Data Flow

### Adding a Task

```
User Input --> Validate Title --> Create Task --> Assign ID --> Add to List --> Return Task
```

### Deleting a Task

```
User Input (ID) --> Find Task --> Remove from List --> Confirm Deletion
```

### Toggling Completion

```
User Input (ID) --> Find Task --> Toggle completed --> Update Task --> Return Updated Task
```

## In-Memory Storage

The TaskList instance persists for the duration of the CLI session:

```
Session Start --> TaskList() created --> Operations performed --> Session End (data lost)
```

**Constraints**:
- No persistence to disk in Phase 1
- No external database
- Data lost on application exit
- Supports at least 100 tasks per SC-006

## Example Data

```python
# After adding 3 tasks
tasks = TaskList()
task1 = tasks.add_task("Buy groceries", "Milk, eggs, bread")
task2 = tasks.add_task("Call mom", "Birthday wishes")
task3 = tasks.add_task("Finish report", "Q4 analysis")

# After marking task 1 as complete
tasks.toggle_complete(1)

# List state:
# [
#   Task(id=1, title="Buy groceries", completed=True),
#   Task(id=2, title="Call mom", completed=False),
#   Task(id=3, title="Finish report", completed=False)
# ]
```

## Validation Examples

### Valid Title
```
"Buy groceries"         -> Valid
"  Task title  "        -> Valid (strips to "Task title")
```

### Invalid Titles
```
""                      -> Invalid (empty after strip)
"   "                   -> Invalid (whitespace only)
"A" * 201               -> Invalid (> 200 chars)
```
