from .parser import time_parser as time_parser
from .timezone_parser import pop_tz_offset_from_string as pop_tz_offset_from_string
from dateparser.utils import (
    apply_timezone as apply_timezone,
    localize_timezone as localize_timezone,
    strip_braces as strip_braces,
)
from typing import Any, Optional

PATTERN: Any

class FreshnessDateDataParser:
    def get_local_tz(self): ...
    def parse(self, date_string: Any, settings: Any): ...
    def get_kwargs(self, date_string: Any): ...
    def get_date_data(self, date_string: Any, settings: Optional[Any] = ...): ...

freshness_date_parser: Any
