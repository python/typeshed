### This .pyi file is a helper for centralized storage types that are reused across different runtime modules. ###
from _typeshed import FileDescriptor
from collections.abc import Awaitable, Callable, Iterable, MutableMapping
from typing import Any, Literal, TypeAlias, TypedDict, type_check_only
from typing_extensions import LiteralString

_StatusType: TypeAlias = str
_HeadersType: TypeAlias = Iterable[tuple[str, str]]

_EnvironType: TypeAlias = MutableMapping[str, Any]  # See https://peps.python.org/pep-0333/
_StartResponseType: TypeAlias = Callable[[_StatusType, _HeadersType], None]
_ResponseBodyType: TypeAlias = Iterable[bytes]
_WSGIAppType: TypeAlias = Callable[[_EnvironType, _StartResponseType], _ResponseBodyType]  # noqa: Y047

_ScopeType: TypeAlias = MutableMapping[str, Any]
_MessageType: TypeAlias = MutableMapping[str, Any]
_ReceiveType: TypeAlias = Callable[[], Awaitable[_MessageType]]
_SendType: TypeAlias = Callable[[_MessageType], Awaitable[None]]
_ASGIAppType: TypeAlias = Callable[[_ScopeType, _ReceiveType, _SendType], Awaitable[None]]  # noqa: Y047

_UnixSocketPathType: TypeAlias = str
_TcpAddressType: TypeAlias = tuple[LiteralString, int]  # noqa: Y047
_AddressType: TypeAlias = _UnixSocketPathType | FileDescriptor | _TcpAddressType  # noqa: Y047

@type_check_only
class _ProxyProtocolInfo(TypedDict):
    proxy_protocol: Literal["TCP4", "TCP6", "UDP4", "UDP6"]
    client_addr: str
    client_port: int
    proxy_addr: str
    proxy_port: int

@type_check_only
class _ProxyProtocolInfoUnknown(TypedDict):
    proxy_protocol: Literal["UNKNOWN", "LOCAL", "UNSPEC"]
    client_addr: None
    client_port: None
    proxy_addr: None
    proxy_port: None

_ProxyProtocolInfoDict: TypeAlias = _ProxyProtocolInfo | _ProxyProtocolInfoUnknown
