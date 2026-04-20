from collections.abc import Mapping
from typing import Any

class _Utils:
    profiler: type[Any]
    def __init__(self, profiler: type[Any]) -> None: ...
    def run(self, statement: str, filename: str | None, sort: str | int) -> None: ...
    def runctx(
        self, statement: str, globals: dict[str, Any], locals: Mapping[str, Any], filename: str | None, sort: str | int
    ) -> None: ...
