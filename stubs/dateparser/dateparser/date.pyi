from typing import Any

APOSTROPHE_LOOK_ALIKE_CHARS: Any
RE_NBSP: Any
RE_SPACES: Any
RE_TRIM_SPACES: Any
RE_TRIM_COLONS: Any
RE_SANITIZE_SKIP: Any
RE_SANITIZE_RUSSIAN: Any
RE_SANITIZE_PERIOD: Any
RE_SANITIZE_ON: Any
RE_SANITIZE_APOSTROPHE: Any
RE_SEARCH_TIMESTAMP: Any

def sanitize_spaces(date_string): ...
def date_range(begin, end, **kwargs) -> None: ...
def get_intersecting_periods(low, high, period: str = ...) -> None: ...
def sanitize_date(date_string): ...
def get_date_from_timestamp(date_string, settings): ...
def parse_with_formats(date_string, date_formats, settings): ...

class _DateLocaleParser:
    locale: Any
    date_string: Any
    date_formats: Any
    def __init__(self, locale, date_string, date_formats, settings: Any | None = ...) -> None: ...
    @classmethod
    def parse(cls, locale, date_string, date_formats: Any | None = ..., settings: Any | None = ...): ...

class DateData:
    date_obj: Any
    period: Any
    locale: Any
    def __init__(self, *, date_obj: Any | None = ..., period: Any | None = ..., locale: Any | None = ...) -> None: ...
    def __getitem__(self, k): ...
    def __setitem__(self, k, v) -> None: ...

class DateDataParser:
    locale_loader: Any
    try_previous_locales: Any
    use_given_order: Any
    languages: Any
    locales: Any
    region: Any
    previous_locales: Any
    def __init__(
        self,
        languages: Any | None = ...,
        locales: Any | None = ...,
        region: Any | None = ...,
        try_previous_locales: bool = ...,
        use_given_order: bool = ...,
        settings: Any | None = ...,
    ) -> None: ...
    def get_date_data(self, date_string, date_formats: Any | None = ...): ...
    def get_date_tuple(self, *args, **kwargs): ...
