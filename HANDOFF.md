# HANDOFF

Status: Draft
Version: 0.7.0
Owner: Project Curvature
Last Updated: 2026-07-18

---

# 1. Mission

Project Curvature is a long-term engineering and world-building project.

Curvature Platform is the production workshop.

The final objective is a persistent living world accessible through Chronicle Client / MUD, 2D, 3D, VR and future multiplayer scale.

---

# 2. Current Priority

The next software sprint is:

WORLD-002 — Time, Events and Chronicle

Completed and verified:

- WORLD-001 — Persistent World State
- LANG-001 — Historical Reconstruction Foundation
- 36 automated project tests passed
- commit and push completed

The Main Workstation is currently reachable through Tailscale and ComfyUI.

---

# 3. Completed Living World Foundations

## WORLD-001

- persistent world identifier
- Place and Entity models
- authoritative WorldState
- controlled state transitions
- versioned JSON storage
- load after restart
- automated tests

## LANG-001

- language form classifications
- confidence levels
- provenance model
- LanguageEntry
- versioned Lexicon
- JSON lexicon storage
- validation separating evidence from invention
- automated tests

Curvature Research owns scientific sources, reconstructions, competing hypotheses and confidence assessments.

Curvature Core owns data structures, validation, persistence and integration.

---

# 4. Exact Next Step

Begin WORLD-002 planning.

Required deliverables:

- world time
- verified events
- cause and effect links
- persistent Chronicle entries
- restart continuity
- automated tests

Before implementation, inspect the current:

- `core/world/state.py`
- `core/world/storage.py`
- `core/world/__init__.py`
- `core/events/__init__.py`
- `tests/test_world.py`
- `CHRONICLE`

Do not design from assumed file state.

---

# 5. Chronicle Principle

`CHRONICLE` is the persistent record of events in the world.

It is not a technical log and not a free-form AI story.

The design must distinguish:

- what objectively happened
- who witnessed it
- who learned about it
- how information spread
- how accounts changed
- how events are narrated

WORLD-002 begins with authoritative facts, ordered time, cause and effect, and persistent Chronicle entries.

---

# 6. Strategic Direction

1. WORLD-002 — Time, Events and Chronicle
2. NPC-001 — Identity, Memory, Goals and Voice
3. CHRONICLE-001 — First Playable Chronicle Client
4. expand World Core and Platform together
5. 2D
6. 3D
7. VR
8. multiplayer and MMORPG scale

---

# 7. ASSISTANT-001 Status

ASSISTANT-001 — Curvature Console MVP is officially approved as a future developer tool.

It is not part of Curvature Platform and not part of gameplay.

Purpose:

- persistent role-based AI workspaces
- automatic context loading
- department separation
- immediate readiness for Curvature Project, Curvature Core and Curvature Research

Status:

Approved for future implementation.

It must not interrupt WORLD-002.

The first future step is architecture and technology evaluation at a safe stopping point.

---

# 8. Infrastructure Incident Status

Remote access is currently restored.

The earlier outage is not fully diagnosed.

Most likely explanation:

- Windows Update or another event restarted the workstation
- GRUB booted Linux Mint
- Windows, Tailscale and ComfyUI therefore remained unavailable

This remains plausible, not verified.

Remaining physical-access tasks:

- set Windows as the default GRUB entry
- verify Tailscale service and Run Unattended
- check key expiry
- verify Tailscale Serve after restart
- configure ComfyUI autostart
- install remote desktop
- perform a controlled restart without login
- configure recovery or watchdog only if needed

Do not restart remotely while GRUB defaults to Mint and nobody is physically present.

---

# 9. Engineering Rules

1. Never guess.
2. Request current files before modifying uncertain code.
3. Deliver complete replacement files.
4. Label every file as replace, create or leave unchanged.
5. One sprint has one goal.
6. Every sprint finishes with working functionality.
7. Every displayed state must be verifiable.
8. Test → Commit → Push.
9. Update HANDOFF after completed work.
10. Documentation is written in English.
11. Development discussion is in Polish.

---

# 10. Paused and Deferred Work

Paused:

- WOL-001
- full restart verification until safe physical access

Deferred:

- S20 FE Wake-on-LAN relay
- conventional Wake-on-LAN relay
- hardware validation
- battery and inverter testing
- HUD
- Marian
- Windows/Linux benchmark

Hardware validation remains deferred until the inverter is confirmed available.

---

# 11. Session End Checklist

- Update HANDOFF.md
- Run tests when code changed
- Commit
- Push
- Record the next exact step

A new Curvature Core session should read HANDOFF.md first.
