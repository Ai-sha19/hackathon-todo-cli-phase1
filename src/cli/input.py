"""Input handling and validation for the CLI.

This module provides functions for prompting user input and validating it.
"""
from typing import Optional


def prompt_input(prefix: str = "") -> str:
    """Get user input with a clean prompt."""
    if prefix:
        return input(f"  [{prefix}] > ").strip()
    return input("  > ").strip()


def validate_title(title: str) -> tuple[bool, str]:
    """Validate a task title."""
    title = title.strip()
    if not title:
        return False, "Task title cannot be empty."
    if len(title) > 200:
        return False, "Task title must be 200 characters or less."
    return True, ""


def validate_description(description: str) -> tuple[bool, str]:
    """Validate a task description."""
    if len(description) > 1000:
        return False, "Task description must be 1000 characters or less."
    return True, ""


def add_task_prompt() -> tuple[str, str]:
    """Prompt for adding a new task."""
    print("\n" + "─" * 44)
    print("         ADD NEW TASK")
    print("─" * 44)

    # Get title with validation
    while True:
        title = prompt_input("Title")
        is_valid, error = validate_title(title)
        if is_valid:
            break
        print(f"  Error: {error}")

    # Get description (optional)
    description = prompt_input("Description")

    # Validate description
    is_valid, error = validate_description(description)
    if not is_valid:
        print(f"  Warning: {error} Description will be truncated.")
        description = description[:1000]

    return title, description


def get_task_id_prompt() -> int:
    """Prompt for a task ID to delete."""
    print()
    while True:
        try:
            task_id_str = prompt_input("Delete ID")
            task_id = int(task_id_str)
            if task_id > 0:
                return task_id
            print("  Error: Task ID must be positive.")
        except ValueError:
            print("  Error: Please enter a valid number.")


def get_task_id_for_update() -> int:
    """Prompt for a task ID to update."""
    print()
    while True:
        try:
            task_id_str = prompt_input("Update ID")
            task_id = int(task_id_str)
            if task_id > 0:
                return task_id
            print("  Error: Task ID must be positive.")
        except ValueError:
            print("  Error: Please enter a valid number.")


def get_task_id_for_mark_complete() -> int:
    """Prompt for a task ID to mark as complete."""
    print()
    while True:
        try:
            task_id_str = prompt_input("Complete ID")
            task_id = int(task_id_str)
            if task_id > 0:
                return task_id
            print("  Error: Task ID must be positive.")
        except ValueError:
            print("  Error: Please enter a valid number.")


def get_update_prompts() -> tuple[Optional[str], Optional[str]]:
    """Prompt for updating a task."""
    print("\n" + "─" * 44)
    print("         UPDATE TASK")
    print("─" * 44)

    # Get new title
    title_input = prompt_input("New title")

    # Get new description
    desc_input = prompt_input("New description")

    # Return None if user wants to keep current value
    new_title = title_input if title_input else None
    new_description = desc_input if desc_input else None

    # Validate title if provided
    if new_title is not None:
        is_valid, error = validate_title(new_title)
        if not is_valid:
            print(f"  Error: {error}")
            return None, None

    # Validate description if provided
    if new_description is not None:
        is_valid, error = validate_description(new_description)
        if not is_valid:
            print(f"  Error: {error}")
            return None, None

    return new_title, new_description


def get_menu_choice() -> Optional[int]:
    """Get menu choice from user."""
    try:
        choice_str = prompt_input("Choice")
        choice = int(choice_str)
        if 1 <= choice <= 6:
            return choice
        return None
    except ValueError:
        return None


def confirm_action(prompt: str) -> bool:
    """Confirm a destructive action."""
    print()
    while True:
        response = input(f"  {prompt} (y/n): ").strip().lower()
        if response in ("y", "yes"):
            return True
        if response in ("n", "no"):
            return False
        print("  Please enter 'y' or 'n'.")


def pause_for_user() -> None:
    """Pause for user to read output."""
    print()
    input("  Press Enter to continue...")
