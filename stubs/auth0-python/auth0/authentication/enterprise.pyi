from typing import Any

from .base import AuthenticationBase as AuthenticationBase

class Enterprise(AuthenticationBase):
    def saml_metadata(self) -> Any: ...
    def wsfed_metadata(self) -> Any: ...
