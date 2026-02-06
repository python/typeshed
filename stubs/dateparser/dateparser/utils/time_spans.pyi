from datetime import date, datetime
from typing import TypedDict, overload, type_check_only
from typing_extensions import NotRequired

from dateparser import _Settings

@type_check_only
class _SpanInformation(TypedDict):
    type: str
    direction: str
    matched_text: str
    start_pos: int
    end_pos: int
    number: NotRequired[int]

@overload
def get_week_start(date: datetime, start_of_week: str = "monday") -> datetime: ...
@overload
def get_week_start(date: date, start_of_week: str = "monday") -> date: ...
@overload
def get_week_end(date: datetime, start_of_week: str = "monday") -> datetime: ...
@overload
def get_week_end(date: date, start_of_week: str = "monday") -> date: ...
def detect_time_span(text: str) -> _SpanInformation | None: ...
@overload
def generate_time_span(
    span_info: _SpanInformation, base_date: datetime | None = None, settings: _Settings | None = None
) -> tuple[datetime, datetime]: ...
@overload
def generate_time_span(
    span_info: _SpanInformation, base_date: date = ..., settings: _Settings | None = None
) -> tuple[date, date]: ...
