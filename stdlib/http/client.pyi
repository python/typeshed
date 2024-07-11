import email.message
import io
import ssl
import sys
import types
from _typeshed import ReadableBuffer, SupportsRead, SupportsReadline, WriteableBuffer
from collections.abc import Callable, Iterable, Iterator, Mapping
from socket import socket
from typing import Any, BinaryIO, Final, TypeVar, overload
from typing_extensions import Self, TypeAlias

__all__ = [
    "HTTPResponse",
    "HTTPConnection",
    "HTTPException",
    "NotConnected",
    "UnknownProtocol",
    "UnknownTransferEncoding",
    "UnimplementedFileMode",
    "IncompleteRead",
    "InvalidURL",
    "ImproperConnectionState",
    "CannotSendRequest",
    "CannotSendHeader",
    "ResponseNotReady",
    "BadStatusLine",
    "LineTooLong",
    "RemoteDisconnected",
    "error",
    "responses",
    "HTTPSConnection",
]

_DataType: TypeAlias = SupportsRead[bytes] | Iterable[ReadableBuffer] | ReadableBuffer
_T = TypeVar("_T")
_MessageT = TypeVar("_MessageT", bound=email.message.Message)

HTTP_PORT: Final[int]
HTTPS_PORT: Final[int]

CONTINUE: Final[int]
SWITCHING_PROTOCOLS: Final[int]
PROCESSING: Final[int]

OK: Final[int]
CREATED: Final[int]
ACCEPTED: Final[int]
NON_AUTHORITATIVE_INFORMATION: Final[int]
NO_CONTENT: Final[int]
RESET_CONTENT: Final[int]
PARTIAL_CONTENT: Final[int]
MULTI_STATUS: Final[int]
IM_USED: Final[int]

MULTIPLE_CHOICES: Final[int]
MOVED_PERMANENTLY: Final[int]
FOUND: Final[int]
SEE_OTHER: Final[int]
NOT_MODIFIED: Final[int]
USE_PROXY: Final[int]
TEMPORARY_REDIRECT: Final[int]

BAD_REQUEST: Final[int]
UNAUTHORIZED: Final[int]
PAYMENT_REQUIRED: Final[int]
FORBIDDEN: Final[int]
NOT_FOUND: Final[int]
METHOD_NOT_ALLOWED: Final[int]
NOT_ACCEPTABLE: Final[int]
PROXY_AUTHENTICATION_REQUIRED: Final[int]
REQUEST_TIMEOUT: Final[int]
CONFLICT: Final[int]
GONE: Final[int]
LENGTH_REQUIRED: Final[int]
PRECONDITION_FAILED: Final[int]
REQUEST_ENTITY_TOO_LARGE: Final[int]
REQUEST_URI_TOO_LONG: Final[int]
UNSUPPORTED_MEDIA_TYPE: Final[int]
REQUESTED_RANGE_NOT_SATISFIABLE: Final[int]
EXPECTATION_FAILED: Final[int]
UNPROCESSABLE_ENTITY: Final[int]
LOCKED: Final[int]
FAILED_DEPENDENCY: Final[int]
UPGRADE_REQUIRED: Final[int]
PRECONDITION_REQUIRED: Final[int]
TOO_MANY_REQUESTS: Final[int]
REQUEST_HEADER_FIELDS_TOO_LARGE: Final[int]

INTERNAL_SERVER_ERROR: Final[int]
NOT_IMPLEMENTED: Final[int]
BAD_GATEWAY: Final[int]
SERVICE_UNAVAILABLE: Final[int]
GATEWAY_TIMEOUT: Final[int]
HTTP_VERSION_NOT_SUPPORTED: Final[int]
INSUFFICIENT_STORAGE: Final[int]
NOT_EXTENDED: Final[int]
NETWORK_AUTHENTICATION_REQUIRED: Final[int]

responses: dict[int, str]

class HTTPMessage(email.message.Message[str, str]):
    def getallmatchingheaders(self, name: str) -> list[str]: ...  # undocumented

@overload
def parse_headers(fp: SupportsReadline[bytes], _class: Callable[[], _MessageT]) -> _MessageT: ...
@overload
def parse_headers(fp: SupportsReadline[bytes]) -> HTTPMessage: ...

