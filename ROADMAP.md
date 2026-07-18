# ROADMAP

Status: Draft
Version: 0.7.0
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

Transition from Curvature Platform Foundation to Living World Foundation

Most recently completed sprint

LANG-001 — Historical Reconstruction Foundation

Current verified remote state

- endpoint `thing` resolves
- port `8188` is online
- ComfyUI API is READY
- AI Runtime Heartbeat is READY
- current and last successful verification timestamps are displayed
- 36 automated project tests pass
- WORLD-001 verified
- LANG-001 verified

Next software sprint

WORLD-002 — Time, Events and Chronicle

---

# Strategic Direction

Curvature will now move from the minimum reliable workshop into an early living-world vertical slice.

The workshop will not be expanded indefinitely before the world begins.

Approved progression:

1. create persistent world state
2. establish the historical language foundation
3. add time, events and Chronicle
4. add character identity, memory, goals and voice
5. create the first playable Chronicle Client / MUD
6. expand the Platform and world together
7. add 2D
8. add 3D
9. add VR
10. grow toward multiplayer and MMORPG scale

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
- REMOTE-004 completed
- endpoint resolution state
- ComfyUI port state
- ComfyUI API state
- Heartbeat READY, ATTENTION and OFFLINE states
- current verification timestamp
- last successful verification timestamp
- failure transition handling
- automated Remote Runtime and heartbeat tests
- 21 automated project tests passed

---

# Completed Living World Milestones

## WORLD-001 — Persistent World State

Goal

Create the minimum authoritative World Core.

Required deliverables

- persistent world identifier
- one place
- basic entities
- state storage
- load after restart
- verified state transitions
- automated tests

Scope rule

WORLD-001 must remain small.

It must prove authoritative persistence before adding:

- Chronicle
- NPC intelligence
- language interpretation
- multiplayer
- graphical frontends
- large-scale procedural generation

---

## LANG-001 — Historical Reconstruction Foundation

Goal

Create a trustworthy method for reconstructing and extending the world's language.

Required deliverables

- provenance model
- confidence categories
- Proto-Slavic research structure
- early West Slavic and Polan reference framework
- initial phonological assumptions
- controlled construction rules
- small initial lexicon
- naming rules

---

# Active Software Milestone

## WORLD-002 — Time, Events and Chronicle

Goal

Give the world ordered history and durable consequence.

Required deliverables

- world time
- verified events
- cause and effect links
- persistent Chronicle entries
- restart continuity
- automated tests

---

## NPC-001 — Identity, Memory, Goals and Voice

Goal

Create characters that persist as world entities.

Required deliverables

- identity
- knowledge
- memory
- goals
- relationships
- cultural profile
- linguistic profile
- recognisable voice constraints

---

## CHRONICLE-001 — First Playable Chronicle Client

Goal

Create the first world-facing frontend.

Required vertical slice

- one persistent place
- several characters
- natural-language player intent
- verified world actions
- memory
- consequences
- Chronicle output
- restart continuity

The first version may be single-player.

It is the first proof that the living world exists.

---

# Approved Developer Tooling

## ASSISTANT-001 — Curvature Console MVP

Purpose

Create an internal development client with permanent workspaces for:

- Curvature Project
- Curvature Core
- Curvature Research

Each workspace automatically loads its role, documentation and current state.

Status

Approved for future implementation.

Priority

High — Developer Tooling

Scheduling rule

Do not interrupt WORLD-002 or another active sprint.

The first future milestone is architecture and technology evaluation at a safe stopping point.

Required planning deliverables

- architecture proposal
- technology evaluation
- implementation roadmap
- estimated development effort
- repository structure
- MVP specification

Curvature Console is not part of Curvature Platform and not part of gameplay.

---

# Infrastructure Hardening

## Main Workstation Recovery and Restart Safety

Current condition

Remote access is restored, but the original outage is not fully diagnosed.

Likely operational explanation

A restart may have caused GRUB to boot Linux Mint instead of Windows.

This remains a working explanation, not a verified root cause.

Required physical-access tasks

- set Windows as the default GRUB entry
- verify Tailscale Windows service status and startup type
- verify Run Unattended
- check device key expiry
- verify Tailscale Serve after restart
- configure ComfyUI autostart
- install a remote desktop path
- perform a controlled restart without login
- configure native service recovery if required
- add a watchdog only if required

Safety rule

Do not remotely restart the workstation while GRUB still defaults to Mint and nobody is physically present.

This infrastructure work must be completed when safe physical access is available, but it does not block WORLD-001 while the current remote runtime remains available.

---

# Later Milestones

## Language Development

- expanded lexicon
- grammar growth
- dialects
- language evolution
- ritual and social registers
- translated and original dialogue

## World Development

- additional places
- expanded characters
- economy
- conflict
- travel
- cultures
- larger histories

## Frontend Progression

- 2D client
- 3D client
- VR client

## Multiplayer Progression

- networking
- shared world rules
- concurrency
- multiplayer systems
- MMORPG scale

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

- battery health
- full-shutdown self-discharge
- real runtime
- peak-load stability
- vehicle AC or inverter compatibility
- full Curvature mission
- suspend and sleep behaviour

Status

Deferred until the user confirms that the inverter is available.

It must not interrupt the software roadmap before that confirmation.

---

# Notes

Only completed work belongs in CHANGELOG.

Ideas intentionally postponed belong in PIPELINE.

Living World, Language and Chronicle are core roadmap items, not Pipeline ideas.
