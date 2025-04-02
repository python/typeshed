from _typeshed import Incomplete

from .base import AuthenticationBase as AuthenticationBase

class Enterprise(AuthenticationBase):
    def saml_metadata(self) -> Incomplete: ...
    def wsfed_metadata(self) -> Incomplete: ...