class HTTPResponse(io.BufferedIOBase, BinaryIO):  # type: ignore[misc]  # incompatible method definitions in the base classes
    msg: HTTPMessage
    headers: HTTPMessage
    version: int
    debuglevel: int
    fp: io.BufferedReader
    closed: bool
    status: int
    reason: str
    chunked: bool
    chunk_left: int | None
    length: int | None
    will_close: bool
    # url is set on instances of the class in urllib.request.AbstractHTTPHandler.do_open
    # to match urllib.response.addinfourl's interface.
    # It's not set in HTTPResponse.__init__ or any other method on the class
    url: str
    def __init__(self, sock: socket, debuglevel: int = 0, method: str | None = None, url: str | None = None) -> None: ...
    def peek(self, n: int = -1) -> bytes: ...
    def read(self, amt: int | None = None) -> bytes: ...
    def read1(self, n: int = -1) -> bytes: ...
    def readinto(self, b: WriteableBuffer) -> int: ...
    def readline(self, limit: int = -1) -> bytes: ...  # type: ignore[override]
    @overload
    def getheader(self, name: str) -> str | None: ...
    @overload
    def getheader(self, name: str, default: _T) -> str | _T: ...
    def getheaders(self) -> list[tuple[str, str]]: ...
    def isclosed(self) -> bool: ...
    def __iter__(self) -> Iterator[bytes]: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None
    ) -> None: ...
    def info(self) -> email.message.Message: ...
    def geturl(self) -> str: ...
    def getcode(self) -> int: ...
    def begin(self) -> None: ...

class HTTPConnection:
    auto_open: int  # undocumented
    debuglevel: int
    default_port: int  # undocumented
    response_class: type[HTTPResponse]  # undocumented
    timeout: float | None
    host: str
    port: int
    sock: socket | Any  # can be `None` if `.connect()` was not called
    def __init__(
        self,
        host: str,
        port: int | None = None,
        timeout: float | None = ...,
        source_address: tuple[str, int] | None = None,
        blocksize: int = 8192,
    ) -> None: ...
    def request(
        self,
        method: str,
        url: str,
        body: _DataType | str | None = None,
        headers: Mapping[str, str] = {},
        *,
        encode_chunked: bool = False,
    ) -> None: ...
    def getresponse(self) -> HTTPResponse: ...
    def set_debuglevel(self, level: int) -> None: ...
    if sys.version_info >= (3, 12):
        def get_proxy_response_headers(self) -> HTTPMessage | None: ...

    def set_tunnel(self, host: str, port: int | None = None, headers: Mapping[str, str] | None = None) -> None: ...
    def connect(self) -> None: ...
    def close(self) -> None: ...
    def putrequest(self, method: str, url: str, skip_host: bool = False, skip_accept_encoding: bool = False) -> None: ...
    def putheader(self, header: str | bytes, *argument: str | bytes) -> None: ...
    def endheaders(self, message_body: _DataType | None = None, *, encode_chunked: bool = False) -> None: ...
    def send(self, data: _DataType | str) -> None: ...

class HTTPSConnection(HTTPConnection):
    # Can be `None` if `.connect()` was not called:
    sock: ssl.SSLSocket | Any
    if sys.version_info >= (3, 12):
        def __init__(
            self,
            host: str,
            port: int | None = None,
            *,
            timeout: float | None = ...,
            source_address: tuple[str, int] | None = None,
            context: ssl.SSLContext | None = None,
            blocksize: int = 8192,
        ) -> None: ...
    else:
        def __init__(
            self,
            host: str,
            port: int | None = None,
            key_file: str | None = None,
            cert_file: str | None = None,
            timeout: float | None = ...,
            source_address: tuple[str, int] | None = None,
            *,
            context: ssl.SSLContext | None = None,
            check_hostname: bool | None = None,
            blocksize: int = 8192,
        ) -> None: ...

class HTTPException(Exception): ...

error = HTTPException

class NotConnected(HTTPException): ...
class InvalidURL(HTTPException): ...

class UnknownProtocol(HTTPException):
    def __init__(self, version: str) -> None: ...

class UnknownTransferEncoding(HTTPException): ...
class UnimplementedFileMode(HTTPException): ...

class IncompleteRead(HTTPException):
    def __init__(self, partial: bytes, expected: int | None = None) -> None: ...
    partial: bytes
    expected: int | None

class ImproperConnectionState(HTTPException): ...
class CannotSendRequest(ImproperConnectionState): ...
class CannotSendHeader(ImproperConnectionState): ...
class ResponseNotReady(ImproperConnectionState): ...

class BadStatusLine(HTTPException):
    def __init__(self, line: str) -> None: ...

class LineTooLong(HTTPException):
    def __init__(self, line_type: str) -> None: ...

class RemoteDisconnected(ConnectionResetError, BadStatusLine): ...
