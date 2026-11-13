import io
import sys
import threading
from _typeshed import ConvertibleToFloat, FileDescriptorOrPath, Incomplete, StrOrBytesPath, SupportsWrite
from collections import defaultdict
from collections.abc import Callable
from socket import AF_INET6 as AF_INET6, AddressFamily, SocketKind
from typing import BinaryIO, Final, ParamSpec, SupportsIndex, TypeVar, overload

from . import _ntuples as ntp

POSIX: Final[bool]
WINDOWS: Final[bool]
LINUX: Final[bool]
MACOS: Final[bool]
FREEBSD: Final[bool]
OPENBSD: Final[bool]
NETBSD: Final[bool]
BSD: Final[bool]
SUNOS: Final[bool]
AIX: Final[bool]

ENCODING: Final[str]
ENCODING_ERRS: Final[str]

conn_tmap: dict[str, tuple[list[AddressFamily], list[SocketKind]]]

class Error(Exception): ...

class NoSuchProcess(Error):
    pid: int
    name: str | None
    msg: str
    def __init__(self, pid: int, name: str | None = None, msg: str | None = None) -> None: ...

class ZombieProcess(NoSuchProcess):
    ppid: int | None
    def __init__(self, pid: int, name: str | None = None, ppid: int | None = None, msg: str | None = None) -> None: ...

class AccessDenied(Error):
    pid: int | None
    name: str | None
    msg: str
    def __init__(self, pid: int | None = None, name: str | None = None, msg: str | None = None) -> None: ...

class TimeoutExpired(Error):
    seconds: float
    pid: int | None
    name: str | None
    msg: str
    def __init__(self, seconds: float, pid: int | None = None, name: str | None = None) -> None: ...

_P = ParamSpec("_P")
_R = TypeVar("_R")
_T = TypeVar("_T")

def usage_percent(used: ConvertibleToFloat, total: float, round_: SupportsIndex | None = None) -> float: ...

# returned function has `cache_activate(proc)` and `cache_deactivate(proc)` attributes:
def memoize_when_activated(fun: Callable[_P, _R]) -> Callable[_P, _R]: ...
def isfile_strict(path: StrOrBytesPath) -> bool: ...
def path_exists_strict(path: StrOrBytesPath) -> bool: ...
def supports_ipv6() -> bool: ...
def parse_environ_block(data: str) -> dict[str, str]: ...
def sockfam_to_enum(num: int) -> AddressFamily: ...
def socktype_to_enum(num: int) -> SocketKind: ...

@overload
def conn_to_ntuple(
    fd: int,
    fam: int,
    type_: int,
    laddr: ntp.addr | tuple[str, int] | tuple[()],
    raddr: ntp.addr | tuple[str, int] | tuple[()],
    status: int | str,
    status_map: dict[int, str] | dict[str, str],
    pid: int,
) -> ntp.sconn: ...
@overload
def conn_to_ntuple(
    fd: int,
    fam: int,
    type_: int,
    laddr: ntp.addr | tuple[str, int] | tuple[()],
    raddr: ntp.addr | tuple[str, int] | tuple[()],
    status: int | str,
    status_map: dict[int, str] | dict[str, str],
    pid: None = None,
) -> ntp.pconn: ...

class _WrapNumbers:
    lock: threading.Lock
    cache: dict[str, dict[str, tuple[int, ...]]]
    reminders: dict[str, defaultdict[Incomplete, int]]
    reminder_keys: dict[str, defaultdict[Incomplete, set[Incomplete]]]
    def __init__(self) -> None: ...
    def run(self, input_dict: dict[str, tuple[int, ...]], name: str) -> dict[str, tuple[int, ...]]: ...
    def cache_clear(self, name: str | None = None) -> None: ...
    def cache_info(
        self,
    ) -> tuple[
        dict[str, dict[str, tuple[int, ...]]],
        dict[str, defaultdict[Incomplete, int]],
        dict[str, defaultdict[Incomplete, set[Incomplete]]],
    ]: ...

def wrap_numbers(input_dict: dict[str, tuple[int, ...]], name: str) -> dict[str, tuple[int, ...]]: ...
def open_binary(fname: FileDescriptorOrPath) -> BinaryIO: ...
def open_text(fname: FileDescriptorOrPath) -> io.TextIOWrapper: ...

@overload
def cat(fname: FileDescriptorOrPath, _open: Callable[[FileDescriptorOrPath], io.TextIOWrapper] = ...) -> str: ...
@overload
def cat(
    fname: FileDescriptorOrPath, fallback: _T = ..., _open: Callable[[FileDescriptorOrPath], io.TextIOWrapper] = ...
) -> str | _T: ...

@overload
def bcat(fname: FileDescriptorOrPath) -> str: ...
@overload
def bcat(fname: FileDescriptorOrPath, fallback: _T = ...) -> str | _T: ...

def bytes2human(n: int) -> str: ...
def decode(s: bytes) -> str: ...
def term_supports_colors(force_color: bool = False) -> bool: ...
def hilite(s: str, color: str | None = None, bold: bool = False, force_color: bool = False) -> str: ...
def print_color(s: str, color: str | None = None, bold: bool = False, file: SupportsWrite[str] = sys.stdout) -> None: ...
def debug(msg: str | Exception) -> None: ...
def warn(msg: str) -> None: ...

__all__ = [
    # OS constants
    "FREEBSD",
    "BSD",
    "LINUX",
    "NETBSD",
    "OPENBSD",
    "MACOS",
    "POSIX",
    "SUNOS",
    "WINDOWS",
    # other constants
    "ENCODING",
    "ENCODING_ERRS",
    "AF_INET6",
    # utility functions
    "conn_tmap",
    "isfile_strict",
    "parse_environ_block",
    "path_exists_strict",
    "usage_percent",
    "supports_ipv6",
    "sockfam_to_enum",
    "socktype_to_enum",
    "wrap_numbers",
    "open_text",
    "open_binary",
    "cat",
    "bcat",
    "bytes2human",
    "conn_to_ntuple",
    "debug",
    "warn",
    # shell utils
    "hilite",
    "term_supports_colors",
    "print_color",
]
