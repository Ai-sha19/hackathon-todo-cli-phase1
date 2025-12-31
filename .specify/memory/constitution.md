<!--
Sync Impact Report:
- Version change: N/A → 1.0.0 (initial ratification)
- Modified principles: N/A (all new)
- Added sections: 4 (Philosophy, Workflow, Architecture Constraints, Technology Constraints, Quality Standards, Governance)
- Removed sections: N/A
- Templates requiring updates: ✅ plan-template.md (no changes needed - Constitution Check section compatible)
- ✅ spec-template.md (no changes needed - aligns with spec-driven approach)
- ✅ tasks-template.md (no changes needed - traces to spec/plan)
- Follow-up TODOs: None
-->

# H2 Todo Constitution

## Core Principles

### I. Spec-Driven Development
Every feature MUST have an approved specification before production code is written. Specifications serve as the authoritative source for implementation details, behavior, and acceptance criteria.

### II. Phase Discipline
Phase I is strictly limited to planning, analysis, and specifications. Production code generation is prohibited until Phase II. This separation ensures thorough design before implementation begins.

### III. Agentic Workflow
The development sequence MUST follow: Constitution → Plan → Tasks → Specify → Implement. Each phase produces artifacts that inform and constrain subsequent phases.

### IV. No Manual Coding (NON-NEGOTIABLE)
Manual code generation is prohibited during Phase I. All code generation must trace to approved Tasks and Specifications.

### V
. Traceability
Every future code change MUST map to a Task and Specification. Changes without traceability are not permitted.

## Additional Constraints

### Architecture Constraints (Phase I)

- **Application Type**: Todo application
- **Storage**: In-memory only (conceptual, no implementation)
- **Interface**: CLI-based (design-level only)
- **Focus**: Data models, user flows, and feature behavior

### Technology Constraints (For Later Phases)

- **Language**: Python 3.13+
- **Package Manager**: uv
- **Style Guide**: PEP 8
- **Documentation**: All logic must be spec-backed

### Quality Standards

- Specifications MUST be clear, testable, and unambiguous
- Edge cases MUST be explicitly documented
- Simplicity is preferred over premature optimization

## Governance

This constitution is the authoritative source for project practices. It supersedes all other informal practices and conventions.

**Amendment Procedure**:
- Proposed amendments MUST be documented with rationale
- Amendments require review and approval
- Complex amendments MUST include a migration plan

**Compliance**:
- All PRs and reviews MUST verify constitution compliance
- Deviations MUST be justified and documented

**Reference**:
- Use `.specify/memory/constitution.md` for governance questions
- Use `specs/` directory for feature-specific specifications
- Use `history/prompts/` for prompt history records

**Version**: 1.0.0 | **Ratified**: 2025-12-31 | **Last Amended**: 2025-12-31
