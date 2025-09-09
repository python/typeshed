from collections.abc import Awaitable, Iterable
from typing import Any, Callable, LiteralString

type _StatusType = str
type _HeadersType = list[tuple[str, str]]

type _EnvironType = dict[str, Any]
# """
# WSGI environment dictionary containing request and server information.
#
# Keys and their types:
# - wsgi.version: tuple[int, int]
#     WSGI version (e.g., (1, 0)). Required.
# - wsgi.url_scheme: str
#     URL scheme (e.g., 'http', 'https'). Required.
# - wsgi.input: io.BytesIO
#     Input stream for request body. Required.
# - wsgi.errors: WSGIErrorsWrapper
#     Error stream for logging. Required.
# - wsgi.multithread: bool
#     Indicates if the server supports multithreading (False in Gunicorn). Required.
# - wsgi.multiprocess: bool
#     Indicates if the server supports multiprocessing (based on cfg.workers). Required.
# - wsgi.run_once: bool
#     Indicates if the application runs once (False in Gunicorn). Required.
# - wsgi.file_wrapper: type[FileWrapper]
#     Type of FileWrapper class for file handling. Required.
# - wsgi.input_terminated: bool
#     Indicates if the input stream is terminated (True in Gunicorn). Required.
# - SERVER_SOFTWARE: str
#     Server software description. Required.
# - gunicorn.socket: socket.socket
#     Socket for the connection. Required.
# - REQUEST_METHOD: str
#     HTTP request method (e.g., 'GET', 'POST'). Required.
# - QUERY_STRING: str
#     Query string (may be empty). Required.
# - RAW_URI: str
#     Raw URI of the request. Required.
# - SERVER_PROTOCOL: str
#     HTTP protocol version (e.g., 'HTTP/1.1'). Required.
# - SERVER_NAME: str
#     Server name. Required.
# - SERVER_PORT: str
#     Server port (may be empty for Unix sockets). Required.
# - PATH_INFO: str
#     Request path, excluding SCRIPT_NAME. Required.
# - SCRIPT_NAME: str
#     Application path prefix (may be empty). Required.
# - REMOTE_ADDR: str
#     Client IP address. Required.
# - REMOTE_PORT: str
#     Client port. Optional.
# - CONTENT_TYPE: str
#     Content type from request headers. Optional.
# - CONTENT_LENGTH: str
#     Content length from request headers. Optional.
# - HTTP_HOST: str
#     Host header value. Optional.
# - HTTP_*: str
#     Other HTTP headers (e.g., HTTP_ACCEPT, HTTP_USER_AGENT). Optional.
# - PROXY_PROTOCOL: str
#     Proxy protocol, if proxy_protocol_info is present. Optional.
# - PROXY_ADDR: str
#     Proxy address, if proxy_protocol_info is present. Optional.
# - PROXY_PORT: str
#     Proxy port, if proxy_protocol_info is present. Optional.
# """

type _StartResponseType = Callable[[_StatusType, _HeadersType], None]
type _ResponseBodyType = Iterable[bytes]

type _WSGIAppType = Callable[[_EnvironType, _StartResponseType], _ResponseBodyType]

type _ScopeType = dict[str, Any]
type _ReceiveType = Callable[[], Awaitable[dict[str, Any]]]
type _SendType = Callable[[dict[str, Any]], Awaitable[None]]
type _ASGIAppType = Callable[[_ScopeType, _ReceiveType, _SendType], Awaitable[None]]

type _UnixSocketPathType = str
type _FileDescriptorType = int
type _TcpAddressType = tuple[LiteralString, int]
type _AddressType = _UnixSocketPathType | _FileDescriptorType | _TcpAddressType
