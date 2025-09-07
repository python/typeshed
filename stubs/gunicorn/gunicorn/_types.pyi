from collections.abc import Iterable
from typing import Any, Callable

type _StatusType = str
type _HeadersType = list[tuple[str, str]]

type _EnvironType = dict[str, Any]
type _StartResponseType = Callable[[_StatusType, _HeadersType], None]
type _ResponseBodyType = Iterable[bytes]

type _WSGIAppType = Callable[[_EnvironType, _StartResponseType], _ResponseBodyType]
