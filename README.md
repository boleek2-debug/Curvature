# Project Curvature

> Building the workshop before building the world.

## Overview

Project Curvature is a long-term engineering project whose final objective is
a fully playable MMORPG and, eventually, an MMORPGVR world.

The current phase is focused on building **Curvature Platform**: the production
workshop that will coordinate the technologies, tools and workflows required
to create that world.

Curvature Platform is not the final product.

It is the system used to build the final product.

## Current Development Focus

The current priority is the laptop-side Curvature Platform.

Implemented foundations include:

- Curvature Core
- local telemetry
- diagnostics
- operational indicators
- text Console
- Workflow Engine foundation
- Remote Runtime
- Tailscale communication
- remote ComfyUI detection
- AI Runtime Console screen

## Architecture

Curvature Platform is divided into three main layers:

### Core

The source of truth for system state.

Current Core components include:

- Telemetry
- Diagnostics
- Indicators
- Configuration
- Logging
- Events

### Services

Operational systems used by the production workshop.

Current and planned services include:

- Remote Runtime
- AI Runtime
- Workflow Engine
- Asset Pipeline
- World Builder
- Export

### Frontends

Interfaces that display information supplied by Core and Services.

Current and planned frontends include:

- Console
- mandatory future HUD
- Mobile
- Web
- VR

Frontends must never invent system state.

Every displayed status must be based on verified information.

## Engineering Principles

Project Curvature follows these rules:

1. Never guess.
2. Request current files before modifying uncertain existing code.
3. Provide complete replacement files.
4. One sprint has one goal.
5. Every sprint ends with working functionality.
6. Every displayed state must be verifiable.
7. Core is the source of truth.
8. Frontends only present Core and Service data.
9. Test before commit.
10. Commit before push.
11. Update `HANDOFF.md` after completed work.
12. Code and documentation are written in English.
13. Development discussion is conducted in Polish.

## Development Environment

### Clone the repository

```bash
git clone https://github.com/boleek2-debug/Curvature.git
cd Curvature
```

### Create the Conda environment

```bash
conda env create -f environment.yml
conda activate comfy
```

### Install pinned Python packages

```bash
python -m pip install -r requirements.txt
```

### Run the Console

```bash
python -m console.main
```

### Run automated tests

```bash
python -m pytest -v
```

## Current Remote Topology

```text
Curvature Dev
      |
  Tailscale
      |
Main Workstation
      |
   ComfyUI
```

The laptop and the main workstation are not expected to share a local network.

Remote communication is designed around Tailscale.

The main workstation currently acts as the remote AI Runtime.

## Project Documentation

- `HANDOFF.md` — current operational state and exact next step
- `CURVATURE.md` — project vision and philosophy
- `BLUEPRINT.md` — current technical architecture
- `ROADMAP.md` — planned development direction
- `PIPELINE.md` — deferred ideas and future features
- `CHANGELOG.md` — completed and verified work

A new development session or ChatGPT instance should read `HANDOFF.md` first.

## Development Workflow

```text
Vision
  |
Architecture
  |
Sprint
  |
Working implementation
  |
Tests
  |
Git commit
  |
GitHub push
  |
Documentation update
  |
Next sprint
```

## Current Sprint

`BUILD-001`

Objective:

Create a reproducible Curvature development environment using:

- `environment.yml`
- `requirements.txt`
- documented installation commands

## Long-Term Goal

Project Curvature is complete only when the production workshop has enabled
the creation of a living, playable MMORPG world.

The later objective is to extend that world into MMORPGVR.
