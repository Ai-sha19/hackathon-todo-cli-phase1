# Feature Specification: Phase 1 - In-Memory Console Todo App

**Feature Branch**: `1-phase1-console`
**Created**: 2025-12-31
**Status**: Draft
**Input**: User description: "Phase 1: In-Memory Python Console App. Implement 5 Basic Features: Add, Delete, Update, View, and Mark Complete. Tech Stack: Python 3.13 and UV. Use full_project_code.txt as reference for data models, task management logic, and CLI flow."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add New Task (Priority: P1)

As a user, I can add a new task to my todo list so that I can track things I need to do.

**Why this priority**: This is the foundational feature - without adding tasks, the todo list serves no purpose. Every other feature depends on having tasks in the list.

**Independent Test**: Can be fully tested by running the app, selecting "Add Task", entering task details, and verifying the task appears in the list with correct data.

**Acceptance Scenarios**:

1. **Given** the todo list is empty, **When** the user adds a task with title "Buy groceries", **Then** the task list contains exactly one task with title "Buy groceries", completed status is false, and a unique ID is assigned.

2. **Given** the todo list has existing tasks, **When** the user adds a task, **Then** the new task appears in the list with a unique ID and all existing tasks remain unchanged.

3. **Given** the user is adding a task, **When** the user provides only a title, **Then** the task is created with the given title and an empty description.

4. **Given** the user is adding a task, **When** the user provides both title and description, **Then** the task is created with both fields populated.

---

### User Story 2 - View All Tasks (Priority: P1)

As a user, I can view all my tasks so that I can see what I need to do and track my progress.

**Why this priority**: Users need visibility into their task list to make informed decisions about what to do next. This is essential for any todo app.

**Independent Test**: Can be fully tested by adding multiple tasks (some complete, some not), viewing the list, and verifying all tasks display with correct information.

**Acceptance Scenarios**:

1. **Given** the todo list is empty, **When** the user views the task list, **Then** the system displays a message indicating no tasks exist.

2. **Given** the todo list has tasks, **When** the user views the task list, **Then** all tasks are displayed with their ID, title, completion status, and description (if present).

3. **Given** the todo list has both completed and incomplete tasks, **When** the user views the task list, **Then** completed tasks are visually distinguished from incomplete tasks.

---

### User Story 3 - Delete Task (Priority: P1)

As a user, I can delete a task from my todo list so that I can remove tasks I no longer need to track.

**Why this priority**: Task cleanup is essential for maintaining a relevant todo list. Users need to remove completed or obsolete tasks.

**Independent Test**: Can be fully tested by adding tasks, deleting one, and verifying it no longer appears in the list.

**Acceptance Scenarios**:

1. **Given** a task with ID 1 exists, **When** the user deletes task ID 1, **Then** task ID 1 no longer appears in the task list.

2. **Given** multiple tasks exist, **When** the user deletes one task, **Then** all other tasks remain unchanged with their original IDs.

3. **Given** the user attempts to delete a non-existent task ID, **When** the system handles the error gracefully, **Then** the user receives a clear error message and no tasks are deleted.

---

### User Story 4 - Mark Task as Complete (Priority: P1)

As a user, I can mark a task as complete so that I can track my progress on completed items.

**Why this priority**: This provides the core todo list functionality of distinguishing between what's done and what's pending.

**Independent Test**: Can be fully tested by adding tasks, marking one as complete, and verifying its status changes while others remain unchanged.

**Acceptance Scenarios**:

1. **Given** a task with ID 1 exists and is incomplete, **When** the user marks task ID 1 as complete, **Then** task ID 1's status changes to completed.

2. **Given** a task with ID 1 exists and is complete, **When** the user marks task ID 1 as complete (toggle behavior), **Then** task ID 1's status changes to incomplete.

3. **Given** the user attempts to mark a non-existent task ID as complete, **When** the system handles the error gracefully, **Then** the user receives a clear error message.

---

### User Story 5 - Update Task (Priority: P2)

As a user, I can update a task's details so that I can correct or modify task information.

**Why this priority**: Users often need to refine task details after creation - correcting typos, adding more detail, or changing the task description.

**Independent Test**: Can be fully tested by adding tasks, updating one, and verifying only that task's details changed while others remain unchanged.

**Acceptance Scenarios**:

1. **Given** a task with ID 1 exists with title "Buy milk", **When** the user updates task ID 1 with new title "Buy almond milk", **Then** task ID 1 now has title "Buy almond milk" and other fields remain unchanged.

2. **Given** a task with ID 1 exists, **When** the user updates the task's description, **Then** only the description changes and title remains the same.

3. **Given** the user attempts to update a non-existent task ID, **When** the system handles the error gracefully, **Then** the user receives a clear error message and no tasks are modified.

---

### Edge Cases

- **Empty input for task title**: When user provides an empty or whitespace-only title, the system MUST reject it and prompt for a valid title.
- **Task not found**: When user references a non-existent task ID for any operation (delete, update, mark complete), the system MUST display a clear error message identifying the task was not found.
- **Duplicate task IDs**: The system MUST ensure each task receives a unique ID that is never reused during the session.
- **Session termination**: Tasks persist in memory for the duration of the session but are lost when the application exits.
- **Special characters in input**: The system MUST handle special characters in task titles and descriptions without breaking the CLI display.
- **Long input strings**: The system MUST handle task titles up to at least 200 characters and descriptions up to at least 1000 characters.
- **Concurrent operations**: Since this is a single-user console app, no concurrent access concerns exist.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to create new tasks with a title (required) and optional description.
- **FR-002**: System MUST assign a unique integer ID to each task upon creation, starting from 1.
- **FR-003**: System MUST store all tasks in memory for the duration of the session.
- **FR-004**: System MUST display all tasks with their ID, title, description (if present), and completion status.
- **FR-005**: System MUST allow users to delete a task by its ID.
- **FR-006**: System MUST allow users to toggle the completion status of a task by its ID.
- **FR-007**: System MUST allow users to update the title and/or description of a task by its ID.
- **FR-008**: System MUST validate that task titles are non-empty after stripping whitespace.
- **FR-009**: System MUST provide clear error messages when users attempt operations on non-existent task IDs.
- **FR-010**: System MUST provide a command-line interface with clear menu options for each operation.
- **FR-011**: System MUST exit cleanly when the user selects the quit option.

### Key Entities *(include if feature involves data)*

- **Task**: Represents a todo item
  - `id`: Integer (unique identifier, auto-incremented)
  - `title`: String (required, 1-200 characters)
  - `description`: String (optional, 0-1000 characters)
  - `completed`: Boolean (default false)

- **TaskList**: In-memory collection that manages tasks
  - `tasks`: List of Task objects
  - `next_id`: Integer counter for generating unique task IDs
  - Provides methods: add(), get(), list(), delete(), update(), toggle_complete()

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can add a task and see it appear in the task list within 5 seconds of command entry.
- **SC-002**: Users can perform all five core operations (add, view, delete, update, mark complete) without encountering unhandled exceptions.
- **SC-003**: Task IDs remain stable and unique throughout the session - no two tasks ever share the same ID.
- **SC-004**: Error messages are displayed within 1 second of invalid input and clearly identify the problem.
- **SC-005**: Users can complete the full add→view→update→mark complete→delete workflow in under 2 minutes during testing.
- **SC-006**: The application handles at least 100 tasks in memory without performance degradation.
