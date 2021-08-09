from typing import Any, Optional

from .conf import apply_settings
from .timezone_parser import pop_tz_offset_from_string
from .utils import apply_timezone, localize_timezone, strip_braces

class DateParser:
    def parse(self, date_string: Any, parse_method: Any, settings: Optional[Any] = ...): ...

date_parser: Any
