import json
from pathlib import Path

from .lexicon import Lexicon, LexiconError


class LexiconStorageError(RuntimeError):
    pass


class JsonLexiconStorage:
    def __init__(self, path: Path | str):
        self.path = Path(path)

    def exists(self) -> bool:
        return self.path.is_file()

    def save(self, lexicon: Lexicon) -> None:
        self.path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        temporary_path = self.path.with_suffix(
            f"{self.path.suffix}.tmp"
        )

        try:
            with temporary_path.open(
                "w",
                encoding="utf-8",
            ) as file:
                json.dump(
                    lexicon.to_dict(),
                    file,
                    ensure_ascii=False,
                    indent=2,
                    sort_keys=True,
                )
                file.write("\n")

            temporary_path.replace(self.path)
        except OSError as error:
            raise LexiconStorageError(
                f"failed to save lexicon: {error}"
            ) from error
        finally:
            if temporary_path.exists():
                temporary_path.unlink()

    def load(self) -> Lexicon:
        try:
            with self.path.open(
                "r",
                encoding="utf-8",
            ) as file:
                data = json.load(file)
        except FileNotFoundError as error:
            raise LexiconStorageError(
                f"lexicon does not exist: {self.path}"
            ) from error
        except (
            OSError,
            json.JSONDecodeError,
        ) as error:
            raise LexiconStorageError(
                f"failed to load lexicon: {error}"
            ) from error

        if not isinstance(data, dict):
            raise LexiconStorageError(
                "lexicon root must be an object"
            )

        try:
            return Lexicon.from_dict(data)
        except (
            ValueError,
            LexiconError,
        ) as error:
            raise LexiconStorageError(
                f"invalid lexicon: {error}"
            ) from error
