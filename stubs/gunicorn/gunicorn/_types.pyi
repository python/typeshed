from collections.abc import Iterable
from typing import Any, Callable, LiteralString

type _StatusType = str
type _HeadersType = list[tuple[str, str]]

type _EnvironType = dict[str, Any]
type _StartResponseType = Callable[[_StatusType, _HeadersType], None]
type _ResponseBodyType = Iterable[bytes]

type _WSGIAppType = Callable[[_EnvironType, _StartResponseType], _ResponseBodyType]

type _UnixSocketPathType = str
type _FileDescriptorType = int
type _TcpAddressType = tuple[LiteralString, int]
type _AddressType = _UnixSocketPathType | _FileDescriptorType | _TcpAddressType
