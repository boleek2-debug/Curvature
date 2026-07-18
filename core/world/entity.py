from dataclasses import dataclass


@dataclass(frozen=True)
class Entity:
    entity_id: str
    name: str
    kind: str
    place_id: str

    def __post_init__(self) -> None:
        if not self.entity_id.strip():
            raise ValueError("entity_id must not be empty")

        if not self.name.strip():
            raise ValueError("name must not be empty")

        if not self.kind.strip():
            raise ValueError("kind must not be empty")

        if not self.place_id.strip():
            raise ValueError("place_id must not be empty")

    def with_place(self, place_id: str) -> "Entity":
        return Entity(
            entity_id=self.entity_id,
            name=self.name,
            kind=self.kind,
            place_id=place_id,
        )

    def to_dict(self) -> dict[str, str]:
        return {
            "entity_id": self.entity_id,
            "name": self.name,
            "kind": self.kind,
            "place_id": self.place_id,
        }

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Entity":
        entity_id = data.get("entity_id")
        name = data.get("name")
        kind = data.get("kind")
        place_id = data.get("place_id")

        if not isinstance(entity_id, str):
            raise ValueError("entity_id must be a string")

        if not isinstance(name, str):
            raise ValueError("name must be a string")

        if not isinstance(kind, str):
            raise ValueError("kind must be a string")

        if not isinstance(place_id, str):
            raise ValueError("place_id must be a string")

        return cls(
            entity_id=entity_id,
            name=name,
            kind=kind,
            place_id=place_id,
        )
