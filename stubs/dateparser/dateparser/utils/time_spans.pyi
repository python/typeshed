import datetime
from typing import TypedDict, TypeVar, overload, type_check_only
from typing_extensions import NotRequired, deprecated

from dateparser.conf import Settings

_DateT = TypeVar("_DateT", bound=datetime.date)

@type_check_only
class _SpanInformation(TypedDict):
    type: str
    direction: str
    matched_text: str
    start_pos: int
    end_pos: int
    number: NotRequired[int]

@deprecated("Deprecated since dateparser 1.5.0; it will be removed in a future version.")
def get_week_start(date: _DateT, start_of_week: str = "monday") -> _DateT: ...
@deprecated("Deprecated since dateparser 1.5.0; it will be removed in a future version.")
def get_week_end(date: _DateT, start_of_week: str = "monday") -> _DateT: ...
def detect_time_span(text: str) -> _SpanInformation | None: ...

@overload
def generate_time_span(span_info: _SpanInformation, base_date: _DateT, settings: Settings) -> tuple[_DateT, _DateT]: ...
@overload
@deprecated("Calling generate_time_span() without base_date or settings is deprecated since dateparser 1.5.0.")
def generate_time_span(
    span_info: _SpanInformation, base_date: _DateT | None = None, settings: Settings | None = None
) -> tuple[_DateT, _DateT]: ...
