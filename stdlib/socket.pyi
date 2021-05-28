import sys
from _typeshed import ReadableBuffer, WriteableBuffer
from collections.abc import Iterable
from enum import IntEnum, IntFlag
from io import RawIOBase
from typing import Any, BinaryIO, Optional, TextIO, TypeVar, Union, overload
from typing_extensions import Literal

import _socket
from _socket import *
from _socket import _Address as _Address, _RetAddress as _RetAddress

_T = TypeVar("_T")

# Re-exported from errno
EBADF: int
EAGAIN: int
EWOULDBLOCK: int

class AddressFamily(IntEnum):
    AF_UNIX: int
    AF_INET: int
    AF_INET6: int
    AF_AAL5: int
    AF_ALG: int
    AF_APPLETALK: int
    AF_ASH: int
    AF_ATMPVC: int
    AF_ATMSVC: int
    AF_AX25: int
    AF_BLUETOOTH: int
    AF_BRIDGE: int
    AF_CAN: int
    AF_DECnet: int
    AF_ECONET: int
    AF_IPX: int
    AF_IRDA: int
    AF_KEY: int
    AF_LINK: int
    AF_LLC: int
    AF_NETBEUI: int
    AF_NETLINK: int
    AF_NETROM: int
    AF_PACKET: int
    AF_PPPOX: int
    AF_QIPCRTR: int
    AF_RDS: int
    AF_ROSE: int
    AF_ROUTE: int
    AF_SECURITY: int
    AF_SNA: int
    AF_SYSTEM: int
    AF_TIPC: int
    AF_UNSPEC: int
    AF_VSOCK: int
    AF_WANPIPE: int
    AF_X25: int

AF_UNIX: AddressFamily  # type: ignore  # redefined from _socket
AF_INET: AddressFamily  # type: ignore  # redefined from _socket
AF_INET6: AddressFamily  # type: ignore  # redefined from _socket
AF_AAL5: AddressFamily  # type: ignore  # redefined from _socket
AF_APPLETALK: AddressFamily  # type: ignore  # redefined from _socket
AF_ASH: AddressFamily  # type: ignore  # redefined from _socket
AF_ATMPVC: AddressFamily  # type: ignore  # redefined from _socket
AF_ATMSVC: AddressFamily  # type: ignore  # redefined from _socket
AF_AX25: AddressFamily  # type: ignore  # redefined from _socket
AF_BRIDGE: AddressFamily  # type: ignore  # redefined from _socket
AF_DECnet: AddressFamily  # type: ignore  # redefined from _socket
AF_ECONET: AddressFamily  # type: ignore  # redefined from _socket
AF_IPX: AddressFamily  # type: ignore  # redefined from _socket
AF_IRDA: AddressFamily  # type: ignore  # redefined from _socket
AF_KEY: AddressFamily  # type: ignore  # redefined from _socket
AF_LLC: AddressFamily  # type: ignore  # redefined from _socket
AF_NETBEUI: AddressFamily  # type: ignore  # redefined from _socket
AF_NETROM: AddressFamily  # type: ignore  # redefined from _socket
AF_PPPOX: AddressFamily  # type: ignore  # redefined from _socket
AF_ROSE: AddressFamily  # type: ignore  # redefined from _socket
AF_ROUTE: AddressFamily  # type: ignore  # redefined from _socket
AF_SECURITY: AddressFamily  # type: ignore  # redefined from _socket
AF_SNA: AddressFamily  # type: ignore  # redefined from _socket
AF_SYSTEM: AddressFamily  # type: ignore  # redefined from _socket
AF_UNSPEC: AddressFamily  # type: ignore  # redefined from _socket
AF_WANPIPE: AddressFamily  # type: ignore  # redefined from _socket
AF_X25: AddressFamily  # type: ignore  # redefined from _socket
if sys.platform == "linux":
    AF_CAN: AddressFamily  # type: ignore  # redefined from _socket
    AF_PACKET: AddressFamily  # type: ignore  # redefined from _socket
    AF_RDS: AddressFamily  # type: ignore  # redefined from _socket
    AF_TIPC: AddressFamily  # type: ignore  # redefined from _socket
    AF_ALG: AddressFamily  # type: ignore  # redefined from _socket
    AF_NETLINK: AddressFamily  # type: ignore  # redefined from _socket
    if sys.version_info >= (3, 7):
        AF_VSOCK: AddressFamily  # type: ignore  # redefined from _socket
    if sys.version_info >= (3, 8):
        AF_QIPCRTR: AddressFamily  # type: ignore  # redefined from _socket
