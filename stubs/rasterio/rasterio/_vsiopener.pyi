from abc import ABC, abstractmethod
from contextlib import AbstractContextManager
from typing import Any, BinaryIO

from rasterio.errors import OpenerRegistrationError as OpenerRegistrationError

class FileContainer(ABC):
    @abstractmethod
    def open(self, path: str, mode: str = "r", **kwds: Any) -> BinaryIO: ...

class MultiByteRangeResource(ABC):
    @abstractmethod
    def get_byte_ranges(self, offsets: list[int], sizes: list[int]) -> list[bytes]: ...

class MultiByteRangeResourceContainer(FileContainer):
    @abstractmethod
    def open(self, path: str, **kwds: Any) -> MultiByteRangeResource: ...  # type: ignore[override]

def to_pyopener(obj: Any) -> FileContainer: ...
def _opener_registration(urlpath: str, obj: Any) -> AbstractContextManager[str]: ...
