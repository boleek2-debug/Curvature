# ROADMAP

Status: Draft
Version: 0.9.0
Owner: Project Curvature
Last Updated: 2026-07-18

---

# Purpose

This roadmap describes the approved order of Project Curvature development.

It is not a changelog.

Completed work belongs in CHANGELOG.

Deferred ideas belong in PIPELINE.

---

# Current Position

Current phase:

Research Enablement and Living World Foundation

Most recently completed sprint:

LANG-001 — Technical Language Foundation

Current verified state:

- WORLD-001 completed
- LANG-001 completed
- 36 automated project tests pass
- persistent World Core exists
- technical language storage and validation foundation exists

Next active sprint:

ASSISTANT-001A — Architecture and Technology Evaluation

---

# Strategic Decision

Curvature now requires a dedicated internal development application before large-scale LANGUAGE research begins.

LANG-001 provides technical structures for language data.

Curvature Research must provide the actual scientific content.

The Curvature Console is a three-department coordination application.

All three workspaces must be visible simultaneously as equal side-by-side panels.

It is required to preserve:

- department roles
- research context
- research state
- publication analysis
- research queues
- source relationships
- missing knowledge
- continuous research graphs
- cross-department awareness
- strict authority boundaries
- controlled handoffs

For this reason, ASSISTANT-001 has been promoted ahead of WORLD-002.

WORLD-002 remains approved and is postponed, not cancelled.

---

# Completed Milestones

## BUILD-001 — Reproducible Development Environment

Completed and verified.

## REMOTE-001 — Remote Runtime Foundation

Completed and verified.

## REMOTE-002 — AI Runtime Console

Completed and verified.

## REMOTE-003 — Remote Runtime Diagnostics

Completed and verified.

## REMOTE-004 — Minimal Service Heartbeat

Completed and verified.

## WORLD-001 — Persistent World State

Completed and verified:

- persistent world identifier
- Place and Entity models
- authoritative WorldState
- controlled state transitions
- versioned JSON storage
- load after restart
- automated tests

## LANG-001 — Technical Language Foundation

Completed and verified:

- language form classifications
- confidence levels
- provenance model
- LanguageEntry model
- versioned Lexicon model
- JSON storage
- validation separating historical evidence from controlled invention
- automated tests

LANG-001 is infrastructure.

It does not claim that the scientific reconstruction, phonology, lexicon or naming system is complete.

---

# Active Milestone

## ASSISTANT-001A — Architecture and Technology Evaluation

Goal

Select a reliable architecture for the Curvature Console.

Required deliverables

- architecture proposal
- technology comparison
- selected implementation approach
- repository boundary decision
- repository structure
- three-panel interaction model
- workspace configuration model
- context assembly model
- department state model
- Department State Bus design
- handoff model
- authority enforcement strategy
- conversation persistence model
- AI provider strategy
- MVP specification
- effort estimate
- implementation roadmap

Evaluation targets

- OpenAI API and Responses API
- Electron
- Tauri
- native Python desktop frameworks
- local browser application
- other suitable approaches

Completion rule

No implementation begins until the recommendation is explicit and justified.

---

# Next Milestone

## ASSISTANT-001B — Curvature Console MVP

Goal

Create a standalone desktop application that restores permanent AI workspaces without manual context rebuilding.

Required workspaces

- Curvature Project
- Curvature Core
- Curvature Research

Required MVP capabilities

- three equal workspaces visible simultaneously
- side-by-side three-panel layout
- independent panel scrolling and input
- resizable panels
- temporary panel focus without state loss
- automatic role loading
- automatic document loading
- separate conversation histories
- persistent department state
- context preview
- loaded-file visibility
- manual context refresh
- AI provider integration
- controlled cross-department awareness
- Department State Bus
- handoff creation and status tracking
- strict department separation

Boundary

Curvature Console is not Curvature Platform and is not gameplay.

---

# Research Enablement Milestone

## RESEARCH-001 — Operational Research Workspace

Goal

Make coordinated LANGUAGE work operational across Project, Core and Research, with Curvature Research providing the first content-heavy workflow.

Required capabilities

- load research role and protocol
- load LANGUAGE research context
- maintain research state and queue
- track active publications
- record references
- identify missing knowledge
- create follow-up research tasks
- maintain a connected research graph
- preserve department continuity
- publish Research status to the Department State Bus
- receive Project decisions and Core requests
- create controlled handoffs without crossing authority boundaries

---

# Language Research Phase

## LANGUAGE Research Foundation

Owned by Curvature Research.

Research scope

- Proto-Slavic evidence
- early West Slavic evidence
- the probable linguistic environment of the Polans
- competing reconstructions
- phonological hypotheses
- morphology
- naming evidence
- confidence assessment
- explicit uncertainty
- documented construction rules for missing material

Outputs must distinguish:

- reconstructed
- plausible
- Curvature-derived
- intentionally fictional
- uncertain

---

## LANG-002 — Research Data Intake

Goal

Import verified Curvature Research outputs into the Core language system.

Required deliverables

- documented research interchange format
- validation of imported records
- provenance preservation
- confidence preservation
- competing-form preservation
- rejection of invalid records
- versioned import
- automated tests

---

# Living World Milestones

## WORLD-002 — Time, Events and Chronicle

Goal

Give the world ordered history and durable consequence.

Required deliverables

- world time
- verified events
- cause and effect links
- persistent Chronicle entries
- restart continuity
- automated tests

## NPC-001 — Identity, Memory, Goals and Voice

Goal

Create persistent characters with identity, knowledge, memory, goals, relationships and voice constraints.

## CHRONICLE-001 — First Playable Chronicle Client

Goal

Create the first world-facing frontend and prove the living world through a text-first vertical slice.

---

# Later Direction

1. expand Language and World Core together
2. expand Chronicle Client
3. add 2D
4. add 3D
5. add VR
6. add multiplayer foundations
7. grow toward MMORPG scale

---

# Infrastructure Hardening

Main Workstation restart safety and Wake-on-LAN remain paused until safe physical access is available.

Do not remotely restart while GRUB defaults to Mint and nobody is physically present.

---

# Rule

An active sprint may be interrupted only by an explicit Project Curvature priority decision.
