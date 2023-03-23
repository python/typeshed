from _typeshed import SupportsItems, SupportsKeysAndGetItem
from _typeshed.wsgi import StartResponse, WSGIApplication
from collections.abc import Iterable
from string import Template
from typing import Any, Protocol
from typing_extensions import Literal, Self

from webob.response import Response

class _JSONFormatter(Protocol):
    def __call__(self, body: str, status: str, title: str, environ: dict[str, Any]) -> str: ...

class HTTPException(Exception):
    wsgi_response: Response
    def __init__(self, message: str, wsgi_response: Response) -> None: ...
    def __call__(self, environ: dict[str, Any], start_response: StartResponse) -> Iterable[bytes]: ...

class WSGIHTTPException(Response, HTTPException):
    code: int
    title: str
    explanation: str
    body_template_obj: Template
    plain_template_obj: Template
    html_template_obj: Template
    empty_body: bool
    detail: str | None
    comment: str | None
    def __init__(
        self,
        detail: str | None = ...,
        headers: SupportsItems[str, str] | SupportsKeysAndGetItem[str, str] | Iterable[tuple[str, str]] | None = ...,
        comment: str | None = ...,
        body_template: str | None = ...,
        json_formatter: _JSONFormatter | None = ...,
        **kw: Any,
    ) -> None: ...
    def plain_body(self, environ: dict[str, Any]) -> str: ...
    def html_body(self, environ: dict[str, Any]) -> str: ...
    def json_formatter(self, body: str, status: str, title: str, environ: dict[str, Any]) -> str: ...
    def json_body(self, environ: dict[str, Any]) -> str: ...
    def generate_response(self, environ: dict[str, Any], start_response: StartResponse) -> Iterable[bytes]: ...
    @property
    def wsgi_response(self) -> Self: ...  # type:ignore[override]
    def __str__(self) -> str: ...  # type:ignore[override]  # noqaY029

class HTTPError(WSGIHTTPException): ...
class HTTPRedirection(WSGIHTTPException): ...
class HTTPOk(WSGIHTTPException): ...
class HTTPCreated(HTTPOk): ...
class HTTPAccepted(HTTPOk): ...
class HTTPNonAuthoritativeInformation(HTTPOk): ...

class HTTPNoContent(HTTPOk):
    empty_body: Literal[True]

class HTTPResetContent(HTTPOk):
    empty_body: Literal[True]

class HTTPPartialContent(HTTPOk): ...

class _HTTPMove(HTTPRedirection):
    explanation: str
    add_slash: bool
    def __init__(
        self,
        detail: str | None = ...,
        headers: str | None = ...,
        comment: str | None = ...,
        body_template: str | None = ...,
        location: str | None = ...,
        add_slash: bool = ...,
    ) -> None: ...

class HTTPMultipleChoices(_HTTPMove): ...
class HTTPMovedPermanently(_HTTPMove): ...
class HTTPFound(_HTTPMove): ...
class HTTPSeeOther(_HTTPMove): ...

class HTTPNotModified(HTTPRedirection):
    empty_body: Literal[True]

class HTTPUseProxy(_HTTPMove): ...
class HTTPTemporaryRedirect(_HTTPMove): ...
class HTTPPermanentRedirect(_HTTPMove): ...
class HTTPClientError(HTTPError): ...
class HTTPBadRequest(HTTPClientError): ...
class HTTPUnauthorized(HTTPClientError): ...
class HTTPPaymentRequired(HTTPClientError): ...
class HTTPForbidden(HTTPClientError): ...
class HTTPNotFound(HTTPClientError): ...
class HTTPMethodNotAllowed(HTTPClientError): ...
class HTTPNotAcceptable(HTTPClientError): ...
class HTTPProxyAuthenticationRequired(HTTPClientError): ...
class HTTPRequestTimeout(HTTPClientError): ...
class HTTPConflict(HTTPClientError): ...
class HTTPGone(HTTPClientError): ...
class HTTPLengthRequired(HTTPClientError): ...
class HTTPPreconditionFailed(HTTPClientError): ...
class HTTPRequestEntityTooLarge(HTTPClientError): ...
class HTTPRequestURITooLong(HTTPClientError): ...
class HTTPUnsupportedMediaType(HTTPClientError): ...
class HTTPRequestRangeNotSatisfiable(HTTPClientError): ...
class HTTPExpectationFailed(HTTPClientError): ...
class HTTPUnprocessableEntity(HTTPClientError): ...
class HTTPLocked(HTTPClientError): ...
class HTTPFailedDependency(HTTPClientError): ...
class HTTPPreconditionRequired(HTTPClientError): ...
class HTTPTooManyRequests(HTTPClientError): ...
class HTTPRequestHeaderFieldsTooLarge(HTTPClientError): ...
class HTTPUnavailableForLegalReasons(HTTPClientError): ...
class HTTPServerError(HTTPError): ...
class HTTPInternalServerError(HTTPServerError): ...
class HTTPNotImplemented(HTTPServerError): ...
class HTTPBadGateway(HTTPServerError): ...
class HTTPServiceUnavailable(HTTPServerError): ...
class HTTPGatewayTimeout(HTTPServerError): ...
class HTTPVersionNotSupported(HTTPServerError): ...
class HTTPInsufficientStorage(HTTPServerError): ...
class HTTPNetworkAuthenticationRequired(HTTPServerError): ...

class HTTPExceptionMiddleware:
    application: WSGIApplication
    def __init__(self, application: WSGIApplication) -> None: ...
    def __call__(self, environ: dict[str, Any], start_response: StartResponse) -> Iterable[bytes]: ...

status_map: dict[int, WSGIHTTPException]
