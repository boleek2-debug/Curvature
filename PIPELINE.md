# PIPELINE

Status: Draft
Version: 0.5.0
Owner: Project Curvature
Last Updated: 2026-07-18

---

# Purpose

The Pipeline stores valuable ideas that are intentionally postponed.

Items in this document must not interrupt the current operational task or software sprint.

Only when an item is promoted does it move into the Roadmap.

Living World, historical language construction and Chronicle Client are no longer Pipeline items.

They are part of the main Roadmap.

---

# Infrastructure

## Curvature Hardware Validation Pipeline

Purpose

Create a standard validation process for development laptops and workstations used by Project Curvature.

Planned documentation

Create a dedicated root-level document:

    HARDWARE_VALIDATION.md

Planned validation scope

- Battery health check
- Full-shutdown self-discharge test
- Real runtime test
- Peak-load battery stability test
- AC and inverter compatibility test
- Full Curvature development mission test
- Suspend and sleep behaviour test

Activation condition

Do not promote or schedule hardware validation until the user explicitly confirms that the inverter is available.

Status

Deferred pending inverter confirmation.

---

## S20 FE Wake-on-LAN Relay

Purpose

Use the retired Samsung Galaxy S20 FE as an always-on Wake-on-LAN relay for the Main Workstation.

Planned topology

    Remote Operator Device
        |
    Tailscale
        |
    Samsung Galaxy S20 FE
        |
    Home Wi-Fi
        |
    Wake-on-LAN Magic Packet
        |
    Main Workstation

Required configuration

- permanent home Wi-Fi,
- permanent charger connection,
- Tailscale,
- Termux,
- Wake-on-LAN utility,
- authenticated wake path,
- local Wake-on-LAN test,
- remote Wake-on-LAN test,
- Main Workstation startup verification,
- ComfyUI READY verification after startup.

Known Main Workstation data

- adapter: Intel I219-V,
- MAC address: D4-5D-64-27-5E-9B,
- wired Ethernet verified,
- Wake on Magic Packet enabled,
- Windows wake permission enabled,
- Fast Startup not blocking Wake-on-LAN.

Status

Deferred until after the trip.

---

## Conventional Wake-on-LAN Relay

Potential relay devices

- Raspberry Pi
- Mini-PC
- NAS
- old laptop
- dedicated low-power relay device

Status

Deferred

---

## Tailscale Watchdog

Purpose

Detect and recover loss of the Main Workstation Tailscale connection after native Windows service configuration has been verified.

Activation rule

Do not implement before checking:

- Run Unattended,
- service startup type,
- service recovery,
- key expiry,
- authentication,
- Tailscale Serve recovery.

A watchdog is a fallback, not the first repair.

Status

Candidate after recovery diagnostics.

---

## Windows vs Linux AI Runtime Benchmark

Compare identical AI workflows on both operating systems before deciding whether migration is beneficial.

Status

Deferred

---

# Platform

## Curvature Assistant

Project-aware assistant integrated into Curvature Platform.

Status

Deferred

---

## HUD

24th-century Slavic operational interface.

Status

Deferred

---

## Design Language

Unified visual language for:

- Console
- HUD
- Mobile
- Web
- Chronicle Client
- future world-facing frontends

Status

Deferred

---

# Mobile

Reconnect the existing Android application once the Platform foundation is stable.

Status

Deferred

---

# Robotics

## Marian

Marian remains part of Project Curvature but is intentionally postponed until the Platform foundation is complete.

Status

Deferred

---

# Game Production

## Game Engine Integration

Curvature Platform prepares assets, workflows and data.

The game engine remains an independent future phase.

Status

Deferred

---

# Rule

Pipeline items never interrupt the active operational task or software sprint.

They are reviewed only when current work is complete or when the user explicitly promotes one.
