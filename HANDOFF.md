# HANDOFF

Status: Draft
Version: 0.3.0
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
- Dedicated Curvature Conda environment
- Reproducible environment definition
- Pinned Python dependencies
- Installation and verification guide

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

Build

BUILD-001 completed.

Verified:

- Clean Conda environment created from environment.yml
- Python 3.11.15 used
- requirements.txt installed successfully
- pip dependency check passed
- 4 automated telemetry tests passed
- Console started successfully
- System Status screen verified
- System Diagnostics state READY
- Workshop Status screen verified
- Workflow Engine screen verified
- AI Runtime screen verified
- Remote ComfyUI state READY

Main AI Runtime

Role: AI Runtime

Endpoint: 100.98.198.68

Port: 8188

---

# 6. Current Sprint

REMOTE-003

Goal:

Extend AI Runtime diagnostics with verified remote runtime telemetry.

Objectives:

- GPU information
- VRAM usage
- Queue status
- Runtime diagnostics

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

REMOTE-003

Before implementation:

- Read current Remote Runtime files
- Read current AI Runtime Console files
- Identify the existing ComfyUI status request path
- Extend the current verified path without changing architecture

Required current files:

- core/remote/manager.py
- core/remote/workstation.py
- core/remote/__init__.py
- console/runtime.py
- console/menu.py
- console/main.py
- console/ui.py
- related tests

First implementation target:

Display verified remote GPU and VRAM information in the AI Runtime Console screen.

---

# 9. Session End Checklist

Before ending a work session:

- Update HANDOFF.md
- Run tests
- Commit
- Push
- Record the next exact step

A new ChatGPT instance should always read this document first.
