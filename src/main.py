"""Main entry point for the todo application.

This module provides the main() function and main_loop() that
initialize and run the todo application.
"""

from src.models.task import TaskList
from src.cli.menu import main_menu


def main_loop() -> None:
    """Run the main application loop.

    Initializes a TaskList and starts the menu interface.
    Tasks persist in memory for the duration of the session.
    """
    tasklist = TaskList()
    main_menu(tasklist)


def main() -> None:
    """Entry point for the application."""
    main_loop()


if __name__ == "__main__":
    main()
