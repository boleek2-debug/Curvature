# HANDOFF

Status: Draft
Version: 0.6.0
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

Those frontends must expose the same world state, history, characters and consequences.

---

# 2. Current Priority

The next software sprint is:

WORLD-001 — Persistent World State

REMOTE-004 is complete and verified.

The Main Workstation is currently reachable again through Tailscale and ComfyUI.

Verified current remote state:

- endpoint `thing` resolves
- Tailscale connectivity is available
- port `8188` is online
- `/system_stats` is available
- AI Runtime Heartbeat is READY
- ComfyUI runtime diagnostics are available

---

# 3. Infrastructure Incident Status

The earlier loss of remote access is not fully diagnosed.

Observed sequence:

- Main Workstation remained physically powered on
- Tailscale device `thing` became unavailable
- Windows was later started and the user logged in
- Tailscale returned online
- ComfyUI was started
- remote API access returned

Most likely operational explanation:

- Windows Update or another event restarted the workstation
- GRUB booted Linux Mint because Mint is the current default
- Windows, Windows Tailscale and ComfyUI therefore remained unavailable

This explanation is plausible but not fully verified.

Do not record Tailscale itself as the confirmed root cause.

Remaining physical-access tasks:

- set Windows as the default GRUB entry
- verify Tailscale Windows service status and startup type
- verify Run Unattended
- check device key expiry
- verify Tailscale Serve after restart
- configure ComfyUI autostart
- install and verify a remote desktop path
- perform a controlled restart without login
- configure native service recovery if required
- add a watchdog only if native recovery is insufficient

Do not restart the workstation remotely while GRUB still defaults to Mint and nobody is physically present.

---

# 4. Strategic Direction

Approved development order:

1. WORLD-001 — Persistent World State
2. LANG-001 — Historical Reconstruction Foundation
3. WORLD-002 — Time, Events and Chronicle
4. NPC-001 — Identity, Memory, Goals and Voice
5. CHRONICLE-001 — First Playable Chronicle Client

The Chronicle Client / MUD is the first world-facing frontend.

The first version may be single-player.

The language foundation is based on Proto-Slavic reconstruction and the probable early medieval West Slavic and Polan linguistic environment.

Missing language elements must be created through explicit and documented rules.

---

# 5. Current Architecture

Current Platform:

- Core
- Services
- Console
- Remote Runtime
- AI Runtime
- Workflow foundation
- Minimal Service Heartbeat

Approved planned architecture:

- World Core
- Persistent World State
- Time
- Events
- Chronicle
- Characters
- Memory
- Language
- Consequences
- Chronicle Client / MUD
- later 2D, 3D and VR frontends

Core remains the source of truth for platform state.

World Core will become the source of truth for world state.

---

# 6. Engineering Rules

1. Never guess.
2. Request current files before modifying existing code when their state is uncertain.
3. Deliver complete replacement files.
4. Label every delivered file as replace, create or leave unchanged.
5. One sprint has one goal.
6. Every sprint finishes with working functionality.
7. Every displayed state must be verifiable.
8. Test → Commit → Push.
9. Update HANDOFF after completed work.
10. Project documentation is written in English.
11. Development discussion is in Polish.

---

# 7. Completed Work

## BUILD-001

Completed and verified:

- dedicated Curvature Conda environment
- reproducible environment definition
- pinned Python dependencies
- installation guide
- automated tests
- Console operation

## REMOTE-001

Completed and verified:

- Tailscale communication
- remote workstation abstraction
- ComfyUI detection

## REMOTE-002

Completed and verified:

- AI Runtime Console
- RemoteManager integration
- live READY and OFFLINE state

## REMOTE-003

Completed and verified:

- HTTP JSON requests
- `/system_stats`
- `/queue`
- GPU
- VRAM
- queue
- operating system
- RAM
- ComfyUI version
- Python version
- PyTorch version
- READY, ATTENTION and OFFLINE state
- 16 automated tests
- commit and push

## REMOTE-004

Completed and verified:

- endpoint resolution state
- ComfyUI port state
- ComfyUI API state
- READY, ATTENTION and OFFLINE heartbeat
- current check timestamp
- last successful check timestamp
- last successful timestamp preserved after failure
- AI Runtime Console heartbeat display
- 21 automated project tests passed
- live verification against `thing`
- endpoint RESOLVED
- port `8188` ONLINE
- API READY
- Heartbeat READY

Verified AI Runtime endpoint:

    http://thing:8188

---

# 8. Exact Next Step

Complete the REMOTE-004 repository closeout:

1. Replace `CHANGELOG.md`, `HANDOFF.md` and `ROADMAP.md`.
2. Review staged changes.
3. Commit.
4. Push to `origin/main`.

Then begin WORLD-001 planning.

Before modifying code for WORLD-001, inspect the current repository structure and request the current files that will own:

- world identity
- persistence
- storage
- state transitions
- tests

Do not design implementation from assumed file paths.

---

# 9. WORLD-001 Objective

Create the minimum authoritative World Core.

Required deliverables:

- persistent world identifier
- one place
- basic entities
- state storage
- load after restart
- verified state transitions
- automated tests

The first implementation should remain deliberately small.

It must prove persistence and authoritative state without prematurely adding Chronicle, NPC intelligence, language processing or networking.

---

# 10. Paused and Deferred Work

Paused:

- WOL-001
- full Tailscale recovery and restart verification until physical access is safe

Deferred:

- S20 FE Wake-on-LAN relay
- conventional Wake-on-LAN relay
- hardware validation
- battery and inverter testing
- hardware adjustments
- Curvature Assistant
- HUD
- Marian
- Windows/Linux benchmark

Hardware validation remains deferred until the user confirms that the inverter is available.

---

# 11. Documentation Structure

- `CURVATURE.md` — project vision and philosophy
- `BLUEPRINT.md` — current and approved technical architecture
- `WORLD.md` — persistent living-world principles
- `LANGUAGE.md` — reconstruction and language-construction method
- `ROADMAP.md` — ordered development direction
- `HANDOFF.md` — current operational state and exact next step
- `PIPELINE.md` — deferred ideas only
- `CHANGELOG.md` — completed and verified work
- `README.md` — repository overview and usage

---

# 12. Session End Checklist

- Update HANDOFF.md
- Run tests when code changed
- Commit
- Push
- Record the next exact step

A new ChatGPT instance should read HANDOFF.md first.
