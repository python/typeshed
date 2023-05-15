from pytz import BaseTzInfo

from tzlocal.utils import assert_tz_offset

__all__ = [
    "get_localzone",
    "get_localzone_name",
    "reload_localzone",
    "assert_tz_offset",
]

def reload_localzone() -> None: ...
def get_localzone() -> BaseTzInfo: ...
def get_localzone_name() -> str: ...
