from _typeshed import OptExcInfo
from _typeshed.wsgi import ErrorStream, InputStream, StartResponse, WSGIApplication, WSGIEnvironment
from abc import abstractmethod
from typing import IO, Callable, MutableMapping

from .headers import Headers
from .util import FileWrapper

__all__ = ["BaseHandler", "SimpleHandler", "BaseCGIHandler", "CGIHandler", "IISCGIHandler", "read_environ"]

def format_date_time(timestamp: float | None) -> str: ...  # undocumented
def read_environ() -> dict[str, str]: ...

class BaseHandler:
    wsgi_version: tuple[int, int]  # undocumented
    wsgi_multithread: bool
    wsgi_multiprocess: bool
    wsgi_run_once: bool

    origin_server: bool
    http_version: str
    server_software: str | None

    os_environ: MutableMapping[str, str]

    wsgi_file_wrapper: type[FileWrapper] | None
    headers_class: type[Headers]  # undocumented

    traceback_limit: int | None
    error_status: str
    error_headers: list[tuple[str, str]]
    error_body: bytes
    def run(self, application: WSGIApplication) -> None: ...
    def setup_environ(self) -> None: ...
    def finish_response(self) -> None: ...
    def get_scheme(self) -> str: ...
    def set_content_length(self) -> None: ...
    def cleanup_headers(self) -> None: ...
    def start_response(
        self, status: str, headers: list[tuple[str, str]], exc_info: OptExcInfo | None = ...
    ) -> Callable[[bytes], None]: ...
    def send_preamble(self) -> None: ...
    def write(self, data: bytes) -> None: ...
    def sendfile(self) -> bool: ...
    def finish_content(self) -> None: ...
    def close(self) -> None: ...
    def send_headers(self) -> None: ...
    def result_is_file(self) -> bool: ...
    def client_is_modern(self) -> bool: ...
    def log_exception(self, exc_info: OptExcInfo) -> None: ...
    def handle_error(self) -> None: ...
    def error_output(self, environ: WSGIEnvironment, start_response: StartResponse) -> list[bytes]: ...
    @abstractmethod
    def _write(self, data: bytes) -> None: ...
    @abstractmethod
    def _flush(self) -> None: ...
    @abstractmethod
    def get_stdin(self) -> InputStream: ...
    @abstractmethod
    def get_stderr(self) -> ErrorStream: ...
    @abstractmethod
    def add_cgi_vars(self) -> None: ...

class SimpleHandler(BaseHandler):
    stdin: InputStream
    stdout: IO[bytes]
    stderr: ErrorStream
    base_env: MutableMapping[str, str]
    def __init__(
        self,
        stdin: InputStream,
        stdout: IO[bytes],
        stderr: ErrorStream,
        environ: MutableMapping[str, str],
        multithread: bool = ...,
        multiprocess: bool = ...,
    ) -> None: ...
    def get_stdin(self) -> InputStream: ...
    def get_stderr(self) -> ErrorStream: ...
    def add_cgi_vars(self) -> None: ...
    def _write(self, data: bytes) -> None: ...
    def _flush(self) -> None: ...

class BaseCGIHandler(SimpleHandler): ...

class CGIHandler(BaseCGIHandler):
    def __init__(self) -> None: ...

class IISCGIHandler(BaseCGIHandler):
    def __init__(self) -> None: ...
