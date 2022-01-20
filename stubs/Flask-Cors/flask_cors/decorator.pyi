from datetime import timedelta
from logging import Logger
from typing import Any, Callable
from typing_extensions import ParamSpec

_P = ParamSpec("_P")

LOG: Logger

def cross_origin(
    *args: Any,
    origins: str | list[str],
    methods: str | list[str],
    expose_headers: str | list[str],
    allow_headers: str | list[str],
    supports_credentials: bool,
    max_age: timedelta | int | str | None,
    send_wildcard: bool,
    vary_header: bool,
    automatic_options: bool,
) -> Callable[[Callable[_P, Any]], Callable[_P, Any]]: ...
