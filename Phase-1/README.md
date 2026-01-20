# Console Todo Application

A simple command-line Todo application with in-memory storage, built as Phase I of the Todo Project evolution.

## Features

- Add new tasks with titles and optional descriptions
- View all tasks with their completion status
- Update existing tasks
- Mark tasks as complete/incomplete
- Delete tasks
- In-memory storage (data is lost when application exits)

## Requirements

- Python 3.13 or higher

## Installation

1. Clone the repository
2. Ensure you have Python 3.13+ installed
3. No additional dependencies required

## Usage

Run the application:

```bash
python main.py
```

Follow the menu prompts to interact with the application:

1. Add task - Create a new todo item
2. View tasks - Display all existing tasks
3. Update task - Modify an existing task
4. Delete task - Remove a task from the list
5. Mark task as complete/incomplete - Toggle completion status
6. Exit - Quit the application

## Architecture

- Single-file application in `main.py`
- `Todo` class represents individual tasks
- `TodoApp` class manages the collection of tasks
- CLI interface for user interaction
- In-memory storage only (no persistence)

## Design Principles

- Educational clarity and simplicity
- Clean separation of concerns
- Proper error handling
- User-friendly interface

## Phase I Constraints

- No external dependencies (uses only standard Python libraries)
- In-memory storage only
- CLI interface only
- No persistence between runs