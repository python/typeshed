import datetime
from collections.abc import Mapping
from typing import Any, Final, Literal, TypedDict, type_check_only

from dateparser.conf import Settings

from ._parts_of_day import PartOfDay as PartOfDay, PartsOfDay as PartsOfDay
from .date import DateDataParser as DateDataParser, _DetectLanguagesFunction

__version__: Final[str]

_default_parser: DateDataParser

@type_check_only
class _Settings(TypedDict, total=False):  # noqa: Y049
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

def parse(
    date_string: str,
    date_formats: list[str] | tuple[str, ...] | set[str] | None = None,
    languages: list[str] | tuple[str, ...] | set[str] | None = None,
    locales: list[str] | tuple[str, ...] | set[str] | None = None,
    region: str | None = None,
    settings: Settings | dict[str, Any] | None = None,
    detect_languages_function: _DetectLanguagesFunction | None = None,
) -> datetime.datetime | None: ...
