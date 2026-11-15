import socketserver
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
from typing_extensions import assert_type


class DefaultHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        assert_type(self.server, socketserver.BaseServer)


class CustomHTTPServer(HTTPServer): ...


class CustomHandler(BaseHTTPRequestHandler[CustomHTTPServer]):
    def do_GET(self) -> None:
        assert_type(self.server, CustomHTTPServer)


class CustomSimpleHandler(SimpleHTTPRequestHandler[CustomHTTPServer]):
    def do_GET(self) -> None:
        assert_type(self.server, CustomHTTPServer)


HTTPServer(("localhost", 0), DefaultHandler)
CustomHTTPServer(("localhost", 0), CustomHandler)
CustomHTTPServer(("localhost", 0), CustomSimpleHandler)
CustomHTTPServer(("localhost", 0), DefaultHandler)
HTTPServer(("localhost", 0), CustomHandler)  # type: ignore[arg-type]
