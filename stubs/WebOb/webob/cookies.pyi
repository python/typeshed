from _typeshed import Incomplete
from collections.abc import ItemsView, Iterator, KeysView, MutableMapping, ValuesView
from typing import Any, TypeVar, overload

_T = TypeVar("_T")

class RequestCookies(MutableMapping[str, str]):
    def __init__(self, environ: dict[str, Any]) -> None: ...
    def __setitem__(self, name: str, value: str) -> None: ...
    def __getitem__(self, name: str) -> str: ...
    @overload
    def get(self, name: str) -> str | None: ...
    @overload
    def get(self, name: str, default: str | _T) -> str | _T: ...
    def __delitem__(self, name: str) -> None: ...
    def keys(self) -> KeysView[str]: ...
    def values(self) -> ValuesView[str]: ...
    def items(self) -> ItemsView[str, str]: ...
    def __contains__(self, name: object) -> bool: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def clear(self) -> None: ...

class Cookie(dict[str, Incomplete]):
    def __init__(self, input: Incomplete | None = ...) -> None: ...
    def load(self, data) -> None: ...
    def add(self, key, val): ...
    __setitem__ = add
    def serialize(self, full: bool = ...): ...
    def values(self): ...

class Morsel(dict[str, Incomplete]):
    name: Incomplete
    value: Incomplete
    def __init__(self, name, value) -> None: ...
    path: Incomplete
    domain: Incomplete
    comment: Incomplete
    expires: Incomplete
    max_age: Incomplete
    httponly: Incomplete
    secure: Incomplete
    samesite: Incomplete
    def __setitem__(self, k, v) -> None: ...
    def serialize(self, full: bool = ...): ...

def make_cookie(
    name,
    value,
    max_age: Incomplete | None = ...,
    path: str = ...,
    domain: Incomplete | None = ...,
    secure: bool = ...,
    httponly: bool = ...,
    comment: Incomplete | None = ...,
    samesite: Incomplete | None = ...,
): ...

class JSONSerializer:
    def dumps(self, appstruct): ...
    def loads(self, bstruct): ...

class Base64Serializer:
    serializer: Incomplete
    def __init__(self, serializer: Incomplete | None = ...) -> None: ...
    def dumps(self, appstruct): ...
    def loads(self, bstruct): ...

class SignedSerializer:
    salt: Incomplete
    secret: Incomplete
    hashalg: Incomplete
    salted_secret: Incomplete
    digestmod: Incomplete
    digest_size: Incomplete
    serializer: Incomplete
    def __init__(self, secret, salt, hashalg: str = ..., serializer: Incomplete | None = ...) -> None: ...
    def dumps(self, appstruct): ...
    def loads(self, bstruct): ...

class CookieProfile:
    cookie_name: Incomplete
    secure: Incomplete
    max_age: Incomplete
    httponly: Incomplete
    samesite: Incomplete
    path: Incomplete
    domains: Incomplete
    serializer: Incomplete
    request: Incomplete
    def __init__(
        self,
        cookie_name,
        secure: bool = ...,
        max_age: Incomplete | None = ...,
        httponly: Incomplete | None = ...,
        samesite: Incomplete | None = ...,
        path: str = ...,
        domains: Incomplete | None = ...,
        serializer: Incomplete | None = ...,
    ) -> None: ...
    def __call__(self, request): ...
    def bind(self, request): ...
    def get_value(self): ...
    def set_cookies(self, response, value, domains=..., max_age=..., path=..., secure=..., httponly=..., samesite=...): ...
    def get_headers(self, value, domains=..., max_age=..., path=..., secure=..., httponly=..., samesite=...): ...

class SignedCookieProfile(CookieProfile):
    secret: Incomplete
    salt: Incomplete
    hashalg: Incomplete
    original_serializer: Incomplete
    def __init__(
        self,
        secret,
        salt,
        cookie_name,
        secure: bool = ...,
        max_age: Incomplete | None = ...,
        httponly: bool = ...,
        samesite: Incomplete | None = ...,
        path: str = ...,
        domains: Incomplete | None = ...,
        hashalg: str = ...,
        serializer: Incomplete | None = ...,
    ) -> None: ...
    def bind(self, request): ...
