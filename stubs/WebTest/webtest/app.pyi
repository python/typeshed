import json
from _typeshed.wsgi import WSGIApplication
from collections.abc import Mapping, Sequence
from http.cookiejar import CookieJar, DefaultCookiePolicy
from typing import Any, Generic, Literal, TypeVar
from typing_extensions import TypeAlias

from webob.request import BaseRequest
from webtest.response import TestResponse

_Files: TypeAlias = Sequence[tuple[str, str] | tuple[str, str, bytes]]
_AppT = TypeVar("_AppT", bound=WSGIApplication, default=WSGIApplication)

__all__ = ["TestApp", "TestRequest"]

class AppError(Exception):
    def __init__(self, message: str, *args: object) -> None: ...

class CookiePolicy(DefaultCookiePolicy): ...

class TestRequest(BaseRequest):
    ResponseClass: type[TestResponse]
    __test__: Literal[False]

class TestApp(Generic[_AppT]):
    RequestClass: type[TestRequest]
    app: _AppT
    lint: bool
    relative_to: str | None
    extra_environ: dict[str, Any]
    use_unicode: bool
    cookiejar: CookieJar
    JSONEncoder: json.JSONEncoder
    __test__: Literal[False]
    def __init__(
        self,
        app: _AppT,
        extra_environ: dict[str, Any] | None = None,
        relative_to: str | None = None,
        use_unicode: bool = True,
        cookiejar: CookieJar | None = None,
        parser_features: Sequence[str] | str | None = None,
        json_encoder: json.JSONEncoder | None = None,
        lint: bool = True,
    ) -> None: ...
    def get_authorization(self) -> tuple[str, str | tuple[str, str]]: ...
    def set_authorization(self, value: tuple[str, str | tuple[str, str]]) -> None: ...
    @property
    def authorization(self) -> tuple[str, str | tuple[str, str]]: ...
    @authorization.setter
    def authorization(self, value: tuple[str, str | tuple[str, str]]) -> None: ...
    @property
    def cookies(self) -> dict[str, str | None]: ...
    def set_cookie(self, name: str, value: str | None) -> None: ...
    def reset(self) -> None: ...
    def set_parser_features(self, parser_features: Sequence[str] | str) -> None: ...
    def get(
        self,
        url: str,
        params: Mapping[str, str] | str | None = None,
        headers: Mapping[str, str] | None = None,
        extra_environ: Mapping[str, Any] | None = None,
        status: int | str | None = None,
        expect_errors: bool = False,
        xhr: bool = False,
    ) -> TestResponse: ...
    def post(
        self,
        url: str,
        params: Mapping[str, str] | str = "",
        headers: Mapping[str, str] | None = None,
        extra_environ: Mapping[str, Any] | None = None,
        status: int | str | None = None,
        upload_files: _Files | None = None,
        expect_errors: bool = False,
        content_type: str | None = None,
        xhr: bool = False,
    ) -> TestResponse: ...
    def put(
        self,
        url: str,
        params: Mapping[str, str] | str = "",
        headers: Mapping[str, str] | None = None,
        extra_environ: Mapping[str, Any] | None = None,
        status: int | str | None = None,
        upload_files: _Files | None = None,
        expect_errors: bool = False,
        content_type: str | None = None,
        xhr: bool = False,
    ) -> TestResponse: ...
    def patch(
        self,
        url: str,
        params: Mapping[str, str] | str = "",
        headers: Mapping[str, str] | None = None,
        extra_environ: Mapping[str, Any] | None = None,
        status: int | str | None = None,
        upload_files: _Files | None = None,
        expect_errors: bool = False,
        content_type: str | None = None,
        xhr: bool = False,
    ) -> TestResponse: ...
    def delete(
        self,
        url: str,
        params: Mapping[str, str] | str = "",
        headers: Mapping[str, str] | None = None,
        extra_environ: Mapping[str, Any] | None = None,
        status: int | str | None = None,
        expect_errors: bool = False,
        content_type: str | None = None,
        xhr: bool = False,
    ) -> TestResponse: ...
    def options(
        self,
        url: str,
        headers: Mapping[str, str] | None = None,
        extra_environ: Mapping[str, Any] | None = None,
        status: int | str | None = None,
        expect_errors: bool = False,
        xhr: bool = False,
    ) -> TestResponse: ...
    def head(
        self,
        url: str,
        params: Mapping[str, str] | str | None = None,
        headers: Mapping[str, str] | None = None,
        extra_environ: Mapping[str, Any] | None = None,
        status: int | str | None = None,
        expect_errors: bool = False,
        xhr: bool = False,
    ) -> TestResponse: ...
    def post_json(
        self,
        url: str,
        params: Any = ...,
        *,
        headers: Mapping[str, str] | None = None,
        extra_environ: Mapping[str, Any] | None = None,
        status: int | str | None = None,
        expect_errors: bool = False,
        content_type: str | None = None,
        xhr: bool = False,
    ) -> TestResponse: ...
    def put_json(
        self,
        url: str,
        params: Any = ...,
        *,
        headers: Mapping[str, str] | None = None,
        extra_environ: Mapping[str, Any] | None = None,
        status: int | str | None = None,
        expect_errors: bool = False,
        content_type: str | None = None,
        xhr: bool = False,
    ) -> TestResponse: ...
    def patch_json(
        self,
        url: str,
        params: Any = ...,
        *,
        headers: Mapping[str, str] | None = None,
        extra_environ: Mapping[str, Any] | None = None,
        status: int | str | None = None,
        expect_errors: bool = False,
        content_type: str | None = None,
        xhr: bool = False,
    ) -> TestResponse: ...
    def delete_json(
        self,
        url: str,
        params: Any = ...,
        *,
        headers: Mapping[str, str] | None = None,
        extra_environ: Mapping[str, Any] | None = None,
        status: int | str | None = None,
        expect_errors: bool = False,
        content_type: str | None = None,
        xhr: bool = False,
    ) -> TestResponse: ...
    def encode_multipart(self, params: Sequence[tuple[str, str]], files: _Files) -> tuple[str, bytes]: ...
    def request(
        self, url_or_req: str | TestRequest, status: int | str | None = None, expect_errors: bool = False, **req_params: Any
    ) -> TestResponse: ...
    def do_request(
        self, req: TestRequest, status: int | str | None = None, expect_errors: bool | None = None
    ) -> TestResponse: ...
