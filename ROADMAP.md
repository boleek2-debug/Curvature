# ROADMAP

Status: Draft
Version: 0.4.1
Owner: Project Curvature
Last Updated: 2026-07-13

---

# Purpose

This roadmap describes the planned evolution of Project Curvature.

It shows where the project is today and the intended direction of development.

It is not a changelog.

---

# Current Position

Current Development Phase

Curvature Platform Foundation

Current Sprint

WOL-001

Objective

Enable reliable remote startup of the Main Workstation before Wednesday for an eight-day period of remote use.

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

# Active Milestone

## WOL-001 — Wake-on-LAN

Goal

Allow the Main Workstation to be powered on remotely through a verified home-LAN relay reachable over Tailscale.

Required deliverables

- BIOS/UEFI Wake-on-LAN verification
- Windows network adapter configuration
- Fast Startup verification
- Wired Ethernet verification
- Local Wake-on-LAN test
- Home-LAN relay identification
- Tailscale relay verification
- Remote Wake-on-LAN test
- Startup confirmation
- ComfyUI availability confirmation after wake

Priority

Immediate.

Deadline

Before Wednesday.

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

WOL-001 temporarily takes priority over REMOTE-004 because remote startup is operationally required before Wednesday.
