# BLUEPRINT

Status: Draft
Version: 0.2.0
Owner: Project Curvature
Last Updated: 2026-07-18

---

# Purpose

This document describes the current technical architecture of Curvature Platform and the approved direction for the future World Core.

Current implementation and planned architecture are explicitly separated.

---

# High-Level Architecture

    Project Curvature
        |
        +-- Curvature Platform
        |     |
        |     +-- Core
        |     +-- Services
        |     +-- Frontends
        |     +-- Planned World Core
        |
        +-- Persistent Living World
              |
              +-- Chronicle Client / MUD
              +-- Future 2D
              +-- Future 3D
              +-- Future VR
              +-- Future Multiplayer / MMORPG

All world-facing frontends must connect to the same persistent world state.

---

# Current Platform Core

Curvature Core is the source of truth for platform state.

Current responsibilities:

- collect telemetry,
- evaluate diagnostics,
- produce indicators,
- manage configuration,
- expose verified data to frontends.

Current components:

- Telemetry
- Diagnostics
- Indicators
- Configuration foundation
- Logging foundation
- Events foundation

---

# Current Services

## Remote Runtime

Current implementation:

- Tailscale communication
- Remote workstation abstraction
- HTTP JSON retrieval
- ComfyUI availability detection
- ComfyUI system statistics
- ComfyUI queue status
- remote GPU and VRAM information
- remote operating system and RAM information
- remote Python, PyTorch and ComfyUI versions

## AI Runtime

Current implementation:

- remote ComfyUI integration
- verified AI Runtime state
- READY, ATTENTION and OFFLINE presentation

## Workflow Engine

Current implementation:

- Workflow registry
- Workflow states

---

# Planned World Core

World Core is approved architecture but is not yet implemented.

It will become the source of truth for world state.

Planned responsibilities:

- persist world state,
- manage world time,
- record events,
- preserve consequences,
- maintain character identity and memory,
- provide facts to narration,
- support the Chronicle,
- expose the same world to all world-facing frontends.

Planned components:

## World State

- places
- entities
- ownership
- relationships
- resources
- conditions
- persistent changes

## Time

- world clock
- durations
- scheduled events
- historical ordering
- ageing and change

## Events

- verified actions
- state transitions
- causes
- effects
- references to actors and places

## Chronicle

- durable historical record
- narrative interpretation of verified events
- multiple viewpoints where appropriate
- separation between fact and narration

## Characters

- identity
- knowledge
- memory
- goals
- relationships
- emotional state
- cultural and linguistic profile

## Language

- historical reconstruction data
- confidence and provenance
- construction rules
- lexicon
- names
- morphology
- phonology
- dialect development
- language evolution

---

# Frontends

## Current

- Console

The Console is an operator interface for Curvature Platform.

It does not represent the world.

## Planned World-Facing Frontends

### Chronicle Client / MUD

The first world-facing frontend.

Responsibilities:

- accept natural-language player intent
- present verified world state through narration
- expose characters and places
- show consequences
- provide access to the Chronicle

### 2D Client

A visual portal into the same world.

### 3D Client

A spatial portal into the same world.

### VR Client

An immersive portal into the same world.

Frontends do not own world state.

They query and present World Core.

---

# Language Architecture

## Historical Reconstruction Layer

Stores reconstructed forms, evidence, uncertainty and provenance.

## Curvature Construction Layer

Defines how missing words and structures are created consistently.

## World Language Layer

Applies regional, social, historical and character-specific variation.

## Player Interpretation Layer

Maps modern natural-language player input into candidate world actions.

No player action becomes world fact until validated against World Core.

---

# Current Production Topology

    Curvature Dev
        |
    Tailscale
        |
    Main Workstation
        |
    ComfyUI

The Main Workstation is treated as a remote AI Runtime.

Current operational issue:

- the workstation is physically powered on,
- Tailscale device `thing` is offline,
- remote recovery and unattended operation must be restored.

---

# Current Verified Components

- Telemetry
- Diagnostics
- Console
- Workflow foundation
- Remote Runtime
- ComfyUI detection over Tailscale
- ComfyUI system statistics
- ComfyUI queue status
- remote GPU and VRAM diagnostics
- remote runtime diagnostics
- automated Remote Runtime tests

---

# Planned Vertical Slice

The first living-world vertical slice should include:

- one persistent place,
- one or more characters,
- world time,
- verified player actions,
- character memory,
- consequences,
- reconstructed language data,
- Chronicle entries,
- a text-based Chronicle Client.

---

# Design Principles

Build simple.

Verify every layer.

Keep platform state and world state authoritative.

Separate fact from narration.

Expand one sprint at a time.

Use the minimum reliable workshop to create the first living slice early.
