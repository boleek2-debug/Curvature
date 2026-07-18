from dataclasses import dataclass


@dataclass(frozen=True)
class Place:
    place_id: str
    name: str

    def __post_init__(self) -> None:
        if not self.place_id.strip():
            raise ValueError("place_id must not be empty")

        if not self.name.strip():
            raise ValueError("name must not be empty")

    def to_dict(self) -> dict[str, str]:
        return {
            "place_id": self.place_id,
            "name": self.name,
        }

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Place":
        place_id = data.get("place_id")
        name = data.get("name")

        if not isinstance(place_id, str):
            raise ValueError("place_id must be a string")

        if not isinstance(name, str):
            raise ValueError("name must be a string")

        return cls(
            place_id=place_id,
            name=name,
        )
