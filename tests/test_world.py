import json

import pytest

from core.world import (
    Entity,
    JsonWorldStorage,
    Place,
    WorldState,
    WorldStateError,
    WorldStorageError,
)


def test_world_creation_has_persistent_identifier() -> None:
    world = WorldState.create(
        name="Curvature",
        initial_place=Place(
            place_id="village-gate",
            name="Village Gate",
        ),
    )

    assert world.world_id
    assert world.name == "Curvature"
    assert list(world.places) == ["village-gate"]


def test_world_state_adds_entity_to_known_place() -> None:
    world = WorldState.create(
        name="Curvature",
        initial_place=Place(
            place_id="village-gate",
            name="Village Gate",
        ),
    )

    world.add_entity(
        Entity(
            entity_id="traveller",
            name="Traveller",
            kind="character",
            place_id="village-gate",
        )
    )

    assert world.entities["traveller"].place_id == (
        "village-gate"
    )


def test_world_state_rejects_entity_in_unknown_place() -> None:
    world = WorldState.create(
        name="Curvature",
        initial_place=Place(
            place_id="village-gate",
            name="Village Gate",
        ),
    )

    with pytest.raises(
        WorldStateError,
        match="unknown place",
    ):
        world.add_entity(
            Entity(
                entity_id="traveller",
                name="Traveller",
                kind="character",
                place_id="missing-place",
            )
        )


def test_world_state_moves_entity() -> None:
    world = WorldState.create(
        name="Curvature",
        initial_place=Place(
            place_id="village-gate",
            name="Village Gate",
        ),
    )
    world.add_place(
        Place(
            place_id="market",
            name="Market",
        )
    )
    world.add_entity(
        Entity(
            entity_id="traveller",
            name="Traveller",
            kind="character",
            place_id="village-gate",
        )
    )

    world.move_entity(
        entity_id="traveller",
        destination_place_id="market",
    )

    assert world.entities["traveller"].place_id == "market"


def test_world_state_survives_save_and_load(
    tmp_path,
) -> None:
    storage = JsonWorldStorage(
        tmp_path / "world.json"
    )
    world = WorldState.create(
        name="Curvature",
        initial_place=Place(
            place_id="village-gate",
            name="Village Gate",
        ),
    )
    world.add_entity(
        Entity(
            entity_id="traveller",
            name="Traveller",
            kind="character",
            place_id="village-gate",
        )
    )

    storage.save(world)
    loaded = storage.load()

    assert loaded.world_id == world.world_id
    assert loaded.name == world.name
    assert loaded.places == world.places
    assert loaded.entities == world.entities


def test_world_storage_writes_versioned_json(
    tmp_path,
) -> None:
    storage = JsonWorldStorage(
        tmp_path / "world.json"
    )
    world = WorldState.create(
        name="Curvature",
        initial_place=Place(
            place_id="village-gate",
            name="Village Gate",
        ),
    )

    storage.save(world)

    data = json.loads(
        storage.path.read_text(
            encoding="utf-8",
        )
    )

    assert data["format_version"] == 1
    assert data["world_id"] == world.world_id


def test_world_storage_rejects_missing_file(
    tmp_path,
) -> None:
    storage = JsonWorldStorage(
        tmp_path / "missing.json"
    )

    with pytest.raises(
        WorldStorageError,
        match="does not exist",
    ):
        storage.load()
