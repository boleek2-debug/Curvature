# CURVATURE CONSOLE ARCHITECTURE

Status: Approved Architecture Proposal
Version: 0.1.0
Owner: Project Curvature
Last Updated: 2026-07-18
Milestone: ASSISTANT-001A

---

# 1. Purpose

Curvature Console is a standalone internal development application for coordinating three permanent Project Curvature departments:

- Curvature Project
- Curvature Core
- Curvature Research

It is not part of:

- Curvature Platform
- World Core
- Chronicle Client
- gameplay

Its purpose is to preserve role boundaries, project continuity, department state, shared awareness and controlled cross-department handoffs.

---

# 2. Core Product Requirement

All three workspaces must be visible simultaneously in the default desktop view.

The application must present:

    +----------------------+----------------------+----------------------+
    | Curvature Project    | Curvature Core       | Curvature Research   |
    +----------------------+----------------------+----------------------+
    | direction            | architecture         | sources              |
    | decisions            | implementation       | evidence             |
    | priorities           | tests                | hypotheses           |
    | roadmap              | repository state     | confidence           |
    +----------------------+----------------------+----------------------+

The departments are peers.

The default interface must not hide departments behind tabs.

Each panel must provide:

- independent conversation history
- independent input
- independent scrolling
- independent loaded context
- visible department status
- resizable width
- temporary focus or enlargement
- restoration to the three-panel view without state loss

---

# 3. Department Authority

## Curvature Project

Owns:

- project direction
- priorities
- milestone approval
- scope decisions
- cross-department arbitration

Must not:

- write implementation code
- decide scientific truth
- replace Core or Research work

## Curvature Core

Owns:

- software architecture
- implementation
- schemas
- validation
- persistence
- tests
- repository integration

Must not:

- decide scientific truth
- invent research conclusions
- independently change project direction

## Curvature Research

Owns:

- scientific and academic research
- source evaluation
- evidence assessment
- competing hypotheses
- confidence
- missing knowledge
- research graph maintenance

Must not:

- define software architecture
- write production implementation
- independently change the project roadmap

---

# 4. Cross-Department Awareness

Every workspace must be aware of the current state of the other two departments.

Awareness must be controlled.

Each workspace receives:

- its own full role context
- its own full department state
- a concise summary of the other departments
- accepted cross-department outputs
- relevant blockers
- pending decisions
- incoming and outgoing handoffs

A workspace may observe another department.

It must not perform work owned by that department.

When another department must act, the workspace creates a handoff.

---

# 5. Department State Bus

Curvature Console must provide a local controlled shared-state layer.

Logical model:

    Department State Bus
    |
    +-- Project status
    +-- Core status
    +-- Research status
    +-- active tasks
    +-- completed outputs
    +-- blockers
    +-- decisions required
    +-- handoffs

The State Bus is not an unrestricted shared conversation.

It publishes structured and intentional department information only.

---

# 6. Handoff Model

Handoffs are the approved mechanism for cross-department work.

Required fields:

- identifier
- source department
- target department
- type
- subject
- summary
- requested action
- supporting references
- status
- created timestamp
- updated timestamp

Initial handoff types:

- Decision Required
- Research Request
- Research Result
- Implementation Request
- Technical Constraint
- Clarification Request
- Review Request

Initial statuses:

- Proposed
- Acknowledged
- Accepted
- Rejected
- Completed

---

# 7. Selected Technology

## Language

Python 3.11+

Reason:

- matches the existing Curvature development environment
- allows shared engineering conventions
- supports direct repository and filesystem access
- avoids adding JavaScript, Node and Rust toolchains to the MVP

## Desktop UI

PySide6 with Qt Widgets

Reason:

- native desktop application
- mature widget system
- QSplitter supports the required three-panel layout
- panel sizes can be resized, saved and restored
- suitable for independent conversation panels
- direct integration with Python domain and infrastructure layers

## AI Integration

OpenAI Responses API behind an AI provider abstraction.

Rule:

The API generates responses.

Curvature Console owns:

- role definitions
- context assembly
- local conversation history
- department state
- handoffs
- project continuity

The architecture must permit future providers without changing the domain model.

## Operational Storage

SQLite

Stores:

- conversations
- messages
- department states
- department summaries
- handoffs
- panel layout state
- application settings
- provider conversation identifiers where applicable

## Human-Readable Configuration

YAML and Markdown

Stores:

- workspace configuration
- role definitions
- responsibility boundaries
- document assignments
- context assembly rules
- project documentation

## Repository Access

Read-only for the MVP.

Curvature Console reads configured Project Curvature repositories and documents.

Repository writing, Git operations and automatic HANDOFF generation remain outside the MVP.

---

# 8. Repository Boundary

Curvature Console must use a separate repository:

    ~/curvature-console

It must not be implemented inside the Curvature Platform repository.

Reasons:

- it is a separate internal product
- it has its own UI and release cycle
- it has different dependencies
- it must not couple its failures to World Core or Platform
- it may later support multiple repositories
- it reads Project Curvature repositories rather than becoming part of them

The initial configured Project Curvature repository is:

    ~/Curvature

---

