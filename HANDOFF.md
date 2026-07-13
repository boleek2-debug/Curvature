# HANDOFF

Status: Draft
Version: 0.2.0
Owner: Project Curvature
Last Updated: 2026-07-13

---

# 1. Mission

Project Curvature is a long-term engineering project.

The final objective is a fully playable MMORPG and, eventually, an MMORPGVR world.

Curvature Platform is the production workshop used to build that world.

The workshop is always developed before the game itself.

---

# 2. Current Priority

Laptop-side Curvature Platform.

Nothing has higher priority.

Current focus:

- Curvature Core
- Console
- Remote Runtime
- AI Runtime integration
- Workflow foundation

Marian is intentionally postponed.

---

# 3. Current Architecture

Infrastructure

    Linux
        |
Curvature Platform
        |
   +----+-------------------+
   |                        |
 Core                  Services
   |                        |
Telemetry             Remote Runtime
Diagnostics           AI Runtime
Indicators            Workflow Engine
Configuration         Asset Pipeline
Logging               World Builder

Frontends

- Console
- Future HUD
- Future Mobile
- Future Web
- Future VR

Core is always the source of truth.

---

# 4. Engineering Rules

1. Never guess.
2. Request current files before modifying existing code.
3. Deliver complete replacement files.
4. One sprint has one goal.
5. Every sprint finishes with working functionality.
6. Every displayed state must be verifiable.
7. Test → Commit → Push.
8. Update HANDOFF after every completed sprint.
9. Project documentation is written in English.
10. Development discussion is in Polish.

---

# 5. Completed Work

Environment

- Linux development environment
- Git
- VS Code
- Conda
- ComfyUI

Core

- Telemetry
- Diagnostics
- Indicators
- Console foundation
- Workflow foundation

Remote

REMOTE-001 completed.

Verified:

- Tailscale communication
- Remote AI Runtime detection
- ComfyUI detection on port 8188
- Positive ONLINE test
- Negative OFFLINE test

REMOTE-002 completed.

Verified:

- AI Runtime menu added
- AI Runtime Console screen implemented
- RemoteManager integration completed
- Live ComfyUI READY/OFFLINE state verified

Main AI Runtime

Role: AI Runtime

Endpoint: 100.98.198.68

Port: 8188

---

# 6. Current Sprint

BUILD-001

Goal:

Create a fully reproducible Curvature development environment.

Deliverables:

- requirements.txt
- environment.yml
- installation guide

---

# 7. Deferred Work

- Wake-on-LAN
- Curvature Assistant
- HUD
- Marian
- Windows/Linux benchmark

These items are intentionally postponed.

---

# 8. Exact Next Step

BUILD-001

Create:

- requirements.txt
- environment.yml

Verify that a clean machine can recreate the complete development environment.

Next Sprint:

REMOTE-003

Objectives:

- GPU information
- VRAM usage
- Queue status
- Runtime diagnostics

---

# 9. Session End Checklist

Before ending a work session:

- Update HANDOFF.md
- Run tests
- Commit
- Push
- Record the next exact step

A new ChatGPT instance should always read this document first.
