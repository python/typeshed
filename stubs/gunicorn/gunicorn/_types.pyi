from collections.abc import Iterable
from typing import Any, Callable, TypeAlias

Status: TypeAlias = str
Headers: TypeAlias = list[tuple[str, str]]

Environ: TypeAlias = dict[str, Any]
StartResponse: TypeAlias = Callable[[Status, Headers], None]
ResponseBody: TypeAlias = Iterable[bytes]

WSGIApp: TypeAlias = Callable[[Environ, StartResponse], ResponseBody]
