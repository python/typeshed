from collections import OrderedDict
from typing import Any, Dict, Optional, Union, List

from dateparser.timezone_parser import StaticTzInfo as StaticTzInfo

def strip_braces(date_string: str) -> str: ...
def normalize_unicode(string: str, form: str = ...) -> str: ...
def combine_dicts(primary_dict: Dict[str, Union[List[Any], Dict[Any, Any]]], supplementary_dict: Dict[str, str]) -> OrderedDict[str, Union[str, List[Any]]]: ...
def find_date_separator(format: Any) -> Any: ...
def localize_timezone(date_time: Any, tz_string: Any): ...
def apply_tzdatabase_timezone(date_time: Any, pytz_string: Any): ...
def apply_dateparser_timezone(utc_datetime: Any, offset_or_timezone_abb: Any): ...
def apply_timezone(date_time: Any, tz_string: Any): ...
def apply_timezone_from_settings(date_obj: Any, settings: Any): ...
def get_last_day_of_month(year: Any, month: Any): ...
def get_previous_leap_year(year: Any): ...
def get_next_leap_year(year: Any): ...
def set_correct_day_from_settings(date_obj: Any, settings: Any, current_day: Optional[Any] = ...): ...
def registry(cls): ...
def get_logger() -> Any: ...
def setup_logging() -> None: ...
