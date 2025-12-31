"""Output formatting for the CLI.

This module provides functions for displaying task information
and application messages with beautiful, professional formatting.
"""

from models import Task


# Unicode icons for status (ASCII-compatible for Windows)
ICON_COMPLETE = "[+]"
ICON_PENDING = "[ ]"
ICON_ADD = "[+]"
ICON_VIEW = "[...]"
ICON_EDIT = "[~]"
ICON_DELETE = "[x]"
ICON_CHECK = "[v]"
ICON_WARN = "[!]"
ICON_INFO = "[i]"
ICON_ERROR = "[X]"


def colored(text: str, color: str) -> str:
    """Add color to text."""
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "cyan": "\033[96m",
        "gray": "\033[90m",
        "reset": "\033[0m",
    }
    if color in colors:
        return f"{colors[color]}{text}{colors['reset']}"
    return text


def display_welcome() -> None:
    """Display the welcome message."""
    print()
    print("============================================")
    print("          TODO LIST APPLICATION")
    print("============================================")
    print()
    print(f"  1. Add Task {ICON_ADD}")
    print(f"  2. View Tasks {ICON_VIEW}")
    print(f"  3. Update Task {ICON_EDIT}")
    print(f"  4. Delete Task {ICON_DELETE}")
    print(f"  5. Mark Complete {ICON_CHECK}")
    print("  6. Exit >")
    print()


def display_goodbye() -> None:
    """Display the goodbye message."""
    print()
    print("  Thanks for using Todo App!")
    print("  See you again soon.")
    print()


def display_add_success(task: Task) -> None:
    """Display task added success message."""
    print()
    print(f"  {colored(f'{ICON_OK} Task added successfully!', 'green')}")
    print(f"  {colored(f'ID: [{task.id}]', 'cyan')}")
    print()


def display_delete_success(task_title: str) -> None:
    """Display task deleted success message."""
    print()
    print(f"  {colored(f'{ICON_OK} Task deleted!', 'green')}")
    print()


def display_update_success(task: Task) -> None:
    """Display task updated success message."""
    print()
    print(f"  {colored(f'{ICON_OK} Task updated!', 'green')}")
    print()


def display_toggle_complete(task: Task, is_now_complete: bool) -> None:
    """Display completion status change message."""
    print()
    if is_now_complete:
        print(f"  {colored(f'{ICON_OK} Task completed!', 'green')}")
    else:
        print(f"  {colored(f'{ICON_OK} Task marked incomplete!', 'yellow')}")
    print()


def display_already_complete(task: Task) -> None:
    """Display message when task is already complete."""
    print()
    print(f"  {colored(f'{ICON_INFO} Task is already complete!', 'yellow')}")
    print()


def display_task_not_found(task_id: int) -> None:
    """Display task not found error."""
    print()
    print(f"  {colored(f'{ICON_ERROR} Task not found!', 'red')}")
    print(f"  {colored(f'ID [{task_id}] does not exist', 'gray')}")
    print()


def display_empty_list() -> None:
    """Display message for empty task list."""
    print()
    print("============================================")
    print("               YOUR TASKS")
    print("============================================")
    print()
    print("  No tasks yet. Add a task to get started.")
    print()


def display_task_list(tasks: list[Task]) -> None:
    """Display all tasks in a formatted table."""
    print()
    print("========================================================")
    print("                     YOUR TASKS")
    print("========================================================")
    print()

    if not tasks:
        print("  No tasks found!")
        print()
        return

    # Fixed table layout: ID=4, STATUS=10, TITLE=28
    border = "+------+------------+------------------------------+"

    # Print table header
    print(border)
    print(f"| {'ID':<4} | {'STATUS':<10} | {'TITLE':<28} |")
    print(border)

    # Print each task row
    for task in tasks:
        if task.completed:
            status = "Done"
        else:
            status = "Pending"

        title = task.title[:28]
        if len(task.title) > 28:
            title = title[:-3] + "..."

        print(f"| {task.id:<4} | {status:<10} | {title:<28} |")

    # Print table footer
    print(border)

    # Stats footer
    pending = sum(1 for t in tasks if not t.completed)
    completed = len(tasks) - pending
    print()
    print(f"  Total: {len(tasks)} tasks ({colored(str(completed), 'green')} done, {colored(str(pending), 'yellow')} pending)")
    print()


def handle_invalid_choice() -> None:
    """Display error for invalid menu choice."""
    print()
    print(f"  {colored(f'{ICON_WARN} Invalid choice! Enter 1-6.', 'red')}")
    print()


def display_error(message: str) -> None:
    """Display a general error message."""
    print()
    print(f"  {colored(f'{ICON_ERROR} {message}', 'red')}")
    print()


# Keep for backward compatibility
ICON_OK = "[OK]"
