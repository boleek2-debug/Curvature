# Project Curvature

> Build the minimum reliable workshop, then use it to create a living world.

## Overview

Project Curvature is a long-term engineering and world-building project.

Its final objective is a persistent living world that can be experienced through progressively richer frontends:

- Chronicle Client / MUD
- 2D
- 3D
- VR
- future multiplayer and MMORPG scale

Curvature Platform is the production workshop used to create, operate and evolve that world.

The Platform is not the world.

The different frontends are not separate games.

They are different portals into the same persistent world state, history, characters and consequences.

## Current State

Implemented foundations include:

- Curvature Core
- telemetry
- diagnostics
- indicators
- Workflow Engine foundation
- Remote Runtime
- Tailscale integration
- remote ComfyUI detection
- GPU and VRAM diagnostics
- queue monitoring
- persistent World Core foundation
- language data foundation
- automated tests

Curvature Console is maintained in a separate repository:

```text
~/curvature-console
```

Its current verified state includes:

- three simultaneous department panels
- local persistence
- context and transfer packages
- browser-mediated ChatGPT send and receive
- one shared ChatGPT Project
- URL-only conversation routing
- one-click normal task submission
- visible Chrome fallback
- independent panel request state

Latest verified Console result:

```text
56 automated tests passed
PROJECT_SCOPED_ROUTE_OK
commit b55c7e6 pushed
```

The next Console sprint is:

```text
ASSISTANT-001B5.2D — Generated File Download Capture
```

## Strategic Direction

After infrastructure recovery, development moves toward the first living-world vertical slice:

1. Persistent World State
2. Historical Language Reconstruction Foundation
3. Time, Events and Chronicle
4. Character Identity, Memory, Goals and Voice
5. First Playable Chronicle Client / MUD

The first Chronicle Client may be single-player.

Its purpose is to prove that the world persists, remembers and reacts before graphics are introduced.

## World Philosophy

The world must:

- survive restarts,
- preserve history,
- remember actions,
- create durable consequences,
- maintain character identity,
- separate fact from narration,
- remain accessible through text, 2D, 3D and VR.

The intended experience is similar to a book written through human thought and action.

## Language Philosophy

The world language is based on historical reconstruction, especially Proto-Slavic and the probable speech environment of early medieval West Slavic communities, including the Polans.

The project does not claim that a complete historically certain language survived.

It will:

- reconstruct supported forms,
- record uncertainty,
- distinguish evidence from invention,
- create missing vocabulary through explicit rules,
- support later dialect and language evolution.

See `LANGUAGE.md`.

## Architecture

### Platform Core

The source of truth for platform state.

Current components include:

- Telemetry
- Diagnostics
- Indicators
- Configuration
- Logging
- Events

### Services

- Remote Runtime
- AI Runtime
- Workflow Engine
- Asset Pipeline
- World Builder
- Export

### Planned World Core

The future source of truth for world state.

Planned components:

- Persistent World State
- Time
- Events
- Chronicle
- Places
- Characters
- Memory
- Language
- Consequences

### Frontends

Current:

- Console

Planned:

- Chronicle Client / MUD
- 2D
- 3D
- VR
- Mobile
- Web

Frontends never invent authoritative state.

## Engineering Principles

1. Never guess.
2. Verify everything.
3. Request current files when their state is uncertain.
4. Deliver complete replacement files.
5. Label files as replace, create or leave unchanged.
6. One sprint has one goal.
7. Every sprint ends with working functionality.
8. Core is the source of truth for platform state.
9. World Core will be the source of truth for world state.
10. Test before commit.
11. Commit before push.
12. Update the appropriate documentation immediately after every confirmed change.
13. Keep `HANDOFF.md` accurate as the current operational source of truth.
14. Code and documentation are written in English.
15. Development discussion is conducted in Polish.
16. Route ChatGPT conversations by persisted URL, never by title.

## Development Environment

### Clone the repository

```bash
git clone https://github.com/boleek2-debug/Curvature.git
cd Curvature
```

### Create the Conda environment

```bash
conda env create -f environment.yml
conda activate curvature
```

### Install pinned Python packages

```bash
python -m pip install -r requirements.txt
```

### Run automated tests

```bash
python -m pytest -v
```

### Run the Console

```bash
python -m console.main
```

## Current Remote Topology

```text
Curvature Dev
      |
  Tailscale
      |
Main Workstation
      |
   ComfyUI
```

The Main Workstation currently acts as the remote AI Runtime.

The verified service hostname is:

```text
thing:8188
```

## Documentation

- `HANDOFF.md` — current state and exact next step
- `CURVATURE.md` — project vision and philosophy
- `BLUEPRINT.md` — current and approved architecture
- `WORLD.md` — living-world principles
- `LANGUAGE.md` — language reconstruction and construction method
- `ROADMAP.md` — ordered development direction
- `PIPELINE.md` — deferred ideas
- `CHANGELOG.md` — completed and verified work

A new session should read `HANDOFF.md` first.

## Development Workflow

```text
Vision
  |
Architecture
  |
Sprint
  |
Working implementation
  |
Tests
  |
Commit
  |
Push
  |
Documentation
  |
Next sprint
```

## Long-Term Goal

Curvature succeeds when the same persistent world can be entered through text, 2D, 3D and VR without losing history, identity or consequence.
