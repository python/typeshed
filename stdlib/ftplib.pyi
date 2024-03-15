import sys
from _typeshed import SupportsRead, SupportsReadline
from collections.abc import Callable, Iterable, Iterator
from socket import socket
from ssl import SSLContext
from types import TracebackType
from typing import Any, Literal, TextIO
from typing_extensions import Self

__all__ = ["FTP", "error_reply", "error_temp", "error_perm", "error_proto", "all_errors", "FTP_TLS"]

MSG_OOB: Literal[1]
FTP_PORT: Literal[21]
MAXLINE: Literal[8192]
CRLF: Literal["\r\n"]
B_CRLF: Literal[b"\r\n"]

class Error(Exception): ...
class error_reply(Error): ...
class error_temp(Error): ...
class error_perm(Error): ...
class error_proto(Error): ...

all_errors: tuple[type[Exception], ...]

class FTP:
    debugging: int
    host: str
    port: int
    maxline: int
    sock: socket | None
    welcome: str | None
    passiveserver: int
    timeout: float | None
    af: int
    lastresp: str
    file: TextIO | None
    encoding: str
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    source_address: tuple[str, int] | None
    if sys.version_info >= (3, 9):
        def __init__(
            self,
            host: str = "",
            user: str = "",
            passwd: str = "",
            acct: str = "",
            timeout: float | None = ...,
            source_address: tuple[str, int] | None = None,
            *,
            encoding: str = "utf-8",
        ) -> None: ...
    else:
        def __init__(
            self,
            host: str = "",
            user: str = "",
            passwd: str = "",
            acct: str = "",
            timeout: float | None = ...,
            source_address: tuple[str, int] | None = None,
        ) -> None: ...

    def connect(
        self, host: str = "", port: int = 0, timeout: float = -999, source_address: tuple[str, int] | None = None
    ) -> str: ...
    def getwelcome(self) -> str: ...
    def set_debuglevel(self, level: int) -> None: ...
    def debug(self, level: int) -> None: ...
    def set_pasv(self, val: bool | Literal[0, 1]) -> None: ...
    def sanitize(self, s: str) -> str: ...
    def putline(self, line: str) -> None: ...
    def putcmd(self, line: str) -> None: ...
    def getline(self) -> str: ...
    def getmultiline(self) -> str: ...
    def getresp(self) -> str: ...
    def voidresp(self) -> str: ...
    def abort(self) -> str: ...
    def sendcmd(self, cmd: str) -> str: ...
    def voidcmd(self, cmd: str) -> str: ...
    def sendport(self, host: str, port: int) -> str: ...
    def sendeprt(self, host: str, port: int) -> str: ...
    def makeport(self) -> socket: ...
    def makepasv(self) -> tuple[str, int]: ...
    def login(self, user: str = "", passwd: str = "", acct: str = "") -> str: ...
    # In practice, `rest` rest can actually be anything whose str() is an integer sequence, so to make it simple we allow integers.
    def ntransfercmd(self, cmd: str, rest: int | str | None = None) -> tuple[socket, int | None]: ...
    def transfercmd(self, cmd: str, rest: int | str | None = None) -> socket: ...
    def retrbinary(
        self, cmd: str, callback: Callable[[bytes], object], blocksize: int = 8192, rest: int | str | None = None
    ) -> str: ...
    def storbinary(
        self,
        cmd: str,
        fp: SupportsRead[bytes],
        blocksize: int = 8192,
        callback: Callable[[bytes], object] | None = None,
        rest: int | str | None = None,
    ) -> str: ...
    def retrlines(self, cmd: str, callback: Callable[[str], object] | None = None) -> str: ...
    def storlines(self, cmd: str, fp: SupportsReadline[bytes], callback: Callable[[bytes], object] | None = None) -> str: ...
    def acct(self, password: str) -> str: ...
    def nlst(self, *args: str) -> list[str]: ...
    # Technically only the last arg can be a Callable but ...
    def dir(self, *args: str | Callable[[str], object]) -> None: ...
    def mlsd(self, path: str = "", facts: Iterable[str] = []) -> Iterator[tuple[str, dict[str, str]]]: ...
    def rename(self, fromname: str, toname: str) -> str: ...
    def delete(self, filename: str) -> str: ...
    def cwd(self, dirname: str) -> str: ...
    def size(self, filename: str) -> int | None: ...
    def mkd(self, dirname: str) -> str: ...
    def rmd(self, dirname: str) -> str: ...
    def pwd(self) -> str: ...
    def quit(self) -> str: ...
    def close(self) -> None: ...

class FTP_TLS(FTP):
    if sys.version_info >= (3, 12):
        def __init__(
            self,
            host: str = "",
            user: str = "",
            passwd: str = "",
            acct: str = "",
            *,
            context: SSLContext | None = None,
            timeout: float | None = ...,
            source_address: tuple[str, int] | None = None,
            encoding: str = "utf-8",
        ) -> None: ...
    elif sys.version_info >= (3, 9):
        def __init__(
            self,
            host: str = "",
            user: str = "",
            passwd: str = "",
            acct: str = "",
            keyfile: str | None = None,
            certfile: str | None = None,
            context: SSLContext | None = None,
            timeout: float | None = ...,
            source_address: tuple[str, int] | None = None,
            *,
            encoding: str = "utf-8",
        ) -> None: ...
    else:
        def __init__(
            self,
            host: str = "",
            user: str = "",
            passwd: str = "",
            acct: str = "",
            keyfile: str | None = None,
            certfile: str | None = None,
            context: SSLContext | None = None,
            timeout: float | None = ...,
            source_address: tuple[str, int] | None = None,
        ) -> None: ...
    ssl_version: int
    keyfile: str | None
    certfile: str | None
    context: SSLContext
    def login(self, user: str = "", passwd: str = "", acct: str = "", secure: bool = True) -> str: ...
    def auth(self) -> str: ...
    def prot_p(self) -> str: ...
    def prot_c(self) -> str: ...
    def ccc(self) -> str: ...

def parse150(resp: str) -> int | None: ...  # undocumented
def parse227(resp: str) -> tuple[str, int]: ...  # undocumented
def parse229(resp: str, peer: Any) -> tuple[str, int]: ...  # undocumented
def parse257(resp: str) -> str: ...  # undocumented
def ftpcp(
    source: FTP, sourcename: str, target: FTP, targetname: str = "", type: Literal["A", "I"] = "I"
) -> None: ...  # undocumented
