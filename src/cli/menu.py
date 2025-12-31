"""CLI menu interface for the todo application.

This module provides the main menu loop and handlers for each
menu option.
"""

from models.task import Task, TaskList
from cli.input import (
    add_task_prompt,
    get_task_id_prompt,
    get_task_id_for_update,
    get_task_id_for_mark_complete,
    get_update_prompts,
    get_menu_choice,
    confirm_action,
    pause_for_user,
)
from cli.output import (
    display_add_success,
    display_delete_success,
    display_update_success,
    display_toggle_complete,
    display_already_complete,
    display_task_not_found,
    display_empty_list,
    display_task_list,
    handle_invalid_choice,
    display_welcome,
    display_goodbye,
)


def handle_add_task(tasklist: TaskList) -> None:
    """Handle adding a new task."""
    try:
        title, description = add_task_prompt()
        task = tasklist.add_task(title, description)
        display_add_success(task)
    except ValueError as e:
        print(f"Error: {e}")


def handle_view_tasks(tasklist: TaskList) -> None:
    """Handle viewing all tasks."""
    tasks = tasklist.list_tasks()
    if not tasks:
        display_empty_list()
    else:
        display_task_list(tasks)
    pause_for_user()


def handle_delete_task(tasklist: TaskList) -> None:
    """Handle deleting a task."""
    task_id = get_task_id_prompt()
    task = tasklist.get_task(task_id)

    if task is None:
        display_task_not_found(task_id)
        return

    if confirm_action(f'Are you sure you want to delete "{task.title}"?'):
        success = tasklist.delete_task(task_id)
        if success:
            display_delete_success(task.title)


def handle_mark_complete(tasklist: TaskList) -> None:
    """Handle marking a task as complete."""
    task_id = get_task_id_for_mark_complete()
    task = tasklist.get_task(task_id)

    if task is None:
        display_task_not_found(task_id)
        return

    if task.completed:
        display_already_complete(task)
        return

    updated = tasklist.mark_complete(task_id)
    display_toggle_complete(updated, True)


def handle_update_task(tasklist: TaskList) -> None:
    """Handle updating a task."""
    print("\n=== Update Task ===\n")

    task_id = get_task_id_for_update()
    task = tasklist.get_task(task_id)

    if task is None:
        display_task_not_found(task_id)
        return

    print(f'Task found: "{task.title}"')
    print()

    new_title, new_description = get_update_prompts()

    if new_title is None and new_description is None:
        print("No changes made.")
        return

    try:
        updated = tasklist.update_task(
            task_id,
            title=new_title,
            description=new_description
        )
        if updated:
            display_update_success(updated)
    except ValueError as e:
        print(f"Error: {e}")


def main_menu(tasklist: TaskList) -> None:
    """Run the main menu loop."""
    while True:
        display_welcome()

        choice = get_menu_choice()

        if choice is None:
            handle_invalid_choice()
            continue

        if choice == 1:
            handle_add_task(tasklist)
        elif choice == 2:
            handle_view_tasks(tasklist)
        elif choice == 3:
            handle_update_task(tasklist)
        elif choice == 4:
            handle_delete_task(tasklist)
        elif choice == 5:
            handle_mark_complete(tasklist)
        elif choice == 6:
            display_goodbye()
            break
