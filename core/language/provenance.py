from dataclasses import dataclass


@dataclass(frozen=True)
class Provenance:
    source: str
    period: str
    region: str
    notes: str = ""

    def __post_init__(self) -> None:
        if not self.source.strip():
            raise ValueError("source must not be empty")

        if not self.period.strip():
            raise ValueError("period must not be empty")

        if not self.region.strip():
            raise ValueError("region must not be empty")

    def to_dict(self) -> dict[str, str]:
        return {
            "source": self.source,
            "period": self.period,
            "region": self.region,
            "notes": self.notes,
        }

    @classmethod
    def from_dict(
        cls,
        data: dict[str, object],
    ) -> "Provenance":
        source = data.get("source")
        period = data.get("period")
        region = data.get("region")
        notes = data.get("notes", "")

        if not isinstance(source, str):
            raise ValueError("source must be a string")

        if not isinstance(period, str):
            raise ValueError("period must be a string")

        if not isinstance(region, str):
            raise ValueError("region must be a string")

        if not isinstance(notes, str):
            raise ValueError("notes must be a string")

        return cls(
            source=source,
            period=period,
            region=region,
            notes=notes,
        )
