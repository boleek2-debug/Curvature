import json

import pytest

from core.language import (
    ConfidenceLevel,
    JsonLexiconStorage,
    LanguageEntry,
    LanguageFormClass,
    Lexicon,
    LexiconError,
    LexiconStorageError,
    Provenance,
)


def test_reconstructed_entry_requires_provenance() -> None:
    with pytest.raises(
        ValueError,
        match="require provenance",
    ):
        LanguageEntry(
            entry_id="water",
            form="voda",
            meaning="water",
            classification=(
                LanguageFormClass.RECONSTRUCTED
            ),
            confidence=ConfidenceLevel.HIGH,
        )


def test_curvature_derived_entry_cannot_claim_high_confidence(
) -> None:
    with pytest.raises(
        ValueError,
        match="cannot claim high historical confidence",
    ):
        LanguageEntry(
            entry_id="created-word",
            form="novotvar",
            meaning="created term",
            classification=(
                LanguageFormClass.CURVATURE_DERIVED
            ),
            confidence=ConfidenceLevel.HIGH,
        )


def test_fictional_entry_cannot_claim_historical_provenance(
) -> None:
    with pytest.raises(
        ValueError,
        match="must not claim historical provenance",
    ):
        LanguageEntry(
            entry_id="fictional-word",
            form="zoryn",
            meaning="fictional term",
            classification=LanguageFormClass.FICTIONAL,
            confidence=ConfidenceLevel.UNKNOWN,
            provenance=Provenance(
                source="invented",
                period="fictional",
                region="Curvature",
            ),
        )


def test_lexicon_adds_and_finds_entry() -> None:
    entry = LanguageEntry(
        entry_id="water",
        form="voda",
        meaning="water",
        classification=LanguageFormClass.RECONSTRUCTED,
        confidence=ConfidenceLevel.HIGH,
        provenance=Provenance(
            source="Proto-Slavic reconstruction",
            period="Proto-Slavic",
            region="Slavic",
        ),
    )
    lexicon = Lexicon(
        language_id="curvature-base",
        name="Curvature Base Language",
    )

    lexicon.add_entry(entry)

    assert lexicon.entries["water"] == entry
    assert lexicon.get_by_form("voda") == (entry,)


def test_lexicon_rejects_duplicate_entry_id() -> None:
    entry = LanguageEntry(
        entry_id="water",
        form="voda",
        meaning="water",
        classification=LanguageFormClass.RECONSTRUCTED,
        confidence=ConfidenceLevel.HIGH,
        provenance=Provenance(
            source="Proto-Slavic reconstruction",
            period="Proto-Slavic",
            region="Slavic",
        ),
    )
    lexicon = Lexicon(
        language_id="curvature-base",
        name="Curvature Base Language",
    )
    lexicon.add_entry(entry)

    with pytest.raises(
        LexiconError,
        match="entry already exists",
    ):
        lexicon.add_entry(entry)


def test_lexicon_survives_save_and_load(
    tmp_path,
) -> None:
    storage = JsonLexiconStorage(
        tmp_path / "lexicon.json"
    )
    lexicon = Lexicon(
        language_id="curvature-base",
        name="Curvature Base Language",
    )
    lexicon.add_entry(
        LanguageEntry(
            entry_id="water",
            form="voda",
            meaning="water",
            classification=(
                LanguageFormClass.RECONSTRUCTED
            ),
            confidence=ConfidenceLevel.HIGH,
            provenance=Provenance(
                source="Proto-Slavic reconstruction",
                period="Proto-Slavic",
                region="Slavic",
            ),
            competing_forms=("woda",),
        )
    )

    storage.save(lexicon)
    loaded = storage.load()

    assert loaded == lexicon


def test_lexicon_storage_writes_versioned_json(
    tmp_path,
) -> None:
    storage = JsonLexiconStorage(
        tmp_path / "lexicon.json"
    )
    lexicon = Lexicon(
        language_id="curvature-base",
        name="Curvature Base Language",
    )

    storage.save(lexicon)

    data = json.loads(
        storage.path.read_text(
            encoding="utf-8",
        )
    )

    assert data["format_version"] == 1
    assert data["language_id"] == "curvature-base"


def test_lexicon_storage_rejects_missing_file(
    tmp_path,
) -> None:
    storage = JsonLexiconStorage(
        tmp_path / "missing.json"
    )

    with pytest.raises(
        LexiconStorageError,
        match="does not exist",
    ):
        storage.load()
