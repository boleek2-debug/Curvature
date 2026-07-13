# HANDOFF

Status: Draft
Version: 0.4.1
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

Wake-on-LAN for the Main Workstation.

This is the immediate operational priority.

Reason:

- Wake-on-LAN must be ready before Wednesday.
- Remote access will be required during an eight-day trip.
- The Main Workstation must be startable remotely before further Remote Runtime work continues.

Current platform focus remains:

- Curvature Core
- Console
- Remote Runtime
- AI Runtime integration
- Workflow foundation

Marian remains intentionally postponed.

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

The current Wake-on-LAN task does not change this architecture.

---

# 4. Engineering Rules

1. Never guess.
2. Request current files before modifying existing code when their state is uncertain.
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
- Commit completed
- Push to origin/main completed

Main AI Runtime

Name: Main Workstation

Role: AI Runtime

Tailscale hostname: thing

Verified service endpoint: http://thing:8188

ComfyUI system statistics endpoint: /system_stats

ComfyUI queue endpoint: /queue

---

# 6. Current Sprint

WOL-001

Goal:

Enable reliable remote startup of the Main Workstation before Wednesday.

Required outcome:

- Main Workstation can be powered on remotely while the operator is away from the home network.
- Wake request can travel through a verified Tailscale-connected relay on the home LAN.
- Startup is confirmed by a verifiable online or service state.

---

# 7. WOL-001 Scope

Required verification:

- Main Workstation uses a wired Ethernet connection
- Motherboard BIOS/UEFI Wake-on-LAN support
- Windows network adapter Wake-on-LAN settings
- Wake on Magic Packet
- Power management settings
- Windows Fast Startup state
- Network adapter MAC address
- Local Wake-on-LAN test
- Availability of an always-on device inside the home LAN
- Tailscale connectivity of the relay device
- Remote Wake-on-LAN test from outside the home LAN
- Main Workstation startup confirmation
- ComfyUI availability confirmation after startup

Implementation must not begin by guessing the relay device or network path.

---

# 8. Deferred Work

- REMOTE-004 Service Heartbeat
- Remote commands
- Curvature Assistant
- HUD
- Marian
- Windows/Linux benchmark

These items remain intentionally postponed until WOL-001 is complete.

---

# 9. Exact Next Step

Start WOL-001 with infrastructure verification.

On the Main Workstation verify:

1. Current motherboard or computer model.
2. BIOS/UEFI Wake-on-LAN settings.
3. Windows network adapter name.
4. Wake-on-LAN advanced properties.
5. Power management properties.
6. Windows Fast Startup state.
7. Wired Ethernet link.
8. Active IPv4 address.
9. Physical MAC address.

Then identify an always-on device on the same home LAN that can:

- remain powered while the Main Workstation is off,
- connect to the home Ethernet or Wi-Fi network,
- connect to Tailscale,
- send a Wake-on-LAN magic packet inside the home LAN.

No Curvature code changes are required until the Wake-on-LAN network path is verified manually.

---

# 10. Session End Checklist

Before ending a work session:

- Update HANDOFF.md
- Run tests when code changed
- Commit
- Push
- Record the next exact step

A new ChatGPT instance should always read this document first.
