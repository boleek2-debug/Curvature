# HANDOFF

Status: Draft
Version: 0.9.0
Owner: Project Curvature
Last Updated: 2026-07-18

---

# 1. Mission

Project Curvature is a long-term engineering and world-building project.

Curvature Platform is the production workshop.

The final objective is a persistent living world accessible through:

- Chronicle Client / MUD
- 2D
- 3D
- VR
- future multiplayer and MMORPG scale

Those interfaces must expose the same authoritative world state, history, characters and consequences.

---

# 2. Current Priority

The next active sprint is:

ASSISTANT-001A — Architecture and Technology Evaluation

Purpose:

Design the Curvature Console as a standalone internal development application that provides persistent, role-based AI workspaces and removes the need to rebuild context manually.

The first practical use case is coordinated work on LANGUAGE across Curvature Project, Curvature Core and Curvature Research.

Curvature Console is not a Research-only application.

Completed and verified:

- WORLD-001 — Persistent World State
- LANG-001 — Technical Language Foundation
- 36 automated project tests passed
- commit and push completed

---

# 3. Why Curvature Console Is Now Required

LANG-001 created the technical structures that can store classified language data, provenance and confidence.

It did not create the scientific content of the language.

That content must be produced through long-running Curvature Research work involving:

- academic publications
- competing reconstructions
- evidence assessment
- confidence evaluation
- reference analysis
- missing-knowledge identification
- follow-up research tasks
- a connected research graph

The current workflow based on separate ChatGPT conversations requires repeated manual context reconstruction and risks losing research continuity.

Curvature Console is therefore a prerequisite for efficient LANGUAGE research rather than a distant convenience.

---

# 4. Curvature Console Definition

Curvature Console is a standalone internal developer tool.

It is not:

- Curvature Platform
- World Core
- Chronicle Client
- gameplay
- a wrapper around one shared chat

It must provide three permanent and strictly separated workspaces:

1. Curvature Project
2. Curvature Core
3. Curvature Research

All three workspaces must be visible simultaneously, side by side, as equal panels in the default application view.

The default interface must not hide departments behind tabs.

Each workspace must own:

- a role definition
- allowed and prohibited responsibilities
- required documents
- department state
- active task
- conversation history
- context assembly rules

Opening the application must automatically restore all three departments to a usable state without manual copying and pasting.

Each panel must support independent scrolling, input, history and loaded context.

Panels must be resizable and one panel may be temporarily enlarged without destroying or unloading the other two.

---

# 5. Programmatic Responsibilities

The application must include the following logical components:

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

Required workflow:

    start application
    → restore Project, Core and Research simultaneously
    → load each role
    → load assigned documents
    → load each department state
    → load shared department summaries
    → load handoffs
    → assemble isolated context for each department
    → display all three panels
    → persist conversations, department states and handoffs

The repository and explicit department state are the durable source of continuity.

AI conversation memory alone must not be treated as authoritative project storage.

---

## Cross-Department Awareness and Authority

Every workspace must know the current state of the other two departments.

This awareness must be controlled.

Each workspace receives:

- its own full context
- a concise summary of the other departments
- accepted outputs
- blockers
- pending decisions
- relevant handoffs

A workspace may observe another department.

It must not perform work owned by that department.

Authority boundaries:

- Project owns direction, priorities and approval
- Core owns architecture, implementation, validation and tests
- Research owns scientific evidence, hypotheses and confidence

When action by another department is required, the workspace creates a handoff.

Required initial handoff statuses:

- Proposed
- Acknowledged
- Accepted
- Rejected
- Completed

The application must include this instruction in every workspace role:

    Observe the state and outputs of other departments.
    Do not perform work owned by another department.
    Create a handoff when cross-department action is required.


# 6. MVP Scope

ASSISTANT-001B — Curvature Console MVP must provide:

- standalone desktop application
- three permanent workspaces visible simultaneously
- three equal side-by-side panels
- independent panel scrolling and input
- resizable panels
- temporary panel focus without state loss
- automatic role loading
- automatic document loading
- separate conversation histories
- persistent department state
- context preview
- visible list of loaded files
- manual context refresh
- AI provider integration
- Department State Bus
- controlled cross-department awareness
- handoff creation and tracking
- strict department separation

Outside the MVP:

- automatic Git operations
- automatic HANDOFF generation
- unrestricted department-to-department messaging
- shared knowledge index
- plugin system
- Chronicle interface integration
- voice mode
- local AI support

---

# 7. Curvature Research Workspace

The first operational target is coordinated LANGUAGE work across all three departments.

Curvature Research is the first content-heavy workflow, but Project and Core are equal first-class workspaces.

It must be able to load:

- Research role definition
- research protocol
- LANGUAGE.md
- research roadmap
- research state
- research queue
- active publication or research project
- source and reference records
- research graph state

The research workflow must support:

    publication
    → summary
    → confirmed facts
    → hypotheses
    → evidence
    → confidence
    → reference analysis
    → missing knowledge
    → follow-up tasks
    → research graph update

Curvature Research owns scientific interpretation.

Curvature Core owns application architecture, schemas, validation, persistence and integration.

---

# 8. Exact Next Step

Complete ASSISTANT-001A.

Required deliverables:

1. architecture proposal
2. technology evaluation
3. selected implementation approach
4. repository boundary decision
5. proposed repository structure
6. state and context storage design
7. AI provider strategy
8. MVP specification
9. three-panel interaction model
10. Department State Bus design
11. handoff model
12. authority enforcement strategy
13. implementation roadmap
14. development effort estimate

Technologies to evaluate include:

- OpenAI API and Responses API
- Electron
- Tauri
- native Python desktop approaches
- browser-based local application
- other suitable desktop architectures

Do not begin implementation until the evaluation produces a clear recommendation.

---

# 9. Approved Development Order

1. ASSISTANT-001A — Architecture and Technology Evaluation
2. ASSISTANT-001B — Curvature Console MVP
3. RESEARCH-001 — Operational Research Workspace
4. LANGUAGE Research Foundation
5. LANG-002 — Research Data Intake
6. WORLD-002 — Time, Events and Chronicle
7. NPC-001 — Identity, Memory, Goals and Voice
8. CHRONICLE-001 — First Playable Chronicle Client
9. expand World Core and Platform together
10. 2D
11. 3D
12. VR
13. multiplayer and MMORPG scale

Research can continue in parallel after RESEARCH-001 becomes operational.

---

# 10. Infrastructure Status

The Main Workstation is currently reachable through Tailscale and ComfyUI.

The earlier outage is not fully diagnosed.

The restart-to-Linux explanation remains plausible but unverified.

Do not restart the workstation remotely while GRUB defaults to Mint and nobody is physically present.

Remaining physical-access tasks stay deferred until safe access is available.

---

# 11. Engineering Rules

1. Never guess.
2. Request current files before modifying uncertain code.
3. Deliver complete replacement files.
4. Label every file as replace, create or leave unchanged.
5. One sprint has one goal.
6. Every sprint finishes with working functionality.
7. Every displayed state must be verifiable.
8. Test → Commit → Push.
9. Update HANDOFF after completed work.
10. Project documentation is written in English.
11. Development discussion is in Polish.

---

# 12. Session End Checklist

- Update HANDOFF.md
- Run tests when code changed
- Commit
- Push
- Record the next exact step

A new Curvature Core session should read HANDOFF.md first.
