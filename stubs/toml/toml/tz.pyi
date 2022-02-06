from _typeshed import Self
from datetime import datetime, timedelta, tzinfo
from typing import Any


class TomlTz(tzinfo):
    def __init__(self, toml_offset: str) -> None: ...
    def __deepcopy__(self: Self, memo: Any) -> Self: ...
    def tzname(self, dt: datetime | None) -> str: ...
    def utcoffset(self, dt: datetime | None) -> timedelta: ...
    def dst(self, dt: datetime | None) -> timedelta: ...
