from collections.abc import Callable
from typing import Any
from typing_extensions import TypeAlias

from authlib.oauth2.rfc6749 import ClientMixin

_TokenGenerator: TypeAlias = Callable[[ClientMixin, str, Any, str], str]

class BearerTokenGenerator:
    DEFAULT_EXPIRES_IN: int
    GRANT_TYPES_EXPIRES_IN: dict[str, int]
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
        user: Any | None = None,
        scope: str | None = None,
        expires_in: int | None = None,
        include_refresh_token: bool = True,
    ) -> dict[str, str | int]: ...
    def __call__(
        self,
        grant_type: str,
        client: ClientMixin,
        user: Any | None = None,
        scope: str | None = None,
        expires_in: int | None = None,
        include_refresh_token: bool = True,
    ) -> dict[str, str | int]: ...
