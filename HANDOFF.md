# HANDOFF

Status: Active
Version: 1.1.0
Owner: Project Curvature
Last Updated: 2026-07-20

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

# 2. Documentation Rule

Project documentation is a live source of truth.

Every confirmed change to:

- current state
- architecture
- decisions
- plan
- implementation status
- verification status
- commit or push status
- known issues
- exact next step

must be recorded in the appropriate document immediately.

Documentation updates are not deferred to sprint closeout.

Document responsibilities:

- `HANDOFF.md` — current operational truth and exact next step
- `ROADMAP.md` — approved order and active milestone
- `CHANGELOG.md` — completed and verified work only
- `BLUEPRINT.md` — current and approved architecture
- `ASSISTANT_ARCHITECTURE.md` — detailed Curvature Console architecture
- `PIPELINE.md` — intentionally deferred ideas
- `ADR-001.md` — non-negotiable engineering rules
- `README.md` — repository entry point and operating summary

---

# 3. Current Priority

The active cross-repository work is:

```text
Curvature Console documentation alignment
```

Curvature Console is implemented in the separate repository:

```text
~/curvature-console
```

The main Project Curvature repository is:

```text
~/Curvature
```

Curvature Console is currently ahead of the stale architecture previously recorded in this repository.

The Console repository has completed and pushed:

```text
ASSISTANT-001B5.2C — Reliable ChatGPT Conversation Routing
```

Verified Console state:

```text
56 automated tests passed
live routing verification passed
commit b55c7e6 pushed
main == origin/main
working tree clean
```

Verified live response:

```text
PROJECT_SCOPED_ROUTE_OK
```

---

# 4. Approved ChatGPT Operating Model

Curvature Console uses one shared ChatGPT Project:

```text
Curvature
```

The Project contains three departmental conversations:

- Curvature Project / System Theorist
- Curvature Core
- Curvature Research

Conversation titles are presentation-only and must never be used as technical identifiers.

Routing is based on:

```text
department_id
→ persisted active_conversation_url
→ conversation URL history
```

Supported verified conversation URL forms include:

```text
https://chatgpt.com/c/<conversation-id>
https://chatgpt.com/g/<project-id>/c/<conversation-id>
```

The shared Project URL is used only to create a new departmental chat during Thread Handoff.

The Console must never route by:

- conversation title
- sidebar text
- visible item order
- guessed project name
- guessed DOM position

---

# 5. Verified Console Interaction Model

Normal task:

```text
enter task
→ click Send Task once
→ Console sends to the persisted active conversation URL
→ Console waits for the response
→ response returns to the originating department panel
```

Thread Handoff:

```text
prepare handoff
→ one explicit confirmation
→ open the shared Curvature Project
→ create a new chat
→ send the handoff
→ capture the resulting conversation URL
→ persist it as the active route for that department
```

Current browser model:

- official ChatGPT web interface
- browser automation through Playwright
- existing ChatGPT Plus subscription
- no mandatory paid OpenAI API
- visible Chrome fallback when headless rendering is insufficient
- only the active department panel is locked during its request
- other department panels remain usable
- browser lifecycle failures must return an error and release the UI

---

# 6. Package and File-Transfer Direction

The next Console sprint is:

```text
ASSISTANT-001B5.2D — Generated File Download Capture
```

Planned flow:

```text
ChatGPT response
→ detect generated file download
→ save to data/inbox/<department>/
→ preserve filename and source conversation URL
→ avoid accidental overwrite
→ expose the file inside Curvature Console
```

The following sprint will introduce a Package Apply Engine.

Approved package standard:

```text
root of ZIP = root of target repository
```

Packages must:

- preserve repository-relative paths
- avoid an unnecessary wrapper directory
- include a machine-readable manifest
- identify the target repository
- identify every included file and intended action
- block absolute paths, `..`, unsafe links and path traversal
- require explicit approval before writing into a repository

The assistant is responsible for producing packages in the approved structure.

---

# 7. Project State

Completed and verified in the main Project Curvature repository:

- BUILD-001
- REMOTE-001
- REMOTE-002
- REMOTE-003
- REMOTE-004
- WORLD-001
- LANG-001

Current verified Project Curvature baseline recorded by the repository:

```text
36 automated project tests passed
```

WORLD-002 remains approved and postponed, not cancelled.

Research enablement remains the reason Curvature Console has priority.

---

# 8. Repository Boundaries

Main Project Curvature repository:

```text
~/Curvature
```

Curvature Console repository:

```text
~/curvature-console
```

Current rule:

- Console reads `~/Curvature`
- Console does not silently modify either repository
- generated files may be downloaded into a controlled Console inbox
- repository writes require a visible apply plan and explicit user approval
- automatic Git commit or push is not part of the current implementation

---

# 9. Exact Next Step

1. Apply this documentation alignment package to `~/Curvature`.
2. Run the Project Curvature test suite.
3. Run `git diff --check`.
4. Review `git status` and `git diff --stat`.
5. Commit and push the documentation alignment.
6. Confirm both repositories have current documentation.
7. Start `ASSISTANT-001B5.2D — Generated File Download Capture`.

---

# 10. Engineering Rules

1. Never guess.
2. Request current files, screenshots or command output before modifying uncertain state.
3. Deliver complete replacement files.
4. Label every file as replace, create or leave unchanged.
5. One sprint has one goal.
6. Every displayed state must be verifiable.
7. Update documentation immediately after every confirmed change.
8. Test → verify → document → commit → push.
9. Code and documentation are written in English.
10. Development discussion is conducted in Polish.
11. No hidden or automatic paid operations.
12. Conversation titles are never technical routing identifiers.
