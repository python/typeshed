from collections.abc import Callable, Collection

from authlib.oauth2 import OAuth2Request
from authlib.oauth2.rfc6749 import ClientMixin

__all__ = ["ClientAuthentication"]

class ClientAuthentication:
    query_client: Callable[[str], ClientMixin]
    def __init__(self, query_client: Callable[[str], ClientMixin]) -> None: ...
    def register(self, method: str, func: Callable[[Callable[[str], ClientMixin], OAuth2Request], ClientMixin]) -> None: ...
    def authenticate(self, request: OAuth2Request, methods: Collection[str], endpoint: str) -> ClientMixin: ...
    def __call__(self, request: OAuth2Request, methods: Collection[str], endpoint: str = "token") -> ClientMixin: ...
