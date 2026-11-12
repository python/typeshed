from collections.abc import Set as AbstractSet
from datetime import datetime
from typing import Any, Literal, TypeAlias, overload

from dateparser.conf import Settings

from ..date import _DetectLanguagesFunction, _Period

_DateFormats: TypeAlias = list[str] | tuple[str, ...] | AbstractSet[str]

@overload
def search_dates(
    text: str,
    languages: list[str] | tuple[str, ...] | AbstractSet[str] | None,
    settings: Settings | dict[str, Any] | None,
    add_detected_language: Literal[True],
    detect_languages_function: _DetectLanguagesFunction | None = None,
    strategy: Literal["split", "ngram"] = "split",
    date_formats: _DateFormats | None = None,
    add_period: Literal[False] = False,
) -> list[tuple[str, datetime, str]] | None: ...
@overload
def search_dates(
    text: str,
    languages: list[str] | tuple[str, ...] | AbstractSet[str] | None = None,
    settings: Settings | dict[str, Any] | None = None,
    *,
    add_detected_language: Literal[True],
    detect_languages_function: _DetectLanguagesFunction | None = None,
    strategy: Literal["split", "ngram"] = "split",
    date_formats: _DateFormats | None = None,
    add_period: Literal[False] = False,
) -> list[tuple[str, datetime, str]] | None: ...
@overload
def search_dates(
    text: str,
    languages: list[str] | tuple[str, ...] | AbstractSet[str] | None = None,
    settings: Settings | dict[str, Any] | None = None,
    add_detected_language: Literal[False] = False,
    detect_languages_function: _DetectLanguagesFunction | None = None,
    strategy: Literal["split", "ngram"] = "split",
    date_formats: _DateFormats | None = None,
    *,
    add_period: Literal[True],
) -> list[tuple[str, datetime, _Period | None]] | None: ...
@overload
def search_dates(
    text: str,
    languages: list[str] | tuple[str, ...] | AbstractSet[str] | None = None,
    settings: Settings | dict[str, Any] | None = None,
    *,
    add_detected_language: Literal[True],
    detect_languages_function: _DetectLanguagesFunction | None = None,
    strategy: Literal["split", "ngram"] = "split",
    date_formats: _DateFormats | None = None,
    add_period: Literal[True],
) -> list[tuple[str, datetime, _Period | None, str]] | None: ...
@overload
def search_dates(
    text: str,
    languages: list[str] | tuple[str, ...] | AbstractSet[str] | None = None,
    settings: Settings | dict[str, Any] | None = None,
    add_detected_language: Literal[False] = False,
    detect_languages_function: _DetectLanguagesFunction | None = None,
    strategy: Literal["split", "ngram"] = "split",
    date_formats: _DateFormats | None = None,
    add_period: Literal[False] = False,
) -> list[tuple[str, datetime]] | None: ...
@overload
def search_dates(
    text: str,
    languages: list[str] | tuple[str, ...] | AbstractSet[str] | None = None,
    settings: Settings | dict[str, Any] | None = None,
    add_detected_language: bool = False,
    detect_languages_function: _DetectLanguagesFunction | None = None,
    strategy: Literal["split", "ngram"] = "split",
    date_formats: _DateFormats | None = None,
    add_period: bool = False,
) -> (
    list[tuple[str, datetime]]
    | list[tuple[str, datetime, str]]
    | list[tuple[str, datetime, _Period | None]]
    | list[tuple[str, datetime, _Period | None, str]]
    | None
): ...
