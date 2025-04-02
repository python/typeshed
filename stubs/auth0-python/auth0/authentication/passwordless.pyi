from _typeshed import Incomplete

from .base import AuthenticationBase as AuthenticationBase

class Passwordless(AuthenticationBase):
    def email(self, email: str, send: str = "link", auth_params: dict[str, str] | None = None) -> Incomplete: ...
    def sms(self, phone_number: str) -> Incomplete: ...
