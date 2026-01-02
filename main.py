#!/usr/bin/env python3
"""
Console Todo Application
A simple command-line Todo application with in-memory storage.
"""

import json
from typing import List, Dict, Optional


class Todo:
    """
    Represents a single todo task with id, title, description, and completion status.
    """

    def __init__(self, id: int, title: str, description: str = "", completed: bool = False):
        """
        Initialize a Todo object.

        Args:
            id (int): Unique identifier for the task
            title (str): Title of the task (required)
            description (str): Optional description of the task
            completed (bool): Completion status (default: False)
        """
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self) -> Dict:
        """
        Convert the Todo object to a dictionary representation.

        Returns:
            Dict: Dictionary representation of the Todo object
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

    def __str__(self) -> str:
        """
        String representation of the Todo object for display.

        Returns:
            str: Formatted string representation
        """
        status = "✔" if self.completed else "✘"
        description_str = f" | Description: {self.description}" if self.description else ""
        return f"ID: {self.id} | Title: {self.title}{description_str} | Status: {status} {'Complete' if self.completed else 'Incomplete'}"


class TodoApp:
    """
    Todo application class that manages the collection of Todo items.
    """

    def __init__(self):
        """
        Initialize the TodoApp with an empty list of tasks.
        """
        self.todos: List[Todo] = []
        self.next_id = 1

    def add_task(self, title: str, description: str = "") -> Todo:
        """
        Add a new task to the todo list.

        Args:
            title (str): Title of the task (required)
            description (str): Optional description of the task

        Returns:
            Todo: The newly created Todo object
        """
        if not title.strip():
            raise ValueError("Title cannot be empty")

        todo = Todo(id=self.next_id, title=title.strip(), description=description.strip())
        self.todos.append(todo)
        self.next_id += 1
        return todo

    def get_all_tasks(self) -> List[Todo]:
        """
        Get all tasks in the todo list.

        Returns:
            List[Todo]: List of all Todo objects
        """
        return self.todos

    def get_task_by_id(self, task_id: int) -> Optional[Todo]:
        """
        Get a specific task by its ID.

        Args:
            task_id (int): ID of the task to retrieve

        Returns:
            Optional[Todo]: The Todo object if found, None otherwise
        """
        for todo in self.todos:
            if todo.id == task_id:
                return todo
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update an existing task's title and/or description.

        Args:
            task_id (int): ID of the task to update
            title (Optional[str]): New title (if provided)
            description (Optional[str]): New description (if provided)

        Returns:
            bool: True if task was updated, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            if title is not None:
                task.title = title.strip() if title.strip() else task.title
            if description is not None:
                task.description = description.strip()
            return True
        return False

    def toggle_completion(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task.

        Args:
            task_id (int): ID of the task to toggle

        Returns:
            bool: True if task status was toggled, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = not task.completed
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task from the todo list.

        Args:
            task_id (int): ID of the task to delete

        Returns:
            bool: True if task was deleted, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            self.todos.remove(task)
            return True
        return False


def get_user_input(prompt: str) -> str:
    """
    Get input from the user with a prompt.

    Args:
        prompt (str): Prompt to display to the user

    Returns:
        str: User input string
    """
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
        exit(0)


def display_menu():
    """
    Display the main menu options to the user.
    """
    print("\nTODO APPLICATION")
    print("================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Mark task as complete/incomplete")
    print("6. Exit")


def handle_add_task(app: TodoApp):
    """
    Handle the add task functionality.

    Args:
        app (TodoApp): The Todo application instance
    """
    print("\n--- Add Task ---")
    title = get_user_input("Enter task title: ")

    if not title:
        print("Error: Title cannot be empty.")
        return

    description = get_user_input("Enter task description (optional): ")

    try:
        new_task = app.add_task(title, description)
        print(f"Task added successfully with ID {new_task.id}!")
    except ValueError as e:
        print(f"Error: {e}")


def handle_view_tasks(app: TodoApp):
    """
    Handle the view tasks functionality.

    Args:
        app (TodoApp): The Todo application instance
    """
    print("\n--- All Tasks ---")
    tasks = app.get_all_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(task)


def handle_update_task(app: TodoApp):
    """
    Handle the update task functionality.

    Args:
        app (TodoApp): The Todo application instance
    """
    print("\n--- Update Task ---")

    try:
        task_id_input = get_user_input("Enter task ID to update: ")
        if not task_id_input:
            print("Error: Task ID cannot be empty.")
            return

        task_id = int(task_id_input)
    except ValueError:
        print("Error: Please enter a valid number for task ID.")
        return

    task = app.get_task_by_id(task_id)
    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return

    current_title = task.title
    current_description = task.description

    new_title = get_user_input(f"Enter new title (current: '{current_title}'): ")
    new_description = get_user_input(f"Enter new description (current: '{current_description}'): ")

    # Use current values if user doesn't provide new ones
    title_to_update = new_title if new_title else None
    description_to_update = new_description if new_description else None

    if app.update_task(task_id, title_to_update, description_to_update):
        print(f"Task {task_id} updated successfully!")
    else:
        print(f"Error: Failed to update task {task_id}.")


def handle_delete_task(app: TodoApp):
    """
    Handle the delete task functionality.

    Args:
        app (TodoApp): The Todo application instance
    """
    print("\n--- Delete Task ---")

    try:
        task_id_input = get_user_input("Enter task ID to delete: ")
        if not task_id_input:
            print("Error: Task ID cannot be empty.")
            return

        task_id = int(task_id_input)
    except ValueError:
        print("Error: Please enter a valid number for task ID.")
        return

    if app.delete_task(task_id):
        print(f"Task {task_id} deleted successfully!")
    else:
        print(f"Error: Task with ID {task_id} not found.")


def handle_toggle_completion(app: TodoApp):
    """
    Handle the toggle completion functionality.

    Args:
        app (TodoApp): The Todo application instance
    """
    print("\n--- Toggle Task Completion ---")

    try:
        task_id_input = get_user_input("Enter task ID to toggle: ")
        if not task_id_input:
            print("Error: Task ID cannot be empty.")
            return

        task_id = int(task_id_input)
    except ValueError:
        print("Error: Please enter a valid number for task ID.")
        return

    task = app.get_task_by_id(task_id)
    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return

    if app.toggle_completion(task_id):
        status = "complete" if task.completed else "incomplete"
        print(f"Task {task_id} marked as {status}!")
    else:
        print(f"Error: Failed to toggle completion for task {task_id}.")


def main():
    """
    Main function to run the Todo application.
    """
    app = TodoApp()

    print("Welcome to the Todo Application!")

    while True:
        display_menu()

        choice = get_user_input("Choose an option (1-6): ")

        if choice == "1":
            handle_add_task(app)
        elif choice == "2":
            handle_view_tasks(app)
        elif choice == "3":
            handle_update_task(app)
        elif choice == "4":
            handle_delete_task(app)
        elif choice == "5":
            handle_toggle_completion(app)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()
