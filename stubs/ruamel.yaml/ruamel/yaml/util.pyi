import datetime
from _typeshed import Incomplete
from collections.abc import Generator
from typing import Any, Callable

from .compat import StreamTextType as StreamTextType

class LazyEval:
    def __init__(self, func: Callable[..., Any], *args, **kwargs) -> None: ...
    def __getattribute__(self, name: str): ...
    def __setattr__(self, name: str, value) -> None: ...

RegExp: Incomplete
timestamp_regexp: Incomplete

def create_timestamp(
    year, month, day, t, hour, minute, second, fraction, tz, tz_sign, tz_hour, tz_minute
) -> datetime.datetime | datetime.date: ...
def load_yaml_guess_indent(stream: StreamTextType, **kw): ...
def configobj_walker(cfg) -> Generator[Incomplete, None, None]: ...
