from email.errors import MessageDefect
from http.client import IncompleteRead as httplib_IncompleteRead
from typing import Any

from urllib3.connectionpool import ConnectionPool, HTTPResponse
from urllib3.util.retry import Retry

class HTTPError(Exception): ...
class HTTPWarning(Warning): ...

class PoolError(HTTPError):
    pool: ConnectionPool
    def __init__(self, pool: ConnectionPool, message: str) -> None: ...
    def __reduce__(self) -> tuple[Any, tuple[Any, ...]]: ...

class RequestError(PoolError):
    url: str
    def __init__(self, pool: ConnectionPool, url: str, message: str) -> None: ...
    def __reduce__(self) -> tuple[Any, tuple[Any, ...]]: ...

class SSLError(HTTPError): ...

class ProxyError(HTTPError):
    original_error: Exception
    def __init__(self, message: str, error: Exception, *args: Any) -> None: ...

class DecodeError(HTTPError): ...
class ProtocolError(HTTPError): ...

ConnectionError = ProtocolError

class MaxRetryError(RequestError):
    reason: Exception | None
    def __init__(self, pool: ConnectionPool, url: str, reason: Exception | None = ...) -> None: ...

class HostChangedError(RequestError):
    retries: Retry | int
    def __init__(self, pool: ConnectionPool, url: str, retries: Retry | int = ...) -> None: ...

class TimeoutStateError(HTTPError): ...
class TimeoutError(HTTPError): ...
class ReadTimeoutError(TimeoutError, RequestError): ...
class ConnectTimeoutError(TimeoutError): ...
class NewConnectionError(ConnectTimeoutError, HTTPError): ...
class EmptyPoolError(PoolError): ...
class ClosedPoolError(PoolError): ...
class LocationValueError(ValueError, HTTPError): ...

class LocationParseError(LocationValueError):
    location: str
    def __init__(self, location: str) -> None: ...

class URLSchemeUnknown(LocationValueError):
    scheme: str
    def __init__(self, scheme: str) -> None: ...

class ResponseError(HTTPError):
    GENERIC_ERROR: str
    SPECIFIC_ERROR: str

class SecurityWarning(HTTPWarning): ...
class SubjectAltNameWarning(SecurityWarning): ...
class InsecureRequestWarning(SecurityWarning): ...
class SystemTimeWarning(SecurityWarning): ...
class InsecurePlatformWarning(SecurityWarning): ...
class SNIMissingWarning(HTTPWarning): ...
class DependencyWarning(HTTPWarning): ...
class ResponseNotChunked(ProtocolError, ValueError): ...
class BodyNotHttplibCompatible(HTTPError): ...

class IncompleteRead(HTTPError, httplib_IncompleteRead):
    def __init__(self, partial: bytes, expected: int | None) -> None: ...

class InvalidChunkLength(HTTPError, httplib_IncompleteRead):
    response: HTTPResponse
    length: bytes
    def __init__(self, response: HTTPResponse, length: bytes) -> None: ...
    def __repr__(self) -> str: ...

class InvalidHeader(HTTPError): ...

class ProxySchemeUnknown(AssertionError, URLSchemeUnknown):
    def __init__(self, scheme: str | None) -> None: ...

class ProxySchemeUnsupported(ValueError): ...

class HeaderParsingError(HTTPError):
    def __init__(self, defects: list[MessageDefect], unparsed_data: str | bytes | None) -> None: ...

class UnrewindableBodyError(HTTPError): ...
