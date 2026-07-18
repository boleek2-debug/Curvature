from dataclasses import dataclass, field

from .classification import (
    ConfidenceLevel,
    LanguageFormClass,
)
from .provenance import Provenance


@dataclass(frozen=True)
class LanguageEntry:
    entry_id: str
    form: str
    meaning: str
    classification: LanguageFormClass
    confidence: ConfidenceLevel
    provenance: Provenance | None = None
    pronunciation: str = ""
    grammar: str = ""
    notes: str = ""
    competing_forms: tuple[str, ...] = field(
        default_factory=tuple
    )

    def __post_init__(self) -> None:
        if not self.entry_id.strip():
            raise ValueError("entry_id must not be empty")

        if not self.form.strip():
            raise ValueError("form must not be empty")

        if not self.meaning.strip():
            raise ValueError("meaning must not be empty")

        if self.classification == (
            LanguageFormClass.RECONSTRUCTED
        ) and self.provenance is None:
            raise ValueError(
                "reconstructed forms require provenance"
            )

        if self.classification == (
            LanguageFormClass.CURVATURE_DERIVED
        ) and self.confidence == ConfidenceLevel.HIGH:
            raise ValueError(
                "Curvature-derived forms cannot claim "
                "high historical confidence"
            )

        if self.classification == (
            LanguageFormClass.FICTIONAL
        ) and self.provenance is not None:
            raise ValueError(
                "fictional forms must not claim "
                "historical provenance"
            )

        for form in self.competing_forms:
            if not isinstance(form, str) or not form.strip():
                raise ValueError(
                    "competing forms must be non-empty strings"
                )

    def to_dict(self) -> dict[str, object]:
        return {
            "entry_id": self.entry_id,
            "form": self.form,
            "meaning": self.meaning,
            "classification": self.classification.value,
            "confidence": self.confidence.value,
            "provenance": (
                self.provenance.to_dict()
                if self.provenance is not None
                else None
            ),
            "pronunciation": self.pronunciation,
            "grammar": self.grammar,
            "notes": self.notes,
            "competing_forms": list(self.competing_forms),
        }

    @classmethod
    def from_dict(
        cls,
        data: dict[str, object],
    ) -> "LanguageEntry":
        entry_id = data.get("entry_id")
        form = data.get("form")
        meaning = data.get("meaning")
        classification_value = data.get("classification")
        confidence_value = data.get("confidence")
        pronunciation = data.get("pronunciation", "")
        grammar = data.get("grammar", "")
        notes = data.get("notes", "")
        competing_forms = data.get("competing_forms", [])
        provenance_data = data.get("provenance")

        if not isinstance(entry_id, str):
            raise ValueError("entry_id must be a string")

        if not isinstance(form, str):
            raise ValueError("form must be a string")

        if not isinstance(meaning, str):
            raise ValueError("meaning must be a string")

        if not isinstance(classification_value, str):
            raise ValueError(
                "classification must be a string"
            )

        if not isinstance(confidence_value, str):
            raise ValueError("confidence must be a string")

        if not isinstance(pronunciation, str):
            raise ValueError(
                "pronunciation must be a string"
            )

        if not isinstance(grammar, str):
            raise ValueError("grammar must be a string")

        if not isinstance(notes, str):
            raise ValueError("notes must be a string")

        if not isinstance(competing_forms, list):
            raise ValueError(
                "competing_forms must be a list"
            )

        if not all(
            isinstance(item, str)
            for item in competing_forms
        ):
            raise ValueError(
                "competing_forms must contain strings"
            )

        try:
            classification = LanguageFormClass(
                classification_value
            )
        except ValueError as error:
            raise ValueError(
                f"unknown classification: "
                f"{classification_value}"
            ) from error

        try:
            confidence = ConfidenceLevel(
                confidence_value
            )
        except ValueError as error:
            raise ValueError(
                f"unknown confidence: {confidence_value}"
            ) from error

        provenance = None

        if provenance_data is not None:
            if not isinstance(provenance_data, dict):
                raise ValueError(
                    "provenance must be an object or null"
                )

            provenance = Provenance.from_dict(
                provenance_data
            )

        return cls(
            entry_id=entry_id,
            form=form,
            meaning=meaning,
            classification=classification,
            confidence=confidence,
            provenance=provenance,
            pronunciation=pronunciation,
            grammar=grammar,
            notes=notes,
            competing_forms=tuple(competing_forms),
        )
