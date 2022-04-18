import BaseHTTPServer
from StringIO import StringIO
from typing import IO, Any, AnyStr, Mapping

class SimpleHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    server_version: str
    def do_GET(self) -> None: ...
    def do_HEAD(self) -> None: ...
    def send_head(self) -> IO[str] | None: ...
    def list_directory(self, path: str | unicode) -> StringIO[Any] | None: ...
    def translate_path(self, path: AnyStr) -> AnyStr: ...
    def copyfile(self, source: IO[AnyStr], outputfile: IO[AnyStr]): ...
    def guess_type(self, path: str | unicode) -> str: ...
    extensions_map: Mapping[str, str]
