import sys

from .tz import (
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

if sys.platform == "win32":
    from .win import tzwin as tzwin, tzwinlocal as tzwinlocal
else:
    tzwin: None
    tzwinlocal: None

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
    "UTC",
    "DeprecatedTzFormatWarning",
]

class DeprecatedTzFormatWarning(Warning): ...
