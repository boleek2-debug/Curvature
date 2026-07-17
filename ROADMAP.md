# ROADMAP

Status: Draft
Version: 0.5.0
Owner: Project Curvature
Last Updated: 2026-07-18

---

# Purpose

This roadmap describes the planned evolution of Project Curvature.

It shows where the project is today and the intended order of development.

It is not a changelog.

---

# Current Position

Current Development Phase

Curvature Platform Foundation

Current Operational Priority

Tailscale Recovery and Resilience

Objective

Restore reliable unattended access to the Main Workstation and prevent another loss of the remote Tailscale path.

Current remote condition

- Main Workstation physically powered on
- Tailscale device `thing` offline
- Remote ComfyUI unavailable because the Tailscale path is down

Current working hypothesis

Run Unattended may not be enabled.

This has not yet been verified.

Most recently completed sprint

REMOTE-003

Next software sprint

REMOTE-004 — Minimal Service Heartbeat

---

# Strategic Direction

Curvature will move from a reliable minimum workshop into an early living-world vertical slice.

The workshop will not be expanded indefinitely before the world begins.

Approved progression:

1. restore infrastructure reliability,
2. complete a minimal heartbeat,
3. create persistent world state,
4. establish the historical language foundation,
5. add time, events and Chronicle,
6. add character identity, memory, goals and voice,
7. create the first playable Chronicle Client / MUD,
8. expand the Platform and world together,
9. add 2D,
10. add 3D,
11. add VR,
12. grow toward multiplayer and MMORPG scale.

---

# Completed Milestones

## Foundation

- Linux development environment
- Git repository
- VS Code workspace
- Conda environment
- ComfyUI environment
- BUILD-001 completed
- Dedicated Curvature environment
- Reproducible environment definition
- Pinned Python dependencies
- Installation and verification guide

## Curvature Core

- Telemetry
- Diagnostics
- Indicators
- Console foundation

## Workflow

- Workflow registry
- Workflow states

## Remote

- REMOTE-001 completed
- Tailscale integration
- Remote AI Runtime detection
- ComfyUI service verification
- REMOTE-002 completed
- AI Runtime Console
- RemoteManager integration
- Live ComfyUI status
- REMOTE-003 completed
- Remote GPU information
- Remote VRAM usage
- Queue monitoring
- Remote operating system information
- Remote RAM usage
- ComfyUI version diagnostics
- Remote Python version diagnostics
- Remote PyTorch version diagnostics
- Automated Remote Runtime tests

---

# Active Operational Milestone

## Tailscale Recovery and Resilience

Goal

Make remote access to the Main Workstation reliable without requiring an interactive Windows login.

Required deliverables

- login-response diagnostic,
- Tailscale service status verification,
- automatic service startup verification,
- Run Unattended verification and configuration,
- device key expiry verification,
- Tailscale authentication verification,
- Tailscale Serve restart verification,
- ComfyUI startup verification,
- Windows service recovery configuration if required,
- watchdog only if required,
- full restart test without login,
- remote `thing` availability confirmation,
- remote `/system_stats` confirmation,
- Curvature AI Runtime READY confirmation.

---

# Near-Term Software Milestones

## REMOTE-004 — Minimal Service Heartbeat

Goal

Provide a small, reliable and verifiable heartbeat for the Main Workstation and remote AI Runtime.

Required deliverables

- host reachability state,
- Tailscale path state,
- ComfyUI API state,
- last successful verification time,
- failure transition handling,
- automated tests.

Scope rule

REMOTE-004 must remain small.

It must not delay the first World Core work through unnecessary infrastructure expansion.

---

## WORLD-001 — Persistent World State

Goal

Create the minimum authoritative World Core.

Required deliverables

- persistent world identifier,
- one place,
- basic entities,
- state storage,
- load after restart,
- verified state transitions,
- automated tests.

---

## LANG-001 — Historical Reconstruction Foundation

Goal

Create a trustworthy method for reconstructing and extending the world's language.

Required deliverables

- provenance model,
- confidence categories,
- Proto-Slavic research structure,
- early West Slavic and Polan reference framework,
- initial phonological assumptions,
- controlled construction rules,
- small initial lexicon,
- naming rules.

---

## WORLD-002 — Time, Events and Chronicle

Goal

Give the world ordered history and durable consequence.

Required deliverables

- world time,
- verified events,
- cause and effect links,
- persistent Chronicle entries,
- restart continuity,
- automated tests.

---

## NPC-001 — Identity, Memory, Goals and Voice

Goal

Create characters that persist as world entities.

Required deliverables

- identity,
- knowledge,
- memory,
- goals,
- relationships,
- cultural profile,
- linguistic profile,
- recognisable voice constraints.

---

## CHRONICLE-001 — First Playable Chronicle Client

Goal

Create the first world-facing frontend.

Required vertical slice

- one persistent place,
- several characters,
- natural-language player intent,
- verified world actions,
- memory,
- consequences,
- Chronicle output,
- restart continuity.

The first version may be single-player.

It is the first proof that the living world exists.

---

# Later Milestones

## Language Development

- expanded lexicon,
- grammar growth,
- dialects,
- language evolution,
- ritual and social registers,
- translated and original dialogue.

## World Development

- additional places,
- expanded characters,
- economy,
- conflict,
- travel,
- cultures,
- larger histories.

## Frontend Progression

- 2D client,
- 3D client,
- VR client.

## Multiplayer Progression

- networking,
- shared world rules,
- concurrency,
- multiplayer systems,
- MMORPG scale.

---

# Paused Milestone

## WOL-001 — Wake-on-LAN

Verified preparation

- ASUS PRIME Z490M-PLUS identified
- Intel I219-V identified
- wired Ethernet verified
- MAC address recorded
- Wake on Magic Packet enabled
- Windows wake permission enabled
- Fast Startup not blocking Wake-on-LAN

Status

Paused until after the trip.

The planned S20 FE relay remains in PIPELINE.

---

# Deferred Hardware Validation

Curvature hardware validation includes:

- battery health,
- full-shutdown self-discharge,
- real runtime,
- peak-load stability,
- vehicle AC or inverter compatibility,
- full Curvature mission,
- suspend and sleep behaviour.

Status

Deferred until the user confirms that the inverter is available.

It must not interrupt the software roadmap before that confirmation.

---

# Notes

Only completed work belongs in CHANGELOG.

Ideas intentionally postponed belong in PIPELINE.

Living World, Language and Chronicle are now core roadmap items, not Pipeline ideas.
