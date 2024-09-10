from _typeshed import Incomplete

from ..base_client import FrameworkIntegration

token_update: Incomplete

class DjangoIntegration(FrameworkIntegration):
    def update_token(self, token, refresh_token: Incomplete | None = None, access_token: Incomplete | None = None) -> None: ...
    @staticmethod
    def load_config(oauth, name, params): ...
