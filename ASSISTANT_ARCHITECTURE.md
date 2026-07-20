# CURVATURE CONSOLE ARCHITECTURE

Status: Approved and Active
Version: 1.1.0
Owner: Project Curvature
Last Updated: 2026-07-20
Milestone: ASSISTANT-001

---

# 1. Purpose

Curvature Console is a standalone internal development application coordinating:

- Curvature Project
- Curvature Core
- Curvature Research

It preserves department state, context, authority boundaries and controlled continuity across ChatGPT conversations.

It is separate from:

- Curvature Platform
- World Core
- Chronicle Client
- gameplay

---

# 2. Non-Negotiable Cost Architecture

Normal Console operation must not require spending beyond the user's existing ChatGPT Plus subscription.

Therefore the current architecture:

- does not require the paid OpenAI API
- does not require an API key
- does not perform hidden paid requests
- uses the official ChatGPT web interface
- uses Playwright browser automation
- keeps local state in Curvature Console
- keeps repository changes explicit and user-approved

Any future paid provider requires a new explicit Project decision.

---

# 3. Selected Technology

- Python 3.11
- PySide6 with Qt Widgets
- SQLite
- YAML and Markdown
- Playwright
- Google Chrome with a dedicated Console profile

Curvature Console repository:

```text
~/curvature-console
```

Project Curvature repository:

```text
~/Curvature
```

---

# 4. Three-Panel Workspace

All departments remain visible simultaneously.

Each panel owns independent:

- role
- context
- draft
- local conversation
- attachments
- route state
- browser request state
- persistence
- focus state

Only the department that submits a browser request is locked.

Other panels remain usable.

---

# 5. Department Authority

## Project

Owns direction, priorities, approval, scope and arbitration.

## Core

Owns architecture, implementation, schemas, persistence, validation and tests.

## Research

Owns sources, evidence, hypotheses, confidence, missing knowledge and research graph.

A department may observe concise state from another department.

It must not perform another department's work.

Cross-department action requires an explicit handoff.

---

# 6. Shared ChatGPT Project Model

Approved structure:

```text
ChatGPT Project: Curvature
├── Project / System Theorist conversation
├── Core conversation
└── Research conversation
```

Conversation titles are mutable and presentation-only.

They are forbidden as technical routing identifiers.

The routing model is:

```text
department_id
→ active_conversation_url
→ conversation URL history
```

Verified route forms:

```text
https://chatgpt.com/c/<conversation-id>
https://chatgpt.com/g/<project-id>/c/<conversation-id>
```

The shared Project URL is used only when creating a new chat during Thread Handoff.

---

# 7. Browser Bridge

The browser bridge:

- connects through Chrome DevTools Protocol
- uses a dedicated browser profile
- opens the persisted conversation URL
- enters the prepared task
- sends it
- waits for a completed assistant response
- returns the response to the originating panel
- persists a verified resulting route
- releases the UI after success or failure

Visible Chrome is an approved fallback when headless rendering does not expose the required ChatGPT interface.

Browser lifecycle failures must:

- be detected
- return an explicit error
- stop owned browser processes
- release the active panel
- never leave the application permanently waiting

The ChatGPT DOM is an external and changeable dependency.

Selectors and route handling must be based on observed behavior and verified through tests and live checks.

---

# 8. User Interaction

## Send Task

```text
enter task
→ click Send Task once
→ send immediately to the active department route
```

There is no second confirmation.

## Thread Handoff

```text
prepare handoff
→ one explicit confirmation
→ open shared Project
→ create new chat
→ send handoff
→ capture new conversation URL
→ persist it as active for the department
```

---

# 9. Persistence

SQLite state includes or is planned to include:

- department conversation text
- department draft
- attachment metadata
- layout and focus state
- active conversation URL
- conversation URL history
- structured conversation records
- generated-file records
- handoff records
- thread pressure state

The active route is authoritative for browser delivery.

Conversation title is not authoritative.

---

# 10. Generated File Capture

Next implementation unit:

```text
ASSISTANT-001B5.2D
```

Required behavior:

```text
ChatGPT response
→ detect download
→ save to data/inbox/<department>/
→ preserve original name
→ avoid collision
→ record source conversation URL
→ associate file with the response
→ expose it in the Console
```

Downloading into the Console inbox does not require a second confirmation.

Writing into a repository does require explicit approval.

---

# 11. Package Apply Engine

Planned implementation unit:

```text
ASSISTANT-001B5.2E
```

Approved package contract:

```text
root of ZIP = root of target repository
```

Every package must include a machine-readable manifest describing:

- package type
- target repository
- files
- repository-relative paths
- intended action

Required safety:

- reject absolute paths
- reject `..`
- reject path traversal
- reject unsafe symlinks
- reject ambiguous target repositories
- classify replace, add, conflict and skip
- show an apply preview
- require one explicit approval
- do not commit or push automatically

The assistant is responsible for generating conforming packages.

---

# 12. Logical Components

```text
Curvature Console
|
+-- Presentation
|   +-- MainWindow
|   +-- DepartmentPanel
|   +-- BrowserBridgeWorker
|   +-- TransferPackageDialog
|   +-- future Download Inbox
|   +-- future Package Apply Preview
|
+-- Infrastructure
|   +-- RepositoryReader
|   +-- WorkspaceContextLoader
|   +-- TransferPackageBuilder
|   +-- SQLiteStateStore
|   +-- ChatGPTBrowserBridge
|   +-- future DownloadCapture
|   +-- future PackageValidator
|   +-- future PackageApplyEngine
|
+-- Configuration
    +-- workspace YAML
    +-- role Markdown
```

---

# 13. Verification State

Latest completed Console unit:

```text
ASSISTANT-001B5.2C — Reliable ChatGPT Conversation Routing
```

Verified:

```text
56 automated tests passed
PROJECT_SCOPED_ROUTE_OK
commit b55c7e6 pushed
```

---

# 14. Documentation Rule

Documentation is updated immediately after each confirmed change to:

- state
- architecture
- decision
- plan
- verification
- commit or push status
- known issue
- exact next step

Documentation is not deferred to sprint closeout.

---

# 15. Governing Rules

```text
Never guess.
Use current files and observed behavior.
Route by persisted URL, never by conversation title.
One sprint, one goal.
One-click normal task.
One confirmation for Thread Handoff.
Automatic file download to a controlled inbox.
Explicit approval before repository writes.
No hidden paid operations.
Keep documentation current at all times.
```
