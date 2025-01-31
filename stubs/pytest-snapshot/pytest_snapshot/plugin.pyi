from pathlib import Path
from types import TracebackType
from typing import Any, Generator, Union

import pytest

@pytest.fixture
def snapshot(request: pytest.FixtureRequest) -> Generator[Snapshot, Any, None]:
    ...


class Snapshot:
    def __init__(
        self,
        snapshot_update: bool,
        allow_snapshot_deletion: bool,
        snapshot_dir: Path,
    ): ...
    def __enter__(self): ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...

    @property
    def snapshot_dir(self) -> Path:
        ...

    @snapshot_dir.setter
    def snapshot_dir(self, value: str | Path) -> None: ...

    def assert_match(
        self,
        value: Union[str, bytes],
        snapshot_name: Union[str, Path],
    ) -> None: ...

    def assert_match_dir(
        self,
        dir_dict: dict[Any, Any],
        snapshot_dir_name: Union[str, Path],
    ) -> None: ...
