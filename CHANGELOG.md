# CHANGELOG

Status: Active
Version: 0.4.0
Owner: Project Curvature
Last Updated: 2026-07-13

---

# Purpose

This document records completed work only.

Planned work belongs in ROADMAP.

Ideas belong in PIPELINE.

Current operational state belongs in HANDOFF.

Architecture belongs in BLUEPRINT.

---

## 2026-07-13

### REMOTE-003

Completed

- HTTP JSON request support in Workstation
- ComfyUI /system_stats integration
- ComfyUI /queue integration
- Remote GPU information
- Remote VRAM usage and load
- Remote queue running count
- Remote queue pending count
- Remote queue total
- Remote operating system information
- Remote RAM usage and load
- ComfyUI version display
- Remote Python version display
- Remote PyTorch version display
- Runtime diagnostics ATTENTION state
- Automated Remote Runtime test suite

Verified

- Tailscale Serve hostname routing through thing:8188
- /system_stats returned HTTP 200 and valid JSON
- /queue returned HTTP 200 and valid JSON
- NVIDIA GeForce RTX 4060 detected
- Live VRAM values displayed
- Live queue values displayed
- Windows runtime information displayed
- Live RAM values displayed
- ComfyUI 0.26.2 displayed
- Python 3.13.12 displayed
- PyTorch 2.10.0+cu130 displayed
- AI Runtime Console state READY
- 16 automated tests passed

Result

The AI Runtime Console now displays verified live telemetry and diagnostics from the remote ComfyUI workstation over Tailscale.

---

## 2026-07-13

### BUILD-001

Completed

- Dedicated Curvature Conda environment
- environment.yml
- requirements.txt
- Installation guide
- Clean environment recreation procedure
- Environment verification procedure

Verified

- Environment created from environment.yml
- Environment name: curvature
- Python 3.11.15
- Interpreter path: /home/seb/miniconda3/envs/curvature/bin/python
- requirements.txt installed successfully
- pip check reported no broken requirements
- 4 automated telemetry tests passed
- Console launched successfully
- System Status screen displayed live telemetry
- System Diagnostics state READY
- Workshop Status screen displayed
- Workflow Engine screen displayed
- AI Runtime screen displayed
- Remote ComfyUI state READY

Result

Curvature Platform now has a clean, dedicated and reproducible development environment independent from the ComfyUI environment.

---

## 2026-07-13

### REMOTE-002

Completed

- AI Runtime Console screen
- AI Runtime menu entry
- RemoteManager integration
- Live ComfyUI state

Verified

- READY state displayed when ComfyUI was available
- OFFLINE state displayed when ComfyUI was unavailable
- Remote status obtained from RemoteManager
- Manual verification completed

Result

Console now communicates with the remote AI Runtime and displays the real service state.

---

## 2026-07-13

### Documentation Foundation

Completed

- Initial HANDOFF document
- Initial CURVATURE document
- Initial BLUEPRINT document
- Initial ROADMAP document
- Initial PIPELINE document
- Initial CHANGELOG document

Result

Project documentation foundation established.

---

## 2026-07-13

### REMOTE-001

Completed

- Remote Runtime foundation
- Workstation abstraction
- RemoteManager implementation
- Tailscale integration
- Remote endpoint abstraction
- AI Runtime role
- Remote ComfyUI detection

Verified

- OFFLINE detection works correctly
- ONLINE detection works correctly
- Remote AI Runtime reachable through Tailscale
- ComfyUI availability successfully verified

Current verified endpoint

thing:8188

---

## 2026-07-12

### Curvature Core Foundation

Completed

- Core package
- Telemetry
- Diagnostics
- Indicators
- Console foundation
- Workflow foundation

Verified

Telemetry tests completed successfully.
