# BLUEPRINT

Status: Draft
Version: 0.3.0
Owner: Project Curvature
Last Updated: 2026-07-18

---

# Purpose

This document describes the current technical architecture of Curvature Platform and the approved direction for the future World Core.

Current implementation and planned architecture are explicitly separated.

---

# High-Level Architecture

    Project Curvature
        |
        +-- Curvature Platform
        |     |
        |     +-- Core
        |     +-- Services
        |     +-- Frontends
        |     +-- Planned World Core
        |
        +-- Persistent Living World
              |
              +-- Chronicle Client / MUD
              +-- Future 2D
              +-- Future 3D
              +-- Future VR
              +-- Future Multiplayer / MMORPG

All world-facing frontends must connect to the same persistent world state.

---

# Current Platform Core

Curvature Core is the source of truth for platform state.

Current responsibilities:

- collect telemetry,
- evaluate diagnostics,
- produce indicators,
- manage configuration,
- expose verified data to frontends.

Current components:

- Telemetry
- Diagnostics
- Indicators
- Configuration foundation
- Logging foundation
- Events foundation

---

# Current Services

## Remote Runtime

Current implementation:

- Tailscale communication
- Remote workstation abstraction
- HTTP JSON retrieval
- ComfyUI availability detection
- ComfyUI system statistics
- ComfyUI queue status
- remote GPU and VRAM information
- remote operating system and RAM information
- remote Python, PyTorch and ComfyUI versions

## AI Runtime

Current implementation:

- remote ComfyUI integration
- verified AI Runtime state
- READY, ATTENTION and OFFLINE presentation

## Workflow Engine

Current implementation:

- Workflow registry
- Workflow states

---

---

# Curvature Console Architecture

Curvature Console is a standalone internal development application.

It is separate from:

- Curvature Platform
- World Core
- Chronicle Client
- gameplay

Its purpose is to coordinate three permanent departments:

- Curvature Project
- Curvature Core
- Curvature Research

## Three-Panel Workspace Model

All three departmental workspaces must be visible at the same time.

The default desktop layout is:

    +----------------------+----------------------+----------------------+
    | Curvature Project    | Curvature Core       | Curvature Research   |
    +----------------------+----------------------+----------------------+
    | direction            | architecture         | sources              |
    | decisions            | implementation       | evidence             |
    | priorities           | tests                | hypotheses           |
    | roadmap              | repository state     | confidence           |
    +----------------------+----------------------+----------------------+

The workspaces are peers.

No workspace is treated as the primary workspace with the other two hidden behind tabs.

Each panel must support:

- independent scrolling
- independent conversation history
- independent input
- independent loaded context
- visible department status
- resizable width
- temporary focus or enlargement
- restoration to the three-panel view without losing state

## Department Responsibilities

### Curvature Project

Owns:

- project direction
- priorities
- milestone approval
- scope decisions
- cross-department arbitration

Must not:

- write implementation code
- decide scientific truth
- replace Curvature Core or Curvature Research work

### Curvature Core

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

### Curvature Research

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

## Cross-Department Awareness

Every workspace must be aware of the current state of the other two departments.

Awareness must be provided through explicit shared state, not uncontrolled access to all conversation history.

Each workspace receives:

- its own full role context
- its own full department state
- a concise status summary of the other departments
- accepted cross-department outputs
- relevant blockers
- pending decisions
- incoming and outgoing handoffs

A workspace may observe another department's status.

It must not perform work owned by that department.

When cross-department action is required, the workspace creates a handoff.

## Department State Bus

Curvature Console must provide a controlled shared-state layer:

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

The State Bus is not a shared unrestricted conversation.

It exposes only structured, relevant and intentionally published department information.

## Handoff Model

Handoffs are the approved mechanism for cross-department work.

Required handoff fields:

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

Initial handoff statuses:

- Proposed
- Acknowledged
- Accepted
- Rejected
- Completed

A workspace must not bypass the handoff model by performing another department's work itself.

## Context Isolation and Context Sharing

Each department has an isolated context package containing:

