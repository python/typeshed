from collections.abc import Iterable
from datetime import datetime, timedelta, tzinfo
from typing_extensions import Self
from zoneinfo._common import ZoneInfoNotFoundError as ZoneInfoNotFoundError, _IOBytes  # pyright: ignore
from zoneinfo._tzpath import (  # pyright: ignore [reportMissingTypeStubs]
    TZPATH as TZPATH,
    InvalidTZPathWarning as InvalidTZPathWarning,
    available_timezones as available_timezones,
    reset_tzpath as reset_tzpath,
)

# the pragmas above are because pyright errors on the imports
# when sys.version_info < (3, 9)
# line 4 should have the specifier [reportMissingTypeStubs, reportGeneralTypeIssues]
# but ruff is moving the comment to it's own line if it's that long

__all__ = ["ZoneInfo", "reset_tzpath", "available_timezones", "TZPATH", "ZoneInfoNotFoundError", "InvalidTZPathWarning"]

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

def __dir__() -> list[str]: ...
