# WORLD

Status: Draft
Version: 0.1.0
Owner: Project Curvature
Last Updated: 2026-07-18

---

# Purpose

This document defines the approved conceptual foundation of the persistent living world in Project Curvature.

---

# Core Definition

The Curvature world is persistent.

It must survive application restarts, frontend changes, pauses in development and migration from text to 2D, 3D and VR.

The world is not owned by any frontend.

Chronicle Client, 2D, 3D and VR are different portals into the same world.

---

# World as History

Actions create events.

Events may change state.

State changes create consequences.

Consequences affect future events, relationships and narration.

The result should feel like a book written through human thought and action, while remaining grounded in recorded world state.

---

# Source of Truth

World Core will be the source of truth for world facts.

Narration may interpret facts.

Characters may misunderstand facts.

The Chronicle may preserve multiple viewpoints.

No frontend, narrator or character may silently rewrite authoritative world state.

---

# Persistence

The minimum persistent world must preserve:

- time,
- places,
- characters,
- relationships,
- possessions,
- conditions,
- events,
- consequences,
- memories,
- Chronicle entries.

A restart must not reset the world unless an explicit development reset is performed.

---

# Time

World time must support:

- ordered events,
- durations,
- scheduled events,
- ageing,
- travel,
- delay,
- memory of when something happened.

The first model may advance through verified actions and controlled ticks.

---

# Places

Places are persistent entities.

A place may contain physical properties, inhabitants, resources, ownership, current conditions, history, culture and linguistic context.

The first vertical slice should use one small place rather than a large empty map.

---

# Characters

Characters are world entities, not dialogue generators.

Each character should eventually contain:

- identity,
- origin,
- knowledge,
- memory,
- goals,
- relationships,
- beliefs,
- emotional state,
- cultural profile,
- linguistic profile,
- recognisable voice.

Characters may be wrong, biased or uncertain.

Their statements are not automatically world facts.

---

# Memory

Memory must distinguish between:

- verified world events,
- what a character witnessed,
- what a character was told,
- what a character believes,
- what a character has forgotten or distorted.

---

# Consequences

Player actions must be evaluated against world rules and current state.

Possible results include success, partial success, failure, delayed effect, social reaction, relationship change, state change or a new future event.

Consequences must persist.

---

# Chronicle

The Chronicle is the historical memory of the world.

Raw events preserve facts.

Chronicle entries interpret and present those facts.

Chronicle records should include time, actors, places, causes, effects, uncertainty and narrative summaries.

---

# Player Input

The player should be able to express intent in natural language.

The system must separate intended action, target, context, assumptions, constraints, character reaction, state change, narration and Chronicle impact.

Natural language does not bypass world rules.

---

# First Vertical Slice

The first playable slice should contain:

- one place,
- a small number of characters,
- basic world time,
- persistent state,
- one meaningful action loop,
- memory,
- consequences,
- Chronicle generation,
- text presentation.

It may be single-player.

---

# Frontend Progression

    Chronicle Client / MUD
        |
        v
    2D
        |
        v
    3D
        |
        v
    VR

Each frontend must preserve access to the same world.

---

# Non-Goals for the First Slice

The first slice does not require:

- MMORPG networking,
- a complete continent,
- full combat,
- complete economy,
- final graphics,
- full artificial language coverage,
- unrestricted AI autonomy.
