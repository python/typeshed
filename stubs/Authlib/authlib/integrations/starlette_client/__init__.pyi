from _typeshed import Incomplete

from ..base_client import BaseOAuth, OAuthError as OAuthError
from .apps import StarletteOAuth1App as StarletteOAuth1App, StarletteOAuth2App as StarletteOAuth2App
from .integration import StarletteIntegration as StarletteIntegration

__all__ = ["OAuth", "OAuthError", "StarletteIntegration", "StarletteOAuth1App", "StarletteOAuth2App"]

class OAuth(BaseOAuth):
    oauth1_client_cls = StarletteOAuth1App
    oauth2_client_cls = StarletteOAuth2App
    framework_integration_cls = StarletteIntegration
    config: Incomplete
    def __init__(
        self,
        config: Incomplete | None = None,
        cache: Incomplete | None = None,
        fetch_token: Incomplete | None = None,
        update_token: Incomplete | None = None,
    ) -> None: ...
