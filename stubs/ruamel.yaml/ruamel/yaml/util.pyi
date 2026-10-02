import re
from collections.abc import Callable, Iterator
from datetime import date, datetime
from typing import Any, Final

from configobj import (  # type: ignore[import-not-found]  # pyright: ignore[reportMissingImports]  # ty:ignore[unresolved-import]  # pyrefly: ignore [missing-import]
    ConfigObj as _ConfigObj,
)

from .compat import _ReadStream
from .main import _YAMLObject

class LazyEval:
    def __init__(self, func: Callable[..., object], *args, **kwargs) -> None: ...
    # Attribute access is forwarded dynamically, so its result cannot be expressed without Any.
    def __getattribute__(self, name: str, /) -> Any: ...
    def __setattr__(self, name: str, value: object, /) -> None: ...

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
def load_yaml_guess_indent(stream: _ReadStream, /, **kw: object) -> tuple[_YAMLObject, int | None, int | None]: ...
def configobj_walker(cfg: _ConfigObj, /) -> Iterator[str]: ...
