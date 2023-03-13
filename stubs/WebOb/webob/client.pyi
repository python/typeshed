from http.client import HTTPMessage
from typing import Any, ClassVar

from webob.response import _StartResponse

class SendRequest:
    def __init__(self, HTTPConnection=..., HTTPSConnection=...) -> None: ...
    def __call__(self, environ: dict[str, Any], start_response: _StartResponse): ...
    filtered_headers: ClassVar[tuple[str, ...]]
    def parse_headers(self, message: HTTPMessage): ...

send_request_app: SendRequest
