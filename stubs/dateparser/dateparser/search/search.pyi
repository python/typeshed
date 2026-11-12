import datetime
import re
from collections import OrderedDict
from collections.abc import Iterable, Sequence, Set as AbstractSet
from typing import Any, Final, Literal, TypedDict, type_check_only

from dateparser.conf import Settings
from dateparser.date import DateData, DateDataParser, _DetectLanguagesFunction, _Period
from dateparser.languages.loader import LocaleDataLoader
from dateparser.languages.locale import Locale
from dateparser.search.ngram_search import _NgramDateSearch

@type_check_only
class _SearchDates(TypedDict):
    Language: str | None
    Dates: list[tuple[str, datetime.datetime]] | None

RELATIVE_REG: Final[re.Pattern[str]]
TRANSLATED_RELATIVE_REG: Final[re.Pattern[str]]

def date_is_relative(translation: str) -> bool: ...

class _ExactLanguageSearch:
    loader: LocaleDataLoader
    def __init__(self, loader: LocaleDataLoader) -> None: ...
    def get_current_language(self, shortname: str) -> Locale: ...
    def search(self, shortname: str, text: str, settings: Settings | None) -> tuple[list[str], list[str]]: ...
    def choose_best_split(
        self, possible_parsed_splits: Sequence[list[tuple[DateData, bool]]], possible_substrings_splits: Sequence[list[str]]
    ) -> tuple[list[tuple[DateData, bool]], list[str]]: ...
    def split_by(self, item: str, original: str, splitter: str) -> list[list[list[str]]]: ...
    def split_by_relative_expression(
        self, parser: DateDataParser, item: str, original: str, language: Locale, settings: Settings
    ) -> list[list[list[str]]]: ...
    def split_around_skipped_words(
        self, item: str, original: str, language: Locale, settings: Settings
    ) -> list[list[list[str]]]: ...
    def split_off_trailing_quantity(
        self, item: str, original: str, language: Locale, settings: Settings
    ) -> tuple[list[str], list[str]] | None: ...
    def split_off_numeric_date(
        self, parser: DateDataParser, item: str, original: str, language: Locale, settings: Settings
    ) -> list[list[list[str]]]: ...
    def split_off_leading_number(self, parser: DateDataParser, item: str, original: str) -> list[list[list[str]]]: ...
    def split_if_not_parsed(
        self, parser: DateDataParser, item: str, original: str, language: Locale, settings: Settings
    ) -> list[list[list[str]]]: ...
    def parse_item(
        self,
        parser: DateDataParser,
        item: str,
        translated_item: str,
        relative_base: datetime.datetime | None,
        need_relative_base: bool,
    ) -> tuple[DateData, bool]: ...
    def parse_found_objects(
        self,
        parser: DateDataParser,
        to_parse: Sequence[str],
        original: Sequence[str],
        translated: Sequence[str],
        settings: Settings,
        language: Locale,
        relative_base: datetime.datetime | None = None,
    ) -> tuple[list[tuple[DateData, bool]], list[str]]: ...
    def search_parse(
        self, shortname: str, text: str, settings: Settings
    ) -> list[tuple[str, datetime.datetime, _Period | None]]: ...

class DateSearchWithDetection:
    loader: LocaleDataLoader
    available_language_map: OrderedDict[str, Locale]
    search: _ExactLanguageSearch
    ngram_search: _NgramDateSearch
    def __init__(self) -> None: ...
    def detect_language(
        self,
        text: str,
        languages: list[str] | tuple[str, ...] | AbstractSet[str] | None,
        settings: Settings | dict[str, Any] | None = None,
        detect_languages_function: _DetectLanguagesFunction | None = None,
    ) -> str | None: ...
    def search_dates(
        self,
        text: str,
        languages: list[str] | tuple[str, ...] | AbstractSet[str] | None = None,
        settings: Settings | dict[str, Any] | None = None,
        detect_languages_function: _DetectLanguagesFunction | None = None,
        strategy: Literal["split", "ngram"] = "split",
        date_formats: list[str] | tuple[str, ...] | AbstractSet[str] | None = None,
    ) -> _SearchDates: ...
    def preprocess_text(self, text: str, languages: Iterable[str] | None) -> str: ...