# 9. Logical Architecture

    Curvature Console
    |
    +-- Presentation
    |   +-- MainWindow
    |   +-- ThreePanelLayout
    |   +-- ProjectPanel
    |   +-- CorePanel
    |   +-- ResearchPanel
    |
    +-- Application
    |   +-- WorkspaceManager
    |   +-- ContextOrchestrator
    |   +-- DepartmentStateBus
    |   +-- HandoffManager
    |   +-- ConversationManager
    |
    +-- Domain
    |   +-- Department
    |   +-- Workspace
    |   +-- DepartmentState
    |   +-- DepartmentSummary
    |   +-- Handoff
    |   +-- Conversation
    |   +-- ContextPackage
    |
    +-- Infrastructure
    |   +-- RepositoryReader
    |   +-- DocumentLoader
    |   +-- SQLiteStore
    |   +-- OpenAIResponsesProvider
    |   +-- SecretStore
    |
    +-- Configuration
        +-- project.yaml
        +-- core.yaml
        +-- research.yaml
        +-- role documents

---

# 10. Context Assembly

Each department receives an isolated context package.

Private department context:

- role definition
- allowed responsibilities
- prohibited responsibilities
- required documents
- department state
- active task
- department conversation history
- context assembly rules

Shared context:

- concise department summaries
- accepted outputs
- blockers
- required decisions
- relevant handoffs

Full conversation histories are not shared automatically between departments.

---

# 11. Processing Flow

    start application
    → restore Project, Core and Research
    → load role definitions
    → load assigned documents
    → load department states
    → load department summaries
    → load handoffs
    → assemble isolated context for each department
    → display all three panels simultaneously
    → process independent AI requests
    → persist messages, states, summaries and handoffs

---

# 12. Concurrency

Each workspace may have one active AI request.

The UI must remain responsive while requests are running.

MVP approach:

- background worker per active request
- UI updates through Qt signals
- cancellation where supported
- no blocking API calls on the main UI thread

All three departments may process requests independently.

---

# 13. MVP Scope

ASSISTANT-001B must provide:

- standalone PySide6 desktop application
- three simultaneous side-by-side department panels
- independent panel input and history
- resizable panels
- saved and restored panel layout
- temporary single-panel focus
- automatic role loading
- automatic document loading
- visible loaded-context list
- manual context refresh
- local conversation persistence
- persistent department state
- Department State Bus
- controlled department summaries
- handoff creation
- handoff status tracking
- OpenAI provider integration
- strict authority boundaries

---

# 14. Outside the MVP

- repository write integration
- automatic Git operations
- automatic HANDOFF generation
- unrestricted department messaging
- shared semantic knowledge index
- plugin architecture
- Chronicle interface integration
- voice mode
- local AI provider
- remote synchronization
- multi-user collaboration

---

# 15. Proposed Repository Structure

    curvature-console/
    |
    +-- README.md
    +-- HANDOFF.md
    +-- ROADMAP.md
    +-- CHANGELOG.md
    +-- pyproject.toml
    +-- environment.yml
    +-- .gitignore
    |
    +-- src/
    |   +-- curvature_console/
    |       +-- __init__.py
    |       +-- main.py
    |       |
    |       +-- presentation/
    |       +-- application/
    |       +-- domain/
    |       +-- infrastructure/
    |       +-- configuration/
    |
    +-- config/
    |   +-- workspaces/
    |       +-- project.yaml
    |       +-- core.yaml
    |       +-- research.yaml
    |
    +-- roles/
    |   +-- project.md
    |   +-- core.md
    |   +-- research.md
    |
    +-- data/
    |   +-- .gitkeep
    |
    +-- tests/
        +-- unit/
        +-- integration/

---

# 16. Implementation Roadmap

## ASSISTANT-001B1 — Repository and Application Foundation

- separate repository
- reproducible environment
- package structure
- application entry point
- empty main window
- automated startup test

## ASSISTANT-001B2 — Three-Panel Desktop Shell

- Project, Core and Research panels
- QSplitter layout
- independent scrolling and input
- resize persistence
- temporary panel focus
- UI tests where practical

## ASSISTANT-001B3 — Workspace Configuration and Context Loading

- YAML workspace definitions
- role documents
- repository reader
- document loader
- context preview
- manual refresh

## ASSISTANT-001B4 — Local State and Conversation Persistence

- SQLite schema
- conversation storage
- department state storage
- panel layout storage
- restart continuity

## ASSISTANT-001B5 — AI Provider Integration

- provider abstraction
- OpenAI Responses provider
- background requests
- independent department conversations
- error states
- API configuration

## ASSISTANT-001B6 — Department State Bus and Handoffs

- department summaries
- blockers and decisions
- handoff model
- handoff status transitions
- controlled cross-department awareness
- authority instructions in every context

## ASSISTANT-001B7 — MVP Verification and Closeout

- end-to-end three-department workflow
- restart continuity
- authority-boundary verification
- documentation
- packaging instructions
- commit and push

---

# 17. Effort Estimate

For one developer with AI assistance:

- B1: small
- B2: medium
- B3: medium
- B4: medium
- B5: medium to large
- B6: medium to large
- B7: medium

Expected MVP scale:

- approximately 7 implementation sprints
- likely several thousand lines of application and test code
- functional desktop shell should appear early
- reliable department coordination requires the later persistence, provider and handoff sprints

---

# 18. Architecture Decision

Approved baseline:

    Python 3.11+
    PySide6 / Qt Widgets
    horizontal QSplitter
    three simultaneous DepartmentPanel instances
    SQLite operational storage
    YAML and Markdown configuration
    OpenAI Responses API through provider abstraction
    read-only Project Curvature repository access
    separate curvature-console repository
    isolated department contexts
    Department State Bus
    controlled handoffs

This architecture is the baseline for ASSISTANT-001B.

Any major deviation requires an explicit Project Curvature decision.
