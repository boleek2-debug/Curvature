# HANDOFF

Status: Draft Version: 0.1.0 Owner: Project Curvature Last Updated:
2026-07-13

------------------------------------------------------------------------

# 1. Mission

Project Curvature is a long-term engineering project.

The final objective is a fully playable MMORPG and, eventually, an
MMORPGVR world.

Curvature Platform is the production workshop used to build that world.

The workshop is always developed before the game itself.

------------------------------------------------------------------------

# 2. Current Priority

Laptop-side Curvature Platform.

Nothing has higher priority.

Current focus:

-   Curvature Core
-   Console
-   Remote Runtime
-   AI Runtime integration
-   Workflow foundation

Marian is intentionally postponed.

------------------------------------------------------------------------

# 3. Current Architecture

Infrastructure

    Linux
        |

Curvature Platform \| +----+-------------------+ \| \| Core Services \|
\| Telemetry Remote Runtime Diagnostics AI Runtime Indicators Workflow
Engine Asset Pipeline

Frontends

-   Console
-   Future HUD
-   Future Mobile
-   Future Web
-   Future VR

Core is always the source of truth.

------------------------------------------------------------------------

# 4. Engineering Rules

1.  Never guess.
2.  Request current files before modifying existing code.
3.  Deliver complete replacement files.
4.  One sprint has one goal.
5.  Every sprint finishes with working functionality.
6.  Every displayed state must be verifiable.
7.  Test → Commit → Push.
8.  Project documentation is written in English.
9.  Development discussion is in Polish.

------------------------------------------------------------------------

# 5. Completed Work

Environment

-   Linux development environment
-   Git
-   VS Code
-   Conda
-   ComfyUI

Core

-   Telemetry
-   Diagnostics
-   Indicators
-   Console foundation
-   Workflow foundation

Remote

REMOTE-001 completed.

Verified:

-   Tailscale communication
-   Remote AI Runtime detection
-   ComfyUI detection on port 8188
-   Positive ONLINE test
-   Negative OFFLINE test

Main AI Runtime

Role: AI Runtime

Endpoint: 100.98.198.68

Port: 8188

------------------------------------------------------------------------

# 6. Current Sprint

REMOTE-002

Goal:

Add an AI Runtime screen to the Console using the real RemoteManager
state.

------------------------------------------------------------------------

# 7. Deferred Work

-   Wake-on-LAN
-   Curvature Assistant
-   HUD
-   Marian
-   Windows/Linux benchmark

These items are intentionally postponed.

------------------------------------------------------------------------

# 8. Exact Next Step

Request:

console/menu.py

Integrate:

AI Runtime

Display:

Role

Endpoint

ComfyUI status

using:

RemoteManager().comfyui_available()

Never hard-code READY.

------------------------------------------------------------------------

# 9. Session End Checklist

Before ending a work session:

-   Update HANDOFF.md
-   Run tests
-   Commit
-   Push
-   Record the next exact step

A new ChatGPT instance should always read this document first.
