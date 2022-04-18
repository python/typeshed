from collections import OrderedDict
from collections.abc import Mapping
from typing import Any

def strip_braces(date_string: str) -> str: ...
def normalize_unicode(string: str, form: str = ...) -> str: ...
def combine_dicts(
    primary_dict: Mapping[Any, Any], supplementary_dict: Mapping[Any, Any]
) -> OrderedDict[str, str | list[Any]]: ...
def find_date_separator(format) -> Any: ...
def localize_timezone(date_time, tz_string): ...
def apply_tzdatabase_timezone(date_time, pytz_string): ...
def apply_dateparser_timezone(utc_datetime, offset_or_timezone_abb): ...
def apply_timezone(date_time, tz_string): ...
def apply_timezone_from_settings(date_obj, settings): ...
def get_last_day_of_month(year, month): ...
def get_previous_leap_year(year): ...
def get_next_leap_year(year): ...
def set_correct_day_from_settings(date_obj, settings, current_day: Any | None = ...): ...
def registry(cls): ...
def get_logger() -> Any: ...
def setup_logging() -> None: ...
