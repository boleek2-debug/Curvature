# ROADMAP

Status: Draft
Version: 0.4.2
Owner: Project Curvature
Last Updated: 2026-07-16

---

# Purpose

This roadmap describes the planned evolution of Project Curvature.

It shows where the project is today and the intended direction of development.

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

Next software sprint

REMOTE-004 Service Heartbeat

Most recently completed sprint

REMOTE-003

Completed objective

Extend AI Runtime diagnostics with verified remote GPU information, VRAM usage, queue status and runtime diagnostics.

---

# Completed Milestones

Foundation

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

Curvature Core

- Telemetry
- Diagnostics
- Indicators
- Console foundation

Workflow

- Workflow registry
- Workflow states

Remote

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

- Login-response diagnostic
- Tailscale service status verification
- Automatic service startup verification
- Run Unattended verification and configuration
- Device key expiry verification
- Tailscale authentication verification
- Tailscale Serve restart verification
- ComfyUI startup verification
- Windows service recovery configuration if required
- Watchdog only if required
- Full restart test without login
- Remote `thing` availability confirmation
- Remote `/system_stats` confirmation
- Curvature AI Runtime READY confirmation

Target work session

Saturday, 2026-07-18.

---

# Paused Milestone

## WOL-001 — Wake-on-LAN

Goal

Allow the Main Workstation to be powered on remotely through a verified home-LAN relay reachable over Tailscale.

Verified preparation

- ASUS PRIME Z490M-PLUS identified
- Intel I219-V identified
- Wired Ethernet verified
- MAC address recorded
- Wake on Magic Packet enabled
- Windows wake permission enabled
- Fast Startup not blocking Wake-on-LAN

Blocked deliverables

- BIOS/UEFI Wake-on-LAN verification
- Local Wake-on-LAN test
- Home-LAN relay implementation
- Tailscale relay verification
- Remote Wake-on-LAN test
- Startup confirmation
- ComfyUI availability confirmation after wake

Status

Paused until after the trip.

The planned S20 FE relay remains in PIPELINE.

---

# Planned Milestones

Remote Runtime

- REMOTE-004 Service Heartbeat
- Remote commands

Workflow Engine

- Dependency verification
- Workflow execution
- Progress reporting
- History

Curvature Interface

- HUD foundation
- Slavic 24th-century design language
- Integrated Console

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

Hardware validation must not interrupt Tailscale recovery or the existing software roadmap before that confirmation.

---

# Long-Term Goals

World Production

- World Builder
- Character production
- Environment production
- Asset production

Game Production

- Game engine integration
- Networking
- Multiplayer systems

Final Objective

A complete MMORPG.

Future Objective

A complete MMORPGVR world.

---

# Notes

Only completed work belongs in CHANGELOG.

Ideas that are intentionally postponed belong in PIPELINE.

Infrastructure recovery takes priority over REMOTE-004 because the remote AI Runtime cannot currently be reached.
