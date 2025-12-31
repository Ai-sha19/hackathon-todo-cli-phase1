# CLI Command Contracts

This document defines the command-line interface contracts for the todo application.

## Main Menu

The application presents a numbered menu to the user:

```
===========================================
          TODO LIST APPLICATION
===========================================

1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete
6. Exit

===========================================
Enter your choice (1-6):
```

## Command Specifications

### 1. Add Task

**Input**:
```
=== Add New Task ===

Enter task title: [user input]
Enter task description (optional, press Enter to skip): [user input or Enter]
```

**Output (Success)**:
```
Task added successfully!
Task ID: 1

[Returns to main menu]
```

**Output (Error)**:
```
Error: Task title cannot be empty.
Please enter a valid title.

[Prompt again for title]
```

**Validation**:
- Title must be 1-200 characters (after strip)
- Description can be 0-1000 characters

---

### 2. View Tasks

**Input**: No additional input required

**Output (Empty List)**:
```
=== Your Tasks ===

No tasks found. Add a task to get started!

[Returns to main menu]
```

**Output (With Tasks)**:
```
=== Your Tasks ===

ID | Status    | Title
---|-----------|----------------------------------------
1  | [ ]       | Buy groceries
2  | [X]       | Call mom
3  | [ ]       | Finish report

Total: 3 tasks (2 pending, 1 completed)

[Returns to main menu]
```

**Display Format**:
- `[ ]` = Incomplete
- `[X]` = Complete
- Title truncated to 35 characters if longer
- Description shown on separate line if present

---

### 3. Update Task

**Input**:
```
=== Update Task ===

Enter task ID to update: [user input]
Task found: "Buy groceries"

Enter new title (press Enter to keep current): [user input or Enter]
Enter new description (press Enter to keep current): [user input or Enter]
```

**Output (Success)**:
```
Task updated successfully!

[Returns to main menu]
```

**Output (Task Not Found)**:
```
Error: Task with ID 5 not found.

[Returns to main menu]
```

**Output (Keep Current)**:
- Pressing Enter without typing keeps the current value
- Title: "" = keep current, otherwise update
- Description: "" = keep current, otherwise update

---

### 4. Delete Task

**Input**:
```
=== Delete Task ===

Enter task ID to delete: [user input]
```

**Output (Success)**:
```
Task "Buy groceries" deleted successfully.

[Returns to main menu]
```

**Output (Confirmation for Important Action)**:
```
Are you sure you want to delete "Buy groceries"? (y/n): [user input]
```

**Output (Task Not Found)**:
```
Error: Task with ID 5 not found.

[Returns to main menu]
```

---

### 5. Mark Complete

**Input**:
```
=== Mark Task Complete ===

Enter task ID to toggle: [user input]
```

**Output (Marked Complete)**:
```
Task "Buy groceries" marked as complete.

[Returns to main menu]
```

**Output (Marked Incomplete)**:
```
Task "Buy groceries" marked as incomplete.

[Returns to main menu]
```

**Output (Task Not Found)**:
```
Error: Task with ID 5 not found.

[Returns to main menu]
```

---

### 6. Exit

**Input**: No additional input required

**Output**:
```
Goodbye! Your tasks have been saved for this session.

[Application exits]
```

## Error Message Standards

All error messages follow this format:

```
Error: [Clear description of the problem]
```

**Common Error Messages**:

| Error | Message |
|-------|---------|
| Empty title | "Error: Task title cannot be empty." |
| Title too long | "Error: Task title must be 200 characters or less." |
| Task not found | "Error: Task with ID {id} not found." |
| Invalid menu choice | "Error: Invalid choice. Please enter a number 1-6." |

## Input Handling

**Special Keys**:
- `Ctrl+C` - Graceful exit with "Operation cancelled by user."
- `Enter` with no input - Uses default (keep current value for updates)

**Input Sanitization**:
- Leading/trailing whitespace is stripped
- Empty input after strip is validated
- Special characters are preserved as-is

## Session Flow

```
Start --> Main Menu --> Operation --> Output --> Main Menu --> ... --> Exit --> End
```
