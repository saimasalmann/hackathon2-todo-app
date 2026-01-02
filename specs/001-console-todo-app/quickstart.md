# Quickstart Guide: Console Todo Application

**Date**: 2026-01-02
**Feature**: Console Todo Application
**Branch**: 001-console-todo-app

## Overview
This quickstart guide provides step-by-step instructions to set up, run, and use the Phase I Console Todo Application. The application is a simple command-line interface for managing todo tasks with in-memory storage.

## Prerequisites
- Python 3.13 or higher
- `uv` package manager installed
- Basic command-line knowledge

## Setup Instructions

### 1. Clone or Navigate to Project Directory
```bash
cd /path/to/todo-app
```

### 2. Verify Python Version
```bash
python --version
# Should show Python 3.13.x or higher
```

### 3. Install Dependencies (if any)
```bash
# For Phase I, no external dependencies are used
# All functionality uses standard Python libraries only
```

### 4. Run the Application
```bash
python main.py
```

## Using the Application

### 1. Main Menu
After running the application, you'll see a menu with the following options:
```
TODO APPLICATION
================
1. Add task
2. View tasks
3. Update task
4. Delete task
5. Mark task as complete/incomplete
6. Exit
Choose an option (1-6):
```

### 2. Adding a Task
1. Select option `1`
2. Enter the task title when prompted
3. Optionally enter a description (press Enter to skip)
4. The task will be added with a unique ID and "incomplete" status

### 3. Viewing Tasks
1. Select option `2`
2. All tasks will be displayed with:
   - Task ID
   - Title
   - Description (if present)
   - Completion status (✔ for complete, ✘ for incomplete)

### 4. Updating a Task
1. Select option `3`
2. Enter the task ID you want to update
3. Enter the new title (or press Enter to keep current)
4. Enter the new description (or press Enter to keep current)

### 5. Deleting a Task
1. Select option `4`
2. Enter the task ID you want to delete
3. The task will be permanently removed

### 6. Marking Task Complete/Incomplete
1. Select option `5`
2. Enter the task ID you want to toggle
3. The completion status will switch (complete ↔ incomplete)

### 7. Exiting the Application
1. Select option `6`
2. The application will terminate
3. All data will be lost (in-memory storage only)

## Example Usage Session

```
TODO APPLICATION
================
1. Add task
2. View tasks
3. Update task
4. Delete task
5. Mark task as complete/incomplete
6. Exit
Choose an option (1-6): 1
Enter task title: Buy groceries
Enter task description (optional): Milk, bread, eggs
Task added successfully with ID 1!

TODO APPLICATION
================
1. Add task
2. View tasks
3. Update task
4. Delete task
5. Mark task as complete/incomplete
6. Exit
Choose an option (1-6): 2
All Tasks:
ID: 1 | Title: Buy groceries | Description: Milk, bread, eggs | Status: ✘ Incomplete

TODO APPLICATION
================
1. Add task
2. View tasks
3. Update task
4. Delete task
5. Mark task as complete/incomplete
6. Exit
Choose an option (1-6): 5
Enter task ID to toggle: 1
Task 1 marked as complete!

TODO APPLICATION
================
1. Add task
2. View tasks
3. Update task
4. Delete task
5. Mark task as complete/incomplete
6. Exit
Choose an option (1-6): 2
All Tasks:
ID: 1 | Title: Buy groceries | Description: Milk, bread, eggs | Status: ✔ Complete

TODO APPLICATION
================
1. Add task
2. View tasks
3. Update task
4. Delete task
5. Mark task as complete/incomplete
6. Exit
Choose an option (1-6): 6
Goodbye!
```

## Troubleshooting

### Common Issues

1. **Python version too old**
   - Error: "SyntaxError" or "Invalid syntax"
   - Solution: Install Python 3.13 or higher

2. **File not found**
   - Error: "No such file or directory: main.py"
   - Solution: Ensure you're in the correct project directory

3. **Invalid task ID**
   - Error: "Task not found" or "Invalid ID"
   - Solution: Check the ID exists by viewing tasks first

4. **Application crashes**
   - Error: Unexpected exit
   - Solution: The application should handle errors gracefully; if not, report the issue

## Tips and Best Practices

1. **Task Management**
   - Keep task titles concise but descriptive
   - Use descriptions for additional details
   - Regularly mark completed tasks to keep the list manageable

2. **Data Persistence**
   - Remember that data is stored only in memory
   - Plan your work session accordingly
   - Data will be lost when the application exits

3. **Error Handling**
   - The application provides clear error messages
   - Follow the prompts to correct any mistakes
   - Invalid inputs will not crash the application

## Next Steps
- Successfully complete all basic Todo operations (add, view, update, delete, complete)
- Verify the application runs without errors during normal usage
- Test edge cases like invalid IDs and empty inputs
- Prepare for Phase II which will introduce persistent storage