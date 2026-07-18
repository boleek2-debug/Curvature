from dataclasses import dataclass, field

from .entry import LanguageEntry


class LexiconError(ValueError):
    pass


@dataclass
class Lexicon:
    language_id: str
    name: str
    entries: dict[str, LanguageEntry] = field(
        default_factory=dict
    )

    FORMAT_VERSION = 1

    def __post_init__(self) -> None:
        if not self.language_id.strip():
            raise LexiconError(
                "language_id must not be empty"
            )

        if not self.name.strip():
            raise LexiconError("name must not be empty")

    def add_entry(
        self,
        entry: LanguageEntry,
    ) -> None:
        if entry.entry_id in self.entries:
            raise LexiconError(
                f"entry already exists: {entry.entry_id}"
            )

        self.entries[entry.entry_id] = entry

    def get_by_form(
        self,
        form: str,
    ) -> tuple[LanguageEntry, ...]:
        return tuple(
            entry
            for entry in self.entries.values()
            if entry.form == form
        )

    def to_dict(self) -> dict[str, object]:
        return {
            "format_version": self.FORMAT_VERSION,
            "language_id": self.language_id,
            "name": self.name,
            "entries": [
                entry.to_dict()
                for entry in self.entries.values()
            ],
        }

    @classmethod
    def from_dict(
        cls,
        data: dict[str, object],
    ) -> "Lexicon":
        format_version = data.get("format_version")
        language_id = data.get("language_id")
        name = data.get("name")
        entries_data = data.get("entries")

        if format_version != cls.FORMAT_VERSION:
            raise LexiconError(
                f"unsupported format_version: "
                f"{format_version}"
            )

        if not isinstance(language_id, str):
            raise LexiconError(
                "language_id must be a string"
            )

        if not isinstance(name, str):
            raise LexiconError("name must be a string")

        if not isinstance(entries_data, list):
            raise LexiconError(
                "entries must be a list"
            )

        entries: dict[str, LanguageEntry] = {}

        for item in entries_data:
            if not isinstance(item, dict):
                raise LexiconError(
                    "entry must be an object"
                )

            entry = LanguageEntry.from_dict(item)

            if entry.entry_id in entries:
                raise LexiconError(
                    f"duplicate entry: {entry.entry_id}"
                )

            entries[entry.entry_id] = entry

        return cls(
            language_id=language_id,
            name=name,
            entries=entries,
        )
