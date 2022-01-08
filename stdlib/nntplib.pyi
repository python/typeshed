import datetime
import socket
import ssl
import sys
from _typeshed import Self
from typing import IO, Any, Iterable, NamedTuple, Union

_File = Union[IO[bytes], bytes, str, None]

class NNTPError(Exception):
    response: str

class NNTPReplyError(NNTPError): ...
class NNTPTemporaryError(NNTPError): ...
class NNTPPermanentError(NNTPError): ...
class NNTPProtocolError(NNTPError): ...
class NNTPDataError(NNTPError): ...

NNTP_PORT: int
NNTP_SSL_PORT: int

class GroupInfo(NamedTuple):
    group: str
    last: str
    first: str
    flag: str

class ArticleInfo(NamedTuple):
    number: int
    message_id: str
    lines: list[bytes]

def decode_header(header_str: str) -> str: ...

_list = list  # conflicts with a method named "list"

class _NNTPBase:
    encoding: str
    errors: str

    host: str
    file: IO[bytes]
    debugging: int
    welcome: str
    readermode_afterauth: bool
    tls_on: bool
    authenticated: bool
    nntp_implementation: str
    nntp_version: int
    def __init__(self, file: IO[bytes], host: str, readermode: bool | None = ..., timeout: float = ...) -> None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args: Any) -> None: ...
    def getwelcome(self) -> str: ...
    def getcapabilities(self) -> dict[str, _list[str]]: ...
    def set_debuglevel(self, level: int) -> None: ...
    def debug(self, level: int) -> None: ...
    def capabilities(self) -> tuple[str, dict[str, _list[str]]]: ...
    def newgroups(self, date: datetime.date | datetime.datetime, *, file: _File = ...) -> tuple[str, _list[str]]: ...
    def newnews(self, group: str, date: datetime.date | datetime.datetime, *, file: _File = ...) -> tuple[str, _list[str]]: ...
    def list(self, group_pattern: str | None = ..., *, file: _File = ...) -> tuple[str, _list[str]]: ...
    def description(self, group: str) -> str: ...
    def descriptions(self, group_pattern: str) -> tuple[str, dict[str, str]]: ...
    def group(self, name: str) -> tuple[str, int, int, int, str]: ...
    def help(self, *, file: _File = ...) -> tuple[str, _list[str]]: ...
    def stat(self, message_spec: Any = ...) -> tuple[str, int, str]: ...
    def next(self) -> tuple[str, int, str]: ...
    def last(self) -> tuple[str, int, str]: ...
    def head(self, message_spec: Any = ..., *, file: _File = ...) -> tuple[str, ArticleInfo]: ...
    def body(self, message_spec: Any = ..., *, file: _File = ...) -> tuple[str, ArticleInfo]: ...
    def article(self, message_spec: Any = ..., *, file: _File = ...) -> tuple[str, ArticleInfo]: ...
    def slave(self) -> str: ...
    def xhdr(self, hdr: str, str: Any, *, file: _File = ...) -> tuple[str, _list[str]]: ...
    def xover(self, start: int, end: int, *, file: _File = ...) -> tuple[str, _list[tuple[int, dict[str, str]]]]: ...
    def over(
        self, message_spec: None | str | _list[Any] | tuple[Any, ...], *, file: _File = ...
    ) -> tuple[str, _list[tuple[int, dict[str, str]]]]: ...
    if sys.version_info < (3, 9):
        def xgtitle(self, group: str, *, file: _File = ...) -> tuple[str, _list[tuple[str, str]]]: ...
        def xpath(self, id: Any) -> tuple[str, str]: ...
    def date(self) -> tuple[str, datetime.datetime]: ...
    def post(self, data: bytes | Iterable[bytes]) -> str: ...
    def ihave(self, message_id: Any, data: bytes | Iterable[bytes]) -> str: ...
    def quit(self) -> str: ...
    def login(self, user: str | None = ..., password: str | None = ..., usenetrc: bool = ...) -> None: ...
    def starttls(self, context: ssl.SSLContext | None = ...) -> None: ...

class NNTP(_NNTPBase):
    port: int
    sock: socket.socket
    def __init__(
        self,
        host: str,
        port: int = ...,
        user: str | None = ...,
        password: str | None = ...,
        readermode: bool | None = ...,
        usenetrc: bool = ...,
        timeout: float = ...,
    ) -> None: ...

class NNTP_SSL(_NNTPBase):
    sock: socket.socket
    def __init__(
        self,
        host: str,
        port: int = ...,
        user: str | None = ...,
        password: str | None = ...,
        ssl_context: ssl.SSLContext | None = ...,
        readermode: bool | None = ...,
        usenetrc: bool = ...,
        timeout: float = ...,
    ) -> None: ...
