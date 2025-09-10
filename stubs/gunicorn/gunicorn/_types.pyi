from collections.abc import Awaitable, Callable, Iterable
from typing import Any
from typing_extensions import LiteralString, TypeAlias

_StatusType: TypeAlias = str
_HeadersType: TypeAlias = list[tuple[str, str]]

_EnvironType: TypeAlias = dict[str, Any]
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

_StartResponseType: TypeAlias = Callable[[_StatusType, _HeadersType], None]
_ResponseBodyType: TypeAlias = Iterable[bytes]
_WSGIAppType: TypeAlias = Callable[[_EnvironType, _StartResponseType], _ResponseBodyType]  # noqa: Y047

_ScopeType: TypeAlias = dict[str, Any]
_ReceiveType: TypeAlias = Callable[[], Awaitable[dict[str, Any]]]
_SendType: TypeAlias = Callable[[dict[str, Any]], Awaitable[None]]
_ASGIAppType: TypeAlias = Callable[[_ScopeType, _ReceiveType, _SendType], Awaitable[None]]  # noqa: Y047

_UnixSocketPathType: TypeAlias = str
_FileDescriptorType: TypeAlias = int
_TcpAddressType: TypeAlias = tuple[LiteralString, int]  # noqa: Y047
_AddressType: TypeAlias = _UnixSocketPathType | _FileDescriptorType | _TcpAddressType  # noqa: Y047
