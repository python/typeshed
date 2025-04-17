from _typeshed import Incomplete

__all__ = ["AsyncOpenIDMixin"]

class AsyncOpenIDMixin:
    async def fetch_jwk_set(self, force: bool = False): ...
    async def userinfo(self, **kwargs): ...
    async def parse_id_token(
        self, token, nonce, claims_options: Incomplete | None = None, claims_cls: Incomplete | None = None, leeway: int = 120
    ): ...
