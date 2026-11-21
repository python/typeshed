from collections.abc import Callable
from typing import Final, Protocol, TypedDict, type_check_only
from typing_extensions import NotRequired

from authlib.oauth2.rfc6749 import ClientMixin

@type_check_only
class _TokenGenerator(Protocol):
    def __call__(self, *, client: ClientMixin, grant_type: str, user, scope: str) -> str: ...

@type_check_only
class _Token(TypedDict):
    token_type: str
    access_token: str
    expires_in: NotRequired[int]
    refresh_token: NotRequired[str]
    scope: NotRequired[str]

class BearerTokenGenerator:
    DEFAULT_EXPIRES_IN: Final[int]
    GRANT_TYPES_EXPIRES_IN: Final[dict[str, int]]

    access_token_generator: _TokenGenerator
    refresh_token_generator: _TokenGenerator
    expires_generator: Callable[[ClientMixin, str], int]

    def __init__(
        self,
        access_token_generator: _TokenGenerator,
        refresh_token_generator: _TokenGenerator | None = None,
        expires_generator: Callable[[ClientMixin, str], int] | None = None,
    ) -> None: ...
    @staticmethod
    def get_allowed_scope(client: ClientMixin, scope: str) -> str: ...
    def generate(
        self,
        grant_type: str,
        client: ClientMixin,
        user=None,
        scope: str | None = None,
        expires_in: int | None = None,
        include_refresh_token: bool = True,
    ) -> _Token: ...
    def __call__(
        self,
        grant_type: str,
        client: ClientMixin,
        user=None,
        scope: str | None = None,
        expires_in: int | None = None,
        include_refresh_token: bool = True,
    ) -> _Token: ...
