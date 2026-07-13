# HANDOFF

Status: Draft
Version: 0.4.0
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

Build

BUILD-001 completed.

Verified:

- Clean Conda environment created from environment.yml
- Python 3.11.15 used
- requirements.txt installed successfully
- pip dependency check passed
- Console started successfully
- System Status screen verified
- System Diagnostics state READY
- Workshop Status screen verified
- Workflow Engine screen verified
- AI Runtime screen verified

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

REMOTE-003 completed.

Implemented:

- HTTP JSON requests through Workstation
- ComfyUI /system_stats integration
- ComfyUI /queue integration
- Remote GPU information
- Remote VRAM usage
- Remote queue monitoring
- Remote operating system information
- Remote RAM usage
- ComfyUI version
- Remote Python version
- Remote PyTorch version
- ATTENTION state when the service port is reachable but runtime diagnostics are unavailable
- Automated Remote Runtime tests

Verified:

- Tailscale Serve hostname routing
- Verified endpoint: thing:8188
- ComfyUI /system_stats returned HTTP 200 and valid JSON
- ComfyUI /queue returned HTTP 200 and valid JSON
- NVIDIA GeForce RTX 4060 detected
- Live VRAM values displayed
- Live queue values displayed
- Windows runtime information displayed
- Live RAM values displayed
- ComfyUI 0.26.2 displayed
- Python 3.13.12 displayed
- PyTorch 2.10.0+cu130 displayed
- Console AI Runtime state READY
- 16 automated tests passed

Main AI Runtime

Name: Main Workstation

Role: AI Runtime

Tailscale hostname: thing

Verified service endpoint: http://thing:8188

ComfyUI system statistics endpoint: /system_stats

ComfyUI queue endpoint: /queue

---

# 6. Current Sprint

REMOTE-003 closure

Status:

Implementation and verification complete.

Remaining actions:

- Update project documentation
- Run final tests
- Commit
- Push

No new sprint has been started.

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

Complete REMOTE-003 repository closure.

Required sequence:

1. Replace HANDOFF.md, CHANGELOG.md and ROADMAP.md with the completed versions.
2. Run the complete automated test suite.
3. Verify that all 16 tests pass.
4. Review git status.
5. Commit the REMOTE-003 implementation and documentation.
6. Push the commit to origin/main.
7. Select the next sprint from the existing Roadmap without changing architecture during the closure step.

Files expected in the REMOTE-003 commit:

- console/runtime.py
- core/remote/__init__.py
- core/remote/manager.py
- core/remote/workstation.py
- tests/test_remote.py
- HANDOFF.md
- CHANGELOG.md
- ROADMAP.md

---

# 9. Session End Checklist

Before ending a work session:

- Update HANDOFF.md
- Run tests
- Commit
- Push
- Record the next exact step

A new ChatGPT instance should always read this document first.
