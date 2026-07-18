# ROADMAP

Status: Active
Version: 1.0.0
Owner: Project Curvature
Last Updated: 2026-07-18

---

# Purpose

This roadmap describes the approved order of Project Curvature development.

Completed work belongs in CHANGELOG.

Deferred ideas belong in PIPELINE.

Current operational state belongs in HANDOFF.

---

# Product Constraint

Normal Curvature Console operation must not require spending beyond the user's existing ChatGPT Plus subscription.

The MVP uses:

- official ChatGPT Projects for AI conversations;
- manual, user-controlled transfer packages;
- local Console persistence;
- no paid OpenAI API;
- no automatic paid model or tool calls.

---

# Current Position

Current phase:

```text
Research Enablement and Living World Foundation
```

Completed Project milestones:

- BUILD-001
- REMOTE-001
- REMOTE-002
- REMOTE-003
- REMOTE-004
- WORLD-001
- LANG-001

Current verified Project baseline:

```text
36 automated tests passed
```

Active Console milestone:

```text
ASSISTANT-001B5 — ChatGPT Plus Workflow Integration
```

Active implementation unit:

```text
ASSISTANT-001B5.1 — Task Package and Thread Handoff Package
```

---

# Curvature Console Milestones

## ASSISTANT-001A — Architecture and Technology Evaluation

Completed.

The selected implementation is:

- separate `~/curvature-console` repository;
- Python 3.11;
- PySide6 Qt Widgets;
- SQLite;
- YAML and Markdown;
- read-only access to `~/Curvature`.

The original paid-provider decision has been superseded by the zero-additional-cost ChatGPT Plus workflow.

## ASSISTANT-001B1 — Repository and Application Foundation

Completed and verified.

## ASSISTANT-001B2 — Three-Panel Desktop Shell

Completed and verified.

## Per-Department Attachments

Completed and verified.

## ASSISTANT-001B3 — Workspace Configuration and Context Loading

Completed and verified.

## ASSISTANT-001B4 — Local State and Conversation Persistence

Completed and verified:

- SQLite operational state;
- independent department state;
- drafts and conversation text;
- attachment metadata;
- persistent screenshots;
- splitter layout;
- Focus mode;
- restart continuity.

Verified Console baseline:

```text
22 passed
```

## ASSISTANT-001B5 — ChatGPT Plus Workflow Integration

Goal:

Use the existing ChatGPT Plus subscription without paid API integration.

### B5.1 — Task Package and Thread Handoff Package

Deliver:

- compact Task Package;
- comprehensive Thread Handoff Package;
- department authority;
- full role;
- mode-specific document inclusion;
- bounded conversation;
- current task;
- attachment manifest;
- preview;
- exact clipboard copy;
- no network call;
- no API dependency;
- automated tests.

### B5.2 — Assistant Response Import

Deliver:

- explicit target department;
- response preview;
- accepted response import;
- original text preservation;
- local persistence;
- automated tests.

### B5.3 — Structured Department Conversation Records

Deliver:

- user and assistant entries;
- timestamps;
- transfer source markers;
- restart persistence;
- migration from plain transcript where required.

### B5.4 — Thread Pressure Estimation

Deliver:

- locally estimated package and conversation size;
- GREEN / AMBER / RED state;
- advisory warning;
- Thread Handoff generation from AMBER or RED;
- no claim of exact ChatGPT capacity.

### B5.5 — Workflow Verification and Closeout

Verify:

- Project workflow;
- Core workflow;
- Research workflow;
- ChatGPT Project thread transition;
- attachment isolation;
- restart continuity;
- zero network calls;
- zero paid dependencies;
- documentation.

## ASSISTANT-001B6 — Department State Bus and Handoffs

- structured department summaries;
- controlled cross-department awareness;
- explicit handoffs;
- authority enforcement;
- no automatic sharing of full conversations.

## ASSISTANT-001B7 — MVP Verification and Closeout

- end-to-end workflow;
- restart continuity;
- authority boundaries;
- cost rule;
- packaging;
- documentation.

---

# Research Enablement

## RESEARCH-001 — Operational Research Workspace

Goal:

Make coordinated LANGUAGE research operational across Project, Core and Research.

Required capabilities:

- research role and protocol;
- publication analysis;
- evidence and confidence;
- references;
- missing knowledge;
- follow-up tasks;
- connected research graph;
- controlled handoffs.

## LANGUAGE Research Foundation

Owned by Curvature Research.

Must distinguish:

- reconstructed;
- plausible;
- Curvature-derived;
- intentionally fictional;
- uncertain.

## LANG-002 — Research Data Intake

Import verified Research outputs into the Core language system while preserving provenance, confidence and competing forms.

---

# Living World Milestones

## WORLD-002 — Time, Events and Chronicle

Give the world ordered history and durable consequences.

## NPC-001 — Identity, Memory, Goals and Voice

Create persistent characters with identity, knowledge, memory, goals, relationships and voice constraints.

## CHRONICLE-001 — First Playable Chronicle Client

Prove the living world through the first text-first world-facing vertical slice.

---

# Later Direction

1. expand Language and World Core together;
2. expand Chronicle Client;
3. add 2D;
4. add 3D;
5. add VR;
6. add multiplayer foundations;
7. grow toward MMORPG scale.

---

# Rule

An active sprint may be interrupted only by an explicit Project Curvature priority decision.
