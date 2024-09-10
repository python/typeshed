from _typeshed import Incomplete

class BearerTokenGenerator:
    DEFAULT_EXPIRES_IN: int
    GRANT_TYPES_EXPIRES_IN: Incomplete
    access_token_generator: Incomplete
    refresh_token_generator: Incomplete
    expires_generator: Incomplete
    def __init__(
        self,
        access_token_generator,
        refresh_token_generator: Incomplete | None = None,
        expires_generator: Incomplete | None = None,
    ) -> None: ...
    @staticmethod
    def get_allowed_scope(client, scope): ...
    def generate(
        self,
        grant_type,
        client,
        user: Incomplete | None = None,
        scope: Incomplete | None = None,
        expires_in: Incomplete | None = None,
        include_refresh_token: bool = True,
    ): ...
    def __call__(
        self,
        grant_type,
        client,
        user: Incomplete | None = None,
        scope: Incomplete | None = None,
        expires_in: Incomplete | None = None,
        include_refresh_token: bool = True,
    ): ...
