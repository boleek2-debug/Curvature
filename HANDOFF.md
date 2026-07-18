# HANDOFF

Status: Active
Version: 1.0.0
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

All interfaces must expose the same authoritative world state, history, characters and consequences.

---

# 2. Current Priority

The active work is:

```text
ASSISTANT-001B5.1 — ChatGPT Transfer and Thread Handoff Packages
```

Curvature Console is implemented in the separate repository:

```text
~/curvature-console
```

Completed Console work:

- B1 repository and application foundation
- B2 three-panel desktop shell
- independent attachment queues
- B3 workspace configuration and context loading
- B4 local state and restart persistence
- initial B5.1 transfer-package implementation

Current verified Console baseline before the B5.1 revision:

```text
30 passed
```

Current Console implementation commit before uncommitted B5.1 work:

```text
f2f5114 Redefine B5 as zero-cost ChatGPT Plus workflow
```

---

# 3. Non-Negotiable AI Cost Decision

Normal Curvature Console operation must not cost more than the user's existing ChatGPT Plus subscription.

Therefore the MVP:

- does not use the paid OpenAI API;
- does not require `OPENAI_API_KEY`;
- does not perform automatic paid model requests;
- does not perform automatic paid web-search or tool requests;
- uses official ChatGPT Projects as the AI conversation environment;
- uses Curvature Console as the local context, persistence, transfer and continuity layer.

A paid provider may only be reconsidered through a new explicit Project decision. It must be optional, disabled by default and protected by visible spending controls.

---

# 4. ChatGPT Projects Workflow

The approved operational structure is:

```text
ChatGPT Project: Curvature Project
ChatGPT Project: Curvature Core
ChatGPT Project: Curvature Research
```

Each ChatGPT Project may contain successive chats for the same department.

Curvature Console does not assume that ChatGPT Project memory is an authoritative project database.

The durable source of continuity remains:

- Project Curvature repository documentation;
- Curvature Console SQLite state;
- explicit transfer packages;
- explicit thread handoffs;
- later Department State Bus and handoff records.

---

# 5. Package Types

## Task Package

Used for normal work in the current ChatGPT thread.

It contains:

- department identity and authority;
- full department role;
- bounded excerpts from configured documents;
- bounded recent local conversation;
- current task;
- attachment manifest.

It must remain compact enough for frequent use.

## Thread Handoff Package

Used when moving to a new chat inside the same ChatGPT Project.

It contains:

- department identity and authority;
- full loaded department context;
- a larger recent conversation excerpt;
- current task;
- attachment manifest;
- explicit continuation instructions.

It prioritises continuity over compactness.

---

# 6. Thread Limit Strategy

Curvature Console cannot read the exact remaining context capacity of an official ChatGPT thread.

It may estimate thread pressure locally using recorded package and conversation size.

Planned indicator:

```text
GREEN — normal work
AMBER — prepare a Thread Handoff Package
RED — start a new chat in the same ChatGPT Project
```

The estimate is advisory, not an authoritative value from ChatGPT.

The user remains responsible for creating the new ChatGPT chat, pasting the generated handoff and sending it.

Unsupported browser automation must not be used to bypass official ChatGPT controls.

---

# 7. Current B5.1 Revision Goal

Replace the single oversized transfer package with two explicit modes:

1. compact `Task Package`;
2. comprehensive `Thread Handoff Package`.

Required verification:

- correct department identity;
- authority boundary;
- compact Task context;
- full Handoff context;
- bounded conversation history;
- attachment manifest;
- exact clipboard copy;
- zero network calls;
- zero API dependencies;
- complete automated test suite;
- manual Project/Core/Research verification.

---

# 8. Project State

Completed and verified:

- BUILD-001
- REMOTE-001
- REMOTE-002
- REMOTE-003
- REMOTE-004
- WORLD-001
- LANG-001

Project Curvature baseline:

```text
36 automated project tests passed
```

WORLD-002 remains approved and postponed, not cancelled.

Research enablement remains the reason Curvature Console has priority.

---

# 9. Repository Boundaries

Main Project Curvature repository:

```text
~/Curvature
```

Curvature Console repository:

```text
~/curvature-console
```

During the Console MVP:

- Console reads `~/Curvature`;
- Console does not write `~/Curvature`;
- Console does not run Git operations automatically;
- proposed repository changes remain user-controlled.

---

# 10. Exact Next Step

1. Replace stale Curvature Console architecture documentation in `~/Curvature`.
2. Commit and push the main documentation correction.
3. Install the revised B5.1 Console package.
4. Run the complete Console test suite.
5. Manually verify Task and Thread Handoff packages for all departments.
6. Commit the Console implementation only after verification.

---

# 11. Engineering Rules

1. Never guess.
2. Request current files before modifying uncertain code.
3. Deliver complete replacement files.
4. Label every file as replace, create or leave unchanged.
5. One sprint has one goal.
6. Every displayed state must be verifiable.
7. Test → Commit → Push.
8. Update HANDOFF after completed work.
9. Project documentation is written in English.
10. Development discussion is in Polish.
11. No hidden or automatic paid operations.
