import re
from collections.abc import Callable, Iterator
from datetime import date, datetime
from typing import Any, Final

from configobj import ConfigObj  # type: ignore[import-not-found]  # pyright: ignore[reportMissingImports]

from .compat import _ReadStream

class LazyEval:
    def __init__(self, func: Callable[..., Any], *args, **kwargs) -> None: ...
    def __getattribute__(self, name: str, /) -> Any: ...
    def __setattr__(self, name: str, value: Any, /) -> None: ...

RegExp: Final = re.compile
timestamp_regexp: Final[re.Pattern[str]]

def create_timestamp(
    *,
    year: str,
    month: str,
    day: str,
    t: str | None,
    hour: str | None,
    minute: str | None,
    second: str | None,
    fraction: str | None,
    tz: str | None,
    tz_sign: str | None,
    tz_hour: str | None,
    tz_minute: str | None,
) -> date | datetime: ...
def load_yaml_guess_indent(stream: _ReadStream, /) -> tuple[Any, int | None, int | None]: ...
def configobj_walker(cfg: ConfigObj, /) -> Iterator[str]: ...
