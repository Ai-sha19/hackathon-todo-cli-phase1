# Research: Phase 1 - In-Memory Console Todo App

## Summary

This document captures the research findings for implementing an in-memory Python console todo application. All technical decisions are based on the constitution requirements, hackathon specifications, and Python best practices.

## Technical Decisions

### 1. Python Version and Package Management

**Decision**: Python 3.13+ with UV package manager

**Rationale**:
- Python 3.13 is the latest stable release with performance improvements
- UV is specified in the constitution as the required package manager
- UV provides faster dependency resolution than pip
- UV supports PEP 8 compliant project structure

**Alternatives Considered**:
- pip: Slower, no longer the preferred tool per constitution
- Poetry: Good but constitution specifies UV
- pipenv: Deprecated in favor of UV

### 2. In-Memory Data Structure

**Decision**: Use Python dataclass for Task and a list-based TaskList class

**Rationale**:
- dataclass provides clean, type-annotated model definition
- List-based storage is simple and meets the in-memory requirement
- Auto-incrementing ID counter is straightforward to implement
- No external dependencies needed

**Implementation**:
```python
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    completed: bool = False

class TaskList:
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id: int = 1
```

### 3. CLI Interaction Pattern

**Decision**: Use a main loop with numbered menu options

**Rationale**:
- Simple, intuitive interface for console users
- Clear visual distinction between operations
- Easy to extend with additional menu options
- Standard pattern for CLI utilities

**Menu Structure**:
```
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete
6. Exit
```

### 4. Input Validation Strategy

**Decision**: Validate input at CLI layer, reject empty/whitespace titles

**Rationale**:
- Immediate feedback for users
- Prevents invalid data from entering the system
- Clear error messages as specified in requirements

**Validation Rules**:
- Title must be non-empty after strip()
- Title max 200 characters
- Description max 1000 characters
- Task ID must exist for operations requiring it

### 5. Error Handling Approach

**Decision**: Use custom exceptions with user-friendly messages

**Rationale**:
- Separates error handling from business logic
- Consistent error messages per requirements
- Easy to extend for additional error types

**Exception Types**:
- TaskNotFoundError: Raised when task ID doesn't exist
- ValidationError: Raised for invalid input
- EmptyTitleError: Raised when title is empty

### 6. Code Structure

**Decision**: Modular structure with separate modules for models, services, and CLI

**Rationale**:
- Clean separation of concerns
- Easy to test individual components
- Extensible for future phases
- Follows Python best practices

**Structure**:
```
src/
├── models/
│   └── task.py      # Task dataclass and TaskList class
├── services/
│   └── task_service.py  # Business logic
└── cli/
    └── main.py      # Entry point and menu loop
```

## Best Practices Reference

### PEP 8 Compliance
- Use 4 spaces for indentation
- Maximum line length: 88 characters (Black formatter default)
- Snake_case for function and variable names
- PascalCase for class names
- Descriptive docstrings for all public functions

### CLI Design Principles
- Clear prompts for each input
- Confirmation for destructive operations (delete)
- Visual feedback for successful operations
- Consistent error message format

### Error Message Format
```
Error: [Clear description]
Action: [Suggested next step]
```

## References

- [Python 3.13 Release Notes](https://docs.python.org/3.13/)
- [UV Documentation](https://docs.astral.sh/uv/)
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
- [Python dataclasses](https://docs.python.org/3/library/dataclasses.html)

## Notes

All decisions align with the constitution requirements:
- Spec-driven: All based on approved spec.md
- No manual coding: Implementation will be generated from tasks.md
- Traceability: Each decision links to specific requirements
