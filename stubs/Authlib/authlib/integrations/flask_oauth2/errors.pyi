from _typeshed import Incomplete

from werkzeug.exceptions import HTTPException

class _HTTPException(HTTPException):
    code: Incomplete
    body: Incomplete
    headers: Incomplete
    def __init__(self, code, body, headers, response: Incomplete | None = None) -> None: ...
    def get_body(self, environ: Incomplete | None = None): ...
    def get_headers(self, environ: Incomplete | None = None): ...

class _HTTPException(HTTPException):
    code: Incomplete
    body: Incomplete
    headers: Incomplete
    def __init__(self, code, body, headers, response: Incomplete | None = None) -> None: ...
    def get_body(self, environ: Incomplete | None = None, scope: Incomplete | None = None): ...
    def get_headers(self, environ: Incomplete | None = None, scope: Incomplete | None = None): ...

def raise_http_exception(status, body, headers) -> None: ...
