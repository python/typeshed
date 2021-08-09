from typing import Any, Optional

from dateparser.utils import get_last_day_of_month, get_next_leap_year, get_previous_leap_year, set_correct_day_from_settings
from dateparser.utils.strptime import strptime

NSP_COMPATIBLE: Any
MERIDIAN: Any
MICROSECOND: Any
EIGHT_DIGIT: Any
HOUR_MINUTE_REGEX: Any

def no_space_parser_eligibile(datestring: Any): ...
def get_unresolved_attrs(parser_object: Any): ...

date_order_chart: Any

def resolve_date_order(order: Any, lst: Optional[Any] = ...): ...

class _time_parser:
    time_directives: Any = ...
    def __call__(self, timestring: Any): ...

time_parser: Any

class _no_spaces_parser:
    period: Any = ...
    date_formats: Any = ...
    def __init__(self, *args: Any, **kwargs: Any): ...
    @classmethod
    def parse(cls, datestring: Any, settings: Any): ...

class _parser:
    alpha_directives: Any = ...
    num_directives: Any = ...
    settings: Any = ...
    tokens: Any = ...
    filtered_tokens: Any = ...
    unset_tokens: Any = ...
    day: Any = ...
    month: Any = ...
    year: Any = ...
    time: Any = ...
    auto_order: Any = ...
    ordered_num_directives: Any = ...
    def __init__(self, tokens: Any, settings: Any): ...
    @classmethod
    def parse(cls, datestring: Any, settings: Any): ...

class tokenizer:
    digits: str = ...
    letters: str = ...
    instream: Any = ...
    def __init__(self, ds: Any) -> None: ...
    def tokenize(self) -> None: ...