- role definition
- allowed responsibilities
- prohibited responsibilities
- required documents
- department state
- active task
- conversation history
- context assembly rules

Shared context contains only:

- department summaries
- accepted outputs
- blockers
- required decisions
- relevant handoffs

This preserves awareness without role collapse.

## Logical Components

Curvature Console requires:

- Desktop UI
- Three-Panel Layout Manager
- Workspace Manager
- Context Orchestrator
- Document Loader
- Repository Reader
- Department State Store
- Department State Bus
- Handoff Manager
- Conversation Store
- AI Provider abstraction
- Workspace configuration

## Core Processing Flow

    start application
    → restore all three workspaces
    → load each department role
    → load each department documents
    → load each department state
    → load shared department summaries
    → load handoffs
    → assemble isolated context for each workspace
    → display all three workspaces simultaneously
    → persist conversations, department state and handoffs

## Authority Rule

Curvature Console coordinates departments.

It does not erase their boundaries.

The governing rule for every workspace is:

    Observe other departments.
    Respect their authority.
    Do not perform their work.
    Create a handoff when their action is required.


---

# Planned World Core

World Core is approved architecture but is not yet implemented.

It will become the source of truth for world state.

Planned responsibilities:

- persist world state,
- manage world time,
- record events,
- preserve consequences,
- maintain character identity and memory,
- provide facts to narration,
- support the Chronicle,
- expose the same world to all world-facing frontends.

Planned components:

## World State

- places
- entities
- ownership
- relationships
- resources
- conditions
- persistent changes

## Time

- world clock
- durations
- scheduled events
- historical ordering
- ageing and change

## Events

- verified actions
- state transitions
- causes
- effects
- references to actors and places

## Chronicle

- durable historical record
- narrative interpretation of verified events
- multiple viewpoints where appropriate
- separation between fact and narration

## Characters

- identity
- knowledge
- memory
- goals
- relationships
- emotional state
- cultural and linguistic profile

## Language

- historical reconstruction data
- confidence and provenance
- construction rules
- lexicon
- names
- morphology
- phonology
- dialect development
- language evolution

---

# Frontends

## Current

- Console

The Console is an operator interface for Curvature Platform.

It does not represent the world.

## Planned World-Facing Frontends

### Chronicle Client / MUD

The first world-facing frontend.

Responsibilities:

- accept natural-language player intent
- present verified world state through narration
- expose characters and places
- show consequences
- provide access to the Chronicle

### 2D Client

A visual portal into the same world.

### 3D Client

A spatial portal into the same world.

### VR Client

An immersive portal into the same world.

Frontends do not own world state.

They query and present World Core.

---

# Language Architecture

## Historical Reconstruction Layer

Stores reconstructed forms, evidence, uncertainty and provenance.

## Curvature Construction Layer

Defines how missing words and structures are created consistently.

## World Language Layer

Applies regional, social, historical and character-specific variation.

## Player Interpretation Layer

Maps modern natural-language player input into candidate world actions.

No player action becomes world fact until validated against World Core.

---

# Current Production Topology

    Curvature Dev
        |
    Tailscale
        |
    Main Workstation
        |
    ComfyUI

The Main Workstation is treated as a remote AI Runtime.

Current operational issue:

- the workstation is physically powered on,
- Tailscale device `thing` is offline,
- remote recovery and unattended operation must be restored.

---

# Current Verified Components

- Telemetry
- Diagnostics
- Console
- Workflow foundation
- Remote Runtime
- ComfyUI detection over Tailscale
- ComfyUI system statistics
- ComfyUI queue status
- remote GPU and VRAM diagnostics
- remote runtime diagnostics
- automated Remote Runtime tests

---

# Planned Vertical Slice

The first living-world vertical slice should include:

- one persistent place,
- one or more characters,
- world time,
- verified player actions,
- character memory,
- consequences,
- reconstructed language data,
- Chronicle entries,
- a text-based Chronicle Client.

---

# Design Principles

Build simple.

Verify every layer.

Keep platform state and world state authoritative.

Separate fact from narration.

Expand one sprint at a time.

Use the minimum reliable workshop to create the first living slice early.
