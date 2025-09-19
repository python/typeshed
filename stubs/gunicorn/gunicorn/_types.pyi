### This .pyi file is a helper for centralized storage types that are reused across different runtime modules. ###

from collections.abc import Awaitable, Callable, Iterable
from typing import Any
from typing_extensions import LiteralString, TypeAlias

_StatusType: TypeAlias = str
_HeadersType: TypeAlias = list[tuple[str, str]]

_EnvironType: TypeAlias = dict[str, Any]  # See https://peps.python.org/pep-0333/
_StartResponseType: TypeAlias = Callable[[_StatusType, _HeadersType], None]
_ResponseBodyType: TypeAlias = Iterable[bytes]
_WSGIAppType: TypeAlias = Callable[[_EnvironType, _StartResponseType], _ResponseBodyType]  # noqa: Y047

_ScopeType: TypeAlias = dict[str, Any]
_ReceiveType: TypeAlias = Callable[[], Awaitable[dict[str, Any]]]
_SendType: TypeAlias = Callable[[dict[str, Any]], Awaitable[None]]
_ASGIAppType: TypeAlias = Callable[[_ScopeType, _ReceiveType, _SendType], Awaitable[None]]  # noqa: Y047

_UnixSocketPathType: TypeAlias = str
_FileDescriptorType: TypeAlias = int
_TcpAddressType: TypeAlias = tuple[LiteralString, int]  # noqa: Y047
_AddressType: TypeAlias = _UnixSocketPathType | _FileDescriptorType | _TcpAddressType  # noqa: Y047
