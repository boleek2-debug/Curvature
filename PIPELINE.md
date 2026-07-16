# PIPELINE

Status: Draft
Version: 0.4.0
Owner: Project Curvature
Last Updated: 2026-07-16

---

# Purpose

The Pipeline stores valuable ideas that are intentionally postponed.

Items in this document must not interrupt the current operational task or software sprint.

Only when an item is promoted does it move into the Roadmap.

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

Required battery data

- Design capacity
- Full charge capacity
- Battery health percentage
- Charge cycle count
- Current charge level
- Battery model and manufacturer where available

Vehicle power target

- Curvature Dev ASUS ROG laptop
- Mercedes Turismo 2
- 12 V vehicle socket
- 15 A protected circuit
- compatible inverter or 12 V laptop adapter

Final device status

- READY
- READY WITH LIMITATIONS
- ATTENTION
- FAILED

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

Planned components

- Samsung Galaxy S20 FE
- Permanent home Wi-Fi connection
- Permanent charger connection
- Tailscale
- Termux
- Wake-on-LAN utility
- Small authenticated wake endpoint or equivalent command path

Required configuration

- Tailscale logged into the Curvature tailnet
- Incoming Tailscale connections allowed
- Battery optimisation disabled for Tailscale
- Battery optimisation disabled for Termux
- Termux installed from a supported source
- Wake-on-LAN package installed
- Main Workstation MAC address configured
- Local Wake-on-LAN test
- Remote Wake-on-LAN test through Tailscale
- Main Workstation startup verification
- Tailscale availability verification after startup
- ComfyUI READY verification after startup

Known Main Workstation network adapter

- Adapter: Intel I219-V
- MAC address: D4-5D-64-27-5E-9B
- Wired Ethernet connection: verified
- Wake on Magic Packet: enabled
- Windows wake permission: enabled
- Fast Startup: unavailable and not blocking Wake-on-LAN

Status

Deferred until after the trip.

---

## Conventional Wake-on-LAN Relay

Purpose

Allow Curvature to start the Main Workstation through an always-on device inside the home LAN.

Potential relay devices

- Raspberry Pi
- Mini-PC
- NAS
- Old laptop
- Dedicated low-power relay device

Planned flow

    Curvature Dev
        |
    Tailscale
        |
    Home-LAN Relay
        |
    Wake Main Workstation
        |
    Wait for Tailscale
        |
    Verify ComfyUI
        |
    READY

Status

Deferred

---

## Tailscale Watchdog

Purpose

Detect and recover loss of the Main Workstation Tailscale connection after the native Windows service configuration has been verified.

Possible responsibilities

- periodically verify Tailscale backend state,
- restart the Tailscale service when the backend is unhealthy,
- record recovery attempts,
- avoid restart loops,
- expose a verifiable health state to Curvature later.

Activation rule

Do not implement a watchdog before checking:

- Run Unattended,
- Windows service startup type,
- service recovery options,
- device key expiry,
- authentication state,
- Tailscale Serve recovery after restart.

A watchdog is a fallback, not the first repair.

Status

Candidate after Saturday diagnostics.

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

They are reviewed only when the current work is complete or when the user explicitly promotes one.
