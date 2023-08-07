from _typeshed import StrPath
from collections.abc import Iterable, Sequence
from datetime import datetime, timedelta, tzinfo
from typing import Any, Protocol
from typing_extensions import Self

__all__ = ["ZoneInfo", "reset_tzpath", "available_timezones", "TZPATH", "ZoneInfoNotFoundError", "InvalidTZPathWarning"]

class _IOBytes(Protocol):
    def read(self, __size: int) -> bytes: ...
    def seek(self, __size: int, __whence: int = ...) -> Any: ...

class ZoneInfo(tzinfo):
    @property
    def key(self) -> str: ...
    def __init__(self, key: str) -> None: ...
    @classmethod
    def no_cache(cls, key: str) -> Self: ...
    @classmethod
    def from_file(cls, __fobj: _IOBytes, key: str | None = None) -> Self: ...
    @classmethod
    def clear_cache(cls, *, only_keys: Iterable[str] | None = None) -> None: ...
    def tzname(self, __dt: datetime | None) -> str | None: ...
    def utcoffset(self, __dt: datetime | None) -> timedelta | None: ...
    def dst(self, __dt: datetime | None) -> timedelta | None: ...

# Note: Both here and in clear_cache, the types allow the use of `str` where
# a sequence of strings is required. This should be remedied if a solution
# to this typing bug is found: https://github.com/python/typing/issues/256
def reset_tzpath(to: Sequence[StrPath] | None = None) -> None: ...
def available_timezones() -> set[str]: ...

TZPATH: tuple[str, ...]

class ZoneInfoNotFoundError(KeyError): ...
class InvalidTZPathWarning(RuntimeWarning): ...

def __dir__() -> list[str]: ...
