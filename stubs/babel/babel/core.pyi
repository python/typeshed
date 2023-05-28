from collections.abc import Iterable, Mapping
from typing import Any, overload
from typing_extensions import Literal, TypeAlias

from babel.localedata import LocaleDataDict
from babel.plural import PluralRule

class UnknownLocaleError(Exception):
    identifier: str
    def __init__(self, identifier: str) -> None: ...

class Locale:
    language: str
    territory: str | None
    script: str | None
    variant: str | None
    def __init__(
        self, language: str, territory: str | None = None, script: str | None = None, variant: str | None = None
    ) -> None: ...
    @classmethod
    def default(cls, category: str | None = None, aliases: Mapping[str, str] = ...) -> Locale: ...
    @classmethod
    def negotiate(
        cls, preferred: Iterable[str], available: Iterable[str], sep: str = "_", aliases: Mapping[str, str] = ...
    ) -> Locale | None: ...
    @overload
    @classmethod
    def parse(cls, identifier: None, sep: str = "_", resolve_likely_subtags: bool = True) -> None: ...
    @overload
    @classmethod
    def parse(cls, identifier: str | Locale, sep: str = "_", resolve_likely_subtags: bool = True) -> Locale: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def get_display_name(self, locale: Locale | str | None = None) -> str | None: ...
    @property
    def display_name(self) -> str | None: ...
    def get_language_name(self, locale: Locale | str | None = None) -> str | None: ...
    @property
    def language_name(self) -> str | None: ...
    def get_territory_name(self, locale: Locale | str | None = None) -> str | None: ...
    @property
    def territory_name(self) -> str | None: ...
    def get_script_name(self, locale: Locale | str | None = None) -> str | None: ...
    @property
    def script_name(self) -> str | None: ...
    @property
    def english_name(self) -> str | None: ...
    @property
    def languages(self) -> LocaleDataDict: ...
    @property
    def scripts(self) -> LocaleDataDict: ...
    @property
    def territories(self) -> LocaleDataDict: ...
    @property
    def variants(self) -> LocaleDataDict: ...
    @property
    def currencies(self) -> LocaleDataDict: ...
    @property
    def currency_symbols(self) -> LocaleDataDict: ...
    @property
    def number_symbols(self) -> LocaleDataDict: ...
    @property
    def decimal_formats(self) -> LocaleDataDict: ...
    @property
    def compact_decimal_formats(self) -> LocaleDataDict: ...
    @property
    def currency_formats(self) -> LocaleDataDict: ...
    @property
    def percent_formats(self) -> LocaleDataDict: ...
    @property
    def scientific_formats(self) -> LocaleDataDict: ...
    @property
    def periods(self) -> LocaleDataDict: ...
    @property
    def day_periods(self) -> LocaleDataDict: ...
    @property
    def day_period_rules(self) -> LocaleDataDict: ...
    @property
    def days(self) -> LocaleDataDict: ...
    @property
    def months(self) -> LocaleDataDict: ...
    @property
    def quarters(self) -> LocaleDataDict: ...
    @property
    def eras(self) -> LocaleDataDict: ...
    @property
    def time_zones(self) -> LocaleDataDict: ...
    @property
    def meta_zones(self) -> LocaleDataDict: ...
    @property
    def zone_formats(self) -> LocaleDataDict: ...
    @property
    def first_week_day(self) -> int: ...
    @property
    def weekend_start(self) -> int: ...
    @property
    def weekend_end(self) -> int: ...
    @property
    def min_week_days(self) -> int: ...
    @property
    def date_formats(self) -> LocaleDataDict: ...
    @property
    def time_formats(self) -> LocaleDataDict: ...
    @property
    def datetime_formats(self) -> LocaleDataDict: ...
    @property
    def datetime_skeletons(self) -> LocaleDataDict: ...
    @property
    def interval_formats(self) -> LocaleDataDict: ...
    @property
    def plural_form(self) -> PluralRule: ...
    @property
    def list_patterns(self) -> LocaleDataDict: ...
    @property
    def ordinal_form(self) -> PluralRule: ...
    @property
    def measurement_systems(self) -> LocaleDataDict: ...
    @property
    def character_order(self) -> str: ...
    @property
    def text_direction(self) -> str: ...
    @property
    def unit_display_names(self) -> LocaleDataDict: ...

def default_locale(category: str | None = None, aliases: Mapping[str, str] = ...) -> str | None: ...
def negotiate_locale(
    preferred: Iterable[str], available: Iterable[str], sep: str = "_", aliases: Mapping[str, str] = ...
) -> str | None: ...
def parse_locale(identifier: str, sep: str = "_") -> tuple[str, str | None, str | None, str | None]: ...
def get_locale_identifier(tup: tuple[str, str | None, str | None, str | None], sep: str = "_") -> str: ...
def get_global(key: _GLOBAL_KEY) -> Mapping[str, Any]: ...

_GLOBAL_KEY: TypeAlias = Literal[
    "all_currencies",
    "currency_fractions",
    "language_aliases",
    "likely_subtags",
    "parent_exceptions",
    "script_aliases",
    "territory_aliases",
    "territory_currencies",
    "territory_languages",
    "territory_zones",
    "variant_aliases",
    "windows_zone_mapping",
    "zone_aliases",
    "zone_territories",
]
