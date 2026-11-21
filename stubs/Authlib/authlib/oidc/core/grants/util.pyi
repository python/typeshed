from _typeshed import FloatInt, ReadableBuffer
from collections.abc import Collection, Iterable
from typing import Literal, SupportsBytes, SupportsIndex, TypeVar, overload

from authlib.oauth2.rfc6749.grants.base import BaseGrant
from authlib.oidc.core import UserInfo
from authlib.oidc.core.grants.implicit import OpenIDImplicitGrant

_G = TypeVar("_G", bound=BaseGrant)

def is_openid_scope(scope: Collection[str] | str | None) -> bool: ...
def validate_request_prompt(grant: _G, redirect_uri: str, redirect_fragment: bool = False) -> _G: ...
def validate_form_post_redirect_uri(grant: OpenIDImplicitGrant, redirect_uri: str) -> None: ...
def validate_nonce(request, exists_nonce, required: bool = False): ...
def generate_id_token(
    token: dict[str, str | int],
    user_info: UserInfo,
    key: str,
    iss: str,
    aud: list[str],
    alg: str = "RS256",
    exp: int = 3600,
    nonce: str | None = None,
    auth_time: int | None = None,
    acr: str | None = None,
    amr: list[str] | None = None,
    code: str | bytes | FloatInt | Iterable[SupportsIndex] | SupportsIndex | SupportsBytes | ReadableBuffer | None = None,
    kid: str | None = None,
) -> str: ...

@overload
def create_response_mode_response(
    redirect_uri: str, params: Iterable[tuple[str, str]], response_mode: Literal["form_post"]
) -> tuple[Literal[200], str, list[tuple[str, str]]]: ...
@overload  # `params` can accept dict in another mode
def create_response_mode_response(
    redirect_uri: str, params: Iterable[tuple[str, str]] | dict[str, str], response_mode: Literal["query", "fragment"]
) -> tuple[Literal[302], str, list[tuple[str, str]]]: ...
