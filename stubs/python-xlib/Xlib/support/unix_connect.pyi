import sys
from platform import uname_result
from re import Pattern
from socket import socket
from typing_extensions import Literal, TypeAlias

from Xlib._typing import Address, Unused

F_SETFD: int
FD_CLOEXEC: int

if sys.platform == "darwin":
    SUPPORTED_PROTOCOLS: tuple[  # pyright: ignore[reportGeneralTypeIssues]
        None, Literal["tcp"], Literal["unix"], Literal["darwin"]
    ]
    _Protocol: TypeAlias = Literal[None, "tcp", "unix", "darwin"]  # pyright: ignore[reportGeneralTypeIssues]
    DARWIN_DISPLAY_RE: Pattern[str]
else:
    SUPPORTED_PROTOCOLS: tuple[None, Literal["tcp"], Literal["unix"]]
    _Protocol: TypeAlias = Literal[None, "tcp", "unix"]  # pyright: ignore
uname: uname_result
DISPLAY_RE: Pattern[str]

def get_display(display: str | None) -> tuple[str, str | None, str | None, int, int]: ...
def get_socket(dname: Address, protocol: _Protocol, host: Address | None, dno: int) -> socket: ...
def new_get_auth(sock: socket, dname: Unused, protocol: _Protocol, host: Unused, dno: int) -> tuple[bytes, bytes]: ...
def old_get_auth(sock: Unused, dname: Address, host: Unused, dno: Unused) -> tuple[str, bytes]: ...

get_auth = new_get_auth
