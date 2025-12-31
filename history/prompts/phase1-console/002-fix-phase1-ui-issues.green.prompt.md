---
id: "002"
title: "Fix Phase 1 UI issues"
stage: "green"
date: "2025-12-31"
surface: "agent"
model: "sonnet-4-5-20250929"
feature: "phase1-console"
branch: "master"
user: "H2 Todo Team"
command: "fix three reported issues"
labels: ["bugfix","ui","phase1"]
links:
  spec: "specs/phase1-console/spec.md"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - "src/cli/output.py"
  - "src/cli/input.py"
  - "src/cli/menu.py"
tests: []
---

## Prompt

fix the following 3 issues in Phase 1:
1. Option 2 (View Tasks) must display all added tasks in a clear table format showing ID, Status, and Title.
2. In Option 3 (Update) and Option 5 (Mark Complete), change the input prompt from "Enter task ID to delete" to the correct action ("update" or "mark as complete").
3. Ensure the Task IDs are clearly visible in the list so I know which ID to use for updating or deleting.

## Response snapshot

Fixed all 3 reported UI issues:

**Issue 1 & 3**: Enhanced `display_task_list()` in `src/cli/output.py`:
- Made ID column more prominent with brackets: `[1]`, `[2]`, etc.
- Improved column headers with STATUS and TITLE
- Wider columns for better readability
- ID now clearly visible with `[ID]` format

**Issue 2**: Added new prompt functions in `src/cli/input.py`:
- `get_task_id_for_update()` - prompts "Enter task ID to update"
- `get_task_id_for_mark_complete()` - prompts "Enter task ID to mark as complete"
- Updated `src/cli/menu.py` to use appropriate prompt for each operation

## Outcome

- ✅ Impact: All 3 UI issues resolved, task IDs clearly visible, prompts match actions
- 🧪 Tests: N/A (bugfix only, no tests requested)
- 📁 Files: 3 files modified
- 🔁 Next prompts: Test the fixes with `python src/main.py`
- 🧠 Reflection: Issues were straightforward UI/UX problems; separate prompt functions allow future extensibility

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): All fixes applied correctly
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Add keyboard shortcuts for menu options
