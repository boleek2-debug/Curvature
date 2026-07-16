# PIPELINE

Status: Draft
Version: 0.3.0
Owner: Project Curvature
Last Updated: 2026-07-14

---

# Purpose

The Pipeline stores valuable ideas that are intentionally postponed.

Items in this document must not interrupt the current sprint.

Only when an item is promoted does it move into the Roadmap.

---

# Infrastructure

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

Current operational decision

The Main Workstation will remain powered on during the upcoming eight-day trip.

Sleep and hibernation must remain disabled.

Monitors may remain switched off.

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

Pipeline items never interrupt the active sprint.

They are reviewed only when the current sprint is complete or when the user explicitly promotes one.
