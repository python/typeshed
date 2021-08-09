from datetime import tzinfo
from typing import Any

from .timezones import timezone_info_list

class StaticTzInfo(tzinfo):
    def __init__(self, name: Any, offset: Any) -> None: ...
    def tzname(self, dt: Any): ...
    def utcoffset(self, dt: Any): ...
    def dst(self, dt: Any): ...
    def localize(self, dt: Any, is_dst: bool = ...): ...
    def __getinitargs__(self): ...

def pop_tz_offset_from_string(date_string: Any, as_offset: bool = ...): ...
def word_is_tz(word: Any): ...
def convert_to_local_tz(datetime_obj: Any, datetime_tz_offset: Any): ...
def build_tz_offsets(search_regex_parts: Any): ...
def get_local_tz_offset(): ...

local_tz_offset: Any
