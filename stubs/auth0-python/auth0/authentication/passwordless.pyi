from typing import Any

from .base import AuthenticationBase as AuthenticationBase

class Passwordless(AuthenticationBase):
    def email(self, email: str, send: str = "link", auth_params: dict[str, str] | None = None) -> Any: ...
    def sms(self, phone_number: str) -> Any: ...
