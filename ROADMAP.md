# ROADMAP

Status: Active
Version: 1.1.0
Owner: Project Curvature
Last Updated: 2026-07-20

---

# Purpose

This roadmap describes the approved order of Project Curvature development.

Completed work belongs in `CHANGELOG.md`.

Deferred ideas belong in `PIPELINE.md`.

Current operational state belongs in `HANDOFF.md`.

Every confirmed change to the plan must be recorded here immediately.

---

# Product Constraint

Normal Curvature Console operation must not require spending beyond the user's existing ChatGPT Plus subscription.

The approved Console workflow uses:

- one shared ChatGPT Project named `Curvature`
- three departmental conversations
- local Console persistence
- Playwright browser automation through the official ChatGPT interface
- no mandatory paid OpenAI API
- no hidden paid model or tool calls

---

# Current Position

Current phase:

```text
Research Enablement and Living World Foundation
```

Completed Project milestones:

- BUILD-001
- REMOTE-001
- REMOTE-002
- REMOTE-003
- REMOTE-004
- WORLD-001
- LANG-001

Current verified Project baseline:

```text
36 automated tests passed
```

Active Console milestone:

```text
ASSISTANT-001B5 — ChatGPT Plus Workflow Integration
```

Completed Console implementation unit:

```text
ASSISTANT-001B5.2C — Reliable ChatGPT Conversation Routing
```

Next Console implementation unit:

```text
ASSISTANT-001B5.2D — Generated File Download Capture
```

---

# Curvature Console Milestones

## ASSISTANT-001A — Architecture and Technology Evaluation

Completed.

Selected implementation:

- separate `~/curvature-console` repository
- Python 3.11
- PySide6 Qt Widgets
- SQLite
- YAML and Markdown
- read-only Project Curvature access until an explicitly approved apply action
- existing ChatGPT Plus subscription
- browser automation instead of a mandatory paid API

## ASSISTANT-001B1 — Repository and Application Foundation

Completed and verified.

## ASSISTANT-001B2 — Three-Panel Desktop Shell

Completed and verified.

## Per-Department Attachments

Completed and verified.

## ASSISTANT-001B3 — Workspace Configuration and Context Loading

Completed and verified.

## ASSISTANT-001B4 — Local State and Conversation Persistence

Completed and verified.

## ASSISTANT-001B5 — ChatGPT Plus Workflow Integration

### B5.1 — Task Package and Thread Handoff Package

Completed and verified.

Delivered:

- compact Task Package
- comprehensive Thread Handoff Package
- department authority and role context
- bounded documents and conversation
- attachment manifest
- package preview
- exact package generation
- no mandatory API dependency

### B5.2A — Browser Bridge Foundation

Completed and verified.

Delivered:

- dedicated browser profile
- Playwright CDP connection
- visible browser proof of concept
- local browser lifecycle foundation

### B5.2B — Visible Send and Receive Workflow

Completed and verified.

Delivered:

- browser-mediated message sending
- response capture
- worker integration
- department route persistence
- visible Chrome workflow

### B5.2C — Reliable ChatGPT Conversation Routing

Completed, verified and pushed.

Delivered:

- one-click `Send Task`
- one confirmation for `Thread Handoff`
- one shared ChatGPT Project
- URL-only department routing
- no routing by conversation title
- persisted active conversation URL
- conversation URL history
- support for standard and project-scoped conversation URLs
- visible Chrome fallback
- browser lifecycle failure handling
- originating-panel-only locking
- response return to the correct panel

Verified:

```text
56 automated tests passed
PROJECT_SCOPED_ROUTE_OK
commit b55c7e6 pushed
```

### B5.2D — Generated File Download Capture

Active next sprint.

Deliver:

- Playwright download event capture
- controlled per-department inbox
- original filename preservation
- collision-safe filename handling
- source conversation URL
- response-to-file association
- visible downloaded-file record in Console
- lifecycle cleanup
- automated tests
- live generated-file verification

### B5.2E — Package Apply Engine

Deliver:

- machine-readable package manifest
- target repository identification
- repository-relative path validation
- ZIP traversal protection
- symlink and unsafe-entry rejection
- file classification:
  - replace existing
  - add new
  - conflict
  - skip
- apply preview
- one explicit approval before repository writes
- backup or rollback strategy
- test command integration
- Git diff presentation
- no automatic commit or push

Package construction rule:

```text
root of ZIP = root of target repository
```

### B5.3 — Structured Department Conversation Records

Deliver:

- user and assistant entries
- timestamps
- source and route markers
- restart persistence
- migration from plain transcript where required

### B5.4 — Thread Pressure Estimation

Deliver:

- local package and conversation size estimate
- GREEN / AMBER / RED state
- advisory warning
- handoff preparation
- no claim of exact ChatGPT context capacity

### B5.5 — Workflow Verification and Closeout

Verify:

- Project workflow
- Core workflow
- Research workflow
- new-chat Thread Handoff
- generated file capture
- package application
- attachment isolation
- restart continuity
- zero mandatory paid API use
- current documentation

## ASSISTANT-001B6 — Department State Bus and Handoffs

- structured department summaries
- controlled cross-department awareness
- explicit handoffs
- authority enforcement
- no automatic sharing of full conversations

## ASSISTANT-001B7 — MVP Verification and Closeout

- end-to-end workflow
- restart continuity
- authority boundaries
- cost rule
- packaging
- documentation

---

# Research Enablement

## RESEARCH-001 — Operational Research Workspace

Goal:

Make coordinated LANGUAGE research operational across Project, Core and Research.

Required capabilities:

- research role and protocol
- publication analysis
- evidence and confidence
- references
- missing knowledge
- follow-up tasks
- connected research graph
- controlled handoffs

## LANGUAGE Research Foundation

Owned by Curvature Research.

Must distinguish:

- reconstructed
- plausible
- Curvature-derived
- intentionally fictional
- uncertain

## LANG-002 — Research Data Intake

Import verified Research outputs into the Core language system while preserving provenance, confidence and competing forms.

---

# Living World Milestones

## WORLD-002 — Time, Events and Chronicle

Give the world ordered history and durable consequences.

## NPC-001 — Identity, Memory, Goals and Voice

Create persistent characters with identity, knowledge, memory, goals, relationships and voice constraints.

## CHRONICLE-001 — First Playable Chronicle Client

Prove the living world through the first text-first world-facing vertical slice.

---

# Rule

An active sprint may be interrupted only by an explicit Project Curvature priority decision.

Documentation must remain current throughout development, not only at sprint closeout.
