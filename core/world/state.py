from dataclasses import dataclass, field
from uuid import uuid4

from .entity import Entity
from .place import Place


class WorldStateError(ValueError):
    pass


@dataclass
class WorldState:
    world_id: str
    name: str
    places: dict[str, Place] = field(default_factory=dict)
    entities: dict[str, Entity] = field(default_factory=dict)

    FORMAT_VERSION = 1

    def __post_init__(self) -> None:
        if not self.world_id.strip():
            raise WorldStateError("world_id must not be empty")

        if not self.name.strip():
            raise WorldStateError("name must not be empty")

        self._validate_references()

    @classmethod
    def create(
        cls,
        name: str,
        initial_place: Place,
    ) -> "WorldState":
        return cls(
            world_id=str(uuid4()),
            name=name,
            places={
                initial_place.place_id: initial_place,
            },
        )

    def add_place(self, place: Place) -> None:
        if place.place_id in self.places:
            raise WorldStateError(
                f"place already exists: {place.place_id}"
            )

        self.places[place.place_id] = place

    def add_entity(self, entity: Entity) -> None:
        if entity.entity_id in self.entities:
            raise WorldStateError(
                f"entity already exists: {entity.entity_id}"
            )

        if entity.place_id not in self.places:
            raise WorldStateError(
                f"unknown place: {entity.place_id}"
            )

        self.entities[entity.entity_id] = entity

    def move_entity(
        self,
        entity_id: str,
        destination_place_id: str,
    ) -> None:
        entity = self.entities.get(entity_id)

        if entity is None:
            raise WorldStateError(
                f"unknown entity: {entity_id}"
            )

        if destination_place_id not in self.places:
            raise WorldStateError(
                f"unknown place: {destination_place_id}"
            )

        self.entities[entity_id] = entity.with_place(
            destination_place_id
        )

    def to_dict(self) -> dict[str, object]:
        return {
            "format_version": self.FORMAT_VERSION,
            "world_id": self.world_id,
            "name": self.name,
            "places": [
                place.to_dict()
                for place in self.places.values()
            ],
            "entities": [
                entity.to_dict()
                for entity in self.entities.values()
            ],
        }

    @classmethod
    def from_dict(
        cls,
        data: dict[str, object],
    ) -> "WorldState":
        format_version = data.get("format_version")
        world_id = data.get("world_id")
        name = data.get("name")
        places_data = data.get("places")
        entities_data = data.get("entities")

        if format_version != cls.FORMAT_VERSION:
            raise WorldStateError(
                f"unsupported format_version: {format_version}"
            )

        if not isinstance(world_id, str):
            raise WorldStateError("world_id must be a string")

        if not isinstance(name, str):
            raise WorldStateError("name must be a string")

        if not isinstance(places_data, list):
            raise WorldStateError("places must be a list")

        if not isinstance(entities_data, list):
            raise WorldStateError("entities must be a list")

        places: dict[str, Place] = {}

        for item in places_data:
            if not isinstance(item, dict):
                raise WorldStateError(
                    "place entry must be an object"
                )

            place = Place.from_dict(item)

            if place.place_id in places:
                raise WorldStateError(
                    f"duplicate place: {place.place_id}"
                )

            places[place.place_id] = place

        entities: dict[str, Entity] = {}

        for item in entities_data:
            if not isinstance(item, dict):
                raise WorldStateError(
                    "entity entry must be an object"
                )

            entity = Entity.from_dict(item)

            if entity.entity_id in entities:
                raise WorldStateError(
                    f"duplicate entity: {entity.entity_id}"
                )

            entities[entity.entity_id] = entity

        return cls(
            world_id=world_id,
            name=name,
            places=places,
            entities=entities,
        )

    def _validate_references(self) -> None:
        for entity in self.entities.values():
            if entity.place_id not in self.places:
                raise WorldStateError(
                    f"entity {entity.entity_id} references "
                    f"unknown place {entity.place_id}"
                )
