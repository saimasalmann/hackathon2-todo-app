# CLI Interface Contract: Console Todo Application

**Date**: 2026-01-02
**Feature**: Console Todo Application
**Branch**: 001-console-todo-app

## Overview
This document defines the contract for the Command Line Interface (CLI) of the Phase I Console Todo Application. It specifies the user interaction patterns, input/output formats, and behavior expectations.

## Interface Definition

### Main Menu Interface

**Input**: User selects option (1-6) via numeric input
**Output**: Application performs requested operation and returns to main menu
**Error Handling**: Invalid input shows error message and returns to menu

**Menu Options**:
1. `1` - Add task
2. `2` - View tasks
3. `3` - Update task
4. `4` - Delete task
5. `5` - Mark task as complete/incomplete
6. `6` - Exit

### Operation Contracts

#### 1. Add Task (`1`)
**Input Flow**:
- Prompt: "Enter task title:"
- User provides non-empty string
- Prompt: "Enter task description (optional):"
- User provides string or empty input

**Output**:
- Success: "Task added successfully with ID [ID]!"
- Error: Appropriate error message

**Data Format**:
- ID: Auto-assigned integer
- Title: Required string (non-empty)
- Description: Optional string
- Status: Default "incomplete" (False)

#### 2. View Tasks (`2`)
**Input**: None required
**Output**:
- If tasks exist: List all tasks in format "ID: [ID] | Title: [title] | Description: [desc] | Status: [✔/✘] [Status]"
- If no tasks: "No tasks found."

**Display Format**:
```
All Tasks:
ID: 1 | Title: Task Title | Description: Task description | Status: ✘ Incomplete
ID: 2 | Title: Another Task | Description: | Status: ✔ Complete
```

#### 3. Update Task (`3`)
**Input Flow**:
- Prompt: "Enter task ID to update:"
- User provides valid task ID
- Prompt: "Enter new title (current: '[current]'):", user provides new title or empty to keep current
- Prompt: "Enter new description (current: '[current]'):", user provides new description or empty to keep current

**Output**:
- Success: "Task [ID] updated successfully!"
- Error: "Task not found." or appropriate error message

#### 4. Delete Task (`4`)
**Input Flow**:
- Prompt: "Enter task ID to delete:"
- User provides valid task ID

**Output**:
- Success: "Task [ID] deleted successfully!"
- Error: "Task not found." or appropriate error message

#### 5. Mark Task Complete/Incomplete (`5`)
**Input Flow**:
- Prompt: "Enter task ID to toggle:"
- User provides valid task ID

**Output**:
- Success: "Task [ID] marked as [complete/incomplete]!"
- Error: "Task not found." or appropriate error message

#### 6. Exit (`6`)
**Input**: None required
**Output**: "Goodbye!" message and application termination

## Input Validation

### Input Types
- **Integer**: Menu selection, task IDs (positive integers only)
- **String**: Task titles, descriptions (non-empty for titles)

### Validation Rules
1. **Menu Selection**: Must be integer 1-6
2. **Task ID**: Must be positive integer that exists in current task list
3. **Task Title**: Must be non-empty string
4. **Task Description**: Can be empty string

### Error Messages
- Invalid menu selection: "Invalid option. Please choose 1-6."
- Invalid task ID: "Task not found."
- Empty title: "Title cannot be empty."
- Non-numeric input where number expected: "Please enter a valid number."

## State Management

### In-Memory Storage
- All tasks stored in Python list/dict during session
- No persistence between application runs
- Tasks exist only in current session

### Task Lifecycle
1. **Create**: Task added to in-memory collection with unique ID
2. **Read**: Task retrieved from collection for display
3. **Update**: Task modified in collection
4. **Delete**: Task removed from collection
5. **Complete/Incomplete**: Task status toggled in collection

## Error Handling Contract

### Error Types
1. **User Input Error**: Invalid data provided by user
2. **Business Logic Error**: Invalid operation (e.g., updating non-existent task)
3. **System Error**: Unexpected application error

### Error Response Pattern
1. Display clear, human-readable error message
2. Return to appropriate menu or prompt
3. Do not crash the application
4. Maintain data integrity

## Success Metrics

### User Experience
- All operations complete in under 1 second
- Clear feedback for all user actions
- Consistent interface behavior
- Intuitive menu navigation

### Reliability
- Application never crashes on valid or invalid input
- Data remains consistent during all operations
- All error conditions handled gracefully

## Constraints

### Performance
- Response time: < 1 second for all operations
- Memory usage: Minimal (in-memory storage)

### Compatibility
- Cross-platform: Works on Windows, macOS, Linux
- Python version: 3.13+
- Terminal: Standard console/terminal support

### Security
- No external data access
- No network communication
- Input sanitization for local operations only