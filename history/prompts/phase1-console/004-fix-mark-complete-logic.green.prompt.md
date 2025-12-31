---
id: "004"
title: "Fix Mark Complete logic"
stage: "green"
date: "2025-12-31"
surface: "agent"
model: "sonnet-4-5-20250929"
feature: "phase1-console"
branch: "master"
user: "H2 Todo Team"
command: "/sp.improve Option 5 Mark Complete"
labels: ["bugfix","mark-complete","phase1"]
links:
  spec: "specs/phase1-console/spec.md"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - "src/cli/output.py"
  - "src/cli/menu.py"
  - "src/models/task.py"
tests: []
---

## Prompt

improve Option 5 (Mark Complete) logic:

When a task is already 'Complete', and the user selects Option 5 for it again, the system should check its current status.

Instead of automatically marking it 'Incomplete', it should inform the user: 'Task is already marked as complete.'

Only mark it as 'Complete' if its current status is 'Pending'

## Response snapshot

Fixed the Mark Complete logic:

**Changes made:**

1. **`src/cli/output.py`**: Added `display_already_complete(task)` function that displays "Task '{title}' is already marked as complete."

2. **`src/models/task.py`**: Added `mark_complete(task_id)` method that:
   - Returns the task if not found (None)
   - Returns the task as-is if already complete (no status change)
   - Sets `completed = True` only if task is currently pending

3. **`src/cli/menu.py`**: Updated `handle_mark_complete()` to:
   - Get the task first
   - Check if task is None → show "not found" error
   - Check if task is already complete → show "already complete" message
   - Only call `mark_complete()` and show success if task was pending

## Outcome

- ✅ Impact: Option 5 now only marks pending tasks as complete; already complete tasks show informative message
- 🧪 Tests: N/A (bugfix only, no tests requested)
- 📁 Files: 3 files modified
- 🔁 Next prompts: Test with `python src/main.py` - add a task, mark it complete, try to mark it complete again
- 🧠 Reflection: Clear separation of concerns between display logic (output.py), model logic (task.py), and menu flow (menu.py)

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): Fix applied correctly
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Add option to mark task as incomplete
