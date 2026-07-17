# HANDOFF

Status: Draft
Version: 0.5.0
Owner: Project Curvature
Last Updated: 2026-07-18

---

# 1. Mission

Project Curvature is a long-term engineering and world-building project.

Curvature Platform is the production workshop.

The final objective is a persistent living world accessible through:

- Chronicle Client / MUD,
- 2D,
- 3D,
- VR,
- future multiplayer and MMORPG scale.

Those frontends must expose the same world state, history, characters and consequences.

---

# 2. Current Priority

Restore and harden remote access to the Main Workstation.

The Main Workstation is physically powered on, but Tailscale device `thing` is offline.

Immediate recovery goals:

- restore Tailscale connectivity,
- identify the actual failure cause,
- prevent recurrence,
- verify remote ComfyUI access.

Working hypothesis:

- Run Unattended may not be enabled,
- the Windows user session may not be logged in,
- Tailscale may therefore not have returned.

This remains unverified.

---

# 3. Strategic Direction

After infrastructure recovery:

1. REMOTE-004 — Minimal Service Heartbeat
2. WORLD-001 — Persistent World State
3. LANG-001 — Historical Reconstruction Foundation
4. WORLD-002 — Time, Events and Chronicle
5. NPC-001 — Identity, Memory, Goals and Voice
6. CHRONICLE-001 — First Playable Chronicle Client

The Chronicle Client / MUD is the first world-facing frontend.

The first version may be single-player.

The language foundation is based on Proto-Slavic reconstruction and the probable early medieval West Slavic and Polan linguistic environment.

Missing language elements must be created through explicit and documented rules.

---

# 4. Current Architecture

Current Platform:

- Core
- Services
- Console
- Remote Runtime
- AI Runtime
- Workflow foundation

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

# 5. Engineering Rules

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

# 6. Completed Work

## BUILD-001

Completed and verified:

- dedicated Curvature Conda environment,
- reproducible environment definition,
- pinned Python dependencies,
- installation guide,
- automated tests,
- Console operation.

## REMOTE-001

Completed and verified:

- Tailscale communication,
- remote workstation abstraction,
- ComfyUI detection.

## REMOTE-002

Completed and verified:

- AI Runtime Console,
- RemoteManager integration,
- live READY and OFFLINE state.

## REMOTE-003

Completed and verified:

- HTTP JSON requests,
- `/system_stats`,
- `/queue`,
- GPU,
- VRAM,
- queue,
- operating system,
- RAM,
- ComfyUI version,
- Python version,
- PyTorch version,
- READY, ATTENTION and OFFLINE state,
- 16 automated tests,
- commit and push.

Verified AI Runtime endpoint:

    http://thing:8188

---

# 7. Current Operational Task

Tailscale Recovery and Resilience

Required verification sequence:

1. Marta logs in to Windows.
2. Observe whether `thing` returns online.
3. Check Tailscale service status.
4. Check service startup type.
5. Verify Run Unattended.
6. Enable it if disabled.
7. Check device key expiry.
8. Verify authentication state.
9. Verify Tailscale Serve.
10. Verify ComfyUI startup.
11. Configure service recovery if required.
12. Add a watchdog only if native recovery is insufficient.
13. Restart Windows.
14. Do not log in.
15. Verify `thing` from Curvature Dev.
16. Verify `/system_stats`.
17. Verify AI Runtime READY.

No Curvature code changes are required during initial diagnosis.

---

# 8. Exact Next Step

From Curvature Dev after Marta logs in:

    tailscale status
    tailscale ping thing
    curl --max-time 5 http://thing:8188/system_stats

Then on the Main Workstation in elevated PowerShell:

    Get-Service Tailscale |
        Select-Object Name, Status, StartType

    tailscale status

Capture the current state before changing recovery, scheduled tasks or watchdog configuration.

---

# 9. Paused and Deferred Work

Paused:

- WOL-001

Deferred:

- S20 FE Wake-on-LAN relay,
- conventional Wake-on-LAN relay,
- hardware validation,
- battery and inverter testing,
- hardware adjustments,
- Curvature Assistant,
- HUD,
- Marian,
- Windows/Linux benchmark.

Hardware validation remains deferred until the user confirms that the inverter is available.

---

# 10. Documentation Structure

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

# 11. Session End Checklist

- Update HANDOFF.md
- Run tests when code changed
- Commit
- Push
- Record the next exact step

A new ChatGPT instance should read HANDOFF.md first.
