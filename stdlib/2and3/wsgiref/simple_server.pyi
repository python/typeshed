import sys
from types import TracebackType
from typing import Optional, Dict, TextIO, Text, List, Tuple, Callable, Union, Type, TypeVar

from .handlers import SimpleHandler
from .types import WSGIApplication, WSGIEnvironment, ErrorStream

if sys.version_info < (3,):
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
else:
    from http.server import HTTPServer, BaseHTTPRequestHandler

_exc_info = Tuple[Optional[Type[BaseException]],
                  Optional[BaseException],
                  Optional[TracebackType]]
_StartResponse = Union[
    Callable[[Text, List[Tuple[Text, Text]]], Callable[[bytes], None]],
    Callable[[Text, List[Tuple[Text, Text]], _exc_info], Callable[[bytes], None]]
]

server_version: str  # undocumented
sys_version: str  # undocumented
software_version: str  # undocumented

class ServerHandler(SimpleHandler):  # undocumented
    server_software: str
    def close(self) -> None: ...

class WSGIServer(HTTPServer):
    application: Optional[WSGIApplication]
    base_environ: Dict[str, str]  # only available after call to setup_environ()
    def setup_environ(self) -> None: ...
    def get_app(self) -> Optional[WSGIApplication]: ...
    def set_app(self, application: Optional[WSGIApplication]) -> None: ...

class WSGIRequestHandler(BaseHTTPRequestHandler):
    server_version: str
    def get_environ(self) -> WSGIEnvironment: ...
    def get_stderr(self) -> ErrorStream: ...
    def handle(self) -> None: ...

def demo_app(environ: WSGIEnvironment, start_response: _StartResponse) -> List[bytes]: ...

_S = TypeVar("_S", bound=WSGIServer)

def make_server(host: str, port: int, app: WSGIApplication, server_class: Type[_S] = ..., handler_class: Type[WSGIRequestHandler] = ...) -> _S: ...
