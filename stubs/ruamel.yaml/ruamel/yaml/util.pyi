import datetime
from _typeshed import Incomplete
from typing import Any, Callable

from .compat import StreamTextType as StreamTextType

class LazyEval:
    def __init__(self, func: Callable[..., Any], *args: Any, **kwargs: Any) -> None: ...
    def __getattribute__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...

RegExp: Incomplete
timestamp_regexp: Incomplete

def create_timestamp(
    year: Any,
    month: Any,
    day: Any,
    t: Any,
    hour: Any,
    minute: Any,
    second: Any,
    fraction: Any,
    tz: Any,
    tz_sign: Any,
    tz_hour: Any,
    tz_minute: Any,
) -> datetime.datetime | datetime.date: ...
def load_yaml_guess_indent(stream: StreamTextType, **kw: Any) -> Any: ...
def configobj_walker(cfg: Any) -> Any: ...
