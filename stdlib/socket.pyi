import sys
from collections.abc import Iterable
from enum import IntEnum, IntFlag
from io import RawIOBase
from typing import Any, BinaryIO, Optional, TextIO, TypeVar, Union, overload
from typing_extensions import Literal

import _socket
from _socket import *
from _socket import _Address, _RetAddress

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

AF_UNIX: AddressFamily
AF_INET: AddressFamily
AF_INET6: AddressFamily
AF_AAL5: AddressFamily
AF_APPLETALK: AddressFamily
AF_ASH: AddressFamily
AF_ATMPVC: AddressFamily
AF_ATMSVC: AddressFamily
AF_AX25: AddressFamily
AF_BRIDGE: AddressFamily
AF_DECnet: AddressFamily
AF_ECONET: AddressFamily
AF_IPX: AddressFamily
AF_IRDA: AddressFamily
AF_KEY: AddressFamily
AF_LLC: AddressFamily
AF_NETBEUI: AddressFamily
AF_NETROM: AddressFamily
AF_PPPOX: AddressFamily
AF_ROSE: AddressFamily
AF_ROUTE: AddressFamily
AF_SECURITY: AddressFamily
AF_SNA: AddressFamily
AF_SYSTEM: AddressFamily
AF_UNSPEC: AddressFamily
AF_WANPIPE: AddressFamily
AF_X25: AddressFamily
if sys.platform == "linux":
    AF_CAN: AddressFamily
    AF_PACKET: AddressFamily
    AF_RDS: AddressFamily
    AF_TIPC: AddressFamily
    AF_ALG: AddressFamily
    AF_NETLINK: AddressFamily
    if sys.version_info >= (3, 7):
        AF_VSOCK: AddressFamily
    if sys.version_info >= (3, 8):
        AF_QIPCRTR: AddressFamily
AF_LINK: AddressFamily  # Availability: BSD, macOS
if sys.platform != "win32" and sys.platform != "darwin":
    AF_BLUETOOTH: AddressFamily

class SocketKind(IntEnum):
    SOCK_STREAM: int
    SOCK_DGRAM: int
    SOCK_RAW: int
    SOCK_RDM: int
    SOCK_SEQPACKET: int
    SOCK_CLOEXEC: int
    SOCK_NONBLOCK: int

SOCK_STREAM: SocketKind
SOCK_DGRAM: SocketKind
SOCK_RAW: SocketKind
SOCK_RDM: SocketKind
SOCK_SEQPACKET: SocketKind
if sys.platform == "linux":
    SOCK_CLOEXEC: SocketKind
    SOCK_NONBLOCK: SocketKind

class MsgFlag(IntFlag):
    MSG_CTRUNC: int
    MSG_DONTROUTE: int
    MSG_DONTWAIT: int
    MSG_EOR: int
    MSG_OOB: int
    MSG_PEEK: int
    MSG_TRUNC: int
    MSG_WAITALL: int

MSG_BCAST: MsgFlag
MSG_BTAG: MsgFlag
MSG_CMSG_CLOEXEC: MsgFlag
MSG_CONFIRM: MsgFlag
MSG_CTRUNC: MsgFlag
MSG_DONTROUTE: MsgFlag
MSG_DONTWAIT: MsgFlag
MSG_EOF: MsgFlag
MSG_EOR: MsgFlag
MSG_ERRQUEUE: MsgFlag
MSG_ETAG: MsgFlag
MSG_FASTOPEN: MsgFlag
MSG_MCAST: MsgFlag
MSG_MORE: MsgFlag
MSG_NOSIGNAL: MsgFlag
MSG_NOTIFICATION: MsgFlag
MSG_OOB: MsgFlag
MSG_PEEK: MsgFlag
MSG_TRUNC: MsgFlag
MSG_WAITALL: MsgFlag

class AddressInfo(IntFlag):
    AI_ADDRCONFIG: int
    AI_ALL: int
    AI_CANONNAME: int
    AI_NUMERICHOST: int
    AI_NUMERICSERV: int
    AI_PASSIVE: int
    AI_V4MAPPED: int

AI_ADDRCONFIG: AddressInfo
AI_ALL: AddressInfo
AI_CANONNAME: AddressInfo
AI_DEFAULT: AddressInfo
AI_MASK: AddressInfo
AI_NUMERICHOST: AddressInfo
AI_NUMERICSERV: AddressInfo
AI_PASSIVE: AddressInfo
AI_V4MAPPED: AddressInfo
AI_V4MAPPED_CFG: AddressInfo

if sys.platform == "win32":
    errorTab: dict[int, str]  # undocumented

class socket(_socket.socket):
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
    def family(self) -> AddressFamily: ...
    @property
    def type(self) -> SocketKind: ...
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
    def socketpair(
        family: Union[int, AddressFamily, None] = ..., type: Union[SocketType, int] = ..., proto: int = ...
    ) -> tuple[socket, socket]: ...

class SocketIO(RawIOBase):
    def __init__(self, sock: socket, mode: Literal["r", "w", "rw", "rb", "wb", "rwb"]) -> None: ...
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
def getaddrinfo(
    host: Optional[Union[bytearray, bytes, str]],
    port: Union[str, int, None],
    family: int = ...,
    type: int = ...,
    proto: int = ...,
    flags: int = ...,
) -> list[tuple[AddressFamily, SocketKind, int, str, Union[tuple[str, int], tuple[str, int, int, int]]]]: ...
