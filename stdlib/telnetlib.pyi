import socket
from collections.abc import Callable, Sequence
from re import Match, Pattern
from types import TracebackType
from typing import Any, Final
from typing_extensions import Self

__all__ = ["Telnet"]

DEBUGLEVEL: Final[int]
TELNET_PORT: Final[int]

IAC: Final[bytes]
DONT: Final[bytes]
DO: Final[bytes]
WONT: Final[bytes]
WILL: Final[bytes]
theNULL: bytes

SE: Final[bytes]
NOP: Final[bytes]
DM: Final[bytes]
BRK: Final[bytes]
IP: Final[bytes]
AO: Final[bytes]
AYT: Final[bytes]
EC: Final[bytes]
EL: Final[bytes]
GA: Final[bytes]
SB: Final[bytes]

BINARY: Final[bytes]
ECHO: Final[bytes]
RCP: Final[bytes]
SGA: Final[bytes]
NAMS: Final[bytes]
STATUS: Final[bytes]
TM: Final[bytes]
RCTE: Final[bytes]
NAOL: Final[bytes]
NAOP: Final[bytes]
NAOCRD: Final[bytes]
NAOHTS: Final[bytes]
NAOHTD: Final[bytes]
NAOFFD: Final[bytes]
NAOVTS: Final[bytes]
NAOVTD: Final[bytes]
NAOLFD: Final[bytes]
XASCII: Final[bytes]
LOGOUT: Final[bytes]
BM: Final[bytes]
DET: Final[bytes]
SUPDUP: Final[bytes]
SUPDUPOUTPUT: Final[bytes]
SNDLOC: Final[bytes]
TTYPE: Final[bytes]
EOR: Final[bytes]
TUID: Final[bytes]
OUTMRK: Final[bytes]
TTYLOC: Final[bytes]
VT3270REGIME: Final[bytes]
X3PAD: Final[bytes]
NAWS: Final[bytes]
TSPEED: Final[bytes]
LFLOW: Final[bytes]
LINEMODE: Final[bytes]
XDISPLOC: Final[bytes]
OLD_ENVIRON: Final[bytes]
AUTHENTICATION: Final[bytes]
ENCRYPT: Final[bytes]
NEW_ENVIRON: Final[bytes]

TN3270E: Final[bytes]
XAUTH: Final[bytes]
CHARSET: Final[bytes]
RSP: Final[bytes]
COM_PORT_OPTION: Final[bytes]
SUPPRESS_LOCAL_ECHO: Final[bytes]
TLS: Final[bytes]
KERMIT: Final[bytes]
SEND_URL: Final[bytes]
FORWARD_X: Final[bytes]
PRAGMA_LOGON: Final[bytes]
SSPI_LOGON: Final[bytes]
PRAGMA_HEARTBEAT: Final[bytes]
EXOPL: Final[bytes]
NOOPT: Final[bytes]

class Telnet:
    host: str | None  # undocumented
    sock: socket.socket | None  # undocumented
    def __init__(self, host: str | None = None, port: int = 0, timeout: float = ...) -> None: ...
    def open(self, host: str, port: int = 0, timeout: float = ...) -> None: ...
    def msg(self, msg: str, *args: Any) -> None: ...
    def set_debuglevel(self, debuglevel: int) -> None: ...
    def close(self) -> None: ...
    def get_socket(self) -> socket.socket: ...
    def fileno(self) -> int: ...
    def write(self, buffer: bytes) -> None: ...
    def read_until(self, match: bytes, timeout: float | None = None) -> bytes: ...
    def read_all(self) -> bytes: ...
    def read_some(self) -> bytes: ...
    def read_very_eager(self) -> bytes: ...
    def read_eager(self) -> bytes: ...
    def read_lazy(self) -> bytes: ...
    def read_very_lazy(self) -> bytes: ...
    def read_sb_data(self) -> bytes: ...
    def set_option_negotiation_callback(self, callback: Callable[[socket.socket, bytes, bytes], object] | None) -> None: ...
    def process_rawq(self) -> None: ...
    def rawq_getchar(self) -> bytes: ...
    def fill_rawq(self) -> None: ...
    def sock_avail(self) -> bool: ...
    def interact(self) -> None: ...
    def mt_interact(self) -> None: ...
    def listener(self) -> None: ...
    def expect(
        self, list: Sequence[Pattern[bytes] | bytes], timeout: float | None = None
    ) -> tuple[int, Match[bytes] | None, bytes]: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, type: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    def __del__(self) -> None: ...
