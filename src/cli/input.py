"""Input handling and validation for the CLI.

This module provides functions for prompting user input and validating it.
"""
from typing import Optional
import sys


def validate_title(title: str) -> tuple[bool, str]:
    """Validate a task title.

    Args:
        title: The title to validate.

    Returns:
        Tuple of (is_valid, error_message).
    """
    title = title.strip()
    if not title:
        return False, "Task title cannot be empty."
    if len(title) > 200:
        return False, "Task title must be 200 characters or less."
    return True, ""


def validate_description(description: str) -> tuple[bool, str]:
    """Validate a task description.

    Args:
        description: The description to validate.

    Returns:
        Tuple of (is_valid, error_message).
    """
    if len(description) > 1000:
        return False, "Task description must be 1000 characters or less."
    return True, ""


def add_task_prompt() -> tuple[str, str]:
    """Prompt for adding a new task.

    Returns:
        Tuple of (title, description).
    """
    print("\n=== Add New Task ===\n")

    # Get title with validation
    while True:
        title = input("Enter task title: ").strip()
        is_valid, error = validate_title(title)
        if is_valid:
            break
        print(f"Error: {error}")
        print("Please enter a valid title.")

    # Get description (optional)
    description = input(
        "Enter task description (optional, press Enter to skip): "
    ).strip()

    # Validate description
    is_valid, error = validate_description(description)
    if not is_valid:
        print(f"Warning: {error} Description will be truncated.")
        description = description[:1000]

    return title, description


def get_task_id_prompt() -> int:
    """Prompt for a task ID to delete.

    Returns:
        The validated task ID.
    """
    while True:
        try:
            task_id_str = input("Enter task ID to delete: ").strip()
            task_id = int(task_id_str)
            if task_id > 0:
                return task_id
            print("Error: Task ID must be a positive integer.")
        except ValueError:
            print("Error: Please enter a valid number.")


def get_task_id_for_update() -> int:
    """Prompt for a task ID to update.

    Returns:
        The validated task ID.
    """
    while True:
        try:
            task_id_str = input("Enter task ID to update: ").strip()
            task_id = int(task_id_str)
            if task_id > 0:
                return task_id
            print("Error: Task ID must be a positive integer.")
        except ValueError:
            print("Error: Please enter a valid number.")


def get_task_id_for_mark_complete() -> int:
    """Prompt for a task ID to mark as complete/incomplete.

    Returns:
        The validated task ID.
    """
    while True:
        try:
            task_id_str = input("Enter task ID to mark as complete: ").strip()
            task_id = int(task_id_str)
            if task_id > 0:
                return task_id
            print("Error: Task ID must be a positive integer.")
        except ValueError:
            print("Error: Please enter a valid number.")


def get_update_prompts() -> tuple[Optional[str], Optional[str]]:
    """Prompt for updating a task.

    Returns:
        Tuple of (new_title, new_description).
        Values are None if user pressed Enter to keep current.
    """
    print("\n=== Update Task ===\n")

    # Get new title
    title_input = input(
        "Enter new title (press Enter to keep current): "
    ).strip()

    # Get new description
    desc_input = input(
        "Enter new description (press Enter to keep current): "
    ).strip()

    # Return None if user wants to keep current value
    new_title = title_input if title_input else None
    new_description = desc_input if desc_input else None

    # Validate title if provided
    if new_title is not None:
        is_valid, error = validate_title(new_title)
        if not is_valid:
            print(f"Error: {error}")
            return None, None

    # Validate description if provided
    if new_description is not None:
        is_valid, error = validate_description(new_description)
        if not is_valid:
            print(f"Error: {error}")
            return None, None

    return new_title, new_description


def get_menu_choice() -> Optional[int]:
    """Get menu choice from user.

    Returns:
        The menu choice number, or None if invalid.
    """
    try:
        choice_str = input("\nEnter your choice (1-6): ").strip()
        choice = int(choice_str)
        if 1 <= choice <= 6:
            return choice
        return None
    except ValueError:
        return None


def confirm_action(prompt: str) -> bool:
    """Confirm a destructive action.

    Args:
        prompt: The confirmation prompt to display.

    Returns:
        True if confirmed, False otherwise.
    """
    while True:
        response = input(f"{prompt} (y/n): ").strip().lower()
        if response in ("y", "yes"):
            return True
        if response in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")


def pause_for_user() -> None:
    """Pause for user to read output."""
    input("\nPress Enter to continue...")
