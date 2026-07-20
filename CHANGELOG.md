# CHANGELOG

Status: Active
Version: 0.7.0
Owner: Project Curvature
Last Updated: 2026-07-20

---

# Purpose

This document records completed and verified work only.

Planned work belongs in `ROADMAP.md`.

Ideas belong in `PIPELINE.md`.

Current operational state belongs in `HANDOFF.md`.

Architecture belongs in `BLUEPRINT.md`.

---

## 2026-07-20

### ASSISTANT-001B5.2C — Reliable ChatGPT Conversation Routing

Completed

- one shared ChatGPT Project selected for all three departments
- three departmental conversations retained inside the shared Project
- conversation titles removed from technical routing
- URL-only routing implemented
- active conversation URL persisted per department
- conversation URL history retained
- standard conversation URL support
- project-scoped conversation URL support
- one-click `Send Task`
- one explicit confirmation for `Thread Handoff`
- visible Chrome fallback
- browser lifecycle failure handling
- correct UI release after browser errors
- only the originating department panel locked during a request
- response returned to the correct department panel
- Console documentation aligned with the verified architecture

Verified

```text
56 automated tests passed
PROJECT_SCOPED_ROUTE_OK
commit b55c7e6 pushed
main == origin/main
working tree clean
```

Verified project-scoped route form

```text
https://chatgpt.com/g/<project-id>/c/<conversation-id>
```

Result

Curvature Console can reliably send a task to the persisted departmental conversation and return the response without depending on a mutable conversation title.

---

# Purpose

This document records completed work only.

Planned work belongs in ROADMAP.

Ideas belong in PIPELINE.

Current operational state belongs in HANDOFF.

Architecture belongs in BLUEPRINT.

---

## 2026-07-18

### Curvature Console ChatGPT Plus Architecture Amendment

Accepted

- mandatory paid OpenAI API integration removed from the Console MVP
- official ChatGPT Projects selected as the AI conversation environment
- zero additional mandatory AI cost rule adopted
- Task Package approved for normal work
- Thread Handoff Package approved for moving to a new chat
- local GREEN / AMBER / RED thread-pressure estimation approved as advisory
- unsupported browser automation rejected
- repository documentation and Console state remain authoritative continuity layers

Result

Curvature Console can coordinate long-running Project, Core and Research work without requiring API billing beyond the existing ChatGPT Plus subscription.

---


### LANG-001

Completed

- language form classification model
- confidence level model
- provenance model
- language entry model
- versioned lexicon model
- JSON lexicon storage
- validation separating reconstruction, plausibility, Curvature-derived forms, fiction and uncertainty
- automated language foundation tests

Verified

- reconstructed forms require provenance
- Curvature-derived forms cannot claim high historical confidence
- fictional forms cannot claim historical provenance
- duplicate entry identifiers are rejected
- lexicon entries survive save and load
- lexicon JSON format version is preserved
- missing lexicon files are rejected
- 36 automated project tests passed
- commit and push completed

Result

Curvature now has a technical language foundation that distinguishes historical evidence from controlled invention.

---

## 2026-07-18

### WORLD-001

Completed

- persistent world identifier
- Place model
- Entity model
- authoritative WorldState
- controlled state transitions
- versioned JSON world storage
- load after restart
- automated World Core tests

Verified

- world identifier persists across save and load
- entities cannot reference unknown places
- entity movement validates destinations
- world state survives save and load
- world JSON format version is preserved
- 28 automated project tests passed
- commit and push completed

Result

Curvature now has the first minimum authoritative and persistent World Core.

---

## 2026-07-18

### REMOTE-004

Completed

- Minimal Service Heartbeat
- endpoint name resolution check
- ComfyUI service port check
- ComfyUI API verification
- heartbeat state model
- READY state
- ATTENTION state
- OFFLINE state
- current verification timestamp
- last successful verification timestamp
- preservation of the last successful timestamp after later failures
- heartbeat information in the AI Runtime Console
- automated heartbeat tests

Verified

- endpoint `thing` resolved successfully
- port `8188` reported ONLINE
- `/system_stats` API reported READY
- Heartbeat state displayed READY
- current check time displayed
- last successful check time displayed
- live NVIDIA GeForce RTX 4060 data remained available
- live VRAM data remained available
- live queue data remained available
- live Windows runtime information remained available
- 21 automated project tests passed

Result

Curvature now provides a small, explicit and verifiable heartbeat for the remote AI Runtime without treating name resolution alone as proof that the workstation or ComfyUI API is healthy.

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
