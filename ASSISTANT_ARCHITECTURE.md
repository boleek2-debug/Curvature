# CURVATURE CONSOLE ARCHITECTURE

Status: Approved and Amended
Version: 1.0.0
Owner: Project Curvature
Last Updated: 2026-07-18
Milestone: ASSISTANT-001

---

# 1. Purpose

Curvature Console is a standalone internal development application coordinating:

- Curvature Project;
- Curvature Core;
- Curvature Research.

It is separate from:

- Curvature Platform;
- World Core;
- Chronicle Client;
- gameplay.

It preserves department state, context, authority boundaries and controlled continuity across ChatGPT threads.

---

# 2. Non-Negotiable Cost Architecture

Normal Console operation must not require spending beyond the user's existing ChatGPT Plus subscription.

Therefore the MVP:

- does not use the paid OpenAI API;
- does not require an API key;
- does not perform automatic paid requests;
- uses official ChatGPT Projects as the AI conversation environment;
- uses local manual transfer packages;
- keeps all transfer actions user-controlled.

Any future provider integration must be optional, disabled by default and approved through a new explicit architecture decision.

---

# 3. Selected Technology

## Language

Python 3.11.

## Desktop UI

PySide6 with Qt Widgets.

## Operational Storage

SQLite.

## Human-Readable Configuration

YAML and Markdown.

## Repository Access

Read-only access to Project Curvature during the MVP.

## AI Workflow

Official ChatGPT under the user's existing Plus subscription.

Curvature Console owns:

- roles;
- context assembly;
- local state;
- transfer packages;
- conversation records;
- attachment manifests;
- thread handoffs;
- later Department State Bus and cross-department handoffs.

ChatGPT provides AI responses through the official user interface.

---

# 4. Repository Boundary

Curvature Console repository:

```text
~/curvature-console
```

Project Curvature repository:

```text
~/Curvature
```

Console must not automatically edit or run Git operations in the Project Curvature repository during the MVP.

---

# 5. Three-Panel Workspace

All departments are visible simultaneously:

```text
+----------------------+----------------------+----------------------+
| Curvature Project    | Curvature Core       | Curvature Research   |
+----------------------+----------------------+----------------------+
```

Each panel has independent:

- role;
- context;
- draft;
- local conversation;
- attachments;
- transfer actions;
- persistence;
- Focus state.

Attachments are not shared automatically.

---

# 6. Department Authority

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

# 7. ChatGPT Projects Model

Approved structure:

```text
ChatGPT Project: Curvature Project
ChatGPT Project: Curvature Core
ChatGPT Project: Curvature Research
```

Each Project may contain successive department chats.

Project memory is helpful but is not authoritative storage.

Authoritative continuity comes from:

- repository documentation;
- SQLite department state;
- explicit package content;
- thread handoffs;
- later structured State Bus and handoffs.

---

# 8. Transfer Package Model

## Task Package

Purpose:

Frequent work inside the current ChatGPT thread.

Content:

- department identity;
- authority boundary;
- full role;
- bounded excerpts from configured documents;
- bounded recent local conversation;
- current task;
- attachment manifest;
- response instructions.

The Task Package favours compactness.

## Thread Handoff Package

Purpose:

Continue work in a new chat inside the same ChatGPT Project.

Content:

- department identity;
- authority boundary;
- full loaded context;
- larger bounded conversation excerpt;
- current task;
- attachment manifest;
- explicit continuation instructions.

The Thread Handoff Package favours continuity.

---

# 9. Thread Pressure

Official ChatGPT does not expose exact remaining thread capacity to Curvature Console.

Console may maintain an advisory estimate:

```text
GREEN
AMBER
RED
```

The estimate may use:

- recorded package size;
- recorded imported response size;
- local conversation size;
- attachment count;
- time and work since the last handoff.

AMBER prepares the user for a handoff.

RED recommends a new chat in the same ChatGPT Project.

Console must not claim the estimate is an exact ChatGPT token reading.

---

# 10. Manual Processing Flow

```text
start Console
→ restore three workspaces
→ load roles and configured documents
→ restore local state and attachments
→ prepare Task or Thread Handoff Package
→ preview package
→ copy package
→ user pastes package into official ChatGPT
→ user receives response
→ user imports response into Console
→ Console persists department continuity
```

No paid request is made by Console.

---

# 11. Logical Components

```text
Curvature Console
|
+-- Presentation
|   +-- MainWindow
|   +-- DepartmentPanel
|   +-- ContextPreviewDialog
|   +-- TransferPackageDialog
|
+-- Infrastructure
|   +-- RepositoryReader
|   +-- WorkspaceContextLoader
|   +-- TransferPackageBuilder
|   +-- SQLiteStateStore
|
+-- Configuration
|   +-- workspace YAML
|   +-- role Markdown
|
+-- Planned
    +-- ResponseImporter
    +-- ConversationRecordStore
    +-- ThreadPressureEstimator
    +-- DepartmentStateBus
    +-- HandoffManager
```

There is no mandatory AI provider component in the MVP.

---

# 12. Persistence

Current SQLite state includes:

- department conversation text;
- department draft;
- attachment metadata;
- splitter layout;
- focused department.

Planned additions:

- structured conversation entries;
- package records;
- thread identifiers;
- handoff records;
- thread pressure state;
- department summaries.

---

# 13. MVP Scope

The MVP must provide:

- standalone PySide6 application;
- three simultaneous department panels;
- isolated roles and context;
- independent state and attachments;
- persistent restart continuity;
- Task Package;
- Thread Handoff Package;
- response import;
- structured local conversation records;
- thread pressure estimation;
- controlled Department State Bus;
- explicit handoffs;
- strict authority boundaries;
- zero mandatory paid API usage.

---

# 14. Outside the MVP

- automatic repository writes;
- automatic Git operations;
- unrestricted department messaging;
- unsupported browser automation;
- shared unrestricted conversation history;
- plugin architecture;
- voice mode;
- remote synchronisation;
- multi-user collaboration;
- mandatory paid providers.

---

# 15. Implementation Roadmap

## B1

Repository and application foundation — completed.

## B2

Three-panel desktop shell — completed.

## Attachments

Independent attachment queues — completed.

## B3

Workspace configuration and context loading — completed.

## B4

Local state and restart persistence — completed.

## B5

ChatGPT Plus workflow:

1. Task and Thread Handoff packages;
2. response import;
3. structured conversation records;
4. thread pressure estimation;
5. workflow verification.

## B6

Department State Bus and handoffs.

## B7

MVP verification and closeout.

---

# 16. Governing Rules

```text
Observe other departments.
Respect their authority.
Do not perform their work.
Create a handoff when their action is required.
Use official ChatGPT through the existing Plus subscription.
Do not create hidden or automatic paid operations.
```
