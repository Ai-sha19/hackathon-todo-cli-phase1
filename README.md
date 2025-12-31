# H2 Todo Application

A simple in-memory console todo application built with Python 3.13 and UV.

## Features

- Add new tasks with title and optional description
- View all tasks with completion status
- Update task details
- Delete tasks
- Mark tasks as complete/incomplete

## Quick Start

### Prerequisites

- Python 3.13 or higher
- UV package manager

### Installation

```bash
# Install UV if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Initialize the project
uv venv
uv pip install -e .
```

### Running the Application

```bash
# Run the todo app
python src/main.py

# Or with UV
uv run python src/main.py
```

## Project Structure

```
h2-todo/
├── src/
│   ├── __init__.py
│   ├── main.py              # Entry point
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py          # Task and TaskList classes
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py  # Task business logic
│   └── cli/
│       ├── __init__.py
│       ├── menu.py          # CLI menu interface
│       ├── input.py         # Input validation
│       └── output.py        # Output formatting
├── tests/
│   ├── __init__.py
│   └── unit/
│       ├── __init__.py
│       ├── test_task.py     # Task model tests
│       └── test_service.py  # Service layer tests
├── specs/
│   └── phase1-console/
│       ├── spec.md          # Feature specification
│       ├── plan.md          # Implementation plan
│       ├── tasks.md         # Task list
│       └── ...
├── pyproject.toml
└── README.md
```

## Usage

1. Run the application: `python src/main.py`
2. Select an option from the menu:
   - `1` - Add a new task
   - `2` - View all tasks
   - `3` - Update a task
   - `4` - Delete a task
   - `5` - Mark task as complete/incomplete
   - `6` - Exit

## License

MIT
