import json
from pathlib import Path

from .state import WorldState, WorldStateError


class WorldStorageError(RuntimeError):
    pass


class JsonWorldStorage:
    def __init__(self, path: Path | str):
        self.path = Path(path)

    def exists(self) -> bool:
        return self.path.is_file()

    def save(self, world: WorldState) -> None:
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
                    world.to_dict(),
                    file,
                    ensure_ascii=False,
                    indent=2,
                    sort_keys=True,
                )
                file.write("\n")

            temporary_path.replace(self.path)
        except OSError as error:
            raise WorldStorageError(
                f"failed to save world state: {error}"
            ) from error
        finally:
            if temporary_path.exists():
                temporary_path.unlink()

    def load(self) -> WorldState:
        try:
            with self.path.open(
                "r",
                encoding="utf-8",
            ) as file:
                data = json.load(file)
        except FileNotFoundError as error:
            raise WorldStorageError(
                f"world state does not exist: {self.path}"
            ) from error
        except (
            OSError,
            json.JSONDecodeError,
        ) as error:
            raise WorldStorageError(
                f"failed to load world state: {error}"
            ) from error

        if not isinstance(data, dict):
            raise WorldStorageError(
                "world state root must be an object"
            )

        try:
            return WorldState.from_dict(data)
        except (
            ValueError,
            WorldStateError,
        ) as error:
            raise WorldStorageError(
                f"invalid world state: {error}"
            ) from error
