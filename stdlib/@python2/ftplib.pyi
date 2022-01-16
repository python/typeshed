from _typeshed import SupportsRead, SupportsReadline
from socket import socket
from ssl import SSLContext
from typing import Any, BinaryIO, Callable, List, Text, Tuple, Type, Union
from typing_extensions import Literal

_IntOrStr = Union[int, Text]

MSG_OOB: int
FTP_PORT: int
MAXLINE: int
CRLF: str

class Error(Exception): ...
class error_reply(Error): ...
class error_temp(Error): ...
class error_perm(Error): ...
class error_proto(Error): ...

all_errors: Tuple[Type[Exception], ...]

class FTP:
    debugging: int

    # Note: This is technically the type that's passed in as the host argument.  But to make it easier in Python 2 we
    # accept Text but return str.
    host: str

    port: int
    maxline: int
    sock: socket | None
    welcome: str | None
    passiveserver: int
    timeout: int
    af: int
    lastresp: str

    file: BinaryIO | None
    def __init__(
        self, host: Text = ..., user: Text = ..., passwd: Text = ..., acct: Text = ..., timeout: float = ...
    ) -> None: ...
    def connect(self, host: Text = ..., port: int = ..., timeout: float = ...) -> str: ...
    def getwelcome(self) -> str: ...
    def set_debuglevel(self, level: int) -> None: ...
    def debug(self, level: int) -> None: ...
    def set_pasv(self, val: bool | int) -> None: ...
    def sanitize(self, s: Text) -> str: ...
    def putline(self, line: Text) -> None: ...
    def putcmd(self, line: Text) -> None: ...
    def getline(self) -> str: ...
    def getmultiline(self) -> str: ...
    def getresp(self) -> str: ...
    def voidresp(self) -> str: ...
    def abort(self) -> str: ...
    def sendcmd(self, cmd: Text) -> str: ...
    def voidcmd(self, cmd: Text) -> str: ...
    def sendport(self, host: Text, port: int) -> str: ...
    def sendeprt(self, host: Text, port: int) -> str: ...
    def makeport(self) -> socket: ...
    def makepasv(self) -> Tuple[str, int]: ...
    def login(self, user: Text = ..., passwd: Text = ..., acct: Text = ...) -> str: ...
    # In practice, `rest` rest can actually be anything whose str() is an integer sequence, so to make it simple we allow integers.
    def ntransfercmd(self, cmd: Text, rest: _IntOrStr | None = ...) -> Tuple[socket, int]: ...
    def transfercmd(self, cmd: Text, rest: _IntOrStr | None = ...) -> socket: ...
    def retrbinary(
        self, cmd: Text, callback: Callable[[bytes], Any], blocksize: int = ..., rest: _IntOrStr | None = ...
    ) -> str: ...
    def storbinary(
        self,
        cmd: Text,
        fp: SupportsRead[bytes],
        blocksize: int = ...,
        callback: Callable[[bytes], Any] | None = ...,
        rest: _IntOrStr | None = ...,
    ) -> str: ...
    def retrlines(self, cmd: Text, callback: Callable[[str], Any] | None = ...) -> str: ...
    def storlines(self, cmd: Text, fp: SupportsReadline[bytes], callback: Callable[[bytes], Any] | None = ...) -> str: ...
    def acct(self, password: Text) -> str: ...
    def nlst(self, *args: Text) -> List[str]: ...
    # Technically only the last arg can be a Callable but ...
    def dir(self, *args: str | Callable[[str], None]) -> None: ...
    def rename(self, fromname: Text, toname: Text) -> str: ...
    def delete(self, filename: Text) -> str: ...
    def cwd(self, dirname: Text) -> str: ...
    def size(self, filename: Text) -> int | None: ...
    def mkd(self, dirname: Text) -> str: ...
    def rmd(self, dirname: Text) -> str: ...
    def pwd(self) -> str: ...
    def quit(self) -> str: ...
    def close(self) -> None: ...

class FTP_TLS(FTP):
    def __init__(
        self,
        host: Text = ...,
        user: Text = ...,
        passwd: Text = ...,
        acct: Text = ...,
        keyfile: str | None = ...,
        certfile: str | None = ...,
        context: SSLContext | None = ...,
        timeout: float = ...,
        source_address: Tuple[str, int] | None = ...,
    ) -> None: ...
    ssl_version: int
    keyfile: str | None
    certfile: str | None
    context: SSLContext
    def login(self, user: Text = ..., passwd: Text = ..., acct: Text = ..., secure: bool = ...) -> str: ...
    def auth(self) -> str: ...
    def prot_p(self) -> str: ...
    def prot_c(self) -> str: ...

class Netrc:
    def __init__(self, filename: Text | None = ...) -> None: ...
    def get_hosts(self) -> List[str]: ...
    def get_account(self, host: Text) -> Tuple[str | None, str | None, str | None]: ...
    def get_macros(self) -> List[str]: ...
    def get_macro(self, macro: Text) -> Tuple[str, ...]: ...

def parse150(resp: str) -> int | None: ...  # undocumented
def parse227(resp: str) -> Tuple[str, int]: ...  # undocumented
def parse229(resp: str, peer: Any) -> Tuple[str, int]: ...  # undocumented
def parse257(resp: str) -> str: ...  # undocumented
def ftpcp(
    source: FTP, sourcename: str, target: FTP, targetname: str = ..., type: Literal["A", "I"] = ...
) -> None: ...  # undocumented