AF_LINK: AddressFamily  # type: ignore  # redefined from _socket, availability: BSD, macOS
if sys.platform != "win32" and sys.platform != "darwin":
    AF_BLUETOOTH: AddressFamily  # type: ignore  # redefined from _socket

class SocketKind(IntEnum):
    SOCK_STREAM: int
    SOCK_DGRAM: int
    SOCK_RAW: int
    SOCK_RDM: int
    SOCK_SEQPACKET: int
    SOCK_CLOEXEC: int
    SOCK_NONBLOCK: int

SOCK_STREAM: SocketKind  # type: ignore  # redefined from _socket
SOCK_DGRAM: SocketKind  # type: ignore  # redefined from _socket
SOCK_RAW: SocketKind  # type: ignore  # redefined from _socket
SOCK_RDM: SocketKind  # type: ignore  # redefined from _socket
SOCK_SEQPACKET: SocketKind  # type: ignore  # redefined from _socket
if sys.platform == "linux":
    SOCK_CLOEXEC: SocketKind  # type: ignore  # redefined from _socket
    SOCK_NONBLOCK: SocketKind  # type: ignore  # redefined from _socket

class MsgFlag(IntFlag):
    MSG_CTRUNC: int
    MSG_DONTROUTE: int
    MSG_DONTWAIT: int
    MSG_EOR: int
    MSG_OOB: int
    MSG_PEEK: int
    MSG_TRUNC: int
    MSG_WAITALL: int

MSG_BCAST: MsgFlag  # type: ignore  # redefined from _socket
MSG_BTAG: MsgFlag  # type: ignore  # redefined from _socket
MSG_CMSG_CLOEXEC: MsgFlag  # type: ignore  # redefined from _socket
MSG_CONFIRM: MsgFlag  # type: ignore  # redefined from _socket
MSG_CTRUNC: MsgFlag  # type: ignore  # redefined from _socket
MSG_DONTROUTE: MsgFlag  # type: ignore  # redefined from _socket
MSG_DONTWAIT: MsgFlag  # type: ignore  # redefined from _socket
MSG_EOF: MsgFlag  # type: ignore  # redefined from _socket
MSG_EOR: MsgFlag  # type: ignore  # redefined from _socket
MSG_ERRQUEUE: MsgFlag  # type: ignore  # redefined from _socket
MSG_ETAG: MsgFlag  # type: ignore  # redefined from _socket
MSG_FASTOPEN: MsgFlag  # type: ignore  # redefined from _socket
MSG_MCAST: MsgFlag  # type: ignore  # redefined from _socket
MSG_MORE: MsgFlag  # type: ignore  # redefined from _socket
MSG_NOSIGNAL: MsgFlag  # type: ignore  # redefined from _socket
MSG_NOTIFICATION: MsgFlag  # type: ignore  # redefined from _socket
MSG_OOB: MsgFlag  # type: ignore  # redefined from _socket
MSG_PEEK: MsgFlag  # type: ignore  # redefined from _socket
MSG_TRUNC: MsgFlag  # type: ignore  # redefined from _socket
MSG_WAITALL: MsgFlag  # type: ignore  # redefined from _socket

class AddressInfo(IntFlag):
    AI_ADDRCONFIG: int
    AI_ALL: int
    AI_CANONNAME: int
    AI_NUMERICHOST: int
    AI_NUMERICSERV: int
    AI_PASSIVE: int
    AI_V4MAPPED: int

AI_ADDRCONFIG: AddressInfo  # type: ignore  # redefined from _socket
AI_ALL: AddressInfo  # type: ignore  # redefined from _socket
AI_CANONNAME: AddressInfo  # type: ignore  # redefined from _socket
AI_DEFAULT: AddressInfo  # type: ignore  # redefined from _socket
AI_MASK: AddressInfo  # type: ignore  # redefined from _socket
AI_NUMERICHOST: AddressInfo  # type: ignore  # redefined from _socket
AI_NUMERICSERV: AddressInfo  # type: ignore  # redefined from _socket
AI_PASSIVE: AddressInfo  # type: ignore  # redefined from _socket
AI_V4MAPPED: AddressInfo  # type: ignore  # redefined from _socket
AI_V4MAPPED_CFG: AddressInfo  # type: ignore  # redefined from _socket

