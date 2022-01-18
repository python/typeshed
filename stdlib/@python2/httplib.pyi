import mimetools
from typing import Any, Protocol

class HTTPMessage(mimetools.Message):
    def addcontinue(self, key: str, more: str) -> None: ...
    dict: dict[str, str]
    def addheader(self, key: str, value: str) -> None: ...
    unixfrom: str
    headers: Any
    status: str
    seekable: bool
    def readheaders(self) -> None: ...

class HTTPResponse:
    fp: Any
    debuglevel: Any
    strict: Any
    msg: Any
    version: Any
    status: Any
    reason: Any
    chunked: Any
    chunk_left: Any
    length: Any
    will_close: Any
    def __init__(
        self, sock, debuglevel: int = ..., strict: int = ..., method: Any | None = ..., buffering: bool = ...
    ) -> None: ...
    def begin(self): ...
    def close(self): ...
    def isclosed(self): ...
    def read(self, amt: Any | None = ...): ...
    def fileno(self): ...
    def getheader(self, name, default: Any | None = ...): ...
    def getheaders(self): ...

# This is an API stub only for HTTPConnection and HTTPSConnection, as used in
# urllib2.AbstractHTTPHandler.do_open, which takes either the class
# HTTPConnection or the class HTTPSConnection, *not* an instance of either
# class. do_open does not use all of the parameters of HTTPConnection.__init__
# or HTTPSConnection.__init__, so HTTPConnectionProtocol only implements the
# parameters that do_open does use.
class HTTPConnectionProtocol(Protocol):
    def __call__(self, host: str, timeout: int = ..., **http_con_args: Any) -> HTTPConnection: ...

class HTTPConnection:
    response_class: Any
    default_port: Any
    auto_open: Any
    debuglevel: Any
    strict: Any
    timeout: Any
    source_address: Any
    sock: Any
    host: str = ...
    port: int = ...
    def __init__(
        self, host, port: Any | None = ..., strict: Any | None = ..., timeout=..., source_address: Any | None = ...
    ) -> None: ...
    def set_tunnel(self, host, port: Any | None = ..., headers: Any | None = ...): ...
    def set_debuglevel(self, level): ...
    def connect(self): ...
    def close(self): ...
    def send(self, data): ...
    def putrequest(self, method, url, skip_host: int = ..., skip_accept_encoding: int = ...): ...
    def putheader(self, header, *values): ...
    def endheaders(self, message_body: Any | None = ...): ...
    def request(self, method, url, body: Any | None = ..., headers=...): ...
    def getresponse(self, buffering: bool = ...): ...

class HTTP:
    debuglevel: Any
    def __init__(self, host: str = ..., port: Any | None = ..., strict: Any | None = ...) -> None: ...
    def connect(self, host: Any | None = ..., port: Any | None = ...): ...
    def getfile(self): ...
    file: Any
    headers: Any
    def getreply(self, buffering: bool = ...): ...
    def close(self): ...

class HTTPSConnection(HTTPConnection):
    default_port: Any
    key_file: Any
    cert_file: Any
    def __init__(
        self,
        host,
        port: Any | None = ...,
        key_file: Any | None = ...,
        cert_file: Any | None = ...,
        strict: Any | None = ...,
        timeout=...,
        source_address: Any | None = ...,
        context: Any | None = ...,
    ) -> None: ...
    sock: Any
    def connect(self): ...

class HTTPS(HTTP):
    key_file: Any
    cert_file: Any
    def __init__(
        self,
        host: str = ...,
        port: Any | None = ...,
        key_file: Any | None = ...,
        cert_file: Any | None = ...,
        strict: Any | None = ...,
        context: Any | None = ...,
    ) -> None: ...

class HTTPException(Exception): ...
class NotConnected(HTTPException): ...
class InvalidURL(HTTPException): ...

class UnknownProtocol(HTTPException):
    args: Any
    version: Any
    def __init__(self, version) -> None: ...

class UnknownTransferEncoding(HTTPException): ...
class UnimplementedFileMode(HTTPException): ...

class IncompleteRead(HTTPException):
    args: Any
    partial: Any
    expected: Any
    def __init__(self, partial, expected: Any | None = ...) -> None: ...

class ImproperConnectionState(HTTPException): ...
class CannotSendRequest(ImproperConnectionState): ...
class CannotSendHeader(ImproperConnectionState): ...
class ResponseNotReady(ImproperConnectionState): ...

class BadStatusLine(HTTPException):
    args: Any
    line: Any
    def __init__(self, line) -> None: ...

class LineTooLong(HTTPException):
    def __init__(self, line_type) -> None: ...

error: Any

class LineAndFileWrapper:
    def __init__(self, line, file) -> None: ...
    def __getattr__(self, attr): ...
    def read(self, amt: Any | None = ...): ...
    def readline(self): ...
    def readlines(self, size: Any | None = ...): ...

# Constants

responses: dict[int, str]

HTTP_PORT: int
HTTPS_PORT: int

# status codes
# informational
CONTINUE: int
SWITCHING_PROTOCOLS: int
PROCESSING: int

# successful
OK: int
CREATED: int
ACCEPTED: int
NON_AUTHORITATIVE_INFORMATION: int
NO_CONTENT: int
RESET_CONTENT: int
PARTIAL_CONTENT: int
MULTI_STATUS: int
IM_USED: int

# redirection
MULTIPLE_CHOICES: int
MOVED_PERMANENTLY: int
FOUND: int
SEE_OTHER: int
NOT_MODIFIED: int
USE_PROXY: int
TEMPORARY_REDIRECT: int

# client error
BAD_REQUEST: int
UNAUTHORIZED: int
PAYMENT_REQUIRED: int
FORBIDDEN: int
NOT_FOUND: int
METHOD_NOT_ALLOWED: int
NOT_ACCEPTABLE: int
PROXY_AUTHENTICATION_REQUIRED: int
REQUEST_TIMEOUT: int
CONFLICT: int
GONE: int
LENGTH_REQUIRED: int
PRECONDITION_FAILED: int
REQUEST_ENTITY_TOO_LARGE: int
REQUEST_URI_TOO_LONG: int
UNSUPPORTED_MEDIA_TYPE: int
REQUESTED_RANGE_NOT_SATISFIABLE: int
EXPECTATION_FAILED: int
UNPROCESSABLE_ENTITY: int
LOCKED: int
FAILED_DEPENDENCY: int
UPGRADE_REQUIRED: int

# server error
INTERNAL_SERVER_ERROR: int
NOT_IMPLEMENTED: int
BAD_GATEWAY: int
SERVICE_UNAVAILABLE: int
GATEWAY_TIMEOUT: int
HTTP_VERSION_NOT_SUPPORTED: int
INSUFFICIENT_STORAGE: int
NOT_EXTENDED: int
