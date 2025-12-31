# Quickstart: Phase 1 - Console Todo App

This guide provides the essential steps to set up and run the console todo application.

## Prerequisites

- Python 3.13 or higher
- UV package manager

## Setup

### 1. Install UV (if not already installed)

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Initialize the Project

```bash
# Navigate to project root
cd h2-todo

# Initialize UV project (creates pyproject.toml)
uv init

# Add Python 3.13 requirement
uv python cpython 3.13
```

### 3. Project Structure

After setup, your directory structure should be:

```
h2-todo/
├── pyproject.toml
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py
│   └── cli/
│       ├── __init__.py
│       └── menu.py
├── specs/
│   └── phase1-console/
│       ├── spec.md
│       ├── plan.md
│       ├── research.md
│       ├── data-model.md
│       └── contracts/
└── README.md
```

### 4. Install Dependencies

```bash
# Create virtual environment and install dependencies
uv venv
uv pip install .
```

## Running the Application

### Development Mode

```bash
# Run directly with Python
python src/main.py

# Or with UV
uv run python src/main.py
```

### Production Build

```bash
# Build the package
uv build

# Install in editable mode
uv pip install -e .
```

## Usage Workflow

### First Time Setup

1. Run `uv init` in the project directory
2. Verify Python version: `python --version`
3. Test UV installation: `uv --version`

### Running the Todo App

1. Execute: `python src/main.py`
2. You will see the main menu
3. Select option 1 to add your first task
4. View tasks with option 2
5. Practice all operations

### Exiting the Application

- Select option 6 (Exit) from the main menu
- Data is not persisted (in-memory only)

## Development Commands

| Command | Description |
|---------|-------------|
| `uv add <package>` | Add a dependency |
| `uv remove <package>` | Remove a dependency |
| `uv sync` | Sync dependencies |
| `uv pip list` | List installed packages |
| `uv python install 3.13` | Install Python 3.13 |

## Testing

```bash
# Run tests with pytest
uv run pytest

# Run with coverage
uv run pytest --cov
```

## Troubleshooting

### "Python 3.13 not found"

```bash
uv python install cpython 3.13
```

### "UV not recognized"

Restart your terminal after installing UV, or add UV to your PATH:
```bash
export PATH="$HOME/.local/bin:$PATH"  # macOS/Linux
```

### Module import errors

Ensure you're running from the project root and the virtual environment is activated:
```bash
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

## Next Steps

After successful setup:
1. Review the spec at `specs/phase1-console/spec.md`
2. Review the plan at `specs/phase1-console/plan.md`
3. Proceed to `/sp.tasks` to generate implementation tasks
4. Run `/sp.implement` to generate the code
