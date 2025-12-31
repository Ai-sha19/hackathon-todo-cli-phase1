"""Task model and TaskList for the todo application.

This module defines the Task dataclass and TaskList class that manage
tasks in memory for the duration of the session.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """Represents a single todo item.

    Attributes:
        id: Unique identifier for the task (auto-assigned).
        title: Short task description (required, 1-200 chars).
        description: Detailed task information (optional, 0-1000 chars).
        completed: Completion status (default False).
    """

    id: int
    title: str
    description: str = ""
    completed: bool = False


class TaskList:
    """Manages a collection of tasks in memory.

    Provides methods for CRUD operations on tasks.
    All tasks persist for the duration of the session.
    """

    def __init__(self) -> None:
        """Initialize an empty task list with ID counter."""
        self.tasks: list[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """Create and add a new task.

        Args:
            title: Task title (required, 1-200 chars).
            description: Optional task description.

        Returns:
            The created Task with assigned ID.

        Raises:
            ValueError: If title is empty or too long.
        """
        # Validate title
        title = title.strip()
        if not title:
            raise ValueError("Task title cannot be empty.")
        if len(title) > 200:
            raise ValueError("Task title must be 200 characters or less.")

        # Validate description length
        if len(description) > 1000:
            description = description[:1000]

        # Create and add task
        task = Task(
            id=self.next_id,
            title=title,
            description=description,
            completed=False
        )
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """Retrieve a task by ID.

        Args:
            task_id: The unique task identifier.

        Returns:
            The Task if found, None otherwise.
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def list_tasks(self) -> list[Task]:
        """Return all tasks.

        Returns:
            List of all tasks in creation order.
        """
        return list(self.tasks)

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID.

        Args:
            task_id: The unique task identifier.

        Returns:
            True if task was found and deleted, False otherwise.
        """
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True
        return False

    def update_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None
    ) -> Optional[Task]:
        """Update a task's title and/or description.

        Args:
            task_id: The unique task identifier.
            title: New title (if provided, updates title).
            description: New description (if provided, updates description).

        Returns:
            The updated Task if found, None otherwise.
        """
        task = self.get_task(task_id)
        if task is None:
            return None

        # Update title if provided
        if title is not None:
            title = title.strip()
            if not title:
                raise ValueError("Task title cannot be empty.")
            if len(title) > 200:
                raise ValueError("Task title must be 200 characters or less.")
            task.title = title

        # Update description if provided
        if description is not None:
            if len(description) > 1000:
                description = description[:1000]
            task.description = description

        return task

    def toggle_complete(self, task_id: int) -> Optional[Task]:
        """Toggle a task's completion status.

        Args:
            task_id: The unique task identifier.

        Returns:
            The updated Task if found, None otherwise.
        """
        task = self.get_task(task_id)
        if task is None:
            return None
        task.completed = not task.completed
        return task

    def mark_complete(self, task_id: int) -> Optional[Task]:
        """Mark a task as complete only if it's currently pending.

        Args:
            task_id: The unique task identifier.

        Returns:
            The updated Task if found and was pending, None otherwise.
        """
        task = self.get_task(task_id)
        if task is None:
            return None
        if task.completed:
            return task  # Return task as-is without changing status
        task.completed = True
        return task
