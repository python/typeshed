from typing import Any, Dict, NoReturn, Optional, Protocol, Type

from wsgiref.types import WSGIEnvironment
from werkzeug.wrappers import Response

class _EnvironContainer(Protocol):
    @property
    def environ(self) -> WSGIEnvironment: ...

class HTTPException(Exception):
    code = ...  # type: Optional[int]
    description = ...  # type: Optional[str]
    response = ...  # type: Optional[Response]
    def __init__(self, description: Optional[str]=..., response: Optional[Response]=...) -> None: ...
    @classmethod
    def wrap(cls, exception: Type[Exception], name=Optional[str]=...): ...
    @property
    def name(self) -> str: ...
    def get_description(self, environ=Optional[WSGIEnvironment]=...) -> str: ...
    def get_body(self, environ=Optional[WSGIEnvironment]=...) -> str: ...
    def get_headers(self, environ=Optional[WSGIEnvironment]=...) -> Dict[str, str]: ...
    def get_response(self, environ: Optional[Union[WSGIEnvironment, _EnvironContainer]]=...) -> Response: ...
    def __call__(self, environ: WSGIEnvironment, start_response: typing.Any) -> Response: ...

default_exceptions: Dict[int, HTTPException]

class BadRequest(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class ClientDisconnected(BadRequest): ...
class SecurityError(BadRequest): ...
class BadHost(BadRequest): ...

class Unauthorized(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class Forbidden(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class NotFound(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class MethodNotAllowed(HTTPException):
    code = ...  # type: int
    description = ...  # type: str
    valid_methods = ...  # type: Any
    def __init__(self, valid_methods=None, description=None): ...
    def get_headers(self, environ): ...

class NotAcceptable(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class RequestTimeout(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class Conflict(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class Gone(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class LengthRequired(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class PreconditionFailed(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class RequestEntityTooLarge(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class RequestURITooLarge(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class UnsupportedMediaType(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class RequestedRangeNotSatisfiable(HTTPException):
    code = ...  # type: int
    description = ...  # type: str
    length = ...  # type: Any
    units = ...  # type: Any
    def __init__(self, length=None, units='', description=None): ...
    def get_headers(self, environ): ...

class ExpectationFailed(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class ImATeapot(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class UnprocessableEntity(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class Locked(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class PreconditionRequired(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class TooManyRequests(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class RequestHeaderFieldsTooLarge(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class UnavailableForLegalReasons(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class InternalServerError(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class NotImplemented(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class BadGateway(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class ServiceUnavailable(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class GatewayTimeout(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class HTTPVersionNotSupported(HTTPException):
    code = ...  # type: int
    description = ...  # type: str

class Aborter:
    mapping = ...  # type: Any
    def __init__(self, mapping=None, extra=None) -> None: ...
    def __call__(self, code, *args, **kwargs) -> NoReturn: ...

def abort(status: Any, *args: Any, **kwargs: Any) -> NoReturn: ...
