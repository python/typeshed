from _typeshed.wsgi import StartResponse
from collections.abc import Iterable
from http.client import HTTPMessage
from typing import Any, ClassVar

class SendRequest:
    def __init__(self, HTTPConnection=..., HTTPSConnection=...) -> None: ...
    def __call__(self, environ: dict[str, Any], start_response: StartResponse) -> Iterable[bytes]: ...
    filtered_headers: ClassVar[tuple[str, ...]]
    def parse_headers(self, message: HTTPMessage) -> list[tuple[str, str]]: ...

send_request_app: SendRequest
