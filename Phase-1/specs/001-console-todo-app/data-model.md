# Data Model: Console Todo Application

**Date**: 2026-01-02
**Feature**: Console Todo Application
**Branch**: 001-console-todo-app

## Overview
This document defines the data model for the Phase I Console Todo Application, based on the functional requirements and entities specified in the feature specification.

## Core Entities

### 1. Todo Entity

**Description**: Represents a single task in the todo list with all required attributes as specified in the feature requirements.

**Attributes**:
- `id`: `int` - Unique identifier for the task (assigned sequentially)
- `title`: `str` - Required title of the task (non-empty string)
- `description`: `str` - Optional description of the task (can be empty)
- `completed`: `bool` - Boolean indicating completion status (default: False)

**Validation Rules**:
- `id` must be unique within the current session
- `title` must not be empty or None
- `completed` must be a boolean value
- `description` can be empty but not None

**State Transitions**:
- `completed = False` → `completed = True` (when marking as complete)
- `completed = True` → `completed = False` (when marking as incomplete)

**Example**:
```python
{
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, bread, eggs",
    "completed": False
}
```

### 2. TaskList Collection

**Description**: In-memory collection that stores all Todo entities during the application session.

**Structure**: Python list containing Todo objects/dictionaries

**Operations**:
- Add: Append a new Todo to the collection
- Get All: Retrieve all Todos in the collection
- Get by ID: Retrieve a specific Todo by its unique ID
- Update: Modify attributes of an existing Todo
- Delete: Remove a Todo from the collection
- Filter: Get completed/incomplete tasks

**Constraints**:
- Must maintain unique IDs across all items
- No persistence between application runs
- Maximum recommended size: 100 tasks (for optimal performance)

## Data Relationships

### 1. TaskList → Todo (One-to-Many)
- One TaskList contains multiple Todo items
- Each Todo belongs to exactly one TaskList during its lifetime
- When TaskList is cleared (application restart), all Todos are removed

## Data Validation

### 1. Input Validation
- Title validation: Must be non-empty string with length > 0
- ID validation: Must be unique integer within collection
- Boolean validation: Completion status must be True or False
- Type validation: All attributes must match expected types

### 2. Business Rule Validation
- Cannot update or delete a Todo that doesn't exist
- Cannot mark a non-existent task as complete/incomplete
- All operations must provide clear feedback for invalid requests

## Data Lifecycle

### 1. Todo Creation
1. User provides title and optional description
2. System assigns next available ID
3. System sets completion status to False (default)
4. Todo is added to TaskList collection

### 2. Todo Modification
1. User specifies Todo ID and new values
2. System validates ID exists
3. System updates specified attributes
4. Modified Todo remains in TaskList collection

### 3. Todo Deletion
1. User specifies Todo ID
2. System validates ID exists
3. System removes Todo from TaskList collection
4. ID may be reused in future (implementation dependent)

### 4. Session End
1. Application terminates
2. All data in TaskList collection is lost
3. No persistence to external storage

## Data Access Patterns

### 1. Read Operations
- Get all tasks: Returns complete TaskList for display
- Get single task: Returns specific Todo by ID
- Filter tasks: Returns subset based on completion status

### 2. Write Operations
- Create task: Adds new Todo to TaskList
- Update task: Modifies existing Todo attributes
- Delete task: Removes Todo from TaskList
- Toggle completion: Updates completion status of existing Todo

## Performance Considerations

### 1. Memory Usage
- Each Todo object uses minimal memory (typically < 100 bytes)
- For 100 tasks: ~10KB memory usage
- Linear search time for ID lookups (acceptable for small lists)

### 2. Operation Complexity
- Add: O(1) - append to list
- Get by ID: O(n) - linear search through list
- Update: O(n) - find by ID then update
- Delete: O(n) - find by ID then remove
- Get all: O(1) - return entire list

## Error Handling

### 1. Invalid ID Operations
- Attempting to access non-existent ID returns appropriate error message
- Operations gracefully handle missing IDs
- User receives clear feedback about invalid operations

### 2. Validation Failures
- Invalid input is rejected with clear error messages
- System state remains consistent after validation failures
- User is prompted to provide valid input