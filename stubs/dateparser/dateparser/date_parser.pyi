from .conf import apply_settings as apply_settings
from .timezone_parser import pop_tz_offset_from_string as pop_tz_offset_from_string
from .utils import apply_timezone as apply_timezone, localize_timezone as localize_timezone, strip_braces as strip_braces
from typing import Any, Optional

class DateParser:
    def parse(self, date_string: Any, parse_method: Any, settings: Optional[Any] = ...): ...

date_parser: Any
