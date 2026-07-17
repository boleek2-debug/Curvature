# CURVATURE

Status: Draft
Version: 0.2.0
Owner: Project Curvature
Last Updated: 2026-07-18

---

# Purpose

Project Curvature is a long-term engineering and world-building project.

Its final objective is a persistent living world that can be experienced through progressively richer interfaces:

- Chronicle Client / MUD
- 2D
- 3D
- VR
- multiplayer and eventually MMORPG scale

Curvature Platform is the production workshop created to make that world possible.

The Platform is not the world.

It is the engineering environment used to create, operate, observe and evolve the world.

---

# Core Philosophy

## Workshop First

The workshop must exist before the world can be built reliably.

However, the workshop is not developed indefinitely in isolation.

> Build the minimum reliable workshop, then use it immediately to create a living slice of the world.

Every major platform capability must eventually prove its value by enabling world creation, operation or continuity.

## Living World First

The world is not defined by graphics.

Chronicle Client / MUD, 2D, 3D and VR are not separate games. They are different portals into the same persistent world state, history, characters and consequences.

## Chronicle

The world must remember.

Actions, decisions, relationships and events must leave a durable trace.

The Chronicle is the historical memory of the world and the basis for continuity, consequence, reputation, memory and future interpretation of past events.

The intended experience is similar to a book that writes itself through human thought and action.

## Language

Language is a structural part of the world, not decoration.

The linguistic foundation will be based on historical reconstruction, especially Proto-Slavic and the probable speech environment of early medieval West Slavic communities, including the Polans.

The project must never pretend that a complete historically certain language survived.

It must:

- reconstruct what can be supported,
- mark uncertainty,
- define explicit construction rules,
- create missing vocabulary consistently,
- allow dialects and daughter forms to develop from the same foundation.

The player's input language and the world's internal language are separate layers.

## Source of Truth

Curvature Core is the source of truth for platform state.

The future World Core will be the source of truth for world state.

Frontends never invent authoritative state.

Every world-facing description must be grounded in actual world state, events, memory and known uncertainty.

---

# Platform and World Layers

Infrastructure

- Linux
- Windows AI Runtime
- Git
- Development tools
- NVIDIA / CUDA
- Tailscale
- Network
- Reproducible environments

Curvature Platform

- Core
- Services
- Frontends
- World Core

Core

- Telemetry
- Diagnostics
- Indicators
- Configuration
- Logging
- Events

Services

- Remote Runtime
- AI Runtime
- Workflow Engine
- Asset Pipeline
- World Builder
- Export

World Core

- Persistent World State
- Time
- Events
- Chronicle
- Places
- Characters
- Memory
- Language
- Consequences

Frontends

- Console
- Chronicle Client / MUD
- Future 2D client
- Future 3D client
- Future VR client
- Future mobile and web interfaces

---

# First World-Facing Milestone

The first world-facing proof of concept will be a text-based Chronicle Client.

It must demonstrate that the world can:

- persist,
- remember,
- interpret actions,
- react,
- maintain character identity,
- preserve consequences,
- write its own Chronicle.

It may begin as a single-player experience.

Multiplayer is not required to prove the living-world model.

---

# Engineering Philosophy

- Never guess.
- Verify everything.
- One sprint has one goal.
- Architecture before implementation.
- Complete file replacements.
- Request current files when their state is uncertain.
- Test before commit.
- Commit before push.
- Update HANDOFF after completed work.
- Code and documentation are written in English.
- Development discussion is conducted in Polish.

---

# Visual and Cultural Direction

The long-term interface and world direction are inspired by Slavic cultures and the previously established 24th-century Slavic civilisation.

Operational interfaces must prioritise clarity over decoration.

World-facing interfaces must preserve cultural consistency across text, 2D, 3D and VR.

---

# Long-Term Objective

Project Curvature is complete only when:

- Curvature Platform can reliably build and operate world systems.
- The persistent world survives restarts and frontend changes.
- The Chronicle preserves history and consequences.
- Characters have identity, memory, goals and recognisable voices.
- The language system remains historically grounded and internally consistent.
- The Chronicle Client proves the world through text.
- 2D, 3D and VR become richer portals into the same world.
- Multiplayer and MMORPG scale can grow from the same foundations.