if sys.platform == "win32":
    errorTab: dict[int, str]  # undocumented

class socket(_socket.socket):  # type: ignore  # redefined from _socket
    def __init__(
        self,
        family: Union[AddressFamily, int] = ...,
        type: Union[SocketKind, int] = ...,
        proto: int = ...,
        fileno: Optional[int] = ...,
    ) -> None: ...
    def __enter__(self: _T) -> _T: ...
    def __exit__(self, *args: object) -> None: ...
    def dup(self: _T) -> _T: ...
    def accept(self) -> tuple[socket, _RetAddress]: ...
    # Note that the makefile's documented windows-specific behavior is not represented
    # mode strings with duplicates are intentionally excluded
    @overload
    def makefile(
        self,
        mode: Literal["r", "w", "rw", "wr", ""] = ...,
        buffering: Optional[int] = ...,
        *,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
    ) -> TextIO: ...
    @overload
    def makefile(
        self,
        mode: Literal["b", "rb", "br", "wb", "bw", "rwb", "rbw", "wrb", "wbr", "brw", "bwr"],
        buffering: Optional[int] = ...,
        *,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
    ) -> BinaryIO: ...
    def sendfile(self, file: BinaryIO, offset: int = ..., count: Optional[int] = ...) -> int: ...
    def close(self) -> None: ...
    def detach(self) -> int: ...
    @property
    def family(self) -> AddressFamily: ...  # type: ignore
    @property
    def type(self) -> SocketKind: ...  # type: ignore
    def get_inheritable(self) -> bool: ...
    def set_inheritable(self, inheritable: bool) -> None: ...

def fromfd(fd: int, family: Union[AddressFamily, int], type: Union[SocketKind, int], proto: int = ...) -> socket: ...

if sys.platform != "win32":
    if sys.version_info >= (3, 9):
        # flags and address appear to be unused in send_fds and recv_fds
        def send_fds(
            sock: socket, buffers: Iterable[bytes], fds: Union[bytes, Iterable[int]], flags: int = ..., address: None = ...
        ) -> int: ...
        def recv_fds(sock: socket, bufsize: int, maxfds: int, flags: int = ...) -> tuple[bytes, list[int], int, Any]: ...

if sys.platform == "win32":
    def fromshare(info: bytes) -> socket: ...

if sys.platform == "win32":
    def socketpair(family: int = ..., type: int = ..., proto: int = ...) -> tuple[socket, socket]: ...

else:
    def socketpair(  # type: ignore
        family: Union[int, AddressFamily, None] = ..., type: Union[SocketType, int] = ..., proto: int = ...
    ) -> tuple[socket, socket]: ...

class SocketIO(RawIOBase):
    def __init__(self, sock: socket, mode: Literal["r", "w", "rw", "rb", "wb", "rwb"]) -> None: ...
    def readinto(self, b: WriteableBuffer) -> Optional[int]: ...
    def write(self, b: ReadableBuffer) -> Optional[int]: ...
    @property
    def name(self) -> int: ...  # return value is really "int"
    @property
    def mode(self) -> Literal["rb", "wb", "rwb"]: ...

def getfqdn(name: str = ...) -> str: ...
def create_connection(
    address: tuple[Optional[str], int],
    timeout: Optional[float] = ...,
    source_address: Optional[tuple[Union[bytearray, bytes, str], int]] = ...,
) -> socket: ...

if sys.version_info >= (3, 8):
    def has_dualstack_ipv6() -> bool: ...
    def create_server(
        address: _Address, *, family: int = ..., backlog: Optional[int] = ..., reuse_port: bool = ..., dualstack_ipv6: bool = ...
    ) -> socket: ...

# the 5th tuple item is an address
def getaddrinfo(  # type: ignore  # redefined from _socket
    host: Optional[Union[bytearray, bytes, str]],
    port: Union[str, int, None],
    family: int = ...,
    type: int = ...,
    proto: int = ...,
    flags: int = ...,
) -> list[tuple[AddressFamily, SocketKind, int, str, Union[tuple[str, int], tuple[str, int, int, int]]]]: ...
