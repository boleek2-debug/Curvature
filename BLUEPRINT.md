# BLUEPRINT

Status: Draft Version: 0.1.0 Owner: Project Curvature Last Updated:
2026-07-13

------------------------------------------------------------------------

# Purpose

This document describes the current technical architecture of Curvature
Platform.

It explains how the platform is organised. It does not describe future
plans or sprint history.

------------------------------------------------------------------------

# High-Level Architecture

Project Curvature \| +------------------------------+ \| \| Curvature
Platform Future Game \| +------------------------------+ \| \| Core
Services \| \| Telemetry Remote Runtime Diagnostics AI Runtime
Indicators Workflow Engine Configuration Asset Pipeline Logging World
Builder Export

        |
        +------------------------------+
        |
    Frontends

-   Console
-   Future HUD
-   Future Mobile
-   Future Web
-   Future VR

------------------------------------------------------------------------

# Core

Curvature Core is the single source of truth.

Responsibilities:

-   Collect telemetry
-   Evaluate diagnostics
-   Produce indicators
-   Manage configuration
-   Expose data to frontends

------------------------------------------------------------------------

# Services

Remote Runtime

Current implementation:

-   Tailscale communication
-   Remote workstation abstraction
-   ComfyUI availability detection

AI Runtime

Current implementation:

-   Remote ComfyUI integration

Workflow Engine

Current implementation:

-   Workflow registry
-   Workflow states

------------------------------------------------------------------------

# Frontends

Current:

-   Console

Planned:

-   HUD
-   Mobile
-   Web
-   VR

Frontends display data. They do not create system state.

------------------------------------------------------------------------

# Current Production Topology

Curvature Dev \| Tailscale \| Main Workstation \| ComfyUI

The workstation is treated as a remote AI Runtime.

------------------------------------------------------------------------

# Current Verified Components

-   Telemetry
-   Diagnostics
-   Console
-   Workflow foundation
-   Remote Runtime
-   ComfyUI detection over Tailscale

------------------------------------------------------------------------

# Design Principle

Build simple.

Verify every layer.

Expand one sprint at a time.
