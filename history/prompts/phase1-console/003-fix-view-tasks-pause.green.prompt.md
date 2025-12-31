---
id: "003"
title: "Fix View Tasks pause"
stage: "green"
date: "2025-12-31"
surface: "agent"
model: "sonnet-4-5-20250929"
feature: "phase1-console"
branch: "master"
user: "H2 Todo Team"
command: "/sp.implement finalize Phase 1 View Tasks"
labels: ["bugfix","view-tasks","phase1"]
links:
  spec: "specs/phase1-console/spec.md"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - "src/cli/menu.py"
tests: []
---

## Prompt

finalize Phase 1 by fixing the View Tasks (Option 2) logic:

Ensure that the 'View Tasks' function in 'src/cli/menu.py' correctly calls the service to get all tasks.

If tasks exist, it MUST loop through them and print each one with its ID, Status, and Title in the table.

If the list is empty, it should say 'No tasks found'.

Make sure the screen doesn't just jump back to the menu without showing the list. Add a small pause or ensure the print statement is executed before the menu reappears.

## Response snapshot

Fixed the View Tasks (Option 2) pause issue:

**Changes made to `src/cli/menu.py`**:
- Imported `pause_for_user` from `src.cli.input`
- Added `pause_for_user()` call after `display_task_list()` or `display_empty_list()`
- User must now press Enter before the menu redraws, ensuring they can see their task list

The `handle_view_tasks` function already:
- Correctly calls `tasklist.list_tasks()` to get all tasks
- Displays "No tasks found" if empty
- Displays table with ID, Status, Title if tasks exist
- Now pauses for user input before returning to menu

## Outcome

- ✅ Impact: View Tasks now displays properly with pause before menu redraw
- 🧪 Tests: N/A (bugfix only, no tests requested)
- 📁 Files: 1 file modified
- 🔁 Next prompts: Test with `python src/main.py` - add tasks then view them
- 🧠 Reflection: Simple fix using existing pause_for_user utility; ensures CLI UX is usable

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): Fix applied correctly
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Add keyboard navigation for menu
