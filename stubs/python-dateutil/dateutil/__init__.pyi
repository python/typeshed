# These are all lazy-loaded on demand at runtime
from . import (
    easter as easter,
    parser as parser,
    relativedelta as relativedelta,
    rrule as rrule,
    tz as tz,
    utils as utils,
    zoneinfo as zoneinfo,
)

__all__ = ["easter", "parser", "relativedelta", "rrule", "tz", "utils", "zoneinfo"]

def __dir__() -> list[str]: ...
