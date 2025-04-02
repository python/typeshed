from typing import Any

from .base import AuthenticationBase as AuthenticationBase

class Database(AuthenticationBase):
    def signup(
        self,
        email: str,
        password: str,
        connection: str,
        username: str | None = None,
        user_metadata: dict[str, Any] | None = None,
        given_name: str | None = None,
        family_name: str | None = None,
        name: str | None = None,
        nickname: str | None = None,
        picture: str | None = None,
    ) -> dict[str, Any]: ...
    def change_password(
        self, email: str, connection: str, password: str | None = None, organization: str | None = None
    ) -> str: ...
