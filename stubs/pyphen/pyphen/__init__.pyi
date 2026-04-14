from collections.abc import Generator
from pathlib import Path
from typing import Any
from typing_extensions import Self

__all__ = ("LANGUAGES", "Pyphen", "language_fallback")
LANGUAGES: dict[str, Path]

def language_fallback(language: str) -> str: ...

class AlternativeParser:
    change: str
    index: int
    cut: int

    def __init__(self, pattern: str, alternative: str) -> None: ...
    def __call__(self, value: str) -> int: ...

class DataInt(int):
    def __new__(cls, value: int, data: Any = ..., reference: DataInt | None = ...) -> Self: ...

class HyphDict:
    patterns: dict[str, tuple[int, tuple[int, ...]]]
    cache: dict[str, list[DataInt]]
    maxlen: int

    def __init__(self, path: Path) -> None: ...
    def positions(self, word: str) -> list[DataInt]: ...

class Pyphen:
    hd: HyphDict

    def __init__(
        self, filename: str | Path | None = ..., lang: str | None = ..., left: int = 2, right: int = 2, cache: bool = True
    ) -> None: ...
    def positions(self, word: str) -> list[DataInt]: ...
    def iterate(self, word: str) -> Generator[tuple[str, str], None, None]: ...
    def wrap(self, word: str, width: int, hyphen: str = "-") -> tuple[str, str] | None: ...
    def inserted(self, word: str, hyphen: str = "-") -> str: ...
    __call__ = iterate
