"""Output formatting for the CLI.

This module provides functions for displaying task information
and application messages.
"""

from src.models.task import Task


def display_welcome() -> None:
    """Display the welcome message."""
    print("=" * 44)
    print("          TODO LIST APPLICATION")
    print("=" * 44)
    print()
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete")
    print("6. Exit")
    print()
    print("=" * 44)


def display_goodbye() -> None:
    """Display the goodbye message."""
    print()
    print("Goodbye! Your tasks have been saved for this session.")
    print()


def display_add_success(task: Task) -> None:
    """Display task added success message.

    Args:
        task: The newly created task.
    """
    print()
    print("Task added successfully!")
    print(f"Task ID: {task.id}")
    print()


def display_delete_success(task_title: str) -> None:
    """Display task deleted success message.

    Args:
        task_title: The title of the deleted task.
    """
    print()
    print(f'Task "{task_title}" deleted successfully.')
    print()


def display_update_success(task: Task) -> None:
    """Display task updated success message.

    Args:
        task: The updated task.
    """
    print()
    print("Task updated successfully!")
    print()


def display_toggle_complete(task: Task, is_now_complete: bool) -> None:
    """Display completion status change message.

    Args:
        task: The task that was toggled.
        is_now_complete: Whether the task is now complete.
    """
    status = "complete" if is_now_complete else "incomplete"
    print()
    print(f'Task "{task.title}" marked as {status}.')
    print()


def display_already_complete(task: Task) -> None:
    """Display message when task is already complete.

    Args:
        task: The task that is already complete.
    """
    print()
    print(f'Task "{task.title}" is already marked as complete.')
    print()


def display_task_not_found(task_id: int) -> None:
    """Display task not found error.

    Args:
        task_id: The ID that was not found.
    """
    print()
    print(f"Error: Task with ID {task_id} not found.")
    print()


def display_empty_list() -> None:
    """Display message for empty task list."""
    print("\n=== Your Tasks ===\n")
    print("No tasks found. Add a task to get started!")
    print()


def format_task_display(task: Task) -> str:
    """Format a single task for display.

    Args:
        task: The task to format.

    Returns:
        Formatted string representation.
    """
    status = "[X]" if task.completed else "[ ]"
    title = task.title[:35] + "..." if len(task.title) > 35 else task.title
    lines = [
        f"{status}  {title}",
    ]
    if task.description:
        desc = task.description[:70] + "..." if len(task.description) > 70 else task.description
        lines.append(f"     {desc}")
    return "\n".join(lines)


def display_task_list(tasks: list[Task]) -> None:
    """Display all tasks in a formatted table.

    Args:
        tasks: List of tasks to display.
    """
    print("\n=== Your Tasks ===\n")

    # Column widths - make ID column more prominent
    id_width = 4
    status_width = 10
    title_width = 50

    # Header with clear column labels
    id_header = "ID".center(id_width)
    status_header = "STATUS".center(status_width)
    title_header = "TITLE".center(title_width)
    print(f"{id_header} | {status_header} | {title_header}")
    print("-" * (id_width + status_width + title_width + 6))

    # Task rows
    for task in tasks:
        status = "Complete" if task.completed else "Pending"
        title = task.title[:48] + "..." if len(task.title) > 48 else task.title
        id_str = f"[{task.id}]"  # Make ID more prominent with brackets
        print(f"{id_str:<{id_width}} | {status:<{status_width}} | {title:<{title_width}}")
        if task.description:
            desc = task.description[:56] + "..." if len(task.description) > 56 else task.description
            print(f"{'':>{id_width + 2}}{desc}")

    # Footer
    print()
    pending = sum(1 for t in tasks if not t.completed)
    completed = len(tasks) - pending
    print(f"Total: {len(tasks)} tasks ({pending} pending, {completed} completed)")
    print()


def handle_invalid_choice() -> None:
    """Display error for invalid menu choice."""
    print()
    print("Error: Invalid choice. Please enter a number 1-6.")
    print()


def display_error(message: str) -> None:
    """Display a general error message.

    Args:
        message: The error message to display.
    """
    print()
    print(f"Error: {message}")
    print()
