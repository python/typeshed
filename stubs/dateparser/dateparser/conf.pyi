import datetime
from collections.abc import Callable, Mapping
from typing import Any, Literal, ParamSpec, TypeVar
from typing_extensions import Self, deprecated

from ._parts_of_day import PartsOfDay

_P = ParamSpec("_P")
_R = TypeVar("_R")

class Settings:
    # Next attributes are optional and may be missing.
    # Please keep in sync with _Settings TypedDict
    DATE_ORDER: Literal["DMY", "DYM", "MDY", "MYD", "YDM", "YMD"]
    PREFER_LOCALE_DATE_ORDER: bool
    STRICT_DATE_ORDER: Literal["none", "year", "all"]
    TIMEZONE: str
    TO_TIMEZONE: str
    RETURN_AS_TIMEZONE_AWARE: bool
    TIMEZONE_ABBREVIATIONS: Mapping[str, datetime.timedelta]
    PREFER_MONTH_OF_YEAR: Literal["current", "first", "last"]
    PREFER_DAY_OF_MONTH: Literal["current", "first", "last"]
    PREFER_DATES_FROM: Literal["current_period", "future", "past"]
    RELATIVE_BASE: datetime.datetime
    STRICT_PARSING: bool
    REQUIRE_PARTS: list[Literal["day", "month", "year"]]
    IGNORE_SURROUNDING_TEXT: bool
    SKIP_TOKENS: list[str]
    NORMALIZE: bool
    RETURN_TIME_AS_PERIOD: bool
    RETURN_TIME_SPAN: bool
    DEFAULT_START_OF_WEEK: Literal["monday", "sunday"]
    DEFAULT_DAYS_IN_MONTH: int
    PARTS_OF_DAY: PartsOfDay
    PARSERS: list[Literal["timestamp", "relative-time", "custom-formats", "absolute-time", "no-spaces-time"]]
    DEFAULT_LANGUAGES: list[str]
    USE_GIVEN_LANGUAGE_ORDER: bool
    LANGUAGE_DETECTION_CONFIDENCE_THRESHOLD: float
    CACHE_SIZE_LIMIT: int

    def __init__(self, settings: Mapping[str, Any] | None = None) -> None: ...
    @classmethod
    @deprecated("Deprecated since dateparser 1.5.0; it will be removed in a future version.")
    def get_key(cls, settings: Mapping[str, Any] | None = None) -> str: ...
    def replace(self, mod_settings: Mapping[str, Any] | None = None, **kwds: Any) -> Self: ...

settings: Settings

def apply_settings(f: Callable[_P, _R]) -> Callable[_P, _R]: ...

class SettingValidationError(ValueError): ...

def check_settings(settings: Settings) -> None: ...
