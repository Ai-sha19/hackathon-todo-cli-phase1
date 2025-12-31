# Tasks: Phase 1 - Console Todo App

**Input**: Design documents from `specs/phase1-console/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/
**Tests**: Tests not explicitly requested in spec - implementation-only

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project structure from plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create src/ directory structure with __init__.py files in src/, src/models/, src/services/, src/cli/
- [X] T002 Create tests/ directory structure with __init__.py in tests/, tests/unit/
- [X] T003 Create pyproject.toml with Python 3.13+ requirement, project name "hackathon-todo", and UV configuration
- [X] T004 [P] Create README.md with project description and quick start instructions

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 Create Task dataclass in src/models/task.py with id (int), title (str), description (str), completed (bool) fields
- [X] T006 [P] Create TaskList class in src/models/task.py with tasks list and next_id counter, __init__ method
- [X] T007 [P] [US1] Implement add_task(title, description) method in TaskList class in src/models/task.py (validates title, assigns unique ID)
- [X] T008 [US2] Implement list_tasks() method in TaskList class in src/models/task.py (returns all tasks)
- [X] T009 [US3] Implement delete_task(task_id) method in TaskList class in src/models/task.py (returns bool for success)
- [X] T010 [US4] Implement toggle_complete(task_id) method in TaskList class in src/models/task.py (toggles completed status)
- [X] T011 [US5] Implement update_task(task_id, title, description) method in TaskList class in src/models/task.py (updates only provided fields)
- [X] T012 [P] [US2] Implement get_task(task_id) method in TaskList class in src/models/task.py (returns Task or None)

**Checkpoint**: Foundation ready - Task model and TaskList class complete. User story implementation can now begin in parallel.

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Users can add new tasks with a title (required) and optional description

**Independent Test**: Run the app, select "Add Task", enter task details, verify task appears in list with correct data

### Implementation for User Story 1

- [X] T013 [US1] Create input validation module src/cli/input.py with validate_title(title) function (1-200 chars, not empty)
- [X] T014 [US1] Create src/cli/input.py with validate_description(description) function (0-1000 chars)
- [X] T015 [US1] Implement add_task_prompt() function in src/cli/input.py (prompts for title and description)
- [X] T016 [US1] Implement display_add_success(task) function in src/cli/output.py (shows task added message)
- [X] T017 [US1] Implement handle_add_task(tasklist) function in src/cli/menu.py (coordinates input, validation, add_task, display)
- [X] T018 [US1] Add "1. Add Task" menu option and handle_add_task call in main_menu() function in src/cli/menu.py

**Checkpoint**: User Story 1 complete. App can add tasks and display them. MVP ready for demo.

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Users can view all tasks with their ID, title, completion status, and description

**Independent Test**: Add multiple tasks (some complete), view list, verify all tasks display correctly with visual distinction between complete/incomplete

### Implementation for User Story 2

- [X] T019 [US2] Implement format_task_display(task) function in src/cli/output.py (formats single task for display)
- [X] T020 [US2] Implement display_task_list(tasks) function in src/cli/output.py (displays all tasks with table header, counts)
- [X] T021 [US2] Implement display_empty_list() function in src/cli/output.py (shows "no tasks" message)
- [X] T022 [US2] Implement handle_view_tasks(tasklist) function in src/cli/menu.py (calls list_tasks, routes to display functions)
- [X] T023 [US2] Add "2. View Tasks" menu option and handle_view_tasks call in main_menu() function in src/cli/menu.py

**Checkpoint**: User Story 2 complete. App can view all tasks with proper formatting.

---

## Phase 5: User Story 3 - Delete Task (Priority: P1)

**Goal**: Users can delete a task by ID with confirmation and error handling

**Independent Test**: Add tasks, delete one, verify it no longer appears in the list

### Implementation for User Story 3

- [X] T024 [US3] Implement get_task_id_prompt() function in src/cli/input.py (prompts for task ID with validation)
- [X] T025 [US3] Implement display_delete_success(task_title) function in src/cli/output.py (shows task deleted message)
- [X] T026 [US3] Implement display_task_not_found(task_id) function in src/cli/output.py (shows error for invalid ID)
- [X] T027 [US3] Implement handle_delete_task(tasklist) function in src/cli/menu.py (gets ID, calls delete_task, displays result)
- [X] T028 [US3] Add "4. Delete Task" menu option and handle_delete_task call in main_menu() function in src/cli/menu.py

**Checkpoint**: User Story 3 complete. App can delete tasks with proper error handling.

---

## Phase 6: User Story 4 - Mark Task as Complete (Priority: P1)

**Goal**: Users can toggle task completion status (complete/incomplete)

**Independent Test**: Add tasks, mark one as complete, verify status changes while others remain unchanged

### Implementation for User Story 4

- [X] T029 [US4] Implement display_toggle_complete(task, is_now_complete) function in src/cli/output.py (shows completion status change)
- [X] T030 [US4] Implement handle_mark_complete(tasklist) function in src/cli/menu.py (gets ID, calls toggle_complete, displays result)
- [X] T031 [US4] Add "5. Mark Complete" menu option and handle_mark_complete call in main_menu() function in src/cli/menu.py

**Checkpoint**: User Story 4 complete. App can toggle task completion status.

---

## Phase 7: User Story 5 - Update Task (Priority: P2)

**Goal**: Users can update task title and/or description while preserving unchanged fields

**Independent Test**: Add tasks, update one, verify only that task's details changed

### Implementation for User Story 5

- [X] T032 [US5] Implement get_update_prompts() function in src/cli/input.py (prompts for new title/description with Enter to keep)
- [X] T033 [US5] Implement display_update_success(task) function in src/cli/output.py (shows task updated message)
- [X] T034 [US5] Implement handle_update_task(tasklist) function in src/cli/menu.py (gets ID, prompts for updates, calls update_task)
- [X] T035 [US5] Add "3. Update Task" menu option and handle_update_task call in main_menu() function in src/cli/menu.py

**Checkpoint**: User Story 5 complete. App can update task details.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Integration, main loop, and overall application quality

- [X] T036 Implement main_loop() function in src/main.py (initializes TaskList, runs menu loop)
- [X] T037 [P] Implement display_welcome() function in src/cli/output.py (shows welcome message)
- [X] T038 [P] Implement display_goodbye() function in src/cli/output.py (shows exit message)
- [X] T039 [P] Implement handle_invalid_choice() function in src/cli/output.py (shows error for invalid menu input)
- [X] T040 Implement main() function in src/main.py with if __name__ == "__main__": guard
- [X] T041 [P] Add type hints to all functions in src/models/task.py (per PEP 8 and plan.md)
- [X] T042 [P] Add docstrings to all public functions in src/models/task.py
- [X] T043 [P] Add docstrings to all functions in src/cli/input.py
- [X] T044 [P] Add docstrings to all functions in src/cli/output.py
- [X] T045 [P] Add docstrings to all functions in src/cli/menu.py
- [X] T046 [P] Add docstrings to all functions in src/main.py

---

## Dependencies & Execution Order

### Phase Dependencies

| Phase | Depends On | Blocks |
|-------|------------|--------|
| Setup (1) | None | Foundational |
| Foundational (2) | Setup | All User Stories |
| User Story 1 (3) | Foundational | Polish |
| User Story 2 (4) | Foundational | Polish |
| User Story 3 (5) | Foundational | Polish |
| User Story 4 (6) | Foundational | Polish |
| User Story 5 (7) | Foundational | Polish |
| Polish (8) | All User Stories | Complete |

### User Story Dependencies

| User Story | Can Start After | Dependencies |
|------------|-----------------|--------------|
| US1 (Add) | Phase 2 | Task/TaskList (no other story) |
| US2 (View) | Phase 2 | Task/TaskList (no other story) |
| US3 (Delete) | Phase 2 | Task/TaskList (no other story) |
| US4 (Mark Complete) | Phase 2 | Task/TaskList (no other story) |
| US5 (Update) | Phase 2 | Task/TaskList (no other story) |

**Note**: All user stories can proceed in parallel after Phase 2 is complete since they all depend only on the foundational Task/TaskList classes.

### Within Each User Story

- Models (Task, TaskList) complete in Phase 2
- Input/Output helpers complete within story phase
- Handler function integrates all components
- Story complete before moving to Polish

### Parallel Opportunities

- All Setup tasks (T001-T004) can run in parallel
- All Foundational tasks marked [P] (T006, T007, T012) can run in parallel
- All User Stories (US1-US5) can start in parallel after Phase 2
- All Polish tasks marked [P] (T037-T039, T041-T045) can run in parallel

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T004)
2. Complete Phase 2: Foundational (T005-T012)
3. Complete Phase 3: User Story 1 (T013-T018)
4. **STOP and VALIDATE**: Test add task functionality
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Demo (MVP!)
3. Add User Story 2 → Test independently → Demo
4. Add User Story 3 → Test independently → Demo
5. Add User Story 4 → Test independently → Demo
6. Add User Story 5 → Test independently → Demo
7. Polish → Final delivery
8. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together (T001-T012)
2. Once Foundational is done:
   - Developer A: User Story 1 (T013-T018)
   - Developer B: User Story 2 (T019-T023)
   - Developer C: User Story 3 (T024-T028)
3. Once US1-US3 are complete:
   - Developer A: User Story 4 (T029-T031)
   - Developer B: User Story 5 (T032-T035)
4. Polish (T036-T046) can be split or done together

---

## Task Summary

| Phase | Tasks | Description |
|-------|-------|-------------|
| Phase 1: Setup | T001-T004 | Project structure, pyproject.toml |
| Phase 2: Foundational | T005-T012 | Task dataclass, TaskList methods |
| Phase 3: US1 Add | T013-T018 | Add task CLI flow |
| Phase 4: US2 View | T019-T023 | View tasks CLI flow |
| Phase 5: US3 Delete | T024-T028 | Delete task CLI flow |
| Phase 6: US4 Mark Complete | T029-T031 | Toggle completion CLI flow |
| Phase 7: US5 Update | T032-T035 | Update task CLI flow |
| Phase 8: Polish | T036-T046 | Main loop, docs, type hints |

**Total Tasks**: 46

| Metric | Value |
|--------|-------|
| Total Tasks | 46 |
| Parallelizable [P] | 16 |
| User Story Tasks | 23 (US1: 6, US2: 5, US3: 5, US4: 3, US5: 4) |
| MVP Scope (US1) | 18 tasks (Phases 1-3) |

---

## Notes

- [P] tasks = different files, no dependencies on incomplete tasks
- [Story] label maps task to specific user story for traceability
- Each user story is independently completable and testable
- Story complete before moving to next priority
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
