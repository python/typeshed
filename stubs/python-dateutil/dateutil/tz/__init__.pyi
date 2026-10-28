import builtins
import sys
from collections.abc import Sequence
from datetime import datetime
from typing_extensions import Self
from zoneinfo import reset_tzpath as reset_tzpath

from ._common import tzrangebase
from .tz import (
    DeprecatedTzKeyWarning as DeprecatedTzKeyWarning,
    available_iana_timezones as available_iana_timezones,
    datetime_ambiguous as datetime_ambiguous,
    datetime_exists as datetime_exists,
    enfold as enfold,
    gettz as gettz,
    resolve_imaginary as resolve_imaginary,
    tzfile as tzfile,
    tzical as tzical,
    tzlocal as tzlocal,
    tzoffset as tzoffset,
    tzrange as tzrange,
    tzstr as tzstr,
    tzutc as tzutc,
)

# UTC, tzwin, tzwinlocal are defined in this class
# otherwise pyright complains about unknown import symbol:
if sys.platform == "win32":
    class tzwinbase(tzrangebase):
        hasdst: bool
        def __eq__(self, other: tzwinbase) -> bool: ...  # type: ignore[override]
        @staticmethod
        def list() -> builtins.list[str]: ...
        def display(self) -> str | None: ...
        def transitions(self, year: int) -> tuple[datetime, datetime] | None: ...

    class tzwin(tzwinbase):
        hasdst: bool
        def __init__(self, name: str) -> None: ...
        def __reduce__(self) -> tuple[type[Self], tuple[str, ...]]: ...  # type: ignore[override]

    class tzwinlocal(tzwinbase):
        hasdst: bool
        def __init__(self) -> None: ...
        def __reduce__(self) -> tuple[type[Self], tuple[str, ...]]: ...  # type: ignore[override]

else:
    tzwin: None
    tzwinlocal: None

TZPATH: Sequence[str]

UTC: tzutc

__all__ = [
    "tzutc",
    "tzoffset",
    "tzlocal",
    "tzfile",
    "tzrange",
    "tzstr",
    "tzical",
    "tzwin",
    "tzwinlocal",
    "gettz",
    "enfold",
    "datetime_ambiguous",
    "datetime_exists",
    "resolve_imaginary",
    "available_iana_timezones",
    "UTC",
    "TZPATH",
    "reset_tzpath",
    "DeprecatedTzKeyWarning",
    "DeprecatedTzFormatWarning",
]

class DeprecatedTzFormatWarning(Warning): ...
