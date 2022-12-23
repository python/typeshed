# Stubs-only module with type aliases for ExifRead.

from collections.abc import Callable
from typing import Protocol
from typing_extensions import Literal, TypeAlias

TagDict: TypeAlias = dict[str, tuple[str] | tuple[str, dict[int, str | Callable[[bytes], str]]]]

class Reader(Protocol):
    def __iter__(self) -> bytes: ...
    def read(self, __size: int) -> bytes: ...
    def tell(self) -> int: ...
    def seek(self, __offset: int, __whence: Literal[0, 1] = ...) -> object: ...
