# HANDOFF

Status: Draft
Version: 0.4.2
Owner: Project Curvature
Last Updated: 2026-07-16

---

# 1. Mission

Project Curvature is a long-term engineering project.

The final objective is a fully playable MMORPG and, eventually, an MMORPGVR world.

Curvature Platform is the production workshop used to build that world.

The workshop is always developed before the game itself.

---

# 2. Current Priority

Restore and harden remote access to the Main Workstation.

The Main Workstation is physically powered on, but its Tailscale device `thing` is currently offline.

The immediate priority for Saturday is:

- restore Tailscale connectivity,
- identify the actual failure cause,
- prevent the same failure from recurring,
- verify remote ComfyUI access again.

Current working hypothesis:

- Tailscale Run Unattended may not be enabled,
- the Windows user session may not currently be logged in,
- Tailscale may therefore not have returned after restart or session loss.

This hypothesis is not yet verified.

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

The current Tailscale recovery task does not change this architecture.

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

Expected service endpoint: http://thing:8188

ComfyUI system statistics endpoint: /system_stats

ComfyUI queue endpoint: /queue

Current remote state:

- Main Workstation physically powered on
- Tailscale device `thing` offline
- Last observed Tailscale state: offline
- ComfyUI unreachable remotely because the Tailscale path is unavailable

---

# 6. Current Operational Task

Tailscale Recovery and Resilience

Goal:

Restore reliable unattended remote access to the Main Workstation.

Required outcome:

- `thing` returns online,
- Tailscale works before Windows user login,
- Tailscale survives a restart,
- Tailscale Serve returns automatically,
- ComfyUI becomes remotely reachable again,
- a recurring failure is detected or recovered automatically.

No new Curvature implementation sprint has started.

REMOTE-004 remains the next software sprint after infrastructure recovery.

---

# 7. Saturday Recovery Scope

Required verification sequence:

1. Have Marta log in to Windows.
2. Observe whether `thing` immediately returns online.
3. Check the Windows Tailscale service status.
4. Check the Tailscale service startup type.
5. Verify whether Run Unattended is enabled.
6. Enable Run Unattended if it is disabled.
7. Check device key expiry for `thing`.
8. Verify current Tailscale authentication state.
9. Verify Tailscale Serve configuration.
10. Verify whether Tailscale Serve returns after restart.
11. Verify ComfyUI startup behaviour.
12. Configure Tailscale service recovery if required.
13. Add a watchdog only if service recovery is insufficient.
14. Perform a full Windows restart.
15. Do not log in.
16. Verify from Curvature Dev that `thing` returns online.
17. Verify `http://thing:8188/system_stats`.
18. Verify AI Runtime state READY in Curvature Console.

The initial login test is diagnostic.

If logging in causes `thing` to return online immediately, this strongly supports the Run Unattended hypothesis, but the remaining checks must still be completed.

---

# 8. Wake-on-LAN Status

WOL-001 is not complete.

Verified:

- Main Workstation motherboard: ASUS PRIME Z490M-PLUS
- Network adapter: Intel I219-V
- Wired Ethernet connection
- MAC address: D4-5D-64-27-5E-9B
- Wake on Magic Packet enabled
- Windows wake permission enabled
- Fast Startup unavailable and not blocking Wake-on-LAN

Blocked:

- no configured always-on home-LAN relay,
- no completed local Wake-on-LAN test,
- no completed remote Wake-on-LAN test.

Decision:

- S20 FE relay implementation is deferred until after the trip.
- The Main Workstation was intended to remain powered on during the trip.
- Tailscale resilience must be fixed before relying on this operational model again.

---

# 9. Deferred Work

- WOL-001 completion
- S20 FE Wake-on-LAN relay
- REMOTE-004 Service Heartbeat
- Remote commands
- Curvature hardware validation
- Battery and inverter testing
- Curvature Assistant
- HUD
- Marian
- Windows/Linux benchmark

Hardware validation, battery testing and resulting hardware changes remain deferred until the user confirms that the inverter is available.

---

# 10. Exact Next Step

On Saturday, begin with the Main Workstation Windows session.

First diagnostic:

1. Marta logs in to Windows.
2. From Curvature Dev run:

       tailscale status
       tailscale ping thing
       curl --max-time 5 http://thing:8188/system_stats

3. Record whether `thing` returns online immediately after login.

Then inspect the Main Workstation using an elevated PowerShell session:

    Get-Service Tailscale |
        Select-Object Name, Status, StartType

    tailscale status

Do not change service recovery, scheduled tasks or watchdog configuration until the current state is captured.

No Curvature code changes are required during the initial recovery diagnosis.

---

# 11. Session End Checklist

Before ending a work session:

- Update HANDOFF.md
- Run tests when code changed
- Commit
- Push
- Record the next exact step

A new ChatGPT instance should always read this document first.
